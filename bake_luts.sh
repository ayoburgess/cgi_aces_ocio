#!/bin/bash
ociobakelut --iconfig config.ocio --inputspace "Linear (ACES2065-1)" --shaperspace "Log2 48 nits Shaper gamma" --shapersize 4096 --outputspace "Linear (sRGB) to ACES Rec 709 ODT" --cubesize 64 --format houdini --v houdini/linear_sRGB_to_ACES_Rec709_ODT.lut
ociobakelut --iconfig config.ocio --inputspace "Linear (ACES2065-1)" --shaperspace "Log2 48 nits Shaper gamma" --shapersize 4096 --outputspace "Linear (ACEScg) to ACES Rec 709 ODT" --cubesize 64 --format houdini --v houdini/linear_ACEScg_to_ACES_Rec709_ODT.lut
