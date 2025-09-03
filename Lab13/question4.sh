#!/bin/bash
gawk '{if($1=="ATOM" && $4=="PHE") print$0}' 1HK0.pdb > PHE_atoms.xyz
