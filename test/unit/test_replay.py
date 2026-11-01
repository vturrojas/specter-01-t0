import json
import subprocess
import tempfile
import unittest
from pathlib import Path

CLI = Path(__file__).resolve().parents[2] / 'bin' / 'specter-t0'


class ReplayTests(unittest.TestCase):
    def replay(self, values, **overrides):
        data = {
            'schema_version': 1,
            'tick_ms': 100,
            'samples': [{'tick': i, 'value': value} for i, value in enumerate(values)],
            **overrides,
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'replay.json'
            path.write_text(json.dumps(data))
            return subprocess.run([str(CLI), 'replay', str(path)], text=True, capture_output=True)

    def test_transient_spike_stays_quiet_even_if_metadata_claims_anomaly(self):
        result = self.replay([0, 1, 0, 0], expected={'final_state': 'ANOMALY'})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, 'FINAL_STATE=QUIET\n')

    def test_sustained_elevation_enters_anomaly_and_recovers(self):
        result = self.replay([0, 0.5, 0.8, 1, 0, 0, 0])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, 'STATE=ANOMALY\nSTATE=QUIET\nFINAL_STATE=QUIET\n')

    def test_sustained_elevation_remains_anomaly_without_full_recovery(self):
        result = self.replay([1, 1, 1, 0, 0])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, 'STATE=ANOMALY\nFINAL_STATE=ANOMALY\n')

    def test_missing_ticks_break_streak(self):
        result = self.replay([], samples=[{'tick': 0, 'value': 1}, {'tick': 2, 'value': 1}, {'tick': 3, 'value': 1}])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, 'FINAL_STATE=QUIET\n')

    def test_invalid_input_fails_without_final_state(self):
        for samples in ([], [{'tick': 0, 'value': True}], [{'tick': 1, 'value': 1}, {'tick': 1, 'value': 1}]):
            with self.subTest(samples=samples):
                result = self.replay([], samples=samples)
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn('FINAL_STATE=', result.stdout)


if __name__ == '__main__':
    unittest.main()
