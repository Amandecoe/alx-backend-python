#!/usr/bin/env python3
"""This module contains unit tests for the GithubOrgClient class in client.py.

The tests cover various methods of the GithubOrgClient class including:
- org property
- _public_repos_url property
- public_repos method
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch, Mock
from client import GithubOrgClient
from fixture import TEST_PAYLOAD
org_payload, repos_payload, expected_repos, apache2_repos = TEST_PAYLOAD[0]

class TestGithubOrgClient(unittest.TestCase):
    """This tests that GithubOrgClient.org returns the correct value."""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')  # get_json return data from a url but
    # now it is patched to return a mock value
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct organization data.
        Args:
            org_name: The name of the organization to test (parameterized)
            mock_get_json: Mock object for the get_json function
        Verifies:
            - The returned organization data matches the expected payload
            - get_json is called exactly once with the correct URL
        """
        expected_payload = {'login': org_name}  # stores the org_name in
        # dictionary format
        mock_get_json.return_value = expected_payload
        # when the return value of mock_get_json
        # is asked it returns expected_payload({'login':org_name})
        client = GithubOrgClient(org_name)
        # is an object created for the GithubOrgClient
        # class in client.py and takes org_name as a parameter
        result = client.org  # takes the
        # org_name and passes it into the org function in
        # client.py which displays org_name in json format

        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns
        the correct value from the org payload"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
            return_value={
                "repos_url": "https://api.github.com/orgs/orgname/repos"}
        )as mock_org:
            client = GithubOrgClient("orgname")
            result = client._public_repos_url
            self.assertEqual(
                result, "https://api.github.com/orgs/orgname/repos")
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """This tests that the list of
          repos is what you expect from the chosen payload."""
        test_public_repos = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": None},
        ]
        mock_get_json.return_value = test_public_repos

        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api." \
                "github.com/orgs/torr/repos"

            client = GithubOrgClient("torr")
            result = client.public_repos()

            expected = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected)
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/torr/repos")
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({},"my_license", False),
        ({"license":None}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, expected):
        client = GithubOrgClient("testorgs")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient with mocked API calls"""
    
    @classmethod
    def setUpClass(cls):
        """Set up the mock for requests.get"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        
        def side_effect(url, *args, **kwargs):
            mock = Mock()
            # Match organization endpoint
            if url == "https://api.github.com/orgs/google":
                mock.json.return_value = cls.org_payload
            # Match repos endpoint
            elif url == "https://api.github.com/orgs/google/repos":
                mock.json.return_value = cls.repos_payload
            return mock
            
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()
    
    def test_public_repos(self):
        """Test that public_repos returns the expected repositories"""
        client = GithubOrgClient("google")
        
        # Test all public repos
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
        
        # Verify mock was called with correct URLs
        self.assertEqual(self.mock_get.call_count, 2)
        self.mock_get.assert_any_call("https://api.github.com/orgs/google")
        self.mock_get.assert_any_call("https://api.github.com/orgs/google/repos")
    
    def test_public_repos_with_license(self):
        """Test public_repos with license filtering"""
        client = GithubOrgClient("google")
        
        # Test Apache-licensed repos
        apache_repos = client.public_repos(license="apache-2.0")
        self.assertEqual(apache_repos, self.apache2_repos)
          
if __name__ == '__main__':
    unittest.main()
