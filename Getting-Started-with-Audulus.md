<img src="img/Audulus_logo.svg" style="width: 200px;"/>

### Welcome to Audulus!

<div class="tagline">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audulus. A Modular Audio Processing App for iPad, iPhone, Mac, Linux, and Windows. Created by Developer Taylor Holliday. Promoted by Mark Boyd, Audulus Evangelist.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;With Audulus, you can build synthesizers
from first principles, design new sounds, or process audio &mdash; all with
real-time, low-latency processing suitable for live performance.
</div>

<br>
To get started, begin with the UI Basics for your platform (<a href="#ui-basics-ipadiphone">iOS</a> or <a href="#ui-basics-mac">Mac/Windows</a>).

### Join the Audulus Mailing List

First, be sure to sign up for the Audulus mailing list!

<!-- Begin MailChimp Signup Form -->
<div id="mc_embed_signup">
<form action="//audulus.us9.list-manage.com/subscribe/post?u=2c81276aefb1edcfbb9934c74&amp;id=aae8478e6c" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">

<div class="mc-field-group">
	<label for="mce-EMAIL">Email Address </label>
	<input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
</div>
	<div id="mce-responses" class="clear">
		<div class="response" id="mce-error-response" style="display:none"></div>
		<div class="response" id="mce-success-response" style="display:none"></div>
	</div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_2c81276aefb1edcfbb9934c74_aae8478e6c" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>

<!--End mc_embed_signup-->

We will send you information about new Audulus features, and updates from the Audulus community.

# What is Audulus?

Audulus is a modular synthesizer visual programming environment for iOS, Mac, Windows, and Linux.

Audulus gives you the tools to create your own custom synthesizers, sequencers, filters, and effects.

### What is a modular synthesizer?

A modular synthesizer is a flexible type of synthesizer.

Most synthesizers have a fixed signal flow like this:

`Oscillator > Filter > Amplifier`

Modular synthesizers allow you to rearrange the signal flow, like this:

`Oscillator > Amplifier > Filter`

You can do this because in a modular synthesizer, each module has inputs and outputs that can be connected together in different ways with patch cables.
 What is visual programming?

Visual programming is similar to modular synthesis in this way.

Visual programming uses patch cables to connect little packets of code called “nodes.”

Just as each synthesizer module has hidden behind it a collection of electronic components, nodes have hidden inside them a collection of text code.

By linking these nodes together, you create a program that Audulus compiles and runs in real time, as if you had created the synthesizer from scratch yourself.

### What does Audulus run on?

Audulus is an iOS app that runs on both iPhone and iPad. Buying one iOS license allows you to use Audulus on both your iPhone and iPad simultaneously.

Audulus is also a standalone program that runs on Mac, Windows, and Linux computers. Mac and Windows/Linux licenses must be purchased separately.

Audulus is also a plugin that you can use with any DAW. Mac users get an AU while Windows and Linux users get a VST.

Audulus files are universal. This means you can create something on an iPad and later open it on your Mac or PC, or vice versa.

The major difference between these versions is the visual interface. Otherwise, Audulus runs identically on all platforms.



# Is Audulus difficult to use?

In a word: No. You can create all sorts of beautiful self-playing patches with gorgeous tones and complex sequences with just a little knowledge about synthesis.

That said, Audulus is very powerful, and a little understanding of both math and computer science can help you realize just how powerful it is.

Good thing is, Audulus helps you learn these concepts as you go in a fun, free-form way.

### Are there any tutorials?

There is a growing library of Audulus tutorials catalogued in the Audulus forum.

There are several in-app tutorials as well as many video tutorials that demonstrate how to use Audulus from a beginner to advanced level.

Join the weekly Audulus Tutorial Livestreams to have a chance to ask your questions in realtime. If you miss out on the livestream, you can always watched the archived footage.

### How do I get help?

Support for Audulus is easy to get and available in three different places.

Email us at support@audulus.com and we will respond usually within 24 hours. If you email us for help, please attach the patch you need help with to your email.

Join our Slack support channel. This requires you to have a Slack account, but it’s free to use. This is a good way to get help in real time.

Post your question on the Audulus forum. This is the fastest way to get help as we have a very active forum userbase that is friendly and ready to help.

### How do I report a bug?

If you feel like you’ve run into a bug, please do not post about it on the forum. We try to keep the forum focused on how to use Audulus, not troubleshoot it.

Instead, please email us at support@audulus.com. Include  the patch where you encountered the bug and explicit steps to reproduce the issue.

For most, Audulus runs totally problem-free. But when you do encounter a bug and report it, know that we always work as quickly as possible to fix it.

Providing clear reproducible steps to make the bug happen goes a long way to fixing the issue quickly.


# What are Audulus’ rules & conventions?

Below is a list of basic information about how Audulus works, what signals are and how they’re generated, and how to connect everything together.

### What is the Audulus Canvas?

When you open a new patch in Audulus, you will be presented with a blank screen. This blank background is called the Canvas.

To get going, tap on the background and press Create (iOS) or right click (Computer) and navigate to a node or module.

To explore the Canvas, you’ll need to create at least two nodes and separate them a little. Once you’ve done that, you’ll be able to pinch-to-zoom (iOS) or use the mouse wheel to zoom in and out.

