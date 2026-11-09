---
symbol: "RUFY3"
type: "gene"
col: 304
ensembl_id: "ENSG00000018189"
name: "RUN and FYVE domain containing 3"
location: "4q13.3"
module: 124
arm: "+"
pooled_cpm: 74.79
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# RUFY3

*RUN and FYVE domain containing 3* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.37× (z +7.3, q 2e-10, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.399× (z -21.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUTM2A-AS1]] (+0.63, fdr 1e-05), [[NUTM2B-AS1]] (+0.62, fdr 1e-05), [[FBXO30]] (+0.61, fdr 3e-05); moves opposite to [[TLE6]] (-0.58, fdr 2e-05), [[RAB3A]] (-0.57, fdr 1e-04), [[STN1]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BEND7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +7.3 | 2e-10 | 29/48 (C32, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +7.2 | 2e-10 | 31/48 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.37×** | +6.9 | 1e-09 | 26/48 (C32, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +6.3 | 3e-08 | 29/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +5.6 | 3e-06 | 25/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +4.9 | 9e-05 | 13/48 (C32, PANC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.9 | 9e-05 | 23/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.24×** | +4.8 | 1e-04 | 24/47 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.6 | 2e-04 | 17/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +4.5 | 4e-04 | 21/50 (C32, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.4 | 6e-04 | 20/47 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +4.3 | 9e-04 | 21/48 (SW480, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.004 | 19/47 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.004 | 21/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.009 | 21/48 (A549, A498, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.018 | 14/48 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.11× | +3.5 | 0.018 | 8/49 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.4 | 0.020 | 12/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.020 | 17/48 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.031 | 10/48 (A498, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.399×** | -21.2 | 0e+00 | 47/48 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.413×** | -20.4 | 0e+00 | 44/48 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.557×** | -13.5 | 3e-39 | 43/48 (HT-29, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.432×** | -10.1 | 6e-22 | 37/49 (NCI-H1792, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.810×** | -4.7 | 3e-04 | 23/48 (RKO, J82, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -4.6 | 3e-04 | 25/48 (BT-474, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.817×** | -4.6 | 3e-04 | 24/48 (A-427, C-33 A, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.835× | -4.1 | 0.003 | 22/48 (Panc 03.27, HT-29, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.831×** | -4.1 | 0.003 | 21/50 (hTERT-HPNE, RPMI-7951, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.015 | 20/48 (SW 900, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~81% of this change | 0.860× | -3.5 | 0.028 | 17/47 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.901× | -3.4 | 0.036 | 12/48 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.855× | -3.3 | 0.037 | 21/44 (C-33 A, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -3.3 | 0.037 | 17/48 (CHP-212, H4, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.763×** | -3.3 | 0.041 | 14/36 (AsPC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.041 | 17/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.769×** | -3.2 | 0.054 | 9/48 (COLO 205, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.9 | 4 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.29× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.373× (z -13.4) |
| [[A549 (line)]] | wt | 67.2 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -16.2) |
| [[BT-474 (line)]] | alt | 85.4 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -13.7) |
| [[HT-29 (line)]] | alt | 123 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -20.7) |
| [[PANC-1 (line)]] | alt | 89.4 | 1 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.76× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -11.6) |
| [[A-172 (line)]] | wt | 113 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -12.9) |
| [[A-427 (line)]] | wt | 113 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.472× (z -9.5) |
| [[A498 (line)]] | wt | 103 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -16.4) |
| [[SK-MEL-2 (line)]] | alt | 164 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.376× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 40.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Lonafarnib (drug)]] 5 µM 0.0969× (z -10.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.351× (z -9.2) |
| [[C32 (line)]] | wt | 74.5 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.84× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 51.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.81× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 56.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -13.6) |
| [[J82 (line)]] | alt | 42.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -10.5) |
| [[LoVo (line)]] | wt | 55.0 | 1 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.06× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -17.1) |
| [[LS 180 (line)]] | wt | 58.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 61.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -17.7) |
| [[RKO (line)]] | wt | 64.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 204 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -14.2) |
| [[SNU-423 (line)]] | alt | 56.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -11.8) |
| [[AN3 CA (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 151 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 50.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 73.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.485× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 73.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 56.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.458× (z -10.2) |
| [[SW1417 (line)]] | alt | 44.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -10.9) |
| [[H4 (line)]] | wt | 164 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 108 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -10.6) |
| [[Hs 766T (line)]] | wt | 39.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 42.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 61.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.124× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 59.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -8.7) |
| [[SW 1088 (line)]] | alt | 127 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0960× (z -9.2) |
| [[SW 900 (line)]] | alt | 61.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -9.2) |
| [[SW48 (line)]] | wt | 51.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTM2A-AS1]] | +0.63 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[FBXO30]] | +0.61 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[MAFG]] | +0.60 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[CLIP1]] | +0.60 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[POU6F1]] | +0.58 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[HTATIP2]] | +0.57 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[RHBDD3]] | +0.57 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[FTX]] | +0.57 | +0.60 / +0.35 | both halves | 1e-04 |  |
| [[MARK1]] | +0.56 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[PLEKHA5]] | +0.55 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[DENND5B]] | +0.54 | +0.58 / +0.37 | both halves | 8e-05 | same gene group |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLE6]] | -0.58 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[RAB3A]] | -0.57 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[STN1]] | -0.57 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[WRAP53]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[RIN1]] | -0.52 | -0.53 / -0.32 | both halves | 1e-04 |  |
| [[PTGS1]] | -0.52 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ST3GAL5]] | -0.52 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[SLC2A3]] | -0.51 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[FSCN1]] | -0.51 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[C8orf58]] | -0.50 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[LTN1]] | -0.50 | -0.51 / -0.24 | both halves | 4e-04 |  |
| [[INTS13]] | -0.49 | -0.40 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEND7]] | B | BEND7 activity lowers RUFY3's level | lines that do not express BEND7 (12) vs lines expressing it (38) | 1.59× higher at baseline in the lines without BEND7 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZIC2 |
| [[RCN3]] | B | RCN3 activity raises RUFY3's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without RCN3 | 0.059 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FSCN1]] | C | FSCN1 activity lowers RUFY3's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 1.09× higher at baseline in the lines without FSCN1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-15.1, 12.3); signed map (10.7, -6.7). **Vector** length 117, 31.3% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.6 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.5 | +7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +8.0 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.5 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.7 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +3.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.7 | -21.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -20.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.3 | -13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | RUN and FYVE domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:70,704,204-70,808,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIPx, KIAA0871, Singar1, ZFYVE30 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; RUN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L099](https://www.uniprot.org/uniprotkb/Q7L099) (Protein RUFY3):

> ARL8 effector that promotes the coupling of endolysosomes to dynein-dynactin for retrograde transport along microtubules. Acts by binding both GTP-bound ARL8 and dynein-dynactin. In nonneuronal cells, promotes concentration of endolysosomes in the juxtanuclear area. In hippocampal neurons, drives retrograde transport of endolysosomes from the axon to the soma. Plays a role in the generation of neuronal polarity formation and axon growth (By similarity). Implicated in the formation of a single …

**Summary**, from NCBI Gene [22902](https://www.ncbi.nlm.nih.gov/gene/22902):

> This gene encodes a RPIP8, UNC-14, and NESCA domain-containing protein that is required for maintenance of neuronal polarity. In addition, it has been implicated in mediation of gastric cancer cell migration and invasion via interaction with P21-activated kinase-1, which promotes its expression. The encoded protein localizes to F-actin-enriched invadopodia to induce formation of protrusions, thereby facilitating cell migration. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:30285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30285) · Entrez [22902](https://www.ncbi.nlm.nih.gov/gene/22902) · UniProt [Q7L099](https://www.uniprot.org/uniprotkb/Q7L099) · Ensembl [ENSG00000018189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000018189)

## Data

Gene col 304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 304); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 304]; `tensor/DDL_lfc|DDL_z.npy` [304]; `embed/gene_vectors.npy` [304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 304 or target_col == 304). Every well: [[RUFY3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUFY3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
