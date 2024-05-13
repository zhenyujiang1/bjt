#!/usr/bin/env python
# -*- coding: utf-8 -*-   编码声明          SIC
from devsim import *
device="bjt"
region="bjt"
mesh_name="bjt"

from . import read_gmsh 
from . import netdoping
from . import initial_guess 
from . import bjt_params
from . import setup_dd22       

def main():
    read_gmsh.run("raser/field/bjt.msh", device, region, "Silicon", ("base", "collector", "emitter"))

    netdoping.run(device, region)
    initial_guess.run(device, region)  ##第一次solve

    bjt_params.run(device, region)

    setup_dd22.run(device, region)

    #Get the initial guess from here
    set_node_values(device=device, region=region, name="Electrons", init_from="IntrinsicElectrons")
    set_node_values(device=device, region=region, name="Holes", init_from="IntrinsicHoles")

        
    
    element_from_edge_model(edge_model="EField", device=device, region=region)
    element_model(device=device, region=region, name="Emag", equation="(EField_x^2 + EField_y^2)^(0.5)")
    element_from_edge_model(edge_model="Jn", device=device, region=region)
    element_from_edge_model(edge_model="Jp", device=device, region=region)
    element_model(device=device, region=region, name="Jnmag", equation="(Jn_x^2 + Jn_y^2)^(0.5)")
    element_model(device=device, region=region, name="Jpmag", equation="(Jp_x^2 + Jp_y^2)^(0.5)")


    solve(type="dc", absolute_error=1e4, relative_error=1e10, maximum_iterations=100)
    
    
    write_devices    (file="bjt_dd_0.msh", type="devsim")




    
