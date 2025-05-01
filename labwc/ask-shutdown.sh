#!/bin/bash

yad --image dialog-question --title 'Shutdown'  --button=Cancel:1 --button=Yes:0 --text 'Shutdown the system?' && shutdown 0
