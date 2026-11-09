---
symbol: "EIF4B"
type: "gene"
col: 718
ensembl_id: "ENSG00000063046"
name: "eukaryotic translation initiation factor 4B"
location: "12q13.13"
module: 20
arm: "+"
pooled_cpm: 201.46
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EIF4B

*eukaryotic translation initiation factor 4B* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 4.17× (z +14.0, q 1e-41, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.636× (z -8.4, q 2e-14, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 0.735× (z -3.7, q 0.016, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1A1]] (+0.68, fdr 7e-06), [[RPS3A]] (+0.64, fdr 1e-05), [[EIF3C]] (+0.64, fdr 1e-05); moves opposite to [[TRAPPC4]] (-0.61, fdr 2e-05), [[PLIN3]] (-0.52, fdr 9e-05), [[CDKN2D]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **4.17×** | +14.0 | 1e-41 | 47/48 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.06×** | +13.7 | 3e-40 | 48/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.9 | 2e-04 | 31/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.4 | 0.001 | 27/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.4 | 0.001 | 32/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.027 | 25/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.041 | 25/48 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.057 | 22/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.18× | +3.0 | 0.16 | 22/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.636×** | -8.4 | 2e-14 | 45/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.642×** | -8.3 | 4e-14 | 44/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.675×** | -7.3 | 4e-11 | 42/48 (NCI-H23, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.827×** | -5.0 | 9e-05 | 23/49 (A498, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.796×** | -4.2 | 0.003 | 32/48 (SW1417, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.810×** | -3.9 | 0.008 | 31/48 (A498, SW1417, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.800×** | -3.7 | 0.016 | 35/49 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.735×** | -3.7 | 0.016 | 33/48 (Hs 766T, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.811×** | -3.6 | 0.020 | 27/47 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.822×** | -3.5 | 0.025 | 23/48 (NCI-H460, A498, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.812×** | -3.5 | 0.025 | 32/49 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.828×** | -3.3 | 0.043 | 24/48 (AN3 CA, J82, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.773×** | -3.1 | 0.091 | 26/47 (C-33 A, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 222 | 5 (3 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.19× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 162 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.95× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 310 | 4 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.20× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 204 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.13× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.525× (z -9.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 358 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.96× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.545× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 301 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.10× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 323 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.06× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.527× (z -9.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 195 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.03× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 176 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.85× (z +12.5) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.185× (z -9.6) ⚠ toxic |
| [[J82 (line)]] | alt | 147 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.54× (z +11.3) | [[Belinostat (drug)]] 5 µM 0.526× (z -9.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 227 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.57× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 213 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.74× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.545× (z -9.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 98.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.74× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 176 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.34× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 139 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.77× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 127 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.08× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 209 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.94× (z +11.8) | — |
| [[KATO III (line)]] | alt | 211 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.55× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 140 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.95× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 210 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.39× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 174 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.22× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 191 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.83× (z +12.0) | — |
| [[RKO (line)]] | wt | 244 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.42× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 121 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.75× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 258 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.80× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 193 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.40× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 163 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.65× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 199 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.48× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 242 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.59× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 163 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.29× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 281 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.70× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 118 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.51× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 125 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.76× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 184 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.32× (z +8.8) | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.246× (z -10.9) |
| [[SHP-77 (line)]] | alt | 148 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.65× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 159 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.15× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 209 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 240 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 164 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 294 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 288 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1A1]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 | STRING 588 |
| [[RPS3A]] | +0.64 | +0.54 / +0.74 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 518 |
| [[EIF3C]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 813 |
| [[RPL6]] | +0.62 | +0.55 / +0.67 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 435 |
| [[NPM1]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RPS9]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 655 |
| [[EIF3D]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 666 |
| [[RPL3]] | +0.61 | +0.63 / +0.73 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 540 |
| [[MATR3]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[U2AF2]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 | same gene group |
| [[MRRF]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[RPSA]] | +0.60 | +0.49 / +0.69 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 563 |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC4]] | -0.61 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[PLIN3]] | -0.52 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[CDKN2D]] | -0.51 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[CIB1]] | -0.51 | -0.23 / -0.60 | both halves | 5e-04 |  |
| [[ORAI1]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TUBB4B]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 | pathway: M-decay: degradation of maternal mRNAs by maternally stored factors |
| [[KATNBL1]] | -0.50 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[FAM89B]] | -0.49 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[SH3BGRL3]] | -0.49 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[ISG20]] | -0.49 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ERVK3-1]] | -0.48 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ORMDL2]] | -0.48 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.6, -24.9); signed map (-22.8, -34.2). **Vector** length 124, 39.7% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.59 to 10); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.55 to 10); *Peptide chain elongation* (reactome, mean cos +0.59 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.2 | +13.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.9 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.6 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | -0.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.4 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.3 | +1.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | -0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.7 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.5 | -7.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.2 | -2.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.9 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,006,282-53,042,215 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 16 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; mTORC1-mediated signalling; Deadenylation of mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P23588](https://www.uniprot.org/uniprotkb/P23588) (Eukaryotic translation initiation factor 4B):

> Required for the binding of mRNA to ribosomes. Functions in close association with EIF4-F and EIF4-A. Binds near the 5'-terminal cap of mRNA in presence of EIF-4F and ATP. Promotes the ATPase activity and the ATP-dependent RNA unwinding activity of both EIF4-A and EIF4-F.

**Summary**, from NCBI Gene [1975](https://www.ncbi.nlm.nih.gov/gene/1975):

> Enables RNA binding activity. Predicted to be involved in regulation of translational initiation. Predicted to be located in cytosol. Predicted to be part of eukaryotic translation initiation factor 4F complex. Predicted to be active in nucleus and postsynapse. Biomarker of autism spectrum disorder and major depressive disorder. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3285) · Entrez [1975](https://www.ncbi.nlm.nih.gov/gene/1975) · UniProt [P23588](https://www.uniprot.org/uniprotkb/P23588) · Ensembl [ENSG00000063046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063046)

## Data

Gene col 718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 718); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 718]; `tensor/DDL_lfc|DDL_z.npy` [718]; `embed/gene_vectors.npy` [718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 718 or target_col == 718). Every well: [[EIF4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
