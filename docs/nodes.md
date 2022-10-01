# nodes reference

## introduction to nodes

<img src="img/nodes_reference/introduction_to_nodes/all_nodes.png"
alt="all node" 
width="800"/>

Everything in Audulus is built with `nodes`. There are 53 nodes in total.

Nodes are packets of code that do things. A node may have inputs, outputs, both, or none.

`Inputs` are on the left side of nodes and are blue. `Outputs` are on the right side of nodes and are red.

Nodes can be moved around the canvas, but they cannot be rotated.

You connect nodes together by dragging a wire from an output to an input. You cannot drag a wire from an input to an output. You can connect one output to as many inputs as you want.

You disconnect nodes by unhooking a wire from an input. Wires cannot be disconnected from an output. An input only accepts one wire. To connect multiple wires to one input, you must use an `add` node to first add the signals together.

Wires can go from any output anywhere to any input anywhere: up, down, left, or right. However, overall signal flow in Audulus is from left to right.

Nodes send and receive signals through wires. Every signal is a number. [^1] Although all signals are numbers, there are several categories of signals. These categories are defined by their range, unit, and how they are used.

[^1]: Audulus signals are signed 32-bit floats.

The table below describes every type of signal that nodes use.

signal | range
:-- | :--
`any` | `any` signals can be any number and type of signal
`audio` | `-1 to 1`[^2]
`gate` | `0 or high` where `high` is any non-zero positive 32-bit number.
`hz`| `0 to sampleRate/2`[^3]
`midi value` | integers `0 to 127`
`mod`| `0 to 1`
`seconds` | `0 to 2^32-1`

[^2]: Audio signals can exceed the `-1 to 1` range, but they will be clipped to that range upon output.
[^3]: Hz values above `sampleRate/2` can be generated but are limited in use. Negative `hz` signals can be used to flip the phase of the phasor node, useful for through-zero FM.

Some nodes have attributes that are accessible in the `inspector panel`. Every node has an `(x, y)` position attribute in this panel.

Nodes can be packaged into `modules` and `submodules`. `Modules` are containers for nodes that allow you to create a user interface for you to interact with. `Submodules` are used inside of `modules`. They are like user-created nodes.

Some nodes are exposable, meaning they have some element that can appear on UI of a `module`. Some, like the `knob` node, are automatically exposed while others, like the `text` node, have an option to expose.

If a node is exposable, a node will have an `(x, y)` coordinate for where it is inside the module and another `(x, y)` coordinate for where it is on the UI of the module.

Other nodes have attributes you can change directly on the node.

There are 10 different categories of nodes. The table below lists each category and provides a short description.

category | description
:-- | :--
`util` | various utilities
`math` | use math and logic to manipulate and create signals
`meter` | displays for monitoring signals
`midi`| MIDI utilities
`level`| tools for adjusting and analyzing signal levels
`dsp`| digital signal processing tools
`synth`| essential primitive-level synthesis tools
`module`| used for creating modules and submodules
`poly`| utilities for creating and managing polyphonic signals
`switch`| tools for routing signals

Some nodes count as outputs. Examples of outputs are `value`, `light`, and `dac` nodes.

If a node is not connected to an output, it will not be evaluated.

<br>

---


## util

**description**

`util` nodes are various utilities that do some very essential things. 

- The `adc` and `dac` nodes are used to get `audio` and `CV` in and out of Audulus. 
- The `text` node is used for labeling and commenting inside of patches. 
- The `timer` node has a variety of uses including creating envelopes and driving automation. 
- The `zero cross` node analyzes incoming audio and outputs its frequency in `hz`.

<br>

---


### adc

<img src="img/nodes_reference/util/adc/adc_node.png"
alt="adc node" 
width="200"/>


output | signal
:-- | :--
`adc` | `audio`

control | description
:-- | :--
`channel number` | access to 1 of 16 channels indexed from `0`

exposable | ❌
:-- | :--

**description**

The `adc` node is how you get `audio` and `CV` into Audulus from an external source. An external source could be a microphone, a DAW, or a CV input from a hardware modular synth.

The `adc` node outputs an `audio` signal, but in this case, all that means is that incoming signals are clamped between `-1 and 1`. The `adc` node is often used as an `audio` input, but it can also be used to pass a `gate` signal from a modular synth.

The `adc` node can access the first 16 inputs of any class-compliant audio interface.

The channels are indexed from `0`. Clicking or tapping on the channel number will increment it by 1 up to 15 when it will wrap around to 0 again.

In most cases, `0` is the left channel and `1` is the right channel.

<br>

---


### dac

<img src="img/nodes_reference/util/dac/dac_node.png"
alt="dac node" 
width="200"/>

input | signal
:-- | :--
`dac` | `audio`

control | description
:-- | :--
`channel number` | access to 1 of 16 channels indexed from `0`

exposable | ❌
:-- | :--

**description**

The `dac` node is how you get `audio` and `CV` out of Audulus and send it to an external output. An external output could be your headphones, speakers, a DAW, or a CV output to a hardware modular synth.

