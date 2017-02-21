<style>
body {
  background-color: black;
  color: rgb(136, 136, 136);
  font-family: 'Input Sans', sans-serif;
}

img, video {
  max-width: 100%;
}

img[alt=icon] { 
  width: 100px;
  border: 2px solid #293E4D;
  border-radius: 5px;
}

h2 {
 color: #2a9fd6;
}

h3 {
 color: white;
}

h4 {
 color: white;
}

</style>

# Control Glossary

## Control Glossary


The following chart is a list of the most common Audulus control abbreviations. For more information on how a particular control works on a certain module, refer to the module's description.

Control | Meaning | Notes 
:------------- | :------------- | :------------- 
`+`  | Add | The Add control is module specific, meaning on an m2m converter, it will add at most 1, but on an m2o converter, it can add -4 to 4.  There is no subtract control because adding a negative number is subtraction.
`*`  | Multiply | The Multiply control is module specific, meaning on an m2m converter, it will multiply by most 1, but on an m2o converter, it will multiply by -1 to 1.  As you can probably tell, in most cases the multiply control really is a divide control, because you are multiplying by numbers less than 1.
`Ø`  | Phase | This knob controls the phase relationship between one signal and another.  The control may be scaled differently in each application, but is usually scaled to 0-90, 0-180, or 0-360 degrees.
`^v`  | Translate Up/Down | This is pretty much identical to the Add (+) control, but is used for clarity in some situations, like on the envelope module.
`<>`  | Shift Left/Right | This control may shift a collection of data left or right, or it can also be used to define a range of values.
`A`  | Attack | The Attack portion of an envelope, or how long the note takes to reach maximum volume before decaying to the level set by sustain.
`A/B` | Fade between A (left) and B (right) | This control is found on pan and crossfade modules, but also biased probability modules.  Turned to the left is "All A" and to the right is "All B" and in the middle is "half A, half B."
`BPF`  | Bandpass Filter Cutoff | Some modules have a built in band pass filter for tone shaping, and this control is the cutoff point of that filter.
`Clr`  | Clear | Clears out the held bit of memory or loop.
`D`  | Decay | The Decay portion of an envelope, or how long the volume of a note takes to drop to the level set by the sustain control.
`depth`  | Depth | Depth controls are used to indicate the level of modulation sent to an effect like a vibrato or tremolo.  Should not be confused with Mix, which can mean the "Depth" of any effect.
`det`  | Detune | Detune is present in VCOs or pitch effects, and it means to be detuned versus a reference pitch.  Turning a det knob does not detune the reference oscillator.  May also appear as (det)(une) over two knobs, or (de)(tu)(ne) over three knobs.
`drive`  | Drive | Drive is used to indicate the tanh(x) soft clipping expression, which gives a over-driven, tube-like sound.  Can also be used for other overdrive effects, but the tanh(x) expression is the most common.  Not to be confused with level, though drive can add significant volume.  When using drive in your designs, place it before a level control for more predictable results.
`fb`  | Feedback | Feedback is most often found on delays, and indicates the level of the delay output that is fed back into its input.
`fm`  | Frequency Modulation | An FM parameter adjusts the level of an incoming FM operator as it mixes with the original signal.
`Hz`  | Hertz (Frequency, Speed) | Hertz is cycles per second, and is related to pitch of oscillators, cutoff points in filters, and speeds of effects like tremolo or vibrato.
`HPF`  | High Pass Filter Cutoff | Some modules have a built in high pass filter for tone shaping, and this control is the cutoff point of that filter.
`L/R`  | Left/Right Delay Time | An L and R on a delay effect indicate that the delay is a stereo delay, and the L and R indicate the delay time for the left and right channels respectively.
`level`  | Level (Volume, Amount) | Level knobs are used to control an overall signal strength of an input or output.  Level controls should be the last control in a module for an output, or the first control in a module for an input.  Do not confuse with Mix or Depth.
`LPF`  | Low Pass Filter Cutoff | Some modules have a built in low pass filter for tone shaping, and this control is the cutoff point of that filter.
`max`  | Maximum | Maximum is often found on sequencers to indicate maximum step length, but can also be anywhere where a maximum signal level is defined.
`min`  | Minimum | Minimum is often found on sequencers to indicate minimum step length, but can also be anywhere where a maximum signal level is defined.
`mix`  | Mix | Mix indicates the balance between a dry signal (left) and an effected signal (right).  If the knob is set halfway, the mix between the signals is equal.  An equal power crossfade module should be used with mix controls.
`mode`  | Mode | Mode switches are module-specific, but in general, they are toggle switches that swap between two different types of operation.  Used when modulating the mode state with a control signal isn't a priority.
`NOT`  | Notch Filter Center Frequency | Some modules have a built in notch filter for tone shaping, and this control is the center frequency of that filter.
`oct`  | Octave | Octave controls set the octave of an oscillator or sequencer.
`out`  | Output | Generally only used for the main audio output, can also be used for a module's output, similar to a level control.
`PWM`  | Pulse Width Modulation | Pulse Width Modulation is the relationship of on to off time of square wave oscillators.
`Q`  | Q-Factor | Pulse Width Modulation is the relationship of on to off time of square wave oscillators.
`R`  | Release | Release is the amount of time an envelope takes to decay from the sustain level to 0 when its gate goes low.
`S`  | Sustain | Sustain is the level to which an envelope decays after the initial Attack-Decay period while its gate is still high.
`shape`  | Shape | Shape mostly indicates the amount of non-linearity applied to a signal.  For example, the shape control on the envelope fades from exponential (left) to linear (middle) to logarithmic (right).  In general, this knob is mostly used to shape control signals, though it can also be used for audio distortion effects.
`Tap`  | Tap | Tap is used for manually entering gate information, like on a tap tempo.  It is used for controls that are tapped, not held, so the control should always have the toggle option unchecked.
`width`  | Width | Width is used in stereo effects and controls the size of the stereo field.  In some applications, the width control will go from wide (left) to mono (middle) to swapped wide (right), where the stereo channels are reversed.
`xm`  | Cross Modulation | Cross Modulation is like a linear A/B crossfader between two (or possibly more) control signals or oscillators.  It's not the same as frequency modulation, where one oscillator is controlling the pitch of another.




















