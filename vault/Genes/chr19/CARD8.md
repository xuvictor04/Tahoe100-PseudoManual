---
symbol: "CARD8"
type: "gene"
col: 2609
ensembl_id: "ENSG00000105483"
name: "caspase recruitment domain family member 8"
location: "19q13.33"
module: 88
arm: "+"
pooled_cpm: 27.66
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# CARD8

*caspase recruitment domain family member 8* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.21× (z +4.5, q 0.003, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.384× (z -16.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNRD2]] (+0.72, fdr 7e-06), [[RBM23]] (+0.69, fdr 2e-05), [[GABPB2]] (+0.69, fdr 8e-05); moves opposite to [[SLC29A4]] (-0.66, fdr 2e-05), [[METRN]] (-0.63, fdr 2e-05), [[ANKRD27]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[OTUD7A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.5 | 0.003 | 21/48 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.041 | 13/47 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.100 | 8/48 (RKO, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.21× | +3.2 | 0.19 | 7/48 (C-33 A, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.23 | 12/47 (C-33 A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.24 | 12/47 (A549, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.384×** | -16.3 | 0e+00 | 46/48 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.440×** | -14.0 | 8e-42 | 45/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.465×** | -13.0 | 2e-36 | 44/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.510×** | -11.5 | 3e-28 | 36/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -11.2 | 5e-27 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.522×** | -11.1 | 2e-26 | 43/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.525×** | -11.0 | 4e-26 | 41/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -9.3 | 1e-18 | 34/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -8.6 | 6e-16 | 41/48 (HT-29, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -8.0 | 7e-14 | 33/48 (H4, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.646×** | -7.2 | 4e-11 | 32/47 (SW480, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -7.1 | 7e-11 | 27/47 (SW480, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.660×** | -7.1 | 7e-11 | 28/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.482×** | -6.5 | 3e-09 | 30/48 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -6.2 | 3e-08 | 30/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.762×** | -4.6 | 1e-04 | 24/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.764×** | -4.6 | 1e-04 | 23/48 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.833×** | -4.4 | 3e-04 | 19/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.3 | 0 | 11 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -19.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 32.9 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.274× (z -12.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -11.3) |
| [[PANC-1 (line)]] | alt | 25.8 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.253× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 33.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.231× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 29.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.297× (z -10.6) |
| [[H4 (line)]] | wt | 42.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -13.7) |
| [[HCT15 (line)]] | alt | 48.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.173× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 37.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.317× (z -10.4) |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0933× (z -13.1) |
| [[SHP-77 (line)]] | alt | 30.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.242× (z -10.4) |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.214× (z -9.9) |
| [[A-427 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -12.8) ⚠ cell-cycle shift, explains ~58% of this change |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0701× (z -8.6) |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.212× (z -9.6) |
| [[C-33 A (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 31.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -8.6) |
| [[LoVo (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.319× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.298× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -10.4) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SW 1271 (line)]] | alt | 71.2 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0934× (z -8.6) |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.254× (z -9.4) |
| [[SW48 (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNRD2]] | +0.72 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[RBM23]] | +0.69 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[GABPB2]] | +0.69 | +0.69 / +0.37 | both halves | 8e-05 |  |
| [[CLHC1]] | +0.67 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[GTF2H1]] | +0.67 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ST7L]] | +0.65 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[WDR33]] | +0.65 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RCBTB2]] | +0.65 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[MEPCE]] | +0.64 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[RAB30-DT]] | +0.64 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[BRPF3]] | +0.64 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LATS1]] | +0.64 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC29A4]] | -0.66 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[METRN]] | -0.63 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD27]] | -0.62 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[LPCAT4]] | -0.62 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[TSEN54]] | -0.61 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[CTXN1]] | -0.61 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[TMEM120B]] | -0.60 | -0.64 / -0.27 | both halves | 3e-04 |  |
| [[SH3GL3]] | -0.59 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[RAP1A]] | -0.59 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[HEBP1]] | -0.58 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[ATP7B]] | -0.58 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[PDZD7]] | -0.58 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OTUD7A]] | B | OTUD7A activity raises CARD8's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without OTUD7A | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[ZNF254]] | B | ZNF254 activity raises CARD8's level | lines that do not express ZNF254 (6) vs lines expressing it (44) | 1.39× lower at baseline in the lines without ZNF254 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ZNF571, ZNF613 |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises CARD8's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-17.1, 8.3); signed map (17.1, -24.5). **Vector** length 86.2, 19.9% of its response variance represented; |z| ≥ 3 in 1,206 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.0 | -16.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.9 | -11.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -14.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -7.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | caspase recruitment domain family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,180,770-48,255,946 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TUCAN, KIAA0955, CARDINAL, NDPP, Dakar |
| Gene groups (HGNC) | Caspase recruitment domain containing |
| Reactome | 7 pathways, smallest: Formation of apoptosome; Regulation of the apoptosome activity; Cytochrome c-mediated apoptotic response |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G2](https://www.uniprot.org/uniprotkb/Q9Y2G2) (Caspase recruitment domain-containing protein 8):

> Inflammasome sensor, which mediates inflammasome activation in response to various pathogen-associated signals, leading to subsequent pyroptosis of CD4(+) T-cells and macrophages. Inflammasomes are supramolecular complexes that assemble in the cytosol in response to pathogens and other damage-associated signals and play critical roles in innate immunity and inflammation. Acts as a recognition receptor (PRR): recognizes specific pathogens and other damage-associated signals, such as HIV-1 …

**Summary**, from NCBI Gene [22900](https://www.ncbi.nlm.nih.gov/gene/22900):

> The protein encoded by this gene belongs to the caspase recruitment domain (CARD)-containing family of proteins, which are involved in pathways leading to activation of caspases or nuclear factor kappa-B (NFKB). This protein may be a component of the inflammasome, a protein complex that plays a role in the activation of proinflammatory caspases. It is thought that this protein acts as an adaptor molecule that negatively regulates NFKB activation, CASP1-dependent IL1B secretion, and apoptosis. …

**Accessions** — [HGNC:17057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17057) · Entrez [22900](https://www.ncbi.nlm.nih.gov/gene/22900) · UniProt [Q9Y2G2](https://www.uniprot.org/uniprotkb/Q9Y2G2) · Ensembl [ENSG00000105483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105483)

## Data

Gene col 2609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2609); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2609]; `tensor/DDL_lfc|DDL_z.npy` [2609]; `embed/gene_vectors.npy` [2609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2609 or target_col == 2609). Every well: [[CARD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
