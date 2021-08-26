#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from psychopy import visual, core, event, gui
from random import shuffle, random
from datetime import datetime

# Enter the colours you want as values, and the keys you want them to match to as the keys
key_bindings = {'f': 'red', 'g': 'blue', 'h': 'green', 'j': 'yellow'}

# Set our escape key to anything except the spacebar
# If you don't want an escape key, set this to 'False'
escape_key = 'escape'

# Choose how many trials there should be between breaks
# If you don't want any breaks, set this to 'False'
break_timer = 20

# If inverted commas are used in either of the two above variables,
# when they shouldn't be, they'll be incorrectly read as strings
# Evaluating them lets them be read as boolean or integer
# Done in a try statement because eval() throws an error if it's given a non-string
try:
    escape_key = eval(escape_key)
except:
    # If eval causes an error, that should mean it was set to 'False' without inverted commas
    # If so, nothing needs to be done
    pass

try:
    break_timer = eval(break_timer)
except:
    pass


# Generate stand-alone lists of the keys and colours
keys = list(key_bindings.keys())
colours = list(key_bindings.values())


# Now we generate our total list of keys the user can use in the experiment
# Generate a list of the keys in uppercase
keys_upper = [x.upper() for x in keys]

# Add our lists of keys together
keys_total = keys + keys_upper
# Only add the escape key if it's been set
if escape_key:
    keys_total.append(escape_key)


# Here we generate the stimuli for all our trials
# First, create an empty list to house them all
stimuli = []

# Run through the colours to get our word, extracting the item and it's index
for idx, word in enumerate(colours):

    # Extract the matching letter from the keys list
    key = keys[idx]

    # Run through the colours list again to get our colour
    for colour in colours:
        if word == colour:
            # If the word matches the colour, we want 15 trials
            num = 15
            # And the condition is congruent
            condition = 'congruent'
        else:
            # If they don't match, we want 5 trials and the condition is incongruent
            num = 5
            condition = 'incongruent'

        # Create the correct number of trials
        for i in range(num):

            # Add the details we've generated to a list for this trial
            trial_info = [word, colour, key, condition]
            # Add that trial to our stimuli list
            stimuli.append(trial_info)

# Randomise the order of trials
shuffle(stimuli)


# Ge information from the participant and set up our output file
# Create variables to hold the participant information
partinfo = {}
partinfo['Experiment name'] = 'Stroop Task Experiment'
partinfo['ID'] = ''
partinfo['Experiment date'] = datetime.now().strftime('%Y%m%d_%H%M')

# Show dialog for participant information to be entered
dlg = gui.DlgFromDict(partinfo,
                      title='Participant Info',
                      fixed=['Experiment name', 'Experiment date'],
                      order=['Experiment name', 'Experiment date', 'ID'])

# If the OK button in the dialog isn't pressed, close the experiment
if not dlg.OK:
    print("Experiment cancelled by user")
    core.quit()

# Generate a .csv filename based on the time and participant info
filename = f"{partinfo['Experiment date']}_P{partinfo['ID']}.csv"

# Create an output file, placing it in our output directory
f = open(filename, 'w')

# Write out our header
f.write('trialnum,colourtext,colourname,condition,response,rt,correct\n')


# Create our window
win = visual.Window([1024, 768], units="pix",
                    fullscr=True, allowGUI=False,
                    color=(-1.0, -1.0, -1.0))

# Here we create all the things we'll be dislaying during the experiment
# Create our fixation cross
fix = visual.TextStim(win, '+', color=(1.0, 1.0, 1.0))

# Create an empty text stimulus to display our stimuli
text = visual.TextStim(win, '', height=35)

# Create two variables to present in the break
break_txt = 'Feel free to take a break'
cont_txt = 'Please press the spacebar to continue'

# Turn them into psychopy text simuli
break_txt_stim = visual.TextStim(win, f'{break_txt:^30}', height=25, pos=(0, 25))
cont_txt_stim = visual.TextStim(win, f'{cont_txt:^30}', height=25, pos=(0, -25))

# Create the stimuli we'll show at the end of the experiment
thanks = visual.TextStim(win, '''The experiment is over, thank you for taking part!\n
This window will close automatically''', height=25)

# Create the variables for our text we'll show in the introduction
welcome = 'Welcome to this Stroop Test Experiment'

intro1 = '''You will be presented with a series of words. Sometimes the colour of the text will match the
word being presented, sometimes it won't.
You must press the button which corresponds with the colour presented, ignoring the word'''

