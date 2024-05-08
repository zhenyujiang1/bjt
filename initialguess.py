#!/usr/bin/env python
# -*- coding: utf-8 -*-   编码声明

##从只有电势的模拟中创建初始猜测

from devsim import *
from . import model_create
from . import new_physics


def run(device, region):

    # this is our solution variable
    model_create.CreateSolution(device, region, "Potential")##在每个节点和边上创建了一个名为 "Potential" 的变量，用于存储电势场的解。
    # start with temperature as a model and not a parameter
    set_parameter(device=device, name="T", value="300")

    new_physics.CreateSiliconPotentialOnly(device, region)
    for i in get_contact_list(device=device):
        set_parameter(device=device, name=new_physics.GetContactBiasName(i), value=0.0)
        new_physics.CreateSiliconPotentialOnlyContact(device, region, i)

    ####
    #### Initial DC solution
    ####
    solve(type="dc", absolute_error=1, relative_error=1e-9, maximum_iterations=40)

