# SPECTER-01 T0

SPECTER-01 T0 is a deliberately small public test fixture for evaluating AI coding agents, model gateways, deterministic acceptance testing, and assurance workflows.

This repository is not intended to be a production security product.

Its purpose is to provide a reproducible environment where an agent can be given a bounded implementation task against a precommitted acceptance harness, and where success can be verified independently of the agent's own claims.

## Why this repository exists

Modern coding agents are very good at producing code, tests, scaffolding, and convincing completion reports.

That does not necessarily mean the resulting system works.

This repository is designed around a stricter rule:

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

The acceptance harness, not the agent, determines whether the task succeeded.

Current experiment

The first experiment tests false-positive restraint in a minimal SPECTER state engine.

Scenario:

QUIET
  ↓
short transient spike
  ↓
return to quiet

Required result:

ANOMALY must never be entered
final state must be QUIET

Frozen acceptance command:

./scripts/acceptance/transient_spike_no_anomaly.sh

A successful implementation must make that command exit 0 without modifying the acceptance fixture.

What this repo may be used to test

This repository may be deliberately reset, broken, modified, or reused to evaluate:

AI coding agents
model-routing gateways
local vs hosted models
agent tool use
deterministic acceptance testing
coding-agent reliability
policy enforcement
execution isolation
reproducibility
assurance receipts
failure recovery
multi-agent development workflows

Future experiments may use systems such as Hermes, OpenCode, Codex, Claude Code, local models, or other agent runtimes.

Design principle

A passing unit-test suite is useful evidence.

An agent saying that a task is complete is not.

The standard for this repository is:

real implementation
+ frozen acceptance test
+ reproducible execution
= evidence
Safety and scope

This is a controlled research and evaluation fixture.

It should not contain:

credentials
production secrets
private infrastructure details
sensitive operational data
proprietary datasets
Status

Experimental.

Expect the repository to change frequently as it is used for agent and assurance testing.


I particularly want to keep this line:

> **The acceptance criterion exists before the implementation, and the builder is not allowed to redefine it.**

That is the whole reason this repo is suddenly useful.

Since you already have the local repo open, the cleanest way is just:

```bash
cd ~/code/specter-01-t0
nano README.md
