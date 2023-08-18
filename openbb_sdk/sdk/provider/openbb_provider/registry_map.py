"""Provider registry map."""

import inspect
import os
from typing import Any, Dict, List, Literal, Optional, Tuple

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.registry import Registry, RegistryLoader

MapType = dict[str, dict[str, dict[str, dict[str, Any]]]]


class RegistryMap:
    """Class to store information about providers in the registry."""

    def __init__(self, registry: Optional[Registry] = None) -> None:
        """Initialize Registry Map."""
        self._registry = registry or RegistryLoader.from_extensions()
        self._required_credentials = self._get_required_credentials(self._registry)
        self._available_providers = self._get_available_providers(self._registry)
        self._map, self._return_map = self._get_map(self._registry)
        self._models = self._get_models(self._map)

    @property
    def registry(self) -> Registry:
        """Get the registry."""
        return self._registry

    @property
    def available_providers(self) -> List[str]:
        """Get list of available providers."""
        return self._available_providers

    @property
    def required_credentials(self) -> List[str]:
        """Get list of required credentials."""
        return self._required_credentials

    @property
    def map(self) -> MapType:
        """Get provider registry map."""
        return self._map

    @property
    def return_map(self) -> MapType:
        """Get provider registry return map."""
        return self._return_map

    @property
    def models(self) -> List[str]:
        """Get available models."""
        return self._models

    def _get_required_credentials(self, registry: Registry) -> List[str]:
        """Get list of required credentials."""
        cred_list = []
        for provider in registry.providers.values():
            for c in provider.required_credentials:
                cred_list.append(c)
        return cred_list

    def _get_available_providers(self, registry: Registry) -> List[str]:
        """Get list of available providers."""
        return sorted(list(registry.providers.keys()))

    def _get_map(self, registry: Registry) -> Tuple[MapType, MapType]:
        """Generate map for the provider package."""
        map_: MapType = {}
        return_map: MapType = {}

        for p in registry.providers:
            for model_name, fetcher in registry.providers[p].fetcher_dict.items():
                f = fetcher()
                standard_query, extra_query = self.extract_info(f, "query_params")
                standard_data, extra_data = self.extract_info(f, "data")
                return_type = self.extract_return_type(f)

                if model_name not in map_:
                    map_[model_name] = {}
                    map_[model_name]["openbb"] = {
                        "QueryParams": standard_query,
                        "Data": standard_data,
                    }

                map_[model_name][p] = {
                    "QueryParams": extra_query,
                    "Data": extra_data,
                }
                return_map[model_name] = return_type

        return map_, return_map

    def _get_models(self, map_: MapType) -> List[str]:
        """Get available models."""
        return list(map_.keys())

    @staticmethod
    def extract_info(fetcher: Fetcher, type_: Literal["query_params", "data"]) -> tuple:
        """Extract info (fields and docstring) from fetcher query params or data."""
        super_model = getattr(fetcher, type_)

        skip_classes = {"object", "Representation", "BaseModel", "QueryParams", "Data"}
        inheritance_list = [
            model for model in super_model.__mro__ if model.__name__ not in skip_classes
        ]

        all_fields = {}
        standard_info: Dict[str, Any] = {"fields": {}, "docstring": None}
        found_standard = False

        for model in inheritance_list:
            model_file_dir = os.path.dirname(inspect.getfile(model))
            model_name = os.path.basename(model_file_dir)

            if (model_name == "standard_models") or found_standard:
                if not found_standard:
                    standard_info["docstring"] = model.__doc__
                found_standard = True
                standard_info["fields"].update(model.__fields__)
            else:
                all_fields.update(model.__fields__)

        extra_info = {"fields": {}, "docstring": super_model.__doc__}

        for name, field in all_fields.items():
            if name not in standard_info["fields"]:
                extra_info["fields"][name] = field

        return standard_info, extra_info

    @staticmethod
    def extract_return_type(fetcher: Fetcher):
        """Extract return info from fetcher."""
        return getattr(fetcher, "return_type", None)