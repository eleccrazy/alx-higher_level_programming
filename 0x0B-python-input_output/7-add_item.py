#!/usr/bin/python3

"""
File: 7-add_item.py
Desc: This module deals with loading, adding, and savig.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""
from sys import argv as av
from os.path import exists
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

name = "add_item.json"

av.remove(av[0])
pre_loaded = []

if exists('add_item.json'):
    pre_loaded = load(name)

pre_loaded += av

save(pre_loaded, name)
