import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class Layer4SeedTests(unittest.TestCase):
    def test_required_industry_presets_exist(self):
        expected = {
            'fashion-apparel.yaml',
            'beauty-personal-care.yaml',
            'electronics-appliances.yaml',
            'furniture-home-decor.yaml',
            'grocery-fmcg.yaml',
            'food-delivery-qsr.yaml',
            'b2b-industrial-construction.yaml',
            'marketplace-multiseller-retail.yaml',
            'd2c-lifestyle.yaml',
            'travel-hospitality.yaml',
            'health-pharmacy-wellness.yaml',
            'services-rental-appointment.yaml',
        }
        actual = {p.name for p in (ROOT / 'presets/industry').glob('*.yaml')}
        self.assertTrue(expected.issubset(actual), expected - actual)

    def test_visual_presets_have_twelve_families_and_thirty_six_options(self):
        visual_root = ROOT / 'presets/visual'
        families = [p for p in visual_root.iterdir() if p.is_dir() and (p / 'preset.yaml').exists()]
        self.assertEqual(12, len(families))
        options = []
        for family in families:
            family_options = sorted(family.glob('option-*.yaml'))
            self.assertEqual(3, len(family_options), family.name)
            options.extend(family_options)
        self.assertEqual(36, len(options))

    def test_visual_palette_options_keep_source_colors_and_semantic_tokens_separate(self):
        option = ROOT / 'presets/visual/premium-neutral/option-a.yaml'
        data = yaml.safe_load(option.read_text(encoding='utf-8'))
        self.assertEqual(4, len(data['source_colors']))
        self.assertIn('semantic_tokens', data)
        self.assertIn('brand_primary', data['semantic_tokens'])
        self.assertIn('cta_text', data['semantic_tokens'])

    def test_experience_pattern_seed_exists(self):
        expected = {'discovery-first.yaml', 'search-first.yaml', 'trade-first.yaml', 'rfq-first.yaml', 'reorder-first.yaml'}
        actual = {p.name for p in (ROOT / 'experience-patterns').glob('*.yaml')}
        self.assertTrue(expected.issubset(actual), expected - actual)

    def test_intelligence_registry_indexes_exist(self):
        for name in ['components.index.yaml', 'patterns.index.yaml', 'journeys.index.yaml', 'presets.index.yaml', 'experience-patterns.index.yaml', 'resources.index.yaml']:
            self.assertTrue((ROOT / 'intelligence-registry' / name).exists(), name)

    def test_representative_flutter_contract_to_code_files_exist(self):
        package = ROOT / 'packages/agency_flutter_ui'
        for path in [
            'pubspec.yaml',
            'lib/agency_flutter_ui.dart',
            'lib/components/product_card.dart',
            'lib/components/price_display.dart',
            'lib/components/verified_badge.dart',
            'test/product_card_test.dart',
            'test/price_display_test.dart',
            'test/verified_badge_test.dart',
        ]:
            self.assertTrue((package / path).exists(), path)

    def test_flutter_public_api_exports_three_seed_components(self):
        public_api = (ROOT / 'packages/agency_flutter_ui/lib/agency_flutter_ui.dart').read_text(encoding='utf-8')
        self.assertIn("export 'components/product_card.dart';", public_api)
        self.assertIn("export 'components/price_display.dart';", public_api)
        self.assertIn("export 'components/verified_badge.dart';", public_api)


if __name__ == '__main__':
    unittest.main()
