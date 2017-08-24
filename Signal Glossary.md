# Signal Glossary

## Signal Glossary

### Introduction

Inputs and Outputs in this module library are labelled in a consistent way so as to make interfacing them easy to understand. The chart below defines all of the standard Audulus input and output signal ranges that you will find in the Module Library.

Interfacing these signals is easy. Hz outputs go to Hz inputs. Gate outputs to gate inputs. Modulation outputs to modulation inputs, and so on.

Audulus does not distinguish between audio and control signals. However, there are conventions for the ranges of each signal type.

In the Module Library under `Utilities -> Translation` you will find all sorts of mini-modules that translate one signal type into another.

There are 4 general types of signals used in the Module Library:

Signal | Range 
:------------- | :------------- 
Audio  | `-1 to 1` 
Modulation | `0 to 1`
Number | `Any 32-Bit Number`
Octave | `-4 to 4`

Each signal type is associated with one or more input or output. Below is an overview of each general type as well as a more detailed breakdown of each signal type.

###Audio
**Input/Outputs: Audio, Left/Right**

Audio signals are the sounds that pass through and out of Audulus. Audio can come from an external instrument or can be created from within Audulus using oscillators, noise sources, and other sound-generating modules.

Audio signals have both a positive and negative component. Audio output cannot exceed the -1 to 1 maximum range. Larger values will be clipped, causing distortion.

###Modulation
**Input/Outputs: Modulation, Gate, Envelope, Knob**

Modulation signals are control signals. They can control a filter's cutoff, advance a sequencer step, trigger an envelope, and much more.

All of the knobs in the module library work in a 0 to 1 range so that they can interface with any modulation signal directly. Because of this, they are also often interchangeable with one another.  However, modules expecting gate signals will only trigger properly with a gate input.

###Number
**Input/Outputs: Number, Inverse, Any Signal, Degrees, High/Low, Hz, Radians**

Number signals can have specific or non-specific ranges. They can act as control signals, but they are not interchangable with modulation signals.

In general, do not connect number signals to any audio, modulation, or octave inputs. Doing so can cause a painful spike in volume or pitch.

###Octave
**Input/Outputs: Octave**

The Octave signal in Audulus is a linearized pitch scale centered at 0 at a specific reference pitch. The default reference pitch is A = 440Hz. Every integer is an octave above or below the reference pitch.

Below is an example of a chromatic scale one octave above and one octave below the reference pitch. It also shows the intervals of the reference pitch to the maximum 4 and the minimum -4. The standard number of intervals in an octave is 12, but you can divide it up more to access microtones. 

Note | Octave Signal
:------------- | :------------- |
**A8 = 7050Hz** | `4`
**A7 = 3520Hz** | `3`
**A6 = 1760Hz** | `2`
A# | `1 + 1/12`
**A5 = 880Hz** | `1`
G# | `11/12`
G| `10/12`
F#| `9/12`
F| `8/12`
E| `7/12`
D#| `6/12`
D| `5/12`
C#| `4/12`
C| `3/12`
B| `2/12`
A# | `1/12`
**A4 = 440Hz** | `0`
G# | `-1/12`
G| `-2/12`
F#| `-3/12`
F| `-4/12`
E| `-5/12`
D#| `-6/12`
D| `-7/12`
C#| `-8/12`
C| `-9/12`
B| `-10/12`
A#| `-11/12`
**A3 = 220Hz** | `-1`
G# | `-1 - 1/12`
**A2 = 110Hz** | `-2`
**A1 = 55Hz** | `-3`
**A0 = 22.5Hz** | `-4`





###Signal Glossary

Below is a chart of the input-output abbreviations. The label is the one-letter or symbol abbreviation at the middle of the input or output. Some labels have lights associated with them. The definition is what the label refers to. The range is the set of expected input-output values. The notes are brief explanations of the signal type and what they do.


Label | Light | Definition | Range  | Notes
:------------- | :------------- | :------------- | :-------------| :-------------
`#`  | -  | Number | `Any 32-Bit Number` |  Number signals are non-specific numbers . Often used for counting.
`-`  | - | Inverse | `Any 32-Bit Number` | This indicator is used to show that the output is an inverted version of an adjacent signal, and is usually placed to the left of the uninverted signal.
`>`  | - | Any Signal | `Any 32-Bit Number` | This symbol is used for inputs and outputs with non-specific signals.  Often found on switch and routing modules.
`a`  | - | Audio | `-1 to 1` | Keep your audio signals in the -1 to 1 range to prevent hard clipping.
`d`  | - | Degrees | `0 to 360` | Useful for indicating phase relationships.
`e`  | red | Envelope | `0 to 1` | Often used to modulate oscillator volume and filter cutoff.
`g`  | green | Gate | `0 or 1` | Gate signals are on/off signals that act mostly as switches and triggers.  Logic expressions and other nodes that react to gates generally react to the rising edge of the gate - the moment the gate changes from low `0` to high `1`.  This library makes no distinction between a gate and a pulse.  For the shortest available pulse, use the One Frame Pulse module under Modules  Utilities. The only exception to the gate signal range is in gate height into an envelope, which allows for dynamics.
`H/L`  | - | High/Low | `Any 32-Bit Number` | Used to set upper and lower limits or signals or to indicate a relationship between two output signals.
`Hz`  | - | Hertz (Frequency) | `0 to Sample Rate` | Hz values are generally used for directly entering precise values for filters, oscillators, or clocks.
`k`  | - | Knob | `0 to 1` | Knobs are kept 0-1 to interface easily with Modulation (m) signals.  When their range needs to be translated, this is done inside the module with math or one of the knob modules.
`L/R`  | - | Left/Right | `-1 to 1` | Stereo audio signals are denoted by the letters L/R.  You do not have to use them as stereo signals, but if you connect L to L and R to R, you can be assured of proper stereo imaging.
`m`  | red | Modulation | `0 to 1` | Modulation signals are all 0 to 1 so that they interface easily with the knobs in this library, which are all also 0 to 1.  LFOs and envelopes are examples of modulation signals.  When a knob's range needs to be translated, it is done so inside the module, rather than directly setting the range of the knob's min and max values.
`o`  | - | Octave | `-4 to 4` |  The Octave signal is a linear pitch scale that allows for simple arithmetic transposing. 0 represents the reference pitch, which is defaulted to A = 440Hz. A signal of 1 is one octave above the reference pitch, and -1 is one octave below the reference pitch. Chromatic notes are accessible in steps of 1/12. Microtonal notes are available in steps of 1/24 and above.
`r`  | - | Radians | `0 to 2*pi` | The Phasor node outputs Radians.  Useful in trigonometric functions.











