#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
import requests
from unittest.mock import patch,Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
    ({"a": 1}, ("a",), 1),
    ({"a": {"b": 2}}, ("a",), {"b": 2}),
    ({"a":{"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected ):
        self.assertEqual(access_nested_map(nested_map, path), expected)
    @parameterized.expand([
    ({}, {"a",}, KeyError),
    ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map,path,expected_exception):
       with self.assertRaises(expected_exception):
        access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock() #created a mock_response object
        mock_response.json.return_value = test_payload #when we ask for the values in the mock_response object(in json value) it returns test_payload("payload:true")
        mock_get.return_value = mock_response ##the new requests.get value returns the values in the mock_response, which are the json values we assigned above (payload:true)


        result = get_json(test_url)

        self.assertEqual(result, test_payload) #checks if our result and the test_payload value is equal
        mock_get.assert_called_once_with(test_url) #counts if the mock_get is called exactly once(the mock_get records everything )
         


if __name__ == "__main__":
    unittest.main()



  
    
  