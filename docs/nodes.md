# nodes reference

###introduction to nodes

Everything in Audulus is built with `nodes`. Nodes are packets of code that do things. A node may have inputs, outputs, or both.

You connect nodes together by dragging a wire from an output to an input. You cannot drag a wire from an input to an output. You can connect one output to as many inputs as you want.

You disconnect nodes by unhooking a wire from an input. Wires cannot be disconnected from an output. An input only accepts one wire.

Wires can go from any output anywhere to any input anywhere: up, down, left, or right. However, overall signal flow in Audulus is from left to right.

Nodes send and receive signals through wires. Every signal is a number. [^1] Although all signals are numbers, there are several categories of signals. These categories are defined by their range, unit, and how they are used.

[^1]: Audulus signals are 32-bit signed floats

The table below describes every type of signal that nodes use.

signal | range
:-- | :--
`any` | `any` signals can be any number and type of signal
`audio` | `-1 to 1`[^2]
`gate` | `0 or high` where `high` is a non-zero positive number.
`hz`| `0 to sampleRate/2`[^3]
`mod`| `0 to 1`
`seconds` | `0 to 2^32-1`

[^2]: Audio signals can exceed the `-1 to 1` range, but they will be clipped to that range upon output.
[^3]: Hz values above `sampleRate/2` can be generated but are limited in use. Negative `hz` signals can be used to flip the phase of the phasor node, useful for through-zero FM.

Some nodes have attributes that are accessible in the `inspector panel`. Every node has an `(x, y)` position attribute in this panel. Other nodes have attributes you can change directly on the node.

Nodes can be packaged into `modules` and `submodules`. Modules are containers for nodes that allow you to create a user interface for you to interact with. Submodules are used inside of modules. They are like user-created nodes.

There are 10 different categories of nodes. The table below lists each category provides a short description.

category | description
:-- | :--
`util` | various utilities
`math` | use math and logic to manipulate and create signals
`meter` | displays for monitoring signals
`midi`| MIDI utilities
`level`| tools for adjusting and analyzing signal levels
`dsp`| digital signal processing tools
`synth`| essential primitive-level synthesis tools
`module`| everything used for creating modules and submodules
`poly`| utilities for creating and managing polyphonic signals
`switch`| tools for routing signals



##util

**description**

`util` nodes are various utilities that do some very essential things. 

- The `adc` and `dac` nodes are used to get `audio` and `CV` in and out of Audulus. 
- The `text` node is used for labeling and commenting inside of patches. 
- The `timer` node has a variety of uses including creating envelopes and driving automation. 
- The `zero cross` node analyzes incoming audio and outputs its frequency in `hz`.


###adc

<img src="img/nodes_reference/util/adc/adc_node.png"
alt="adc node" 
width="200"/>


output | signal
:-- | :--
`adc` | `audio`

control | description
:-- | :--
`channel number` | access to 1 of 16 channels indexed from `0`

**description**

The `adc` node is how you get `audio` and `CV` into Audulus from an external source. An external source could be a microphone, a DAW, or a CV input from a hardware modular synth.

The `adc` node outputs an `audio` signal, but in this case, all that means is that incoming signals are clamped between `-1 and 1`. The `adc` node is often used as an `audio` input, but it can also be used to pass a `gate` signal from a modular synth.

The `adc` node can access the first 16 inputs of any class-compliant audio interface.

The channels are indexed from `0`. Clicking or tapping on the channel number will increment it by 1 up to 15 when it will wrap around to 0 again.

In most cases, `0` is the left channel and `1` is the right channel.


###dac

<img src="img/nodes_reference/util/dac/dac_node.png"
alt="dac node" 
width="200"/>

input | signal
:-- | :--
`dac` | `audio`

control | description
:-- | :--
`channel number` | access to 1 of 16 channels indexed from `0`

**description**

The `dac` node is how you get `audio` and `CV` out of Audulus and send it to an external output. An external output could be your headphones, speakers, a DAW, or a CV output to a hardware modular synth.

