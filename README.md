
### CGI ACES 1.0.3 OCIO Config
OCIO configs for CGI rendering with ACES 1.0.3.

### ACES Transforms
* aces - The Academy Color Encoding System reference color space (ACES 2065-1)
* acescg - The Academy Color Encoding System ACEScg color space
* acesproxy - The Academy Color Encoding System ACESproxy color space
* acescc - The Academy Color Encoding System ACEScc color space
* acescct - The Academy Color Encoding System ACEScct color space

### Display Transforms
* ACES Rec. 709 - The Academy Color Encoding System ACES 1.0 Rec. 709 Output Transform color space
* No LUT - View image with no display transform applied

### Look Transforms
* Shot - Custom shot look transform controlled by $SHOT environment variable

### Input Transforms
* lin_srgb - Scene-linear sRGB color space
* srgb - sRGB color space

### Utility Transforms
* ncd - Non-color data

### References
LUTs used in this configuration were referenced from [hpd/OpenColorIO-Configs](https://github.com/hpd/OpenColorIO-Configs.git).

Color transformation matrices used in this configuration were referenced from [RGB COLOURSPACE MODELS TRANSFORMATION MATRIX](https://www.colour-science.org:8010/apps/rgb_colourspace_models_transformation_matrix)