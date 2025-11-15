from .endpoint import Endpoint
import requests
import allure


class CreatePost(Endpoint):

    @allure.step('Create new post')
    def create_new_post(self, body):
        self.response = requests.post(self.url,json = body,headers=self.headers)
        self.js = self.response.json()
        return self.response







