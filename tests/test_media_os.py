import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("media_os", ROOT / "scripts/media_os.py")
media_os = importlib.util.module_from_spec(spec)
spec.loader.exec_module(media_os)


class WorkspaceTests(unittest.TestCase):
    def test_new_workspace_is_private_unconnected_and_paused(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = media_os.initialize(Path(temporary) / "my work")
            profile = json.loads((destination / "profile.json").read_text())
            self.assertTrue(profile["publishing_paused"])
            self.assertIsNone(profile["brand"]["name"])
            self.assertIsNone(profile["notion_bindings"])
            self.assertEqual(profile["channels"], [])
            self.assertEqual((destination / "publications.jsonl").read_text(), "")

    def test_repeat_init_preserves_user_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = media_os.initialize(Path(temporary) / "workspace")
            path = destination / "profile.json"
            path.write_text("my private notes")
            with self.assertRaises(ValueError):
                media_os.initialize(destination)
            self.assertEqual(path.read_text(), "my private notes")

    def test_package_contains_only_skill_resources_and_never_overwrites(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = media_os.package(temporary)
            with zipfile.ZipFile(target) as archive:
                self.assertEqual(set(archive.namelist()), {
                    "personal-media-os/" + name for name in media_os.SKILL_FILES
                })
            before = target.read_bytes()
            with self.assertRaises(ValueError):
                media_os.package(temporary)
            self.assertEqual(target.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
