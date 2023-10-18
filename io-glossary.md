**Input/Output Abbreviation Glossary**

Inputs and Outputs in the Audulus module library are labelled in a consistent way so as to make interfacing them easy to understand.  If you adopt this naming scheme in your own modules, when you share them, people will be able to use them more easily without needing extensive written instruction.  

Knob (k), Modulation (m), and Gate (g) signals can all be used to directly modulate any knob - however, be aware that attaching out of range signals to knobs (e.g., degrees, radians, octave) may cause a white-out connection (a NaN, feedback, or near-infinity number), or you may cause a significant jump in volume or resonance that could be painful or completely stop audio from processing.

All inputs and outputs in Audulus are 32 bit floating point numbers.  Unlike other digital modular synths, Audulus does not distinguish between different signal types.  This means audio can be used as a switching or triggering signal, and triggers can be used as audio.  

However, having different signal types is useful, so we have created rules for what those types of signals are.  This is a glossary that lays out all of the different types of inputs and outputs you'll see in this module collection.  

Within this library, types of signals have been constrained into ranges that interface well with both nodes and the modules created with them.  Many node controls range from 0 to 1, so Modulation (m), Knob (k), Gate (g), and Envelope (e) signals are also tuned to this range.  

These signals are also tuned to a 0-1 range so that they interface well with one another.  

Audio is an alternating signal, and so it ranges between -1 and 1.  If you send a direct signal that goes from 0-1 to your speakers, you will only be pushing the speakers halfway through their cycle.  The library's master audio output has a built-in DC-blocker node that converts DC signals to AC, so if you use this module, you won't really need to consider this.  

Because pitch is logarithmic in scale, Audulus modules use the Octave (o) signal (1/oct) which allows you to more easily do linear math to effect pitches.  This means to octave shift up, add 1, and to octave shift down, subtract 1.  This also means Vibrato will scale better using Octave scaling versus scaling Hz.


**Abbreviation:** a 
**Meaning:** Audio  
**Signal Range:** -1 to 1

*Denotes an audio path signal - keep within -1 to 1 range to prevent output clipping.*

**Abbreviation:** d  
**Meaning:** Degrees  
**Signal Range:** 0 to 360

*Useful for indicating phase relationships*

e - red light - Envelope - 0 to 1 - 

*Indicates an envelope input - found most often on oscillators.*

g - light node - Gate - 0 or 1* - 

*Gate signals are on/off signals that act mostly as switches and triggers.  Logic expressions and other nodes that react to gates generally react to the rising edge of the gate - the moment the gate changes from low (0) to high (1).  In many applications, it would not matter if the high signal was 100 or 1000, but the low signal must always be 0.  To keep things simple and analogous to digital logic, the high signal is considered to be 1.  Although in Audulus a gate and a pulse are derived similarly, consider a gate as a signal with adjustable pulse width and a pulse as gate with a very short "hard-coded" pulse width like the One Frame Pulse module under Modules -> Utilities.*

**exception: an envelope responds to gate value, which allows for dynamics*

H/L - n/a - High/Low - 

*Any 32-bit number - Sets the high and low values of a range of numbers.*

Hz - n/a - Hertz (cycles per second) - 0 to Sample Rate - 

*Hz values are generally used for directly entering precise values for filters, oscillators, or clocks.  Hz values in general should not be negative (that would be time travel), or larger than sample rate.*

k - n/a - Knob - 0 to 1 - 

*Knobs are kept 0-1 to interface easily with Modulation (m) signals.  When their range needs to be translated, this is done inside the module with math or one of the knob modules.*

L/R - n/a - Left/Right - -1 to 1 - 

*Stereo audio signals are denoted by the letters L/R.  You do not have to use them as stereo signals, but if you connect L to L and R to R, you can be assured of proper stereo imaging.*

m - red light - Modulation - 0 to 1 - 

*Modulation signals are all 0 to 1 so that they interface easily with the knobs in this library, which are all also 0 to 1.  LFOs and envelopes are examples of modulation signals.  When a knob's range needs to be translated, it is done so inside the module.*

o - n/a - Octave (1 per octave centered at 0) - -4 to 4 - 

*1/octave signals work a little differently than 1v/oct modular signals.  In our case 0 = reference pitch hwich defaults to A=440 Hz.  Inputting a 1 transposes up one octave (880 Hz), inputting -1 transposes down one octave (220 Hz).  All oscillator modules are configured to accept only o signals, and effects are generally based on manipulating o signals (like vibrato).*

r - n/a - Radians - 0 to 2pi - 

*The Phasor node outputs Radians.  Useful in trigonometric functions.*

:# - n/a - Number - 

*Any 32-bit number - Number signals are non-specific numbers - most often used for counting, but can be anything.*

:- - (negative sign in light) - Inverse - Inverse of the adjacent signal - 

*This indicator is used to show that the output is an inverted version of an adjacent signal, and is usually placed to the left of the uninverted signal.*

:> - n/a - Any Signal - Any 32-bit Number - 

*This symbol is used for inputs and outputs with non-specific signals.  You'll find these often on switches or routing modules.  They are also featured on distortion modules because disortion is useful for shaping modulation signals as well as audio.*
























