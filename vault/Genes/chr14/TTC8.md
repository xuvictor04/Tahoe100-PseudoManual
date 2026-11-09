---
symbol: "TTC8"
type: "gene"
col: 9142
ensembl_id: "ENSG00000165533"
name: "tetratricopeptide repeat domain 8"
location: "14q31.3"
module: 28
arm: "+"
pooled_cpm: 24.39
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 25
n_dd_up_clean: 10
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TTC8

*tetratricopeptide repeat domain 8* — 14q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.66× (z +10.1, q 3e-21, up in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +7.0, q 5e-10, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.518× (z -9.2, q 2e-17, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.322× (z -8.3, q 2e-14, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC11]] (+0.69, fdr 7e-06), [[MKS1]] (+0.65, fdr 7e-06), [[TATDN3]] (+0.62, fdr 1e-05); moves opposite to [[SNTB2]] (-0.57, fdr 1e-05), [[DIAPH1]] (-0.54, fdr 1e-05), [[CYTH1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC00888]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.66×** | +10.1 | 3e-21 | 39/47 (RKO, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +7.0 | 5e-10 | 25/46 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +5.0 | 8e-05 | 28/47 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.43×** | +5.0 | 8e-05 | 25/47 (RKO, J82, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.005 | 17/47 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.005 | 20/46 (RKO, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.015 | 13/47 (NCI-H2347, COLO 205, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.033 | 12/47 (BT-474, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.037 | 15/47 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.041 | 15/47 (BT-474, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.041 | 17/47 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.1 | 0.086 | 5/47 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.088 | 18/47 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.0 | 0.11 | 13/47 (RPMI-7951, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.518×** | -9.2 | 2e-17 | 34/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.534×** | -8.8 | 5e-16 | 36/46 (PANC-1, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.322×** | -8.3 | 2e-14 | 36/47 (SW 900, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.561×** | -8.1 | 1e-13 | 28/42 (SK-MEL-2, HCT15, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.566×** | -7.9 | 2e-13 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -7.8 | 5e-13 | 31/47 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.579×** | -7.6 | 2e-12 | 30/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.582×** | -7.3 | 2e-11 | 30/45 (NCI-H460, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.571×** | -7.2 | 3e-11 | 26/37 (SK-MEL-2, RPMI-7951, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.599×** | -6.9 | 4e-10 | 24/33 (Panc 03.27, SHP-77, …) | all doses, flat | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.719×** | -4.6 | 2e-04 | 23/46 (NCI-H2030, NCI-H23, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -4.5 | 3e-04 | 24/45 (HS-578T, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.722×** | -4.4 | 5e-04 | 23/46 (SW48, NCI-H23, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.568×** | -4.1 | 0.001 | 18/45 (HCT15, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -3.9 | 0.004 | 20/47 (SW480, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.762×** | -3.8 | 0.005 | 19/47 (HCT15, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.828×** | -3.7 | 0.007 | 19/47 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.772×** | -3.6 | 0.009 | 15/46 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -3.6 | 0.009 | 19/47 (SW48, KATO III, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.701×** | -3.5 | 0.010 | 18/46 (RPMI-7951, SNU-423, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.770×** | -3.5 | 0.011 | 19/47 (AN3 CA, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.011 | 16/47 (HT-29, CHP-212, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.620×** | -3.5 | 0.011 | 14/43 (RPMI-7951, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.645×** | -3.2 | 0.029 | 11/47 (SW 1271, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.2 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.282× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.390× (z -8.9) |
| [[PANC-1 (line)]] | alt | 18.8 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 54.1 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 25.8 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -13.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 24.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +11.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 71.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0612× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -8.5) |
| [[A-172 (line)]] | wt | 15.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -8.7) |
| [[C32 (line)]] | wt | 16.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.86× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HOP62 (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0857× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.290× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[Panc 03.27 (line)]] | alt | 35.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW1417 (line)]] | alt | 21.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW48 (line)]] | wt | 27.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.145× (z -9.2) |
| [[A-427 (line)]] | wt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.1) | — |
| [[A498 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[CFPAC-1 (line)]] | alt | 18.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.05× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -9.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A549 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC11]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[MKS1]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 814 |
| [[TATDN3]] | +0.62 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[TRUB1]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MDM1]] | +0.57 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.57 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ARMCX5]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZFP37]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[NSL1]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ZNF138]] | +0.56 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[AMACR]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTB2]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.54 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[CYTH1]] | -0.53 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[PSEN1]] | -0.51 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | -0.51 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZDHHC11]] | -0.51 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[WNT2B]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PHYHD1]] | -0.50 | -0.37 / -0.59 | both halves | 7e-05 |  |
| [[FBXW7]] | -0.50 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[SLC4A5]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[TMBIM6]] | -0.49 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ATP2A1]] | -0.49 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00888]] | B | LINC00888 activity raises TTC8's level | lines that do not express LINC00888 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without LINC00888 | 0.016 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |
| [[ZNF391]] | B | ZNF391 activity raises TTC8's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without ZNF391 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[ZNF594-DT]] | B | ZNF594-DT activity raises TTC8's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without ZNF594-DT | 0.075 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[TMTC2]] | B | TMTC2 activity lowers TTC8's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without TMTC2 | 0.095 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.9, 2.1); signed map (-20.4, -16.6). **Vector** length 94.8, 22.7% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +8.5 | +10.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.9 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -4.3 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -4.3 | -8.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.3 — chr14:88,824,153-88,881,078 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BBS8, RP51 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; BBSome |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAM2](https://www.uniprot.org/uniprotkb/Q8TAM2) (Tetratricopeptide repeat protein 8):

> The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane. Firstly the BBSome associates with the …

**Summary**, from NCBI Gene [123016](https://www.ncbi.nlm.nih.gov/gene/123016):

> This gene encodes a protein that has been directly linked to Bardet-Biedl syndrome. The primary features of this syndrome include retinal dystrophy, obesity, polydactyly, renal abnormalities and learning disabilities. Experimentation in non-human eukaryotes suggests that this gene is expressed in ciliated cells and that it is involved in the formation of cilia. A mutation in this gene has also been implicated in nonsyndromic retinitis pigmentosa. Alternative splicing results in multiple …

**Accessions** — [HGNC:20087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20087) · Entrez [123016](https://www.ncbi.nlm.nih.gov/gene/123016) · UniProt [Q8TAM2](https://www.uniprot.org/uniprotkb/Q8TAM2) · Ensembl [ENSG00000165533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165533)

## Data

Gene col 9142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9142); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9142]; `tensor/DDL_lfc|DDL_z.npy` [9142]; `embed/gene_vectors.npy` [9142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9142 or target_col == 9142). Every well: [[TTC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