The `dac` node takes an `audio` signal input, but in this case, all that means is that outgoing signals are clamped between `-1 and 1`. The `dac` node is often used as an `audio` output, but it can also be used to pass a `gate` signal to a modular synth.

The `dac` node can access the first 16 outputs of any class-compliant audio interface.

The channels are indexed from `0`. Clicking or tapping on the channel number will increment it by 1 up to 15 when it will wrap around to 0 again.

In most cases, `0` is the left channel and `1` is the right channel.

The `dac` node does not include any DC-offset filtering. A constant DC offset can damage speakers. Most audio interfaces will filter a DC offset, but this offset can still cause distortion by decreasing the amount of headroom you have.

It is best practice to use a `dc blocker` node before a `dac` node unless you explicitly need to send a `mod` or `gate` signal to an external instrument.

<br>

---


### text

<img src="img/nodes_reference/util/text/text_node.png"
alt="text node" 
width="200"/>

exposable | ✅
:-- | :--

**description**

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

<br>

---


### timer

<img src="img/nodes_reference/util/timer/timer_node.png"
alt="timer node"
width="200"/>

input | signal
:-- | :--
`trigger` | `gate`

output | signal
:-- | :--
`time` | `seconds` since last reset

exposable | ❌
:-- | :--

**description**

The `timer` node outputs a signal in `seconds` since its last reset. The node resets on the rising edge of an incoming `gate` signal.

The `timer` output increases smoothly from second to second. Its functional precision is `1/sampleRate seconds`. For example: at a sample rate of 44.1kHz the precision is `1/44,100` or approximately `0.00002 seconds`.

<br>

---


### zero cross

<img src="img/nodes_reference/util/zero_cross/zero_cross_node.png"
alt="zero cross node"
width="200"/>

input | signal
:-- | :--
`in` | `any` but it must cross through or at least touch `0`

output | signal
:-- | :--
`out` | `hz`

exposable | ❌
:-- | :--

**description**

The `zero cross` node counts the time between two zero-crossings and outputs that value as a `hz` signal. To be counted as a zero-crossing, the signal must either pass through `0` or be `= 0` at some point during its cycle.

<br>

---


## math

**description**

The `math` nodes are some of the most powerful and versatile nodes. 

- The `expr` node alone has 40 operators and functions which can be combined in many ways. 
- `sum` and `product` are elegant ways to visually emphasize how signals are combining and can be expanded to have as many inputs as necessary. 
- The `random` node has a `seed` input that ensures multiple copies of the same module can produce different random results with different `seed` values.

<br>

---


### expr

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
`exp(x)` | `e^x`
`exp2(x)` | `2^x`
`pow(x, y)` | exponentiation `x^y`
`sqrt(x)` | square root[^4]
`ln(x)` | natural log
`log2(x)` | log base 2
`log10(x)` | log base 10


[^4]: Cube roots and beyond are accessible like this: `x^(1/y)` where `x = radicand` and `y = degree`. 

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
`mod(x, y)` | remainder of `x / y`
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
`asin(x)` | inverse sine
`acos(x)` | inverse cosine
`atan(x)` | inverse tangent
`sinh(x)` | hyper sine
`cosh(x)` | hyper cosine
`tanh(x)` | hyper tangent
`asinh(x)` | inverse hyper sine
`acosh(x)` | inverse hyper cosine
`atanh(x)` | inverse hyper tangent

constant | description
:-- | :--
`pi` | π
`e` | Euler's number

exposable | ❌
:-- | :--

**description**

The `expr` node is the most versatile node. It does math and basic programming operations.

Double clicking on any input will create an `expr` node.

You enter equations into the `inspector panel`, pictured below. You do not need to add an `=` sign after your expression.

<img src="img/nodes_reference/math/expr/expr_inspector.png"
alt="expr node inspector panel"
width="200"/>

You can drag and drop various selected functions into the text field, or if you know their syntax, type them directly into the text box.

Entering letters or words will create variables as inputs, as pictured below.

<img src="img/nodes_reference/math/expr/expr_var.png"
alt="expr node variables"
width="200"/>

Variables are case-sensitive, meaning `x` is not the same as `X`. Spaces and underscores are not allowed. For long variables, you can use camel case. For example: `thisIsALongVariable`.

Variables can contain numbers, but they must start with a letter. `input1` will generate an input but `1input` will not. Variables cannot contain symbols.

Certain variable names are reserved, like `mod`, `e`, and `pi`. If you need to use them as variables you can capitalize the first letter, like this: `Mod`, `E`, `Pi`.

You can call a variable multiple times within an expression, like `x * x * x`.

Spaces between variables and operators and within functions are optional. `x*y` is the same as `x * y` and `clamp(x,0,1)` is the same as `clamp(x, 0, 1)`.

Functions can be nested within one another, like `max(0, min(x, 1))`.

Divide-by-zero functions return a `0`. In other rare cases it is possible to create an expression that outputs a `nan` value, or "Not a number." The node producing the `nan` will immediately self-disconnect from your signal chain to prevent damage to speakers. A `nan` will be displayed in the `value` node, as pictured below.

