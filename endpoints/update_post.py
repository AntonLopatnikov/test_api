from .endpoints.endpoint import Endpoint
import requests
import allure

class UpdatePost(Endpoint):

    @allure.step('Update a post')
    def update_body(self,post_id,body):
        self.response = requests.put(f'{self.url}/{post_id}',json=body,headers=self.headers)
        self.js = self.response.json()
        return self.response
