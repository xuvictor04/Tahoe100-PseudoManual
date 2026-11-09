---
symbol: "CCNC"
type: "gene"
col: 3340
ensembl_id: "ENSG00000112237"
name: "cyclin C"
location: "6q16.2"
module: 17
arm: "+"
pooled_cpm: 91.98
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CCNC

*cyclin C* — 6q16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +26.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.920× (z -7.5, q 4e-11, down in 1 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.823× (z -7.3, q 1e-10, down in 29 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Panc 03.27 0.555×, LS 180 0.593×, LoVo 0.690×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMCX5]] (+0.68, fdr 7e-06), [[APOOL]] (+0.64, fdr 1e-05), [[MOCS2]] (+0.64, fdr 7e-06); moves opposite to [[IFT140]] (-0.54, fdr 4e-05), [[SIN3A]] (-0.53, fdr 1e-05), [[S100PBP]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RBM11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +26.3 | 0e+00 | 48/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +17.5 | 0e+00 | 44/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.74×** | +14.6 | 0e+00 | 43/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +14.6 | 0e+00 | 44/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +13.9 | 4e-42 | 43/48 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +13.5 | 1e-39 | 41/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +13.3 | 1e-38 | 43/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.43×** | +9.5 | 1e-19 | 33/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +9.4 | 4e-19 | 28/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +8.7 | 1e-16 | 29/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.36×** | +7.7 | 5e-13 | 26/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.33×** | +7.5 | 4e-12 | 31/49 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +7.3 | 9e-12 | 36/49 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.31×** | +7.1 | 4e-11 | 26/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.30×** | +6.8 | 4e-10 | 28/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.44×** | +5.0 | 2e-05 | 25/48 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +4.9 | 3e-05 | 25/48 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 3e-05 | 29/49 (NCI-H2347, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +4.4 | 3e-04 | 20/48 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.001 | 18/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.001 | 21/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.003 | 13/49 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3340.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Panc 03.27 0.555×, LS 180 0.593×, LoVo 0.690×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -7.5 | 4e-11 | 1/50 (H4) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -7.3 | 1e-10 | 29/49 (Panc 03.27, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 0.875× | -3.5 | 0.060 | 11/48 (SW480, LoVo, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.875× | -3.5 | 0.060 | 7/49 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.778×** | -3.5 | 0.060 | 17/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 81.7 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +22.6) | — |
| [[SW480 (line)]] | alt | 130 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 68.7 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +16.3) | — |
| [[LoVo (line)]] | wt | 171 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +18.8) | — |
| [[HOP62 (line)]] | alt | 62.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +20.3) | — |
| [[HEC-1-A (line)]] | alt | 131 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.4) | — |
| [[KATO III (line)]] | alt | 154 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 165 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.96× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 98.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.5) | — |
| [[NCI-H1792 (line)]] | alt | 61.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.8) | — |
| [[A498 (line)]] | wt | 39.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.6) | — |
| [[A549 (line)]] | wt | 56.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 110 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 66.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 72.4 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +14.9) | — |
| [[SK-MEL-2 (line)]] | alt | 86.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 145 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.8) | — |
| [[A-172 (line)]] | wt | 51.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.2) | — |
| [[A-427 (line)]] | wt | 81.2 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.21× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 62.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.2) | — |
| [[C32 (line)]] | wt | 69.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 56.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 144 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 82.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.0) | — |
| [[NCI-H2030 (line)]] | alt | 51.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 73.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 127 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -11.5) |
| [[RKO (line)]] | wt | 114 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 68.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 80.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.4) | — |
| [[H4 (line)]] | wt | 58.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 61.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.0) | — |
| [[J82 (line)]] | alt | 75.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.6) | — |
| [[SW48 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX5]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[APOOL]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[MOCS2]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TTC1]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[RPAP3]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MAP9]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MRPL47]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[DDX1]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[MMADHC]] | +0.56 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[MRPS9]] | +0.55 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[LYPLAL1]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CEP290]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT140]] | -0.54 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[SIN3A]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[S100PBP]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TAF5]] | -0.50 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[NHEJ1]] | -0.48 | -0.26 / -0.56 | both halves | 3e-04 |  |
| [[LINC01128]] | -0.48 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[CTBP2]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MSL1]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LEMD3]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[CRAMP1]] | -0.47 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[ANKMY1]] | -0.47 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[POC1A]] | -0.47 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM11]] | B | RBM11 activity raises CCNC's level | lines that do not express RBM11 (25) vs lines expressing it (25) | 1.06× lower at baseline in the lines without RBM11 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ANKRD20A11P, VWDE |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.444). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-21.5, -0.3); signed map (-22.6, -20.0). **Vector** length 90.3, 23.8% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +13.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +13.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +26.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +4.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -7.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~84% of this change | -4.5 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +4.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | +1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.2 — chr6:99,542,387-99,568,825 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CycC |
| Gene groups (HGNC) | Cyclins; Mediator complex |
| Reactome | 26 pathways, smallest: SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription; NOTCH1 Intracellular Domain Regulates Transcription; Transcriptional activity of SMAD2/SMAD3:SMAD4 heterotrimer |
| Matched by | ensembl_id |

**Function**, from UniProt [P24863](https://www.uniprot.org/uniprotkb/P24863) (Cyclin-C):

> Component of the Mediator complex, a coactivator involved in regulated gene transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [892](https://www.ncbi.nlm.nih.gov/gene/892):

> The protein encoded by this gene is a member of the cyclin family of proteins. The encoded protein interacts with cyclin-dependent kinase 8 and induces the phophorylation of the carboxy-terminal domain of the large subunit of RNA polymerase II. The level of mRNAs for this gene peaks in the G1 phase of the cell cycle. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1581) · Entrez [892](https://www.ncbi.nlm.nih.gov/gene/892) · UniProt [P24863](https://www.uniprot.org/uniprotkb/P24863) · Ensembl [ENSG00000112237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112237)

## Data

Gene col 3340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3340); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3340]; `tensor/DDL_lfc|DDL_z.npy` [3340]; `embed/gene_vectors.npy` [3340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3340 or target_col == 3340). Every well: [[CCNC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