The Canvas is virtually infinite. This means you will run out of CPU or GPU computing power before you ever filled up the entire space of the Canvas.

Subpatch nodes allow you to create a Canvas-within-a-Canvas to separate parts of your design.

Subpatch nodes can even be nested within themselves, though you’ll rarely see a module that uses more than 4 or 5 layers.

At a coding level, Audulus patches use a coordinate system to keep track of the location of nodes and modules.

The (0,0) origin point is directly in the middle of the screen when you open a new patch for the first time. It’s not necessary for you to keep track of these coordinates; this is done automatically.

But if, for example, you copy and paste a group of nodes from one patch to another, they will appear at the same coordinates as they were in the previous patch. This explains why sometimes the pasted group of nodes will seem to appear far off screen.

This coordinate system also applies to the UIs of subpatches. When exposing elements to the UI of a subpatch, it’s generally best to move them a little ways away from this origin point.

If you do not, you may create a new UI element later and it will appear directly in the middle of your UI, forcing you to rearrange things.

### What are signals in Audulus?

Signals are the information that flows between nodes. There are two basic types of signals.

Audio signals are the sound you would hear coming out of your speakers or headphones.

Control signals are used to modify effect parameters, like the loudness of an oscillator, or the cutoff of a filter.

All signals are a just stream of numbers.

The numbers move past any given input or output at the sample rate.

This means at a sample rate of 44.1kHz, 44,100 numbers move past any point in Audulus’ signal flow a given second.

So, for example, a string of numbers exiting an oscillator node might look like this:

`Sample 1: .00001`

`Sample 2: .00023`

`Sample 3: .00045`

`Sample 4: .00067`

At a sample rate of 44.1kHz, those four numbers would exit the oscillator in nine hundred thousandths of a second (0.00009).

`Number of Samples / Sample Rate = Total Time in Seconds`.

The bit depth indicates how accurate a number can be. Audulus uses 32 bit numbers.

### How do signals flow in Audulus?

Signals  flow from left to right; from outputs to inputs.

Inputs include the red Input node as well as the Knob node.

When a signal is attached to the center of a Knob node, the knob will turn blue and animate the signal controlling it.

When a signal is 0, the wire is colored blue. When the signal is -1 or below or 1 or above, the wire is colored red. Between -1 and 1, the red and blue colors mix.

In general, audio signals will look purple whereas control signals will alternate between blue and red.

A single output can be patched to multiple inputs, but a signal input can only recieve one output.

To combine two or more outputs together to feed one input, you must use addition (e.g., an Add node or a mixer).

A node’s output can be connected to its own input. This is called feedback.

If the feedback goes out of control (expands quickly towards infinity), Audulus will automatically halt the audio engine to prevent damage to your speakers or hearing.

To reset the patch, remove the problematic feedback path, and then close and reopen Audulus.

### How to signals enter and exit Audulus?

Audio and control signals enter and exit Audulus through the Mic and Speaker nodes, as well as the ADC and DAC nodes.

The Mic and Speaker nodes are the same as ADC/DAC channels 1 and 2. The ADC/DAC nodes are most useful to people using Audulus in conjunction with hardware synthesizers through a DC-Coupled audio interface, such as the Expert Sleepers ES-8 Eurorack module.

The maximum input and output range for audio and control voltages is -1 to 1. Values outside this range will be hard-clipped.

The Keyboard node will translate incoming Midi signals into Hz (pitch) and Gate (note on/off) signals.

Knob and Trigger nodes can also be directly controlled by Midi. Tap or right click on the Knob or Trigger and select Learn Midi CC (Knob) or Learn Midi Note (Trigger).

The mapped Knobs and Triggers will animate when you turn or press their corresponding control.

### What are the conventional signal ranges for audio?

Audio signals should generally be kept between -1 and 1. This is because when a signal exits Audulus, it must be within that range, or it will be clipped, causing distortion.

However, there are many cases when you would want an audio signal to exceed the -1 to 1 range while still within Audulus.

One such example is driving an audio signal into a hypertangent expression, which mimics soft clipping tube distortion.

`Audio*100` >> `tanh(x)`

Before the audio signal enters the tanh(x) expression, it could be swinging from -100 to 100. (Conveniently, the output of a hypertangent function will never be outside -1 to 1.)

### What are the conventional signal ranges for control signals?

Control signals should always be kept between 0 and 1. This is for two reasons. The first is when a signal exits Audulus, it must be within a -1 to 1 range, or it will be clipped, causing distortion.

The second reason why control signals should be kept between 0 and 1 is for compatability reasons.

First off, many Audulus nodes have inputs that work within the 0 to 1 range. The c input of the Crossfade node, color inputs on the RGB node, and the resonance of the Filter node all expect a range of 0 to 1.

Exceeding this range in either a positive or negative direction can cause these nodes to behave unpredictably.

Secondly, and most importantly, when a Knob node is created, its default range is 0 to 1. If knobs are left in this default range, then all control signals will interact with knobs predictably.

If you want to use a Knob node to control the pitch of an oscillator you are making, you could change the range of the Knob node directly to 20 to 20,000 and attach that to the Hz input of the oscillator.

However, if you wanted to then modulate the knob with an envelope that outputs a signal of 0 to 1, you would have to translate the 0 to 1 envelope output to the 20 to 20,000 range.

