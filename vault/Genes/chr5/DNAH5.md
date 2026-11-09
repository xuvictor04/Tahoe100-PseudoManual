---
symbol: "DNAH5"
type: "gene"
col: 460
ensembl_id: "ENSG00000039139"
name: "dynein axonemal heavy chain 5"
location: "5p15.2"
module: 104
arm: "+"
pooled_cpm: 49.77
n_lines_expressing: 40
n_dd_up: 20
n_dd_down: 31
n_dd_up_clean: 19
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# DNAH5

*dynein axonemal heavy chain 5* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.70× (z +6.0, q 1e-06, up in 21 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.467× (z -12.0, q 2e-30, down in 31 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00886]] (+0.68, fdr 7e-06), [[SLC7A2]] (+0.59, fdr 1e-05), [[JADE1]] (+0.59, fdr 1e-05); moves opposite to [[UBA6]] (-0.58, fdr 2e-05), [[AZIN2]] (-0.55, fdr 3e-05), [[NQO2]] (-0.52, fdr 4e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 5 go from it, the strongest it → [[JPH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.70×** | +6.0 | 1e-06 | 21/37 (SHP-77, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 3e-04 | 21/38 (SHP-77, SNU-423, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.8 | 3e-04 | 24/38 (C-33 A, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 0.002 | 19/37 (MIA PaCa-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.50×** | +4.1 | 0.004 | 18/38 (A-172, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **2.01×** | +4.1 | 0.004 | 24/38 (NCI-H2347, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.006 | 19/37 (NCI-H2030, HOP62, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.006 | 19/38 (HOP62, NCI-H2030, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.012 | 18/38 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.82×** | +3.5 | 0.025 | 16/38 (NCI-H2347, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.028 | 18/38 (SHP-77, A549, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.028 | 14/38 (CFPAC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.041 | 14/38 (A-172, PANC-1, …) | all doses, flat |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.75×** | +3.3 | 0.044 | 11/37 (HT-29, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.050 | 18/38 (NCI-H2347, SW480, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.67×** | +3.0 | 0.089 | 11/38 (A-172, J82, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.467×** | -12.0 | 2e-30 | 31/38 (SW 900, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.386×** | -10.6 | 8e-24 | 32/36 (SHP-77, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.388×** | -10.6 | 9e-24 | 34/38 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.395×** | -10.3 | 6e-23 | 33/38 (SHP-77, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.406×** | -10.0 | 1e-21 | 35/38 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.424×** | -9.6 | 1e-19 | 33/38 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.460×** | -8.7 | 4e-16 | 27/38 (SHP-77, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.481×** | -8.2 | 3e-14 | 33/38 (BT-474, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.492×** | -7.9 | 2e-13 | 27/38 (SHP-77, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.517×** | -7.3 | 1e-11 | 31/38 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.533×** | -6.6 | 2e-09 | 30/38 (NCI-H2030, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.333×** | -6.4 | 7e-09 | 27/38 (NCI-H23, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.581×** | -6.0 | 7e-08 | 27/38 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.610×** | -5.5 | 2e-06 | 28/38 (SHP-77, BT-474, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -5.5 | 2e-06 | 23/36 (BT-474, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.711×** | -5.4 | 3e-06 | 22/38 (SHP-77, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.633×** | -5.1 | 1e-05 | 21/37 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.445×** | -4.7 | 7e-05 | 24/38 (PANC-1, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.578×** | -4.3 | 4e-04 | 22/38 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.732×** | -3.5 | 0.013 | 20/38 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.729×** | -3.4 | 0.017 | 18/38 (Hs 766T, SHP-77, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.739×** | -3.4 | 0.017 | 17/38 (SHP-77, COLO 205, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.729×** | -3.3 | 0.020 | 15/38 (PANC-1, A-427, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.62 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 182 | 17 | 20 (12 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 5.92× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -19.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.150× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 158 | 0 | 14 (8 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0481× (z -16.1) |
| [[PANC-1 (line)]] | alt | 127 | 1 | 11 (8 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.82× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -15.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -13.4) |
| [[BT-474 (line)]] | alt | 114 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0911× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -11.9) |
| [[SW 900 (line)]] | alt | 194 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -14.9) |
| [[COLO 205 (line)]] | alt | 87.6 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.308× (z -9.6) |
| [[A498 (line)]] | wt | 75.9 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.6) |
| [[J82 (line)]] | alt | 64.7 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -11.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.255× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 47.7 | 0 | 8 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.182× (z -12.7) |
| [[H4 (line)]] | wt | 60.9 | 2 | 4 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 4.39× (z +8.8) | [[Ixazomib citrate (drug)]] 5 µM 0.0843× (z -10.4) |
| [[HT-29 (line)]] | alt | 62.1 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.131× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -11.8) |
| [[Hs 766T (line)]] | wt | 111 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.6) |
| [[SNU-423 (line)]] | alt | 34.3 | 4 (1 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.72× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 38.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 67.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.3) |
| [[A549 (line)]] | wt | 29.0 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 7.39× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.1× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 43.9 | 1 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 4.72× (z +9.1) | [[Bortezomib (drug)]] 0.05 µM 0.178× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 72.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -9.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 41.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +10.1) | — |
| [[A-427 (line)]] | wt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.22× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 38.6 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.76× (z +8.9) | — |
| [[SW480 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.93 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.77 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.99 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00886]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SLC7A2]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[JADE1]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CEBPD]] | +0.58 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[KRT7]] | +0.57 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[TAPT1-AS1]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[HOPX]] | +0.56 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ZNF644]] | +0.54 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[CYP1B1-AS1]] | +0.54 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[LATS2]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[RDX]] | +0.53 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ROS1]] | +0.52 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | -0.58 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[AZIN2]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[NQO2]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NGLY1]] | -0.52 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.51 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[POM121]] | -0.51 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[FXYD5]] | -0.51 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[PI4KAP2]] | -0.50 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[MMP1]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[MGAT5]] | -0.50 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[ECI2]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[MYO9B]] | -0.49 | -0.58 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers DNAH5's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LRP1]] | C | LRP1 activity lowers DNAH5's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 4.73× higher at baseline in the lines without LRP1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH2]] | B | DNAH5 activity raises JPH2's level | lines that do not express DNAH5 (10) vs lines expressing it (40) | 3.42× lower at baseline in the lines without DNAH5 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent |
| [[FBXO4]] | B | DNAH5 activity strengthens FBXO4's drug response | lines that do not express DNAH5 (10) vs lines expressing it (38) | the lines without DNAH5 respond 0.84× as strongly (z diff +0.29); strongest at Digitoxin 5 µM: 0.99x vs 0.38x (z diff +3.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MYO9B]] | B | DNAH5 activity lowers MYO9B's level | lines that do not express DNAH5 (10) vs lines expressing it (40) | 1.06× higher at baseline in the lines without DNAH5 | 0.070 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent |
| [[FOSL2]] | B | DNAH5 activity raises FOSL2's level | lines that do not express DNAH5 (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without DNAH5 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent |
| [[POM121]] | B | DNAH5 activity lowers POM121's level | lines that do not express DNAH5 (10) vs lines expressing it (40) | 1.36× higher at baseline in the lines without DNAH5 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.320). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.1, 19.1); signed map (16.2, 25.4). **Vector** length 105, 29.2% of its response variance represented; |z| ≥ 3 in 1,550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.0 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.8 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -10.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.7 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -7.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:13,690,328-14,011,818 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Dnahc5, HL1, PCD, CILD3, KTGNR |
| Gene groups (HGNC) | Dyneins, axonemal outer arm complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE73](https://www.uniprot.org/uniprotkb/Q8TE73) (Dynein axonemal heavy chain 5):

> Force generating protein of respiratory cilia (By similarity). Produces force towards the minus ends of microtubules (By similarity). Key component of dynein, a family of motor proteins essential for movement along microtubules (By similarity). Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP (By similarity). Required for structural and functional integrity of the cilia of ependymal cells lining the brain ventricles (By similarity).

**Summary**, from NCBI Gene [1767](https://www.ncbi.nlm.nih.gov/gene/1767):

> This gene encodes a dynein protein, which is part of a microtubule-associated motor protein complex consisting of heavy, light, and intermediate chains. This protein is an axonemal heavy chain dynein. It functions as a force-generating protein with ATPase activity, whereby the release of ADP is thought to produce the force-producing power stroke. Mutations in this gene cause primary ciliary dyskinesia type 3, as well as Kartagener syndrome, which are both diseases due to ciliary defects. …

**Accessions** — [HGNC:2950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2950) · Entrez [1767](https://www.ncbi.nlm.nih.gov/gene/1767) · UniProt [Q8TE73](https://www.uniprot.org/uniprotkb/Q8TE73) · Ensembl [ENSG00000039139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000039139)

## Data

Gene col 460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 460); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 460]; `tensor/DDL_lfc|DDL_z.npy` [460]; `embed/gene_vectors.npy` [460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 460 or target_col == 460). Every well: [[DNAH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
