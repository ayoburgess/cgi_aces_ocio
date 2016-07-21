#!/bin/bash
ociobakelut --iconfig config.ocio --inputspace "ACES - ACES2065-1" --shaperspace "Utility - Log2 48 nits Shaper" --shapersize 4096 --outputspace "Utility - Input - Linear (sRGB) -> Output - Rec.709" --cubesize 64 --format houdini --v houdini/linear_sRGB_to_ACES_Rec709_output.lut
ociobakelut --iconfig config.ocio --inputspace "ACES - ACES2065-1" --shaperspace "Utility - Log2 48 nits Shaper" --shapersize 4096 --outputspace "Utility - ACES - ACEScg -> Output - Rec.709" --cubesize 64 --format houdini --v houdini/ACEScg_to_ACES_Rec709_output.lut