Worst of all, if someone else made the module, you wouldn’t be able to tell what range each knob was until you inspected the Min and Max values yourself.

Instead, use an Expression node to range the knob internally, like this:

`0 to 1 Knob` >> `Knob*19980+20`

`0*19980+20 = 20`

`1*19980+20 = 20000`

Another advantage of keeping the Knob node at its default 0 to 1 range is that you can apply curves to a knob’s response.

For example, the cutoff knob for a filter works best if it is scaled exponentially. A linear knob at its halfway point would be around 10kHz which is far above the most typical musical range of a filter.

An exponential knob might have a curve where its halfway point would be around 5kHz, and yet it would still cover the same 20Hz to 20kHz range as the linear knob.

To apply an exponential response to a Knob node, you can square the knob (multiply it by itself).

`Knob*Knob*19980+20`

`Knob^2*19980+20`

To apply a logarithmic response to a Knob node, you can square root its output.

`sqrt(Knob)*19980+20`

You cannot easily apply these curves to knobs if you do not keep the output of the signal between 0 and 1.


# iOS User Interface Basics

### What happens when I open Audulus?

When you open Audulus on an iOS device for the first time, after a brief logo animation, Audulus will ask for permission to access the microphone.

Select OK to enable the audio inputs.

You will not have to do this again unless you uninstall and reinstall Audulus.

Next, you will be presented with the Patch Browser.

### What is the Patch Browser?

The Patch Browser keeps your Audulus files organized.

The files you create with Audulus are called patches.

Modular synthesizers use patch cables to connect synthesizer modules together. Connecting modules with these cables is called “patching.” A modular synthesizer “patch” refers to a particular way the synth is wired and configured.

In Audulus, the term “patch” is used more loosely. An Audulus patch can be anything: a synthesizer, an audio effect, a drum machine, or even an entire self-playing musical performance.

Audulus patches end with the file extension “.audulus.”

You can create as many Audulus patches as your device’s storage will allow.

Audulus comes with several example patches for you to explore.

Note: These examples may change from update to update.

### How do I navigate the Patch Browser?

To navigate the Patch Browser, tap and drag up or down on the screen.

### How do I search in the Patch Browser?

To search the Patch Browser, tap and pull down on the screen until the Search Bar appears.

The Search Bar will dynamically limit results as you type. This means if you begin typing “a…” all of the patches that contain the letter “a” will appear below.

To cancel your search, press the “Cancel” icon next to the Search Bar.

### How do I sort patches in the Patch Browser?

To sort patches by date created or by name, tap and pull up on the screen until the Date/Name icon appears in the upper right of the screen, just below the Edit icon.

Patches are sorted by oldest to newest in Date mode, and #-A-Z in Name mode.

### How do I browse by tags in the Patch Browser?

To browse patches by tags, tap and pull up on the screen until the tag list appears below the search bar. Tap on a tag, and all of the patches with that tag will appear. Tap on the tag again to unlimit the search. Multiple tags can be selected at once if patches have more than one tag.

### How do I open patches?

To open a patch, tap on the patch’s screenshot.

Tapping on the patch’s name will open the patch metadata; not the patch.

### How do I create a new patch?

To create a new patch, tap the + symbol in the top left. A small window will appear with two options: “New Patch” and “iCloud Drive.”

Tapping “New Patch” will create a blank patch.

Tapping “iCloud Drive” will allow you to load an existing patch from your iCloud drive.

### How do I save a patch?

Patches are automatically saved whenever you exit the Patch Editor.

Note: Thanks to Audulus’ infinite undo system, if Audulus crashes or your device loses power, your progress will still be saved.

### How do I rename patches?

To rename a patch or edit the patch’s metadata (tags, description, author), tap directly on the title of the patch. A window with all of the patch’s information will appear.

### How do I email a patch?

To email a patch, tap “Edit” in the top right of the screen, tap on the patch you want to send, and then tap the iOS “send” icon in the top left. You can select multiple patches at once.

When you are finished, tap “Done” in the top right of the screen.

Note: Although iOS gives you the option of sending .audulus files through Messenger, the person you send them to will not be able to download them.

This is a quirk of iOS and not something we can fix on our end.

### How do I duplicate a patch?

To duplicate a patch, tap “Edit” in the top right of the screen, tap on the patch you want to duplicate, and then tap the duplicate icon second from the left.

You can select multiple patches at once. When you are finished, tap “Done” in the top right of the screen.

### How do I delete a patch?

To delete a patch, tap “Edit” in the top right of the screen, tap on the patch you want to delete, and then tap the trash can icon third from the left.

You can select multiple patches at once. When you are finished, tap “Done” in the top right of the screen.

### How do I turn on background audio?

To turn on background audio, tap the wrench icon and tap the slider next to “Background Audio.”

This will allow Audulus to continue producing sound even when you switch to another app.

If you want to use Audulus with another app like AUM or Audiobus, you must have background audio turned on.

### How do I store my patches automatically in iCloud?

To store your patches in your iCloud drive, tap the wrench icon and tap the slider next to “Store Patches in iCloud.”

If you already have patches stored in your iCloud drive, once you turn this on, they will begin to download.

If you have patches in your patch browser that are not saved to your iCloud drive, they will be uploaded to your drive.

