#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
import requests
from unittest.mock import patch,Mock
from utils import get_json
from utils import memoize
from unittest.mock import patch

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
         
class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_object = TestClass()

        with patch.object(test_object, 'a_method') as mock_method:
            mock_method.return_value = 42

            
            result1 = test_object.a_property
            self.assertEqual(result1, 42)

            
            result2 = test_object.a_property
            self.assertEqual(result2, 42)

            # Verify a_method was only called once
            mock_method.assert_called_once()

      

if __name__ == "__main__":
    unittest.main()



  
    
  