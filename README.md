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
