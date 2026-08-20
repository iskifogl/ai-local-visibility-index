#!/usr/bin/env python3
"""Reproduce every headline number in the README from the raw dataset.

Usage:  python3 scripts/summarize.py data/2026-08-15.json
"""
import json, sys, collections

path = sys.argv[1] if len(sys.argv) > 1 else 'data/2026-08-15.json'
d = json.load(open(path))
m = d['markets']

roster = sum(x['rosterSize'] for x in m) / len(m)
strict = sum(len(x['namedStrict']) for x in m) / len(m)
loose = sum(len(x['namedLoose']) for x in m) / len(m)

print(f"study    : {d['study']}")
print(f"collected: {d['collected']}")
print(f"markets  : {len(m)}\n")

print(f"Google Maps roster, mean per market : {roster:.1f}")
print(f"named by any engine (strict match)  : {strict:.1f}  ({strict/roster*100:.2f}%)")
print(f"named by any engine (loose match)   : {loose:.1f}  ({loose/roster*100:.2f}%)\n")

eng = collections.defaultdict(list)
for x in m:
    for k, v in (x.get('namedStrictByEngine') or {}).items():
        eng[k].append(len(v) if isinstance(v, list) else v)

print("by engine (mean businesses named per market):")
for k, v in sorted(eng.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
    avg = sum(v) / len(v)
    print(f"  {k:14s} {avg:5.2f}  ({avg/roster*100:5.2f}% of roster)")

vert = collections.defaultdict(list)
for x in m:
    vert[x['market'].split('/')[0].strip()].append(
        len(x['namedStrict']) / x['rosterSize'] * 100)
print("\nby vertical (share of roster named by any engine):")
for k, v in sorted(vert.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
    print(f"  {k:14s} {sum(v)/len(v):5.2f}%")

ov = sum(1 for x in m if x.get('aiOverviewBlockPresent'))
print(f"\nAI Overviews block present in {ov}/{len(m)} markets")