When you edit and exit a patch, your changes will be synced to your iCloud drive.

Be aware that if you are not connected to a WiFi network, your patches may download over your wireless carrier.

You can open the same patch on more than one device. To prevent version confusion, iCloud will only sync the patch that was opened first.

### What is the Patch Editor?

The Patch Editor is where you create, edit, and perform with your Audulus patches.

Only one patch can be opened at a time.

### How do I open the Patch Editor?

To open the Patch Editor, tap on the screenshot of an existing patch, or create a new patch by tapping on the + icon in the top left corner of the Patch Browser.

Note: if you cannot see the + icon, you are probably in Edit mode. To exit Edit mode, tap on the Edit icon in the top right of the Patch Browser.

### What happens when I create a new patch?

When you create a new patch, you will be presented with a blank screen that says, “Empty Patch. Tap to create a node.”

### What is the black background of the Patch Editor?

The background in the Patch Editor is called the Canvas.

The Canvas dynamically adapts to the size of your patch.

If you have only one node or module loaded on your Canvas, you will not be able to zoom out very far.

If you have two nodes or modules loaded, and they are spaced apart, you have more freedom to zoom out.

### How do I exit the Patch Editor?

To exit the Patch Editor, tap the “Exit” icon in the top left of the screen.

### How do I use the on-screen Midi keyboard?

To reveal the on-screen touch keyboard, tap the chevron in the bottom left of the screen.

To hide the keyboard, press the chevron again.

To change the octave of the on-screen touch keyboard, tap the up or down arrows above and below the number 0.

In Audulus, the 0th octave represents the middle octave, e.g., the A in the 0th octave in Audulus is A=440Hz.

The maximum range is -3 to 3. To understand why this is, refer to the Octave Signal in the Glossary at the end of this Getting Started guide.

### How do I lock nodes and modules in place?

To lock nodes and modules in place, tap the padlock icon. This will put Audulus into Performance mode.

Performance mode allows you to zoom, pan, turn knobs, connect and disconnect wires, and push buttons without accidentally moving anything.

### How do I see how much CPU time each node or module is using?

To examine individual node and module CPU timing, tap the Timing icon.

In Timing mode, you can see what percent of a CPU cycle each portion of your patch is using.

Nodes will not use any CPU time unless they are connected to one of the meter nodes or to an audio output.

Nodes will also not animate unless they are connected to a meter node or an audio output.

For example, if you turn the knobs of the ADSR node, the graphic illustrating the envelope shape will not change until the ADSR node has been attached to a meter node or audio output.

Note: The Subpatch Output node is not an audio output.

### What is the CPU:% display in the bottom right of the screen?

The CPU:% display in the bottom right of the screen shows what percent of your device’s central processing unit’s (CPU) cycle is being used by your patch.

In a given CPU cycle, only a certain number of calculations can be made.

The faster your CPU, the more calculations can be made. This means you can open larger, more complex patches on an iPad Pro than you could on an iPhone 5s.

Every node or module you add increases the number of calculations that are computed per cycle.

Other music apps with background audio turned on will also increase CPU usage.

However, this will not be reflected in the CPU:% meter in Audulus. This meter only shows how much CPU the current patch is using.

If you do not have any other music apps running and the CPU usage reads 70% or above, you may hear occasional dropped samples, which sound like crackling.

This is not a bug: It just means that your device may not be fast enough to run the patch.

It is possible to have CPU usage times greater than 100%.

This happens most often when you try to load a patch that was created on a more powerful device.

### What are the Canvas functions?

Canvas functions are accessible by tapping on the Canvas; i.e., any blank space not occupied by a node or module.

### How do I create a node or module?

To create a node or module, tap on the Canvas and press “Create.” This will bring up the Module Browser (see below).

### How do I connect nodes and modules to one another?

Nodes and modules are connected together by wires called patch cables.

To connect one node or module to another, tap on a blue output. As you drag away from the output, a wire will appear under your finger.

Without lifting your finger, drag the wire to the red input of the node or module you want to connect to.

When you are above an Input node and ready to connect, it will grow larger around your finger.

To make the connection, let go of the wire.

To break a connection, tap on the Input node and swipe the wire away. You do not need to lead the wire all the way back to the output node.

Wires can also be directly connected to the knobs of Knob, Constant, and Level nodes as if they were Input nodes.

Disconnecting a wire from a knob works the same way: By tapping, dragging, and releasing the wire away from the knob.

Knob nodes can only be connected to when the Knob node is inside a Subpatch node.

Wires will only connect to the Knob as they appear on the UI of the Subpatch node - not inside the Subpatch node.

When a wire is connected to a Knob node, it can only be disconnected from outside the Subpatch node in which it’s contained.

### How do I select a node or module?

To select a node or module, tap on a blank space (i.e., not on an input, output, or control).

When a node or module is selected its border will change from a thin grey line to a thick pinkish red line.

### How do I lasso select multiple nodes and modules?

To lasso a selection of nodes and/or modules, tap on the Canvas and drag around whatever you want to select.

### How do I select all nodes and modules?

To select all of the elements in a patch, tap on the Canvas and press “Select All.”

### How do I pan?

To pan, tap and drag two fingers around the Canvas.

### How do I zoom in and out?

To zoom in or out, use the iOS pinch-to-zoom gesture.

