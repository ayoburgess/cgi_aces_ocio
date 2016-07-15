#!/usr/bin/env python
from __future__ import print_function
import sys
import PyOpenColorIO as OCIO
config = OCIO.Config()
config.setSearchPath(":".join(["luts"]))

# colorspaces
cs = OCIO.ColorSpace(name="Raw")
cs.setDescription("Raw data")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setIsData(True)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Linear (sRGB)", family="sRGB")
cs.setDescription("Scene-linear, high dynamic range, sRGB/Rec.709 primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("sRGB_to_ACES2065-1.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="sRGB gamma", family="sRGB")
cs.setDescription("sRGB gamma")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([0, 1])
cs.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("sRGB_to_linear.spi1d",
                                interpolation=OCIO.Constants.INTERP_LINEAR,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="sRGB", family="sRGB")
cs.setDescription("sRGB colorspace, gamma and primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (ACES2065-1)",
                                      dst="Linear (sRGB)"))
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (ACES2065-1)",
                                      dst="sRGB gamma"))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Linear (ProPhotoRGB)", family="ProPhoto RGB")
cs.setDescription("Scene-linear, high dynamic range, ProPhoto RGB primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ProPhotoRGB_to_ACES2065-1.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Linear (ACES2065-1)", family="ACES")
cs.setDescription("Scene-linear, high dynamic range, ACES2065-1 primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Linear (ACEScg)", family="ACES")
cs.setDescription("Scene-linear, high dynamic range, ACEScg primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ACEScg_to_ACES2065-1.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Linear (ACESproxy)", family="ACES")
cs.setDescription("Scene-linear, high dynamic range, ACESproxy primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ACESproxy_to_ACES2065-1.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="ACESproxy gamma", family="ACES")
cs.setDescription("ACESproxy gamma")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([0, 1])
cs.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ACESproxy_to_linear.spi1d",
                                interpolation=OCIO.Constants.INTERP_LINEAR,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="ACESproxy", family="ACES")
cs.setDescription("ACESproxy colorspace, gamma and primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (ACES2065-1)",
                                      dst="Linear (ACESproxy)"))
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (ACES2065-1)",
                                      dst="ACESproxy gamma"))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Linear (ACEScc)", family="ACES")
cs.setDescription("Scene-linear, high dynamic range, ACEScc primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-8.0, 5.0, 0.00390625])
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ACEScc_to_ACES2065-1.spimtx",
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="ACEScc gamma", family="ACES")
cs.setDescription("ACEScc gamma")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([-0.3584, 1.468])
cs.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("ACEScc_to_linear.spi1d",
                                interpolation=OCIO.Constants.INTERP_LINEAR,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="ACEScc", family="ACES")
cs.setDescription("ACEScc colorspace, gamma and primaries")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (ACES2065-1)",
                                      dst="Linear (ACEScc)"))
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (ACES2065-1)",
                                      dst="ACEScc gamma"))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Log2 48 nits Shaper gamma", family="ACES Shaper")
cs.setDescription("ACES Log2 48 nits Shaper gamma")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
cs.setAllocationVars([0, 1])
cs.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.FileTransform("Log2_48_nits_Shaper_to_linear.spi1d",
                                interpolation=OCIO.Constants.INTERP_LINEAR,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
config.addColorSpace(cs)

# output device transforms
cs = OCIO.ColorSpace(name="ACES Rec 709 ODT", family="ACES ODT")
cs.setDescription("ACES Rec 709 output device transform")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (ACES2065-1)",
                                      dst="Log2 48 nits Shaper gamma"))
gt.push_back(OCIO.FileTransform("Log2_48_nits_Shaper.RRT.a1.0.1.Rec.709.spi3d",
                                interpolation=OCIO.Constants.INTERP_TETRAHEDRAL,
                                direction=OCIO.Constants.TRANSFORM_DIR_FORWARD))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

# utility transforms
cs = OCIO.ColorSpace(name="Linear (sRGB) to ACES Rec 709 ODT", family="Utility")
cs.setDescription("Utility transform for generating a Houdini LUT for ACES Rec "
                  "709 output device transform from Linear (sRGB)")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (sRGB)",
                                      dst="ACES Rec 709 ODT"))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

cs = OCIO.ColorSpace(name="Linear (ACEScg) to ACES Rec 709 ODT", family="Utility")
cs.setDescription("Utility transform for generating a Houdini LUT for ACES Rec "
                  "709 output device transform from Linear (ACEScg)")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
gt = OCIO.GroupTransform()
gt.push_back(OCIO.ColorSpaceTransform(src="Linear (ACEScg)",
                                      dst="ACES Rec 709 ODT"))
cs.setTransform(gt, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE)
config.addColorSpace(cs)

# displays
rec709_display = "Rec 709"
config.addDisplay(rec709_display, "ACES Rec 709 ODT", "ACES Rec 709 ODT")
config.addDisplay(rec709_display, "Raw", "Raw")

config.setActiveDisplays("Rec 709")
config.setActiveViews(",".join(["ACES Rec 709 ODT",
                                "Raw"]))

# set roles
config.setRole(OCIO.Constants.ROLE_SCENE_LINEAR, "Linear (sRGB)")
config.setRole(OCIO.Constants.ROLE_REFERENCE, "Linear (ACES2065-1)")
config.setRole(OCIO.Constants.ROLE_COLOR_TIMING, "ACEScc")
config.setRole(OCIO.Constants.ROLE_COMPOSITING_LOG, "ACEScc")
config.setRole(OCIO.Constants.ROLE_DATA, "Raw")
config.setRole(OCIO.Constants.ROLE_DEFAULT, "Raw")
config.setRole(OCIO.Constants.ROLE_COLOR_PICKING, "Raw")
config.setRole(OCIO.Constants.ROLE_MATTE_PAINT, "Raw")
config.setRole(OCIO.Constants.ROLE_TEXTURE_PAINT, "Raw")
config.setRole("rendering", "Linear (sRGB)")
config.setRole("compositing_linear", "Linear (sRGB)")

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
