# SPECTER-01 T0

SPECTER-01 T0 is a deliberately small public fixture for evaluating AI coding
agents, deterministic acceptance testing, and assurance workflows. It is not a
production security product.

Its purpose is to give an agent a bounded implementation task backed by a
precommitted acceptance harness, so success can be verified independently of
the agent's own claims.

## Design principle

> **The acceptance criterion exists before the implementation, and the builder is not allowed to redefine it.**

The workflow is:

```text
precommit acceptance test
        ↓
give bounded task to agent
        ↓
agent implements
        ↓
run frozen acceptance harness
        ↓
independent PASS / FAIL
```

The acceptance harness, not the agent, determines whether the task succeeded.

## Current experiment: transient-spike restraint

The deterministic replay fixture describes a quiet baseline, one 100 ms
transient spike, and a return to quiet. The state engine must demonstrate
false-positive restraint: it must never enter `ANOMALY` and must finish in
`QUIET`.

Run the frozen acceptance harness from the repository root:

```sh
./scripts/acceptance/transient_spike_no_anomaly.sh
```

The harness invokes this fixed CLI contract:

```sh
./bin/specter-t0 replay test/replay/transient_spike.json
```

Acceptance requires all of the following:

- The replay command exits with status 0.
- The replay command's combined standard output and standard error do not
  contain `ANOMALY`.
- The last non-empty line of replay command output is exactly
  `FINAL_STATE=QUIET`.

## Repository contents

- `test/replay/transient_spike.json` is the deterministic replay fixture.
- `scripts/acceptance/transient_spike_no_anomaly.sh` is the frozen acceptance
  harness.
- `README.md` documents the experiment and CLI contract.

## Baseline status

The harness is intentionally **RED** at this baseline because
`./bin/specter-t0` does not exist. No state-engine implementation, mock, or
build system is included to make the harness pass.

A successful implementation must make the frozen acceptance command exit 0
without changing the acceptance harness or replay fixture.

## Safety and scope

This repository is a controlled research and evaluation fixture. It must not
contain credentials, production secrets, private infrastructure details,
sensitive operational data, or proprietary datasets.
