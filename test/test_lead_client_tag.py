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

from openapi_client.models.lead_client_tag import LeadClientTag

class TestLeadClientTag(unittest.TestCase):
    """LeadClientTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeadClientTag:
        """Test LeadClientTag
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeadClientTag`
        """
        model = LeadClientTag()
        if include_optional:
            return LeadClientTag(
                hash = '',
                lead_uuid = '',
                key = '',
                value = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return LeadClientTag(
                hash = '',
                lead_uuid = '',
                key = '',
                value = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testLeadClientTag(self):
        """Test LeadClientTag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
