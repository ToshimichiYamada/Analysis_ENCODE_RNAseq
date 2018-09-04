#!/usr/bin/env python2

# Code to convert ensembl_geneID to gene symbol


import mygene
import pandas

mg = mygene.MyGeneInfo()

with open("ensembl_geneID.txt") as f: #ensembl_geneID from text file
    ens = [s.strip() for s in f.readlines()] # read in single line

ginfo = mg.querymany(ens, scopes='ensembl.gene', as_dataframe = 'True')

ginfo.to_csv('symbol.csv')
