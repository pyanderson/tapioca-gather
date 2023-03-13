import requests
from tapioca import (
    JSONAdapterMixin,
    TapiocaAdapter,
    generate_wrapper_from_adapter,
)

from .resource_mapping import RESOURCE_MAPPING


class GatherClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = "https://api.gather.town/api/v2/"
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(GatherClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )
        params["headers"] = {"apiKey": api_params["api_key"]}
        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(
        self, iterator_request_kwargs, response_data, response
    ):
        pass


Gather = generate_wrapper_from_adapter(GatherClientAdapter)
