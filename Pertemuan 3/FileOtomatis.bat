@echo off
setlocal enabledelayedexpansion

set "prefix=praktikum_3."
set "ext=.py"
set "start=1"
set "end=5"

for /l %%N in (%start%,1,%end%) do (
    type nul > "!prefix!%%N!ext!"
)

echo Selesai membuat file dari !prefix!!start!!ext! sampai !prefix!!end!!ext!
pause