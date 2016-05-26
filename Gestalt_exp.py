#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Wed 06 Apr 2016 07:57:06 PM CEST
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
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions_1"
Instructions_1Clock = core.Clock()
Instructions = visual.TextStim(win=win, ori=0, name='Instructions',
    text=u'In dit experiment zal je een aantal afbeeldingen zeer kort aangeboden krijgen. Na elke afbeelding zal je een schaal van 1 tot 9 te zien krijgen waarop je moet aanduiden hoe aangenaam je deze afbeelding vond. 1 staat voor helemaal niet aangenaam en 9 zeer aangenaam.\nOok al heb je de afbeelding maar heel kort gezien, probeer toch zo goed mogelijk je voorkeur aan te duiden. Probeer er ook niet te lang over na te denken, volg gewoon je intu\xeftie.\nAls je een vraag hebt over het experiment, roep de proefleider dan even erbij.\n\nAls je deze instructies hebt doorgelezen, mag je op spatie drukken en dan begint het experiment.',    font='Arial',
    units='norm', pos=[0, 0], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "TRIAL_EXP"
TRIAL_EXPClock = core.Clock()
fixationcross = visual.TextStim(win=win, ori=0, name='fixationcross',
    text='+',    font='Arial',
    units='norm', pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[600, 600],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, 0.0], low=1, high=9, labels=[''], scale='Hoe aangenaam vond je deze afbeelding? 1 = helemaal niet aangenaam, 9 = heel aangenaam')

# Initialize components for Routine "numInstruc"
numInstrucClock = core.Clock()
instruct2 = visual.TextStim(win=win, ori=0, name='instruct2',
    text='Dit is deel 2 van het experiment. Hierbij zal je telkens 2 afbeeldingen na elkaar te zien krijgen.\nDe bedoeling is dat je een schatting maakt van welke afbeelding het meeste aantal dots heeft.\nJe hoeft de dots niet te tellen, een ruwe schatting is voldoende.\n\nAls je vindt dat eerste afbeelding meer dots heeft, dan druk je op het linkerpijltje.\nAls je vindt dat de tweede afbeelding meer dots heeft, dan druk je op het rechterpijltje.\n\nAls je deze instructies goed hebt gelezen, druk op spatie. Deel 2 zal dan beginnen.',    font='Arial',
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

mouse = event.Mouse()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
feedback = visual.TextStim(win=win, ori=0, name='feedback',
    text='Het experiment is afgelopen.Je mag de proefleider laten weten dat je het experiment afgerond hebt.\nBedankt om deel te nemen!',    font='Arial',
    units='norm', pos=[0, 0], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instructions_1"-------
t = 0
Instructions_1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
response = event.BuilderKeyResponse()  # create an object of type KeyResponse
response.status = NOT_STARTED
# keep track of which components have finished
Instructions_1Components = []
Instructions_1Components.append(Instructions)
Instructions_1Components.append(response)
for thisComponent in Instructions_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions_1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if t >= 0.0 and Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions.tStart = t  # underestimates by a little under one frame
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.setAutoDraw(True)
    
    # *response* updates
    if t >= 0.0 and response.status == NOT_STARTED:
        # keep track of start time/frame for later
        response.tStart = t  # underestimates by a little under one frame
        response.frameNStart = frameN  # exact frame index
        response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            response.keys = theseKeys[-1]  # just the last key pressed
            response.rt = response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions_1"-------
for thisComponent in Instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if response.keys in ['', [], None]:  # No response was made
   response.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('response.keys',response.keys)
if response.keys != None:  # we had a response
    thisExp.addData('response.rt', response.rt)
thisExp.nextEntry()
# the Routine "Instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'condAppreciation.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "TRIAL_EXP"-------
    t = 0
    TRIAL_EXPClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image.setImage(images)
    rating.reset()
    # keep track of which components have finished
    TRIAL_EXPComponents = []
    TRIAL_EXPComponents.append(fixationcross)
    TRIAL_EXPComponents.append(image)
    TRIAL_EXPComponents.append(rating)
    for thisComponent in TRIAL_EXPComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "TRIAL_EXP"-------
    continueRoutine = True
    mouse.setVisible(0)
    while continueRoutine:
        # get current time
        t = TRIAL_EXPClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        

        # *fixationcross* updates
        if t >= 0.0 and fixationcross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationcross.tStart = t  # underestimates by a little under one frame
            fixationcross.frameNStart = frameN  # exact frame index
            fixationcross.setAutoDraw(True)
        if fixationcross.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixationcross.setAutoDraw(False)
        
        # *image* updates
        if t >= 1 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and t >= (1 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
        # *rating* updates
        if t >= 1.2 and rating.status == NOT_STARTED:
            mouse.setVisible(1)
            # keep track of start time/frame for later
            rating.tStart = t  # underestimates by a little under one frame
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TRIAL_EXPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "TRIAL_EXP"-------
    for thisComponent in TRIAL_EXPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    # the Routine "TRIAL_EXP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


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
    trialList=data.importConditions(u'condNumerosity.csv'),
    seed=None, name='numLoop')
thisExp.addLoop(numLoop)  # add the loop to the experiment
thisNumLoop = numLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisNumLoop.rgb)
if thisNumLoop != None:
    for paramName in thisNumLoop.keys():
        exec(paramName + '= thisNumLoop.' + paramName)

mouse.setVisible(0)
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
    if random()>0.5:
        firstImg=imgA
        secondImg=imgB
        APos=[0, 0.0]
        BPos=[0, 0.0]
        Alocation='left'
    else:
        firstImg=imgB
        secondImg=imgA
        APos=[0, 0.0]
        BPos=[0, 0.0]
        Alocation='right'
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
    numLoop.addData('numResp.Alocation', Alocation)
    if numResp.keys != None:  # we had a response
        numLoop.addData('numResp.rt', numResp.rt)
    
    # the Routine "numerosity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'numLoop'
mouse.setVisible(1)


#------Prepare to start Routine "Feedback"-------
t = 0
FeedbackClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
FeedbackComponents = []
FeedbackComponents.append(feedback)
for thisComponent in FeedbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Feedback"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = FeedbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedback* updates
    if t >= 0.0 and feedback.status == NOT_STARTED:
        # keep track of start time/frame for later
        feedback.tStart = t  # underestimates by a little under one frame
        feedback.frameNStart = frameN  # exact frame index
        feedback.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Feedback"-------
for thisComponent in FeedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
