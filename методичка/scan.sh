#!/usr/bin/bash

scanimage -d hpaio:/usb/Deskjet_F2100_series?serial=CN79Q4H5GG04TK --format=png --resolution 300 --mode Color -p --batch-prompt --batch=out%d.png