#!/usr/bin/env python3
""" test for utils.py """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ unittests for nested map function """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """ unittest for the function """
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

    @parameterized.expand([
        ({}, ('a',), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_value):
        """ Unittest for exception in a nested map function """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map=nested_map, path=path)

        self.assertEqual(repr(error.exception), repr(expected_value))


class TestGetJson(unittest.TestCase):
    """ Test the response of json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict):
        """	unittest for correct execution """
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Test the memoize decorator """
    def test_memoize(self):
        """	Test the memoize decorator that save the return of the function
        that use it.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_memo:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_memo.assert_called_once()
