# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Crok_dithering_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Crok_dithering_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Crok_dithering_GL"

def getLabel():
    return "Crok_dithering_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "Crok_dithering_GL.png"

def getGrouping():
    return "Community/GLSL/Effect"

def getPluginDescription():
    return "Creates a dithering effect."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(1, 0.2353, 0.2353)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("DITHERING", "Dithering")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.DITHERING = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1paramValueBool5", "Enable : ")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueBool5 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat1", "Scale :")
    param.setMinimum(0.09999999999999999, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0.09999999999999999, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat2", "Dithering blend : ")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat2 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createSeparatorParam("PIXELISATION", "Pixelisation")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.PIXELISATION = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1paramValueBool6", "Enable : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueBool6 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat0", "Size : ")
    param.setMinimum(1, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(10000, 0)
    param.setDefaultValue(150, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat3", "Pixelation blend : ")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat3 = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createSeparatorParam("C64", "C64")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.C64 = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1paramValueBool7", "Enable : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueBool7 = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat4", "C64 blend : ")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat4 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    param = lastNode.createStringParam("sep19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep19 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Crok_dithering_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE101", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE101 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3645)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1")
    lastNode.setLabel("Shadertoy1")
    lastNode.setPosition(4139, 3864)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(150, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat4")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueBool5")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool6")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramValueBool7")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/run/media/ffernandez/FABRICE/PERSO/NATRON/GIT_DEV/natron-plugins/Shadertoy/Crok_dithering.frag.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\r\n//\r\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\r\n//                        MM.                          .MM\r\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\r\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\r\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\r\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\r\n//                   MM.  .MmM              MMMM      MMM.  .MM\r\n//                  MM.  .MMM                 MM       MMM.  .MM\r\n//                 MM.  .MMM                   M        MMM.  .MM\r\n//                MM.  .MMM                              MMM.  .MM\r\n//                 MM.  .MMM                            MMM.  .MM\r\n//                  MM.  .MMM       M                  MMM.  .MM\r\n//                   MM.  .MMM      MM                MMM.  .MM\r\n//                    MM.  .MMM     MMM              MMM.  .MM\r\n//                     MM.  .MMM    MMMM            MMM.  .MM\r\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\r\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\r\n//                        MM.                          .MM\r\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\r\n//\r\n//\r\n//\r\n//\r\n// Adaptation pour Natron par F. Fernandez\r\n// Code original : crok_dithering Matchbox pour Autodesk Flame\r\n\r\n// Adapted to Natron by F.Fernandez\r\n// Original code : crok_dithering Matchbox for Autodesk Flame\r\n\r\n// Dithering code based on: http://devlog-martinsh.blogspot.se/2011/03/glsl-8x8-bayer-matrix-dithering.html\r\n// C64 look effect based on: http://oos.moxiecode.com/js_webgl/c64_shader/  by @oosmoxiecode\r\n\r\n// BBox: iChannel0\r\n\r\nuniform float size = 150; // Size : (size), min=1, max=10000\r\nuniform float scale = 1.0; // Scale : (scale), min=0.1, max=1\r\nuniform float d_blend = 1.0; // Dithering blend : (dithering blend), min=0.0, max=1\r\nuniform float p_blend = 1.0; // Pixelation blend : (pixelisation blend), min=0.0, max=1\r\nuniform float c64_blend = 1.0; // C64 blend : (C64 blend), min=0.0, max=1\r\n\r\n\r\n\r\nuniform bool dithering = true; // Enable : (enable dithering)\r\nuniform bool pixelation = false; // Enable : (enable pixelisation)\r\nuniform bool c64 = false; // Enable : (enable C64)\r\n\r\n\r\n\r\n\r\nfloat softLight( float s, float d )\r\n{\r\n\treturn (s < 0.5) ? d - (1.0 - 2.0 * s) * d * (1.0 - d) \r\n\t\t: (d < 0.25) ? d + (2.0 * s - 1.0) * d * ((16.0 * d - 12.0) * d + 3.0) \r\n\t\t\t\t\t : d + (2.0 * s - 1.0) * (sqrt(d) - d);\r\n}\r\n\r\nvec3 softLight( vec3 s, vec3 d )\r\n{\r\n\tvec3 c;\r\n\tc.x = softLight(s.x,d.x);\r\n\tc.y = softLight(s.y,d.y);\r\n\tc.z = softLight(s.z,d.z);\r\n\treturn c;\r\n}\r\n\r\n\r\n// dithering \r\nfloat find_closest(int x, int y, float c0) {\r\n\tint dither[64];\r\n\r\n\tdither[0] = 0; \r\n\tdither[1] = 32; \r\n\tdither[2] = 8; \r\n\tdither[3] = 40; \r\n\tdither[4] = 2; \r\n\tdither[5] = 32; \r\n\tdither[6] = 10; \r\n\tdither[7] = 42; \r\n\tdither[8] = 48; \r\n\tdither[9] = 16; \r\n\tdither[10] = 56; \r\n\tdither[11] = 24; \r\n\tdither[12] = 50; \r\n\tdither[13] = 18; \r\n\tdither[14] = 58; \r\n\tdither[15] = 26; \r\n\tdither[16] = 12; \r\n\tdither[17] = 44; \r\n\tdither[18] = 4; \r\n\tdither[19] = 36; \r\n\tdither[20] = 14; \r\n\tdither[21] = 46; \r\n\tdither[22] = 6; \r\n\tdither[23] = 38; \r\n\tdither[24] = 60; \r\n\tdither[25] = 28; \r\n\tdither[26] = 52; \r\n\tdither[27] = 20; \r\n\tdither[28] = 62; \r\n\tdither[29] = 30; \r\n\tdither[30] = 54; \r\n\tdither[31] = 22; \r\n\tdither[32] = 3; \r\n\tdither[33] = 35; \r\n\tdither[34] = 11; \r\n\tdither[35] = 43; \r\n\tdither[36] = 1; \r\n\tdither[37] = 33; \r\n\tdither[38] = 9; \r\n\tdither[39] = 41; \r\n\tdither[40] = 51; \r\n\tdither[41] = 19; \r\n\tdither[42] = 59; \r\n\tdither[43] = 27; \r\n\tdither[44] = 49; \r\n\tdither[45] = 17; \r\n\tdither[46] = 57; \r\n\tdither[47] = 25; \r\n\tdither[48] = 15; \r\n\tdither[49] = 47; \r\n\tdither[50] = 7; \r\n\tdither[51] = 39; \r\n\tdither[52] = 13; \r\n\tdither[53] = 45; \r\n\tdither[54] = 5; \r\n\tdither[55] = 37; \r\n\tdither[56] = 63; \r\n\tdither[57] = 31; \r\n\tdither[58] = 55; \r\n\tdither[59] = 23; \r\n\tdither[60] = 61; \r\n\tdither[61] = 29; \r\n\tdither[62] = 53; \r\n\tdither[63] = 21; \r\n\t\r\n\tfloat limit = 0.0; \r\n\tif(x < 8) {\r\n\t\tint index = x + y*8; \r\n\r\n\t\tif (index == 0) {limit = float(dither[0]+1)/64.0;}; \r\n\t\tif (index == 1) {limit = float(dither[1]+1)/64.0;}; \r\n\t\tif (index == 2) {limit = float(dither[2]+1)/64.0;}; \r\n\t\tif (index == 3) {limit = float(dither[3]+1)/64.0;}; \r\n\t\tif (index == 4) {limit = float(dither[4]+1)/64.0;}; \r\n\t\tif (index == 5) {limit = float(dither[5]+1)/64.0;}; \r\n\t\tif (index == 6) {limit = float(dither[6]+1)/64.0;}; \r\n\t\tif (index == 7) {limit = float(dither[7]+1)/64.0;}; \r\n\t\tif (index == 8) {limit = float(dither[8]+1)/64.0;}; \r\n\t\tif (index == 9) {limit = float(dither[9]+1)/64.0;}; \r\n\t\tif (index == 10) {limit = float(dither[10]+1)/64.0;}; \r\n\t\tif (index == 11) {limit = float(dither[11]+1)/64.0;}; \r\n\t\tif (index == 12) {limit = float(dither[12]+1)/64.0;}; \r\n\t\tif (index == 13) {limit = float(dither[13]+1)/64.0;}; \r\n\t\tif (index == 14) {limit = float(dither[14]+1)/64.0;}; \r\n\t\tif (index == 15) {limit = float(dither[15]+1)/64.0;}; \r\n\t\tif (index == 16) {limit = float(dither[16]+1)/64.0;}; \r\n\t\tif (index == 17) {limit = float(dither[17]+1)/64.0;}; \r\n\t\tif (index == 18) {limit = float(dither[18]+1)/64.0;}; \r\n\t\tif (index == 19) {limit = float(dither[19]+1)/64.0;}; \r\n\t\tif (index == 20) {limit = float(dither[20]+1)/64.0;}; \r\n\t\tif (index == 21) {limit = float(dither[21]+1)/64.0;}; \r\n\t\tif (index == 22) {limit = float(dither[22]+1)/64.0;}; \r\n\t\tif (index == 23) {limit = float(dither[23]+1)/64.0;}; \r\n\t\tif (index == 24) {limit = float(dither[24]+1)/64.0;}; \r\n\t\tif (index == 25) {limit = float(dither[25]+1)/64.0;}; \r\n\t\tif (index == 26) {limit = float(dither[26]+1)/64.0;}; \r\n\t\tif (index == 27) {limit = float(dither[27]+1)/64.0;}; \r\n\t\tif (index == 28) {limit = float(dither[28]+1)/64.0;}; \r\n\t\tif (index == 29) {limit = float(dither[29]+1)/64.0;}; \r\n\t\tif (index == 30) {limit = float(dither[30]+1)/64.0;}; \r\n\t\tif (index == 31) {limit = float(dither[31]+1)/64.0;}; \r\n\t\tif (index == 32) {limit = float(dither[32]+1)/64.0;}; \r\n\t\tif (index == 33) {limit = float(dither[33]+1)/64.0;}; \r\n\t\tif (index == 34) {limit = float(dither[34]+1)/64.0;}; \r\n\t\tif (index == 35) {limit = float(dither[35]+1)/64.0;}; \r\n\t\tif (index == 36) {limit = float(dither[36]+1)/64.0;}; \r\n\t\tif (index == 37) {limit = float(dither[37]+1)/64.0;}; \r\n\t\tif (index == 38) {limit = float(dither[38]+1)/64.0;}; \r\n\t\tif (index == 39) {limit = float(dither[39]+1)/64.0;}; \r\n\t\tif (index == 40) {limit = float(dither[40]+1)/64.0;}; \r\n\t\tif (index == 41) {limit = float(dither[41]+1)/64.0;}; \r\n\t\tif (index == 42) {limit = float(dither[42]+1)/64.0;}; \r\n\t\tif (index == 43) {limit = float(dither[43]+1)/64.0;}; \r\n\t\tif (index == 44) {limit = float(dither[44]+1)/64.0;}; \r\n\t\tif (index == 45) {limit = float(dither[45]+1)/64.0;}; \r\n\t\tif (index == 46) {limit = float(dither[46]+1)/64.0;}; \r\n\t\tif (index == 47) {limit = float(dither[47]+1)/64.0;}; \r\n\t\tif (index == 48) {limit = float(dither[48]+1)/64.0;}; \r\n\t\tif (index == 49) {limit = float(dither[49]+1)/64.0;}; \r\n\t\tif (index == 50) {limit = float(dither[50]+1)/64.0;}; \r\n\t\tif (index == 51) {limit = float(dither[51]+1)/64.0;}; \r\n\t\tif (index == 52) {limit = float(dither[52]+1)/64.0;}; \r\n\t\tif (index == 53) {limit = float(dither[53]+1)/64.0;}; \r\n\t\tif (index == 54) {limit = float(dither[54]+1)/64.0;}; \r\n\t\tif (index == 55) {limit = float(dither[55]+1)/64.0;}; \r\n\t\tif (index == 56) {limit = float(dither[56]+1)/64.0;}; \r\n\t\tif (index == 57) {limit = float(dither[57]+1)/64.0;}; \r\n\t\tif (index == 58) {limit = float(dither[58]+1)/64.0;}; \r\n\t\tif (index == 59) {limit = float(dither[59]+1)/64.0;}; \r\n\t\tif (index == 60) {limit = float(dither[60]+1)/64.0;}; \r\n\t\tif (index == 61) {limit = float(dither[61]+1)/64.0;}; \r\n\t\tif (index == 62) {limit = float(dither[62]+1)/64.0;}; \r\n\t\tif (index == 63) {limit = float(dither[63]+1)/64.0;}; \r\n\t} \r\n\r\n\tif(c0 < limit) \r\n\treturn 0.0; \r\n\treturn 1.0; \r\n} \r\n\t\t \r\n\r\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\r\n{ \r\n\tvec2 uv = fragCoord.xy / iResolution.xy;\r\n\tvec2 xy = fragCoord.xy * scale;\r\n\tvec3 col = texture2D(iChannel0, uv).rgb;\r\n\t\r\n\tif ( pixelation )\r\n\t{\r\n\t\tvec2 div = vec2(iResolution.x * size / iResolution.y, size); \r\n\t\tvec2 pixel = floor(uv * div)/div;\r\n\t\tvec3 p_col = texture2D(iChannel0, pixel).rgb;\r\n\t\tcol = mix(col, p_col, p_blend);\r\n\t\t\r\n\t}\r\n\r\n\tif ( dithering )\r\n\t{\r\n\t\tint x = int(mod(xy.x, 8.0)); \r\n\t\tint y = int(mod(xy.y, 8.0)); \r\n\t\tvec3 d_col; \r\n\t\td_col.r = find_closest(x, y, col.r); \r\n\t\td_col.g = find_closest(x, y, col.g); \r\n\t\td_col.b = find_closest(x, y, col.b); \r\n\t\t// overaly the dithered output on top of the pixelated one\r\n\t\tvec3 o_col = softLight(d_col, col);\r\n\t\tcol = mix(col, o_col, d_blend);\r\n\t\t\r\n\t}\r\n\r\n\tif ( c64 )\r\n\t{\r\n\t\tvec3 c64col[16];\r\n\t\tc64col[0] = vec3(0.0,0.0,0.0);\r\n\t\tc64col[1] = vec3(62.0,49.0,162.0);\r\n\t\tc64col[2] = vec3(87.0,66.0,0.0);\r\n\t\tc64col[3] = vec3(140.0,62.0,52.0);\r\n\t\tc64col[4] = vec3(84.0,84.0,84.0);\r\n\t\tc64col[5] = vec3(141.0,71.0,179.0);\r\n\t\tc64col[6] = vec3(144.0,95.0,37.0);\r\n\t\tc64col[7] = vec3(124.0,112.0,218.0);\r\n\t\tc64col[8] = vec3(128.0,128.0,129.0);\r\n\t\tc64col[9] = vec3(104.0,169.0,65.0);\r\n\t\tc64col[10] = vec3(187.0,119.0,109.0);\r\n\t\tc64col[11] = vec3(122.0,191.0,199.0);\r\n\t\tc64col[12] = vec3(171.0,171.0,171.0);\r\n\t\tc64col[13] = vec3(208.0,220.0,113.0);\r\n\t\tc64col[14] = vec3(172.0,234.0,136.0);\r\n\t\tc64col[15] = vec3(255.0,255.0,255.0);\r\n\t\t\r\n\t\tvec3 match = vec3(0.0,0.0,0.0);\r\n\t\tfloat best_dot = 8.0;\r\n\t\r\n\t\tfor (int c6=15;c6>=0;c6--) \r\n\t{\r\n\t\tfloat this_dot = distance(c64col[c6]/255.0, col);\r\n\t\tif (this_dot<best_dot) {\r\n\t\t\tbest_dot=this_dot;\r\n\t\t\tmatch=c64col[c6];\r\n\t\t}\r\n\t}\r\n\tvec3 c64_c = vec3(match/255.0);\r\n\tcol = mix(col, c64_c, c64_blend);\r\n}\r\n\r\n\tfragColor = vec4(col, 1.0); \r\n} \r\n")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(8, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("size")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Size :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("size")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(150, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(10000, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("scale")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Scale :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("scale")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0.09999999999999999, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("d_blend")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Dithering blend :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("dithering blend")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("p_blend")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Pixelation blend :")
        del param

    param = lastNode.getParam("paramHint3")
    if param is not None:
        param.setValue("pixelisation blend")
        del param

    param = lastNode.getParam("paramDefaultFloat3")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat3")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("c64_blend")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("C64 blend :")
        del param

    param = lastNode.getParam("paramHint4")
    if param is not None:
        param.setValue("C64 blend")
        del param

    param = lastNode.getParam("paramDefaultFloat4")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat4")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat4")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("dithering")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("Enable :")
        del param

    param = lastNode.getParam("paramHint5")
    if param is not None:
        param.setValue("enable dithering")
        del param

    param = lastNode.getParam("paramDefaultBool5")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("pixelation")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("Enable :")
        del param

    param = lastNode.getParam("paramHint6")
    if param is not None:
        param.setValue("enable pixelisation")
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("c64")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("Enable :")
        del param

    param = lastNode.getParam("paramHint7")
    if param is not None:
        param.setValue("enable C64")
        del param

    del lastNode
    # End of node "Shadertoy1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1)
    groupShadertoy1.connectInput(0, groupSource)

    param = groupShadertoy1.getParam("paramValueFloat0")
    group.getParam("Shadertoy1paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat1")
    group.getParam("Shadertoy1paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat2")
    group.getParam("Shadertoy1paramValueFloat2").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat3")
    group.getParam("Shadertoy1paramValueFloat3").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat4")
    group.getParam("Shadertoy1paramValueFloat4").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueBool5")
    group.getParam("Shadertoy1paramValueBool5").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueBool6")
    group.getParam("Shadertoy1paramValueBool6").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueBool7")
    group.getParam("Shadertoy1paramValueBool7").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Crok_dithering_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
