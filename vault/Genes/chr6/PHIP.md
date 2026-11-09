---
symbol: "PHIP"
type: "gene"
col: 7078
ensembl_id: "ENSG00000146247"
name: "PHIP subunit of CUL4-Ring ligase complex"
location: "6q14.1"
module: 74
arm: "+"
pooled_cpm: 281.38
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# PHIP

*PHIP subunit of CUL4-Ring ligase complex* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +18.5, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.482× (z -24.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GKAP1]] (+0.66, fdr 1e-05), [[SCAF11]] (+0.66, fdr 1e-05), [[BRWD1]] (+0.60, fdr 1e-05); moves opposite to [[RNPS1]] (-0.59, fdr 4e-05), [[CDC37]] (-0.54, fdr 2e-05), [[SLC35C1]] (-0.52, fdr 3e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +18.5 | 0e+00 | 43/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +17.7 | 0e+00 | 32/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +15.8 | 0e+00 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.48×** | +12.6 | 3e-34 | 37/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +12.0 | 5e-31 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +10.3 | 7e-23 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +9.4 | 5e-19 | 36/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.17× | +5.4 | 5e-06 | 23/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.8 | 1e-04 | 19/48 (LOX-IMVI, SNU-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 1.15× | +4.7 | 1e-04 | 24/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.14× | +4.4 | 6e-04 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +4.2 | 0.001 | 10/49 (A-427, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +4.2 | 0.001 | 16/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.004 | 20/48 (COLO 205, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.10× | +3.3 | 0.041 | 18/48 (A549, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.482×** | -24.5 | 0e+00 | 48/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.542×** | -20.5 | 0e+00 | 46/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -19.6 | 0e+00 | 45/49 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -16.6 | 0e+00 | 40/44 (C-33 A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.602×** | -16.4 | 0e+00 | 47/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.645×** | -14.7 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.651×** | -13.3 | 1e-38 | 42/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.677×** | -13.1 | 2e-37 | 42/49 (AsPC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.778×** | -11.9 | 6e-31 | 36/48 (A498, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -10.5 | 3e-24 | 41/48 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -10.5 | 4e-24 | 27/48 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.788×** | -8.0 | 6e-14 | 30/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.665×** | -7.2 | 3e-11 | 39/48 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.802×** | -7.1 | 4e-11 | 30/50 (SW 900, AN3 CA, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.666×** | -7.1 | 4e-11 | 41/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.693×** | -6.4 | 4e-09 | 37/47 (SW480, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.701×** | -6.2 | 1e-08 | 39/48 (SW480, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.726×** | -5.6 | 5e-07 | 30/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -5.4 | 2e-06 | 19/48 (RKO, NCI-H1573, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.836× | -4.3 | 4e-04 | 20/48 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.801×** | -3.9 | 0.002 | 21/49 (SW480, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.896× | -3.7 | 0.004 | 9/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.005 | 20/48 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.928× | -3.5 | 0.007 | 1/48 (hTERT-HPNE) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 273 | 6 (3 ⚠) | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +17.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.78× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -20.1) |
| [[NCI-H460 (line)]] | wt | 251 | 9 (5 ⚠) | 6 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.54× (z +20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.21× (z +17.3) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -14.8) |
| [[PANC-1 (line)]] | alt | 288 | 9 (6 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +26.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -14.6) |
| [[SW480 (line)]] | alt | 317 | 8 (4 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +22.1) | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -27.2) |
| [[HEC-1-A (line)]] | alt | 421 | 5 (4 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +16.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -19.8) |
| [[LS 180 (line)]] | wt | 301 | 7 (4 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +24.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 274 | 3 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -15.8) |
| [[SW 900 (line)]] | alt | 259 | 3 (1 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -16.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.397× (z -14.9) |
| [[A498 (line)]] | wt | 183 | 2 (2 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +14.1) ⚠ cell-cycle shift, explains ~43% of this change | [[Selinexor (drug)]] 5 µM 0.518× (z -15.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.648× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 248 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +13.0) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 5 µM 0.444× (z -16.0) |
| [[SW1417 (line)]] | alt | 248 | 4 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +14.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.69× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -17.8) |
| [[SW48 (line)]] | wt | 357 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -15.9) |
| [[A-427 (line)]] | wt | 232 | 3 (2 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.80× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.513× (z -12.1) |
| [[A549 (line)]] | wt | 205 | 5 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +19.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -14.5) |
| [[AN3 CA (line)]] | alt | 626 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.361× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 211 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 280 | 0 | 8 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.178× (z -17.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.414× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 213 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.6) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -12.8) |
| [[C-33 A (line)]] | alt | 503 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -30.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.360× (z -15.2) |
| [[HepG2_C3A (line)]] | wt | 284 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -13.8) |
| [[HOP62 (line)]] | alt | 209 | 4 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -10.7) |
| [[HT-29 (line)]] | alt | 271 | 3 (2 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.26× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 343 | 1 (1 ⚠) | 6 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.76× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -16.4) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.399× (z -15.0) |
| [[SHP-77 (line)]] | alt | 346 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.433× (z -14.2) |
| [[SNU-1 (line)]] | wt | 410 | 4 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -13.5) |
| [[SNU-423 (line)]] | alt | 397 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.4) ⚠ cell-cycle shift, explains ~43% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -10.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.480× (z -10.5) |
| [[COLO 205 (line)]] | alt | 208 | 3 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 392 | 3 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.541× (z -9.3) |
| [[RKO (line)]] | wt | 367 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.534× (z -8.7) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 258 | 4 (3 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 2.57× (z +13.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.494× (z -10.1) |
| [[BT-474 (line)]] | alt | 283 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -17.9) |
| [[H4 (line)]] | wt | 225 | 4 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.53× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 349 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -17.4) |
| [[hTERT-HPNE (line)]] | wt | 267 | 3 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.446× (z -9.1) |
| [[J82 (line)]] | alt | 239 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +12.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -13.6) |
| [[LoVo (line)]] | wt | 266 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.91× (z +19.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +17.8) | — |
| [[NCI-H2030 (line)]] | alt | 326 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.364× (z -17.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 529 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -11.1) |
| [[NCI-H661 (line)]] | alt | 1,238 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.0) |
| [[HS-578T (line)]] | alt | 236 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.9) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.626× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 268 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 5 µM 0.468× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -11.4) |
| [[A-172 (line)]] | wt | 182 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[C32 (line)]] | wt | 229 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.468× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 308 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 168 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 393 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GKAP1]] | +0.66 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[SCAF11]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 | STRING 504 |
| [[BRWD1]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 | same gene group |
| [[RSBN1L]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[KMT2A]] | +0.60 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[LCORL]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SMCHD1]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 | STRING 570 |
| [[SMC3]] | +0.58 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[SETD2]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[DEK]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[CEP350]] | +0.58 | +0.36 / +0.62 | both halves | 9e-05 | STRING 524 |
| [[TUT4]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPS1]] | -0.59 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CDC37]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 | pathway: RHOBTB GTPase Cycle |
| [[SLC35C1]] | -0.52 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[CDK9]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HARS1]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.51 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[URB1]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[SNHG16]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[SPTLC1]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[RPSA]] | -0.51 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[PIGG]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[EIF3I]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PHIP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.9, -30.3); signed map (5.4, -14.5). **Vector** length 125, 47.0% of its response variance represented; |z| ≥ 3 in 1,650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.6 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +7.2 | +17.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.9 | +9.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.5 | +0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.3 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.5 | -10.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.2 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -7.3 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.9 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.4 | -7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.2 | -7.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | PHIP subunit of CUL4-Ring ligase complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:78,934,419-79,078,287 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ndrp, BRWD2, RepID, DCAF14, FLJ20705; previously WDR11 |
| Gene groups (HGNC) | Bromodomain and WD repeat domain containing |
| Reactome | 5 pathways, smallest: RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWQ0](https://www.uniprot.org/uniprotkb/Q8WWQ0) (PH-interacting protein):

> Probable regulator of the insulin and insulin-like growth factor signaling pathways. Stimulates cell proliferation through regulation of cyclin transcription and has an anti-apoptotic activity through AKT1 phosphorylation and activation. Plays a role in the regulation of cell morphology and cytoskeletal organization.

**Summary**, from NCBI Gene [55023](https://www.ncbi.nlm.nih.gov/gene/55023):

> This gene encodes a protein that binds to the insulin receptor substrate 1 protein and regulates glucose transporter translocation in skeletal muscle cells. The encoded protein may also regulate growth and survival of pancreatic beta cells. Elevated copy number of this gene may be associated with melanoma severity and the encoded protein may promote melanoma metastasis in human patients. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:15673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15673) · Entrez [55023](https://www.ncbi.nlm.nih.gov/gene/55023) · UniProt [Q8WWQ0](https://www.uniprot.org/uniprotkb/Q8WWQ0) · Ensembl [ENSG00000146247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146247)

## Data

Gene col 7078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7078); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7078]; `tensor/DDL_lfc|DDL_z.npy` [7078]; `embed/gene_vectors.npy` [7078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7078 or target_col == 7078). Every well: [[PHIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
