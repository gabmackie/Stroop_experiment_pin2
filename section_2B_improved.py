#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from glob import glob
from os.path import join, splitext, basename
import numpy as np
import matplotlib.pyplot as plt
import csv

# Create a list of all the participant folders in our chosen folder
# REPLACE THIS WITH YOUR FOLDER
filepath = 'C:/Users/gabri/Documents/Programming/pin_assessment2/data'

# Create a list with all .csv files in that folder
data_files = sorted(glob(join(filepath, '*.csv')))

# Take the number of participants from the number of files
num_sub = len(data_files)

# Print the number of participants
print(f'The number of participants in this analysis is {num_sub}\n')

# Print headers for our table
print('|    Participant    |              Congruent               |             Incongruent              |')
print('|                   |  Mean (RT)  |  Stddev (RT)  |   %    |  Mean (RT)  |  Stddev (RT)  |   %    |')

# Create lists to hold our mean RTs and percentages
con_means = []
incon_means = []
con_accuracy = []
incon_accuracy = []


# Run individual analysis on each participant
for file in data_files:
    # Extract the subject ID
    sub_id = splitext(basename(file))[0]

    # Create lists to hold our data from this participant
    con_rts = []
    incon_rts = []
    con_acc = []
    incon_acc = []

    # Start a with statment to open the file inside
    with open(file, newline='') as csvfile:
        # Read the file and assign it to the variable reader
        reader = csv.DictReader(csvfile)
        
        # Run through each row in the file
        for row in reader:        
            # If the condition is congruent
            if row['condition'] == 'congruent':
                # Add the reaction time and accuracy to their respective lists
                # Convert the RT to a float and evaluate the accuracy as a Boolean
                con_rts.append(float(row['rt']))
                con_acc.append(eval(row['correct']))
    
            # If the condition is incongruent, do the same for the incongruent lists
            elif row['condition'] == 'incongruent':
                incon_rts.append(float(row['rt']))
                incon_acc.append(eval(row['correct']))
    
            # If the condition doesn't match either, show an warning message
            else:
                print('WARNING: Trial does not match either condition')

    # Convert the congruent RTs to a numpy aray and calculate their mean and SD
    con_rts = np.array(con_rts)
    con_ave = np.mean(con_rts)
    con_sd = np.std(con_rts)

    # Do the same for the incongruent RTs
    incon_rts = np.array(incon_rts)
    incon_ave = np.mean(incon_rts)
    incon_sd = np.std(incon_rts)

    # Calculate the percentage accuracy for each condition by dividing the
    # number of True values by the total number of values and multiplying by 100
    con_percent = sum(con_acc) / len(con_acc) * 100
    incon_percent = sum(incon_acc) / len(incon_acc) * 100

    # Print all this participants stats in the table, formatted neatly
    print(f'| {sub_id:^17} | {con_ave:^11.3f} | {con_sd:^13.3f} | {con_percent:^6.2f} |', end='')
    print(f' {incon_ave:^11.3f} | {incon_sd:^13.3f} | {incon_percent:^6.2f} |')

    # Add the stats for this participant to our overall lists
    con_means.append(con_ave)
    incon_means.append(incon_ave)
    con_accuracy.append(con_percent)
    incon_accuracy.append(incon_percent)


# Convert the lists with the participant details into numpy arrays
con_means = np.array(con_means)
incon_means = np.array(incon_means)
con_accuracy = np.array(con_accuracy)
incon_accuracy = np.array(incon_accuracy)

# Calculate and print total means for our mean, SD and accuracy
tot_con_ave = np.mean(con_means)
tot_con_sd = np.std(con_means)

tot_incon_ave = np.mean(incon_means)
tot_incon_sd = np.mean(incon_means)

tot_con_percent = np.mean(con_accuracy)
tot_incon_percent = np.mean(incon_accuracy)

