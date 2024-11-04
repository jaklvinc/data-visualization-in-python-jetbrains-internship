import pytest
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import check_figures_equal
import seaborn as sns
import student_solution



def test_platform_filtering_and_order():
    """Test that platforms are filtered and ordered correctly"""
    ax = plt.gca()

    assert [t.get_text() for t in ax.get_xticklabels()] == ['PS4', 'XOne', 'PC', 'WiiU']


def test_seaborn_theme():
    """Test that seaborn theme is applied"""
    fig = plt.gcf()
    # Get the Seaborn theme as a set of rcParams
    sns_params = plt.rcParams.get('axes.facecolor')
    assert sns_params != plt.rcParamsDefault['axes.facecolor'], "Seaborn theme should be applied"


def test_plot_mechanics():
    """Test the mechanics of the plot (axes, labels, etc)"""
    ax = plt.gca()

    # Check that it's a bar plot
    assert any(isinstance(child, plt.Rectangle) for child in ax.get_children())

    # Check axes labels
    assert ax.get_xlabel() == 'platform'
    assert ax.get_ylabel() == 'count'

def test_genre_sorting():
    """Test that genres are sorted alphabetically"""

    ax = plt.gca()
    legend_labels = [t.get_text() for t in ax.get_legend().get_texts()] if ax.get_legend() else []

    # Check that legend labels are sorted
    assert legend_labels == sorted(legend_labels)


def test_plot_shows_all_genres():
    """Test that all genres in the data are shown in the plot"""
    sample_data = pd.read_csv('../data/dataset.csv')
    ax = plt.gca()

    unique_genres = set(sample_data['genre'].unique())
    legend_genres = set([t.get_text() for t in ax.get_legend().get_texts()] if ax.get_legend() else [])

    assert unique_genres == legend_genres, "Not all genres are shown in the plot"


def test_chart_ok():
    ax = plt.gca()

    assert (ax.patches[0].get_height() > ax.patches[1].get_height() > ax.patches[2].get_height() > ax.patches[3].get_height()) and ( ax.patches[0].get_height() > ax.patches[4].get_height() > ax.patches[8].get_height() )






if __name__ == "__main__":
    pytest.main([__file__])