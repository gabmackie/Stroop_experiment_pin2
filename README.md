# pin_assessment2
Second assessment from my programming in neuroimaging module. Contains the data, zip file of the original submission, and the code that's been improved based on their feedback.

Below are the instructions I was given for the assessment.

-----------------------------------------------------------

# Programming in NeuroImaging – 2020/21: Assessment 2

For the second assignment in the PiN module, you will be required to produce a
portfolio in three parts.

The overall theme for the assessment is to produce a set of tools to allow your
lab members to run a Stroop task on participants and then to analyse the
resulting data.  The code for the stimulus presentation and data analysis must
be clear, robust and easy to use.  The accompanying documentation must be
sufficient for an undergraduate level RA with no experience of coding to be
able to use the scripts you produce with no further instruction.

Extra marks are available for appropriate commenting of the scripts.  Remember,
comments should not  just say what something does – they should explain why it
does it.

## General Guidelines

Some of the things we are looking for include:

 * Appropriate commenting of the scripts.  Remember, comments should not just
   say what something does – they should explain why it does it.
 * Making your scripts neat and adaptable to other situations – for example, if
   you are asked to input three numbers from a user, use a loop with a counter
   rather than copying and pasting the code three times.
 * Where appropriate, ensuring that you handle bad user input in a robust way –
   for example, making sure that your script doesn't crash if you ask for a
   number and the user types a word
 * Where appropriate, ensuring that any output shown to the user is formatted
   neatly.

### Testing your scripts

*Remember: Test your scripts!*  They must at least run through even if they
don't implement all of the functionality required.  Also, make sure that you
submit the correct version of your scripts - we can only mark what you submit!

### Use of Python Modules

Important note regarding the use of Python modules:  Whilst you have almost
complete freedom to use any Python modules installed at YNiC (including those
which we have not used in the course), you may explicitly not use the “pandas”
module.  The aim of the assessment is to assess your ability to handle data
using the low level numpy and scipy routines and our experience is that
students who use the “pandas” module fail to demonstrate this ability.  Use of
the “pandas” module will result in a mark of 0 for the relevant section of the
assessment.

### Data files for the assessment

Data files for the assessment:  The data files for the assessment are available
either from the VLE, or via a Git repository at
<https://vcs.ynic.york.ac.uk/cn/pin-assessment2>

You can clone the above git repository using:

```
git clone https://vcs.ynic.york.ac.uk/cn/pin-assessment2
```

You will require your YNiC username and password to do this.  If you do not
wish to use git, the same files can be found on the PiN VLE page.

Note that if you download the files from the VLE, the data for section B will
be a zip file (due to VLE limitations).  You should unzip this by hand – you do
not need to use Python to do this.  If you get the data from the git
repository, the files will be ready to use.

## Section A - Present a Stroop task using Psychopy

*40% of the available marks for this assessment*

Produce a Psychopy script which presents a Stroop task.  This is a task in
which the names of colours are presented to a participant.  There are two
conditions: congruent and incongruent.  In the congruent condition, the colour
of the text will match the word being presented.  In the incongruent condition,
the colour of the text will not match the word being presented. The participant
must respond by pressing the button which corresponds the colour presented  –
i.e. they must ignore the word.  You should:

 * Present all stimuli on a black background
 * Present all stimuli in lower case.
 * Use the four colours: red, blue, green, yellow
 * Present a total of 120 trials, broken down as follows:
   * 15 congruent trials for each colour
   * 5 incongruent trials for each other combination of colours
   * An example table of the stimulus combinations follows: ![Example stimuli combinations](_images/stimuli.png)
 * Randomise the order of trial presentation
 * Use the following keys for responses:
   * Red: `f`
   * Blue: `g`
   * Green: `h`
   * Yellow: `j`
 * Record responses and response times in a CSV file with the following headers:
```
trialnum,colourtext,colourname,condition,response,rt,correct
```
 * `trialnum` should run from 1 up to 120
 * `colourtext` should be the word shown in the trial
 * `colourname` should be the colour of the text shown in the trial
 * `condition` should be congruent or incongruent
 * `response` should be the colour name of the response the participant made
 * `rt` should be the reaction time formatted appropriately as a floating point number in seconds
 * `correct` should be True or False

An extract from an example output file may therefore look something like this:

```
trialnum,colourtext,colourname,condition,response,rt,correct
1,red,green,incongruent,green,1.374977,True
2,green,green,congruent,green,0.559735,True
3,yellow,red,incongruent,red,0.756133,True
… many more lines …
120,red,yellow,incongruent,yellow,1.184296,True
```

Some possible enhancements (for extra credit), could be:

 * Get information about the participant from the experimenter before starting
   the task and use this to name your output file.
 * Include a “Ready” screen
 * Give the participant a break every n trials where n is configurable in the
   script.  Consider waiting for the participant to indicate that they are
   ready to continue.

**The aim of this assignment is to produce a script which you would be happy to
deploy in a real laboratory.  Once you have your basic script, try and put
yourself in the place of both the experimenter and the participant and consider
what would make it more professional**

### Submission Requirements for Section A

 * Your script.  Call this `section_A.py`
 * One example output file from your experiment.  Call this `data.csv`

## Section B – Analyse the Stroop task output

*30% of the available marks for this assessment*

For this section, you will be provided with a set of 20 data files generated by
participants who have performed the experiment.  Your script must load in these
data files, analyse the data and plot and display it in the appropriate manner.

Your script should perform the following steps:

  1. Load all of the files in a given directory whose names end with `.csv`.  The
     files will be named for participants `P1` to `P20`.
  2. Print a neat table of the mean and standard deviation for each participant
     in each condition. Format the values with three decimal places.  Also
     print the percentage correct for each participant for each condition to two
     decimal places.
     Finally, below the participant information, print the same values for the
     group.
     The table should be neatly formatted and contain the following columns:
       * Participant
       * Congruent: Mean (RT), Stddev (RT), %
       * Incongruent: Mean (RT), Stddev (RT), %
  3. Plot the distribution of participant means for the congruent and
     incongruent conditions.  Use the most appropriate form of plot for the
     data.  Give the plot an appropriate title and make sure that you label the x
     and y axes appropriately.  Extra marks are available for making the plot look
     production quality.  Your script must save the plot as an image file with the
     name `group.png`.

Note that the files which you write out in Section A of your assessment should
be usable by your script for Section B - i.e. your stimulus presentation and
analysis code should work with each other!

### Submission Requirements for Section B

 * Your script.  Call this `section_B.py`
 * An example of your plot.  Call this `group.png`

## Section C – Document your experiment and analysis

30% of the available marks for this assessment: 1000 words maximum (this is not
a target).

Produce a document in the style of a lab “wiki” page which documents the
following:

  1. What the experiment is.
  2. How the experiment should be run.  This should be in a form that someone
     who has never seen the experimental code can follow.  Write down the
     procedure for starting Psychopy, loading the script and running it. You should
     also include information which is to be given to the participant regarding the
     task (i.e. which keys to use etc)
  3. How to analyse the outputs of the experiment using your analysis script
     When producing this document, it may help to have in mind an Undergraduate
     level Research Assistant who is not familiar with programming or the
     experimental task being performed but will be running participants through the
     procedure.  Extra credit will be given for appropriate inclusion of screenshots
     and/or other appropriate diagrams.  Credit will be given for providing all
     relevant information whilst remaining concise.  

### Submission Requirements for Section B

 * Please submit this section as a PDF – these can be exported from Microsoft
   Word or Libreoffice.  Name the PDF `labwiki.pdf`.
