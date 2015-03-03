import json
import requests
from request_base import RequestBase, rest_client_reconnect


class HostedPagesManager(RequestBase):

    @rest_client_reconnect
    def get_signature(self, pageId):
        fullUrl = self.zuora_config.base_url + 'rsa-signatures'
        data = json.dumps({
            'pageId': pageId,
            'method': 'POST',
            'uri': self.zuora_config.hosted_page_uri
        })
        response = requests.post(fullUrl, data=data,
                                 headers=self.zuora_config.headers,
                                 verify=False)
        return self.get_json(response)
