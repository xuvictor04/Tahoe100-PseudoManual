---
symbol: "FH"
type: "gene"
col: 1664
ensembl_id: "ENSG00000091483"
name: "fumarate hydratase"
location: "1q43"
module: 25
arm: "+"
pooled_cpm: 18.62
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# FH

*fumarate hydratase* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +23.2, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.881× (z -7.5, q 3e-11, down in 8 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.648× (z -3.8, q 0.036, down in 10 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.209×, SNU-1 0.110×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0835×; ⚠ cell-cycle shift, would explain all of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (H4 0.0926×); [[Bexarotene (drug)]] 0.5 µM in 1 line (AN3 CA 0.0762×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPO]] (+0.69, fdr 7e-06), [[COPS3]] (+0.66, fdr 1e-05), [[DR1]] (+0.66, fdr 7e-06); moves opposite to [[MAP2K7]] (-0.68, fdr 7e-06), [[ZNF235]] (-0.65, fdr 1e-05), [[RPL18]] (-0.62, fdr 1e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[SEMA6C]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +23.2 | 0e+00 | 42/47 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +19.1 | 0e+00 | 45/46 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.78×** | +17.3 | 0e+00 | 43/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.73×** | +17.0 | 0e+00 | 34/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.59×** | +16.1 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.41×** | +14.9 | 0e+00 | 44/48 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.48×** | +14.8 | 0e+00 | 24/28 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.37×** | +13.5 | 1e-39 | 24/33 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +13.2 | 1e-37 | 39/47 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.14×** | +12.4 | 3e-33 | 37/47 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.04×** | +11.6 | 3e-29 | 35/46 (SW480, SK-MEL-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.89×** | +10.3 | 3e-23 | 36/46 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +8.2 | 1e-14 | 36/48 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +8.2 | 1e-14 | 32/46 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.4 | 4e-12 | 30/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.8 | 2e-07 | 19/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.6 | 7e-07 | 21/48 (HOP62, BT-474, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +5.5 | 1e-06 | 21/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.028 | 11/47 (PANC-1, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1664.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.209×, SNU-1 0.110×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0835×; ⚠ cell-cycle shift, would explain all of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (H4 0.0926×); [[Bexarotene (drug)]] 0.5 µM in 1 line (AN3 CA 0.0762×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.881× | -7.5 | 3e-11 | 8/48 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.648×** | -3.8 | 0.036 | 10/46 (C-33 A, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.752×** | -3.4 | 0.090 | 13/45 (C-33 A, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.866× | -3.4 | 0.090 | 7/48 (SK-MEL-2, Hs 766T, …) | rises with dose | position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | 0.821× | -3.2 | 0.14 | 1/47 (NCI-H2347) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.828× | -3.2 | 0.14 | 13/47 (LoVo, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.828× | -3.1 | 0.17 | 7/47 (NCI-H2030, A-427, …) | rises with dose | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.7 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 19.5 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.1) | — |
| [[SW480 (line)]] | alt | 20.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.0) | — |
| [[A-172 (line)]] | wt | 23.8 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.43× (z +9.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.65× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.4) | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0835× (z -9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Saquinavir (drug)]] 0.5 µM 0.0926× (z -9.1) |
| [[LoVo (line)]] | wt | 15.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +11.0) | — |
| [[A-427 (line)]] | wt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +8.6) | — |
| [[A549 (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 1 | — | [[Bexarotene (drug)]] 0.5 µM 0.0762× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +10.0) | — |
| [[C32 (line)]] | wt | 9.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 8.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.1) | — |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | +0.69 | +0.79 / +0.60 | both halves | 7e-06 | STRING 437 |
| [[COPS3]] | +0.66 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[DR1]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[POGLUT3]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[TOP2B]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[AKAP11]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TMEM237]] | +0.61 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[VARS1]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 | STRING 537 |
| [[ALG10B]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[OXCT1]] | +0.60 | +0.61 / +0.73 | both halves | 7e-06 | pathway: Mitochondrial protein degradation; STRING 488 |
| [[CENPH]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[PGM2]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 | STRING 464 |

## Genes that move opposite

*54 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2K7]] | -0.68 | -0.74 / -0.60 | both halves | 7e-06 |  |
| [[ZNF235]] | -0.65 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.62 | -0.56 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SEMA6C]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[HIC2]] | -0.61 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RPS19]] | -0.61 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.61 | -0.55 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ZNF611]] | -0.60 | -0.40 / -0.68 | both halves | 4e-05 |  |
| [[IGBP1]] | -0.60 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[RPS13]] ⚠ | -0.59 | -0.50 / -0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FAM182B]] | -0.59 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[RPL31]] | -0.59 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[PIAS4]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[RPL35A]] | -0.58 | -0.57 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CAV2]] | B | CAV2 activity lowers FH's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 1.23× higher at baseline in the lines without CAV2 | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-35.3, -23.4); signed map (-17.7, -40.3). **Vector** length 76.5, 16.3% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.7 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.6 | +13.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +3.9 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +23.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.6 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | fumarate hydratase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:241,497,511-241,519,799 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FUM |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Citric acid cycle (TCA cycle); Mitochondrial protein degradation; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P07954](https://www.uniprot.org/uniprotkb/P07954) (Fumarate hydratase, mitochondrial):

> Catalyzes the reversible stereospecific interconversion of fumarate to L-malate. Experiments in other species have demonstrated that specific isoforms of this protein act in defined pathways and favor one direction over the other (Probable).; [Isoform Mitochondrial]: Catalyzes the hydration of fumarate to L-malate in the tricarboxylic acid (TCA) cycle to facilitate a transition step in the production of energy in the form of NADH.; [Isoform Cytoplasmic]: Catalyzes the dehydration of L-malate to …

**Summary**, from NCBI Gene [2271](https://www.ncbi.nlm.nih.gov/gene/2271):

> The protein encoded by this gene is an enzymatic component of the tricarboxylic acid (TCA) cycle, or Krebs cycle, and catalyzes the formation of L-malate from fumarate. It exists in both a cytosolic form and an N-terminal extended form, differing only in the translation start site used. The N-terminal extended form is targeted to the mitochondrion, where the removal of the extension generates the same form as in the cytoplasm. It is similar to some thermostable class II fumarases and functions …

**Accessions** — [HGNC:3700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3700) · Entrez [2271](https://www.ncbi.nlm.nih.gov/gene/2271) · UniProt [P07954](https://www.uniprot.org/uniprotkb/P07954) · Ensembl [ENSG00000091483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091483)

## Data

Gene col 1664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1664); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1664]; `tensor/DDL_lfc|DDL_z.npy` [1664]; `embed/gene_vectors.npy` [1664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1664 or target_col == 1664). Every well: [[FH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