print(f'|       Total       | {tot_con_ave:^11.3f} | {tot_con_sd:^13.3f} | {tot_con_percent:^6.2f} |', end='')
print(f' {tot_incon_ave:^11.3f} | {tot_incon_sd:^13.3f} | {tot_incon_percent:^6.2f} |')


# Now create our plot
# First, create a figure of a reasonable size
fig = plt.figure(figsize=(8, 8))

# Set our style to ggplot
plt.style.use('ggplot')

# Create a 2 by 2 gridspec to hold our three subplots
# Set the ratios of the rows and columns to be 7:2 and 2:7 respectively,
# meaning the first column is much wider than the second, with the reverse true for rows
# Set all the parameters so everything fits in nicely
gs = fig.add_gridspec(2, 2,  width_ratios=(7, 2), height_ratios=(2, 7),
                      left=0.13, right=0.95, bottom=0.15, top=0.85,
                      wspace=0.05, hspace=0.05)

# Add our three subjplots, positioning them with gridspec coordinates
# ax is going to be our main plot
ax = fig.add_subplot(gs[1, 0])
# Then we'll have two other subplots for more direct comparison of conditions
# Going forward, notation mentioning subplots is referring to these two
p_rts = fig.add_subplot(gs[0, 0], sharex=ax)
p_acc = fig.add_subplot(gs[1, 1], sharey=ax)


# On the main plot, add the two conditions as scatter plots of different colours
# Each point represents a single person in a single condition
# Both conditions are shown for easier comparison between them
# For each, mean RT is plotted against mean accuracy
ax.scatter(con_means, con_accuracy, color='red', edgecolors='black', s=50)
ax.scatter(incon_means, incon_accuracy, color='blue', edgecolors='black', s=50)

# Combine the RTs for both conditions and plot them as violin plots above our main plot
both_means = [con_means, incon_means]
plot1 = p_rts.violinplot(both_means, vert=False, showmeans=True)

# Combine the accuracies for both conditons and plot them as violin plots to the right of our main plot
both_accuracy = [con_accuracy, incon_accuracy]
plot2 = p_acc.violinplot(both_accuracy, showmeans=True)


# Now adjust the aesthetics and layout of our plots
# First we'll set the colours for specific violins in our subplots
# For lists, our colours match our main plot, and parts are the various sections of a violin plot
colors = ['red', 'blue']
parts = ['cmeans', 'cmins', 'cmaxes', 'cbars']

# We want to change the colours for both of our plots
for plot in (plot1, plot2):
    # Set the colour of the main body to match the conditions
    # using zip to iterate through both colour and part of the plot
    for patch, color in zip(plot['bodies'], colors):
        # Set the colour of the body (patch) of the violin plot so it matches the condition
        patch.set_color(color)

    # Now set all the other parts of the violin plot to black
    for part in parts:
        # Set 'patch' to each specific part of our plot
        patch = plot[part]

        # Then set its colour to black and opacity to 50%
        patch.set_color('black')
        patch.set_alpha(0.5)


# Add labels and a legend to the main plot
ax.set_ylabel('Percentage of trials correct (%)')
ax.set_xlabel('Reaction time (s)')
ax.legend(['Congruent', 'Incongruent'])

# Remove the bottom and left axis labels for the top and right subplots respectively,
# because these would overlap with our main plot
p_rts.tick_params(axis='x', labelbottom=False)
p_acc.tick_params(axis='y', labelleft=False)

# Add labels to our subplots, rotating when necessary for legibility
p_acc.set_xticks([1, 2])
p_acc.set_xticklabels(['Congruent', 'Incongruent'], rotation=65)
p_rts.set_yticks([1, 2])
p_rts.set_yticklabels(['Congruent', 'Incongruent'])

# Create the title and show it above the top subplot
t1 = 'Mean Stroop Test Results. Plotting Reaction Time '
t2 = 'Against Accuracy (main),\nGroup Reaction Time (above) and Group Accuracy (right)'

p_rts.set_title(t1 + t2, size=12)

# Save the figure to our folder
plt.savefig('group.png', dpi=300)

# Show the figure
plt.show()