<img src="img/nodes_reference/math/expr/expr_nan.png"
alt="expr node not a number error"
width="400"/>

Expressions like the `1/3` in `x * (1/3)` are evaluated once during start-up and replaced by a float in the background of Audulus, saving some compute time.

<br>

---


### sum

<img src="img/nodes_reference/math/sum/sum_node.png"
alt="sum node"
width="200"/>

input | signal
:-- | :--
`in` | `any`
`in` | `any`
`...` | `any`

output | signal
:-- | :--
`sum` | `any`

exposable | ❌
:-- | :--

**description**

The `sum` node adds two or more signals together.

In the `inspector channel` you can specify how many channels you want to add together. The maximum is `256`.

<img src="img/nodes_reference/math/sum/sum_inspector.png"
alt="sum inspector"
width="200"/>

When you increase the number of channels, the number of inputs increases accordingly.

<img src="img/nodes_reference/math/sum/sum_multiple_inputs.png"
alt="sum multiple inputs"
width="200"/>

<br>

---


### product

<img src="img/nodes_reference/math/product/product_node.png"
alt="product node"
width="200"/>

input | signal
:-- | :--
`in` | `any`
`in` | `any`
`...` | `any`

output | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--

**description**

The `product` node multiplies two or more signals together.

In the `inspector channel` you can specify how many channels you want to multiply together. The maximum is `256`.

<img src="img/nodes_reference/math/product/product_inspector.png"
alt="product inspector"
width="200"/>

When you increase the number of channels, the number of inputs increases accordingly.

<img src="img/nodes_reference/math/product/product_multiple_inputs.png"
alt="product multiple inputs"
width="200"/>

<br>

---


### random

<img src="img/nodes_reference/math/random/random_node.png"
alt="random node"
width="200"/>

output | signal
:-- | :--
`out` | `mod`

exposable | ❌
:-- | :--

The `random` node outputs a new random number between `0 and 1` for every sample. In other words, it produces `white noise.`

The `Seed` value can be changed in the `inspector panel`, pictured below. Changing the `Seed` is necessary in cases where you have two or more `random` nodes in a patch and want them to produce a different string of random numbers.

<img src="img/nodes_reference/math/random/random_inspector.png"
alt="random node"
width="200"/>

If the `Seed` remains the same, every time the patch is reopened, the same string of random numbers will be produced.

<br>

---



## meter

**description**

The `meter` nodes are vital for displaying information about signals.

- The `meter` node is responsive and versatile.
- The `waveform` node is a simple way to see how signals change over time.
- The `value` node can help with debugging as well as displaying information on UIs.
- The `light` and `rgb light` nodes are great for adding visual feedback to modules.
- The `scope` node is like the `waveform` node, but suited for examining audio rate signals.
- With the `shader` and `canvas` nodes you can use your own code to create your own beautiful custom meters, visualizers, and UI elements using GLSL and Lua.

<br>

---


### meter

<img src="img/nodes_reference/meter/meter/meter_node.png"
alt="meter node"
width="200"/>

input | signal
:-- | :--
`in` | `audio`

exposable | ✅ 
:-- | :--

**description**

The `meter` node displays the amplitude of a signal. The input works in a range of `-1 to 1`. However, `0 to 1` will display the same as `0 to -1`, as you can see below:

<img src="img/nodes_reference/meter/meter/meter_negative.png"
alt="meter negative"
width="400"/>

In the `inspector panel` the `meter` node can be resized by altering the height and width parameters, as seen below. It is also exposable.

<img src="img/nodes_reference/meter/meter/meter_inspector.png"
alt="meter inspector"
width="200"/>

If both `W` and `H` values are `0`, then the node defaults to its standard size. The node can be resized however you want, but it cannot be rotated.

<img src="img/nodes_reference/meter/meter/meter_sizes.png"
alt="meter sizes"
width="200"/>

If you wire a `poly` signal to a `meter` node, it automatically creates one meter per channel. 

<img src="img/nodes_reference/meter/meter/meter_poly.png"
alt="meter poly"
width="200"/>

<br>

---


### waveform

<img src="img/nodes_reference/meter/waveform/waveform_node.png"
alt="waveform node"
width="200"/>

input | signal
:-- | :--
`in` | `audio`

exposable | ✅
:-- | :--

**description**

The `waveform` node allows you to see signals change over time. It has a fixed 5-second window and moves from left to right.

Since it works with the `audio` range, the top limit of the node is `1`, the center is `0`, and the bottom is `-1`.

<img src="img/nodes_reference/meter/waveform/waveform_range.png"
alt="waveform range"
width="400"/>

The `waveform` node works best with low frequency signals. If you want to examine audio-rate signals, use a `scope` node.

<img src="img/nodes_reference/meter/waveform/waveform_mod_v_audio.png"
alt="waveform mod vs audio"
width="200"/>

<br>

---


### value

<img src="img/nodes_reference/meter/value/value_node.png"
alt="value node"
width="200"/>

input | signal
:-- | :--
`in` | `any`

exposable | ✅
:-- | :--

