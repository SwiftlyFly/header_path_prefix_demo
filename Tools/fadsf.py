#coding=utf-8

from __future__ import unicode_literals
from __future__ import print_function
from subprocess import (check_output as sp_co, CalledProcessError)
from os import path, unlink, rename
import os
from hashlib import md5 as hl_md5
import json
import fileinput
from re import compile as re_compile
from sys import (argv as sys_argv, getfilesystemencoding as sys_get_fs_encoding, version_info)
from collections import deque
from filecmp import cmp as filecmp_cmp
from optparse import OptionParser
import re
from BBAPyPublic import xcode_project_skeleton
import fileinput
import sys
import commands
import subprocess

import BBAPyPublic
from BBAPyPublic import *
import logging

from anytree import Node, RenderTree  #需要安装：pip install anytree




def main():
    # BBAPyPublic.CanonicalProjFormat('/Users/baidu/Desktop/ResourcesMangerTest/ResourcesMangerTest.xcodeproj/project.pbxproj')
    parser = OptionParser()
    parser.add_option("-u", "--update", action="store_true", dest="update", default=False,
                      help="首先根据现有project.pbxproj文件提取project_skeleton.pbxproj文件，然后按照rule重新生成project.pbxproj文件.")
    parser.add_option("-e", "--extract", action="store_true", dest="extract", default=False,
                      help="从工程文件project.pbxproj提取文件project_skeleton.pbxproj，用于版本控制.")
    parser.add_option("-g", "--generate", action="store_true", dest="generate", default=False,
                      help="按照rule以及现有project_skeleton.pbxproj文件生成project.pbxproj文件.")
    (options, args) = parser.parse_args()
    parameter = ''
    true_num = 0
    if options.update == True:
        true_num += 1
        parameter = '-u'
    if options.extract == True:
        true_num += 1
        parameter = '-e'
    if options.generate == True:
        true_num += 1
        parameter = '-g'
    if true_num != 1:
        raise  BBAPyPublic.BBAPyExit("""必须且只能传入以下参数之一：
         "-u":update,首先根据现有project.pbxproj文件提取project_skeleton.pbxproj文件，然后按照rule重新生成project.pbxproj文件.
         "-e":extract,从工程文件project.pbxproj提取文件project_skeleton.pbxproj，用于版本控制.
         "-g":generate,按照rule以及现有project_skeleton.pbxproj文件生成project.pbxproj文件.\n""")
    this_dir = os.getcwd()
    rule_path = os.path.join(os.path.dirname(this_dir), BBAPyPublic.BBAGlobalVariable.rule_file_name)
    cmd = ['python', rule_path, parameter]
    subprocess.call(cmd, 0, None, None, None, None)
if __name__ == '__main__':
    main()



