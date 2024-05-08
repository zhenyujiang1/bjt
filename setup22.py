#!/usr/bin/env python
# -*- coding: utf-8 -*-   SIC

from devsim import *
from . import new_physics22
from . import model_create


def run(device, region):

    # this is our solution variable
    
    model_create.CreateSolution(device, region, "Electrons")
    model_create.CreateSolution(device, region, "Holes")

    #these are needed for velocity saturation
    
    new_physics22.CreateEField(device, region)
    new_physics22.CreateDField(device, region)



    new_physics22.CreateElectronCurrent(device, region, mu_n = '1100', Potential="Potential", sign=-1, ElectronCurrent="Jn", V_t="V_t_edge")
    new_physics22.CreateHoleCurrent(device, region, mu_p = '114', Potential="Potential", sign=-1, HoleCurrent="Jp", V_t="V_t_edge")
    
    
    new_physics22.CreateSiliconDriftDiffusion(device, region,  mu_n="mu_n", mu_p="mu_p", Jn='Jn', Jp='Jp')#################运行到这NC,NV等等等等
    for i in get_contact_list(device=device):
        set_parameter(device=device, name=new_physics22.GetContactBiasName(i), value=0.0)
        new_physics22.CreateSiliconDriftDiffusionContact(device, region, i, Jn='Jn', Jp='Jp')



