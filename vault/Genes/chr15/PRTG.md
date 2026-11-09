---
symbol: "PRTG"
type: "gene"
col: 9309
ensembl_id: "ENSG00000166450"
name: "protogenin"
location: "15q21.3"
module: 94
arm: "+"
pooled_cpm: 35.5
n_lines_expressing: 36
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 12
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# PRTG

*protogenin* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 2.00× (z +18.1, q 0e+00, up in 29 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.383× (z -17.1, q 0e+00, down in 20 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.528× (z -11.8, q 4e-30, down in 27 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC8D]] (+0.65, fdr 7e-06), [[RNF150]] (+0.59, fdr 2e-05), [[CNNM1]] (+0.55, fdr 1e-05); moves opposite to [[GLYR1]] (-0.52, fdr 5e-05), [[MUC20-OT1]] (-0.52, fdr 2e-05), [[KATNIP]] (-0.47, fdr 7e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); 12 go from it, the strongest it → [[BBS5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.00×** | +18.1 | 0e+00 | 29/34 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.26×** | +15.1 | 0e+00 | 31/34 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.17×** | +14.3 | 3e-44 | 30/34 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.67×** | +9.4 | 5e-19 | 27/33 (HepG2/C3A, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +6.8 | 1e-09 | 19/34 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.8 | 1e-09 | 20/34 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.1 | 9e-08 | 19/33 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +4.7 | 2e-04 | 14/34 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +4.4 | 7e-04 | 11/34 (SK-MEL-2, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.011 | 18/34 (NCI-H2347, Panc 03.27, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.012 | 10/34 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.022 | 5/33 (SK-MEL-2, H4, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.035 | 8/33 (HOP62, BT-474, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.3 | 0.035 | 6/33 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.065 | 5/33 (C32, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.383×** | -17.1 | 0e+00 | 20/29 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.498×** | -12.9 | 8e-36 | 22/32 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.528×** | -11.8 | 4e-30 | 27/34 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -10.6 | 3e-24 | 24/33 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -8.6 | 1e-15 | 23/33 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.634×** | -8.4 | 3e-15 | 23/33 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.665×** | -7.0 | 2e-10 | 20/29 (Panc 03.27, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -6.3 | 2e-08 | 21/34 (A-427, NCI-H2030, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.707×** | -6.1 | 8e-08 | 16/34 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.574×** | -5.4 | 4e-06 | 18/31 (LoVo, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -5.3 | 6e-06 | 17/33 (SK-MEL-2, AN3 CA, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -5.1 | 2e-05 | 16/33 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.761×** | -5.1 | 2e-05 | 15/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.605×** | -4.9 | 5e-05 | 16/33 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.836× | -4.7 | 1e-04 | 17/34 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.638×** | -4.4 | 5e-04 | 14/34 (HEC-1-A, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.785×** | -4.2 | 7e-04 | 10/34 (A498, LoVo, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.679×** | -4.1 | 0.001 | 11/34 (A498, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.803×** | -3.8 | 0.004 | 13/34 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.731×** | -3.3 | 0.024 | 4/34 (MIA PaCa-2, A498, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.882× | -3.3 | 0.024 | 6/34 (CFPAC-1, C32, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.839× | -3.3 | 0.025 | 9/34 (PANC-1, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.3 | 3 | 10 (7 ⚠) | [[Selinexor (drug)]] 5 µM 2.63× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -17.5) |
| [[SNU-1 (line)]] | wt | 106 | 1 | 10 (7 ⚠) | [[Selinexor (drug)]] 5 µM 2.07× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0858× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 44.2 | 2 | 7 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.89× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 91.1 | 2 | 4 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.99× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 15.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +21.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.53× (z +12.9) | — |
| [[J82 (line)]] | alt | 59.5 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 79.3 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +19.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.05× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -17.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.1 | 2 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.53× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.9) ⚠ cell-cycle shift, explains ~12% of this change |
| [[AN3 CA (line)]] | alt | 161 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0576× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.169× (z -10.2) |
| [[C-33 A (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0816× (z -23.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 212 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -13.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 52.3 | 2 | 1 | [[Selinexor (drug)]] 5 µM 2.42× (z +9.2) | [[Ixazomib citrate (drug)]] 0.5 µM 0.220× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 64.8 | 1 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.95× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -16.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 49.3 | 3 | 0 | [[Selinexor (drug)]] 0.05 µM 5.45× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 59.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.6) ⚠ cell-cycle shift, explains ~12% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 30.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.299× (z -13.7) |
| [[A549 (line)]] | wt | 61.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.95× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 12.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 17.1× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 11.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.21× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0469× (z -15.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 29.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.57× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 601 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 60.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.238× (z -11.2) |
| [[SNU-423 (line)]] | alt | 22.7 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.92× (z +9.6) | — |
| [[A498 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8D]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RNF150]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[CNNM1]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SLC16A14]] | +0.54 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[WDSUB1]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[SLC16A9]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ZNF32]] | +0.53 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[ZNF485]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SLC9A2]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CHST3]] | +0.52 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TFAP4]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DUSP15]] | +0.52 | +0.38 / +0.60 | both halves | 7e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLYR1]] | -0.52 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[MUC20-OT1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[KATNIP]] | -0.47 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[IL18BP]] | -0.44 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[FAM120B]] | -0.44 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[EOLA2-DT]] | -0.44 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[MFSD11]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises PRTG's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without MCOLN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[LRP3]] | B | LRP3 activity raises PRTG's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 5.14× lower at baseline in the lines without LRP3 | 0.051 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[ULK2]] | B | ULK2 activity raises PRTG's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 3.52× lower at baseline in the lines without ULK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[ST6GAL1]] | B | ST6GAL1 activity raises PRTG's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without ST6GAL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BBS5]] | B | PRTG activity raises BBS5's level | lines that do not express PRTG (14) vs lines expressing it (36) | 3.05× lower at baseline in the lines without PRTG | 0.007 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[ALDH5A1]] | B | PRTG activity raises ALDH5A1's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.28× lower at baseline in the lines without PRTG | 0.027 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[SMO]] | B | PRTG activity raises SMO's level | lines that do not express PRTG (14) vs lines expressing it (36) | 3.48× lower at baseline in the lines without PRTG | 0.030 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[STK33]] | B | PRTG activity raises STK33's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without PRTG | 0.044 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[LRP3]] | B | PRTG activity raises LRP3's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without PRTG | 0.060 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[ZNF391]] | B | PRTG activity raises ZNF391's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without PRTG | 0.062 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[ULK2]] | B | PRTG activity raises ULK2's level | lines that do not express PRTG (14) vs lines expressing it (36) | 3.08× lower at baseline in the lines without PRTG | 0.076 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[MVB12B]] | B | PRTG activity raises MVB12B's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.32× lower at baseline in the lines without PRTG | 0.077 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[C3orf33]] | B | PRTG activity raises C3orf33's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without PRTG | 0.079 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[QDPR]] | B | PRTG activity raises QDPR's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.28× lower at baseline in the lines without PRTG | 0.088 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[GLYR1]] | B | PRTG activity lowers GLYR1's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.16× higher at baseline in the lines without PRTG | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[ST6GAL1]] | B | PRTG activity raises ST6GAL1's level | lines that do not express PRTG (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without PRTG | 0.091 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.4, 24.4); signed map (13.9, -16.6). **Vector** length 111, 31.2% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.7 | +18.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.7 | +14.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.6 | +15.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +6.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +9.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -8.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -8.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | -11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.1 | -4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | protogenin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,611,544-55,743,152 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25756, IGDCC5 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2VWP7](https://www.uniprot.org/uniprotkb/Q2VWP7) (Protogenin):

> May play a role in anteroposterior axis elongation.

**Summary**, from NCBI Gene [283659](https://www.ncbi.nlm.nih.gov/gene/283659):

> This gene encodes a member of the immunoglobulin superfamily. The encoded transmembrane protein has been associated with the development of various tissues, especially neurogenesis. It has been suggested that this gene may be associated with attention deficit hyperactivity disorder (ADHD). [provided by RefSeq, Nov 2014]

**Accessions** — [HGNC:26373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26373) · Entrez [283659](https://www.ncbi.nlm.nih.gov/gene/283659) · UniProt [Q2VWP7](https://www.uniprot.org/uniprotkb/Q2VWP7) · Ensembl [ENSG00000166450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166450)

## Data

Gene col 9309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9309); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9309]; `tensor/DDL_lfc|DDL_z.npy` [9309]; `embed/gene_vectors.npy` [9309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9309 or target_col == 9309). Every well: [[PRTG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRTG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
