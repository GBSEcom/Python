# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.12.0.20200605.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.secure3_d_authentication_response_secure3d_method import Secure3DAuthenticationResponseSecure3dMethod  # noqa: E501
from openapi_client.rest import ApiException

class TestSecure3DAuthenticationResponseSecure3dMethod(unittest.TestCase):
    """Secure3DAuthenticationResponseSecure3dMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Secure3DAuthenticationResponseSecure3dMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.secure3_d_authentication_response_secure3d_method.Secure3DAuthenticationResponseSecure3dMethod()  # noqa: E501
        if include_optional :
            return Secure3DAuthenticationResponseSecure3dMethod(
                method_form = '&lt;!DOCTYPE iframe SYSTEM "about:legacy-compat"&gt; &lt;iframe id="tdsMmethodTgtFrame" name="tdsMmethodTgtFrame"
         style="width: 1px; height: 1px; display: none;" src="javascript:false;" xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;!--.--&gt; &lt;/iframe&gt;&lt;form id="tdsMmethodForm" name="tdsMmethodForm"
         action="https://localhost.modirum.com:8543/dstests/ACSEmu2" method="post"
         target="tdsMmethodTgtFrame" xmlns="http://www.w3.org/1999/xhtml"&gt; &lt;input type="hidden" name="3DSMethodData"
         value="eyAidGhyZWVEU1NlcnZlclRyYW5zSUQiIDogIjAwMDAwMDAwLTU2NzYtNTY2My04MDAwLTAwMDAw
&amp;#10;MDAwNDFhOSIsICJ0aHJlZURTTWV0aG9kTm90aWZpY2F0aW9uVVJMIiA6ICJodHRwczovL2xvY
         2Fs&amp;#10;aG9zdC5tb2RpcnVtLmNvbTo4NTQzL21kcGF5bXBpL01lcmNoYW50U2VydmVyP21uPVkmdHhpZD0x
&amp;#10;NjgwOSZkaWdlc3Q9aSUyQnhhUEF5NWFOcVJRbllqNmozbWFDZlFJbTdFdjJYTmkwNn
         h6YmZNJTJG&amp;#10;R3MlM0QiIH0"/&gt; &lt;input type="hidden" name="threeDSMethodData"
         value="eyAidGhyZWVEU1NlcnZlclRyYW5zSUQiIDogIjAwMDAwMDAwLTU2NzYtNTY2My04MDAwLTAwMDA
         w&amp;#10;MDAwNDFhOSIsICJ0aHJlZURTTWV0aG9kTm90aWZpY2F0aW9uVVJMIiA6ICJodHRwczovL2xvY
         2Fs&amp;#10;aG9zdC5tb2RpcnVtLmNvbTo4NTQzL21kcGF5bXBpL01lcmNoYW50U2VydmVyP21uPVkmd
         HhpZD0x&amp;#10;NjgwOSZkaWdlc3Q9aSUyQnhhUEF5NWFOcVJRbllqNmozbWFDZlFJbTdFdjJYTmkwNn
         h6YmZNJTJG&amp;#10;R3MlM0QiIH0"/&gt;
&lt;/form&gt;&lt;script type="text/javascript" xmlns="http://www.w3.org/1999/xhtml"&gt;
         document.getElementById("tdsMmethodForm").submit(); &lt;/script&gt;', 
                secure3d_trans_id = '3ac7caa7-aa42-2663-791b-2ac05a542c4a'
            )
        else :
            return Secure3DAuthenticationResponseSecure3dMethod(
        )

    def testSecure3DAuthenticationResponseSecure3dMethod(self):
        """Test Secure3DAuthenticationResponseSecure3dMethod"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
