# nodes reference

###introduction to nodes

Everything in Audulus is built with `nodes`. Nodes are packets of code that do things. A node may have inputs, outputs, or both.

You connect nodes together by dragging a wire from an output to an input. You cannot drag a wire from an input to an output. You can connect one output to as many inputs as you want.

You disconnect nodes by unhooking a wire from an input. Wires cannot be disconnected from an output. An input only accepts one wire.

Wires can go from any output anywhere to any input anywhere: up, down, left, or right. However, overall signal flow in Audulus is from left to right.

Nodes send and receive signals through wires. Every signal is a number. [^1] Although all signals are numbers, there are several categories of signals. These categories are defined by their range, unit, and how they are used.

[^1]: Audulus signals are signed 32-bit floats

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
The `text` node has no inputs or outputs. `text` nodes are used for labeling and commenting inside your patches. Click or tap on the node and open the `inspector panel` (pictured below). You can then type in the text field and text will appear inside the node.

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
alt="timer node"
width="200"/>

input | signal
:-- | :--
`trigger` | `gate`

output | signal
:-- | :--
`time` | `seconds` since last reset

**description**

The `timer` node outputs a signal in `seconds` since its last reset. The node resets on the rising edge of an incoming `gate` signal.

The `timer` output increases smoothly from second to second. Its functional precision is `1/sampleRate seconds`. For example: at a sample rate of 44.1kHz the precision is `1/44,100` or approximately `0.00002 seconds`.

###zero cross

<img src="img/nodes_reference/util/zero_cross/zero_cross_node.png"
alt="zero cross node"
width="200"/>

input | signal
:-- | :--
`in` | `any` but it must cross through or at least touch `0`

output | signal
:-- | :--
`out` | `hz`

**description**

The `zero cross` node counts the time between two zero-crossings and outputs that value as a `hz` signal. To be counted as a zero-crossing, the signal must either pass through `0` or be `= 0` at some point during its cycle.


##math

**description**

The `math` nodes are some of the most powerful and versatile nodes. 

- The `expr` node alone has 40 operators and functions which can be combined in many ways. 
- `sum` and `product` are elegant ways to visually emphasize how signals are combining and can be expanded to have as many inputs as necessary. 
- The `random` node has a `seed` input that ensures multiple copies of the same module can produce different random results with different `seed` values.


###expr

<img src="img/nodes_reference/math/expr/expr_node.png"
alt="expr node"
width="200"/>

arithmetic operator | description
:-- | :--
`x + y` | addition
`x - y` | subtraction
`x * y` | multiplication
`x / y` | division
`x^y` | exponentiation
`-x` | negation
`(x)` | parenthetical grouping

exponential function | description
:-- | :--
`pow(x, y)` | exponentiation
`exp(x)` | `e^x`
`ln(x)` | natural log
`log2(x)` | log base 2
`log10(x)` | log base 10
`exp2(x)` | `2^x`
`sqrt(x)` | square root[^4]

[^4]: Cube roots and beyond are accessible like this: `x^(1/y)` where `y = degree` and `x = radicand`. 

boolean operator | description
:-- | :--
`x == y` | `x` is exactly equal to `y`
`x != y` | `x` is not `y`
`x < y` | `x` is less than `y`
`x <= y` | `x` is less than or equal to `y`
`x > y` | `x` is greater than `y`
`x >= y` | `x` is greater than or equal to `y`

common function | description
:-- | :--
`abs(x)` | absolute value
`floor(x)` | round down to integer
`ceil(x)` | round up to integer
`fract(x)` | `x - floor(x)`
`mod(x,y)` | remainder of `x / y`
`min(x, y)` | returns lesser of `x` and `y`
`max(x, y)` | returns greater of `x` and `y`
`clamp(x, a, b)` | restricts `x` to the interval `[a, b]`
`step(x, edge)` | `1` if `x > edge` otherwise `0`
`smoothstep(a, b, x)` | smooth step from `0 to 1` at the interval `[a, b]`
`mix(x, a, b)` | `0 to 1` at `x` smoothly transitions between the interval `[a, b]`

trigonometric function | description
:-- | :--
`sin(x)` | sine
`cos(x)` | cosine
`tan(x)` | tangent
`asin(x)` | arc sine
`acos(x)` | arc cosine
`atan(x)` | arc tangent
`sinh(x)` | hyper sine
`cosh(x)` | hyper cosine
`tanh(x)` | hyper tangent

constant | description
:-- | :--
`pi` | π
`e` | Euler's number

**description**

The `expr` node is the most versatile node. It does math and basic programming operations.

You enter equations into the `inspector panel`, pictured below.

<img src="img/nodes_reference/math/expr/expr_inspector.png"
alt="expr node inspector panel"
width="200"/>

You can drag and drop various selected functions into the text field, or if you know their syntax, type them directly into the text box.

Entering letters or words will create variables as inputs, pictured below.

<img src="img/nodes_reference/math/expr/expr_var.png"
alt="expr node variables"
width="200"/>

Variables are case-sensitive, meaning `x` is not the same as `X`. Spaces and underscores are not allowed. For long variables, you can use camel case. For example: `thisIsALongVariable`.

Certain variable names are reserved, like `mod`, `e`, and `pi`. If you need to use them as variables you can capitalize the first letter, like this: `Mod`, `E`, `Pi`.

You can call a variable multiple times within an expression, like `x * x * x`.

Spaces between variables and operators and within functions are optional. `x*y` is the same as `x * y` and `clamp(x,0,1)` is the same as `clamp(x, 0, 1)`.

Functions can be nested within one another, like `max(0, min(x, 1)`.

Expressions like the `1/3` in `x * (1/3)` are evaluated once and replaced by a float in the background of Audulus. In other words, `1/3` is calculated once on start up and replaced internally by the number `0.3333...`, saving some compute time.

Divide-by-zero functions return a `0`. In other rare cases it is possible to create an expression that outputs a `nan` value, or "Not a number." The node producing the `nan` will immediately self-disconnect from your signal chain to prevent damage to speakers. A `nan` will be displayed in the `value` node, as pictured below.

<img src="img/nodes_reference/math/expr/expr_nan.png"
alt="expr node not a number error"
width="400"/>


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