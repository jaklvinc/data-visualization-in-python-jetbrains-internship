# Data Preparation and Analysis with Pandas

## Theory

### What is Pandas?
Pandas is a powerful Python library for data manipulation and analysis, particularly useful for handling structured data.  
It provides data structures like Series (for one-dimensional data) and DataFrame (for two-dimensional data), making it easier to work with structured data, perform operations, and prepare data for analysis or visualization.

### Pandas key advantages
- **Data manipluation**: It offers flexible data manipulation tools for filtering, sorting, and aggregating data, making it ideal for cleaning and preparing datasets.
- **Data Analysis**: With powerful methods for group operations, reshaping, merging, and handling missing values, Pandas is commonly used for exploring and analyzing data effectively.
- **Flexible Indexing**: The ability to set and change indices easily allows for advanced data selection, making operations like slicing, indexing, and subsetting straightforward.

### Basic data analysis

When we get a dataset, it is nice to know some basic things about it.
Pandas can help us with that. 

#### 1. Loading the data  

To load the data from a csv file, we can use ```pd.read_csv()```. We can input the file path as a string argument.  
The basic naming convention for a Pandas dataframe is ```df```.

#### 2. Inspecting the data structure and contents

To see how the data looks, we can use different commands:

- ```df.head()``` - shows us first 5 entries, we can manipulate the number with an argument
- ```df.info()``` - shows us basic information about the dataset
- ```df.nunique()``` - shows us how many unique values each column has. This can be useful to determine which columns may be important.
- ```df["COLUMN_NAME"].unique()``` - shows all unique values of column with COLUMN_NAME

#### 3. Accessing data 
To access data in a certain column, we can use ```df[COLUMN_NAME]```.  
If we want to see data from multiple specified columns, we can use```df[[COLUMN_NAME,COLUMN_NAME]]```.

If we want a row, based on index, we can use ```df.iloc[IDX]```.  
If we want a row, based on content, we can use ```df.loc[CONTENT]```.

If we want to select rows based on a condition, we can use ```df[df[COLUMN_NAME] > x]```. Of course, we can select different comparisons than ```== != < > <= >=```. To compare against a list, you can use ```.isin([YOUR_LIST])```  
For multiple conditions ```.query()``` can be used, read more on it [here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html).

#### 4. Data manipulation

*Be careful that by default, pandas does not work inplace, so when you want to manipulate data, you need to save the result into a new dataframe.*

- ```df.rename(columns={ORIGINAL_NAME: NEW_NAME})``` - allows us to change column names. The dictionary can contain more than one change.
- ```df.sort_values()``` - the first argument is the column/s you want to sort by. Default is ascending sort, which can be changed by setting ```ascending = False```  

##### groupby 

```df.groupby()``` - groups other columns by the first argument column. 

- It is possible to group by more than one column.
- By default, it returns a groupby object, so in order to turn it back to a DataFrame, it is a good practice to put an aggregating function like ```max()```,```count()```,```min()``` or ```mean()``` after it.  
- Groupby also sets a new index on the grouped columns.

For example when we want to count how much each gender is represented in a dataset, we can call:
```python
df.groupby('gender').count() 
```
This will give us a table which shows how many entries there are for each gender in the dataset.  

To avoid problems with your data being on the index, you can call ```reset_index()``` after calling groupby and the index will reset to a new numeric one.

#### 5. Dropping data

We can drop unwanted data using ```df.drop()```.

If we want to drop some columns, we can do so by specifying the ```columns``` argument, or using the `axis` argument, like this:
```python
df.drop(columns=['A','B'])
df.drop(['A','B'], axis=1)
```

If we want to drop rows, we can specify the indeces:
```python
df.drop([0,3,5])
```

# Task
Create a simple Python script, that shows how you understand working with Pandas.

- Load the provided dataset in ```data/dataset.csv```
- Print information about the dataset
- Save the 5th row into a variable
- Print unique genres and consoles and save those into variables
- Create a new dataframe using ```groupby()``` that contains the count of games for each platform

## Requirements
- ```df``` variable stores the provided dataset
- ```fifth_entry``` contains the 5th entry in the dataset
- ```unique_genres``` and ```unique_consoles``` variables store specified unique values
- ```new_df``` should contain 1 column apart from the index of genre names
  - ```count``` with the count of all games for certain platform






