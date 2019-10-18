import math
import operator
from unittest import TestCase
from unittest.mock import Mock, call

from pypeline import Pypeline


class PypelineTest(TestCase):
    def test_pypeline__two_chained_simple_functions_arg_list__expected_correctly_value(self):
        # FIXTURE
        pipeline = Pypeline().append(
            math.pow, 2, 2
        ).append(
            operator.add, 5
        )

        # EXERCISE
        result = pipeline.do()

        # VERIFY
        self.assertEqual(9, result)  # add(pow(2**2), 5)

    def test_pypeline__two_chained_simple_functions_kwargs__expected_correctly_value(self):
        # FIXTURE
        pow = lambda x, y: math.pow(x, y)  # pow take no kwarg
        add = lambda a, b: operator.add(a, b)  # add take no kwargs

        pipeline = Pypeline().append(
            pow, x=2, y=2
        ).append(
            add, b=5
        )

        # EXERCISE
        result = pipeline.do()

        # VERIFY
        self.assertEqual(9, result)  # add(pow(x=2,y=2), b=5)

    def test_pypeline__two_chained_simple_functions_kwargs_and_arg_list__expected_correctly_value(self):
        # FIXTURE
        pow = lambda x, y: math.pow(x, y)  # pow take no kwarg
        add = lambda a, b: operator.add(a, b)  # add take no kwargs

        pipeline = Pypeline().append(
            pow, 2, y=2
        ).append(
            add, 5
        )

        # EXERCISE
        result = pipeline.do()

        # VERIFY
        self.assertEqual(9, result)  # add(pow(2,y=2), 5)

    def test_pypeline__two_chained_pipelines_mock_functions__expected_correctly_value(self):
        # FIXTURE
        expected = object()
        test_method = Mock(return_value=expected)
        sub_pipeline = Pypeline().append(
            test_method, 'first', 'second', third='third'
        ).append(
            test_method, something_else=True
        )
        pipeline = Pypeline().append_context(
            sub_pipeline
        ).append_context(
            sub_pipeline
        )

        # EXERCISE
        result = pipeline.do()

        # VERIFY
        self.assertIsNone(result)
        self.assertEqual(4, test_method.call_count)
        # first
        self.assertEqual(call('first', 'second', third='third'), test_method.mock_calls[0])
        self.assertEqual(call(expected, something_else=True), test_method.mock_calls[1])
        self.assertEqual(call('first', 'second', third='third'), test_method.mock_calls[2])
        self.assertEqual(call(expected, something_else=True), test_method.mock_calls[3])
