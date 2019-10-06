import os
import PyOpenColorIO as OCIO


__version__ = "0.7.0"


def build_config(output_path):
    """Generate OCIO config"""
    config = OCIO.Config()
    config.setSearchPath(":".join(["luts", "mtx"]))

    # add colorspaces
    config.addColorSpace(aces_colorspace())
    config.addColorSpace(acescg_colorspace())
    config.addColorSpace(acesproxy_colorspace())
    config.addColorSpace(acescc_colorspace())
    config.addColorSpace(acescct_colorspace())
    config.addColorSpace(log248nitsshaper_colorspace())
    config.addColorSpace(aces_out_rec709_colorspace())
    config.addColorSpace(lin_srgb_colorspace())
    config.addColorSpace(srgb_colorspace())
    config.addColorSpace(ncd_colorspace())

    # add looks
    config.addLook(shot_look())
    config.addLook(neutral_look())

    # add displays
    rec709_display_spaces = [
        ["ACES Rec. 709", "aces_out_rec709", ""],
        ["Shot", "acesproxy", "+shot"],
        ["No LUT", "ncd", ""],
    ]
    for name, colorspace, look in rec709_display_spaces:
        config.addDisplay("rec709", name, colorspace, look)

    config.setActiveViews(",".join(["ACES Rec. 709", "Shot", "No LUT"]))
    config.setActiveDisplays(",".join(["rec709"]))

    # set roles
    config.setRole(OCIO.Constants.ROLE_SCENE_LINEAR, "acescg")
    config.setRole(OCIO.Constants.ROLE_REFERENCE, "aces")
    config.setRole(OCIO.Constants.ROLE_DATA, "ncd")
    config.setRole(OCIO.Constants.ROLE_DEFAULT, "ncd")
    config.setRole(OCIO.Constants.ROLE_COLOR_PICKING, "srgb")
    config.setRole(OCIO.Constants.ROLE_TEXTURE_PAINT, "acescg")
    config.setRole(OCIO.Constants.ROLE_MATTE_PAINT, "acesproxy")
    config.setRole(OCIO.Constants.ROLE_COLOR_TIMING, "acescct")
    config.setRole(OCIO.Constants.ROLE_COMPOSITING_LOG, "acescc")
    config.setRole("rendering", "acescg")

    config.sanityCheck()

    with open(output_path, "w") as fhandle:
        fhandle.write(config.serialize())
    print("Wrote {} successfully".format(output_path))


def aces_colorspace():
    """The Academy Color Encoding System reference color space (ACES 2065-1)"""
    col_space = OCIO.ColorSpace(name="aces", family="ACES")
    col_space.setDescription(
        "The Academy Color Encoding System reference color space (ACES 2065-1)"
    )
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([-8.0, 5.0, 0.00390625])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_LG2)
    return col_space


