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
**1. Creating the plot figure and axes**  
  
To create plot, we usually use the function ```plt.subplots()```.
This is a function from the Matplotlib library, that Seaborn is built on the top of.  
```plt.subplots()``` gives us two objects: 
   - ```fig``` - serves as a container for the plots
   - ```axes``` - represents the actual plot/s themselves

Default usage:
```python
   fig, ax = plt.subplots()
```

If we want to put more axes into one figure, we can specify the arguements ```nrows: int, ncols: int```.  
If we want to specify the size of the figure, we can use the argument ```figsize: (float,float)``` to set the width and height in inches.

**2. Setting the theme**  
  
You can set the theme, using ```sns.set_theme()```.
This can take parameters, but by default it sets the graph to a grey color with white gridlines.
You can find more possibilities [here](https://seaborn.pydata.org/tutorial/aesthetics.html).

**3. Creating a plot from a dataset**  
  
To create a plot, we need to call the appropriate function.
For example to create a histogram, which can be useful to find out the distribution of our dataset, we would use ```sns.histplot()```  

Plot functions in seaborn usually take our dataset as the first argument, and then name of a column, that is specified as ```x``` or ```y```.  

For example, if we wanted to create a histogram with the distribution of height in a dataset with people, we would call:
```python
sns.histplot(people, x='Height')
```

**4. Adding title and axis labels**
- To add a title to the plot use ```plt.title()```
- To add a label to each axis, use ```plt.xlabel()``` or ```plt.ylabel()```

**5. Showing the plot**

To show the plot in a window, we call ```plt.show()```.  
If you wanted to save the plot to a file, you can use ```plt.savefig()```

# Task

Create a simple seaborn Python script using the data provided in the template.

1. Create a histogram of the distribution of heights in the dataset.
2. 