---
symbol: "PRDM15"
type: "gene"
col: 6582
ensembl_id: "ENSG00000141956"
name: "PR/SET domain 15"
location: "21q22.3"
module: 5
arm: "+"
pooled_cpm: 16.09
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PRDM15

*PR/SET domain 15* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +15.8, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.673× (z -6.7, q 1e-08, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM10]] (+0.78, fdr 7e-06), [[TMEM11-DT]] (+0.71, fdr 7e-06), [[HCFC1]] (+0.68, fdr 1e-05); moves opposite to [[SNAPIN]] (-0.68, fdr 1e-05), [[LINC00888-1]] (-0.65, fdr 1e-05), [[UBE2B]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +15.8 | 0e+00 | 39/47 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.97×** | +11.4 | 1e-27 | 38/47 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +10.7 | 3e-24 | 38/48 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +10.3 | 7e-23 | 37/46 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.76×** | +9.5 | 3e-19 | 36/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +8.9 | 8e-17 | 34/46 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.67×** | +8.6 | 9e-16 | 34/46 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +8.4 | 4e-15 | 27/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.5 | 6e-12 | 27/46 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +6.6 | 2e-09 | 30/46 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.36×** | +5.1 | 2e-05 | 19/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +5.0 | 2e-05 | 20/47 (A-172, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +4.9 | 4e-05 | 20/47 (HOP62, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.69×** | +4.6 | 2e-04 | 13/46 (C32, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.5 | 2e-04 | 14/48 (A498, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.001 | 14/46 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.004 | 9/47 (NCI-H460, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.015 | 6/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.015 | 5/44 (C32, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.078 | 13/47 (SW480, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.673×** | -6.7 | 1e-08 | 23/47 (C-33 A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.815×** | -4.9 | 3e-04 | 19/48 (A-427, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.776×** | -4.3 | 0.003 | 21/48 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.761×** | -4.3 | 0.003 | 13/36 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.2 | 0.003 | 14/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.787×** | -4.1 | 0.004 | 19/48 (SW1417, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.788×** | -4.0 | 0.004 | 15/47 (SK-MEL-2, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.789×** | -4.0 | 0.004 | 13/47 (MIA PaCa-2, A-427, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.802×** | -3.7 | 0.012 | 17/47 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -3.7 | 0.015 | 11/26 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.822×** | -3.3 | 0.043 | 16/48 (SW48, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.822×** | -3.3 | 0.043 | 7/48 (hTERT-HPNE, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 0.872× | -3.3 | 0.045 | 20/47 (RKO, LOX-IMVI, …) | rises with dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.774×** | -3.1 | 0.080 | 13/45 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.834× | -3.1 | 0.080 | 0/48 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 28.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0672× (z -20.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 21.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.2) ⚠ cell-cycle shift, explains ~82% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 20.5 | 1 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.20× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -16.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 30.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.9) ⚠ cell-cycle shift, explains ~82% of this change |
| [[A-427 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -11.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 40.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.249× (z -9.4) |
| [[C32 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[COLO 205 (line)]] | alt | 9.74 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0936× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0901× (z -9.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[LoVo (line)]] | wt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.16× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.289× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -12.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.156× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.5) | — |
| [[A-172 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM10]] | +0.78 | +0.73 / +0.64 | both halves | 7e-06 | same gene group |
| [[TMEM11-DT]] | +0.71 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[HCFC1]] | +0.68 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[KMT2D]] | +0.65 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MIATNB]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LYRM4]] | +0.65 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[LRRC69]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MACROD1]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SENP3]] | +0.63 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ATR]] | +0.63 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[MCM9]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPIN]] | -0.68 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[LINC00888-1]] | -0.65 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.61 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[CREB3]] | -0.59 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[DMXL1]] | -0.59 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[SPAG9]] | -0.57 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[ABI1]] | -0.57 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[KIFAP3]] | -0.56 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[SKAP2]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RP9]] | -0.55 | -0.64 / -0.32 | both halves | 1e-04 |  |
| [[CRBN]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TPR]] | -0.55 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRDM15's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BEGAIN]] | B | BEGAIN activity raises PRDM15's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.36× lower at baseline in the lines without BEGAIN | 0.036 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-10.5, 19.9); signed map (-8.1, -40.3). **Vector** length 96.2, 20.3% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +15.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.3 | +8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.7 | +10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.2 | +11.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.4 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -4.3 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.8 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -3.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:41,798,225-41,879,482 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF298, C21orf83 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [P57071](https://www.uniprot.org/uniprotkb/P57071) (PR domain zinc finger protein 15):

> Sequence-specific DNA-binding transcriptional regulator. Plays a role as a molecular node in a transcriptional network regulating embryonic development and cell fate decision. Stimulates the expression of upstream key transcriptional activators and repressors of the Wnt/beta-catenin and MAPK/ERK pathways, respectively, that are essential for naive pluripotency and self-renewal maintenance of embryonic stem cells (ESCs). Specifically promotes SPRY1 and RSPO1 transcription activation through …

**Summary**, from NCBI Gene [63977](https://www.ncbi.nlm.nih.gov/gene/63977):

> Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and promoter-specific chromatin binding activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II; regulation of signal transduction; and regulation of stem cell division. Located in nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13999) · Entrez [63977](https://www.ncbi.nlm.nih.gov/gene/63977) · UniProt [P57071](https://www.uniprot.org/uniprotkb/P57071) · Ensembl [ENSG00000141956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141956)

## Data

Gene col 6582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6582); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6582]; `tensor/DDL_lfc|DDL_z.npy` [6582]; `embed/gene_vectors.npy` [6582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6582 or target_col == 6582). Every well: [[PRDM15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