def acescg_colorspace():
    """The Academy Color Encoding System ACEScg color space"""
    col_space = OCIO.ColorSpace(name="acescg", family="ACES")
    col_space.setDescription("The Academy Color Encoding System ACEScg color space")
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([-8.0, 5.0, 0.00390625])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_LG2)
    ftransform = OCIO.FileTransform(
        "ap1_to_ap0.spimtx", direction=OCIO.Constants.TRANSFORM_DIR_FORWARD
    )
    col_space.setTransform(ftransform, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
    return col_space


def acesproxy_colorspace():
    """The Academy Color Encoding System ACESproxy color space"""
    col_space = OCIO.ColorSpace(name="acesproxy", family="ACES")
    col_space.setDescription("The Academy Color Encoding System ACESproxy color space")
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([0, 1])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
    group_xform = OCIO.GroupTransform()
    group_xform.push_back(
        OCIO.FileTransform(
            "ACESproxy_to_linear.spi1d",
            interpolation=OCIO.Constants.INTERP_LINEAR,
            direction=OCIO.Constants.TRANSFORM_DIR_FORWARD,
        )
    )
    group_xform.push_back(
        OCIO.FileTransform(
            "ap1_to_ap0.spimtx", direction=OCIO.Constants.TRANSFORM_DIR_FORWARD
        )
    )
    col_space.setTransform(group_xform, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
    return col_space


def acescc_colorspace():
    """The Academy Color Encoding System ACEScc color space"""
    col_space = OCIO.ColorSpace(name="acescc", family="ACES")
    col_space.setDescription("The Academy Color Encoding System ACEScc color space")
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([-0.3584, 1.468])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
    group_xform = OCIO.GroupTransform()
    group_xform.push_back(
        OCIO.FileTransform(
            "ACEScc_to_linear.spi1d",
            interpolation=OCIO.Constants.INTERP_LINEAR,
            direction=OCIO.Constants.TRANSFORM_DIR_FORWARD,
        )
    )
    group_xform.push_back(
        OCIO.FileTransform(
            "ap1_to_ap0.spimtx", direction=OCIO.Constants.TRANSFORM_DIR_FORWARD
        )
    )
    col_space.setTransform(group_xform, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
    return col_space


def acescct_colorspace():
    """The Academy Color Encoding System ACEScct color space"""
    col_space = OCIO.ColorSpace(name="acescct", family="ACES")
    col_space.setDescription("The Academy Color Encoding System ACEScct color space")
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([-0.249136, 1.468])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
    group_xform = OCIO.GroupTransform()
    group_xform.push_back(
        OCIO.FileTransform(
            "ACEScct_to_linear.spi1d",
            interpolation=OCIO.Constants.INTERP_LINEAR,
            direction=OCIO.Constants.TRANSFORM_DIR_FORWARD,
        )
    )
    group_xform.push_back(
        OCIO.FileTransform(
            "ap1_to_ap0.spimtx", direction=OCIO.Constants.TRANSFORM_DIR_FORWARD
        )
    )
    col_space.setTransform(group_xform, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
    return col_space


def log248nitsshaper_colorspace():
    """The Academy Color Encoding System Log2 48 nits Shaper color space"""
    col_space = OCIO.ColorSpace(name="log248nitsshaper", family="ACES")
    col_space.setDescription(
        "The Academy Color Encoding System Log2 48 nits Shaper color space"
    )
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([0, 1])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
    ftransform = OCIO.FileTransform(
        "Log2_48_nits_Shaper_to_linear.spi1d",
        interpolation=OCIO.Constants.INTERP_LINEAR,
        direction=OCIO.Constants.TRANSFORM_DIR_FORWARD,
    )
    col_space.setTransform(ftransform, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
    return col_space


def aces_out_rec709_colorspace():
    """The Academy Color Encoding System ACES 1.0 Rec. 709 Output Transform color space"""
    col_space = OCIO.ColorSpace(name="aces_out_rec709", family="ACES")
    col_space.setDescription(
        "The Academy Color Encoding System ACES 1.0 Rec. 709 Output Transform color space"
    )
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([0, 1])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
    group_xform_from = OCIO.GroupTransform()
    group_xform_from.push_back(
        OCIO.ColorSpaceTransform(src="aces", dst="log248nitsshaper")
    )
    group_xform_from.push_back(
        OCIO.FileTransform(
            "Log2_48_nits_Shaper.RRT.Rec.709.spi3d",
            interpolation=OCIO.Constants.INTERP_TETRAHEDRAL,
        )
    )
    col_space.setTransform(
        group_xform_from, OCIO.Constants.COLORSPACE_DIR_FROM_REFERENCE
    )

    group_xform_to = OCIO.GroupTransform()
    group_xform_to.push_back(
        OCIO.FileTransform(
            "InvRRT.Rec.709.Log2_48_nits_Shaper.spi3d",
            interpolation=OCIO.Constants.INTERP_TETRAHEDRAL,
        )
    )
    group_xform_to.push_back(
        OCIO.ColorSpaceTransform(src="log248nitsshaper", dst="aces")
    )
    col_space.setTransform(group_xform_to, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
    return col_space


def shot_look():
    """
    Custom shot look transform controlled by $SHOT environment variable.
    Process space is ACESproxy
    """
    look = OCIO.Look(name="shot", processSpace="acesproxy")
    look.setDescription(
        "Custom shot look transform controlled by $SHOT "
        "environment variable. Process space is ACESproxy"
    )
    ftransform = OCIO.FileTransform(
        "$SHOT.cube", interpolation=OCIO.Constants.INTERP_TETRAHEDRAL
    )
    look.setTransform(ftransform)
    return look


def neutral_look():
    """
    Custom shot neutralization transform controlled by $SHOT environment variable.
    Process space is ACEScg"""
    look = OCIO.Look(name="neutral_cc", processSpace="acescg")
    look.setDescription(
        "Custom shot neutralization transform controlled by $SHOT "
        "environment variable. Process space is ACEScg"
    )
    ftransform = OCIO.FileTransform("${SHOT}_neutral.cc")
    look.setTransform(ftransform)
    return look


def lin_srgb_colorspace():
    """Scene-linear sRGB color space"""
    col_space = OCIO.ColorSpace(name="lin_srgb", family="sRGB")
    col_space.setDescription("Scene-linear sRGB color space")
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([-8.0, 5.0, 0.00390625])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_LG2)
    ftransform = OCIO.FileTransform(
        "srgb_to_ap0.bradford.spimtx", direction=OCIO.Constants.TRANSFORM_DIR_FORWARD
    )
    col_space.setTransform(ftransform, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
    return col_space


def srgb_colorspace():
    """sRGB color space"""
    col_space = OCIO.ColorSpace(name="srgb", family="sRGB")
    col_space.setDescription("sRGB color space")
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setAllocationVars([0, 1])
    col_space.setAllocation(OCIO.Constants.ALLOCATION_UNIFORM)
    group_xform = OCIO.GroupTransform()
    group_xform.push_back(
        OCIO.FileTransform(
            "sRGB_to_linear.spi1d",
            interpolation=OCIO.Constants.INTERP_LINEAR,
            direction=OCIO.Constants.TRANSFORM_DIR_FORWARD,
        )
    )
    group_xform.push_back(
        OCIO.FileTransform(
            "srgb_to_ap0.bradford.spimtx",
            direction=OCIO.Constants.TRANSFORM_DIR_FORWARD,
        )
    )
    col_space.setTransform(group_xform, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)
    return col_space


def ncd_colorspace():
    """Non-color data"""
    col_space = OCIO.ColorSpace(name="ncd", family="Data")
    col_space.setDescription("Non-color data")
    col_space.setBitDepth(OCIO.Constants.BIT_DEPTH_F32)
    col_space.setIsData(True)
    return col_space


def main():
    """Main function"""
    this_dir = os.path.abspath(os.path.dirname(__file__))
    output_path = os.path.join(this_dir, "config.ocio")
    build_config(output_path)


if __name__ == "__main__":
    main()
