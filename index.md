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

li {
  list-style-image: url(img/bullet.png);
}

.responsive-container { position: relative; padding-bottom: 56.25%; padding-top: 30px; height: 0; overflow: hidden; }
.responsive-container iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }

</style>

![Audulus Logo](img/logo.png)

Welcome to **Audulus**! With Audulus you can build synthesizers
from first principles, design new sounds, or process audio. All with
real-time low-latency processing suitable for live performance.
    
To get started, begin with the UI Basics for your platform (<a href="#ui-basics-ipadiphone">iOS</a> or <a href="#ui-basics-mac">Mac</a>).

Be sure to sign up [here](http://eepurl.com/-8vkP) for the Audulus mailing list.

If you need help or have found a bug, please contact us at:

![Support Email Address](img/support.png)

We're here to help!

---

## UI Basics (iPad/iPhone)

### Patch Editor

![Patch Editor](img/editor.png)

The Patch Editor is Audulus's main view. It consists of an infinite canvas for creating patches, with toolbar at the bottom primarily for adding new modules to your patch. Open and close the toolbar using the ![Show](img/Show.png) and ![Hide](img/Hide.png) buttons. Exit to the patch browser using the ![Exit](img/Exit.png) button (also used for exiting sub-patches).

The iPad/iPhone Audulus UI at a glance:

-   Pinch with two fingers to zoom in and out of your patch.
-   Drag on the background or with two fingers to pan.
-   Double-tap on a node to zoom in for editing.
-   Double-tap on the background to zoom out and see your entire patch.
-   Many operations use context menus - tap and hold to bring up the context menu.
-   To make a connection, zoom in and drag from an output to an input.
-   To disconnect, drag from an input.
-   Audulus will automatically detect your MIDI keyboard or control
    surface.

Toolbar buttons:

-   ![Lock Mode Button](img/Lock.png) **Lock Mode** - Locks the nodes in
    place. This is useful for performing.
-   ![Timing Mode Button](img/Stopwatch.png) **Timing Mode** - Toggles
    timing mode. Timing Mode shows the percentage of CPU time each node
    in your patch takes to compute. The Timing Mode button is only shown
    if the Timing Mode upgrade has been purchased.
-   ![Help Button](img/help.png) **Help** - Shows the Audulus documentation.

### Patch Browser

The Patch Browser allows you to create, delete, duplicate, and share patches.

![Patch Browser](img/browser.png)

-   **"+"** - Creates a new patch.
-   ![Collapse Button](img/CollapseButton.png) **Collapse** - Collapses the
    patch thumbnails down to just their names, for browsing large
    collections of patches by name.
-   **"Select"** - Toggles the Path Browser's **Selection Mode** - When
    in selection mode, tapping on a patch thumbnail will select the
    patch and activate the Share, Duplicate, and Delete buttons.
    Multiple patches may be selected.
-   ![Share Patch Button](img/share.png) **Share** - Shares selected patches
    via email when in selection mode.
-   ![Duplicate Patch Button](img/duplicate.png) **Duplicate** - Duplicates
    selected patches when in selection mode.
-   ![Delete Patch Button](img/Delete.png) **Delete** - Deletes selected
    patches when in selection mode.
-   ![Settings Button](img/settings.png) **Settings** - Shows the Audulus
    settings.

---

## UI Basics (Mac/Windows)

The Desktop Audulus UI at a glance:

-   many operations use right-click context menus (control click if you
    have one button)
-   to create a new node, right-click on the background
-   to zoom, use the mouse wheel or pinch with two fingers on your trackpad
-   to pan, use two fingers on your trackpad, or hold the Option/Alt key and drag
-   Apple Magic Mouse users: swipe on the mouse to pan, hold the Control key and swipe vertically to zoom.
-   to select a node just click on it
-   to select multiple nodes, hold shift while clicking, or drag on the background to lasso-select.
-   to make a connection between nodes, drag from an output to an input
-   to disconnect, drag from an input
-   to get help on a node, right click and select "Help"

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


