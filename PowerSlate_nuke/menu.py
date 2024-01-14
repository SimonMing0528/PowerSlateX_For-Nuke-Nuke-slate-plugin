# add menu
sideBar = nuke.menu('Nodes')
pow = sideBar.addMenu('PowerSlate', icon='icon_Normal.png')

def createRenameShot():
    new_node = nuke.createNode('pw_shot')
    if new_node:
        new_node.setName('PowerSlate_Shot')
        core_button = new_node.knob('Core')
        if core_button:
            core_button.execute()

def createRenameLdv():
    new_node = nuke.createNode('pw_LDV')
    if new_node:
        new_node.setName('PowerSlate_LDV')


def setOnLoad():
    project_settings = nuke.toNode('root')  
    if 'onScriptLoad' in project_settings.knobs():
        on_script_load_knob = project_settings['onScriptLoad']
        on_script_load_knob.setValue('from mainCallBack import* ;preStart();aftRenderDisable()')


# add Group to the menu
pow.addCommand('Shot',"createRenameShot(); setOnLoad()")
pow.addCommand('LookDev',"createRenameLdv()")