**description**

The `value` node displays the current value of any signal.

In the `inspector panel`, you can set precision from `0` to `0.0000`, and an option to alight `Left`, `Right`, or `Center`. The `value` node is also exposable.

<img src="img/nodes_reference/meter/value/value_inspector.png"
alt="value inspector"
width="200"/>

Changing precision can be useful for UI displays. For example, a sequencer's `current step` display should be a whole number, not a decimal.

<img src="img/nodes_reference/meter/value/value_precision.png"
alt="value precision"
width="200"/>

If you wire a `poly` signal to a `value` node, it automatically creates one value display per channel. 

<img src="img/nodes_reference/meter/value/value_poly.png"
alt="value precision"
width="400"/>

<br>

---


### light

<img src="img/nodes_reference/meter/light/light_node.png"
alt="light node"
width="200"/>

input | signal
:-- | :--
`in` | `gate`

exposable | ✅ automatic
:-- | :--


**description**

The `light` node turns on when the incoming signal is `high` (any non-zero positive number). Otherwise it stays off.

<img src="img/nodes_reference/meter/light/light_on.png"
alt="light on"
width="400"/>

<br>

---


### rgb light

<img src="img/nodes_reference/meter/rgb_light/rgb_light_node.png"
alt="rgb light node"
width="200"/>

input | signal
:-- | :--
`r` | `mod`
`g` | `mod`
`b` | `mod`

exposable | ✅ automatic
:-- | :--


**description**

The `rgb light` node has 3 inputs: one for red `r`, one for green `g`, and one for blue `b`.

<img src="img/nodes_reference/meter/rgb_light/rgb_light_colors.png"
alt="rgb light colors"
width="200"/>

Each input works with a `mod` signal. When the signal is `0`, the light is off. When the signal is `1`, the light is fully on.

<img src="img/nodes_reference/meter/rgb_light/rgb_light_brightness.png"
alt="light node"
width="400"/>

Colors can be mixed by sending different values to each input.

<img src="img/nodes_reference/meter/rgb_light/rgb_light_mix.png"
alt="light node"
width="200"/>

<br>

---

### scope

<img src="img/nodes_reference/meter/scope/scope_node.png"
alt="scope node"
width="200"/>

input | signal
:-- | :--
`x` | `audio`
`y` | `audio`
`r` | `mod`
`g` | `mod`
`b` | `mod`
`s` | `mod`

exposable | ✅
:-- | :--


**description**

The `scope` node can visualize high frequency waveforms, phase relationships, and Lissajous curves that you otherwise could not with the `waveform` node.

A cursor draws a dot with a color of `{r, g, b}` at the coordinates `(x, y)` where both `x` and `y` have a range of `-1 to 1`. The point `(0, 0)` is the center of the display.

<img src="img/nodes_reference/meter/scope/scope_circle.png"
alt="scope circle"
width="400"/>

The `s` variable is a measure of the persistence of the line drawn where `0` means only the current position of the cursor is shown and `1` means the cursor will draw a line that persists infinitely. `s` values between `0` and `1` will cause the line to fade quickly or gradually over time.

There can be a large difference between what an `s` value of `0.9`, `0.99`, and `0.999` look like, so experiment with what works best for your use.

In the `scope` node's `inspector panel` there are options to change both the `Size` and resolution (`Image Size`) of the scope.

<img src="img/nodes_reference/meter/scope/scope_inspector.png"
alt="scope inspector"
width="200"/>

The default size is `W = 200` and `H = 200` with an image size of `W = 512` and `H = 512`. 

For a crisp, clean-looking line, the `Image Size` should be at least double the `Size` parameter. For a more digital-looking, stair-stepped size, the `Image Size` should be the same or smaller than the `Size.`

<img src="img/nodes_reference/meter/scope/scope_size_resolution.png"
alt="scope sizes"
width="400"/>

<br>

---


### shader

<img src="img/nodes_reference/meter/shader/shader_node.png"
alt="shader node"
width="200"/>

exposable | ✅
:-- | :--


**description**

The `shader` node is an OpenGL shader that allows you to write your own shader using GLSL, a programming language similar to C.

Although the default example has `r` `g` `b` inputs, you are not limited to just those inputs. You can have 0 inputs or as many as you need to run your code.

You write code in the `inspector panel`.

<img src="img/nodes_reference/meter/shader/shader_code.png"
alt="shader code"
width="400"/>

At the bottom of the `inspector panel` you can also find `Size` and `Image Size` parameters.

<img src="img/nodes_reference/meter/shader/shader_inspector.png"
alt="shader inspector"
width="200"/>

Error messages, if any, appear above these parameters.

<img src="img/nodes_reference/meter/shader/shader_errors.png"
alt="shader errors"
width="200"/>

<br>

---


### canvas

<img src="img/nodes_reference/meter/canvas/canvas_node.png"
alt="canvas node"
width="200"/>

exposable | ✅
:-- | :--


**description**

The `canvas` node is an allows you to draw things using Lua, a simple interpreted programming language.

