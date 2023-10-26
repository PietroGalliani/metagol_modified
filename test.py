# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:27:26 2023

@author: pgalliani
"""

from pyswip import Prolog


prolog = Prolog()

prolog.consult("metagol.pl")
prolog.consult("metarules.pl")

prolog.consult("examples/grandparent2.pl")


