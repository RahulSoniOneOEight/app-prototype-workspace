import unittest

from scripts.validate_design_contract import (
    validate_direction_document,
    validate_resource_source_document,
)


class ExperienceDirectionValidationTests(unittest.TestCase):
    def test_direction_requires_material_product_difference_fields(self):
        errors = []
        validate_direction_document(
            {
                "id": "direction-a",
                "name": "Discovery-led",
                "strategy": "discovery_led",
                "structure": {"entry": "home", "navigation": "consumer_bottom_nav"},
                "journeys": {"primary": ["b2c.discovery_to_purchase"]},
                "patterns": {"home": "b2c.discovery_home"},
                "density": "spacious",
                "merchandising": {"emphasis": ["collections"]},
                "interactions": {"search_prominence": "secondary"},
                "visual_style": {"imagery": "editorial"},
                "resources": {"imagery_style": "editorial", "icon_family": "iconoir"},
            },
            "client-a/directions/direction-a.yaml",
            errors,
        )
        self.assertEqual([], errors)

    def test_direction_missing_journeys_is_rejected(self):
        errors = []
        validate_direction_document(
            {
                "id": "direction-a",
                "name": "Discovery-led",
                "strategy": "discovery_led",
                "structure": {"entry": "home"},
                "patterns": {"home": "shared.home"},
                "density": "spacious",
                "merchandising": {},
                "interactions": {},
                "visual_style": {},
            },
            "direction-a.yaml",
            errors,
        )
        self.assertTrue(any("journeys" in error for error in errors))


class ResourceSourceValidationTests(unittest.TestCase):
    def test_resource_source_requires_search_evaluation_and_provenance(self):
        errors = []
        validate_resource_source_document(
            {
                "id": "pexels",
                "resource_types": ["stock_photography", "stock_video"],
                "search": {"method": "api", "supports": ["query", "orientation"]},
                "evaluation": {"check": ["license", "resolution", "subject_fit"]},
                "usage": {"prototype": {"preferred": "remote_url"}},
                "provenance": {"store": ["provider", "asset_id", "source_url", "license", "query"]},
            },
            "agency-resources/sources/pexels.yaml",
            errors,
        )
        self.assertEqual([], errors)

    def test_resource_source_without_license_evaluation_is_rejected(self):
        errors = []
        validate_resource_source_document(
            {
                "id": "pexels",
                "resource_types": ["stock_photography"],
                "search": {"method": "api", "supports": ["query"]},
                "evaluation": {"check": ["resolution"]},
                "usage": {"prototype": {"preferred": "remote_url"}},
                "provenance": {"store": ["provider", "asset_id", "source_url", "license", "query"]},
            },
            "pexels.yaml",
            errors,
        )
        self.assertTrue(any("license" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