Although the default example has no inputs or outputs, you can create as many as you'd like by declaring them in the inspector panel above the code block.

<img src="img/nodes_reference/meter/canvas/canvas_io.png"
alt="canvas io"
width="200"/>

To create inputs and outputs, you must enter each variable with a space in between.

<img src="img/nodes_reference/meter/canvas/canvas_declare_variables.png"
alt="canvas declare variables"
width="400"/>

Below the field where you declare variables you can use Lua code to draw things on the `canvas` node.

<img src="img/nodes_reference/meter/canvas/canvas_code.png"
alt="canvas code"
width="400"/>

Below the code block are all of the available Lua functions which you can drag and drop into your code.

<img src="img/nodes_reference/meter/canvas/canvas_functions.png"
alt="canvas functions"
width="400"/>

Below the functions are options to change the `Size` of the `canvas` node and `Save Data` between patch loads.

<img src="img/nodes_reference/meter/canvas/canvas_inspector.png"
alt="canvas inspector"
width="200"/>

Unlike other nodes, the `canvas` node does not run at audio rate, making it unsuitable to be within any audio or time-critical control paths. As the name implies, it is intended to be space to draw things.

<br>

---



## midi

**description**

The `midi` nodes send and receive MIDI signals in and out of Audulus.

- The `keyboard` allows you to play Audulus synths with an external MIDI controller or feed in MIDI notes from a DAW.
- The `note send` node sends MIDI notes out of Audulus to hardware or DAWs.
- The `cc send` node sends MIDI CC messages from Audulus to hardware or or DAWs.
- The `trigger` node can both act like a button within Audulus and can also receive on/off MIDI messages.

<br>

---



### keyboard

<img src="img/nodes_reference/midi/keyboard/keyboard_node.png"
alt="keyboard node"
width="200"/>

output | signal
:-- | :--
`Hz` | `Hz`
`gate` | `gate`

control | description
:-- | :--
`Legato/Poly(2,4,8,16)` | sets the number of voices
`Omni/(1-16)` | sets the MIDI channel

exposable | ❌
:-- | :--


**description**

The `keyboard` node receives input from MIDI keyboards, DAWs, and other input MIDI devices.

It outputs a `Hz` value for the note and a `gate` signal for note on/off. The height of the gate represents the velocity.

There are also two controls on the `keyboard` node. The first cycles through `Legato` and `Poly(2,4,8,16)`. 

`Legato` means only one note (the last played) will be outputted. `Poly 2` means 2 notes can be played at once, `Poly 4` means 4, and so on.

Higher poly counts multiply CPU usage, so only set it to the count you need.

The `Omni/(1-16)` control specifies which incoming MIDI channel is referenced. On `Omni`, any messages from any of the channels will come through. You can also set the keyboard node to listen to a specific channel `1-16`.

<br>

---


### note send

<img src="img/nodes_reference/midi/note_send/note_send_node.png"
alt="note send node"
width="200"/>

input | signal
:-- | :--
`note` | `midi value`
`gate` | `gate`
`velocity` | `midi value`

exposable | ❌
:-- | :--


**description**

The `note send` node sends MIDI note, gate, and velocity data from Audulus to external instruments.

The `note` and `velocity` inputs correspond to the `0-127` integer values expected by MIDI. Inputs are floored, so if the value is between `0` and `1`, `0` is the output.

The `gate` input sends a note on/off signal where `high` is on and `0` is off.

<br>

---


### cc send

<img src="img/nodes_reference/midi/cc_send/cc_send_node.png"
alt="cc send node"
width="200"/>

input | signal
:-- | :--
`value` | `midi value`
`number` | `midi value`
`trigger` | `gate`

exposable | ❌
:-- | :--


**description**

The `cc send` node sends MIDI CC value from Audulus to external instruments.

When the `trigger` input goes high, the signal present at the `value` input is sent to the `number` CC.

<br>

---


### trigger

<img src="img/nodes_reference/midi/trigger/trigger_node.png"
alt="trigger node"
width="200"/>

control | description
:-- | :--
`button` | outputs `gate` when pressed

exposable | ✅ automatic
:-- | :--


**description**

The `trigger` node outputs a gate when its button is pressed. The button can be clicked, tapped, or assigned to an external hardware MIDI signal in MIDI mapping mode.

<br>

---


## level

**description**

The `level` nodes are tools helpful for manipulating the level of a signal.

- You can create custom lines with the `spline` node and trace over them to output a continuous series of custom values.
- The `mapper` node allows you to shape the response curve of a knob or signal moving through it.
- The `env follow` node traces the loudness envelope of an incoming signal and outputs it as a `mod` signal.

<br>

---


### spline

<img src="img/nodes_reference/level/spline/spline_node.png"
alt="spline node"
width="400"/>

input | signal
:-- | :--
`in` | `mod`

out | signal
:-- | :--
`out` | `mod`


control | description
:-- | :--
`spline` | create breakpoints to draw spline

exposable | ✅
:-- | :--


**description**

The `spline` node allows you to draw a line using two or more breakpoints and then trace over that line using a `mod` input.

