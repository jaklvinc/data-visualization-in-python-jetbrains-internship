import pytest
import pandas as pd
import student_solution


def test_df_variable_exists():
    # Check if the df variable exists and contains the expected data
    assert hasattr(student_solution, 'df'), "The variable 'df' does not exist."
    assert isinstance(student_solution.df, pd.DataFrame), "'df' should be a pandas DataFrame."

def test_fifth_entry_variable():
    # Check if fifth_entry exists and contains the fifth row of df
    assert hasattr(student_solution, 'fifth_entry'), "The variable 'fifth_entry' does not exist."
    expected_fifth_entry = student_solution.df.iloc[4]  # 5th row is index 4
    pd.testing.assert_series_equal(student_solution.fifth_entry, expected_fifth_entry,
                                   check_names=False)


def test_unique_genres_and_consoles():
    # Check unique_genres and unique_consoles variables
    assert hasattr(student_solution, 'unique_genres'), "The variable 'unique_genres' does not exist."
    assert hasattr(student_solution, 'unique_consoles'), "The variable 'unique_consoles' does not exist."

    expected_unique_genres = student_solution.df['genre'].unique()
    expected_unique_consoles = student_solution.df['platform'].unique()

    assert set(student_solution.unique_genres) == set(expected_unique_genres), \
        "The variable 'unique_genres' does not contain the correct unique values."
    assert set(student_solution.unique_consoles) == set(expected_unique_consoles), \
        "The variable 'unique_consoles' does not contain the correct unique values."


def test_new_df_structure():
    # Check if new_df exists and has the correct structure
    assert hasattr(student_solution, 'new_df'), "The variable 'new_df' does not exist."
    new_df = student_solution.new_df

    # Verify that new_df has the right columns and data types
    assert isinstance(new_df, pd.DataFrame), "'new_df' should be a pandas DataFrame."
    assert set(new_df.columns) == {"count"}, "new_df should contain 'count' column."
    assert pd.api.types.is_integer_dtype(new_df['count']), "The 'count' column should have integer type."

    # Verify that new_df counts are correct
    expected_counts = student_solution.df[['name','platform']].groupby('platform').count().rename(columns={'name':'count'})
    expected_counts.columns = ['count']
    pd.testing.assert_frame_equal(new_df.sort_values(by='count').reset_index(drop=True),
                                  expected_counts.sort_values(by='count').reset_index(drop=True),
                                  check_dtype=False)
