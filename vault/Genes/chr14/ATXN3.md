---
symbol: "ATXN3"
type: "gene"
col: 828
ensembl_id: "ENSG00000066427"
name: "ataxin 3"
location: "14q32.12"
module: 187
arm: "+"
pooled_cpm: 80.89
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 30
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# ATXN3

*ataxin 3* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +6.0, q 1e-06, up in 26 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.427× (z -17.4, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.556× (z -17.0, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EZH1]] (+0.77, fdr 7e-06), [[FBXL20]] (+0.76, fdr 7e-06), [[HINFP]] (+0.70, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.64, fdr 7e-06), [[VARS1]] (-0.64, fdr 7e-06), [[FAT1]] (-0.62, fdr 7e-06).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANAPC1P4]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +6.0 | 1e-06 | 26/49 (SW 900, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.61×** | +5.1 | 8e-05 | 34/49 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.018 | 23/50 (HCT15, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.8 | 0.018 | 10/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.033 | 17/49 (Panc 03.27, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.21×** | +3.4 | 0.062 | 14/50 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.12× | +3.3 | 0.077 | 8/49 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.077 | 12/48 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[MK-3903 (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.077 | 10/48 (NCI-H460, J82, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.086 | 16/48 (PANC-1, C32, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.086 | 18/48 (PANC-1, LS 180, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Resveratrol (drug)]] 5 µM |  | 1.11× | +3.1 | 0.086 | 4/49 (SW 900, NCI-H1573, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.17× | +3.1 | 0.086 | 8/47 (LoVo, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 828.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.427×** | -17.4 | 0e+00 | 47/48 (MIA PaCa-2, NCI-H1792, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.556×** | -17.0 | 0e+00 | 41/48 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.556×** | -12.0 | 8e-31 | 44/48 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain | **0.560×** | -11.4 | 8e-28 | 34/44 (SK-MEL-2, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.563×** | -11.3 | 2e-27 | 42/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change; position correction uncertain | **0.554×** | -11.2 | 7e-27 | 39/45 (Panc 03.27, H4, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.375×** | -10.5 | 8e-24 | 46/48 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change; position correction uncertain | **0.615×** | -9.9 | 2e-21 | 39/49 (NCI-H1792, LOX-IMVI, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.406×** | -9.6 | 3e-20 | 40/49 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.634×** | -9.3 | 8e-19 | 35/48 (PANC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | **0.430×** | -9.0 | 1e-17 | 45/48 (MIA PaCa-2, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.451×** | -8.5 | 7e-16 | 42/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.463×** | -8.2 | 8e-15 | 40/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.486×** | -7.7 | 5e-13 | 41/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.707×** | -6.8 | 4e-10 | 31/47 (HS-578T, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.704×** | -5.1 | 1e-05 | 29/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -4.9 | 3e-05 | 27/48 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.797×** | -4.4 | 3e-04 | 25/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.680×** | -4.1 | 9e-04 | 26/47 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.774×** | -3.7 | 0.004 | 22/48 (SW 900, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.006 | 20/49 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 117 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -20.8) |
| [[PANC-1 (line)]] | alt | 74.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -20.1) |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 7 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -19.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.431× (z -13.1) |
| [[SW 900 (line)]] | alt | 89.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -16.1) |
| [[A549 (line)]] | wt | 116 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.2) |
| [[HOP62 (line)]] | alt | 110 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -17.7) |
| [[hTERT-HPNE (line)]] | wt | 87.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -23.1) |
| [[LS 180 (line)]] | wt | 76.5 | 1 (1 ⚠) | 4 (3 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.67× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -13.5) ⚠ cell-cycle shift, explains ~96% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.339× (z -10.3) |
| [[SNU-423 (line)]] | alt | 92.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -18.0) |
| [[SW480 (line)]] | alt | 87.4 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.383× (z -13.2) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.395× (z -12.8) |
| [[A498 (line)]] | wt | 43.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -19.5) |
| [[HS-578T (line)]] | alt | 75.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -21.0) |
| [[J82 (line)]] | alt | 67.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 94.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -17.8) |
| [[NCI-H23 (line)]] | alt | 84.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change; position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.569× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 66.4 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -13.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.576× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 97.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -11.4) |
| [[SW1417 (line)]] | alt | 72.5 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -13.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.488× (z -11.9) |
| [[A-172 (line)]] | wt | 52.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.6) |
| [[AN3 CA (line)]] | alt | 75.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 60.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -14.6) |
| [[C32 (line)]] | wt | 73.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.7) |
| [[H4 (line)]] | wt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change; position correction uncertain |
| [[Hs 766T (line)]] | wt | 67.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 87.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change; position correction uncertain |
| [[SK-MEL-2 (line)]] | alt | 86.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -10.0) |
| [[SW48 (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain |
| [[A-427 (line)]] | wt | 84.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain |
| [[BT-474 (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain |
| [[C-33 A (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain |
| [[COLO 205 (line)]] | alt | 63.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -14.5) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain |
| [[LoVo (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.360× (z -10.8) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change; position correction uncertain |
| [[NCI-H2347 (line)]] | alt | 68.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -8.6) |
| [[SHP-77 (line)]] | alt | 71.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.396× (z -8.5) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 87.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -10.5) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EZH1]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.76 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[HINFP]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[BSDC1]] | +0.69 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[ECT2L]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.68 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[RETREG3]] | +0.67 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[KLHL24]] | +0.67 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[ZER1]] | +0.67 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[AAMDC]] | +0.67 | +0.46 / +0.73 | both halves | 3e-05 |  |
| [[LMBR1L]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[GARRE1]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[VARS1]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[FAT1]] | -0.62 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[NAA15]] | -0.61 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[CEP41]] | -0.60 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[PSMG1]] | -0.59 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANAPC1P4]] | C | ANAPC1P4 activity raises ATXN3's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 1.32× lower at baseline in the lines without ANAPC1P4 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.9, -43.0); signed map (-16.8, 11.5). **Vector** length 134, 44.0% of its response variance represented; |z| ≥ 3 in 1,247 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.9 | +0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.6 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.6 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +3.1 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.3 | -17.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.1 | -10.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.2 | -8.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | -7.1 | -9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -12.0 |
|  | [[EX229 (drug)]] 5 µM |  | -6.7 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:92,044,496-92,106,621 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATX3, JOS; previously SCA3, MJD |
| Gene groups (HGNC) | Ataxin 3 family |
| Reactome | 4 pathways, smallest: Josephin domain DUBs; FOXO-mediated transcription of oxidative stress, metabolic and neuronal genes; FOXO-mediated transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P54252](https://www.uniprot.org/uniprotkb/P54252) (Ataxin-3):

> Deubiquitinating enzyme involved in protein homeostasis maintenance, transcription, cytoskeleton regulation, myogenesis and degradation of misfolded chaperone substrates. Binds long polyubiquitin chains and trims them, while it has weak or no activity against chains of 4 or less ubiquitins. Involved in degradation of misfolded chaperone substrates via its interaction with STUB1/CHIP: recruited to monoubiquitinated STUB1/CHIP, and restricts the length of ubiquitin chain attached to STUB1/CHIP …

**Summary**, from NCBI Gene [4287](https://www.ncbi.nlm.nih.gov/gene/4287):

> Machado-Joseph disease, also known as spinocerebellar ataxia-3, is an autosomal dominant neurologic disorder. The protein encoded by this gene contains (CAG)n repeats in the coding region, and the expansion of these repeats from the normal 12-44 to 52-86 is one cause of Machado-Joseph disease. There is a negative correlation between the age of onset and CAG repeat numbers. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by …

**Accessions** — [HGNC:7106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7106) · Entrez [4287](https://www.ncbi.nlm.nih.gov/gene/4287) · UniProt [P54252](https://www.uniprot.org/uniprotkb/P54252) · Ensembl [ENSG00000066427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066427)

## Data

Gene col 828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 828); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 828]; `tensor/DDL_lfc|DDL_z.npy` [828]; `embed/gene_vectors.npy` [828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 828 or target_col == 828). Every well: [[ATXN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
