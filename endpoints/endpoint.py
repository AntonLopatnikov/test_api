import allure


class Endpoint:
    url = 'https://jsonplaceholder.typicode.com/posts'
    default_headers = {"Content-Type": "application/json"}

    def __init__(self, headers=None, js=None, response=None):
        self.js = js
        self.response = response
        self.headers = headers or self.default_headers



    @allure.step('check test in correct')
    def check_test(self, expected_title=None, expected_body=None, expected_userId=None):
        assert self.response is not None, "Ответ сервера отсутствует"
        if self.response.status_code == 201:
            print(self.response.status_code)
            pass
        elif self.response.status_code == 200:
            print(self.response.status_code)
            pass
        else:
            assert False, f"Статус {self.response.status_code}, ожидается 200 или 201"

        if self.js is None:
            print("Ответ не содержит JSON (возможно, статус 204)")
            return  # Пропускаем проверку полей, если JSON нет

        # Проверяем только если ожидаемые значения переданы
        if expected_title is not None:
            assert self.js.get('title') == expected_title, f"Заголовок {self.js.get('title')}, ожидается {expected_title}"
            print(f'title: {self.js.get('title')}')
        if expected_body is not None:
            assert self.js.get('body') == expected_body, f"Тело {self.js.get('body')}, ожидается {expected_body}"
            print(f'body: {self.js.get('body')}')
        if expected_userId is not None:
            assert self.js.get('userId') == expected_userId, f"userId {self.js.get('userId')}, ожидается {expected_userId}"
            print(f'userId: {self.js.get('body')}')

