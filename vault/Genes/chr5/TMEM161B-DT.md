---
symbol: "TMEM161B-DT"
type: "gene"
col: 14507
ensembl_id: "ENSG00000247828"
name: "TMEM161B divergent transcript"
location: "5q14.3"
module: 37
arm: "+"
pooled_cpm: 101.97
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TMEM161B-DT

*TMEM161B divergent transcript* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.93× (z +6.6, q 2e-08, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.493× (z -13.5, q 5e-39, down in 36 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.625× (z -9.0, q 3e-17, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLEC4A]] (+0.67, fdr 7e-06), [[ADAM20]] (+0.63, fdr 1e-05), [[LINC00640]] (+0.62, fdr 1e-05); moves opposite to [[DBNL]] (-0.54, fdr 1e-05), [[WDR1]] (-0.54, fdr 1e-05), [[MACF1]] (-0.50, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.93×** | +6.6 | 2e-08 | 39/49 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +4.4 | 0.002 | 21/48 (AsPC-1, LS 180, …) | rises with dose | low cells (technical?) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.54×** | +4.4 | 0.002 | 27/49 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.1 | 0.005 | 18/48 (LS 180, A498, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.018 | 21/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.11 | 19/48 (KATO III, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.15 | 20/47 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.15 | 16/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.17× | +3.0 | 0.15 | 22/49 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.0 | 0.15 | 19/48 (AsPC-1, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 26 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.493×** | -13.5 | 5e-39 | 36/49 (COLO 205, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.502×** | -12.2 | 8e-32 | 37/45 (C-33 A, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.547×** | -11.1 | 2e-26 | 34/44 (NCI-H23, NCI-H460, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.563×** | -10.6 | 5e-24 | 37/48 (A498, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.625×** | -9.0 | 3e-17 | 39/48 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.629×** | -8.9 | 8e-17 | 41/48 (HOP62, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.730×** | -8.5 | 1e-15 | 31/48 (A498, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.636×** | -8.3 | 6e-15 | 36/47 (C32, RPMI-7951, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -7.7 | 1e-12 | 37/48 (C32, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.681×** | -7.3 | 1e-11 | 38/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -7.2 | 4e-11 | 40/49 (COLO 205, C32, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.717×** | -6.4 | 1e-08 | 31/48 (A498, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.718×** | -6.3 | 1e-08 | 35/48 (SW 900, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.724×** | -6.2 | 3e-08 | 30/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.712×** | -6.1 | 4e-08 | 33/48 (COLO 205, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.761×** | -5.0 | 2e-05 | 29/47 (CFPAC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.800×** | -4.2 | 6e-04 | 25/47 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.738×** | -4.1 | 1e-03 | 23/48 (COLO 205, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.813×** | -3.8 | 0.003 | 21/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.696×** | -3.6 | 0.006 | 19/46 (CHP-212, SHP-77, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.881× | -3.4 | 0.014 | 17/49 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.839× | -3.3 | 0.017 | 18/48 (COLO 205, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.841× | -3.3 | 0.018 | 17/48 (CHP-212, A-427, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.857× | -2.9 | 0.052 | 16/48 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.861× | -2.8 | 0.067 | 18/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 121 | 0 | 10 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A498 (line)]] | wt | 136 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -23.2) ⚠ cell-cycle shift, explains ~79% of this change |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -14.8) ⚠ cell-cycle shift, explains ~79% of this change |
| [[C32 (line)]] | wt | 156 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.305× (z -12.0) |
| [[PANC-1 (line)]] | alt | 83.7 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -13.7) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.497× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 124 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.1) ⚠ cell-cycle shift, explains ~79% of this change | [[Dinaciclib (drug)]] 5 µM 0.128× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HOP62 (line)]] | alt | 138 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.451× (z -8.8) |
| [[LS 180 (line)]] | wt | 139 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.452× (z -8.6) |
| [[RKO (line)]] | wt | 131 | 0 | 5 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0468× (z -30.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 97.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 221 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 125 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 44.7 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.245× (z -11.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[C-33 A (line)]] | alt | 168 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 372 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HepG2_C3A (line)]] | wt | 80.7 | 0 | 3 (2 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.275× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 83.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 145 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 66.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.5) ⚠ cell-cycle shift, explains ~79% of this change |
| [[CHP-212 (line)]] | wt | 124 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0801× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[vincristine (drug)]] 5 µM 0.0717× (z -9.0) |
| [[H4 (line)]] | wt | 74.9 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.221× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 68.3 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.171× (z -10.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 90.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.1) ⚠ cell-cycle shift, explains ~79% of this change |
| [[NCI-H1792 (line)]] | alt | 75.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 64.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.83× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.313× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SHP-77 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 93.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.3) ⚠ cell-cycle shift, explains ~79% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.9) ⚠ cell-cycle shift, explains ~79% of this change |
| [[HCT15 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW 1271 (line)]] | alt | 198 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW48 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 98.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC4A]] | +0.67 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ADAM20]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[LINC00640]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TMEM14B]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[BNIPL]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZNF248]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ADAM20P1]] | +0.58 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[TSNAX-DISC1]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[BET1]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[DCAF10]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[HYPK]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SLC30A5]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBNL]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[WDR1]] | -0.54 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[MACF1]] | -0.50 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[HIGD1A]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PSMD2]] | -0.48 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[EXT2]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, -21.0); signed map (7.6, 5.0). **Vector** length 101, 29.8% of its response variance represented; |z| ≥ 3 in 1,347 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +6.6 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +3.1 | -5.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +6.6 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.7 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -7.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.0 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | TMEM161B divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.3 — chr5:88,268,864-88,439,337 (+) |
| Ensembl biotype | lncRNA |
| Also known as | uc.165, linc-POLR3G-8; previously TMEM161B-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100505894](https://www.ncbi.nlm.nih.gov/gene/100505894):

> Predicted to be a structural constituent of ribosome. Predicted to be located in ribosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:43839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43839) · Entrez [100505894](https://www.ncbi.nlm.nih.gov/gene/100505894) · Ensembl [ENSG00000247828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247828)

## Data

Gene col 14507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14507); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14507]; `tensor/DDL_lfc|DDL_z.npy` [14507]; `embed/gene_vectors.npy` [14507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14507 or target_col == 14507). Every well: [[TMEM161B-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM161B-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
