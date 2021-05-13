# KivyShaderTransitions
Contains a variety of shader screen transitions to choose from

[![Build Status](https://travis-ci.org/shashi278/KivyShaderTransitions.svg?branch=main)](https://travis-ci.org/shashi278/KivyShaderTransitions) ![pypi version](https://img.shields.io/pypi/v/kivytransitions) ![code size](https://img.shields.io/github/languages/code-size/shashi278/KivyShaderTransitions) ![repo size](https://img.shields.io/github/repo-size/shashi278/KivyShaderTransitions)

<!--![demo](https://raw.githubusercontent.com/shashi278/KivyShaderTransitions/main/demo/demo.gif)-->

####

### How to use
Install:
```bash
pip install kivytransitions
```
Import:
```python
from kivytransitions.transitions import Cube
```
Use:
```python
# ....
screenmanager.transition = Cube(duration=2, direction="lr") #two available directions: "lr" and "rl"
# ....
```
*GLSL transitions taken from: https://gl-transitions.com/*

## Available Transitions

### Angular:
![Angular](https://raw.githubusercontent.com/shashi278/KivyShaderTransitions/main/gifs/Angular.gif)

### Bounce:
![Bounce](https://raw.githubusercontent.com/shashi278/KivyShaderTransitions/main/gifs/Bounce.gif)
