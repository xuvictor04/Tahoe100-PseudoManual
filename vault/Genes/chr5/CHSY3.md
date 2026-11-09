---
symbol: "CHSY3"
type: "gene"
col: 12532
ensembl_id: "ENSG00000198108"
name: "chondroitin sulfate synthase 3"
location: "5q23.3"
module: 19
arm: "+"
pooled_cpm: 28.85
n_lines_expressing: 27
n_dd_up: 16
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CHSY3

*chondroitin sulfate synthase 3* — 5q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.59× (z +21.4, q 0e+00, up in 24 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.578× (z -6.4, q 6e-08, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLI3]] (+0.50, fdr 3e-05), [[GPR135]] (+0.50, fdr 3e-05), [[ITGA4]] (+0.49, fdr 6e-05); moves opposite to [[FIG4]] (-0.52, fdr 1e-05), [[UBXN2B]] (-0.46, fdr 1e-04), [[LPIN3]] (-0.45, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[PPRC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.59×** | +21.4 | 0e+00 | 24/25 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +10.5 | 2e-23 | 16/25 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +9.2 | 8e-18 | 7/24 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.36×** | +8.2 | 3e-14 | 18/24 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.7 | 2e-09 | 6/24 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.78×** | +6.6 | 5e-09 | 13/24 (H4, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.65×** | +5.7 | 1e-06 | 6/19 (C32, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +5.7 | 1e-06 | 11/24 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.3 | 7e-06 | 5/25 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.32×** | +5.2 | 1e-05 | 16/25 (LoVo, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.45×** | +4.4 | 5e-04 | 10/24 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.41×** | +4.1 | 0.002 | 13/24 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.40×** | +4.0 | 0.003 | 8/24 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.8 | 0.006 | 9/19 (SK-MEL-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.009 | 13/24 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Penfluridol (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.067 | 8/24 (HEC-1-A, J82, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.072 | 6/25 (HOP62, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.578×** | -6.4 | 6e-08 | 14/24 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -5.4 | 1e-05 | 17/24 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.632×** | -5.4 | 1e-05 | 16/24 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.733×** | -5.1 | 4e-05 | 13/25 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -4.7 | 3e-04 | 16/24 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.781×** | -4.1 | 0.004 | 14/25 (LoVo, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -3.9 | 0.007 | 16/24 (A498, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.708×** | -3.9 | 0.007 | 8/25 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.534×** | -3.9 | 0.007 | 11/24 (hTERT-HPNE, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -3.8 | 0.007 | 17/24 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.718×** | -3.7 | 0.009 | 9/24 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | **0.800×** | -3.7 | 0.010 | 6/25 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.733×** | -3.7 | 0.011 | 14/24 (NCI-H1573, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.748×** | -3.4 | 0.026 | 4/24 (RPMI-7951, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.772×** | -3.0 | 0.094 | 13/24 (LoVo, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -3.0 | 0.096 | 10/24 (A498, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 102 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.137× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 162 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -10.8) |
| [[LoVo (line)]] | wt | 73.9 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -11.7) |
| [[H4 (line)]] | wt | 28.5 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.59× (z +10.4) | [[Harringtonine (drug)]] 0.05 µM 0.0664× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.153× (z -8.7) |
| [[J82 (line)]] | alt | 32.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 8.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.134× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 29.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +11.3) | — |
| [[C32 (line)]] | wt | 20.7 | 1 | 0 | [[Cobimetinib (drug)]] 0.5 µM 7.72× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.30× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -8.8) ⚠ cell-cycle shift, explains ~69% of this change |
| [[Panc 03.27 (line)]] | alt | 26.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 9.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.01× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +8.7) | — |
| [[A-172 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLI3]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[GPR135]] | +0.50 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[ITGA4]] | +0.49 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[DOK6]] | +0.49 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[PDE3A]] | +0.48 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[L3HYPDH]] | +0.47 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[DOCK10]] | +0.46 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[PRKACB]] | +0.45 | +0.40 / +0.38 | both halves | 7e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[RHOBTB1]] | +0.45 | +0.42 / +0.38 | both halves | 7e-05 |  |
| [[CDH11]] | +0.45 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[NTNG1]] | +0.45 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[CDH7]] | +0.45 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIG4]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[UBXN2B]] | -0.46 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[LPIN3]] | -0.45 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[RABGAP1]] | -0.41 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[TMEM184C]] | -0.41 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[VPS41]] | -0.41 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[RRAGD]] | -0.41 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[HSDL1]] | -0.41 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[DHX40]] | -0.41 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[PREPL]] | -0.41 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[CASP9]] | -0.40 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[SNX2]] | -0.39 | -0.29 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHSY3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01508]] | B | LINC01508 activity raises CHSY3's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 2.56× lower at baseline in the lines without LINC01508 | 0.0996 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX |
| [[C5orf46]] | C | C5orf46 activity raises CHSY3's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 3.85× lower at baseline in the lines without C5orf46 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[GLI3]] | C | GLI3 activity raises CHSY3's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 3.53× lower at baseline in the lines without GLI3 | 0.071 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2; co-absent with the target |
| [[NID2]] | C | NID2 activity raises CHSY3's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.92× lower at baseline in the lines without NID2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises CHSY3's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.54× lower at baseline in the lines without SEMA5A | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPRC1]] | B | CHSY3 activity lowers PPRC1's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 1.27× higher at baseline in the lines without CHSY3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5 |
| [[HNRNPAB]] | B | CHSY3 activity lowers HNRNPAB's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 1.45× higher at baseline in the lines without CHSY3 | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5 |
| [[NID2]] | C | CHSY3 activity raises NID2's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 3.24× lower at baseline in the lines without CHSY3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |
| [[SEMA5A]] | C | CHSY3 activity raises SEMA5A's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 5.12× lower at baseline in the lines without CHSY3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |
| [[C5orf46]] | C | CHSY3 activity raises C5orf46's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 1.95× lower at baseline in the lines without CHSY3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |
| [[ITGA4]] | C | CHSY3 activity raises ITGA4's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 5.36× lower at baseline in the lines without CHSY3 | 0.058 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |
| [[NRP2]] | C | CHSY3 activity raises NRP2's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 3.63× lower at baseline in the lines without CHSY3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |
| [[TDO2]] | C | CHSY3 activity raises TDO2's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 2.31× lower at baseline in the lines without CHSY3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.395). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.9, 24.0); signed map (36.2, 45.4). **Vector** length 76.5, 23.3% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +21.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -0.2 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +1.2 | +2.6 |
|  | [[Busulfan (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.0 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.1 | -4.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.7 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.3 | +4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | chondroitin sulfate synthase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.3 — chr5:129,904,465-130,186,634 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSS3, CHSY-2 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases; Beta 3-glycosyltransferases |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70JA7](https://www.uniprot.org/uniprotkb/Q70JA7) (Chondroitin sulfate synthase 3):

> Catalytic component of CHSY3-CHPF2 and CHSY3-CHPF chondroitin sulfate synthase complexes. Has both beta-1,3-glucuronic acid and beta-1,4-N-acetylgalactosamine transferase activity. Transfers glucuronic acid (GlcUA) from UDP-GlcUA and N-acetylgalactosamine (GalNAc) from UDP-GalNAc to the non-reducing end of the elongating chondroitin polymer. Specific activity is much reduced compared to CHSY1.

**Summary**, from NCBI Gene [337876](https://www.ncbi.nlm.nih.gov/gene/337876):

> CSS3 is a glycosyltransferase that has both glucuronyltransferase and N-acetylgalactosaminyltransferase activities (Yada et al., 2003 [PubMed 12907687]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24293) · Entrez [337876](https://www.ncbi.nlm.nih.gov/gene/337876) · UniProt [Q70JA7](https://www.uniprot.org/uniprotkb/Q70JA7) · Ensembl [ENSG00000198108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198108)

## Data

Gene col 12532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12532); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12532]; `tensor/DDL_lfc|DDL_z.npy` [12532]; `embed/gene_vectors.npy` [12532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12532 or target_col == 12532). Every well: [[CHSY3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHSY3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