The `dac` node takes an `audio` signal input, but in this case, all that means is that outgoing signals are clamped between `-1 and 1`. The `dac` node is often used as an `audio` output, but it can also be used to pass a `gate` signal to a modular synth.

The `dac` node can access the first 16 outputs of any class-compliant audio interface.

The channels are indexed from `0`. Clicking or tapping on the channel number will increment it by 1 up to 15 when it will wrap around to 0 again.

In most cases, `0` is the left channel and `1` is the right channel.

The `dac` node does not include any DC-offset filtering. A constant DC offset can damage speakers. Most audio interfaces will filter a DC offset, but this offset can still cause distortion by decreasing the amount of headroom you have.

It is best practice to use a `dc blocker` node before a `dac` node unless you explicitly need to send a `mod` or `gate` signal to an external instrument.

###text

<img src="img/nodes_reference/util/text/text_node.png"
alt="text node" 
width="200"/>

**description**

The `text` node has no inputs or outputs. `text` nodes are used for labeling and commenting inside your patches. Click or tap on the node and open the inspector window (pictured below). You can then type in the text field and text will appear inside the node.

<img src="img/nodes_reference/util/text/text_inspector.png"
alt="text inspector panel" 
width="200"/>

option | description
:-- | :--
`Align` | Choose from `Left`, `Center`, and `Right` aligned text
`Exposed` | Check the box to expose this node to the UI of the module it is contained within

The `text` node can be resized by tapping or clicking on the blue ball that appears when selecting the node and dragging the ball left or right.

<img src="img/nodes_reference/util/text/text_resize.png"
alt="text resizing"
width="200"/>

Below are all of the characters that will render correctly in the `text` node.

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
ÄÅÃÁÂÀÆæâäáàåãÇçÐðÊËÉÈêëéè
ÍÎÏÌïîíìÑñÖØÓÔÒÕõöóòôøÜÚÛÙ
üûúùÝýÿßþÞ
0123456789
!"#$%&'()*+,-./:;<=>?@[\]^
_`{|}~£×¿®¬½¼¡«»©¢¥¤ı¦µ¯´¬
±¾¶§÷¸°¨•
```
Text size cannot be changed. The `canvas` node can do many manipulations with text that the `text` node cannot.


###timer

<img src="img/nodes_reference/util/timer/timer_node.png"
alt="timer node" width="200"/>

input | signal
:-- | :--
`trigger`   | `gate`

output | signal
:-- | :--
`time`   | `seconds` since last reset

**description**

The `timer` node outputs a signal in `seconds` since its last reset. The node resets on the rising edge of an incoming `gate` signal.

The `timer` output increases smoothly from second to second. Its functional precision is `1/sampleRate seconds`. For example: at a sample rate of 44.1kHz the precision is `1/44,100` or approximately `0.00002 seconds`.

###zero cross

<img src="img/nodes_reference/util/zero_cross/zero_cross_node.png"
alt="timer node" width="200"/>

input | signal
:-- | :--
`in`   | `any` but it must cross through or at least touch `0`

output | signal
:-- | :--
`out`   | `hz`

**description**

The `zero cross` node counts the time between two zero-crossings and outputs that value as a `hz` signal. To be counted as a zero-crossing, the signal must either pass through `0` or be `= 0` at some point during its cycle.


##math
###expr
###sum
###product
###random



##meter
###meter
###waveform
###value
###light
###rgb light
###scope
###shader
###canvas



##midi
###keyboard
###note send
###cc send
###trigger



##level
###spline
###mapper
###env follow



##dsp
###unit delay
###biquad
###low-pass
###high-pass
###delay line
###dc blocker
###sample rate
###resample
###memory



##synth
###osc
###phasor
###sample & hold
###adsr



##module
###module
###input
###output
###knob
###xy pad
###slider
###toggle
###touch pad



##poly
###combine
###split
###poly mix
###channel index
###channel count



##switch
###mux
###demux
###spigot