#!/bin/bash
ls -d yaw* > cases.txt
split -l 11 --numeric-suffixes=0 --suffix-length=2 cases.txt cases_
