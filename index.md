<style>
body {
  background-color: black;
  color: rgb(136, 136, 136);
  font-family: 'Input Sans', sans-serif;
}

img, video {
  max-width: 100%;
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

em {
  color: #2a9fd6;
}

li {
  list-style-image: url(img/bullet.png);
}

.responsive-container { position: relative; padding-bottom: 56.25%; padding-top: 30px; height: 0; overflow: hidden; }
.responsive-container iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }

</style>

![Audulus Logo](img/logo.png)

Welcome to *Audulus!*  

With Audulus, you can build synthesizers
from first principles, design new sounds, or process audio - all with
real-time, low-latency processing suitable for live performance.
    
To get started, begin with the UI Basics for your platform (<a href="#ui-basics-ipadiphone">iOS</a> or <a href="#ui-basics-mac">Mac/Windows</a>).

### Be sure to sign up for the Audulus mailing list!

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

*We will send no more than 1 email per month* - the newsletter is mostly a round-up of all the new patches and discussions happening over the forum - an excellent resource if you do not want to participate in the forum yourself but still want to keep up with all the new patches and the latest techniques.

### If you need help or have found a bug, please contact us at:

![Support Email Address](img/support.png)

*We will respond within 24 hours - often sooner.*  When making a bug report, please: 

-	attach whatever patch you were working on when Audulus crashed.
-  give as much detailed information as you can about how to reproduce the bug. **If a bug is not reproduceable, it is difficult to know what to fix.**
-  Crash reports are sent automatically and do not need to be included.

*We are also available to help you "debug" your patches.* If Audulus is working fine, but your patch is not, please do not contact us through our support email - instead, post it on the forum under the "Help" heading along with a description of how you *think* your patch should be working. We will download it, fix it, and reupload it to the forum for you, with a detailed explanation of what we did to fix it. This can be a very educational process that benefits all our forum members, and that is why we would prefer this kind of help to happen over at the forum.

---

## UI Basics (iPad/iPhone)

### Patch Editor

![Patch Editor](img/editor.png)

The Patch Editor is Audulus's main view. It consists of an infinite canvas for creating patches, with toolbar at the bottom.  

- The canvas grows and shrinks to fit the size of the patch.  If you have just one small node in a patch, you will not be able to zoom out - you need to add at least 2 nodes or modules and space them apart to give yourself some "breathing room."

Open and close the toolbar using the ![Show](img/Show.png) and ![Hide](img/Hide.png) chevron buttons. Exit to the patch browser using the ![Exit](img/Exit.png) button. This button is also used to exit a subpatch.  To enter a subpatch, double tap in a blank space on the UI of a module.

- The toolbar is primarily for adding new modules to your patch, but it also contains the node browser and an on-screen multi-touch keyboard. 
- *We highly recommend that new users create patches with modules* - working with nodes can be cumbersome and slow, and to speed up patch construction was one of the primary reasons the Module Library was created. Most of the nodes are non-functional as-is.  For example: a crossfade node needs a knob attached to the input "C" to access the node's basic function.  The Crossfade Module, however, comes with indicator lights, a knob, and even a switch!  As you can see, modules are much more useful "out-of-the-box" than nodes are.  
- You can think of nodes as the "atoms" of Audulus.  Modules are more like molecules.  If you know anything about chemistry, you will know that working with elements alone does not lead to much interesting chemistry.  
- That said, some nodes, like the expression node or the light node, cannot be built up into a module and must be used as nodes.
 
## The iPad/iPhone Audulus UI at a glance:

