#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 十一月 07, 2020, at 15:40
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'older_version_IORpsychopy'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='\\\\Mac\\Home\\Desktop\\IORpsychopy\\older_version_IORpsychopy_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='IORmonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text='default text',
    font='Arial',
    pos=(-9, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start = keyboard.Keyboard()
text= "              欢迎参加本次实验！\n \
        实验开始时会出现两个方块和一个十字，请正视十字。\n " \
       "50ms后一个方框会随机出现在左边或者右边，然后一\n \
       段时间后一个目标黑色圆形会出现，你的任务是尽快的选\n \
       择目标黑色圆形图案的方向，方向键左键代表目标在左边，\n \
       方向键右键代表目标在右边。目标方块可能会现也可能不出现，\n \
       不出现的情况下不需要按任何键。请注意，方框的位置和目标 \n \
       黑色圆形图案的位置无关。\n \
                     ——按空格开始——"

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
cross_fixation = visual.ShapeStim(
    win=win, name='cross_fixation', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
square_left_fixation = visual.Rect(
    win=win, name='square_left_fixation',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(-5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
square_right_fixation = visual.Rect(
    win=win, name='square_right_fixation',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "cue"
cueClock = core.Clock()
cross_cue = visual.ShapeStim(
    win=win, name='cross_cue', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
square_left_cue = visual.Rect(
    win=win, name='square_left_cue',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(-5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
suqare_right_cue = visual.Rect(
    win=win, name='suqare_right_cue',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
cue_square = visual.Rect(
    win=win, name='cue_square',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "target"
targetClock = core.Clock()
cross_target = visual.ShapeStim(
    win=win, name='cross_target', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
square_left_target = visual.Rect(
    win=win, name='square_left_target',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(-5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
square_right_target = visual.Rect(
    win=win, name='square_right_target',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Targetcircle_target = visual.Polygon(
    win=win, name='Targetcircle_target',
    edges=200, size=(0.7, 0.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
resp = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
restText = visual.TextStim(win=win, name='restText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='感谢您参与本次实验。\n请告知实验人员，耐心等待。',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
instrText.setText(text)
start.keys = []
start.rt = []
_start_allKeys = []
# keep track of which components have finished
instructionComponents = [instrText, start]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    
    # *start* updates
    waitOnFlip = False
    if start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start.frameNStart = frameN  # exact frame index
        start.tStart = t  # local t and not account for scr refresh
        start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start, 'tStartRefresh')  # time at next scr refresh
        start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start.clock.reset)  # t=0 on next screen flip
    if start.status == STARTED and not waitOnFlip:
        theseKeys = start.getKeys(keyList=['space'], waitRelease=False)
        _start_allKeys.extend(theseKeys)
        if len(_start_allKeys):
            start.keys = _start_allKeys[-1].name  # just the last key pressed
            start.rt = _start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
n_blocks = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='n_blocks')
thisExp.addLoop(n_blocks)  # add the loop to the experiment
thisN_block = n_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisN_block.rgb)
if thisN_block != None:
    for paramName in thisN_block:
        exec('{} = thisN_block[paramName]'.format(paramName))

for thisN_block in n_blocks:
    currentLoop = n_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisN_block.rgb)
    if thisN_block != None:
        for paramName in thisN_block:
            exec('{} = thisN_block[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=15, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condition.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [cross_fixation, square_left_fixation, square_right_fixation]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_fixation* updates
            if cross_fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                cross_fixation.frameNStart = frameN  # exact frame index
                cross_fixation.tStart = t  # local t and not account for scr refresh
                cross_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_fixation, 'tStartRefresh')  # time at next scr refresh
                cross_fixation.setAutoDraw(True)
            if cross_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_fixation.tStop = t  # not accounting for scr refresh
                    cross_fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross_fixation, 'tStopRefresh')  # time at next scr refresh
                    cross_fixation.setAutoDraw(False)
            
            # *square_left_fixation* updates
            if square_left_fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_left_fixation.frameNStart = frameN  # exact frame index
                square_left_fixation.tStart = t  # local t and not account for scr refresh
                square_left_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_left_fixation, 'tStartRefresh')  # time at next scr refresh
                square_left_fixation.setAutoDraw(True)
            if square_left_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_left_fixation.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    square_left_fixation.tStop = t  # not accounting for scr refresh
                    square_left_fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_left_fixation, 'tStopRefresh')  # time at next scr refresh
                    square_left_fixation.setAutoDraw(False)
            
            # *square_right_fixation* updates
            if square_right_fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_right_fixation.frameNStart = frameN  # exact frame index
                square_right_fixation.tStart = t  # local t and not account for scr refresh
                square_right_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_right_fixation, 'tStartRefresh')  # time at next scr refresh
                square_right_fixation.setAutoDraw(True)
            if square_right_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_right_fixation.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    square_right_fixation.tStop = t  # not accounting for scr refresh
                    square_right_fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_right_fixation, 'tStopRefresh')  # time at next scr refresh
                    square_right_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('cross_fixation.started', cross_fixation.tStartRefresh)
        trials.addData('cross_fixation.stopped', cross_fixation.tStopRefresh)
        trials.addData('square_left_fixation.started', square_left_fixation.tStartRefresh)
        trials.addData('square_left_fixation.stopped', square_left_fixation.tStopRefresh)
        trials.addData('square_right_fixation.started', square_right_fixation.tStartRefresh)
        trials.addData('square_right_fixation.stopped', square_right_fixation.tStopRefresh)
        
        # ------Prepare to start Routine "cue"-------
        continueRoutine = True
        routineTimer.add(0.050000)
        # update component parameters for each repeat
        cue_square.setPos((cueX, 0))
        # keep track of which components have finished
        cueComponents = [cross_cue, square_left_cue, suqare_right_cue, cue_square]
        for thisComponent in cueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cue"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cueClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cueClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_cue* updates
            if cross_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_cue.frameNStart = frameN  # exact frame index
                cross_cue.tStart = t  # local t and not account for scr refresh
                cross_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_cue, 'tStartRefresh')  # time at next scr refresh
                cross_cue.setAutoDraw(True)
            if cross_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_cue.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_cue.tStop = t  # not accounting for scr refresh
                    cross_cue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross_cue, 'tStopRefresh')  # time at next scr refresh
                    cross_cue.setAutoDraw(False)
            
            # *square_left_cue* updates
            if square_left_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_left_cue.frameNStart = frameN  # exact frame index
                square_left_cue.tStart = t  # local t and not account for scr refresh
                square_left_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_left_cue, 'tStartRefresh')  # time at next scr refresh
                square_left_cue.setAutoDraw(True)
            if square_left_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_left_cue.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    square_left_cue.tStop = t  # not accounting for scr refresh
                    square_left_cue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square_left_cue, 'tStopRefresh')  # time at next scr refresh
                    square_left_cue.setAutoDraw(False)
            
            # *suqare_right_cue* updates
            if suqare_right_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                suqare_right_cue.frameNStart = frameN  # exact frame index
                suqare_right_cue.tStart = t  # local t and not account for scr refresh
                suqare_right_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(suqare_right_cue, 'tStartRefresh')  # time at next scr refresh
                suqare_right_cue.setAutoDraw(True)
            if suqare_right_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > suqare_right_cue.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    suqare_right_cue.tStop = t  # not accounting for scr refresh
                    suqare_right_cue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(suqare_right_cue, 'tStopRefresh')  # time at next scr refresh
                    suqare_right_cue.setAutoDraw(False)
            
            # *cue_square* updates
            if cue_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cue_square.frameNStart = frameN  # exact frame index
                cue_square.tStart = t  # local t and not account for scr refresh
                cue_square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue_square, 'tStartRefresh')  # time at next scr refresh
                cue_square.setAutoDraw(True)
            if cue_square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue_square.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    cue_square.tStop = t  # not accounting for scr refresh
                    cue_square.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cue_square, 'tStopRefresh')  # time at next scr refresh
                    cue_square.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cue"-------
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('cross_cue.started', cross_cue.tStartRefresh)
        trials.addData('cross_cue.stopped', cross_cue.tStopRefresh)
        trials.addData('square_left_cue.started', square_left_cue.tStartRefresh)
        trials.addData('square_left_cue.stopped', square_left_cue.tStopRefresh)
        trials.addData('suqare_right_cue.started', suqare_right_cue.tStartRefresh)
        trials.addData('suqare_right_cue.stopped', suqare_right_cue.tStopRefresh)
        trials.addData('cue_square.started', cue_square.tStartRefresh)
        trials.addData('cue_square.stopped', cue_square.tStopRefresh)
        
        # ------Prepare to start Routine "target"-------
        continueRoutine = True
        # update component parameters for each repeat
        Targetcircle_target.setPos((targetX, 0))
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        targetComponents = [cross_target, square_left_target, square_right_target, Targetcircle_target, resp]
        for thisComponent in targetComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        targetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "target"-------
        while continueRoutine:
            # get current time
            t = targetClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=targetClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_target* updates
            if cross_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_target.frameNStart = frameN  # exact frame index
                cross_target.tStart = t  # local t and not account for scr refresh
                cross_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_target, 'tStartRefresh')  # time at next scr refresh
                cross_target.setAutoDraw(True)
            
            # *square_left_target* updates
            if square_left_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_left_target.frameNStart = frameN  # exact frame index
                square_left_target.tStart = t  # local t and not account for scr refresh
                square_left_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_left_target, 'tStartRefresh')  # time at next scr refresh
                square_left_target.setAutoDraw(True)
            
            # *square_right_target* updates
            if square_right_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_right_target.frameNStart = frameN  # exact frame index
                square_right_target.tStart = t  # local t and not account for scr refresh
                square_right_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_right_target, 'tStartRefresh')  # time at next scr refresh
                square_right_target.setAutoDraw(True)
            
            # *Targetcircle_target* updates
            if Targetcircle_target.status == NOT_STARTED and tThisFlip >= SOA-frameTolerance:
                # keep track of start time/frame for later
                Targetcircle_target.frameNStart = frameN  # exact frame index
                Targetcircle_target.tStart = t  # local t and not account for scr refresh
                Targetcircle_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Targetcircle_target, 'tStartRefresh')  # time at next scr refresh
                Targetcircle_target.setAutoDraw(True)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= SOA-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            if targetX == 200:
                if t >= SOA:
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in targetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "target"-------
        for thisComponent in targetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('cross_target.started', cross_target.tStartRefresh)
        trials.addData('cross_target.stopped', cross_target.tStopRefresh)
        trials.addData('square_left_target.started', square_left_target.tStartRefresh)
        trials.addData('square_left_target.stopped', square_left_target.tStopRefresh)
        trials.addData('square_right_target.started', square_right_target.tStartRefresh)
        trials.addData('square_right_target.stopped', square_right_target.tStopRefresh)
        trials.addData('Targetcircle_target.started', Targetcircle_target.tStartRefresh)
        trials.addData('Targetcircle_target.stopped', Targetcircle_target.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp.keys',resp.keys)
        trials.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
        trials.addData('resp.started', resp.tStartRefresh)
        trials.addData('resp.stopped', resp.tStopRefresh)
        # the Routine "target" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 15 repeats of 'trials'
    
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    restTime = '离休息结束还有 30 秒'
    # keep track of which components have finished
    restComponents = [restText]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *restText* updates
        if restText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            restText.frameNStart = frameN  # exact frame index
            restText.tStart = t  # local t and not account for scr refresh
            restText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(restText, 'tStartRefresh')  # time at next scr refresh
            restText.setAutoDraw(True)
        if restText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > restText.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                restText.tStop = t  # not accounting for scr refresh
                restText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(restText, 'tStopRefresh')  # time at next scr refresh
                restText.setAutoDraw(False)
        if restText.status == STARTED:  # only update if drawing
            restText.setText(restTime, log=False)
        timer = str(f'{30-t:.0f}')
        restTime = "离休息结束还有 {} 秒".format(timer)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    n_blocks.addData('restText.started', restText.tStartRefresh)
    n_blocks.addData('restText.stopped', restText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'n_blocks'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [endText]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
