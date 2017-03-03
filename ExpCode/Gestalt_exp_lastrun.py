#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), mei 17, 2016, at 21:32
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Gestalt_exp1'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\Elise\\Dropbox\\GestaltAppreciation\\Gestalt_exp.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1600, 900), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "numInstruc"
numInstrucClock = core.Clock()
instruct2 = visual.TextStim(win=win, ori=0, name='instruct2',
    text='Dit is deel 2 van het experiment. Hierbij zal je telkens 2 afbeeldingen naast mekaar te zien krijgen.&#10;De bedoeling is dat je een schatting maakt van welke afbeelding het meeste aantal dots heeft.&#10;Je hoeft de dots niet te tellen, het is gewoon een ruwe schatting die je maakt.&#10;&#10;Als je vindt dat de linkerafbeelding meer dots heeft, dan druk je op het linkerpijltje.&#10;Als je vindt dat de rechterafbeelding meer dots heeft, dan druk je op het rechterpijltje.&#10;&#10;Als je deze instructies hebt gelezen, druk op spatie. Deel 2 zal dan beginnen.',    font='Arial',
    units='norm', pos=[0, 0], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "numerosity"
numerosityClock = core.Clock()

text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=[0, 0], height=40, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
Left = visual.ImageStim(win=win, name='Left',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[600, 600],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Right = visual.ImageStim(win=win, name='Right',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[600, 600],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "numInstruc"-------
t = 0
numInstrucClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
numInstrucComponents = []
numInstrucComponents.append(instruct2)
numInstrucComponents.append(key_resp_2)
for thisComponent in numInstrucComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "numInstruc"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = numInstrucClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct2* updates
    if t >= 0.0 and instruct2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct2.tStart = t  # underestimates by a little under one frame
        instruct2.frameNStart = frameN  # exact frame index
        instruct2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in numInstrucComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "numInstruc"-------
for thisComponent in numInstrucComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "numInstruc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
numLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condNumerosity.csv'),
    seed=None, name='numLoop')
thisExp.addLoop(numLoop)  # add the loop to the experiment
thisNumLoop = numLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisNumLoop.rgb)
if thisNumLoop != None:
    for paramName in thisNumLoop.keys():
        exec(paramName + '= thisNumLoop.' + paramName)

for thisNumLoop in numLoop:
    currentLoop = numLoop
    # abbreviate parameter names if possible (e.g. rgb = thisNumLoop.rgb)
    if thisNumLoop != None:
        for paramName in thisNumLoop.keys():
            exec(paramName + '= thisNumLoop.' + paramName)
    
    #------Prepare to start Routine "numerosity"-------
    t = 0
    numerosityClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if random()>0.5:&#10;    firstImg=imgA&#10;    secondImg=imgB&#10;    APos=[0, 0.0]&#10;    BPos=[0, 0.0]&#10;    Alocation='left'&#10;else:&#10;    firstImg=imgB&#10;    secondImg=imgA&#10;    APos=[0, 0.0]&#10;    BPos=[0, 0.0]&#10;    Alocation='right'
    Left.setPos(APos)
    Left.setImage(firstImg)
    Right.setPos(BPos)
    Right.setImage(secondImg)
    numResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    numResp.status = NOT_STARTED
    print imgA, imgB
    # keep track of which components have finished
    numerosityComponents = []
    numerosityComponents.append(text)
    numerosityComponents.append(Left)
    numerosityComponents.append(Right)
    numerosityComponents.append(numResp)
    for thisComponent in numerosityComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "numerosity"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = numerosityClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *Left* updates
        if t >= 1 and Left.status == NOT_STARTED:
            # keep track of start time/frame for later
            Left.tStart = t  # underestimates by a little under one frame
            Left.frameNStart = frameN  # exact frame index
            Left.setAutoDraw(True)
        if Left.status == STARTED and t >= (1 + (0.500-win.monitorFramePeriod*0.75)): #most of one frame period left
            Left.setAutoDraw(False)
        
        # *Right* updates
        if t >= 1.5 and Right.status == NOT_STARTED:
            # keep track of start time/frame for later
            Right.tStart = t  # underestimates by a little under one frame
            Right.frameNStart = frameN  # exact frame index
            Right.setAutoDraw(True)
        if Right.status == STARTED and t >= (1.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Right.setAutoDraw(False)
        
        # *numResp* updates
        if t >= 2 and numResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            numResp.tStart = t  # underestimates by a little under one frame
            numResp.frameNStart = frameN  # exact frame index
            numResp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(numResp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if numResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                numResp.keys = theseKeys[-1]  # just the last key pressed
                numResp.rt = numResp.clock.getTime()
                # was this 'correct'?
                if (numResp.keys == str(Alocation)) or (numResp.keys == Alocation):
                    numResp.corr = 1
                else:
                    numResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in numerosityComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "numerosity"-------
    for thisComponent in numerosityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if numResp.keys in ['', [], None]:  # No response was made
       numResp.keys=None
       # was no response the correct answer?!
       if str(Alocation).lower() == 'none': numResp.corr = 1  # correct non-response
       else: numResp.corr = 0  # failed to respond (incorrectly)
    # store data for numLoop (TrialHandler)
    numLoop.addData('numResp.keys',numResp.keys)
    numLoop.addData('numResp.corr', numResp.corr)
    if numResp.keys != None:  # we had a response
        numLoop.addData('numResp.rt', numResp.rt)
    
    # the Routine "numerosity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'numLoop'



win.close()
core.quit()
