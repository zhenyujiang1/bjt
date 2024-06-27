#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import os
def main():
    for filename in os.listdir('.'):
        if filename.startswith('vb2_') and filename.endswith('.out'):
            new_filename = filename.replace('vb2_', 'ic_vce_')
            with open(filename, 'r') as file:
                lines = file.readlines()
                with open(new_filename, 'w') as new_file:
                    for line in lines:
                        if "CURVE: " in line:
                            new_line = line.replace("CURVE: ", "")
                            new_file.write(new_line)