### How do I zoom out so that everything on the Canvas fits in the screen?

To zoom to fit so that everything in your patch appears on screen at once, tap the Canvas and select Fit.

### How do I undo an action?

To undo an action, tap the Canvas and press “Undo.”

Audulus has an infinite undo feature that persists even when the patch is closed.

### How do I clear the patch history?

To clear the patch history, tap on the Canvas and press Clear History.

All of the changes you make are kept track of in the patch history.

If you are satisfied with a patch and know that you do not want to revert to a previous state, clearing the history will shrink the file size.

### What are node and module functions?

Node and module functions are accessible by tapping on any blank space in a node or module.

If your screen is small or you tap near the edge of the screen, the Context Menu may be truncated.

This is indicated by a > icon. Pressing the > icon will reveal more functions.

Alternately, you can zoom out and try pressing on the node or module again.

### How do I cut a module?

To cut a node or module, tap and press Cut.

You can then paste it somewhere else. If you have multiple nodes or modules selected, all of them will be cut.

### How do I copy a module?

To copy a node or module, tap and press Copy.

You can then paste a copy of it somewhere else. If you have multiple nodes or modules selected, all of them will be copied.

### How do I paste a module?

To paste a node or module, you must have first cut or copied. Once you have, tap on the canvas and press “Paste.”

Note: You can cut/copy/paste between patches. This means if you have a portion of a patch you want to reuse in a new patch, you can select it, copy it, enter a new patch, and paste it in.

### How do I get help on using a node?

To get help about a particular node, tap on it and press Help.

Note: The Help function requires an internet connection.

### How do I delete a node or module?

To delete a node or module, tap on it and press Delete.

If you have multiple nodes or modules selected, all of them will be deleted.

### How do I group nodes and modules into a new Subpatch node?

To group a selection of nodes and/or modules into a Subpatch node, tap them and press Group.

If the selection being grouped has inputs and/or outputs outside of the selection range, these connections will be preserved with automatically generated and labeled Input/Output nodes.

### What are module functions?

Module functions are accessible by tapping on any blank space in a module.

They are specific to modules (i.e., Subpatch nodes).

If your screen is small or you tap near the edge of the screen, the Context Menu may be truncated. This is indicated by a > icon. Pressing the > icon will reveal more functions.

Alternately, you can zoom out and try pressing on the node or module again.

### How do I enter and exit a module?

To enter a module, tap on it and press, Open.

To exit, press the Exit icon in the upper left corner.

### How do I edit the UI or front panel of a module?

To edit the UI (User Interface) of a module, tap it and select Edit UI.

You can then drag and position nodes and exposable elements (e.g., oscillator waveshape, lights, meters) wherever you want.

The border of the Subpatch node will resize to accommodate whatever it contains.

There is a rudimentary layer system that makes whatever element was created most recently rise to the top.

To pull an element above another one, enter the subpatch, find the element you want to be on top, cut it, and then and paste it.

Audulus will consider the pasted node to be a new node, and so it will rise to the top.

The node will reconnect to any of its inputs, but this will break output connections, if any; so remember to reconnect them.

### How do I stop editing the UI of a module?

To stop editing the UI of a module, tap the module and select Lock UI.

This will prevent nodes and exposable elements from moving around and allow you to interact with controls and draw wires to and from inputs and outputs.

### How do I add my own modules to the Module Browser?

To add a module to the module browser, tap on it and press, Add Module.

### What are node functions?

Many nodes have specific contextual functions.

These functions are accessible by tapping on any blank space in the node.

If your screen is small or you tap near the edge of the screen, the Context Menu may be truncated. This is indicated by a > icon. Pressing the > icon will reveal more functions.

Alternately, you can zoom out and try pressing on the node or module again.

### What are the Expression node’s functions?

To edit an expression node, tap it and press Edit.

A box labeled Enter Expression will appear and you can then use the keyboard to change the expression.

### What are the Text node’s functions?

To edit a Text node, tap it and press Edit.

A box labeled Edit will appear and you can then use the keyboard to change the text.

### What are the Knob and Constant nodes’ functions?

To change the minimum value of a Knob or Constant node, tap directly on the knob and press Set Min.

A box labeled Set Min will appear and you can then use the keyboard to change the minimum value.

To change the maximum value of a Knob or Constant node, tap directly on the knob and press Set Max.

A box labeled Set Max will appear and you can then use the keyboard to change the maximum value.

To set the value of a Knob or Constant node, tap directly on the knob and press Set Value.

A box labeled Set Value will appear and you can then use the keyboard to change the current value.

To assign a MIDI CC to a Knob or Constant node, tap directly on the knob and press Learn Midi CC.

Next, twist, push, or slide the corresponding control of a plugged-in MIDI interface, and the controls will be linked.

Note: These functions also apply to the knobs on the ADSR node. The exception is that the minimum value for any given knob should be no less than 0 (time parameters cannot be negative).

### What are the Trigger node’s functions?

To turn a momentary Trigger node into a toggle switch, tap on a blank space on the node and press [ ] Toggle.

To turn a toggle Trigger node into a momentary switch, tap on a blank space on the node and press [X] Toggle.

To assign a MIDI note to the Trigger node, tap on a blank space on the node and press, Learn Midi Note.

### What is the Module Browser?

