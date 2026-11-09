---
symbol: "URGCP"
type: "gene"
col: 2781
ensembl_id: "ENSG00000106608"
name: "upregulator of cell proliferation"
location: "7p13"
module: 11
arm: "+"
pooled_cpm: 48.54
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# URGCP

*upregulator of cell proliferation* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.15× (z +9.7, q 2e-19, up in 33 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.410× (z -23.5, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF282]] (+0.71, fdr 7e-06), [[COIL]] (+0.68, fdr 1e-05), [[YTHDF2]] (+0.68, fdr 7e-06); moves opposite to [[SAR1A]] (-0.60, fdr 1e-05), [[TPP2]] (-0.59, fdr 1e-05), [[P3H1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +9.7 | 2e-19 | 33/49 (SW480, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +7.4 | 3e-11 | 32/48 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +5.7 | 3e-06 | 22/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +5.0 | 6e-05 | 17/48 (A498, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +4.8 | 2e-04 | 17/48 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.059 | 17/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.10× | +3.4 | 0.059 | 13/48 (AsPC-1, HT-29, …) | top dose only | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.3 | 0.067 | 4/48 (A498, H4, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.09× | +3.3 | 0.067 | 2/48 (CFPAC-1, H4) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.094 | 4/48 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.094 | 8/48 (PANC-1, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2781.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.410×** | -23.5 | 0e+00 | 46/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.413×** | -23.3 | 0e+00 | 40/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.421×** | -22.8 | 0e+00 | 48/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.461×** | -20.4 | 0e+00 | 44/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.483×** | -18.4 | 0e+00 | 34/39 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.535×** | -15.3 | 0e+00 | 34/43 (RPMI-7951, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -12.9 | 5e-36 | 33/48 (AsPC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -12.3 | 9e-33 | 38/48 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.650×** | -10.9 | 6e-26 | 32/48 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.664×** | -10.4 | 2e-23 | 31/49 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.732×** | -8.2 | 1e-14 | 30/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.753×** | -7.5 | 4e-12 | 29/48 (SW480, A498, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -6.0 | 9e-08 | 2/49 (COLO 205, SW 1271) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.797×** | -5.8 | 4e-07 | 22/47 (C-33 A, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -5.2 | 9e-06 | 20/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.722×** | -4.1 | 0.001 | 17/48 (NCI-H2030, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.882× | -3.3 | 0.031 | 12/48 (NCI-H661, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 72.0 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.277× (z -14.9) |
| [[SW480 (line)]] | alt | 63.5 | 1 | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.41× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.285× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 75.7 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 45.5 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.347× (z -12.7) |
| [[SW1417 (line)]] | alt | 62.2 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -21.7) |
| [[SW48 (line)]] | wt | 88.8 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.18× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.232× (z -13.2) |
| [[A498 (line)]] | wt | 71.8 | 4 (4 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.467× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 84.2 | 1 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -17.2) |
| [[A-172 (line)]] | wt | 52.9 | 0 | 6 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -15.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.507× (z -10.2) |
| [[HOP62 (line)]] | alt | 37.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 66.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.378× (z -11.1) |
| [[PANC-1 (line)]] | alt | 53.0 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.3) |
| [[HS-578T (line)]] | alt | 48.5 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 38.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 43.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.258× (z -13.2) |
| [[AN3 CA (line)]] | alt | 62.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0842× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.225× (z -8.6) |
| [[C-33 A (line)]] | alt | 51.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.211× (z -11.8) |
| [[KATO III (line)]] | alt | 59.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -16.0) |
| [[RKO (line)]] | wt | 43.0 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.285× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 44.9 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.366× (z -9.6) |
| [[SNU-423 (line)]] | alt | 41.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.302× (z -11.5) |
| [[J82 (line)]] | alt | 36.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -10.1) |
| [[LoVo (line)]] | wt | 59.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -16.0) |
| [[LS 180 (line)]] | wt | 37.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.359× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 55.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0607× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 42.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +9.8) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[HT-29 (line)]] | alt | 32.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.330× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 39.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.264× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 42.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 48.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 33.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -9.4) |
| [[BT-474 (line)]] | alt | 56.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.3) |
| [[C32 (line)]] | wt | 39.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.350× (z -8.8) |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -9.5) |
| [[H4 (line)]] | wt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0835× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 34.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -9.9) |
| [[NCI-H661 (line)]] | alt | 35.8 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0741× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF282]] | +0.71 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[COIL]] | +0.68 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[YTHDF2]] | +0.68 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.65 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ZNF302]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RPP38]] | +0.64 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[ZNF594]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PHAX]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[RNF115]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[KLHL42]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TMEM70]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[RDH14]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAR1A]] | -0.60 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TPP2]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[P3H1]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[RECQL]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FAM91A1]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[APLP2]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ODF2]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[LMAN1]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MLF2]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SEPTIN2]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MAGT1]] | -0.52 | -0.39 / -0.48 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises URGCP's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[P3H1]] | C | P3H1 activity raises URGCP's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.36× lower at baseline in the lines without P3H1 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.8, 8.5); signed map (0.8, -19.4). **Vector** length 102, 25.3% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.8 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +6.3 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.6 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -12.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.6 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -3.2 | -23.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -22.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -23.5 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[Pimozide (drug)]] 5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | upregulator of cell proliferation |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:43,875,894-43,926,411 (-) |
| Ensembl biotype | protein_coding |
| Also known as | URG4, KIAA1507, FLJ20654, DKFZp666G166, DKFZp686O0457 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCY9](https://www.uniprot.org/uniprotkb/Q8TCY9) (Up-regulator of cell proliferation):

> May be involved in cell cycle progression through the regulation of cyclin D1 expression. May participate in the development of hepatocellular carcinoma (HCC) by promoting hepatocellular growth and survival. May play an important role in development of gastric cancer.

**Summary**, from NCBI Gene [55665](https://www.ncbi.nlm.nih.gov/gene/55665):

> URG4 is upregulated in the presence of hepatitis B virus (HBV)-encoded X antigen (HBxAg) and may contribute to the development of hepatocellular carcinoma by promoting hepatocellular growth and survival (Tufan et al., 2002 [PubMed 12082552]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30890) · Entrez [55665](https://www.ncbi.nlm.nih.gov/gene/55665) · UniProt [Q8TCY9](https://www.uniprot.org/uniprotkb/Q8TCY9) · Ensembl [ENSG00000106608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106608)

## Data

Gene col 2781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2781); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2781]; `tensor/DDL_lfc|DDL_z.npy` [2781]; `embed/gene_vectors.npy` [2781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2781 or target_col == 2781). Every well: [[URGCP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/URGCP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
