#!/usr/bin/env python
# -*- coding: utf-8 -*-   

from devsim import *

device="bjt"
region="bjt"
mesh_name="bjt"


set_parameter(name = "extended_solver", value=True)
set_parameter(name = "extended_model", value=True)
set_parameter(name = "extended_equation", value=True)

import sys
Vb=float(sys.argv[1])

from raser.field import bjt_common22
bjt_common22.run()##设置物理参数，求解, load bjt_dd_0.msh

from ramp2 import *
#rampvoltage("bjt", "Vb", 2.5, Vb, 0.01, 0.0001, 100, 1e-2, 1e6, bjt_common22.make_bias("base"))

#Vb=3V
rampvoltage("bjt", "Vb", 2.5, Vb, 0.025, 0.0001, max_iter=30, rel_error=1e-14, abs_error=1e20, callback=bjt_common22.make_bias("base"))
rampvoltage("bjt", "Vc", 0, 4, 0.025, 0.00001, 100, 1e-4, 1e20, bjt_common22.make_sweep(("base", "collector", "emitter"), ("Vb", "Vc", "Ve")))


#为了得到Ic-Vce的图像，即输出特性曲线，Vb固定