Breakpoints are added by double clicking or tapping on the blank field inside the node. Once created, they can be dragged around anywhere inside of the field.

<img src="img/nodes_reference/level/spline/spline_draw.png"
alt="spline draw"
width="400"/>

The coordinate system determining the output is `(in, line)`. The bottom left of the field is `(0, 0)` and the top right is `(1, 1)`. The output of the node is the `y` value of the line given `x` input.

In the example below, identical spline nodes are driven by two different LFO shapes. The top is a saw wave and the bottom is a triangle wave.

<img src="img/nodes_reference/level/spline/spline_lfo.png"
alt="spline lfo"
width="400"/>

<br>

---


### mapper

<img src="img/nodes_reference/level/mapper/mapper_node.png"
alt="mapper node"
width="200"/>

input | signal
:-- | :--
`in` | `mod`

out | signal
:-- | :--
`out` | `mod` [^5]

[^5]: The output of the `mapper` node can overshoot the maximum and minimum of the `mod` signal by `~0.12`.

control | description
:-- | :--
`mapper` | move one of three breakpoints up or down to shape curve

exposable | ✅
:-- | :--


**description**

The `mapper` node allows you to change the response of an incoming modulation signal depending on the curve drawn in the node's field.

Below are some of the possible shapes you can draw using the mapper node.

<img src="img/nodes_reference/level/mapper/mapper_shapes.png"
alt="mapper shapes"
width="400"/>

The coordinate system determining the output is `(in, line)`. The bottom left of the field is `(0, 0)` and the top right is `(1, 1)`. The output of the node is the `y` value of the line given `x` input.

The image below shows how the different shapes transform the incoming saw LFO.

<img src="img/nodes_reference/level/mapper/mapper_lfo.png"
alt="mapper lfo"
width="400"/>

As you can see in the above image, the mapper node can overshoot the modulation signal. This exception is a maximum of approximately `+/- 0.12`.

<img src="img/nodes_reference/level/mapper/mapper_overshoot.png"
alt="mapper overshoot"
width="400"/>

<br>

---


### env follow

<img src="img/nodes_reference/level/env_follow/env_follow_node.png"
alt="env follow node"
width="200"/>

input | signal
:-- | :--
`in` | `audio`

out | signal
:-- | :--
`out` | `mod` [^6]

[^6]: In most cases, the `env follow` node is used to extract an amplitude envelope of an `audio` signal, and `abs(audio) = mod`. However, in reality the `env follow` node outputs `abs(any)` with some minor filtering to smooth transitions between samples.

exposable | ❌
:-- | :--


**description**

The `env follow` node extracts an envelope from an incoming audio signal and transforms it into a modulation signal. It does this by taking the absolute value of the incoming signal and applying a small amount of filtering to smooth transitions between samples.

<br>

---


## dsp

**description**

DSP is an acronym that means digital signal processing. The `dsp` nodes are essentials for creating filters and manipulating signals at a conceptually low level.

- The `unit delay` node delays a signal by a single sample and marks precisely where a feedback delay happens within a feedback loop.
- The `biquad` node is a building block for creating custom biquad filters.
- The `low-pass` and `high-pass` nodes are conveniently packaged, non-resonant filters.
- The `delay line` node can delay a signal up to 20 seconds.
- The `dc blocker` node prevents a signal with a DC-offset from harming speakers.
- The `sample rate` node outputs the current sample rate, useful in many calculations where the precise sample rate is needed.
- The `resample` node allows you to up- and then down-sample a signal to run certain parts of a module at a higher sample rate.
- The `memory` node allows you to record, playback, and import audio or control signals.

<br>

---


### unit delay

<img src="img/nodes_reference/dsp/unit_delay/unit_delay_node.png"
alt="unit delay node"
width="200"/>

input | signal
:-- | :--
`in` | `any`

out | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--


**description**

The `unit delay` node delays an incoming signal by `1` sample. It also explicitly tells Audulus where to insert a single sample feedback delay within a feedback loop. 

If a `unit delay` is not inserted somewhere within a feedback loop, Audulus will guess where to put it. Much of the time this is ok, but in some cases, like when creating analog-modeling filters, you need to be explicit about where the feedback delay goes.

<br>

---


### biquad

<img src="img/nodes_reference/dsp/biquad/biquad_node.png"
alt="biquad node"
width="200"/>

input | signal
:-- | :--
`in` | `any`
`a1` | a1 coefficient
`a2` | a2 coefficient
`a3` | a3 coefficient
`b1` | b1 coefficient
`b2` | b2 coefficient


out | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--


**description**

The `biquad` node allows you to create all different types of biquadratic filters. Refer to [this guide](https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html) for more information. 

You need to calculate the coefficient inputs separately from the node using `expr` nodes.

<br>

---


### low-pass

<img src="img/nodes_reference/dsp/low-pass/low-pass_node.png"
alt="low-pass node"
width="200"/>

input | signal
:-- | :--
`in` | `any`
`alpha` | `mod`

out | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--


**description**

The `low pass` node is a simple non-resonant `6dB/oct` low-pass filter. The `alpha` input is the smoothing factor where `1 = no filtering` and `0 = maximum filtering`. 

