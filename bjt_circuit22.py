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
rampvoltage("bjt", "Vb", 2.5, Vb, 0.01, 0.0001, 100, 1e-2, 1e6, bjt_common22.make_bias("base"))
rampvoltage("bjt", "Vc", 2.5, 60, 0.005, 0.0001, 100, 1e-2, 1e6, bjt_common22.make_sweep(("base", "collector", "emitter"), ("Vb", "Vc", "Ve")))
##迭代的细节

#initial:
#rampvoltage("bjt", "Vb", 0.0, Vb, 0.1, 0.001, 40, 1e-2, 1e6, bjt_common22.make_bias("base"))
#rampvoltage("bjt", "Vc", 0.0, 1.5, 0.05, 0.0001, 10, 1e-3, 1e6, bjt_common22.make_sweep(("base", "collector", "emitter"), ("Vb", "Vc", "Ve")))

#def rampvoltage(device, Vsource, begin_bias, end_bias, init_step_size, min_step, max_iter, rel_error, abs_error, callback):