-   Pinch with two fingers to zoom in and out of your patch.
-   Drag with two fingers to pan.
-   Drag with one finger on the background to lasso-select multiple nodes. ( *See note 1 below* )
-   Double-tap on a node to zoom in for editing.
-   Double-tap on the background and Audulus will zoom to fit the entire patch comfortably in view.
-   Many operations use context menus - tap and hold to bring up the context menu.
-   To make a connection, zoom in and drag from an output to an input. Connections can *only* be made from an output to an input.
-   To disconnect, drag the connection away from an input.
-   To "hot swap" or live patch, keep your finger held down and wave the output wire over an input or knob. This is similar to performing with patch cables on a modular, but you'll never wear out your inputs in Audulus!  Audulus is also optimized to prevent clicking/popping connection noise, so go crazy with it!
-   To make a long connection, drag to to the edge of the screen. Audulus will zoom out, widening your field of view. Move your finger away from the edge of the screen, and Audulus will zoom back in, centering around your finger, so you can place the connection.
-   If you are zoomed too far out to make a connection, the inputs and outputs will visibly "lock" or "close." Zoom back in and they will "open" again, and you can now make and break connections as well as turn knobs.  If you have knobs and triggers mapped to MIDI, this is a non-issue. ( *See note 2 below* )
-   Speaking of mapping and controllers: Audulus will automatically detect your MIDI keyboard or control surface. 
-   To map a knob or a trigger to MIDI, press and hold the element you want to map and select "Learn Midi CC," then twist/press the corresponding knob/button on your control surface, and the controls will thereafter be linked.

       
*Note 1:* The lasso tool - new in Audulus 3 - works in a somewhat unique way. The lasso can do much more than rope an entire area into selection. As it is, the lasso gives you surgical control over what you select, allowing you to accurately clip out portions of others' designs for use in your own. Much of the progress that is made in the Audulus community happens when people leapfrog with shared knowledge.  The new lasso tool in Audulus 3 just makes that process *much* easier.  As you can see, it is worth your time to get to know how the lasso works, as doing so will make your workflow much more efficient.

*Note 2:* This is not how the zoom worked in Audulus 2, and unfortunately, it does make detailed work on iOS a little more time-consuming (though surely this is made up for by having the Module Library at your disposal). It has to be this way, however, to be compliant with Apple's iOS touch standards. Apple probably never envisioned an app like Audulus when making this rule, and perhaps this requirement will be relaxed in the future.  For now though - it *does* have a side benefit of preventing accidental disconnections when zoomed out - a nightmare when working on a complicated patch on iOS.  In Audulus 2, you could easily accidentally swipe a connection away, and if you're not working on a patch that is making sound, you might not notice the disconnection for a long time.  *The best thing you can do to improve your Audulus 3 workflow is invest in a conductive stylus (pen).*  Fingers are still great - even superior - for performance, but detailed, precise "assembly" work is much easier with a stylus - a suitable one can often be found for $10 or less.


##Toolbar buttons:

-   ![Lock Mode Button](img/Lock.png) **Lock Mode** - Locks the nodes in
    place. This is useful for performing.
-   ![Timing Mode Button](img/Stopwatch.png) **Timing Mode** - Toggles
    timing mode. Timing Mode shows the percentage of CPU time each node
    in your patch takes to compute.
-   ![Help Button](img/help.png) **Help** - Shows the Audulus documentation.

### Patch Browser

The Patch Browser allows you to create, delete, duplicate, and share patches.

![Patch Browser](img/browser.png)

-   *"+"* - Upper left corner - Creates a new patch.
-   ![Collapse Button](img/CollapseButton.png) **Collapse** - Collapses the
    patch thumbnails down to just their names, for browsing large
    collections of patches by name.
-   **"Select"** - Toggles the Patch Browser's **Selection Mode** - When
    in Selection Mode, tapping on a patch thumbnail will select the
    patch and activate the Share, Duplicate, and Delete buttons.
    Multiple patches may be selected at once. 
    - **Note:** *It is very common to forget to exit this mode - you will not be able to create or enter a patch while in* **Selection Mode**.
-   ![Share Patch Button](img/share.png) **Share** - Shares selected patches
    via email when in **Selection Mode.**
-   ![Duplicate Patch Button](img/duplicate.png) **Duplicate** - Duplicates
    selected patches when in **Selection Mode.**
-   ![Delete Patch Button](img/Delete.png) **Delete** - Deletes selected
    patches when in **Selection Mode.**
-   ![Settings Button](img/settings.png) **Settings** - Shows Audulus'
    settings.

---

## UI Basics (Mac/Windows)

The Desktop Audulus UI at a glance:

-   Many operations use right-click context menus (or control+click if you
    have one button)
-   To create a new node, right-click on the background. A menu will pop up that gives you access to all the nodes and Modules.  The Module Library is found at the bottom of the menu. ( *See Note 1* )
-   To zoom, use the mouse wheel or pinch with two fingers on your trackpad.
-   To pan, use two fingers on your trackpad, or hold the Option/Alt key and drag.  You can also zoom out, hover your mouse over a new focal point, and zoom back in - this may seem an odd way to navigate at first, but it is much faster than simply panning because it requires less mouse movement.
-   *Apple Magic Mouse users:* swipe on the mouse to pan, hold the Control key and swipe vertically to zoom. You may need to turn off "Use scroll gesture with modifier keys to zoom," in the Zoom section of the Accessibility control panel in System Preferences.
-   to select a node just click on it
-   to select multiple nodes, hold shift while clicking, or drag on the background to lasso-select.
-   to make a connection between nodes, drag from an output to an input
-   to disconnect, drag from an input
-   to get help on a node, right click and select "Help"