<br>

---


### high-pass

<img src="img/nodes_reference/dsp/high-pass/high-pass_node.png"
alt="high-pass node"
width="200"/>

input | signal
:-- | :--
`in` | `any`
`alpha` | `mod`

out | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--


**description**

The `low pass` node is a simple non-resonant `6dB/oct` high-pass filter. The `alpha` input is the smoothing factor where `1 = maximum filtering` and `0 = no filtering`. 

<br>

---


### delay line

<img src="img/nodes_reference/dsp/delay_line/delay_line_node.png"
alt="delay line node"
width="200"/>

input | signal
:-- | :--
`in` | `any`
`time` | `seconds`

out | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--


**description**

The `delay line` node delays an incoming signal by a set number of seconds, determined by the value at the `time` input.

<br>

---


### dc blocker

<img src="img/nodes_reference/dsp/dc_blocker/dc_blocker_node.png"
alt="dc blocker node"
width="200"/>

input | signal
:-- | :--
`in` | `audio`

out | signal
:-- | :--
`out` | `audio`

exposable | ❌
:-- | :--


**description**

The `dc blocker` node removes any DC offset from an `audio` signal. 

<br>

---


### sample rate

<img src="img/nodes_reference/dsp/sample_rate/sample_rate_node.png"
alt="sample rate node"
width="200"/>

out | signal
:-- | :--
`sample rate` | `Hz`

exposable | ❌
:-- | :--


**description**

The `sample rate` node outputs the current sample rate in `Hz`.

<br>

---


### resample

<img src="img/nodes_reference/dsp/resample/resample_node.png"
alt="resample node"
width="200"/>

in | signal
:-- | :--
`in` | `any`

out | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--


**description**

The `resample` node lets you run a portion of a patch at a higher sample rate, also known as supersampling.

In the `inspector` you can choose from different multiples of the base sample rate from `1x` to `16x`. Higher sample rates use more CPU time.

<img src="img/nodes_reference/dsp/resample/resample_inspector.png"
alt="resample inspector"
width="200"/>

For example, given a base sample rate of `44.1kHz`, `4x` sample rate would be `176.4kHz`.

To properly use the `resample` node, you have to have two `resample` nodes in your patch, one to mark where you want to begin supersampling and one to mark where you want to downsample back to the original sample rate, as well as a pre-downsampling low-pass filter with a cutoff set to half the base sample rate.

<img src="img/nodes_reference/dsp/resample/resample_example.png"
alt="resample example"
width="800"/>

Nodes that are super-sampled have a multiple in parentheses next to their titles, like `Resample (4x)`.


<br>

---


### memory

<img src="img/nodes_reference/dsp/memory/memory_node.png"
alt="memory node"
width="400"/>

in | signal
:-- | :--
`read index` | `any` (positive)
`write index` | `any` (positive)
`write value` | `any` 
`write enable` | `gate` 

out | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--


**description**

The `memory` node can read, write, and store `audio` and control signals. Information is stored in the `memory` node as a series of samples.

The `read index` is the sample number currently outputted, indexed from `0`.

The `write index` is the sample number currently selected to be (over)written, indexed from `0`.

The `write value` is the value of the sample to be written.

The `write enable` input will, if held `high`, write the `write value` to the `write index`.

Reading and writing to the `memory` node can happen at different index values at the same time.

You can also import audio to the memory node. On Mac, you do this by dragging an `.AIFF` or `.WAV` file from a Finder window into the space marked `Drop audio file here`. There is also a check box labeled `Save Data` that, when checked, will save the contents of the `memory` node in between patch loads.

<img src="img/nodes_reference/dsp/memory/memory_inspector.png"
alt="memory inspector"
width="200"/>

<br>

---


## synth

**description**

The `synth` nodes are low-level building blocks specific to audio synthesis.

- The `osc` node outputs one of 4 classic anti-aliased waveforms.
- The `phasor` node outputs an un-aliased phasor signal from `0 to 2π` useful for creating custom oscillators
- The `sample & hold` node can sample an input signal, store it, and hold that value at its output.
- The `adsr` node generates an envelope according to an incoming `gate` signal.


<br>

---


### osc

<img src="img/nodes_reference/synth/osc/osc_node.png"
alt="osc node"
width="200"/>

in | signal
:-- | :--
`Hz` | `Hz`
`amp` | `mod`
`sync` | `gate` or `audio`
`shp` | `mod` 

out | signal
:-- | :--
`out` | `audio`

control | description
:-- | :--
`waveform selector` | selects one of 4 waveforms

exposable | ✅
:-- | :--


**description**

The `osc` node outputs as `audio` one of four anti-aliased elemental waveforms, selectable on the panel of the node: sine, square, triangle, and saw.

The `osc` node is intended as an audio-rate oscillator. This means it is anti-aliased. Using the `osc` node as an LFO can lead to some unpredictable behavior with overshooting caused by the anti-aliasing.

The `Hz` input controls the speed of the oscillator from `0` to `sampleRate/2 Hz`. 

