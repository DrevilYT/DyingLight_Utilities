!include("varlist_desaturate.scr")

VarFloat("f_pp_desaturate", 0.0)
VarVec3("v_pp_desaturate_factor_lum", [0.0000, 0.0000, 0.0000] )
VarVec3("v_pp_desaturate_factor_mask", [0.0, 0.0, 0.0] )
VarVec3("v_pp_desaturate_tint", [0.0, 0.0, 0.0] )
VarVec3("v_pp_desaturate_tint_masked", [0.0, 0.0, 0.0] )

VarVec4("v_pp_desaturate_tint__weight", [0.0, 0.0, 0.0, 0.0] )

VarFloat("f_pp_desaturate_lum_mask", 0.0)
VarFloat("f_pp_desaturate_lum_mask_min", 0.0)
VarFloat("f_pp_desaturate_lum_mask_max", 0.0)
