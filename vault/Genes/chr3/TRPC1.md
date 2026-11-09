---
symbol: "TRPC1"
type: "gene"
col: 6947
ensembl_id: "ENSG00000144935"
name: "transient receptor potential cation channel subfamily C member 1"
location: "3q23"
module: 23
arm: "+"
pooled_cpm: 89.36
n_lines_expressing: 44
n_dd_up: 2
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# TRPC1

*transient receptor potential cation channel subfamily C member 1* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.44× (z +4.5, q 0.004, up in 30 of 41 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.32× (z +3.8, q 0.039, up in 25 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 2.17×, AsPC-1 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 2.22×, SW480 1.79×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.281× (z -17.5, q 0e+00, down in 41 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLAGL1]] (+0.65, fdr 1e-05), [[IPO9-AS1]] (+0.62, fdr 2e-05), [[C2orf92]] (+0.61, fdr 2e-05); moves opposite to [[PTGES2]] (-0.53, fdr 3e-04), [[ZDHHC3]] (-0.52, fdr 6e-05), [[LRP5]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MIR137HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6947.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 2.17×, AsPC-1 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 2.22×, SW480 1.79×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +4.5 | 0.004 | 30/41 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.039 | 25/41 (SW480, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.28× | +3.4 | 0.11 | 23/42 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.18 | 20/42 (HS-578T, AN3 CA, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.18 | 11/42 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.18 | 19/41 (LoVo, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6947.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.281×** | -17.5 | 0e+00 | 41/42 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.327×** | -15.4 | 0e+00 | 41/42 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.377×** | -13.4 | 7e-39 | 39/42 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.362×** | -12.4 | 2e-33 | 37/41 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.418×** | -12.0 | 5e-31 | 38/42 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.445×** | -11.1 | 9e-27 | 34/42 (H4, PANC-1, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.236×** | -10.4 | 2e-23 | 40/43 (H4, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.482×** | -10.0 | 7e-22 | 36/42 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.553×** | -8.1 | 2e-14 | 34/42 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.527×** | -8.1 | 2e-14 | 34/39 (H4, BT-474, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.569×** | -7.7 | 5e-13 | 30/42 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.534×** | -7.7 | 8e-13 | 31/38 (NCI-H23, A-172, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.585×** | -7.4 | 8e-12 | 31/42 (SNU-423, NCI-H1792, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.361×** | -7.3 | 1e-11 | 35/42 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.571×** | -7.1 | 6e-11 | 29/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.775×** | -3.5 | 0.013 | 22/42 (AsPC-1, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.773×** | -3.3 | 0.021 | 20/42 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.785×** | -2.9 | 0.071 | 16/43 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.810×** | -2.9 | 0.083 | 17/42 (SW 1088, SNU-423, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.862× | -2.9 | 0.088 | 7/43 (C-33 A, SW480, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.675×** | -2.8 | 0.093 | 14/42 (Hs 766T, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.799×** | -2.8 | 0.094 | 19/42 (HOP62, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 247 | 0 | 15 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 84.4 | 0 | 15 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 75.8 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -15.8) |
| [[PANC-1 (line)]] | alt | 187 | 0 | 14 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -25.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -24.5) |
| [[SNU-423 (line)]] | alt | 161 | 0 | 14 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.235× (z -14.1) |
| [[HOP62 (line)]] | alt | 152 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -12.5) |
| [[J82 (line)]] | alt | 162 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 120 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 144 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.289× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 74.6 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.179× (z -16.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -16.4) |
| [[SW480 (line)]] | alt | 64.3 | 2 (2 ⚠) | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.5 µM 0.243× (z -14.6) |
| [[A-172 (line)]] | wt | 234 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -11.6) |
| [[HCT15 (line)]] | alt | 89.2 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -11.8) |
| [[LoVo (line)]] | wt | 51.7 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -14.1) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.336× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 136 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 158 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -13.1) |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0698× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.145× (z -9.7) |
| [[C-33 A (line)]] | alt | 98.4 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.285× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 87.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.270× (z -11.0) |
| [[Hs 766T (line)]] | wt | 44.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 47.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.317× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 127 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.291× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.305× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 86.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -11.2) |
| [[SW 1271 (line)]] | alt | 156 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0917× (z -11.8) |
| [[A-427 (line)]] | wt | 141 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.172× (z -10.3) |
| [[AN3 CA (line)]] | alt | 53.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[CHP-212 (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[GSK1059615 (drug)]] 5 µM 0.0623× (z -8.9) |
| [[A549 (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[C32 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 71.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0904× (z -15.9) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 44.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 56.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -10.2) |
| [[SHP-77 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.231× (z -11.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SW 900 (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A498 (line)]] | wt | 99.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAGL1]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[IPO9-AS1]] | +0.62 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[C2orf92]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SEPTIN7-DT]] | +0.58 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[LINC00863]] | +0.58 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ZNF425]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.57 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[LRCH3]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[APLF]] | +0.56 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[MARCHF7]] | +0.56 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[EIF3J-DT]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[CAMSAP2]] | +0.56 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGES2]] | -0.53 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[ZDHHC3]] | -0.52 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[LRP5]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SEPTIN7P14]] | -0.52 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ERMP1]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[LHPP]] | -0.51 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[NDRG3]] | -0.51 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SORT1]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MAP2K6]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PIK3R2]] | -0.50 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PARP1]] | -0.50 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[BCR]] | -0.50 | -0.55 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR137HG]] | B | MIR137HG activity raises TRPC1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.82× lower at baseline in the lines without MIR137HG | 0.018 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2 |
| [[DENND2A]] | B | DENND2A activity raises TRPC1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without DENND2A | 0.021 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[TSHZ3-AS1]] | B | TSHZ3-AS1 activity raises TRPC1's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without TSHZ3-AS1 | 0.031 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[JAM2]] | B | JAM2 activity raises TRPC1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without JAM2 | 0.056 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[DENND5A]] | C | DENND5A activity raises TRPC1's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 7.94× lower at baseline in the lines without DENND5A | 0.012 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (30.0, -6.0); signed map (26.1, 8.9). **Vector** length 101, 34.6% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | -0.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.2 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -4.9 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.3 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily C member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:142,724,034-142,807,888 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HTRP-1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Transient receptor potential cation channel subfamily C |
| Reactome | 14 pathways, smallest: Role of second messengers in netrin-1 signaling; TRP channels; Antigen activates B Cell Receptor (BCR) leading to generation of second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [P48995](https://www.uniprot.org/uniprotkb/P48995) (Short transient receptor potential channel 1):

> Forms a receptor-activated non-selective calcium permeant cation channel. Forms a heteromeric ion channel with TRPC4 or TRPC5 that has reduced calcium permeability compared to the homomeric TRPC4 or TRPC5 channel. Also permeable to monovalent ions including sodium, lithium and cesium ions.; [Isoform Short]: Forms a receptor-activated non-selective calcium permeant cation channel. Also activated by intracellular calcium store depletion.

**Summary**, from NCBI Gene [7220](https://www.ncbi.nlm.nih.gov/gene/7220):

> The protein encoded by this gene is a membrane protein that can form a non-selective channel permeable to calcium and other cations. The encoded protein appears to be induced to form channels by a receptor tyrosine kinase-activated phosphatidylinositol second messenger system and also by depletion of intracellular calcium stores. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:12333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12333) · Entrez [7220](https://www.ncbi.nlm.nih.gov/gene/7220) · UniProt [P48995](https://www.uniprot.org/uniprotkb/P48995) · Ensembl [ENSG00000144935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144935)

## Data

Gene col 6947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6947); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6947]; `tensor/DDL_lfc|DDL_z.npy` [6947]; `embed/gene_vectors.npy` [6947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6947 or target_col == 6947). Every well: [[TRPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
