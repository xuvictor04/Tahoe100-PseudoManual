---
symbol: "NIPAL3"
type: "gene"
col: 9
ensembl_id: "ENSG00000001461"
name: "NIPA like domain containing 3"
location: "1p36.11"
module: 76
arm: "+"
pooled_cpm: 32.22
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 25
n_dd_up_clean: 17
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# NIPAL3

*NIPA like domain containing 3* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.47× (z +16.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.233× (z -26.1, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.423× (z -15.4, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACL1]] (+0.70, fdr 7e-06), [[PLEKHM3]] (+0.63, fdr 1e-05), [[TFDP2]] (+0.62, fdr 1e-05); moves opposite to [[TMEM147-AS1]] (-0.51, fdr 6e-05), [[MIRLET7IHG]] (-0.49, fdr 1e-04), [[ST7L]] (-0.49, fdr 9e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +16.3 | 0e+00 | 44/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +14.9 | 0e+00 | 43/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +14.8 | 0e+00 | 35/46 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +14.4 | 4e-45 | 44/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +11.2 | 5e-27 | 42/48 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +7.7 | 2e-12 | 34/46 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.24×** | +7.6 | 2e-12 | 37/48 (HT-29, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +7.0 | 1e-10 | 34/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.5 | 4e-09 | 18/36 (hTERT-HPNE, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.0 | 1e-07 | 23/48 (A498, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +5.3 | 6e-06 | 22/47 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +5.3 | 7e-06 | 23/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.35×** | +5.2 | 7e-06 | 21/47 (SW480, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +5.1 | 1e-05 | 21/48 (A498, H4, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.70×** | +5.0 | 2e-05 | 22/46 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 2e-05 | 22/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 2e-04 | 18/48 (HOP62, KATO III, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.26×** | +4.3 | 5e-04 | 21/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 1e-03 | 20/48 (HOP62, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.233×** | -26.1 | 0e+00 | 48/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.423×** | -15.4 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.582×** | -13.7 | 2e-40 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -12.8 | 2e-35 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.491×** | -12.7 | 5e-35 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -11.5 | 2e-28 | 35/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.302×** | -11.2 | 3e-27 | 42/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.536×** | -11.1 | 5e-27 | 34/46 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[EX229 (drug)]] 5 µM |  | **0.326×** | -10.5 | 5e-24 | 41/47 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.346×** | -10.0 | 1e-21 | 41/47 (HT-29, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.346×** | -10.0 | 1e-21 | 36/45 (PANC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -9.5 | 1e-19 | 32/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.366×** | -9.4 | 2e-19 | 38/47 (SW1417, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.506×** | -8.7 | 1e-16 | 39/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -6.9 | 2e-10 | 28/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.714×** | -5.7 | 5e-07 | 27/48 (Hs 766T, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.736×** | -5.5 | 2e-06 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.726×** | -5.4 | 2e-06 | 25/48 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.0 | 4 | 10 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.126× (z -20.5) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.182× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 22.4 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.275× (z -11.0) |
| [[HT-29 (line)]] | alt | 51.0 | 4 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.158× (z -19.6) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.195× (z -9.1) |
| [[LS 180 (line)]] | wt | 67.8 | 4 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -10.7) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.464× (z -8.5) |
| [[SW480 (line)]] | alt | 52.1 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.225× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -16.8) |
| [[C32 (line)]] | wt | 65.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -16.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -12.3) |
| [[HOP62 (line)]] | alt | 22.1 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 4.26× (z +9.1) | [[Digitoxin (drug)]] 0.5 µM 0.199× (z -10.1) |
| [[A498 (line)]] | wt | 31.4 | 2 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.70× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.231× (z -13.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -9.3) |
| [[J82 (line)]] | alt | 25.3 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.220× (z -11.8) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -8.8) |
| [[LoVo (line)]] | wt | 32.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +13.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -17.2) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 30.8 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0720× (z -18.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 20.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.229× (z -8.9) |
| [[C-33 A (line)]] | alt | 35.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -11.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 47.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -9.7) |
| [[H4 (line)]] | wt | 51.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 40.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +13.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -14.8) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.185× (z -11.3) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0686× (z -9.4) |
| [[KATO III (line)]] | alt | 44.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.176× (z -14.9) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -13.8) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.235× (z -9.5) |
| [[SW1417 (line)]] | alt | 27.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.149× (z -14.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0533× (z -11.3) |
| [[A-427 (line)]] | wt | 32.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 18.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.140× (z -12.2) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 50.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 52.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 28.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 28.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -11.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 30.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -9.4) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 45.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.370× (z -8.6) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -12.0) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.219× (z -11.5) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -10.7) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACL1]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[PLEKHM3]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TFDP2]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[WIPI2]] | +0.61 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[MBTPS1]] | +0.59 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[UBE4B]] | +0.58 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ZNF277]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CRIPT]] | +0.57 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[MACO1]] | +0.57 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[GINM1]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[FBXO3]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[FBXL20]] | +0.56 | +0.31 / +0.59 | both halves | 2e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM147-AS1]] | -0.51 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[MIRLET7IHG]] | -0.49 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ST7L]] | -0.49 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[MMP25]] | -0.48 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[RXYLT1]] | -0.48 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[SLC13A3]] | -0.47 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[CFAP161]] | -0.46 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[PPIEL-1]] | -0.46 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[RBM26-AS1]] | -0.46 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[EXOSC6]] | -0.46 | -0.41 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers NIPAL3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.2, -46.7); signed map (-19.6, 8.6). **Vector** length 90.9, 24.3% of its response variance represented; |z| ≥ 3 in 1,557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | +7.1 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.6 |
|  | [[NG25 (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +7.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.6 | -26.1 |
|  | [[EX229 (drug)]] 5 µM |  | -7.2 | -10.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.9 | -11.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.6 | -9.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.5 | -10.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.4 | -10.0 |

## What is on record

|  |  |
|---|---|
| Name | NIPA like domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,415,802-24,472,976 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DJ462O23.2, SLC57A5; previously NPAL3 |
| Gene groups (HGNC) | Solute carrier family 57, NIPA-like magnesium transporters |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

UniProt [Q6P499](https://www.uniprot.org/uniprotkb/Q6P499) carries no function annotation.

**Summary**, from NCBI Gene [57185](https://www.ncbi.nlm.nih.gov/gene/57185):

> Predicted to enable magnesium ion transmembrane transporter activity. Predicted to be involved in magnesium ion transport. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25233) · Entrez [57185](https://www.ncbi.nlm.nih.gov/gene/57185) · UniProt [Q6P499](https://www.uniprot.org/uniprotkb/Q6P499) · Ensembl [ENSG00000001461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001461)

## Data

Gene col 9: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9]; `tensor/DDL_lfc|DDL_z.npy` [9]; `embed/gene_vectors.npy` [9]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9 or target_col == 9). Every well: [[NIPAL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPAL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
