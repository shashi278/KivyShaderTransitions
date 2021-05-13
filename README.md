# KivyShaderTransitions
Contains a variety of shader screen transitions to choose from

[![Build Status](https://travis-ci.org/shashi278/KivyShaderTransitions.svg?branch=main)](https://travis-ci.org/shashi278/KivyShaderTransitions) ![pypi version](https://img.shields.io/pypi/v/kivytransitions) ![code size](https://img.shields.io/github/languages/code-size/shashi278/KivyShaderTransitions) ![repo size](https://img.shields.io/github/repo-size/shashi278/KivyShaderTransitions)

![demo](https://raw.githubusercontent.com/shashi278/KivyShaderTransitions/main/demo/demo.gif)

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
|          |             |    |    |
| :-------------: |:-------------:|:-----:|:-----:|
| [**Angular**](https://gl-transitions.com/transition/angular) | [**Bounce**](https://gl-transitions.com/transition/Bounce) | [**BowTieHorizontal**](https://gl-transitions.com/transition/BowTieHorizontal) | [**BowTieVertical**](https://gl-transitions.com/transition/BowTieVertical) |
| [**Burn**](https://gl-transitions.com/transition/burn) | [**ButterflyWaveScrawler**](https://gl-transitions.com/transition/ButterflyWaveScrawler) | [**CannabisLeaf**](https://gl-transitions.com/transition/cannabisleaf) | [**Circle**](https://gl-transitions.com/transition/circle) |
| [**CircleOpen**](https://gl-transitions.com/transition/circleopen) | [**ColorPhase**](https://gl-transitions.com/transition/colorphase) | [**ColourDistance**](https://gl-transitions.com/transition/ColourDistance) | [**CrazyParametricFun**](https://gl-transitions.com/transition/CrazyParametricFun) |
| [**CrossHatch**](https://gl-transitions.com/transition/crosshatch) | [**CrossWarp**](https://gl-transitions.com/transition/crosswarp) | [**CrossZoom**](https://gl-transitions.com/transition/CrossZoom) | [**Cube**](https://gl-transitions.com/transition/cube) |
| [**DirectionalEasing**](https://gl-transitions.com/transition/DirectionalEasing) | [**DirectionalWarp**](https://gl-transitions.com/transition/directionalwarp) | [**DirectionalWipe**](https://gl-transitions.com/transition/directionalwipe) | [**Displacement**](https://gl-transitions.com/transition/displacement) |
| [**DoomScreenTransition**](https://gl-transitions.com/transition/DoomScreenTransition) | [**Doorway**](https://gl-transitions.com/transition/doorway) | [**Dreamy**](https://gl-transitions.com/transition/Dreamy) | [**DreamyZoom**](https://gl-transitions.com/transition/DreamyZoom) |
| [**Fade**](https://gl-transitions.com/transition/fade) | [**FadeColor**](https://gl-transitions.com/transition/fadecolor) | [**FadeGrayscale**](https://gl-transitions.com/transition/fadegrayscale) | [**FilmBurn**](https://gl-transitions.com/transition/FilmBurn) |
| [**FlyEye**](https://gl-transitions.com/transition/flyeye) | [**GlitchDisplace**](https://gl-transitions.com/transition/GlitchDisplace) | [**GlitchMemories**](https://gl-transitions.com/transition/GlitchMemories) | [**GridFlip**](https://gl-transitions.com/transition/GridFlip) |
| [**Heart**](https://gl-transitions.com/transition/heart) | [**Hexagonalize**](https://gl-transitions.com/transition/hexagonalize) | [**Kaleidoscope**](https://gl-transitions.com/transition/kaleidoscope) | [**LeftRight**](https://gl-transitions.com/transition/LeftRight) |
| [**LinearBlur**](https://gl-transitions.com/transition/LinearBlur) | [**Luma**](https://gl-transitions.com/transition/luma) | [**LuminanceMelt**](https://gl-transitions.com/transition/luminance_melt) | [**Morph**](https://gl-transitions.com/transition/morph) |
| [**Mosaic**](https://gl-transitions.com/transition/Mosaic) | [**MultiplyBlend**](https://gl-transitions.com/transition/multiply_blend) | [**PageCurl**](https://gl-transitions.com/transition/PageCurl) | [**Perlin**](https://gl-transitions.com/transition/perlin) |
| [**Pinwheel**](https://gl-transitions.com/transition/pinwheel) | [**Pixelize**](https://gl-transitions.com/transition/pixelize) | [**PolarFunction**](https://gl-transitions.com/transition/polar_function) | [**PolkaDotsCurtain**](https://gl-transitions.com/transition/PolkaDotsCurtain) |
| [**Radial**](https://gl-transitions.com/transition/Radial) | [**RandomNoise**](https://gl-transitions.com/transition/RandomNoise) | [**RandomSquares**](https://gl-transitions.com/transition/randomsquares) | [**Ripple**](https://gl-transitions.com/transition/ripple) |
| [**RotateScaleFade**](https://gl-transitions.com/transition/rotate_scale_fade) | [**RotateTransition**](https://gl-transitions.com/transition/RotateTransition) | [**SimpleZoom**](https://gl-transitions.com/transition/SimpleZoom) | [**SquaresWire**](https://gl-transitions.com/transition/squareswire) |
| [**Squeeze**](https://gl-transitions.com/transition/squeeze) | [**StereoViewer**](https://gl-transitions.com/transition/StereoViewer) | [**Swap**](https://gl-transitions.com/transition/swap) | [**Swirl**](https://gl-transitions.com/transition/Swirl) |
| [**TangentMotionBlur**](https://gl-transitions.com/transition/TangentMotionBlur) | [**TopBottom**](https://gl-transitions.com/transition/TopBottom) | [**UndulatingBurnOut**](https://gl-transitions.com/transition/undulatingBurnOut) | [**WaterDrop**](https://gl-transitions.com/transition/WaterDrop) |
| [**Wind**](https://gl-transitions.com/transition/wind) | [**WindowBlinds**](https://gl-transitions.com/transition/windowblinds) | [**WindowSlice**](https://gl-transitions.com/transition/windowslice) | [**WipeDown**](https://gl-transitions.com/transition/wipeDown) |
| [**WipeLeft**](https://gl-transitions.com/transition/wipeLeft) | [**WipeRight**](https://gl-transitions.com/transition/wipeRight) | [**WipeUp**](https://gl-transitions.com/transition/wipeUp) | [**ZoomInCircles**](https://gl-transitions.com/transition/ZoomInCircles) |
