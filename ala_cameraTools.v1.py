# ala_cameraTools.0.03.py
# This tool creates a camera based on a real lworld camera, and lets user set Arri Master Prime focal lengths.

import maya.cmds as cmds

# creates an AlexaLF camera and sets the film back. Sets the Far Clip PLane to 10,000. Also setting the render settings to HD.
def createCamera():
    cameraName = cmds.camera(horizontalFilmAperture=1.247, verticalFilmAperture=0.702, farClipPlane=100000, depthOfField = True)
    setResolutionWidth = cmds.setAttr('defaultResolution.width', 1920)
    setResolutionHeight = cmds.setAttr('defaultResolution.height', 1080)
    setDeviceAspectRatio = cmds.setAttr('defaultResolution.deviceAspectRatio', 1.778)

    
# Sets the camera Aperature made by the pipeline to match an AlexaLF camera. And sets the scene Render Settings to HD.
def alexaCamera():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".horizontalFilmAperture", 1.247)
            cmds.setAttr(cam_shp[0]+".verticalFilmAperture", 0.702)
            cmds.setAttr(cam_shp[0]+".farClipPlane", 100000)
            
    setResolutionWidth = cmds.setAttr('defaultResolution.width', 1920)
    setResolutionHeight = cmds.setAttr('defaultResolution.height', 1080)
    setDeviceAspectRatio = cmds.setAttr('defaultResolution.deviceAspectRatio', 1.778)

 
def focalLength12():
#loop over all cameras that are selected (transform node)
    for each_cam_tf in cmds.ls(sl=True):
#find the shape node
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
#only set attr if a camera shape was found 
        if cam_shp:
#set focal length
            cmds.setAttr(cam_shp[0]+".fl", 12)


def focalLength14():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 14)
                        
def focalLength16():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 16)
            
def focalLength18():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 18)
            
def focalLength21():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 21)
            
def focalLength25():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 25)
            
def focalLength27():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 27)
            
def focalLength32():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 32)
            
def focalLength35():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 35)
            
def focalLength40():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 40)
            
def focalLength50():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 50)
            
def focalLength65():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 65)
            
def focalLength75():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 75)
            
def focalLength100():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 100)
            
def focalLength135():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 135)
            
def focalLength150():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 150)

def focalLength150():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 150)

def dof50():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 50)
def dof100():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 100)

def dof200():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 200)
            
def dof300():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 300)

def dof400():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 400)

def dof500():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 500)

def dof600():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 600)

def dof700():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 700)

def dof800():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 800)

def dof900():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 900)

def dof1000():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 1000)

def dof1200():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 1200)

def dof1400():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 1400)

def dof1700():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 1700)

def dof2000():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fd", 2000)


def cameraTools():
    
    if cmds.window('cameraTools', exists = True):
        cmds.deleteUI('cameraTools')
        
    cmds.window('cameraTools', resizeToFitChildren=True)
    
#    cmds.window('cameraTools', widthHeight=(200, 450))

    cmds.columnLayout(adjustableColumn = True)
    
    cmds.separator(h=10)
    cmds.text('PREVIS: Creates an AlexaLF camera', align = "center")
    cmds.text('Sets the correct render settings', align = "center")
    cmds.separator(h=10)
    
    cmds.button(label = 'Create Camera', command = 'createCamera()', align = "center")


    cmds.separator(h=30)
    cmds.text('LAYOUT: AlexaLF Settings', align = "center")
    cmds.separator(h=10)
    
    cmds.button(label = 'AlexaLF Settings', command = 'alexaCamera()', align = "center")
    
    cmds.separator(h=30)
    cmds.text('Focal Length', align = "center")
    cmds.separator(h=10)
    
    cmds.rowColumnLayout(numberOfColumns = 16)
    cmds.button(label = '12mm', align = "center", command = 'focalLength12()')
    cmds.button(label = '14mm', align = "center", command = 'focalLength14()')
    cmds.button(label = '16mm', align = "center", command = 'focalLength16()')
    cmds.button(label = '18mm', align = "center", command = 'focalLength18()')
    cmds.button(label = '21mm', align = "center", command = 'focalLength21()')
    cmds.button(label = '25mm', align = "center", command = 'focalLength25()')
    cmds.button(label = '27mm', align = "center", command = 'focalLength27()')
    cmds.button(label = '32mm', align = "center", command = 'focalLength32()')
    cmds.button(label = '35mm', align = "center", command = 'focalLength35()')
    cmds.button(label = '40mm', align = "center", command = 'focalLength40()')
    cmds.button(label = '50mm', align = "center", command = 'focalLength50()')
    cmds.button(label = '65mm', align = "center", command = 'focalLength65()')
    cmds.button(label = '75mm', align = "center", command = 'focalLength75()')
    cmds.button(label = '100mm', align = "center", command = 'focalLength100()')
    cmds.button(label = '135mm', align = "center", command = 'focalLength135()')
    cmds.button(label = '150mm', align = "center", command = 'focalLength150()')

    
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    
    cmds.text('Depth of Field', align = "center")
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)
    cmds.separator(h=40)

    
    cmds.button(label = '50mm', align = "center", command = 'dof50()')
    cmds.button(label = '100mm', align = "center", command = 'dof100()')
    cmds.button(label = '150mm', align = "center", command = 'dof200()')
    cmds.button(label = '200mm', align = "center", command = 'dof300()')
    cmds.button(label = '300mm', align = "center", command = 'dof400())')
    cmds.button(label = '400mm', align = "center", command = 'dof500()')
    cmds.button(label = '500mm', align = "center", command = 'dof500()')
    cmds.button(label = '600mm', align = "center", command = 'dof600()')
    cmds.button(label = '700mm', align = "center", command = 'dof700()')
    cmds.button(label = '800mm', align = "center", command = 'dof800()')
    cmds.button(label = '900mm', align = "center", command = 'dof900()')
    cmds.button(label = '1000mm', align = "center", command = 'dof1000()')
    cmds.button(label = '1200mm', align = "center", command = 'dof1200()')
    cmds.button(label = '1400mm', align = "center", command = 'dof1400()')
    cmds.button(label = '1700mm', align = "center", command = 'dof1700()')
    cmds.button(label = '2000mm', align = "center", command = 'dof2000()')

    
    cmds.showWindow('cameraTools')

    
cameraTools()