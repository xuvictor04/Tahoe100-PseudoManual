---
symbol: "DICER1-AS1"
type: "gene"
col: 14033
ensembl_id: "ENSG00000235706"
name: "DICER1 antisense RNA 1"
location: "14q32.13"
module: 15
arm: "+"
pooled_cpm: 6.23
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 31
n_dd_up_clean: 22
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DICER1-AS1

*DICER1 antisense RNA 1* — 14q32.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +15.7, q 0e+00, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.348× (z -12.4, q 2e-32, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX59-AS1]] (+0.79, fdr 7e-06), [[SPESP1]] (+0.77, fdr 1e-05), [[AHI1-DT]] (+0.77, fdr 7e-06); moves opposite to [[EDA]] (-0.63, fdr 9e-05), [[GPRIN1]] (-0.62, fdr 2e-04), [[SH3PXD2B]] (-0.62, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +15.7 | 0e+00 | 38/43 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.84×** | +7.1 | 3e-10 | 25/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.5 | 2e-08 | 19/38 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +5.3 | 2e-05 | 16/43 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.8 | 1e-04 | 14/41 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.8 | 2e-04 | 13/48 (NCI-H2030, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +4.7 | 2e-04 | 10/47 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.49×** | +4.7 | 2e-04 | 12/47 (KATO III, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.63×** | +4.6 | 2e-04 | 14/44 (LoVo, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.001 | 7/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.28×** | +4.1 | 0.002 | 10/46 (SK-MEL-2, SW48, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.8 | 0.006 | 2/10 (HOP62, SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.008 | 9/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.012 | 7/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.39×** | +3.5 | 0.016 | 11/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.016 | 8/45 (SW480, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.019 | 8/47 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.020 | 7/47 (BT-474, C-33 A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14033.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.348×** | -12.4 | 2e-32 | 34/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.410×** | -10.5 | 4e-23 | 35/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.442×** | -9.6 | 2e-19 | 27/37 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.410×** | -8.5 | 3e-15 | 30/46 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.512×** | -7.9 | 4e-13 | 26/47 (SW480, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.561×** | -6.8 | 1e-09 | 26/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.357×** | -6.3 | 2e-08 | 21/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.516×** | -6.3 | 2e-08 | 22/47 (PANC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.520×** | -6.2 | 3e-08 | 21/46 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.593×** | -6.1 | 5e-08 | 20/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.600×** | -5.6 | 1e-06 | 18/43 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -4.7 | 1e-04 | 15/38 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.667×** | -4.6 | 2e-04 | 14/30 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.669×** | -4.5 | 2e-04 | 17/46 (NCI-H1792, HOP62, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.687×** | -4.4 | 4e-04 | 17/47 (SW480, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.627×** | -3.9 | 0.003 | 15/48 (SHP-77, SW 1271, …) | rises with dose | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.730×** | -3.7 | 0.008 | 9/47 (HS-578T, AN3 CA, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.554×** | -3.6 | 0.009 | 10/43 (Hs 766T, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.563×** | -3.5 | 0.012 | 10/37 (MIA PaCa-2, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.576×** | -3.4 | 0.020 | 12/35 (SW480, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.769×** | -3.1 | 0.048 | 7/47 (AN3 CA, NCI-H2030, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.761×** | -3.0 | 0.058 | 8/45 (RPMI-7951, J82, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.703×** | -3.0 | 0.061 | 11/41 (Hs 766T, NCI-H1792, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Decitabine (drug)]] 5 µM |  | **0.771×** | -2.9 | 0.061 | 6/43 (J82, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.5 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.196× (z -11.1) |
| [[A498 (line)]] | wt | 3.95 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0774× (z -9.8) |
| [[LoVo (line)]] | wt | 11.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 7.41 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.126× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 7.87 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0618× (z -10.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H2030 (line)]] | alt | 4.09 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +8.7) | — |
| [[A-172 (line)]] | wt | 4.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 4.80 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0781× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[LS 180 (line)]] | wt | 7.82 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.134× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 8.50 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.184× (z -9.4) |
| [[PANC-1 (line)]] | alt | 6.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 4.85 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0633× (z -8.9) |
| [[A-427 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX59-AS1]] | +0.79 | +0.78 / +0.67 | both halves | 7e-06 | same gene group |
| [[SPESP1]] | +0.77 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.77 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[NIFK-AS1]] | +0.77 | +0.73 / +0.62 | both halves | 7e-06 | same gene group |
| [[NSMCE1-DT]] | +0.75 | +0.83 / +0.41 | both halves | 4e-05 |  |
| [[OXA1L-DT]] | +0.75 | +0.80 / +0.40 | both halves | 5e-05 |  |
| [[PCMTD1-DT]] | +0.74 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[ZNF862]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[CDNF]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[GALNT7-DT]] | +0.73 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[HLA-DMA]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[DNAI4]] | +0.72 | +0.73 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDA]] | -0.63 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[GPRIN1]] | -0.62 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[SH3PXD2B]] | -0.62 | -0.57 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DICER1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises DICER1-AS1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.46× lower at baseline in the lines without ANKRD20A21P | 0.0995 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[C10orf95-AS1]] | C | C10orf95-AS1 activity raises DICER1-AS1's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises DICER1-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.65× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |
| [[LRRIQ3]] | C | LRRIQ3 activity raises DICER1-AS1's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.8, 20.0); signed map (28.3, -7.5). **Vector** length 66.1, 10.8% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +15.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +1.9 | -1.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +4.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.1 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -3.9 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -3.9 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | DICER1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q32.13 — chr14:95,157,645-95,181,475 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ45244; previously DICER1-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43017) · Entrez [400242](https://www.ncbi.nlm.nih.gov/gene/400242) · Ensembl [ENSG00000235706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235706)

## Data

Gene col 14033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14033); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14033]; `tensor/DDL_lfc|DDL_z.npy` [14033]; `embed/gene_vectors.npy` [14033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14033 or target_col == 14033). Every well: [[DICER1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DICER1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
