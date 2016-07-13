# CGI ACES OCIO Config
An OCIO config for CGI rendering with ACES 1.0. Houdini LUTs have been generated from this config and are included for convenience. The 1D resolution is 4096 and the 3D resolution is 64x64x64.

# Provided Display transforms
* **ACES Rec 709 ODT**

# Installation (OCIO Compatible Software)
* Set envar **OCIO** = config.ocio

# Installation (Houdini)
* Set envar **HOUDINI_IMAGE_DISPLAY_GAMMA** = 1
* Set envar **HOUDINI_IMAGE_DISPLAY_LUT** = houdini/linear_sRGB_to_ACES_Rec709_ODT.lut

# References
LUTs used in this configuration are referenced from [hpd/OpenColorIO-Configs](https://github.com/hpd/OpenColorIO-Configs.git).

Color transform matrices used in this configuration are referenced from [RGB Colourspace Models Transformations Matrices](http://colour-science.org/cgi-bin/rgb_colourspace_models_transformation_matrices.cgi).
