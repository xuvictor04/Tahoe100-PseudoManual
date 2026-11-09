---
symbol: "KDM6B"
type: "gene"
col: 5332
ensembl_id: "ENSG00000132510"
name: "lysine demethylase 6B"
location: "17p13.1"
module: 173
arm: "+"
pooled_cpm: 67.12
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# KDM6B

*lysine demethylase 6B* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.2× (z +43.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.527× (z -8.4, q 3e-14, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERF]] (+0.69, fdr 9e-06), [[NANOS3]] (+0.69, fdr 1e-05), [[MMRN2]] (+0.68, fdr 7e-06); moves opposite to [[VDAC3]] (-0.67, fdr 1e-05), [[MED23]] (-0.65, fdr 1e-05), [[L2HGDH]] (-0.65, fdr 1e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ELFN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.2×** | +43.3 | 0e+00 | 48/48 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **8.96×** | +27.5 | 0e+00 | 46/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.17×** | +21.4 | 0e+00 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.00×** | +14.3 | 4e-44 | 46/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +12.7 | 5e-35 | 45/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.11×** | +9.7 | 3e-20 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.02×** | +9.2 | 4e-18 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +8.8 | 1e-16 | 33/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.49×** | +8.5 | 1e-15 | 43/49 (NCI-H460, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +7.9 | 1e-13 | 38/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +7.7 | 1e-12 | 38/47 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.007 | 23/49 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +3.8 | 0.007 | 25/48 (SW48, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.009 | 24/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.70×** | +3.6 | 0.012 | 26/48 (SHP-77, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.013 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Resveratrol (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.036 | 25/49 (SNU-423, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.527×** | -8.4 | 3e-14 | 44/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.532×** | -8.2 | 5e-14 | 41/48 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.589×** | -6.9 | 8e-10 | 42/48 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.715×** | -4.4 | 0.002 | 30/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.726×** | -4.2 | 0.003 | 31/47 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -4.2 | 0.003 | 4/50 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.580×** | -3.7 | 0.016 | 24/47 (SNU-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.019 | 28/48 (RKO, LOX-IMVI, …) | top dose only | position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.759×** | -3.6 | 0.019 | 27/48 (SNU-423, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.597×** | -3.5 | 0.024 | 22/49 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.024 | 24/47 (C-33 A, SW480, …) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.032 | 23/48 (SNU-423, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -3.2 | 0.070 | 21/48 (SW48, LOX-IMVI, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.833×** | -3.1 | 0.079 | 17/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.793×** | -3.1 | 0.079 | 18/48 (AsPC-1, LS 180, …) | top dose only | position effect removed |
| [[Voriconazole (drug)]] 5 µM |  | **0.793×** | -3.0 | 0.079 | 20/48 (HCT15, J82, …) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.768×** | -3.0 | 0.099 | 19/47 (RKO, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.1 | 14 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +34.0) | — |
| [[SW 900 (line)]] | alt | 91.5 | 10 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +29.5) | [[Panobinostat (drug)]] 5 µM 0.348× (z -9.0) |
| [[SNU-1 (line)]] | wt | 75.2 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +22.5) | — |
| [[SW480 (line)]] | alt | 69.6 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +18.4) | — |
| [[HS-578T (line)]] | alt | 66.4 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +32.8) | — |
| [[AsPC-1 (line)]] | alt | 49.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +33.5) | — |
| [[HOP62 (line)]] | alt | 83.2 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +34.0) | [[Panobinostat (drug)]] 5 µM 0.341× (z -9.6) |
| [[SW48 (line)]] | wt | 146 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +14.5) | — |
| [[A-172 (line)]] | wt | 76.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +29.8) | — |
| [[A549 (line)]] | wt | 98.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +34.4) | — |
| [[HEC-1-A (line)]] | alt | 45.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +25.9) | — |
| [[HepG2_C3A (line)]] | wt | 95.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +26.0) | — |
| [[hTERT-HPNE (line)]] | wt | 80.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +25.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 66.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +27.8) | — |
| [[NCI-H1573 (line)]] | alt | 109 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +33.8) | — |
| [[NCI-H23 (line)]] | alt | 131 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +19.2) | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -12.2) |
| [[BT-474 (line)]] | alt | 88.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +19.6) | — |
| [[LoVo (line)]] | wt | 55.1 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.93× (z +27.7) | — |
| [[NCI-H2347 (line)]] | alt | 30.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +21.6) | — |
| [[A498 (line)]] | wt | 78.5 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +33.9) | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 94.9 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +19.1) | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -10.1) |
| [[LS 180 (line)]] | wt | 45.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +19.3) | — |
| [[Panc 03.27 (line)]] | alt | 38.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +27.2) | — |
| [[RPMI-7951 (line)]] | alt | 79.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +27.7) | — |
| [[C32 (line)]] | wt | 69.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +25.3) | — |
| [[CFPAC-1 (line)]] | alt | 51.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +33.6) | — |
| [[J82 (line)]] | alt | 66.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +30.7) | — |
| [[KATO III (line)]] | alt | 47.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +27.2) | — |
| [[PANC-1 (line)]] | alt | 46.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +33.3) | — |
| [[SNU-423 (line)]] | alt | 75.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.5× (z +37.2) | — |
| [[SW1417 (line)]] | alt | 44.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +18.0) | — |
| [[A-427 (line)]] | wt | 65.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.6) | — |
| [[AN3 CA (line)]] | alt | 83.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 45.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +22.7) | — |
| [[H4 (line)]] | wt | 56.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +18.9) | — |
| [[Hs 766T (line)]] | wt | 50.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +27.5) | — |
| [[HT-29 (line)]] | alt | 63.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.264× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 39.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +23.8) | — |
| [[NCI-H2030 (line)]] | alt | 46.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +23.7) | — |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +23.6) | — |
| [[HCT15 (line)]] | alt | 65.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.1) | — |
| [[RKO (line)]] | wt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 64.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.3) | — |
| [[SW 1088 (line)]] | alt | 54.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +9.9) | — |
| [[SW 1271 (line)]] | alt | 94.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +13.0) | — |
| [[C-33 A (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | +0.69 | +0.69 / +0.57 | both halves | 9e-06 | pathway: Cellular Senescence |
| [[NANOS3]] | +0.69 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MMRN2]] | +0.68 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[FBRS]] | +0.68 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PCF11]] | +0.68 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[AKT1S1]] | +0.67 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[RGL2]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MEPCE]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SRRM2]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[HIVEP2]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.64 | +0.58 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VDAC3]] | -0.67 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[MED23]] | -0.65 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[L2HGDH]] | -0.65 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SNX4]] | -0.64 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[HACE1]] | -0.63 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[SLC35A3]] | -0.63 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[GRB2]] | -0.63 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ATP5F1C]] | -0.63 | -0.57 / -0.50 | both halves | 1e-05 | STRING 901 |
| [[REPS1]] | -0.62 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SKP2]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[JKAMP]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.62 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN1]] | B | ELFN1 activity raises KDM6B's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.30× lower at baseline in the lines without ELFN1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.4, 9.5); signed map (14.9, -8.7). **Vector** length 119, 39.5% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +43.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +27.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +21.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | -0.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.3 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.4 |
|  | [[NG25 (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -1.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,834,217-7,854,796 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0346; previously JMJD3 |
| Gene groups (HGNC) | Lysine demethylase 6 family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 9 pathways, smallest: Chromatin modifications during the maternal to zygotic transition (MZT); HDMs demethylate histones; Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [O15054](https://www.uniprot.org/uniprotkb/O15054) (Lysine-specific demethylase 6B):

> Histone demethylase that specifically demethylates 'Lys-27' of histone H3, thereby playing a central role in histone code. Demethylates trimethylated and dimethylated H3 'Lys-27'. Plays a central role in regulation of posterior development, by regulating HOX gene expression. Involved in inflammatory response by participating in macrophage differentiation in case of inflammation by regulating gene expression and macrophage differentiation. Plays a demethylase-independent role in chromatin …

**Summary**, from NCBI Gene [23135](https://www.ncbi.nlm.nih.gov/gene/23135):

> The protein encoded by this gene is a lysine-specific demethylase that specifically demethylates di- or tri-methylated lysine 27 of histone H3 (H3K27me2 or H3K27me3). H3K27 trimethylation is a repressive epigenetic mark controlling chromatin organization and gene silencing. This protein can also demethylate non-histone proteins such as retinoblastoma protein. Through its demethylation actvity this gene influences cellular differentiation and development, tumorigenesis, inflammatory diseases, …

**Accessions** — [HGNC:29012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29012) · Entrez [23135](https://www.ncbi.nlm.nih.gov/gene/23135) · UniProt [O15054](https://www.uniprot.org/uniprotkb/O15054) · Ensembl [ENSG00000132510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132510)

## Data

Gene col 5332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5332); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5332]; `tensor/DDL_lfc|DDL_z.npy` [5332]; `embed/gene_vectors.npy` [5332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5332 or target_col == 5332). Every well: [[KDM6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
