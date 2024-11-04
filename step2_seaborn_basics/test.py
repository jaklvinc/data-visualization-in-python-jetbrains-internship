import pytest
import matplotlib.pyplot as plt
import student_solution


def test_figure_exists():
    # Check if figure and axes are created
    fig = plt.gcf()
    assert fig is not None, "No figure created"


def test_axes_count():
    # Check if there are exactly two axes
    fig = plt.gcf()
    axes = fig.get_axes()
    assert len(axes) == 2, f"Expected 2 axes, but found {len(axes)}"


def test_histogram_content():
    # Check the first axis has a histogram with the correct labels
    fig = plt.gcf()
    ax = fig.get_axes()[0]

    assert ax.get_title() == "Histogram", "First plot title should be 'Histogram'"
    assert ax.get_ylabel() == "Count", "Histogram y-axis label should be 'Count'"
    assert ax.get_xlabel() == "Global Sales", "Histogram x-axis label should be 'Global Sales'"


def test_scatter_plot_content():
    # Check the second axis has a scatter plot with the correct labels
    fig = plt.gcf()
    ax = fig.get_axes()[1]

    assert ax.get_title() == "Scatter plot", "Second plot title should be 'Scatter plot'"
    assert ax.get_ylabel() == "EU Sales", "Scatter plot y-axis label should be 'EU Sales'"
    assert ax.get_xlabel() == "NA Sales", "Scatter plot x-axis label should be 'NA Sales'"


def test_theme_applied():
    # Check if Seaborn theme has been applied
    fig = plt.gcf()
    # Get the Seaborn theme as a set of rcParams
    sns_params = plt.rcParams.get('axes.facecolor')
    assert sns_params != plt.rcParamsDefault['axes.facecolor'], "Seaborn theme should be applied"