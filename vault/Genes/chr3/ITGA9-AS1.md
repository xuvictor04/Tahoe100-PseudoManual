---
symbol: "ITGA9-AS1"
type: "gene"
col: 14008
ensembl_id: "ENSG00000235257"
name: "ITGA9 antisense RNA 1"
location: "3p22.2"
module: 46
arm: "+"
pooled_cpm: 12.83
n_lines_expressing: 44
n_dd_up: 2
n_dd_down: 46
n_dd_up_clean: 2
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ITGA9-AS1

*ITGA9 antisense RNA 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.57× (z +4.8, q 9e-04, up in 22 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.212× (z -23.2, q 0e+00, down in 36 of 40 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTDSPL]] (+0.66, fdr 7e-06, ⚠ same locus), [[GOLGA2P5-1]] (+0.58, fdr 4e-05), [[TSPOAP1-AS1]] (+0.57, fdr 4e-05), [[XNDC1N]] (+0.54, fdr 9e-05); moves opposite to [[SLFN11]] (-0.51, fdr 1e-04), [[SFMBT2]] (-0.47, fdr 2e-04), [[EBF2]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NGFR]] → it (grade B ⚠); 4 go from it, the strongest it → [[NGFR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.57×** | +4.8 | 9e-04 | 22/42 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.009 | 11/40 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.4 | 0.11 | 3/42 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.43× | +3.3 | 0.11 | 4/40 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.36× | +3.3 | 0.11 | 14/42 (RKO, BT-474, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.17 | 8/42 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.22× | +3.0 | 0.17 | 15/40 (COLO 205, BT-474, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.17 | 7/38 (COLO 205, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.212×** | -23.2 | 0e+00 | 36/40 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.194×** | -17.3 | 0e+00 | 36/41 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.191×** | -16.8 | 0e+00 | 37/40 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.252×** | -14.6 | 0e+00 | 31/37 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.262×** | -14.1 | 3e-43 | 36/40 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.307×** | -12.5 | 1e-33 | 36/40 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.312×** | -12.3 | 6e-33 | 35/40 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.339×** | -11.4 | 2e-28 | 37/41 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.388×** | -10.0 | 1e-21 | 34/38 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.536×** | -9.3 | 8e-19 | 26/41 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.447×** | -8.5 | 1e-15 | 33/40 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.467×** | -8.0 | 5e-14 | 32/40 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.481×** | -7.7 | 5e-13 | 27/39 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.305×** | -6.6 | 2e-09 | 25/40 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.650×** | -6.4 | 5e-09 | 26/40 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.544×** | -6.4 | 5e-09 | 26/41 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.549×** | -6.3 | 9e-09 | 23/39 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.562×** | -6.1 | 4e-08 | 21/40 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.337×** | -6.0 | 5e-08 | 23/37 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.577×** | -5.8 | 2e-07 | 20/38 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.1 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -22.2) |
| [[LoVo (line)]] | wt | 14.6 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -13.5) |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0775× (z -19.1) |
| [[SK-MEL-2 (line)]] | alt | 46.8 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0757× (z -23.0) |
| [[SW48 (line)]] | wt | 46.4 | 0 | 9 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0450× (z -15.0) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0579× (z -21.3) |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 35.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -20.0) |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0657× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0607× (z -11.7) |
| [[SW1417 (line)]] | alt | 39.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -22.2) |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 5 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0526× (z -11.6) |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0725× (z -11.7) |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 5 | — | [[Harringtonine (drug)]] 0.5 µM 0.0497× (z -14.4) |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0602× (z -12.0) |
| [[C32 (line)]] | wt | 14.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.5) |
| [[HOP62 (line)]] | alt | 8.35 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -10.7) |
| [[KATO III (line)]] | alt | 14.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -13.9) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0996× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0801× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.2) |
| [[A498 (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.1) |
| [[BT-474 (line)]] | alt | 6.56 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0809× (z -8.6) |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0637× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 6.53 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.109× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 4.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0767× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 4.60 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.171× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0700× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTDSPL]] | +0.66 | +0.68 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[GOLGA2P5-1]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[TSPOAP1-AS1]] | +0.57 | +0.55 / +0.42 | both halves | 4e-05 | same gene group |
| [[XNDC1N]] | +0.54 | +0.37 / +0.57 | both halves | 9e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.52 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[GOLGA2P5]] | +0.50 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[TSPOAP1]] | +0.50 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[BDH1]] | +0.50 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[NDUFAF6]] | +0.49 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[PPP1R15B-AS1]] | +0.49 | +0.37 / +0.40 | both halves | 7e-05 | same gene group |
| [[LAMTOR5-AS1]] | +0.49 | +0.32 / +0.43 | both halves | 2e-04 | same gene group |
| [[OVOL2]] | +0.49 | +0.45 / +0.21 | both halves | 7e-04 |  |
| [[VSIG10]] | +0.48 | +0.41 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLFN11]] | -0.51 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[SFMBT2]] | -0.47 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[EBF2]] | -0.47 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[DDIT4L]] | -0.47 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[MICU3]] | -0.46 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[LGSN]] | -0.46 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[NEFL]] | -0.46 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[ELL2]] | -0.46 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[PPP2R5B]] | -0.46 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[HPF1]] | -0.45 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[ALAS1]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[SEMA6A]] | -0.44 | -0.23 / -0.52 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NGFR]] | B | NGFR activity raises ITGA9-AS1's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.06× lower at baseline in the lines without NGFR | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[TRPV4]] | B | TRPV4 activity raises ITGA9-AS1's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.63× lower at baseline in the lines without TRPV4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[B3GAT1-DT]] | B | B3GAT1-DT activity raises ITGA9-AS1's level | lines that do not express B3GAT1-DT (33) vs lines expressing it (17) | 1.59× lower at baseline in the lines without B3GAT1-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000213981, HEPHL1, ENSG00000287069 |
| [[CTDSPL]] | C | CTDSPL activity raises ITGA9-AS1's level | lines that do not express CTDSPL (5) vs lines expressing it (45) | 3.74× lower at baseline in the lines without CTDSPL | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGA9-AS1, SLC43A2, PLAAT3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NGFR]] | B | ITGA9-AS1 activity raises NGFR's level | lines that do not express ITGA9-AS1 (6) vs lines expressing it (44) | 2.54× lower at baseline in the lines without ITGA9-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CTDSPL, SLC43A2; maybe low, not absent |
| [[PIGZ]] | B | ITGA9-AS1 activity raises PIGZ's level | lines that do not express ITGA9-AS1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without ITGA9-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CTDSPL, SLC43A2; maybe low, not absent |
| [[BCAR3-AS1]] | B | ITGA9-AS1 activity lowers BCAR3-AS1's level | lines that do not express ITGA9-AS1 (6) vs lines expressing it (44) | 1.20× higher at baseline in the lines without ITGA9-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: CTDSPL, SLC43A2; maybe low, not absent |
| [[CTDSPL]] | C | ITGA9-AS1 activity raises CTDSPL's level | lines that do not express ITGA9-AS1 (6) vs lines expressing it (44) | 3.99× lower at baseline in the lines without ITGA9-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CTDSPL, SLC43A2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.335). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.8, 28.6); signed map (37.5, -15.8). **Vector** length 82.4, 19.4% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +0.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +1.7 | -6.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +4.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -12.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -16.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ITGA9 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p22.2 — chr3:37,693,655-37,861,802 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49668) · Entrez [101928153](https://www.ncbi.nlm.nih.gov/gene/101928153) · Ensembl [ENSG00000235257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235257)

## Data

Gene col 14008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14008); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14008]; `tensor/DDL_lfc|DDL_z.npy` [14008]; `embed/gene_vectors.npy` [14008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14008 or target_col == 14008). Every well: [[ITGA9-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA9-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