The Module Browser is where all of the nodes and modules are collected.

### How do I open and close the Module Browser?

You can enter the Module Browser by tapping the Canvas and pressing Create.

To exit the module browser without creating a new node or module, press Cancel.

The Cancel icon is at the top right of the red bar in the Module Browser window.

The Module Browser will also automatically close if you select any node or module.

### How do I sort the Module Browser by tags?

In the top of the module browser is a red bar. In this bar is a list of tags. Tags are listed in alphabetical order.

To sort nodes and modules by tags, press on one or more of the tags. Some modules may have multiple tags.

To cancel sort by tags, deselect the tags you have pressed.

To browse the tags, swipe over the Tag Bar.

### How do I browse the nodes and modules?

When you open the module browser, nodes are listed first.

There are 52 nodes. All nodes have a graphical illustration.

Modules, on the other hand, have an automatically generated in-app screenshot.

### How do I create a node or module?

To create a node or module, tap on it. The Module Browser will close and the node or module you selected will appear on the canvas.

To learn more about each module, tap on its name.



# Mac, Windows, & Linux User Interface Basics

### What happens when I open Audulus on a computer?

When you open Audulus on an computer, you will be presented with a file browser window.

The files you create with Audulus are called patches.

Modular synthesizers use patch cables to connect synthesizer modules together. Connecting modules with these cables is called “patching.” A modular synthesizer “patch” refers to a particular way the synth is wired and configured.

In Audulus, the term “patch” is used more loosely. An Audulus patch can be anything: a synthesizer, an audio effect, a drum machine, or even an entire self-playing musical performance.

Audulus patches end with the file extension “.audulus.”

You can create as many Audulus patches as your device’s storage will allow.

Audulus comes with several example patches for you to explore.

These example patches are accessible through the menu File > Open Example.

Note: These examples may change from update to update.

### How do I open patches?

You can open an Audulus patch from the file browser that appears when you open Audulus; from the Audulus File menu; or by double clicking on a patch file without having first opened Audulus.

### How do I create a new patch?

To create a new patch, go to File > New.

Alternately, you can use the shortcut Command+N.

### How do I save a patch?

To save a patch, go to File > Save.

Alternately, you can use the shortcut Command+S.

Note: Thanks to Audulus’ infinite undo system, if Audulus crashes or your device loses power, your progress will still be saved.

### How do I rename patches?

To rename a patch, click on the chevron next to the patch name in the Patch Editor window.

You can also rename the patch file just as you would any other file on your computer from a file browser.

### How do I email a patch?

To email a patch, simply attach the patch to an email as you would any other email attachment.

### How do I duplicate a patch?

To duplicate a patch, go to File > Duplicate.

Alternately, you can use the shortcut Shift+Command+S.
You can select multiple patches at once. When you are finished, tap “Done” in the top right of the screen.

### How do I delete a patch?

To delete a patch, tap “Edit” in the top right of the screen, tap on the patch you want to delete, and then tap the trash can icon third from the left.

You can select multiple patches at once. When you are finished, tap “Done” in the top right of the screen.

### How do I store my patches automatically in iCloud?

To store your patches in your iCloud drive, tap the wrench icon and tap the slider next to “Store Patches in iCloud.”

If you already have patches stored in your iCloud drive, once you turn this on, they will begin to download.

If you have patches in your patch browser that are not saved to your iCloud drive, they will be uploaded to your drive.

When you edit and exit a patch, your changes will be synced to your iCloud drive.

Be aware that if you are not connected to a WiFi network, your patches may download over your wireless carrier.

You can open the same patch on more than one device. To prevent version confusion, iCloud will only sync the patch that was opened first.

### What is the Patch Editor?

The Patch Editor is where you create, edit, and perform with your Audulus patches.

Multiple patches can be opened at the same time.

When multiple patches are opened, they are tabbed in the Audulus window.

### How do I open the Patch Editor?

To open the Patch Editor, open an existing patch, or create a new one.

### What happens when I create a new patch?

When you create a new patch, you will be presented with a blank screen that says, “Empty Patch. Tap to create a node.”

### What is the black background of the Patch Editor?

The background in the Patch Editor is called the Canvas.

The Canvas dynamically adapts to the size of your patch.

If you have only one node or module loaded on your Canvas, you will not be able to zoom out very far.

If you have two nodes or modules loaded, and they are spaced apart, you have more freedom to zoom out.

### How do I use the on-screen Midi keyboard?

At the time of this writing, there is no on-screen keyboard or musical typing in the computer version of Audulus.

There is, however, a user-made keyboard module that can perform the same function.

You can download this keyboard module here:

http://forum.audulus.com/discussion/1093/keyboards-for-mac/p1

### How do I lock nodes and modules in place?

At the time of this writing, there is no lock mode for the computer version of Audulus.

### How do I see how much CPU time each node or module is using?

To examine individual node and module CPU timing, go to View > Execution Times.

Alternately, press T to toggle Timing mode on and off.

In Timing mode, you can see what percent of a CPU cycle each portion of your patch is using.

Nodes will not use any CPU time unless they are connected to one of the meter nodes or to an audio output.

Nodes will also not animate unless they are connected to a meter node or an audio output.

For example, if you turn the knobs of the ADSR node, the graphic illustrating the envelope shape will not change until the ADSR node has been attached to a meter node or audio output.

