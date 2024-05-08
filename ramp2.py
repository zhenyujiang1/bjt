#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
from devsim import *
from raser.field import new_physics

### modify to grow and shrink size
def rampvoltage(device, Vsource, begin_bias, end_bias, init_step_size, min_step, max_iter, rel_error, abs_error, callback):
    '''
      Ramps bias with assignable callback function
    '''
    start_bias=begin_bias

    if (start_bias < end_bias):
        step_sign=1
    else:
        step_sign=-1

    num_successes = 0
    last_bias=start_bias
    step_size=init_step_size
    while(abs(last_bias - end_bias) > min_step):
        print(("last end %e %e") % (last_bias, end_bias))
        next_bias=last_bias + step_sign * step_size
        if next_bias < end_bias:
            next_step_sign=1
        else:
            next_step_sign=-1

        if next_step_sign != step_sign:
            next_bias=end_bias
            print("setting to last bias %e" % (end_bias))
            print("setting next bias %e" % (next_bias))

        circuit_alter(name=Vsource, value=next_bias)
        try:
            solve(type="dc", absolute_error=abs_error, relative_error=rel_error, maximum_iterations=max_iter)
        except error as msg:
            if str(msg).find("Convergence failure") != 0:
                raise
            circuit_alter(name=Vsource, value=last_bias)
            step_size *= 0.5
            print("setting new step size %e" % (step_size))
            if step_size < min_step:
                raise RuntimeError("Min step size too small")
            num_successes = 0
            continue
        num_successes += 1
        if (num_successes > 5) and (step_size < init_step_size):
            step_size *= 2
            if step_size > init_step_size:
                step_size = init_step_size
            print("setting new step size %e" % (step_size))
            num_successes = 0
        print("Succeeded")
        last_bias=next_bias
        callback()

def rampbias(device, contact, end_bias, step_size, min_step, max_iter, rel_error, abs_error, callback):
    '''
      Ramps bias with assignable callback function
    '''
    start_bias= get_parameter(device=device, name=new_physics.GetContactBiasName(contact))
    if (start_bias < end_bias):
        step_sign=1
    else:
        step_sign=-1
    last_bias=start_bias
    while(abs(last_bias - end_bias) > min_step):
        print(("last end %e %e") % (last_bias, end_bias))
        next_bias=last_bias + step_sign * step_size
        if next_bias < end_bias:
            next_step_sign=1
        else:
            next_step_sign=-1

        if next_step_sign != step_sign:
            next_bias=end_bias
            print("setting to last bias %e" % (end_bias))
            print("setting next bias %e" % (next_bias))
        set_parameter(device=device, name=new_physics.GetContactBiasName(contact), value=next_bias)
        try:
            solve(type="dc", absolute_error=abs_error, relative_error=rel_error, maximum_iterations=max_iter)
        except error as msg:
            if str(msg).find("Convergence failure") != 0:
                raise
            set_parameter(device=device, name=new_physics.GetContactBiasName(contact), value=last_bias)
            step_size *= 0.5
            print("setting new step size %e" % (step_size))
            if step_size < min_step:
                raise RuntimeError("Min step size too small")
            continue
        print("Succeeded")
        last_bias=next_bias
        callback()

def rampbias(device, contact, end_bias, step_size, min_step, max_iter, rel_error, abs_error, callback):
    '''
      Ramps bias with assignable callback function
    '''
    start_bias= get_parameter(device=device, name=new_physics.GetContactBiasName(contact))
    if (start_bias < end_bias):
        step_sign=1
    else:
        step_sign=-1
    last_bias=start_bias
    while(abs(last_bias - end_bias) > min_step):
        print(("last end %e %e") % (last_bias, end_bias))
        next_bias=last_bias + step_sign * step_size
        if next_bias < end_bias:
            next_step_sign=1
        else:
            next_step_sign=-1

        if next_step_sign != step_sign:
            next_bias=end_bias
            print("setting to last bias %e" % (end_bias))
            print("setting next bias %e" % (next_bias))
        set_parameter(device=device, name=new_physics.GetContactBiasName(contact), value=next_bias)
        try:
            solve(type="dc", absolute_error=abs_error, relative_error=rel_error, maximum_iterations=max_iter)
        except error as msg:
            if str(msg).find("Convergence failure") != 0:
                raise
            set_parameter(device=device, name=new_physics.GetContactBiasName(contact), value=last_bias)
            step_size *= 0.5
            print("setting new step size %e" % (step_size))
            if step_size < min_step:
                raise RuntimeError("Min step size too small")
            continue
        print("Succeeded")
        last_bias=next_bias
        callback(device)

def printAllCurrents(device, bias):
    '''
      Prints all contact currents on device
    '''
    for c in get_contact_list(device=device):
        x = get_DCcurrent(device, c)

def PrintCurrents(device, contact):
    '''
       print out contact currents
    '''
    contact_bias_name = new_physics.GetContactBiasName(contact)
    electron_current= get_contact_current(device=device, contact=contact, equation=ece_name)
    hole_current    = get_contact_current(device=device, contact=contact, equation=hce_name)
    total_current   = electron_current + hole_current                                        
    voltage         = get_parameter(device=device, name=new_physics.GetContactBiasName(contact))
    print("{0}\t{1}\t{2}\t{3}\t{4}".format(contact, voltage, electron_current, hole_current, total_current))

