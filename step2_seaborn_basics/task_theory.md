# Introduction to Seaborn

## Theory

### What is Seaborn?
Seaborn is a Python data visualization library built on top of Matplotlib. 
It provides a high-level interface for creating attractive statistical graphics. 
While Matplotlib gives you complete control over your visualizations, Seaborn focuses on making it easier to create common statistical visualizations.

### Seaborn key advantages
- **Simplified syntax**: optimized functions and default settings for common plot types, it allows you to create visually appealing plots with minimal code
- **Statistical visualizations**: this library is particularly useful for exploring relationships between variables, visualizing distributions, and highlighting patterns in data.
It can create regression plots, correlation heatmaps etc.
- **Attractive visual styles**: It is easy to create aesthetically pleasing graphs with default styles and color palettes

### Importing
Both matplotlib and seaborn have a usual import shorthand.
```python
import seaborn as sns
import matplotlib.pyplot as plt
```


### First drawing
**1. Setting the theme**  
  
You can set the theme to the seaborn one, using ```sns.set_theme()```. This has to be done before creating an axes.  
You can find more possibilities [here](https://seaborn.pydata.org/tutorial/aesthetics.html).

**2. Creating the plot figure and axes**  
  
To create a plot, we usually use the function ```plt.subplots()```.
This is a function from the Matplotlib library, that Seaborn is built on the top of.  
```plt.subplots()``` gives us two objects that are both empty: 
   - ```fig``` - serves as a container for the plots
   - ```ax``` - represents the actual plot/s themselves

Default usage:
```python
   fig, ax = plt.subplots()
```

If we want to put more axes into one figure, we can specify the arguements ```nrows: int, ncols: int```. The ax object then becomes a list, and we can access different axes in the figure using ```ax[0]``` etc.  

If we want to specify the size of the figure, we can use the argument ```figsize: (float,float)``` to set the width and height in inches.

**3. Creating a plot from a dataset**  
  
To create a plot, we need to call the appropriate function.
For example to create a histogram, which can be useful to find out the distribution of our dataset, we would use ```sns.histplot()```  

Plot functions in seaborn usually take our dataset as the first argument, and then name of a column, that is specified as ```x``` or ```y```.  

For example, if we wanted to create a histogram with the distribution of height in a dataset with people, we would call:
```python
sns.histplot(people, x='Height')
```

If we want to specify what axes to plot to, we can set the ```ax``` argument.

**4. Adding title and axis labels**
- To add a title to the axes use ```YOUR_AXES.title()```
- To add a label to each axis, use ```YOUR_AXES.xlabel()``` or ```YOUR_AXES.ylabel()```

You can do specify these on the whole figure.

**5. Showing the plot**

To show the plot in a window, we call ```plt.show()```.  
If you wanted to save the plot to a file, you can use ```plt.savefig()```

# Task

Create a simple seaborn Python script using the data provided in the template.

1. Create a histogram of the distribution of heights in the dataset.
2. Create a [scatter plot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html) of weight vs height.

## Requirements
- Use the dataset provided in the template
- Both plots are in one figure, and different axes
- Use the sns theme
- First plot is named 'Histogram', second is named 'Scatter plot'
- Axis names are:
  - *Histogram*: ```x``` - 'Height', ```y``` - 'Count'
  - *Scatter plot*: ```x``` - 'Height', ```y``` - 'Weight'