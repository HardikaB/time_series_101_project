import unittest
from inspect import getfullargspec
from ..build import q04_boxplot as student
from greyatomlib.time_series_101_project.q04_boxplot.build import q04_boxplot as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        with open('q04_boxplot/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q04_boxplot/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q04_boxplot/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q04_boxplot/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/perrin-freres-monthly-champagne.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_args(self):
        self.args_student = getfullargspec(self.student_func).args
        self.args_original = getfullargspec(self.solution_func).args
        self.assertEqual(len(self.args_student), len(self.args_original),
                         "Expected argument(s) %d, Given %d" % (len(self.args_original), len(self.args_student)))

        # check the defaults of the function

    def test_defaults(self):
        self.defaults_student = getfullargspec(self.student_func).defaults
        self.defaults_solution = getfullargspec(self.solution_func).defaults
        self.assertEqual(self.defaults_student, self.defaults_solution,
                         "Expected default values do not match given default values")

