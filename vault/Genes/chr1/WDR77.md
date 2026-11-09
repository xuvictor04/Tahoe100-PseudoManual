---
symbol: "WDR77"
type: "gene"
col: 3795
ensembl_id: "ENSG00000116455"
name: "WD repeat domain 77"
location: "1p13.2"
module: 4
arm: "+"
pooled_cpm: 9.18
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# WDR77

*WD repeat domain 77* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.19× (z +19.3, q 0e+00, up in 34 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.51× (z +6.8, q 8e-10, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.799× (z -3.8, q 0.093, down in 17 of 47 measured lines) ⚠ cell-cycle shift, explains ~50% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0789×; ⚠ cell-cycle shift, would explain all of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0367×); [[Rosiglitazone (drug)]] 5 µM in 1 line (RPMI-7951 0.0731×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (C32 0.0698×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCF2]] (+0.83, fdr 7e-06), [[PSME3]] (+0.81, fdr 7e-06), [[TMEM33]] (+0.81, fdr 7e-06); moves opposite to [[SIRT2]] (-0.71, fdr 7e-06), [[UBE2B]] (-0.69, fdr 7e-06), [[TESK2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DHRS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **5.19×** | +19.3 | 0e+00 | 34/35 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.81×** | +17.7 | 0e+00 | 13/14 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.00×** | +15.0 | 0e+00 | 25/25 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.36×** | +10.1 | 1e-21 | 39/47 (HT-29, NCI-H1792, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.93×** | +7.7 | 2e-12 | 34/47 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.87×** | +7.0 | 2e-10 | 25/39 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.8 | 8e-10 | 31/48 (MIA PaCa-2, A-172, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +6.2 | 4e-08 | 21/42 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.71×** | +6.0 | 1e-07 | 24/46 (NCI-H23, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.67×** | +6.0 | 1e-07 | 28/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +5.6 | 1e-06 | 18/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.61×** | +5.3 | 4e-06 | 15/37 (CFPAC-1, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.3 | 5e-06 | 22/46 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.36×** | +5.1 | 2e-05 | 17/43 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.58×** | +5.1 | 2e-05 | 21/47 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.19×** | +4.8 | 6e-05 | 17/42 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.7 | 8e-05 | 21/47 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 7e-04 | 15/45 (LOX-IMVI, A498, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.003 | 11/46 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.85×** | +3.8 | 0.004 | 9/43 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.004 | 13/46 (HOP62, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.005 | 13/43 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +3.5 | 0.007 | 14/40 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.77×** | +3.5 | 0.009 | 12/38 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.009 | 14/46 (CFPAC-1, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3795.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0789×; ⚠ cell-cycle shift, would explain all of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0367×); [[Rosiglitazone (drug)]] 5 µM in 1 line (RPMI-7951 0.0731×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (C32 0.0698×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.799×** | -3.8 | 0.093 | 17/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.762× | -3.1 | 0.38 | 8/46 (CFPAC-1, HS-578T, …) | top dose only | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.44 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.04× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 12.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 10.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.59× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 14.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.72× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 4.05 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0698× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 4.24 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0367× (z -11.8) |
| [[HOP62 (line)]] | alt | 3.97 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.54× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.52× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 4.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.1× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 7.48 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.17 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0789× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 6.77 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0731× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF2]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[PSME3]] | +0.81 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.81 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[LETM1]] | +0.79 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[BOP1]] | +0.77 | +0.79 / +0.80 | both halves | 7e-06 | same gene group |
| [[MYBBP1A]] | +0.76 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[PFAS]] | +0.74 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | STRING 596 |
| [[ATIC]] | +0.74 | +0.76 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.71 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[UBE2B]] | -0.69 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[TESK2]] | -0.68 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.67 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[RNASE4]] | -0.66 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.66 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[SYF2]] | -0.66 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.66 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[ING2]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[MINDY2]] | -0.65 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.65 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.65 | -0.59 / -0.70 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DHRS3]] | B | DHRS3 activity lowers WDR77's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.38× higher at baseline in the lines without DHRS3 | 0.074 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.812). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.8, -33.1); signed map (-6.7, -44.8). **Vector** length 82.9, 16.4% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.52 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.52 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +8.7 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +8.4 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +15.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.5 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.0 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.8 | +3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.7 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 77 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:111,439,890-111,449,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEP50, p44 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 6 pathways, smallest: RMTs methylate histone arginines; Metabolism of non-coding RNA; snRNP Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQA1](https://www.uniprot.org/uniprotkb/Q9BQA1) (Methylosome protein WDR77):

> Non-catalytic component of the methylosome complex, composed of PRMT5, WDR77 and CLNS1A, which modifies specific arginines to dimethylarginines in several spliceosomal Sm proteins and histones. This modification targets Sm proteins to the survival of motor neurons (SMN) complex for assembly into small nuclear ribonucleoprotein core particles. Might play a role in transcription regulation. The methylosome complex also methylates the Piwi proteins (PIWIL1, PIWIL2 and PIWIL4), methylation of Piwi …

**Summary**, from NCBI Gene [79084](https://www.ncbi.nlm.nih.gov/gene/79084):

> The protein encoded by this gene is an androgen receptor coactivator that forms a complex with protein arginine methyltransferase 5, which modifies specific arginines to dimethylarginines in several spliceosomal Sm proteins. The encoded protein may be involved in the early stages of prostate cancer, with most of the protein being nuclear-localized in benign cells but cytoplasmic in cancer cells. Several transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:29652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29652) · Entrez [79084](https://www.ncbi.nlm.nih.gov/gene/79084) · UniProt [Q9BQA1](https://www.uniprot.org/uniprotkb/Q9BQA1) · Ensembl [ENSG00000116455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116455)

## Data

Gene col 3795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3795); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3795]; `tensor/DDL_lfc|DDL_z.npy` [3795]; `embed/gene_vectors.npy` [3795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3795 or target_col == 3795). Every well: [[WDR77 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR77.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
