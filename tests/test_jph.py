import pytest
import requests

TEST_DATA = [{"title": "foo", "body": "bar", "userId": 1},
             {"title": "foof", "body": "bar321", "userId": 1}
            ]

NEGATIVE_DATA = [{"title": "[foo]", "body": "bar", "userId": 342432},
                 {"title": "{{[foo']}}", "body": "bar321", "userId": 1}
                ]

@pytest.mark.post
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(body = data)
    create_post_endpoint.check_test(data['title'], data['body'], data['userId'])

@pytest.mark.post_negative
@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(create_post_endpoint, data):
    create_post_endpoint.create_new_post(body = data)
    create_post_endpoint.check_test(data['title'], data['body'], data['userId'])



@pytest.mark.put
def test_put_a_post(update_post_endpoint):
    body = {
        "title": "foof",
        "body": "bar42",
        "userId": 2
    }
    update_post_endpoint.update_body(42,body)
    update_post_endpoint.check_test(body['title'], body['body'], body['userId'])

@pytest.mark.patch
def test_patch_a_post(patch_endpoint):
    body = {"body": "barrr","userId": 7}
    patch_endpoint.patch_post(42,body)
    patch_endpoint.check_test(expected_body="barrr", expected_userId=7 )
