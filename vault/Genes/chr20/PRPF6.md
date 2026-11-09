---
symbol: "PRPF6"
type: "gene"
col: 2083
ensembl_id: "ENSG00000101161"
name: "pre-mRNA processing factor 6"
location: "20q13.33"
module: 12
arm: "+"
pooled_cpm: 107.45
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PRPF6

*pre-mRNA processing factor 6* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.82× (z +19.9, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.686× (z -12.9, q 2e-35, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IK]] (+0.72, fdr 7e-06), [[CINP]] (+0.71, fdr 7e-06), [[ZNF205]] (+0.70, fdr 1e-05); moves opposite to [[PGRMC1]] (-0.58, fdr 1e-05), [[HPRT1]] (-0.55, fdr 1e-05), [[ATP11C]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.82×** | +19.9 | 0e+00 | 49/49 (SW480, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +11.5 | 2e-28 | 43/48 (SW480, BT-474, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.39×** | +11.3 | 2e-27 | 37/48 (LoVo, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +8.8 | 2e-16 | 35/48 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +6.5 | 1e-08 | 33/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +6.1 | 1e-07 | 31/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 1e-04 | 25/47 (SW1417, BT-474, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +4.7 | 2e-04 | 33/47 (MIA PaCa-2, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | 1.18× | +4.1 | 0.003 | 20/48 (Panc 03.27, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.19× | +4.0 | 0.004 | 18/48 (RKO, A-427, …) | rises with dose | composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 24/49 (SW1417, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.009 | 17/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.014 | 21/48 (LOX-IMVI, NCI-H460, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.020 | 20/48 (CHP-212, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -12.9 | 2e-35 | 42/49 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -8.2 | 6e-14 | 28/44 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -7.1 | 2e-10 | 35/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -6.3 | 4e-08 | 32/50 (SK-MEL-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -6.1 | 9e-08 | 25/48 (HOP62, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.823×** | -4.7 | 2e-04 | 23/49 (Hs 766T, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.2 | 0.002 | 21/48 (NCI-H460, AsPC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.886× | -4.2 | 0.002 | 19/48 (MIA PaCa-2, SNU-423, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -3.9 | 0.007 | 6/48 (A498, Hs 766T, …) | two highest doses |  |
| [[Irinotecan (drug)]] 0.5 µM |  | 0.837× | -3.1 | 0.11 | 6/48 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 172 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.34× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -10.3) |
| [[RKO (line)]] | wt | 94.0 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.0× (z +14.7) | — |
| [[SW480 (line)]] | alt | 106 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.33× (z +17.5) | — |
| [[HOP62 (line)]] | alt | 96.3 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 7.63× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -14.8) |
| [[BT-474 (line)]] | alt | 111 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 7.87× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 82.6 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.46× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 74.5 | 3 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 5.64× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -10.1) |
| [[SW1417 (line)]] | alt | 215 | 3 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.32× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 90.3 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 3.86× (z +9.9) | — |
| [[LoVo (line)]] | wt | 75.4 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 9.02× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 96.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.45× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 112 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.95× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.4) |
| [[A-172 (line)]] | wt | 78.1 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.16× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.629× (z -8.5) |
| [[A-427 (line)]] | wt | 87.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.72× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -18.3) |
| [[HCT15 (line)]] | alt | 103 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -11.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 180 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.38× (z +15.5) | — |
| [[HS-578T (line)]] | alt | 88.2 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.48× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.3) |
| [[LS 180 (line)]] | wt | 80.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.37× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.64× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 79.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.22× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 174 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.28× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.519× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 134 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 101 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.48× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.6) |
| [[SW 900 (line)]] | alt | 132 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.90× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -12.0) |
| [[A549 (line)]] | wt | 81.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.82× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 133 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.24× (z +10.4) | — |
| [[C32 (line)]] | wt | 81.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 103 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.93× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 102 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 19.3× (z +14.0) | — |
| [[H4 (line)]] | wt | 93.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.77× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 132 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.17× (z +11.1) | — |
| [[J82 (line)]] | alt | 96.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.497× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[NCI-H2030 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 93.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.01× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.0914× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -8.7) |
| [[PANC-1 (line)]] | alt | 100 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.54× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 197 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.34× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 112 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -8.8) |
| [[A498 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 91.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IK]] | +0.72 | +0.75 / +0.59 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 995 |
| [[CINP]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.70 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[DIABLO]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ESS2]] | +0.69 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[DRG1]] | +0.69 | +0.78 / +0.49 | both halves | 1e-05 |  |
| [[VIRMA]] | +0.68 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[SF3A2]] | +0.68 | +0.74 / +0.57 | both halves | 8e-06 | pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[RNF40]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PRPF3]] | +0.66 | +0.66 / +0.49 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[DDX55]] | +0.66 | +0.71 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGRMC1]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[HPRT1]] | -0.55 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ATP11C]] | -0.54 | -0.51 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRPF6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.5, -5.5); signed map (-14.6, -11.5). **Vector** length 129, 37.4% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.6 | +19.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.4 | +11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.1 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +8.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +3.6 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +3.1 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -12.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.6 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,981,132-64,033,100 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TOM, bB152O15.1, ANT-1, U5-102K, Prp6, hPrp6, SNRNP102, RP60; previously C20orf14 |
| Gene groups (HGNC) | U5 small nuclear ribonucleoprotein |
| Reactome | 8 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing - Major Pathway; mRNA Splicing |
| Matched by | ensembl_id |

**Function**, from UniProt [O94906](https://www.uniprot.org/uniprotkb/O94906) (Pre-mRNA-processing factor 6):

> Involved in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex, one of the building blocks of the spliceosome. Enhances dihydrotestosterone-induced transactivation activity of AR, as well as dexamethasone-induced transactivation activity of NR3C1, but does not affect estrogen-induced transactivation.

**Summary**, from NCBI Gene [24148](https://www.ncbi.nlm.nih.gov/gene/24148):

> The protein encoded by this gene appears to be involved in pre-mRNA splicing, possibly acting as a bridging factor between U5 and U4/U6 snRNPs in formation of the spliceosome. The encoded protein also can bind androgen receptor, providing a link between transcriptional activation and splicing. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15860) · Entrez [24148](https://www.ncbi.nlm.nih.gov/gene/24148) · UniProt [O94906](https://www.uniprot.org/uniprotkb/O94906) · Ensembl [ENSG00000101161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101161)

## Data

Gene col 2083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2083); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2083]; `tensor/DDL_lfc|DDL_z.npy` [2083]; `embed/gene_vectors.npy` [2083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2083 or target_col == 2083). Every well: [[PRPF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
