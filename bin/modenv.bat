@echo off
set MODINSTALL10v4=C:\Program Files\Modeller10.4
set PYTHONPATH=C:\Program Files\Modeller10.4\modlib;
set LIB_ASGL=C:\Program Files\Modeller10.4\asgl
set BIN_ASGL=C:\Program Files\Modeller10.4\lib\x86_64-w64
set PATH=%MODINSTALL10v4%\lib\x86_64-w64;%PATH%
cd C:\Program Files\Modeller10.4
echo You can find many useful example scripts in the
echo examples\automodel directory.
echo It is recommended that you use Python to run
echo Modeller scripts. However, if you don't have Python installed,
echo you can type 'mod10.4' to run them instead.
