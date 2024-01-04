import nuke

def preStart():
    all_nodes = nuke.allNodes()
    for node in all_nodes:
        if node.name() == 'PowerSlate_Shot':
            core_button = node.knob('Core')
            if core_button:
                core_button.execute()



def aftRenderDisable():#设置渲染后禁用节点callback
    all_nodes = nuke.allNodes()
    for node in all_nodes: 
        if node.name() == "PowerSlate_Shot":
            node['disable'].setValue(1)

