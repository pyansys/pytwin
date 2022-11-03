""".. _ref_example_TBROM_images:

TBROM example for images generation
-----------------------------------

This example shows how PyTwin can be used to load and evaluate a Twin model in order to visualize ROM results in
the form of images with predefined views. The script takes user inputs to evaluate the ROM and will display the
corresponding image. A first image is generated using the point cloud based ROM Viewer embedded in the Ansys Digital
Twin Runtime, and a second image is generated by loading the ROM results and performing the post processing on the
CFD mesh within Fluent.
"""

# sphinx_gallery_thumbnail_path = '_static/TBROM_images_generation.png'

###############################################################################
# Import all necessary modules
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import struct

import matplotlib.pyplot as plt
import matplotlib.image as img
import ansys.fluent.core as pyfluent

from pytwin import TwinModel
from pytwin import examples

twin_file = examples.download_file("ThermalTBROM_23R1_other.twin", "twin_files")
cfd_file = examples.download_file("T_Junction.cas.h5", "other_files")


###############################################################################
# User inputs
# ~~~~~~~~~~~
# Defining user inputs

rom_inputs = {"main_inlet_temperature": 353.15, "side_inlet_temperature": 293.15}
rom_parameters = {"ThermalROM23R1_1_colorbar_min": 290, "ThermalROM23R1_1_colorbar_max": 360, "ThermalROM23R1_1_store_snapshots": 1}

###############################################################################
# Auxiliary functions definition
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Conversion of ROM snapshot for data mapping on CFD mesh.

def snapshot_to_cfd(snapshot_file, geometry_file, field_name, outputFilePath):
    """Create a Fluent Interpolation file that can be loaded in Fluent and map to the CFD mesh
    """

    with open(geometry_file, 'rb') as geo, open(snapshot_file, "rb") as snp:
        nb = struct.unpack('Q', snp.read(8))[0]
        struct.unpack('Q', geo.read(8))[0]
        res_list = []
        for i in range(nb):
            res_line = []
            res_line.append(struct.unpack('d', geo.read(8))[0])
            res_line.append(struct.unpack('d', geo.read(8))[0])
            res_line.append(struct.unpack('d', geo.read(8))[0])
            res_line.append(struct.unpack('d', snp.read(8))[0])
            res_list.append(res_line)

    with open(outputFilePath, 'w') as ipfile:
        ipfile.write("3\n") # IP file format
        ipfile.write("3\n") # 2D or 3D - 3D for now
        ipfile.write(str(len(res_list))+"\n") # number of data
        #ipfile.write(str(len(field_name))+"\n") # number of field data
        #for i in range(0,len(field_name)):
        #    ipfile.write(field_name[i]+"\n") # individual field data name
        ipfile.write("1\n")  # number of field data
        ipfile.write(field_name+"\n")  # number of field data
        for j in range(0, len(res_list[0])):
            ipfile.write("(")
            for i in range(0, len(res_list)):
                ipfile.write(str(res_list[i][j])+"\n")
            ipfile.write(")\n")

    return outputFilePath

###############################################################################
# Loading the Twin Runtime and generate the temperature results from the TBROM
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('Loading model: {}'.format(twin_file))
twin_model = TwinModel(twin_file)

# TODO - following are SDK atomic calls, need to use TBROM class ultimately
twin_model._twin_runtime.twin_instantiate()

directory_path = os.path.join(twin_model.model_dir, 'ROM_files')
visualization_info = twin_model._twin_runtime.twin_get_visualization_resources()
rom_name = ""
for model_name, data in visualization_info.items():
    twin_model._twin_runtime.twin_set_rom_image_directory(model_name, directory_path)
    rom_name = model_name

twin_model._initialize_evaluation(inputs=rom_inputs, parameters=rom_parameters)

snapshot = os.path.join(directory_path, rom_name, 'snapshot_0.000000.bin')
geometry = os.path.join(twin_model._twin_runtime.twin_get_rom_resource_directory(rom_name),
                        'binaryOutputField', 'points.bin')

temperature_file = snapshot_to_cfd(snapshot, geometry, "temperature",
                                   os.path.join(directory_path, rom_name, "cfd_file.ip"))

###############################################################################
# Post-processing with image generated by point cloud based ROM Viewer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

image = img.imread(os.path.join(directory_path, rom_name, 'View1_0.000000.png'))
plt.imshow(image)
plt.show()

###############################################################################
# Post-processing with image generated by Fluent
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

solver = pyfluent.launch_fluent(precision="double", processor_count=2, mode="solver")
solver.file.read(file_type="case", file_name=cfd_file)
tui = solver.tui
tui.file.interpolate.read_data(temperature_file)
tui.display.objects.display("contour-1")
tui.display.save_picture(os.path.join(directory_path, rom_name,"View1_Fluent_0.000000.png"))
solver.exit()

image = img.imread(os.path.join(directory_path, rom_name, "View1_Fluent_0.000000.png"))
plt.imshow(image)
plt.show()
