#!/bin/bash
# Script for converting DOS text file format to UNIX
# Simplifies use of shared folders on a Debian VM
# Replace /media/sf_grid/* with /your/src/*

cp -r /media/sf_grid/* . &&
find . -type f -print0 | xargs -0 -n 1 -P 4 dos2unix &&
chmod 0755 *.cgi && chmod 0755 lib/Grid/*.pm
#cp -r Grid /home/stevie/perl5/lib/perl5/