The `amp` input uses a `mod` signal to control the amplitude of the wave. For example: An amplitude value of `1` will set the output of the `osc` node to range between `-1 and 1`, whereas a value of `0.5` will oscillate between `-0.5 and 0.5`.

<img src="img/nodes_reference/synth/osc/osc_hz_amp.png"
alt="osc hz amp"
width="400"/>

The `sync` input will restart the waveform on the rising edge of an incoming `gate` or `audio` signal. It is a hard sync, meaning it will reset regardless of where it is in its cycle.

<img src="img/nodes_reference/synth/osc/osc_sync.png"
alt="osc sync"
width="400"/>

The `shp` input changes the shape of the square and saw waves. For the square wave, `shp` controls the pulse width from `50% to 100%`. For the saw wave, `shp` will transform the saw wave into a supersaw which, when modulated, simulates the chorusing effect of two detuned saw waves.

<img src="img/nodes_reference/synth/osc/osc_shp.png"
alt="osc shp"
width="400"/>

The waveform selector is exposable.


<br>

---


### phasor

<img src="img/nodes_reference/synth/phasor/phasor_node.png"
alt="phasor node"
width="200"/>

in | signal
:-- | :--
`freq` | `Hz` or `-Hz`
`sync` | `gate` or `audio`

out | signal
:-- | :--
`out` | `0 to 2π`

exposable | ❌
:-- | :--


**description**

The `phasor` node outputs a phasor from `0 to 2π` with 64-bit internal precision.

The `phasor` node is not anti-aliased, making it suitable for creating custom LFOs. If you want to create a custom VCO with a `phasor` node, refer to the `resample` node section to see how to anti-alias its output. You can use an `expr` node to shape and scale the output of the `phasor` node.

<img src="img/nodes_reference/synth/phasor/phasor_waveforms.png"
alt="phasor waveforms"
width="800"/>

The `sync` input will reset the phasor on the rising edge of a `gate` or `audio` signal.

<img src="img/nodes_reference/synth/phasor/phasor_sync.png"
alt="phasor sync"
width="800"/>

Positive `Hz` values at the `freq` input will run the `phasor` from `0 to 2π`, while negative `Hz` values will reverse the direction, running from `2π to 0`.

<img src="img/nodes_reference/synth/phasor/phasor_tzfm.png"
alt="phasor tzfm"
width="800"/>


<br>

---


### sample & hold

<img src="img/nodes_reference/synth/sample_and_hold/sample_and_hold_node.png"
alt="sample and hold node"
width="200"/>

in | signal
:-- | :--
`in` | `any`
`trigger` | `gate`

out | signal
:-- | :--
`out` | `any`

exposable | ❌
:-- | :--


**description**

The `sample & hold` node will sample a value at its input on the rising edge of a `gate` signal at the `trigger` input and hold that value at its output until the `trigger` input is gated again.

You can think of it like a single-sample `memory` node.

In the `inspector` you can select the `Save Data` checkbox to save the held value in between patch loads.

<img src="img/nodes_reference/synth/sample_and_hold/sample_and_hold_inspector.png"
alt="sample and hold inspector"
width="200"/>

In the example below, on the top, a `phasor`-based sine generator is being sampled at `10Hz`, and underneath, the `sample & hold` node is sampling random values produced by a `random` node.

<img src="img/nodes_reference/synth/sample_and_hold/sample_and_hold_example.png"
alt="sample and hold example"
width="800"/>


<br>

---


### adsr

<img src="img/nodes_reference/synth/adsr/adsr_node.png"
alt="adsr node"
width="200"/>

in | signal
:-- | :--
`gate` | `gate`
`a` | `seconds`
`d` | `seconds`
`s` | `mod`
`r` | `seconds`

out | signal
:-- | :--
`out` | `mod`

exposable | ❌
:-- | :--


**description**

The `adsr` node outputs an envelope when the `gate` input is held `high`.

The `a` input is the attack time, `d` is decay time, `s` is sustain level, and `r` is release time.

As long as the `gate` input is held `high`, the output of the `envelope` node increases from `0` to `gate height` over `a` seconds, decreases to the `s` level over `d` seconds, then once the gate goes `low`, decreases from the `s` level back to `0` over `r` seconds.

Below you can see the `envelope` node going through its full cycle superimposed on the incoming `gate` signal.

<img src="img/nodes_reference/synth/adsr/adsr_cycle.png"
alt="adsr cycle"
width="800"/>


<br>

---


## module

**description**

The `module` nodes important elements for creating `modules` and `submodules`.

- The `module` node encases nodes into a `module` or `submodule`.
- The `input` and `output` nodes allow signals to flow into and out of `modules` and `submodules`.
- The `knob`, `xy pad`, `slider`, `toggle`, and `touch pad` are all elements you can interact with that you can set up to control what's going inside a `module`.


<br>

---


### module
### input
### output
### knob
### xy pad
### slider
### toggle
### touch pad



## poly
### combine
### split
### poly mix
### channel index
### channel count



## switch
### mux
### demux
### spigot