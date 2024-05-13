#!/usr/bin/env python
# -*- coding: utf-8 -*-   编码声明


import subprocess


def main():

    for i in [40,41]:
        print(i)
        with open('vb2_{}.out'.format(i), 'w') as f:
            subprocess.call(['python', 'raser/field/bjt_circuit22.py', str(i)], stdout=f, stderr=subprocess.STDOUT)
#subprocess.STDOUT 参数用于将标准错误输出合并到标准输出中
