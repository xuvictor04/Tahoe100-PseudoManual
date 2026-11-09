---
symbol: "CCM2"
type: "gene"
col: 5852
ensembl_id: "ENSG00000136280"
name: "CCM2 scaffold protein"
location: "7p13"
module: 2
arm: "+"
pooled_cpm: 47.39
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CCM2

*CCM2 scaffold protein* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.51× (z +6.6, q 2e-08, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.405× (z -21.3, q 0e+00, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.384× (z -15.4, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBED4]] (+0.67, fdr 7e-06), [[MYO9B]] (+0.63, fdr 1e-05), [[DIP2A]] (+0.62, fdr 1e-05); moves opposite to [[MINDY1]] (-0.62, fdr 1e-05), [[BDH2]] (-0.60, fdr 1e-05), [[DLEU1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02967]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.51×** | +6.6 | 2e-08 | 28/46 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.6 | 5e-06 | 1/47 (NCI-H2347) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 4e-04 | 23/46 (hTERT-HPNE, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.005 | 22/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.009 | 22/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 1.21× | +3.2 | 0.11 | 18/47 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.405×** | -21.3 | 0e+00 | 42/47 (A-172, A-427, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.384×** | -15.4 | 0e+00 | 40/47 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.529×** | -10.6 | 5e-24 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -10.2 | 2e-22 | 28/38 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.369×** | -8.7 | 4e-16 | 37/48 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.587×** | -8.6 | 1e-15 | 32/46 (H4, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -8.1 | 4e-14 | 31/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.618×** | -8.0 | 7e-14 | 34/47 (A-172, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.620×** | -8.0 | 1e-13 | 32/47 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.622×** | -7.9 | 1e-13 | 27/44 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -7.1 | 6e-11 | 25/42 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.653×** | -5.7 | 6e-07 | 27/47 (PANC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.791×** | -5.5 | 1e-06 | 26/47 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -5.5 | 1e-06 | 28/47 (HOP62, BT-474, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.542×** | -5.3 | 4e-06 | 28/46 (SW48, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.780×** | -4.1 | 0.001 | 21/47 (Hs 766T, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.789×** | -3.7 | 0.006 | 21/47 (AsPC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.015 | 14/47 (A-172, PANC-1, …) | top dose only | plate-row cell shift |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.031 | 12/47 (C-33 A, HS-578T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.1 | 0.046 | 20/47 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.835× | -3.0 | 0.060 | 13/47 (BT-474, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 125 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -38.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.144× (z -17.7) |
| [[HOP62 (line)]] | alt | 70.2 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -22.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.256× (z -11.2) |
| [[BT-474 (line)]] | alt | 66.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -12.3) |
| [[H4 (line)]] | wt | 95.2 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -13.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.219× (z -10.0) |
| [[J82 (line)]] | alt | 51.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -21.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 40.0 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.305× (z -8.7) |
| [[HS-578T (line)]] | alt | 71.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -21.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.231× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 62.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.346× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 45.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.352× (z -9.2) |
| [[PANC-1 (line)]] | alt | 71.3 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -17.0) |
| [[A-427 (line)]] | wt | 40.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -22.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.220× (z -14.0) |
| [[A549 (line)]] | wt | 45.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.264× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 57.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.380× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 50.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -15.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -8.6) |
| [[SW480 (line)]] | alt | 41.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -12.5) |
| [[A498 (line)]] | wt | 79.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -21.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 73.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -20.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.163× (z -13.4) |
| [[KATO III (line)]] | alt | 38.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 59.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.388× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 66.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.260× (z -9.0) |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.256× (z -10.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 48.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.274× (z -10.0) |
| [[SW1417 (line)]] | alt | 32.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -9.7) |
| [[AN3 CA (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0998× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -9.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 1 | — | [[ETC-206 (drug)]] 0.05 µM 0.0527× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0980× (z -11.2) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 49.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -16.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 43.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.241× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -16.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED4]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[DIP2A]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TUBB6]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[FBH1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[AXIN1]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[KLC1]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PACS2]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[VKORC1L1]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[BMP2K]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY1]] | -0.62 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[BDH2]] | -0.60 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[DLEU1]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[HINT3]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[CLCN3]] | -0.55 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[DNAH7]] | -0.55 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZNF711]] | -0.53 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[INPP4B]] | -0.53 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[LNX1]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[BTN3A1]] | -0.53 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02967]] | B | LINC02967 activity lowers CCM2's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 1.57× higher at baseline in the lines without LINC02967 | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.444). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-13.2, 0.4); signed map (-45.3, -1.5). **Vector** length 113, 33.1% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.6 | +6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +1.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.7 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +0.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.4 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.6 | -21.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.1 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -2.3 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | CCM2 scaffold protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,999,475-45,076,469 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4607, OSM; previously C7orf22 |
| Gene groups (HGNC) | CCM adhesion complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSQ5](https://www.uniprot.org/uniprotkb/Q9BSQ5) (Cerebral cavernous malformations 2 protein):

> Component of the CCM signaling pathway which is a crucial regulator of heart and vessel formation and integrity. May act through the stabilization of endothelial cell junctions (By similarity). May function as a scaffold protein for MAP2K3-MAP3K3 signaling. Seems to play a major role in the modulation of MAP3K3-dependent p38 activation induced by hyperosmotic shock (By similarity).

**Summary**, from NCBI Gene [83605](https://www.ncbi.nlm.nih.gov/gene/83605):

> This gene encodes a scaffold protein that functions in the stress-activated p38 Mitogen-activated protein kinase (MAPK) signaling cascade. The protein interacts with SMAD specific E3 ubiquitin protein ligase 1 (also known as SMURF1) via a phosphotyrosine binding domain to promote RhoA degradation. The protein is required for normal cytoskeletal structure, cell-cell interactions, and lumen formation in endothelial cells. Mutations in this gene result in cerebral cavernous malformations. Multiple …

**Accessions** — [HGNC:21708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21708) · Entrez [83605](https://www.ncbi.nlm.nih.gov/gene/83605) · UniProt [Q9BSQ5](https://www.uniprot.org/uniprotkb/Q9BSQ5) · Ensembl [ENSG00000136280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136280)

## Data

Gene col 5852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5852); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5852]; `tensor/DDL_lfc|DDL_z.npy` [5852]; `embed/gene_vectors.npy` [5852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5852 or target_col == 5852). Every well: [[CCM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
