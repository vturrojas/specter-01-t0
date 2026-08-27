# SPECTER-01 T0

This repository freezes the first IOC acceptance criterion before any state-engine implementation exists.

## IOC Task 001: transient-spike restraint

The deterministic replay fixture describes a quiet baseline, one 100 ms transient spike, and a return to quiet. The engine must show false-positive restraint: it must never enter `ANOMALY` and must finish in `QUIET`.

Run the acceptance harness from the repository root:

```sh
./scripts/acceptance/transient_spike_no_anomaly.sh
```

The harness invokes this fixed CLI contract:

```sh
./bin/specter-t0 replay test/replay/transient_spike.json
```

Acceptance requires all of the following:

- the replay command exits with status 0;
- combined standard output and standard error do not contain `ANOMALY`;
- the last non-empty output line is exactly `FINAL_STATE=QUIET`.

The harness is intentionally RED at this baseline because `./bin/specter-t0` does not exist. No implementation, mock, or build system is included to make it pass.
