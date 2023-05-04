import pytest

from kartothek.io.eager import delete_dataset
from kartothek.io.testing.delete import *  # noqa


def _delete_store_factory(dataset_uuid, store_factory):
    delete_dataset(dataset_uuid, store_factory)


def _delete_store(dataset_uuid, store_factory):
    delete_dataset(dataset_uuid, store_factory())


@pytest.fixture(params=["factory", "store-factory"])
def bound_delete_dataset(request):
    return _delete_store_factory if request.param == "factory" else _delete_store