*Note 1:* The Module Library is named *The Library of Babel* after a Borges story that imagines a mystical library that contains not only every book ever written, but every book that could ever *be* written. You are perhaps more familiar with the Biblical story of the the Tower of Babel, which, mythically, the Babylonians were building as a kind of space-elevator to Heaven.  Jehovah grew afraid of the power of people working together, and destroyed the project by cursing its workers to speak in a multitude of languages, unable to communicate.  This is the Judeo-Christian origin story that explains why all people do not speak the same language.  If you are not familiar with the Borges story itself, perhaps you are familiar with the concept through Neil Gaiman's *The Sandman*, where the library is referred to as the *Library of Dreams* which contains all the unfinished potential work of every author living & dead.  *So, what does any of this have to do with Audulus?* Well, I, Mark Boyd, the Module Library creator, wanted to convey the sense of infinite possibility that Audulus 3 now holds, and most of all, what can be accomplished when people all over the world - even through language barriers ( 日本人こんにちは！) - can do when they work together. Every module and patch from version 3 and onward will be backwards compatible - meaning nothing will ever be lost or forgotten. While some more established digital modulars exist, you are entering this program at the beginning of something very special, and *you* get to be a founding creator. That said - yes, I understand that it is currently a maze of menus. Know that we are working very hard to streamline both the iOS and computer navigation of this library.  Just stick with it for now and know that it will get better and faster soon - it will *have* to when eventually the module library contains 1000+ modules.

---

## Intro videos

<div class="responsive-container">
<iframe src="http://player.vimeo.com/video/148324131" width="480" height="270" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
</div>

<div class="responsive-container">
<iframe src="http://player.vimeo.com/video/148319769" width="480" height="270" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
</div>

<div class="responsive-container">
<iframe src="http://player.vimeo.com/video/148358980" width="480" height="270" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
</div>

## Getting Help

If you need help or have found a bug, contact us at:

![Support Email Address](img/support.png)

We're here to help!

---

## Audulus Mailing List

Sign up [here](http://eepurl.com/-8vkP) for the Audulus mailing list. You'll get:

*  Updates for new versions of Audulus
*  Tutorials
*  New Patches
*  And more!

## Polyphony

Polyphonic processing in Audulus works seamlessly. A connection between
nodes is polyphonic if it is rendered thicker. Nodes are automatically
capable of polyphonic processing. So for example, feed a **Distortion**
node with a polyphonic connection and the distortion will be applied
separately to each voice in the connection.

A good example of polyphonic processing is the **Subtractive** example.
Set the [**Keyboard**](/nodes/#keyboard) node to "poly" and note the
thicker polyphonic connections. That is, up until the voices are mixed
down by the [**PolyToMono**](/nodes/#polytomono) node.

---

## Custom Nodes

Using **Custom Nodes**, you can design your own node user interfaces.

Use the following steps to create your own node UI.

1. Create a sub-patch using the Patch Node (Utilities -> Patch)
2. Enter the sub-patch by double-tapping (or double-clicking) on the Patch Node
3. Create a Knob node.
5. Exit the sub-patch and you'll see your knob on the front panel.
6. Open the context menu on the Patch Node and select Edit UI
7. Drag the knob to where you'd like it.
8. Open the Path Node's context menu again and select Lock UI to finish editing the UI.

Knobs aren't the only widgets that can be exposed. Various nodes have an "Expose" option in their context menus.

---

## Audulus Audio Unit (Mac Only)

[Download Audio Unit](http://content.audulus.com/Audulus%20Audio%20Unit%203.0.pkg)

To install Audulus as an Audio Unit plugin, download the installer
package above.

The installer package will install the Audio Anit to either a
user-specific (`~/Library/Audio/Plug-Ins/Components`) or a system-wide
(`/Library/Audio/Plug-Ins/Components`) location.

The Audulus Audio Unit will appear under the manufacturer name
"Audulus". Both 32-bit and 64-bit versions are included in the plugin.

Audulus.app must be present in the Applications folder for the Audio Unit to work.


