---
symbol: "MACROD1"
type: "gene"
col: 5439
ensembl_id: "ENSG00000133315"
name: "mono-ADP ribosylhydrolase 1"
location: "11q13.1"
module: 18
arm: "+"
pooled_cpm: 39.05
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MACROD1

*mono-ADP ribosylhydrolase 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +10.0, q 1e-20, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.366× (z -27.8, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY3]] (+0.74, fdr 7e-06), [[CMTM4]] (+0.67, fdr 7e-06), [[LYRM4]] (+0.67, fdr 7e-06); moves opposite to [[VWA5A]] (-0.60, fdr 1e-05), [[SNAPIN]] (-0.55, fdr 4e-05), [[RAB30]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +10.0 | 1e-20 | 34/48 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +6.7 | 8e-09 | 33/48 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.5 | 7e-06 | 27/45 (SHP-77, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.22×** | +5.4 | 8e-06 | 23/48 (PANC-1, NCI-H1573, …) | all doses, flat | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.3 | 1e-05 | 18/47 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.27×** | +4.7 | 2e-04 | 20/48 (PANC-1, A549, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.7 | 2e-04 | 16/39 (BT-474, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +4.5 | 4e-04 | 22/44 (BT-474, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +4.4 | 7e-04 | 18/47 (PANC-1, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.3 | 8e-04 | 14/48 (NCI-H460, A-172, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +4.3 | 8e-04 | 12/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.003 | 15/47 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.003 | 15/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.006 | 9/47 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.22×** | +3.8 | 0.006 | 15/48 (MIA PaCa-2, HCT15, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.14× | +3.7 | 0.008 | 11/48 (A549, SHP-77, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.018 | 14/47 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.024 | 10/47 (COLO 205, Hs 766T, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.039 | 9/47 (J82, HS-578T, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.047 | 8/48 (NCI-H460, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5439.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.366×** | -27.8 | 0e+00 | 45/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.405×** | -17.0 | 0e+00 | 43/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.468×** | -14.9 | 0e+00 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.367×** | -10.3 | 1e-22 | 41/48 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.629×** | -9.1 | 1e-17 | 34/48 (PANC-1, SNU-1, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.459×** | -8.0 | 2e-13 | 33/47 (SW48, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.742×** | -5.8 | 4e-07 | 26/47 (LoVo, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.757×** | -5.4 | 4e-06 | 25/48 (SW48, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.761×** | -5.3 | 6e-06 | 24/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.781×** | -4.8 | 8e-05 | 22/47 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -4.3 | 1e-03 | 19/48 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.661×** | -4.2 | 0.001 | 19/46 (SNU-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.808×** | -4.2 | 0.001 | 20/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.819×** | -3.9 | 0.004 | 22/47 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.699×** | -3.7 | 0.009 | 20/47 (SNU-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.057 | 11/48 (SW480, Panc 03.27, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.750×** | -2.9 | 0.097 | 10/48 (AN3 CA, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 65.4 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -25.3) |
| [[PANC-1 (line)]] | alt | 45.9 | 3 (3 ⚠) | 6 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.76× (z +10.0) ⚠ cell-cycle shift, explains ~78% of this change | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -27.1) |
| [[MIA PaCa-2 (line)]] | alt | 79.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0241× (z -52.7) |
| [[BT-474 (line)]] | alt | 142 | 1 (1 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -26.0) |
| [[A-427 (line)]] | wt | 62.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.8) |
| [[LoVo (line)]] | wt | 54.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -13.4) |
| [[LS 180 (line)]] | wt | 47.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 24.8 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -14.6) |
| [[SW48 (line)]] | wt | 94.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.9) |
| [[C32 (line)]] | wt | 33.3 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 50.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -21.7) |
| [[RKO (line)]] | wt | 53.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -22.2) |
| [[SW480 (line)]] | alt | 61.7 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.12× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -24.0) |
| [[A549 (line)]] | wt | 18.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.9) |
| [[C-33 A (line)]] | alt | 72.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -17.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 54.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -18.4) |
| [[HT-29 (line)]] | alt | 65.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 57.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -19.7) |
| [[A498 (line)]] | wt | 18.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.305× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 27.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.6) | [[Harringtonine (drug)]] 5 µM 0.304× (z -9.1) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.204× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 21.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.9) |
| [[H4 (line)]] | wt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -10.1) |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.2) |
| [[J82 (line)]] | alt | 53.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.2) |
| [[KATO III (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 19.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.221× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.153× (z -9.7) |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.1) |
| [[SW1417 (line)]] | alt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -14.1) |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY3]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[CMTM4]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[LYRM4]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[DHX33]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MDN1]] | +0.65 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[MRPS25]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CAPN15]] | +0.65 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[PRMT3]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ANAPC1]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TRMT1]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[POLR3E]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[METTL8]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA5A]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.55 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RAB30]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[HCFC2]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises MACROD1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without WNK2 | 0.041 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[ADCY3]] | B | ADCY3 activity raises MACROD1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.21× lower at baseline in the lines without ADCY3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[LRRC8D]] | C | LRRC8D activity raises MACROD1's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without LRRC8D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[MTHFD1L]] | C | MTHFD1L activity raises MACROD1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.22× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[PPARGC1B]] | C | PPARGC1B activity raises MACROD1's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |
| [[ANKRD13B]] | C | ANKRD13B activity raises MACROD1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.79× lower at baseline in the lines without ANKRD13B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.6, -36.4); signed map (-1.4, -52.8). **Vector** length 112, 30.5% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -17.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -27.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -10.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | +0.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | mono-ADP ribosylhydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:63,998,558-64,166,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LRP16 |
| Gene groups (HGNC) | Macro domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ69](https://www.uniprot.org/uniprotkb/Q9BQ69) (ADP-ribose glycohydrolase MACROD1):

> Removes ADP-ribose from aspartate and glutamate residues in proteins bearing a single ADP-ribose moiety. Inactive towards proteins bearing poly-ADP-ribose. Deacetylates O-acetyl-ADP ribose, a signaling molecule generated by the deacetylation of acetylated lysine residues in histones and other proteins. Plays a role in estrogen signaling. Binds to androgen receptor (AR) and amplifies the transactivation function of AR in response to androgen. May play an important role in carcinogenesis and/or …

**Summary**, from NCBI Gene [28992](https://www.ncbi.nlm.nih.gov/gene/28992):

> Enables ADP-ribosylglutamate hydrolase activity and deacetylase activity. Involved in DNA damage response; peptidyl-glutamate ADP-deribosylation; and purine nucleoside metabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29598) · Entrez [28992](https://www.ncbi.nlm.nih.gov/gene/28992) · UniProt [Q9BQ69](https://www.uniprot.org/uniprotkb/Q9BQ69) · Ensembl [ENSG00000133315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133315)

## Data

Gene col 5439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5439); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5439]; `tensor/DDL_lfc|DDL_z.npy` [5439]; `embed/gene_vectors.npy` [5439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5439 or target_col == 5439). Every well: [[MACROD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MACROD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
