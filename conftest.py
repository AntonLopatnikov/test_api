import pytest
from test_api.endpoints.create_post import CreatePost
from test_api.endpoints.update_post import UpdatePost
from test_api.endpoints.patch_post import PatchPost

@pytest.fixture()
def create_post_endpoint():
    return CreatePost()

@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def patch_endpoint():
    return PatchPost()
