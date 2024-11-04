# Combining the skills

## Theory

### More on Seaborn 
In seaborn there are more ways you can customize the graphs.
I will now use barplot, which will be used in this task, to show these possible customizations.

**Bar plot** is similar visually to a histogram. 
However, with bar plots we usually use categorical data. The plot shows 

The following are possible visual parameters for barplot apart from data and x,y axis:

 - ```hue``` - this can add another dimension to the data. For boxplot, it can distinguish different subcategories of our data for example.  
It uses a column as an input. So when filling x,y and hue, you can compare 3 variables on a 2D plot.
 - ```order, hue_order``` - order of the categorical data to plot
 - ```color``` - color for the bars
 - ```palette``` - colors to use for the different hue variables
 - ```fill``` - if True, use a solid patch, otherwise draws as line art

There are more possible arguments, but these are the main ones that you can play with in terms of visual difference.

## Task

Create single bar chart showing the number of games per 4 specific gaming platforms (PS4, XOne, PC and WiiU) by game genre from the provided dataset.  
Use the knowledge you have acquired from previous lessons.

### Requirements

- Create the plot with ```sns.barplot()```
- The plot should contain only the specified platforms
- The gaming platforms should be ordered as they are in the assignment
- The game genres should be ordered by alphabet in the graph
- There should be a bar for each genre x platform
- The graph should have the default seaborn theme
- The axis should be named ```count``` and ```platform```

