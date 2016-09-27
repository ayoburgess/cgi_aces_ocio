#!/usr/bin/env python
from __future__ import print_function
import sys
import PyOpenColorIO as OCIO
config = OCIO.Config()
config.setSearchPath(":".join(["luts"]))

# ACES transforms
cs = OCIO.ColorSpace(name="ACES - ACES2065-1", family="ACES")
cs.setDescription("Scene-linear, high dynamic range, AP0 primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="ACES - ACEScg", family="ACES")
cs.setDescription("Scene-linear, high dynamic range, AP1 primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("AP1_to_AP0.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="ACES - ACESproxy", family="ACES")
cs.setDescription("ACESproxy colorspace, gamma and primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([0, 1])
cs.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ACESproxy_to_linear.spi1d",
                                interpolation=OCIO.Constants.INTERP_LINEAR,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
gt.push_back(OCIO.FileTransform("AP1_to_AP0.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="ACES - ACEScc", family="ACES")
cs.setDescription("ACEScc colorspace, gamma and primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-0.3584, 1.468])
cs.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ACEScc_to_linear.spi1d",
                                interpolation=OCIO.Constants.INTERP_LINEAR,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
gt.push_back(OCIO.FileTransform("AP1_to_AP0.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

# Input transforms
cs = OCIO.ColorSpace(name="Input - Linear (sRGB)", family="Input")
cs.setDescription("Scene-linear, high dynamic range, sRGB/Rec.709 primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("sRGB_to_AP0.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Input - sRGB", family="Input")
cs.setDescription("sRGB colorspace, gamma and primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([0, 1])
cs.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("sRGB_to_linear.spi1d",
                                interpolation=OCIO.Constants.INTERP_LINEAR,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
gt.push_back(OCIO.FileTransform("sRGB_to_AP0.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Input - Linear (ProPhoto RGB)", family="Input")
cs.setDescription("Scene-linear, high dynamic range, ProPhoto RGB primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ProPhotoRGB_to_AP0.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

# Output transforms
cs = OCIO.ColorSpace(name="Output - Rec.709", family="Output")
cs.setDescription("ACES Rec.709 output transform")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="ACES - ACES2065-1",
                                      dst="Utility - Log2 48 nits Shaper"))
gt.push_back(OCIO.FileTransform("Log2_48_nits_Shaper.RRT.a1.0.1.Rec.709.spi3d",
                                interpolation=OCIO.Constants.INTERP_TETRAHEDRAL,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

# Utility transforms
cs = OCIO.ColorSpace(name="Utility - Raw", family="Utility")
cs.setDescription("Raw data")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setIsData(True)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Utility - Log2 48 nits Shaper", family="Utility")
cs.setDescription("ACES Log2 48 nits Shaper")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([0, 1])
cs.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("Log2_48_nits_Shaper_to_linear.spi1d",
                                interpolation=OCIO.Constants.INTERP_LINEAR,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Utility - Input - Linear (sRGB) -> Output - Rec.709", family="Utility")
cs.setDescription("Utility transform for generating a Houdini LUT for ACES Rec.709 "
                  "output transform from Linear (sRGB)")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="Input - Linear (sRGB)",
                                      dst="Output - Rec.709"))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Utility - ACES - ACEScg -> Output - Rec.709", family="Utility")
cs.setDescription("Utility transform for generating a Houdini LUT for ACES Rec.709 "
                  "output transform from ACEScg")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="ACES - ACEScg",
                                      dst="Output - Rec.709"))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

# displays
rec709_display = "Rec 709"
config.addDisplay(rec709_display, "ACES Rec.709", "Output - Rec.709")
config.addDisplay(rec709_display, "Raw", "Utility - Raw")
config.addDisplay(rec709_display, "Log", "ACES - ACEScc")

config.setActiveDisplays("Rec 709")
config.setActiveViews(",".join(["ACES Rec.709",
                                "Raw",
                                "Log"]))

# set roles
config.setRole(OCIO.Constants.ROLE_SCENE_LINEAR, "ACES - ACEScg")
config.setRole(OCIO.Constants.ROLE_REFERENCE, "ACES - ACES2065-1")
config.setRole(OCIO.Constants.ROLE_COLOR_TIMING, "ACES - ACEScc")
config.setRole(OCIO.Constants.ROLE_COMPOSITING_LOG, "ACES - ACEScc")
config.setRole(OCIO.Constants.ROLE_DATA, "Utility - Raw")
config.setRole(OCIO.Constants.ROLE_DEFAULT, "Utility - Raw")
config.setRole(OCIO.Constants.ROLE_COLOR_PICKING, "Utility - Raw")
config.setRole(OCIO.Constants.ROLE_MATTE_PAINT, "Utility - Raw")
config.setRole(OCIO.Constants.ROLE_TEXTURE_PAINT, "Utility - Raw")
config.setRole("rendering", "ACES - ACEScg")
config.setRole("compositing_linear", "ACES - ACEScg")

# output config
output_filename = "config.ocio"
try:
    config.sanityCheck()
except Exception as e:
    print(e)
    print("Configuration was not written due to a failed sanity check")
    sys.exit()

with open(output_filename, "w") as f:
    f.write(config.serialize())
print("Wrote {0} successfully".format(output_filename))
