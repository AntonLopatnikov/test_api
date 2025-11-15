import requests
import allure
from ..endpoints.endpoint import Endpoint


class PatchPost(Endpoint):

    @allure.step('Update a post')
    def patch_post(self,post_id,body):
        self.response = requests.patch(f'{self.url}/{post_id}',json=body,headers=self.headers)
        self.js = self.response.json()
        return self.response

