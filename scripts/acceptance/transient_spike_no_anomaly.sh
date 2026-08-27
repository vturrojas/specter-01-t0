#!/usr/bin/env bash

set -uo pipefail

repo_root="$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)"
cd "$repo_root"

set +e
output="$(./bin/specter-t0 replay test/replay/transient_spike.json 2>&1)"
command_status=$?
set -e

printf '%s\n' "$output"

if (( command_status != 0 )); then
  printf 'FAIL: replay command exited with status %d\n' "$command_status" >&2
  exit "$command_status"
fi

if grep -Fq 'ANOMALY' <<<"$output"; then
  printf 'FAIL: replay output entered ANOMALY\n' >&2
  exit 1
fi

final_state_line="$(awk 'NF { line = $0 } END { print line }' <<<"$output")"
if [[ "$final_state_line" != 'FINAL_STATE=QUIET' ]]; then
  printf 'FAIL: replay output did not end with exact final-state line: FINAL_STATE=QUIET\n' >&2
  exit 1
fi

printf 'PASS: transient spike did not enter ANOMALY and returned to QUIET\n'
