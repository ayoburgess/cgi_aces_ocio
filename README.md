# CGI ACES 1.0.3 OCIO Config
OCIO configs for CGI rendering with ACES 1.0.3

# ACES Transforms
* ACES - ACES2065-1
* ACES - ACEScg
* ACES - ACESproxy
* ACES - ACEScc
* ACES - ACEScct

# Output Transforms
* Output - ACES sRGB
* Output - ACES Rec.709

# Input Transforms
* Input - Linear (sRGB)
* Input - sRGB
* Input - Linear (ProPhoto RGB)

# Utility Transforms
* Utility - Raw
* Utility - Log2 48 nits Shaper

# OCIO Config Files
* **config_scene_linear_acescg.ocio** - "scene_linear" and "rendering" roles set to "ACES - ACEScg"
* **config_scene_linear_lin_srgb.ocio** - "scene_linear" and "rendering" roles set to "Input - Linear (sRGB)"

# References
LUTs used in this configuration are referenced from [hpd/OpenColorIO-Configs](https://github.com/hpd/OpenColorIO-Configs.git).

Color transform matrices used in this configuration are referenced from [RGB Colourspace Models Transformations Matrices](http://colour-science.org/cgi-bin/rgb_colourspace_models_transformation_matrices.cgi).
