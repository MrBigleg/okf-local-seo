import datetime as dt
import tempfile
import unittest
from pathlib import Path

from weekly_review import build_report, cadence_days, evidence_date, parsed_date


class WeeklyReviewTests(unittest.TestCase):
    def test_parsed_date_accepts_timestamp_prefix(self):
        self.assertEqual(parsed_date("2026-07-06T00:00:00Z"), dt.date(2026, 7, 6))
        self.assertIsNone(parsed_date("living document"))

    def test_cadence_uses_publication_tiers(self):
        self.assertEqual(cadence_days(Path("agentic/ask-maps.md"), "Concept"), 31)
        self.assertEqual(cadence_days(Path("references/google.md"), "Reference"), 92)
        self.assertEqual(cadence_days(Path("gbp/reviews.md"), "Concept"), 183)

    def test_report_flags_due_and_missing_dates(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = Path(directory)
            (bundle / "agentic").mkdir()
            (bundle / "agentic" / "old.md").write_text(
                "---\ntype: Concept\ntimestamp: 2026-01-01T00:00:00Z\n---\nbody\n",
                encoding="utf-8",
            )
            (bundle / "fresh.md").write_text(
                "---\ntype: Concept\ntimestamp: 2026-07-01T00:00:00Z\n---\nbody\n",
                encoding="utf-8",
            )
            (bundle / "missing.md").write_text(
                "---\ntype: Concept\n---\nbody\n",
                encoding="utf-8",
            )
            report = build_report(bundle, dt.date(2026, 7, 15))
            self.assertIn("`agentic/old.md`", report)
            self.assertIn("`missing.md`", report)
            self.assertNotIn("`fresh.md`", report)

    def test_evidence_date_prefers_verified_then_generated(self):
        generated = "{ by: human:x, at: 2026-01-01T00:00:00Z }"
        verified = "{ by: human:x, at: 2026-06-01T00:00:00Z }"
        # `verified` is the strongest signal, then `generated`, then v0.1 fallbacks.
        self.assertEqual(
            evidence_date({"generated": generated, "verified": verified}),
            dt.date(2026, 6, 1),
        )
        self.assertEqual(evidence_date({"generated": generated}), dt.date(2026, 1, 1))
        self.assertEqual(
            evidence_date({"timestamp": "2025-12-01T00:00:00Z"}), dt.date(2025, 12, 1)
        )
        self.assertIsNone(evidence_date({}))

    def test_stale_after_overrides_cadence(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = Path(directory)
            # Recently generated, but the page declares itself already stale.
            (bundle / "due.md").write_text(
                "---\ntype: Concept\n"
                "generated: { by: human:x, at: 2026-07-10T00:00:00Z }\n"
                "stale_after: 2026-07-14\n---\nbody\n",
                encoding="utf-8",
            )
            # Old enough to trip the 183-day cadence, but not yet past stale_after.
            (bundle / "held.md").write_text(
                "---\ntype: Concept\n"
                "generated: { by: human:x, at: 2026-01-01T00:00:00Z }\n"
                "stale_after: 2026-12-01\n---\nbody\n",
                encoding="utf-8",
            )
            report = build_report(bundle, dt.date(2026, 7, 15))
            self.assertIn("`due.md`", report)
            self.assertNotIn("`held.md`", report)


if __name__ == "__main__":
    unittest.main()
