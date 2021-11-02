/******************** 
 * Iorpsychopy Test *
 ********************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'deg',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'IORpsychopy';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionRoutineBegin());
flowScheduler.add(instructionRoutineEachFrame());
flowScheduler.add(instructionRoutineEnd());
const n_blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(n_blocksLoopBegin, n_blocksLoopScheduler);
flowScheduler.add(n_blocksLoopScheduler);
flowScheduler.add(n_blocksLoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'condition.xlsx', 'path': 'condition.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructionClock;
var instrText;
var instrkesp;
var fixationClock;
var rightSquare;
var leftSquare;
var fixation_fixation;
var cueClock;
var CueSquare;
var cueSquareleft;
var cueSquareright;
var fixation_cue;
var targetClock;
var suqare_target_left;
var square_target_right;
var fixation_target;
var target_circle;
var resp;
var restClock;
var Resttext;
var endClock;
var endText;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  instrText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrText',
    text: '欢迎参加本次实验！\n\n实验开始时会出现两个方块和一个十字，请\n正视十字。50ms后一个方框会随机出现在\n左边或者右边，然后一段时间后一个目标黑\n色圆形会出现，你的任务是尽快的选择目标\n黑色圆形图案的方向，方向键左键代表目标\n在左边，方向键右键代表目标在右边。目标\n方块可能会出现也可能不出现，不出现的情\n况下不需要按任何键。请注意，方框的位置\n和目标黑色圆形图案的位置无关。\n\n——按空格开始——',
    font: 'Arial',
    units: 'deg', 
    pos: [0, 0], height: 5,  wrapWidth: 0, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instrkesp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  rightSquare = new visual.Rect ({
    win: psychoJS.window, name: 'rightSquare', units : 'height', 
    width: [1, 1][0], height: [1, 1][1],
    ori: 0, pos: [5, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  leftSquare = new visual.Rect ({
    win: psychoJS.window, name: 'leftSquare', units : 'height', 
    width: [1, 1][0], height: [1, 1][1],
    ori: 0, pos: [(- 5), 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fixation_fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_fixation', 
    vertices: 'cross', size:[0.5, 0.5],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "cue"
  cueClock = new util.Clock();
  CueSquare = new visual.Rect ({
    win: psychoJS.window, name: 'CueSquare', 
    width: [1.5, 1.5][0], height: [1.5, 1.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  cueSquareleft = new visual.Rect ({
    win: psychoJS.window, name: 'cueSquareleft', 
    width: [1, 1][0], height: [1, 1][1],
    ori: 0, pos: [(- 5), 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  cueSquareright = new visual.Rect ({
    win: psychoJS.window, name: 'cueSquareright', 
    width: [1, 1][0], height: [1, 1][1],
    ori: 0, pos: [5, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  fixation_cue = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_cue', 
    vertices: 'cross', size:[0.5, 0.5],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  // Initialize components for Routine "target"
  targetClock = new util.Clock();
  suqare_target_left = new visual.Rect ({
    win: psychoJS.window, name: 'suqare_target_left', 
    width: [1, 1][0], height: [1, 1][1],
    ori: 0, pos: [(- 5), 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  square_target_right = new visual.Rect ({
    win: psychoJS.window, name: 'square_target_right', 
    width: [1, 1][0], height: [1, 1][1],
    ori: 0, pos: [5, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  fixation_target = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_target', 
    vertices: 'cross', size:[0.5, 0.5],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  target_circle = new visual.Polygon ({
    win: psychoJS.window, name: 'target_circle', 
    edges: 1000, size:[0.7, 0.7],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rest"
  restClock = new util.Clock();
  Resttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'Resttext',
    text: 'Take a break',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.5,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  endText = new visual.TextStim({
    win: psychoJS.window,
    name: 'endText',
    text: '谢谢您参与本次实验',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.5,  wrapWidth: 1, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _instrkesp_allKeys;
var instructionComponents;
function instructionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instruction'-------
    t = 0;
    instructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instrkesp.keys = undefined;
    instrkesp.rt = undefined;
    _instrkesp_allKeys = [];
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(instrText);
    instructionComponents.push(instrkesp);
    
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instruction'-------
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrText* updates
    if (t >= 0.0 && instrText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrText.tStart = t;  // (not accounting for frame time here)
      instrText.frameNStart = frameN;  // exact frame index
      
      instrText.setAutoDraw(true);
    }

    
    // *instrkesp* updates
    if (t >= 0.0 && instrkesp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrkesp.tStart = t;  // (not accounting for frame time here)
      instrkesp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      instrkesp.clock.reset();
      instrkesp.start();
      instrkesp.clearEvents();
    }

    if (instrkesp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instrkesp.getKeys({keyList: ['space'], waitRelease: false});
      _instrkesp_allKeys = _instrkesp_allKeys.concat(theseKeys);
      if (_instrkesp_allKeys.length > 0) {
        instrkesp.keys = _instrkesp_allKeys[_instrkesp_allKeys.length - 1].name;  // just the last key pressed
        instrkesp.rt = _instrkesp_allKeys[_instrkesp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instruction'-------
    for (const thisComponent of instructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var n_blocks;
var currentLoop;
function n_blocksLoopBegin(n_blocksLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  n_blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'n_blocks'
  });
  psychoJS.experiment.addLoop(n_blocks); // add the loop to the experiment
  currentLoop = n_blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisN_block of n_blocks) {
    const snapshot = n_blocks.getSnapshot();
    n_blocksLoopScheduler.add(importConditions(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    n_blocksLoopScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    n_blocksLoopScheduler.add(trialsLoopScheduler);
    n_blocksLoopScheduler.add(trialsLoopEnd);
    n_blocksLoopScheduler.add(restRoutineBegin(snapshot));
    n_blocksLoopScheduler.add(restRoutineEachFrame(snapshot));
    n_blocksLoopScheduler.add(restRoutineEnd(snapshot));
    n_blocksLoopScheduler.add(endLoopIteration(n_blocksLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 15, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
    trialsLoopScheduler.add(cueRoutineBegin(snapshot));
    trialsLoopScheduler.add(cueRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(cueRoutineEnd(snapshot));
    trialsLoopScheduler.add(targetRoutineBegin(snapshot));
    trialsLoopScheduler.add(targetRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(targetRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function n_blocksLoopEnd() {
  psychoJS.experiment.removeLoop(n_blocks);

  return Scheduler.Event.NEXT;
}


var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fixation'-------
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(rightSquare);
    fixationComponents.push(leftSquare);
    fixationComponents.push(fixation_fixation);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fixation'-------
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rightSquare* updates
    if (t >= 0.5 && rightSquare.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rightSquare.tStart = t;  // (not accounting for frame time here)
      rightSquare.frameNStart = frameN;  // exact frame index
      
      rightSquare.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((rightSquare.status === PsychoJS.Status.STARTED || rightSquare.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      rightSquare.setAutoDraw(false);
    }
    
    // *leftSquare* updates
    if (t >= 0.5 && leftSquare.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      leftSquare.tStart = t;  // (not accounting for frame time here)
      leftSquare.frameNStart = frameN;  // exact frame index
      
      leftSquare.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((leftSquare.status === PsychoJS.Status.STARTED || leftSquare.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      leftSquare.setAutoDraw(false);
    }
    
    // *fixation_fixation* updates
    if (t >= 0.5 && fixation_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_fixation.tStart = t;  // (not accounting for frame time here)
      fixation_fixation.frameNStart = frameN;  // exact frame index
      
      fixation_fixation.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((fixation_fixation.status === PsychoJS.Status.STARTED || fixation_fixation.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      fixation_fixation.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fixation'-------
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var cueComponents;
function cueRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'cue'-------
    t = 0;
    cueClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.050000);
    // update component parameters for each repeat
    CueSquare.setPos([cueCorr, 0]);
    // keep track of which components have finished
    cueComponents = [];
    cueComponents.push(CueSquare);
    cueComponents.push(cueSquareleft);
    cueComponents.push(cueSquareright);
    cueComponents.push(fixation_cue);
    
    for (const thisComponent of cueComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function cueRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'cue'-------
    // get current time
    t = cueClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *CueSquare* updates
    if (t >= 0 && CueSquare.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CueSquare.tStart = t;  // (not accounting for frame time here)
      CueSquare.frameNStart = frameN;  // exact frame index
      
      CueSquare.setAutoDraw(true);
    }

    frameRemains = 0 + 0.05 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((CueSquare.status === PsychoJS.Status.STARTED || CueSquare.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      CueSquare.setAutoDraw(false);
    }
    
    // *cueSquareleft* updates
    if (t >= 0.0 && cueSquareleft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cueSquareleft.tStart = t;  // (not accounting for frame time here)
      cueSquareleft.frameNStart = frameN;  // exact frame index
      
      cueSquareleft.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.05 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((cueSquareleft.status === PsychoJS.Status.STARTED || cueSquareleft.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      cueSquareleft.setAutoDraw(false);
    }
    
    // *cueSquareright* updates
    if (t >= 0.0 && cueSquareright.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cueSquareright.tStart = t;  // (not accounting for frame time here)
      cueSquareright.frameNStart = frameN;  // exact frame index
      
      cueSquareright.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.05 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((cueSquareright.status === PsychoJS.Status.STARTED || cueSquareright.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      cueSquareright.setAutoDraw(false);
    }
    
    // *fixation_cue* updates
    if (t >= 0.0 && fixation_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cue.tStart = t;  // (not accounting for frame time here)
      fixation_cue.frameNStart = frameN;  // exact frame index
      
      fixation_cue.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.05 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((fixation_cue.status === PsychoJS.Status.STARTED || fixation_cue.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      fixation_cue.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of cueComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function cueRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'cue'-------
    for (const thisComponent of cueComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _resp_allKeys;
var targetComponents;
function targetRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'target'-------
    t = 0;
    targetClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    target_circle.setPos([targetCorr, 0]);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    if ((targetCorr === 200)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    targetComponents = [];
    targetComponents.push(suqare_target_left);
    targetComponents.push(square_target_right);
    targetComponents.push(fixation_target);
    targetComponents.push(target_circle);
    targetComponents.push(resp);
    
    for (const thisComponent of targetComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function targetRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'target'-------
    // get current time
    t = targetClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *suqare_target_left* updates
    if (t >= 0.0 && suqare_target_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      suqare_target_left.tStart = t;  // (not accounting for frame time here)
      suqare_target_left.frameNStart = frameN;  // exact frame index
      
      suqare_target_left.setAutoDraw(true);
    }

    
    // *square_target_right* updates
    if (t >= 0.0 && square_target_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square_target_right.tStart = t;  // (not accounting for frame time here)
      square_target_right.frameNStart = frameN;  // exact frame index
      
      square_target_right.setAutoDraw(true);
    }

    
    // *fixation_target* updates
    if (t >= 0.0 && fixation_target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_target.tStart = t;  // (not accounting for frame time here)
      fixation_target.frameNStart = frameN;  // exact frame index
      
      fixation_target.setAutoDraw(true);
    }

    
    // *target_circle* updates
    if (t >= SOA && target_circle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_circle.tStart = t;  // (not accounting for frame time here)
      target_circle.frameNStart = frameN;  // exact frame index
      
      target_circle.setAutoDraw(true);
    }

    
    // *resp* updates
    if (t >= SOA && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
    }

    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
        resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
        // was this correct?
        if (resp.keys == corrAns) {
            resp.corr = 1;
        } else {
            resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of targetComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function targetRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'target'-------
    for (const thisComponent of targetComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         resp.corr = 1;  // correct non-response
      } else {
         resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('resp.keys', resp.keys);
    psychoJS.experiment.addData('resp.corr', resp.corr);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        routineTimer.reset();
        }
    
    resp.stop();
    // the Routine "target" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var restComponents;
function restRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'rest'-------
    t = 0;
    restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(60.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    restComponents = [];
    restComponents.push(Resttext);
    
    for (const thisComponent of restComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function restRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'rest'-------
    // get current time
    t = restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Resttext* updates
    if (t >= 0.0 && Resttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Resttext.tStart = t;  // (not accounting for frame time here)
      Resttext.frameNStart = frameN;  // exact frame index
      
      Resttext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Resttext.status === PsychoJS.Status.STARTED || Resttext.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Resttext.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of restComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'rest'-------
    for (const thisComponent of restComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var endComponents;
function endRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(endText);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endText* updates
    if (t >= 0.0 && endText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endText.tStart = t;  // (not accounting for frame time here)
      endText.frameNStart = frameN;  // exact frame index
      
      endText.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end'-------
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
