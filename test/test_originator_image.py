# coding: utf-8

"""
    Engine by MoneyLion API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.58.0
    Contact: help@engine.tech
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.originator_image import OriginatorImage

class TestOriginatorImage(unittest.TestCase):
    """OriginatorImage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OriginatorImage:
        """Test OriginatorImage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OriginatorImage`
        """
        model = OriginatorImage()
        if include_optional:
            return OriginatorImage(
                size_key = '',
                url = ''
            )
        else:
            return OriginatorImage(
                size_key = '',
                url = '',
        )
        """

    def testOriginatorImage(self):
        """Test OriginatorImage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
