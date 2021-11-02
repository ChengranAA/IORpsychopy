#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Fri Nov  6 18:39:47 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.2')


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
psychopyVersion = '2020.2.5'
expName = 'IORpsychopy'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='/Users/andrewli/Desktop/IORpsychopy/IORpsychopy_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
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
    text='欢迎参加本次实验！\n\n实验开始时会出现两个方块和一个十字，请\n正视十字。50ms后一个方框会随机出现在\n左边或者右边，然后一段时间后一个目标黑\n色圆形会出现，你的任务是尽快的选择目标\n黑色圆形图案的方向，方向键左键代表目标\n在左边，方向键右键代表目标在右边。目标\n方块可能会出现也可能不出现，不出现的情\n况下不需要按任何键。请注意，方框的位置\n和目标黑色圆形图案的位置无关。\n\n——按空格开始——',
    font='Arial',
    units='deg', pos=(0, 0), height=0.5, wrapWidth=5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
instrkesp = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
rightSquare = visual.Rect(
    win=win, name='rightSquare',units='deg', 
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
leftSquare = visual.Rect(
    win=win, name='leftSquare',units='deg', 
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(-5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
fixation_fixation = visual.ShapeStim(
    win=win, name='fixation_fixation', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "cue"
cueClock = core.Clock()
CueSquare = visual.Rect(
    win=win, name='CueSquare',
    width=(1.5, 1.5)[0], height=(1.5, 1.5)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
cueSquareleft = visual.Rect(
    win=win, name='cueSquareleft',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(-5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
cueSquareright = visual.Rect(
    win=win, name='cueSquareright',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
fixation_cue = visual.ShapeStim(
    win=win, name='fixation_cue', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "target"
targetClock = core.Clock()
suqare_target_left = visual.Rect(
    win=win, name='suqare_target_left',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(-5, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
square_target_right = visual.Rect(
    win=win, name='square_target_right',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
fixation_target = visual.ShapeStim(
    win=win, name='fixation_target', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
target_circle = visual.Polygon(
    win=win, name='target_circle',
    edges=1000, size=(0.7, 0.7),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
resp = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
Resttext = visual.TextStim(win=win, name='Resttext',
    text='Take a break',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='谢谢您参与本次实验',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
instrkesp.keys = []
instrkesp.rt = []
_instrkesp_allKeys = []
# keep track of which components have finished
instructionComponents = [instrText, instrkesp]
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
    
    # *instrkesp* updates
    if instrkesp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrkesp.frameNStart = frameN  # exact frame index
        instrkesp.tStart = t  # local t and not account for scr refresh
        instrkesp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrkesp, 'tStartRefresh')  # time at next scr refresh
        instrkesp.status = STARTED
        # keyboard checking is just starting
        instrkesp.clock.reset()  # now t=0
        instrkesp.clearEvents(eventType='keyboard')
    if instrkesp.status == STARTED:
        theseKeys = instrkesp.getKeys(keyList=['space'], waitRelease=False)
        _instrkesp_allKeys.extend(theseKeys)
        if len(_instrkesp_allKeys):
            instrkesp.keys = _instrkesp_allKeys[-1].name  # just the last key pressed
            instrkesp.rt = _instrkesp_allKeys[-1].rt
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
        fixationComponents = [rightSquare, leftSquare, fixation_fixation]
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
            
            # *rightSquare* updates
            if rightSquare.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                rightSquare.frameNStart = frameN  # exact frame index
                rightSquare.tStart = t  # local t and not account for scr refresh
                rightSquare.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightSquare, 'tStartRefresh')  # time at next scr refresh
                rightSquare.setAutoDraw(True)
            if rightSquare.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightSquare.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rightSquare.tStop = t  # not accounting for scr refresh
                    rightSquare.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightSquare, 'tStopRefresh')  # time at next scr refresh
                    rightSquare.setAutoDraw(False)
            
            # *leftSquare* updates
            if leftSquare.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                leftSquare.frameNStart = frameN  # exact frame index
                leftSquare.tStart = t  # local t and not account for scr refresh
                leftSquare.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftSquare, 'tStartRefresh')  # time at next scr refresh
                leftSquare.setAutoDraw(True)
            if leftSquare.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftSquare.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    leftSquare.tStop = t  # not accounting for scr refresh
                    leftSquare.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftSquare, 'tStopRefresh')  # time at next scr refresh
                    leftSquare.setAutoDraw(False)
            
            # *fixation_fixation* updates
            if fixation_fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                fixation_fixation.frameNStart = frameN  # exact frame index
                fixation_fixation.tStart = t  # local t and not account for scr refresh
                fixation_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_fixation, 'tStartRefresh')  # time at next scr refresh
                fixation_fixation.setAutoDraw(True)
            if fixation_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_fixation.tStop = t  # not accounting for scr refresh
                    fixation_fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation_fixation.setAutoDraw(False)
            
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
        trials.addData('rightSquare.started', rightSquare.tStartRefresh)
        trials.addData('rightSquare.stopped', rightSquare.tStopRefresh)
        trials.addData('leftSquare.started', leftSquare.tStartRefresh)
        trials.addData('leftSquare.stopped', leftSquare.tStopRefresh)
        trials.addData('fixation_fixation.started', fixation_fixation.tStartRefresh)
        trials.addData('fixation_fixation.stopped', fixation_fixation.tStopRefresh)
        
        # ------Prepare to start Routine "cue"-------
        continueRoutine = True
        routineTimer.add(0.050000)
        # update component parameters for each repeat
        CueSquare.setPos((cueCorr, 0))
        # keep track of which components have finished
        cueComponents = [CueSquare, cueSquareleft, cueSquareright, fixation_cue]
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
            
            # *CueSquare* updates
            if CueSquare.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                CueSquare.frameNStart = frameN  # exact frame index
                CueSquare.tStart = t  # local t and not account for scr refresh
                CueSquare.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CueSquare, 'tStartRefresh')  # time at next scr refresh
                CueSquare.setAutoDraw(True)
            if CueSquare.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CueSquare.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    CueSquare.tStop = t  # not accounting for scr refresh
                    CueSquare.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CueSquare, 'tStopRefresh')  # time at next scr refresh
                    CueSquare.setAutoDraw(False)
            
            # *cueSquareleft* updates
            if cueSquareleft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cueSquareleft.frameNStart = frameN  # exact frame index
                cueSquareleft.tStart = t  # local t and not account for scr refresh
                cueSquareleft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cueSquareleft, 'tStartRefresh')  # time at next scr refresh
                cueSquareleft.setAutoDraw(True)
            if cueSquareleft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cueSquareleft.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    cueSquareleft.tStop = t  # not accounting for scr refresh
                    cueSquareleft.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cueSquareleft, 'tStopRefresh')  # time at next scr refresh
                    cueSquareleft.setAutoDraw(False)
            
            # *cueSquareright* updates
            if cueSquareright.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cueSquareright.frameNStart = frameN  # exact frame index
                cueSquareright.tStart = t  # local t and not account for scr refresh
                cueSquareright.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cueSquareright, 'tStartRefresh')  # time at next scr refresh
                cueSquareright.setAutoDraw(True)
            if cueSquareright.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cueSquareright.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    cueSquareright.tStop = t  # not accounting for scr refresh
                    cueSquareright.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cueSquareright, 'tStopRefresh')  # time at next scr refresh
                    cueSquareright.setAutoDraw(False)
            
            # *fixation_cue* updates
            if fixation_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cue.frameNStart = frameN  # exact frame index
                fixation_cue.tStart = t  # local t and not account for scr refresh
                fixation_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cue, 'tStartRefresh')  # time at next scr refresh
                fixation_cue.setAutoDraw(True)
            if fixation_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cue.tStartRefresh + 0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cue.tStop = t  # not accounting for scr refresh
                    fixation_cue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_cue, 'tStopRefresh')  # time at next scr refresh
                    fixation_cue.setAutoDraw(False)
            
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
        trials.addData('CueSquare.started', CueSquare.tStartRefresh)
        trials.addData('CueSquare.stopped', CueSquare.tStopRefresh)
        trials.addData('cueSquareleft.started', cueSquareleft.tStartRefresh)
        trials.addData('cueSquareleft.stopped', cueSquareleft.tStopRefresh)
        trials.addData('cueSquareright.started', cueSquareright.tStartRefresh)
        trials.addData('cueSquareright.stopped', cueSquareright.tStopRefresh)
        trials.addData('fixation_cue.started', fixation_cue.tStartRefresh)
        trials.addData('fixation_cue.stopped', fixation_cue.tStopRefresh)
        
        # ------Prepare to start Routine "target"-------
        continueRoutine = True
        # update component parameters for each repeat
        target_circle.setPos((targetCorr, 0))
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        if targetCorr == 200:
            continueRoutine = False
        # keep track of which components have finished
        targetComponents = [suqare_target_left, square_target_right, fixation_target, target_circle, resp]
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
            
            # *suqare_target_left* updates
            if suqare_target_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                suqare_target_left.frameNStart = frameN  # exact frame index
                suqare_target_left.tStart = t  # local t and not account for scr refresh
                suqare_target_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(suqare_target_left, 'tStartRefresh')  # time at next scr refresh
                suqare_target_left.setAutoDraw(True)
            
            # *square_target_right* updates
            if square_target_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_target_right.frameNStart = frameN  # exact frame index
                square_target_right.tStart = t  # local t and not account for scr refresh
                square_target_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_target_right, 'tStartRefresh')  # time at next scr refresh
                square_target_right.setAutoDraw(True)
            
            # *fixation_target* updates
            if fixation_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_target.frameNStart = frameN  # exact frame index
                fixation_target.tStart = t  # local t and not account for scr refresh
                fixation_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_target, 'tStartRefresh')  # time at next scr refresh
                fixation_target.setAutoDraw(True)
            
            # *target_circle* updates
            if target_circle.status == NOT_STARTED and tThisFlip >= SOA-frameTolerance:
                # keep track of start time/frame for later
                target_circle.frameNStart = frameN  # exact frame index
                target_circle.tStart = t  # local t and not account for scr refresh
                target_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_circle, 'tStartRefresh')  # time at next scr refresh
                target_circle.setAutoDraw(True)
            
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
        trials.addData('suqare_target_left.started', suqare_target_left.tStartRefresh)
        trials.addData('suqare_target_left.stopped', suqare_target_left.tStopRefresh)
        trials.addData('square_target_right.started', square_target_right.tStartRefresh)
        trials.addData('square_target_right.stopped', square_target_right.tStopRefresh)
        trials.addData('fixation_target.started', fixation_target.tStartRefresh)
        trials.addData('fixation_target.stopped', fixation_target.tStopRefresh)
        trials.addData('target_circle.started', target_circle.tStartRefresh)
        trials.addData('target_circle.stopped', target_circle.tStopRefresh)
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
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    restComponents = [Resttext]
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
        
        # *Resttext* updates
        if Resttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Resttext.frameNStart = frameN  # exact frame index
            Resttext.tStart = t  # local t and not account for scr refresh
            Resttext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Resttext, 'tStartRefresh')  # time at next scr refresh
            Resttext.setAutoDraw(True)
        if Resttext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Resttext.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                Resttext.tStop = t  # not accounting for scr refresh
                Resttext.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Resttext, 'tStopRefresh')  # time at next scr refresh
                Resttext.setAutoDraw(False)
        
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
    n_blocks.addData('Resttext.started', Resttext.tStartRefresh)
    n_blocks.addData('Resttext.stopped', Resttext.tStopRefresh)
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
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