Note: The Subpatch Output node is not an audio output.

### What is the CPU:% display in the bottom right of the Patch Editor?

The CPU:% display in the bottom right of the Patch Editor shows what percent of your device’s central processing unit’s (CPU) cycle is being used by your patch.

In a given CPU cycle, only a certain number of calculations can be made.

The faster your CPU, the more calculations can be made. This means you can open larger, more complex patches on an iMac Pro than you could on an Mac Mini.

Every node or module you add increases the number of calculations that are computed per cycle.

Other programs running on your computer will also increase CPU usage.

However, this will not be reflected in the CPU:% meter in Audulus. This meter only shows how much CPU the current patch is using.

If you do not have any other applications running and the CPU usage reads 70% or above, you may hear occasional dropped samples, which sound like crackling.

This is not a bug: It just means that your device may not be fast enough to run the patch.

It is possible to have CPU usage times greater than 100%.

This happens most often when you try to load a patch that was created on a more powerful device.

### What are the Canvas functions?

Canvas functions are accessible by right-clicking on the Canvas; i.e., any blank space not occupied by a node or module.

### How do I create a node or module?

To create a node or module, right-click on the Canvas and navigate through the Module Browser menu  and click on a node or module.

### How do I connect nodes and modules to one another?

Nodes and modules are connected together by wires called patch cables.

To connect one node or module to another, click and hold on a blue output. As you drag away from the output, a wire will appear under your finger.

Without letting go of the mouse button, drag the wire to the red input of the node or module you want to connect to.

When you are above an Input node and ready to connect, it will grow larger around your cursor.

To make the connection, let go of the mouse button.

To break a connection, click on the Input node and swipe the wire away. You do not need to lead the wire all the way back to the output node.

Wires can also be directly connected to the knobs of Knob, Constant, and Level nodes as if they were Input nodes.

Disconnecting a wire from a knob works the same way: By clicking, dragging, and releasing the wire away from the knob.

Knob nodes can only be connected to when the Knob node is inside a Subpatch node.

Wires will only connect to the Knob as they appear on the UI of the Subpatch node - not inside the Subpatch node.

When a wire is connected to a Knob node, it can only be disconnected from outside the Subpatch node in which it’s contained.

### How do I select a node or module?

To select a node or module, click on a blank space (i.e., not on an input, output, or control).

When a node or module is selected its border will change from a thin grey line to a thick pinkish red line.

### How do I lasso select multiple nodes and modules?

To lasso a selection of nodes and/or modules, click and hold on the Canvas and drag around whatever you want to select.

### How do I shift-select multiple nodes and modules?

To select multiple nodes and modules using the shift modifier, hold down the shift key and click on the nodes and modules you want to select.

### How do I select all nodes and modules?

To select all of the elements in a patch, go to Edit > Select All.

Alternately, you can use the shortcut Command+A.

### How do I pan?

To pan, hold the Alt button and click and drag with your mouse.

### How do I zoom in and out?

To zoom in or out, use your mouse wheel.

### How do I zoom out so that everything on the Canvas fits in the screen?

To zoom to fit so that everything in your patch appears on screen at once, double click on the Canvas.

### How do I undo an action?

To undo an action, go to Edit > Undo.

Alternately, you can use the shortcut Command+Z.

Audulus has an infinite undo feature that persists even when the patch is closed.

### How do I clear the patch history?

To clear the patch history, go to Edit > Clear History.

All of the changes you make are kept track of in the patch history.

If you are satisfied with a patch and know that you do not want to revert to a previous state, clearing the history will shrink the file size.

### What are node and module functions?

Node and module functions are accessible by right clicking on any blank space in a node or module.

### How do I cut a module?

To cut a node or module, select a it and go to Edit > Cut.

Alternately, you can use the shortcut Command+X.

You can then paste it somewhere else. If you have multiple nodes or modules selected, all of them will be cut.

### How do I copy a module?

To cut a node or module, select a it and go to Edit > Copy.

Alternately, you can use the shortcut Command+C.

You can then paste a copy of it somewhere else. If you have multiple nodes or modules selected, all of them will be copied.

### How do I paste a module?

To cut a node or module, select a it and go to Edit > Copy.

Alternately, you can use the shortcut Command+V.

You can then paste a copy of it somewhere else. If you have multiple nodes or modules selected, all of them will be copied.

Note: You can cut/copy/paste between patches. This means if you have a portion of a patch you want to reuse in a new patch, you can select it, copy it, enter a new patch, and paste it in.

### How do I get help on using a node?

To get help about a particular node, right click on it and then click Help.

Note: The Help function requires an internet connection.

### How do I delete a node or module?

To cut a node or module, select a it and go to Edit > Delete.

Alternately, you can use the Backspace key.

If you have multiple nodes or modules selected, all of them will be deleted.

### How do I group nodes and modules into a new Subpatch node?

To group a selection of nodes and/or modules into a Subpatch node, click them and then click Group.

If the selection being grouped has inputs and/or outputs outside of the selection range, these connections will be preserved with automatically generated and labeled Input/Output nodes.

### What are module functions?

Module functions are accessible by right-clicking on any blank space in a module.

They are specific to modules (i.e., Subpatch nodes).

### How do I enter and exit a module?

