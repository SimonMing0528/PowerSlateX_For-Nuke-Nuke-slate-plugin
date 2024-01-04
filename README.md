# PowerSlateX_For Nuke ::: Nuke slate plugin

![normal_X_ForTittle](https://github.com/SimonMing0528/PowerSlateX_For-Nuke-Nuke-slate-plugin/assets/137688513/7bd34e95-3172-4430-ae59-ad976f3f1cad) <br>
<br> 

A Nuke slate plugin developed using Prism2, a VFX project workflow management software, capable of displaying current shot version information within the frame (e.g., shot ID, version number, frame range, project naming, etc.). This facilitates daily progress checks, comparisons, and allows for shot review personnel to confirm version details efficiently during regular work tasks <br>
<br>

![LCT 拷贝](https://github.com/SimonMing0528/PowerSlateX_For-Nuke-Nuke-slate-plugin/assets/137688513/49f3367a-0dfd-4b54-a0e7-daf19954903f)

# Installation
1. Copy the `PowerSlate_nuke` full folder into the Nuke environment directory.<br>
it's usually at `C:\Users\(your username)\.nuke`
<br>
2. Then find the `init.py` file，If there isn't one, create it. and add the following code: <br>
<br>

```
nuke.pluginAddPath('./PowerSlate_nuke')
nuke.pluginAddPath('./PowerSlate_nuke/py')
```

3. Once you've completed the above steps, launch your Nuke application. If the installation was successful, you should see the icon on the left side of the interface
nuke slate plugin for version information of shots used in Nuke ![4200431](https://github.com/SimonMing0528/PowerSlateX_For-Nuke-Nuke-slate-plugin/assets/137688513/df2ef4e5-8a21-494e-92b3-57820ba87289)


# Usage <br>

![104175903](https://github.com/SimonMing0528/PowerSlateX_For-Nuke-Nuke-slate-plugin/assets/137688513/aef75fcb-bef0-45dc-8d5c-faf89d9a52d0) <br>
<br>

Simply input your scene information manually。<br>
<br>
<br>
## TaskStatus：

Status markings are divided into three types: `PostViz`; `In-progress`; `Review`.<br>
<br>

`PostViz`: Simply combines visual elements to get a rough overall effect of the arrangement.

`In-progress`: Indicates the current lens is still ongoing, used for progress checks.

`Review`: Denotes that the current version of the lens is completed, used for reviewers to inspect visual effects in order to provide feedback for modifications <br>
<br>
<br>
<br>

## LetterBox
Checking this option will display all lens information within a black border outside the frame, preventing it from obstructing the image
> When this option is enabled, the information text at the top of the frame might shift higher or lower from its original position. Please manually adjust their positions in the `Text Position` below <br>
<br>

![03225043](https://github.com/SimonMing0528/PowerSlate-Nuke_ForPrism2/assets/137688513/79844a62-c325-4d4c-b3c3-1fb964121355) <br>
<br>
<br>

## Use TC code
This option will display the TIMECODE from the metadata within the frame <br>
<br>
<br>

# Contact
If you have any questions or wish to report a bug related to this gizmo
feel free to leave a message using GitHub's issue section or contact me via the following email: <br>
Simon.lee.edu@outlook.com <br>
<br>
<br>
<br>

