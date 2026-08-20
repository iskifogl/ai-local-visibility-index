# AI Local Visibility Index

How many of the local businesses Google Maps returns for a buyer query actually get
named by an AI assistant?

This repository holds the raw dataset, the method and a script that reproduces every
number below. Collected 15-16 August 2026 across 48 US markets.

## Headline results

Google Maps returns **97.0** businesses for a typical buyer query. Across four AI
assistants, **11.6** of them (11.94%) get named by any engine. The other 88% are
absent from AI answers regardless of where they rank in Maps.

| engine | businesses named per market | share of the Maps roster |
|---|---|---|
| Google AI Overviews | 7.83 | 8.07% |
| ChatGPT | 4.29 | 4.42% |
| Gemini | 2.79 | 2.88% |
| Claude | 1.92 | 1.98% |

By vertical:

| vertical | share named |
|---|---|
| gym | 14.41% |
| coffee shop | 14.13% |
| plumber | 12.18% |
| dentist | 11.51% |
| law firm | 10.02% |
| hair salon | 9.71% |

An AI Overviews block appeared in 47 of the 48 markets.

## Method

48 markets, built from 8 US cities (Austin TX, Boise ID, Columbus OH, Denver CO,
Nashville TN, Portland OR, Raleigh NC, Tucson AZ) across 6 verticals.

For each market:

1. **Denominator.** Query Google Maps for `<vertical> in <city>` at the city
   coordinate, depth 100, deduplicated by title. This is the roster.
2. **Questions.** Three fixed question phrasings per market, asked to four engines,
   three samples per phrasing. Phrasings were written and frozen before collection.
3. **Matching.** Strict phrase match against the roster. A looser matcher is reported
   alongside as an upper bound. A business counts once per engine no matter how many
   times it is named.

### The caveat that changes how you read the engine table

**Google AI Overviews was measured with live web search. The three chat engines were
queried at their production model tier without web browsing enabled.** So the bottom
three rows measure what those models know, not what they can look up. That was the
intended comparison, but it means these numbers are not a claim about what a user of
the consumer ChatGPT product sees today.

## Limitations

- **The denominator is capped.** Maps was queried at depth 100 and several markets came
  back with exactly 100 rows, so the real market is larger than what was counted. The
  published share is an upper bound against "all local businesses" and is not comparable
  to figures that use a wider, unstated denominator.
- **One country, one language.** US cities, English questions.
- **One collection pass.** No trend claim is possible from this data.
- **Google Maps is not a registry.** It is itself a ranked, filtered surface. The
  denominator is "what Google shows", not "what exists".
- **Production model tiers.** Each engine was queried at the tier run in production. A
  larger model may answer differently.

## Reproducing the numbers

```
python3 scripts/summarize.py data/2026-08-15.json
```

No dependencies beyond the Python standard library. Every figure in this README is
printed by that script.

## Data

`data/2026-08-15.json` contains, per market: the roster size, the businesses named
under the strict and loose matchers, the per-engine strict breakdown, whether an AI
Overviews block was present, and any dropped samples.

Individual raw model responses are not published here because they contain third-party
business names in contexts that cannot be verified. They are available on request for
methodology review.

Future collection passes will be added as new dated files in `data/`. Existing files
are not edited after publication.

## Citing

> AI Local Visibility Index, collected 15-16 August 2026. https://localseen.ai/research

Method notes and the rendered study live at <https://localseen.ai/research>.

## Who made this

Built and published by [LocalSeen](https://localseen.ai), which sells an AI visibility
tracking tool for local businesses. That is a financial interest in this subject, which
is exactly why the dataset, the method and the reproduction script are all public. Check
the numbers rather than taking them.

## License

Data is licensed **CC BY 4.0**. Scripts are **MIT**. See [LICENSE](LICENSE).
