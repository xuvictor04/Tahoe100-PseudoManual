---
symbol: "NEO1"
type: "gene"
col: 851
ensembl_id: "ENSG00000067141"
name: "neogenin 1"
location: "15q24.1"
module: 197
arm: "+"
pooled_cpm: 53.91
n_lines_expressing: 43
n_dd_up: 13
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# NEO1

*neogenin 1* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +10.8, q 1e-24, up in 29 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.670× (z -8.1, q 3e-13, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHSD2]] (+0.62, fdr 1e-05), [[LRP6]] (+0.60, fdr 1e-05), [[STIM2]] (+0.57, fdr 1e-05); moves opposite to [[ACOX3]] (-0.63, fdr 2e-05), [[KRBOX4]] (-0.59, fdr 1e-05), [[WDR37]] (-0.56, fdr 1e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[UST]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +10.8 | 1e-24 | 29/41 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +10.7 | 2e-24 | 31/41 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +8.7 | 9e-16 | 26/41 (HEC-1-A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +8.5 | 2e-15 | 30/42 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +7.6 | 3e-12 | 26/41 (J82, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +6.6 | 4e-09 | 21/41 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +5.8 | 6e-07 | 26/42 (NCI-H460, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.7 | 8e-07 | 21/41 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +5.3 | 8e-06 | 18/41 (SW1417, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 8e-06 | 21/41 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +5.1 | 2e-05 | 19/41 (SW1417, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +4.6 | 2e-04 | 18/41 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.9 | 0.004 | 13/41 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +3.5 | 0.021 | 11/42 (SW1417, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.030 | 13/41 (AsPC-1, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.034 | 15/41 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Encorafenib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.065 | 9/41 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.073 | 13/40 (AsPC-1, C32, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +2.9 | 0.097 | 10/41 (AsPC-1, A498, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.11× | +2.9 | 0.097 | 6/41 (AsPC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -8.1 | 3e-13 | 28/41 (SW480, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -6.8 | 3e-09 | 27/42 (CHP-212, LoVo, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -6.4 | 3e-08 | 25/41 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.576×** | -5.8 | 6e-07 | 24/41 (HEC-1-A, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.750×** | -5.8 | 6e-07 | 23/41 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.581×** | -5.8 | 8e-07 | 23/41 (HT-29, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -5.3 | 9e-06 | 24/41 (NCI-H1573, LoVo, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.770×** | -5.3 | 9e-06 | 20/40 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.775×** | -5.0 | 4e-05 | 19/37 (C-33 A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.788×** | -4.8 | 8e-05 | 16/40 (H4, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.637×** | -4.8 | 9e-05 | 22/41 (SW480, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.648×** | -4.6 | 2e-04 | 20/41 (LoVo, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.655×** | -4.5 | 3e-04 | 21/41 (SW 1271, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.806×** | -4.4 | 5e-04 | 19/41 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.808×** | -4.3 | 6e-04 | 20/41 (SNU-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.742×** | -4.3 | 6e-04 | 19/41 (C32, J82, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.803×** | -4.3 | 7e-04 | 19/40 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.753×** | -4.1 | 0.001 | 14/41 (SW480, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.763×** | -3.9 | 0.003 | 14/41 (NCI-H661, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 122 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 21.1 | 7 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.83× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 94.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -14.0) |
| [[SNU-1 (line)]] | wt | 105 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 79.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.0) | — |
| [[A-427 (line)]] | wt | 99.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.461× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 199 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0605× (z -29.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 27.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 66.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 81.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.400× (z -12.9) |
| [[A-172 (line)]] | wt | 18.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.51× (z +9.1) | — |
| [[A549 (line)]] | wt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 98.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 49.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.33× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -8.9) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 95.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.9) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 54.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 94.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD2]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[LRP6]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[STIM2]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RARG]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[CD83]] | +0.54 | +0.35 / +0.69 | both halves | 1e-04 |  |
| [[ISOC1]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CACHD1]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TCF7L2]] | +0.53 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[QPCT]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[RFK]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CX3CL1]] | +0.52 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHA5]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOX3]] | -0.63 | -0.48 / -0.63 | both halves | 2e-05 | pathway: Protein localization |
| [[KRBOX4]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[WDR37]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[FAM156A]] | -0.56 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[SLC30A6]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DRD4]] | -0.51 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TRMT44]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PEX16]] | -0.49 | -0.36 / -0.44 | both halves | 9e-05 | pathway: Protein localization |
| [[PCYT1A]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PMM2]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SZT2]] | -0.48 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[ZNF229]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UST]] | B | UST activity raises NEO1's level | lines that do not express UST (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without UST | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC1A1, SH3GL3 |
| [[PRKAR2B]] | B | PRKAR2B activity raises NEO1's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 1.90× lower at baseline in the lines without PRKAR2B | 0.053 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[PPFIBP2]] | B | PPFIBP2 activity raises NEO1's level | lines that do not express PPFIBP2 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without PPFIBP2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LRRC8D |
| [[DTX4]] | C | DTX4 activity raises NEO1's level | lines that do not express DTX4 (7) vs lines expressing it (43) | 3.76× lower at baseline in the lines without DTX4 | 0.050 | ⚠ within organs, on part of the lines; also absent: NEO1, WNK4, STPG2; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.2, 37.2); signed map (5.0, 12.9). **Vector** length 101, 24.7% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +10.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.6 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -5.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | neogenin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:73,051,710-73,305,205 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NGN, HsT17534, IGDCC2, NTN1R2 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 6 pathways, smallest: Myogenesis; Netrin-1 signaling; Cotranslational targeting of proteins to the endoplasmic reticulum |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92859](https://www.uniprot.org/uniprotkb/Q92859) (Neogenin):

> Multi-functional cell surface receptor regulating cell adhesion in many diverse developmental processes, including neural tube and mammary gland formation, myogenesis and angiogenesis. Receptor for members of the BMP, netrin, and repulsive guidance molecule (RGM) families. Netrin-Neogenin interactions result in a chemoattractive axon guidance response and cell-cell adhesion, the interaction between NEO1/Neogenin and RGMa and RGMb induces a chemorepulsive response.

**Summary**, from NCBI Gene [4756](https://www.ncbi.nlm.nih.gov/gene/4756):

> This gene encodes a cell surface protein that is a member of the immunoglobulin superfamily. The encoded protein consists of four N-terminal immunoglobulin-like domains, six fibronectin type III domains, a transmembrane domain and a C-terminal internal domain that shares homology with the tumor suppressor candidate gene DCC. This protein may be involved in cell growth and differentiation and in cell-cell adhesion. Defects in this gene are associated with cell proliferation in certain cancers. …

**Accessions** — [HGNC:7754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7754) · Entrez [4756](https://www.ncbi.nlm.nih.gov/gene/4756) · UniProt [Q92859](https://www.uniprot.org/uniprotkb/Q92859) · Ensembl [ENSG00000067141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067141)

## Data

Gene col 851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 851); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 851]; `tensor/DDL_lfc|DDL_z.npy` [851]; `embed/gene_vectors.npy` [851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 851 or target_col == 851). Every well: [[NEO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
