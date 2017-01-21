# CGI ACES 1.0.3 OCIO Config
An OCIO config for CGI rendering with ACES 1.0.3. Houdini LUTs have been generated from this config and are included for convenience. The 1D LUT resolution is 4096 and the 3D LUT resolution is 65.

# Provided ACES Transforms
* **ACES - ACES2065-1**
* **ACES - ACEScg**
* **ACES - ACESproxy**
* **ACES - ACEScc**
* **ACES - ACEScct**

# Provided Output Transforms
* **Output - ACES sRGB**
* **Output - ACES Rec.709**

# Provided Input Transforms
* **Input - Linear (sRGB)**
* **Input - sRGB**
* **Input - Linear (ProPhoto RGB)**

# Provided Utility Transforms
* **Utility - Raw**
* **Utility - Log2 48 nits Shaper**
* **Utility - Input - Linear (sRGB) -> Output - Rec.709** - utility for creating Houdini LUT, not needed when using OCIO directly
* **Utility - ACES - ACEScg -> Output - Rec.709** - utility for creating Houdini LUT, not needed when using OCIO directly

# Installation (OCIO Compatible Software)
* Set envar **OCIO** = config.ocio

# Installation (Houdini)
* Set envar **HOUDINI_IMAGE_DISPLAY_GAMMA** = 1
* Set envar **HOUDINI_IMAGE_DISPLAY_LUT** = houdini/linear_sRGB_to_ACES_sRGB_output.lut
* Set envar **HOUDINI_IMAGE_DISPLAY_LUT** = houdini/ACEScg_to_ACES_sRGB_output.lut

# References
LUTs used in this configuration are referenced from [hpd/OpenColorIO-Configs](https://github.com/hpd/OpenColorIO-Configs.git).

Color transform matrices used in this configuration are referenced from [RGB Colourspace Models Transformations Matrices](http://colour-science.org/cgi-bin/rgb_colourspace_models_transformation_matrices.cgi).