To enter a module, right-click on it and then click Open.

Alternately, you can double click on it.

To exit, press the Escape key.

### How do I edit the UI or front panel of a module?

To edit the UI (User Interface) of a module, right-click on it and select Edit UI.

You can then drag and position nodes and exposable elements (e.g., oscillator waveshape, lights, meters) wherever you want.

The border of the Subpatch node will resize to accommodate whatever it contains.

There is a rudimentary layer system that makes whatever element was created most recently rise to the top.

To pull an element above another one, enter the subpatch, find the element you want to be on top, cut it, and then and paste it.

Audulus will consider the pasted node to be a new node, and so it will rise to the top.

The node will reconnect to any of its inputs, but this will break output connections, if any; so remember to reconnect them.

### How do I stop editing the UI of a module?

To stop editing the UI of a module, right-click on the module and select Lock UI.

This will prevent nodes and exposable elements from moving around and allow you to interact with controls and draw wires to and from inputs and outputs.

### How do I add my own modules to the Module Browser?

To add a module to the right-click Module Browser menu, go to Audulus > Open Modules Folder.

This will open a folder in your file browser. You can drop any modules or whole patches you want into this folder and they will appear in the right-click Module Browser menu.

You can also sort modules into multiple nested folders.

### What are node functions?

Many nodes have specific contextual functions.

These functions are accessible by clicking on any blank space in the node.

### What are the Expression node’s functions?

To edit an expression node, click on it and select Edit.

A box labeled Enter Expression will appear and you can then use your keyboard to change the expression.

### What are the Text node’s functions?

To edit a Text node, click on it and select Edit.

A box labeled Edit will appear and you can then use your keyboard to change the text.

### What are the Knob and Constant nodes’ functions?

To change the minimum value of a Knob or Constant node, right-click directly on the knob and select Set Min.

A box labeled Set Min will appear and you can then use your keyboard to change the minimum value.

To change the maximum value of a Knob or Constant node, right-click directly on the knob and select Set Max.

A box labeled Set Max will appear and you can then use your keyboard to change the maximum value.

To set the value of a Knob or Constant node, right-click directly on the knob and select Set Value.

A box labeled Set Value will appear and you can then use your keyboard to change the current value.

To assign a MIDI CC to a Knob or Constant node, right-click directly on the knob and select Learn Midi CC.

Next, twist, push, or slide the corresponding control of a plugged-in MIDI interface, and the controls will be linked.

Note: These functions also apply to the knobs on the ADSR node. The exception is that the minimum value for any given knob should be no less than 0 (time parameters cannot be negative).

### What are the Trigger node’s functions?

To turn a momentary Trigger node into a toggle switch, right-click on a blank space on the node and select [ ] Toggle.

To turn a toggle Trigger node into a momentary switch, right-click on a blank space on the node and select [X] Toggle.

To assign a MIDI note to the Trigger node, right-click on a blank space on the node and select Learn Midi Note.

### What is the Module Browser?

The Module Browser is where all of the nodes and modules are collected.

### How do I browse the nodes and modules?

When you right-click on the Canvas to open the Module Browser, nodes are listed first.

There are 52 nodes. All nodes are nested in various categories.

Modules, on the other hand, are collected in a separate submenu at the bottom of the right-click menu.

### How do I create a node or module?

To create a node or module, tap on its name. The menu will close and the node or module you selected will appear on the canvas.





# How to install and use the Audulus plugin

### What is the Audulus plugin?

Audulus comes with a plugin version that can be loaded into any DAW (e.g., GarageBand, Ableton Live, Logic, etc.)

The plugin version has two types: instrument and effect.

Instruments can receive Midi input from a piano roll or external Midi controller. Use the instrument plugin if you want to use Audulus as a synthesizer or drum machine. Instruments cannot receive audio.

Effects can receive audio from an an audio or Midi track (as long as it is placed after a sound source). Use the effect plugin if you want to use Audulus as an audio effect. Effects cannot receive MIDI.

Note: As of this writing, only the effect plugin is available for Windows/Linux.

### How do I install the Mac AU Plugin?

The Audulus AU plugin is available only for Mac.

As of this writing, an iOS compatible AU version is in development.

To install the Audulus AU plugin on Mac, go to Audulus 3 > Install AU. This will take you to a webpage where you can download the AU installer package with installation instructions.

### How do I install the Windows/Linux VST Plugin?

The Audulus VST plugin is available only for Windows and Linux.

It should install automatically when you first install Audulus.

If you cannot find it, try reinstalling Audulus.

How do I automate parameters in the Audulus plugin?

As of this writing, you cannot directly automate knobs or buttons within Audulus as might normally with other plugins. This feature is still in development.



---

## Audulus Audio Unit (Mac Only)

[Download Audio Unit](http://content.audulus.com/Audulus%20Audio%20Unit%203.3.pkg)

To install Audulus as an Audio Unit plugin, download the installer
package above.

The installer package will install the Audio Anit to either a
user-specific (`~/Library/Audio/Plug-Ins/Components`) or a system-wide
(`/Library/Audio/Plug-Ins/Components`) location.

The Audulus Audio Unit will appear under the manufacturer name
"Audulus". Both 32-bit and 64-bit versions are included in the plugin.

Audulus.app must be present in the Applications folder for the Audio Unit to work.