escape_text = f"You can press the '{escape_key}' key at any time to end the experiment"

break_text = f'You will be given a break every {break_timer} trials, you can take as long as you want for each break'

# Creates a sentence for each of our key/colour pairs and adds it to a string
key_bindings_text = ''

for key, value in key_bindings.items():
    temp = f"If the colour of the text is {value} press the '{key}' key.\n"

    key_bindings_text += temp

# Generate an example based on some of the stimuli they'll be seeing
example = f"""For example, if you had a word that says '{colours[1]}'
and the colour of the text was {colours[0]}, you would press the '{keys[0]}' key
"""


# Create a text stimulus that will display our text in the intro
# Assign it to our first piece of text and show it
intro = visual.TextStim(win, text=welcome, pos=(0, 330))
intro.draw()

# Create a list for the positioning of everything on our intro page, and one of all the text we'll display
positions = [-120, -160, -115, -85, -85, -85]
intro_texts = [intro1, key_bindings_text, example, escape_text, break_text, cont_txt]

# Run through both the position and texts lists
# zip allows us to iterate through two lists at once by returning a tuple
for pos, intro_text in zip(positions, intro_texts):
    # If the escape key or break timer is set to False, we wont display their text
    # Because we're moving each text relative to the one before,
    # skipping these still leaves the other text without any weird gaps
    if intro_text == escape_text and not escape_key:
        continue
    elif intro_text == break_text and not break_timer:
        continue

    # For each intro text, we set our stimulus to the text, move it as necessary, and draw it
    intro.setText(intro_text)
    intro.pos += (0, pos)
    intro.draw()

# Display the introduction page now everything's been displayed on it
win.flip()


# Let them start the experiment by pressing the spacebar or escape keys
start = event.waitKeys(keyList=['space', 'escape'])

# If the escape key is pressed, quit the experiment
if start[0] == escape_key:
    print("User requested to quit: ending experiment")
    win.close()
    core.quit()


# Set the trial number to 1 at the beginning of the experiment
trialnum = 1

# Run through our stimuli list
for stimulus in stimuli:

    # This controls our periodic breaks
    # If the break_timer is set to False it won't run
    if break_timer:
        # Run when it gets to a multiple of the break timer
        if trialnum % break_timer == 0 and (not trialnum == len(stimuli)):

            # Display the break text
            break_txt_stim.draw()
            cont_txt_stim.draw()
            win.flip()

            # Let them end the break by pressing the spacebar or escape key
            end_break = event.waitKeys(keyList=['space', 'escape'])

            # If the escape key is pressed, quit the experiment
            if end_break[0] == escape_key:
                print("User requested to quit: ending experiment")
                f.close()
                win.close()
                core.quit()

    # Draw the fixation cross for a random amount of time between 0.5 and 1.5 seconds
    fix.draw()
    win.flip()
    core.wait(random() + 0.5)

    # Extract the trial information from the trial list
    word, colour, correct_key, congruency = stimulus

    # Set our word and colour for this trial
    text.setText(word)
    text.setColor(colour)

    # Draw the stimuli, and save the time it was drawn
    text.draw()
    drawtime = win.flip()

    # Wait until one of the correct keys is pressed, recording the time this was done
    response = event.waitKeys(keyList=keys_total, timeStamped=True)

    # Extract the key and time from the response
    key, keytime = response[0]

    # Convert the key to lowecase to use
    key = key.lower()

    # If the escape key is pressed, end the experiment
    if key == escape_key:
        print("User requested to quit: ending experiment")
        f.close()
        win.close()
        core.quit()

    # Extract the colour from the key pressed by querying the key_bindings dictionary
    # If the key somehow isn't associated with a colour, throw up an error message
    answer_colour = key_bindings.get(key, 'ERROR: Key pressed is not associated with a colour')

    # Calculate the reaction time
    rt = keytime - drawtime

    # If the answered colour is the same as the actual colour, set correct to True
    # Otherwise set it to false
    correct = answer_colour == colour

    # Write out the results of this trial to our log file
    f.write(f'{trialnum},{word},{colour},{congruency},{answer_colour},{rt:.6f},{correct}\n')
    f.flush()

    # Increase the trial number after each trial
    trialnum += 1


# After the main experiment has ended, draw a fixation cross for a second
fix.draw()
win.flip()
core.wait(1)

# Draw our ending page for 3 seconds
thanks.draw()
win.flip()
core.wait(3)

# Close the output file and end the experiment
f.close()
win.close()
core.quit()
