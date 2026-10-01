# KREAGRICULTURE

Plant stress indicators from bioelectric (membrane voltage, Vmem) traces.
Part of the KIRA family: the same windowed-indicator approach used across
the portfolio, pointed at plants instead of patients.

## What it does

`PlantVeritas` extends the shared `BioelectricVeritas` adapter and adds four
rule-based scores, each between 0 and 1:

| Method | Signals it combines |
|---|---|
| `detect_stomatal_closure()` | per-node indicator + spatial gradient |
| `detect_drought_stress()` | hyperpolarised Vmem (< -100 mV) + high spatial entropy |
| `detect_nutrient_deficiency()` | estimated apoplastic pH (< 5.0) + gradient |
| `detect_root_stress()` | high spatial gradient + hyperpolarised Vmem (< -90 mV) |

`compute_apoplastic_ph()` maps Vmem to an estimated pH with a simple linear
rule, clipped to 5.0–8.0.

## Run it

```bash
python demo_runner.py
```

`demo_runner.py` generates a synthetic depolarisation scenario and prints
each score. It needs the KIRA `shared/` modules (`veritas_bioelectric_adapter`,
`kira_bioelectric_generator`) on the path; they live one level up in the
`kira-agriculture` workspace and are not yet published with this repo.

## Honest status

- Every threshold here is a **v0 starting point**, not a validated plant
  model. The scores are indicators for exploration, not agronomic advice.
- All data so far is **synthetic**. Replace thresholds once real sensor
  data from field trials is available.
- Generated files (`*.csv`, `__pycache__/`) are ignored by git.

## Related

- [krechill](https://github.com/OMWERERE/krechill), sister KIRA module

Built by Mwesigye Eugene (Ujo), Kampala.
