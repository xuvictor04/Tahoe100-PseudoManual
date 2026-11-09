---
symbol: "WEE1"
type: "gene"
col: 9319
ensembl_id: "ENSG00000166483"
name: "WEE1 G2 checkpoint kinase"
location: "11p15.4"
module: 22
arm: "+"
pooled_cpm: 67.76
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 44
n_dd_up_clean: 5
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# WEE1

*WEE1 G2 checkpoint kinase* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.03× (z +11.4, q 2e-27, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.336× (z -17.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF22]] (+0.64, fdr 7e-06), [[NUSAP1]] (+0.62, fdr 1e-05), [[FBXO5]] (+0.62, fdr 7e-06); moves opposite to [[SIKE1]] (-0.57, fdr 1e-05), [[DNAJC24]] (-0.51, fdr 3e-05), [[NDUFB9]] (-0.49, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.03×** | +11.4 | 2e-27 | 47/49 (J82, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.02×** | +9.1 | 3e-17 | 37/48 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.68×** | +8.2 | 5e-14 | 34/48 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.58×** | +7.2 | 6e-11 | 29/48 (J82, H4, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.9 | 8e-10 | 33/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.53×** | +6.7 | 2e-09 | 31/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.48×** | +5.7 | 7e-07 | 33/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.41×** | +5.4 | 4e-06 | 28/47 (J82, H4, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.37×** | +4.6 | 3e-04 | 21/49 (NCI-H460, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.32×** | +4.0 | 0.003 | 21/47 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.18× | +3.7 | 0.010 | 15/49 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.25×** | +3.5 | 0.024 | 19/48 (C-33 A, AN3 CA, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.053 | 15/49 (C-33 A, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.069 | 12/48 (NCI-H460, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.336×** | -17.0 | 0e+00 | 47/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.349×** | -16.5 | 0e+00 | 45/48 (HOP62, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.569×** | -12.5 | 2e-33 | 39/48 (A549, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -11.3 | 1e-27 | 41/48 (HepG2/C3A, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -10.6 | 2e-24 | 36/43 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.506×** | -10.0 | 9e-22 | 40/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.530×** | -9.9 | 3e-21 | 36/48 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.642×** | -9.8 | 8e-21 | 41/48 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.549×** | -9.4 | 5e-19 | 43/48 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.555×** | -9.2 | 2e-18 | 33/47 (C-33 A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.556×** | -9.2 | 2e-18 | 30/48 (HEC-1-A, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.619×** | -7.5 | 4e-12 | 33/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.419×** | -7.1 | 5e-11 | 35/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.633×** | -6.6 | 2e-09 | 32/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.658×** | -6.5 | 2e-09 | 29/48 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -6.2 | 2e-08 | 30/48 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.766×** | -5.9 | 2e-07 | 32/48 (SW48, A549, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.561×** | -4.7 | 7e-05 | 26/46 (HS-578T, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.826×** | -4.2 | 7e-04 | 23/48 (HCT15, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -4.1 | 0.001 | 23/48 (NCI-H1573, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.615×** | -4.0 | 0.002 | 18/48 (NCI-H2030, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.619×** | -3.9 | 0.002 | 23/47 (SNU-423, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 95.6 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -15.2) |
| [[HOP62 (line)]] | alt | 69.2 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -15.9) |
| [[A498 (line)]] | wt | 97.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.301× (z -10.9) |
| [[PANC-1 (line)]] | alt | 121 | 2 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.75× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.206× (z -13.6) |
| [[SNU-423 (line)]] | alt | 136 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -13.5) |
| [[J82 (line)]] | alt | 110 | 2 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +10.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.93× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.349× (z -11.4) |
| [[C-33 A (line)]] | alt | 135 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.81× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0382× (z -29.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.344× (z -9.5) |
| [[HT-29 (line)]] | alt | 144 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 67.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -13.4) |
| [[A-172 (line)]] | wt | 43.4 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.87× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -15.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 96.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.206× (z -12.4) |
| [[Hs 766T (line)]] | wt | 78.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 69.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.291× (z -10.7) |
| [[SHP-77 (line)]] | alt | 61.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.240× (z -11.3) |
| [[SW1417 (line)]] | alt | 59.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.11× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.469× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 62.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -12.1) |
| [[A-427 (line)]] | wt | 43.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.45× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.407× (z -11.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 58.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.94× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.296× (z -14.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 72.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.181× (z -8.5) |
| [[COLO 205 (line)]] | alt | 93.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0909× (z -13.2) |
| [[RKO (line)]] | wt | 62.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.8× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 58.2 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.219× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 61.1 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 9.23× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -8.7) |
| [[SW48 (line)]] | wt | 68.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0610× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Amsacrine (drug)]] 5 µM 0.383× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 46.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -10.0) |
| [[HS-578T (line)]] | alt | 52.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 49.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -9.0) |
| [[LoVo (line)]] | wt | 35.6 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.02× (z +9.1) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 36.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 13.6× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 60.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 74.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 41.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.16× (z +9.1) ⚠ toxic | [[Selinexor (drug)]] 5 µM 0.459× (z -9.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AsPC-1 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 115 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -11.8) |
| [[C32 (line)]] | wt | 57.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -9.8) |
| [[HCT15 (line)]] | alt | 43.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.215× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 46.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 59.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.272× (z -10.1) |
| [[NCI-H661 (line)]] | alt | 74.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 60.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -13.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF22]] | +0.64 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[NUSAP1]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[FBXO5]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 | pathway: G1/S Transition; STRING 569 |
| [[KIF23]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[GTSE1]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[CDCA8]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 694 |
| [[TPX2]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 | pathway: G2/M Transition |
| [[STMN1]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[TOP2A]] | +0.60 | +0.58 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS; STRING 532 |
| [[KIF2C]] | +0.60 | +0.58 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDC25C]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints; STRING 946 |
| [[CDK1]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 998 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIKE1]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[DNAJC24]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[NDUFB9]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WEE1's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.4, -54.5); signed map (-48.4, -44.5). **Vector** length 133, 43.9% of its response variance represented; |z| ≥ 3 in 1,700 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.52 to 28); *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.53 to 8); *Kinesins* (reactome, mean cos +0.55 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.2 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.2 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +9.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.8 | +8.2 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +3.7 | +4.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +1.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.0 | +2.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -8.5 | -10.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -7.7 | -12.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -6.5 | -9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -9.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -6.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | WEE1 G2 checkpoint kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:9,573,670-9,593,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WEE1A |
| Gene groups (HGNC) | WEE family tyrosine specific kinases |
| Hallmark sets | APOPTOSIS, E2F_TARGETS |
| Reactome | 18 pathways, smallest: G2/M DNA replication checkpoint; Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex; Polo-like kinase mediated events |
| Matched by | ensembl_id |

**Function**, from UniProt [P30291](https://www.uniprot.org/uniprotkb/P30291) (Wee1-like protein kinase):

> Acts as a negative regulator of entry into mitosis (G2 to M transition) by protecting the nucleus from cytoplasmically activated cyclin B1-complexed CDK1 before the onset of mitosis by mediating phosphorylation of CDK1 on 'Tyr-15'. Specifically phosphorylates and inactivates cyclin B1-complexed CDK1 reaching a maximum during G2 phase and a minimum as cells enter M phase. Phosphorylation of cyclin B1-CDK1 occurs exclusively on 'Tyr-15' and phosphorylation of monomeric CDK1 does not occur. Its …

**Summary**, from NCBI Gene [7465](https://www.ncbi.nlm.nih.gov/gene/7465):

> This gene encodes a nuclear protein, which is a tyrosine kinase belonging to the Ser/Thr family of protein kinases. This protein catalyzes the inhibitory tyrosine phosphorylation of CDC2/cyclin B kinase, and appears to coordinate the transition between DNA replication and mitosis by protecting the nucleus from cytoplasmically activated CDC2 kinase. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12761) · Entrez [7465](https://www.ncbi.nlm.nih.gov/gene/7465) · UniProt [P30291](https://www.uniprot.org/uniprotkb/P30291) · Ensembl [ENSG00000166483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166483)

## Data

Gene col 9319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9319); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9319]; `tensor/DDL_lfc|DDL_z.npy` [9319]; `embed/gene_vectors.npy` [9319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9319 or target_col == 9319). Every well: [[WEE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WEE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
