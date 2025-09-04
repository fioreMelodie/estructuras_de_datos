@echo off
REM Ir a la carpeta donde está el .bat
cd /d %~dp0

REM Crear carpeta con el mismo nombre que el .bat
md %~n0
cd %~n0

REM Crear estructura de carpetas
md src
md notebooks

REM Crear un archivo Python en src\mis_funciones.py
echo # Archivo de funciones > src\mis_funciones.py
echo def saludar(nombre): >> src\mis_funciones.py
echo     return f"Hola, {nombre}!" >> src\mis_funciones.py

REM Crear un notebook válido (arrays.ipynb)
echo { > notebooks\arrays.ipynb
echo   "cells": [], >> notebooks\arrays.ipynb
echo   "metadata": {}, >> notebooks\arrays.ipynb
echo   "nbformat": 4, >> notebooks\arrays.ipynb
echo   "nbformat_minor": 5 >> notebooks\arrays.ipynb
echo } >> notebooks\arrays.ipynb

REM Crear entorno virtual
python -m venv .venv

REM Activar entorno
call .venv\Scripts\activate

REM Actualizar pip e instalar jupyter
python -m pip install --upgrade pip
python -m pip install jupyter

REM Abrir en Visual Studio Code (proyecto y notebook)

code . "%cd%\notebooks\arrays.ipynb"
