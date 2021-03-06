import sqlite3

import pandas as pd

from learntools.core import *
from learntools.core.asserts import *
from learntools.core.richtext import CodeSolution as CS

class FruitDfCreation(EqualityCheckProblem):
    _var = 'fruits'
    _expected = (
            pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas']),
    )
    # TODO: This is a case where it would be nice to have a helper for creating 
    # a solution with multiple alternatives.
    _solution = CS(
            "fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])"
    )

class FruitSalesDfCreation(EqualityCheckProblem):
    _var = 'fruit_sales'
    _expected = (
            pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales']),
    )
    _solution = CS(
            """fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])""",
            )

class RecipeSeriesCreation(CodingProblem):
    _var = 'ingredients'
    quantities = ['4 cups', '1 cup', '2 large', '1 can']
    items = ['Flour', 'Milk', 'Eggs', 'Spam']
    recipe = pd.Series(quantities, index=items, name='Dinner')
    _solution = CS("""\
quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index=items, name='Dinner')""")

    def check(self, ings):
        assert_series_equals(ings, self.recipe)
        assert ings.name == self.recipe.name, ("Expected `ingredients` to have"
                " `name={!r}`, but was actually `{!r}`").format(
                        self.recipe.name, ings.name)


class ReadWineCsv(EqualityCheckProblem):
    _var = 'reviews'
    # TODO: Hint about index_col
    _expected = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)
    _solution = CS(
    "reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)"
    )

class SaveAnimalsCsv(CodingProblem):

    _solution = CS('animals.to_csv("cows_and_goats.csv")')

    def check(self):
        path = 'cows_and_goats.csv'
        assert_file_exists(path)
        actual = pd.read_csv(path, index_col=0)
        expected = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, 
                index=['Year 1', 'Year 2'])
        assert_df_equals(actual, expected)

class ReadPitchforkSql(EqualityCheckProblem):
    _var = 'music_reviews'
    # TODO: Is loading expected values expensive here? May want to do it on-demand 
    # when check is first called, rather than on import
    conn = sqlite3.connect("../input/pitchfork-data/database.sqlite")
    _expected = (
        pd.read_sql_query("SELECT * FROM artists", conn),
    )
    conn.close()

    _solution = CS("""\
import sqlite3
conn = sqlite3.connect("../input/pitchfork-data/database.sqlite")
music_reviews = pd.read_sql_query("SELECT * FROM artists", conn)""")

qvars = bind_exercises(globals(), [
    FruitDfCreation,
    FruitSalesDfCreation,
    RecipeSeriesCreation,
    ReadWineCsv,
    SaveAnimalsCsv,
    ReadPitchforkSql,
    ],
    tutorial_id=45,
    )
__all__ = list(qvars)
