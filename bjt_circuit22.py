#!/usr/bin/env python
# -*- coding: utf-8 -*-   

import devsim 
devsim.set_parameter(name = "extended_solver", value=True)
devsim.set_parameter(name = "extended_model", value=True)
devsim.set_parameter(name = "extended_equation", value=True)

import sys
Vb=float(sys.argv[1])

from raser.field import bjt_common22
bjt_common22.run()##设置物理参数，求解, load bjt_dd_0.msh

from ramp2 import *
rampvoltage("bjt", "Vb", 0.0, Vb, 0.00001, 0.0000001, 40, 1e-2, 1e6, bjt_common22.make_bias("base"))
rampvoltage("bjt", "Vc", 0.0, 1.5, 0.000005, 0.00000001, 100, 1e-3, 1e6, bjt_common22.make_sweep(("base", "collector", "emitter"), ("Vb", "Vc", "Ve")))
##迭代的细节

#initial:
#rampvoltage("bjt", "Vb", 0.0, Vb, 0.1, 0.001, 40, 1e-2, 1e6, bjt_common.make_bias("base"))
#rampvoltage("bjt", "Vc", 0.0, 1.5, 0.05, 0.0001, 10, 1e-3, 1e6, bjt_common.make_sweep(("base", "collector", "emitter"), ("Vb", "Vc", "Ve")))

#def rampvoltage(device, Vsource, begin_bias, end_bias, init_step_size, min_step, max_iter, rel_error, abs_error, callback):
