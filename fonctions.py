# coding: utf-8

import csv
import random
import os

def csvcount(filename):
    with open(filename, 'r') as f:
        i = 0
        for ligne in f:
            i += 1
    return i


def choisir_facts():
	file_dir = os.path.dirname(os.path.abspath(__file__))
	file = file_dir + '\\fichier.csv'
	fic = open(file,'r')
	tab = fic.readlines()
	lenght = len(tab)
	r = random.randint(1,lenght)
	ligne = tab[r]
	return ligne