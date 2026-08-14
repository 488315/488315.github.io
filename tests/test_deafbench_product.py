from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCT_PAGE = ROOT / "products" / "deafbench" / "index.html"


class ProductPageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"] or "")

    def handle_data(self, data: str) -> None:
        self.text.append(data)


class DeafBenchProductPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = PRODUCT_PAGE.read_text(encoding="utf-8")
        cls.parser = ProductPageParser()
        cls.parser.feed(cls.source)
        cls.visible_text = " ".join(" ".join(cls.parser.text).split())

    def test_explains_public_demo_boundaries(self) -> None:
        self.assertIn("Synthetic accessibility stress demo", self.visible_text)
        self.assertIn("does not measure Deaf or hard-of-hearing speakers", self.visible_text)
        self.assertIn("not a Hugging Face leaderboard result", self.visible_text)
        self.assertIn(
            "I am not accepting customer audio or payment yet", self.visible_text
        )

    def test_lists_every_integrated_model(self) -> None:
        expected_models = (
            "OpenAI Whisper turbo",
            "Faster-Whisper small.en",
            "Whisper-AT medium.en",
            "Distil-Whisper large-v3",
            "Qwen3-ASR 0.6B",
            "Qwen3-ASR 1.7B",
            "Parakeet TDT 0.6B v2",
            "Granite Speech 4.1 2B",
            "Granite Speech 4.1 2B NAR",
            "ARK-ASR 0.6B",
            "ARK-ASR 0.6B INT8 ONNX",
        )
        for model in expected_models:
            with self.subTest(model=model):
                self.assertIn(model, self.visible_text)

    def test_publishes_measured_whisper_evidence(self) -> None:
        self.assertIn(
            "These nine rows are recorded local observations from the same 25-sample corpus",
            self.visible_text,
        )
        self.assertIn("cannot be independently recomputed", self.visible_text)
        self.assertIn("Recorded local observation", self.visible_text)
        self.assertIn(
            "Distil-Whisper large-v3 23.8% 66.1% 91.9% 0.80 CPU",
            self.visible_text,
        )
        self.assertIn(
            "Whisper-AT medium.en 26.2% 67.7% 96.8% 7.34 4.46 GiB",
            self.visible_text,
        )
        self.assertIn(
            "Whisper-AT medium.en Recorded local observation "
            "Synthetic-v2, real-speech smoke, and non-speech-v1",
            self.visible_text,
        )
        self.assertIn(
            "Distil-Whisper large-v3 Recorded local observation "
            "Synthetic-v2 and real-speech smoke",
            self.visible_text,
        )

    def test_covers_accessibility_critical_entity_types(self) -> None:
        expected_entities = (
            "Time",
            "Date",
            "Dosage",
            "Name",
            "Username",
            "Code",
            "Confirmation number",
            "Wi-Fi name",
            "Address",
            "Money",
            "Negation",
        )
        for entity in expected_entities:
            with self.subTest(entity=entity):
                self.assertIn(entity, self.visible_text)

    def test_has_accessible_landmarks_and_unique_ids(self) -> None:
        self.assertIn('<a class="skip-link" href="#main">', self.source)
        self.assertIn('<main id="main"', self.source)
        self.assertEqual(len(self.parser.ids), self.source.count(' id="'))

    def test_homepage_and_sitemap_expose_product_page(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn('href="/products/deafbench/"', homepage)
        self.assertIn(
            "https://488315.github.io/products/deafbench/",
            sitemap,
        )

    def test_declares_product_discovery_metadata(self) -> None:
        expected_tags = (
            '<link rel="canonical" href="https://488315.github.io/products/deafbench/">',
            '<meta property="og:type" content="website">',
            '<meta property="og:image" content="https://488315.github.io/assets/images/deafbench-social-card.png">',
            '<meta name="twitter:card" content="summary_large_image">',
            '<meta name="twitter:image" content="https://488315.github.io/assets/images/deafbench-social-card.png">',
        )
        for tag in expected_tags:
            with self.subTest(tag=tag):
                self.assertIn(tag, self.source)

    def test_publishes_software_and_dataset_structured_data(self) -> None:
        scripts = re.findall(
            r'<script type="application/ld\+json">(.*?)</script>',
            self.source,
            flags=re.DOTALL,
        )
        self.assertEqual(len(scripts), 1)
        payload = json.loads(scripts[0])
        graph = payload["@graph"]
        self.assertEqual(
            {item["@type"] for item in graph},
            {"SoftwareApplication", "Dataset"},
        )
        software = next(item for item in graph if item["@type"] == "SoftwareApplication")
        dataset = next(item for item in graph if item["@type"] == "Dataset")
        self.assertEqual(software["softwareVersion"], "0.2.1")
        self.assertEqual(software["downloadUrl"], "https://pypi.org/project/deafbench/")
        self.assertIn("sample-level run artifacts are not included", dataset["description"])

    def test_links_to_installation_and_methodology(self) -> None:
        self.assertIn('href="https://pypi.org/project/deafbench/"', self.source)
        self.assertIn(
            'href="https://huggingface.co/datasets/kvjones0243/deafbench-synthetic-v2"',
            self.source,
        )
        self.assertIn(
            'href="https://github.com/488315/DeafBench/blob/main/docs/asr-evaluation-methodology.md"',
            self.source,
        )


if __name__ == "__main__":
    unittest.main()
