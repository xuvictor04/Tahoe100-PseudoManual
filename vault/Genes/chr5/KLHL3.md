---
symbol: "KLHL3"
type: "gene"
col: 7054
ensembl_id: "ENSG00000146021"
name: "kelch like family member 3"
location: "5q31.2"
module: 36
arm: "-"
pooled_cpm: 8.66
n_lines_expressing: 38
n_dd_up: 3
n_dd_down: 29
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# KLHL3

*kelch like family member 3* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +8.9, q 2e-16, up in 20 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.204× (z -16.4, q 0e+00, down in 31 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS22]] (+0.56, fdr 3e-05), [[RNF167]] (+0.55, fdr 3e-05), [[RAE1]] (+0.54, fdr 5e-05); moves opposite to [[PACS2]] (-0.55, fdr 1e-05), [[DTNBP1]] (-0.54, fdr 6e-05), [[RBFA]] (-0.54, fdr 4e-05).
> It sits in the **-** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABCA3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[VPS37C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.9 | 2e-16 | 20/33 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +4.4 | 0.003 | 12/34 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.097 | 12/34 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.39× | +3.4 | 0.10 | 8/34 (Panc 03.27, NCI-H23, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.37× | +3.2 | 0.14 | 2/35 (AN3 CA, MIA PaCa-2) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.15 | 10/34 (AsPC-1, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.37× | +3.1 | 0.15 | 5/34 (NCI-H23, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7054.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.204×** | -16.4 | 0e+00 | 31/35 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.273×** | -13.4 | 2e-38 | 27/31 (HOP62, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.300×** | -12.4 | 3e-33 | 31/34 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.323×** | -11.7 | 3e-29 | 25/35 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.320×** | -11.3 | 1e-27 | 27/34 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.394×** | -9.6 | 7e-20 | 22/34 (COLO 205, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.391×** | -9.3 | 9e-19 | 20/28 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.582×** | -7.9 | 2e-13 | 20/32 (COLO 205, CFPAC-1, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -7.0 | 1e-10 | 20/29 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -6.7 | 2e-09 | 19/32 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.585×** | -5.5 | 2e-06 | 18/35 (hTERT-HPNE, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.690×** | -5.4 | 3e-06 | 16/35 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.624×** | -4.9 | 5e-05 | 16/35 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -4.8 | 6e-05 | 15/34 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.558×** | -4.5 | 3e-04 | 12/34 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.663×** | -4.2 | 8e-04 | 17/33 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.675×** | -4.1 | 0.002 | 16/35 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.671×** | -4.0 | 0.002 | 13/34 (CFPAC-1, CHP-212, …) | rises with dose | position effect removed |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.777×** | -3.7 | 0.005 | 10/35 (SW 900, NCI-H460, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.743×** | -3.1 | 0.048 | 7/34 (SW 1271, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 13 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0727× (z -17.8) |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0432× (z -24.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0831× (z -13.8) |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0219× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0150× (z -25.2) |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.114× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0411× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 25.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -18.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -11.2) |
| [[A-427 (line)]] | wt | 19.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.165× (z -10.0) |
| [[J82 (line)]] | alt | 8.51 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -9.9) |
| [[C32 (line)]] | wt | 14.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0427× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -8.7) |
| [[Hs 766T (line)]] | wt | 7.29 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0485× (z -11.3) ⚠ toxic |
| [[KATO III (line)]] | alt | 4.54 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0572× (z -10.2) |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0325× (z -14.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0864× (z -10.5) |
| [[SW1417 (line)]] | alt | 5.86 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0356× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 9.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.5× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0298× (z -9.6) |
| [[H4 (line)]] | wt | 10.1 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0615× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 7.37 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.05 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0988× (z -9.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0379× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 2.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.01× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0951× (z -10.8) |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.140× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 9.85 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0719× (z -9.6) |
| [[A-172 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.931 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.783 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS22]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[RNF167]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RAE1]] | +0.54 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[HFE]] | +0.52 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[SERPINH1]] | +0.51 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[SPAG4]] | +0.51 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[PSMC6]] | +0.50 | +0.48 / +0.38 | both halves | 7e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PKD2L2-DT]] | +0.50 | +0.53 / +0.37 | both halves | 7e-05 |  |
| [[PSMC2]] | +0.50 | +0.46 / +0.31 | both halves | 2e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SPAG16]] | +0.50 | +0.50 / +0.34 | both halves | 1e-04 | same gene group |
| [[TGFB3]] | +0.50 | +0.29 / +0.36 | both halves | 2e-04 |  |
| [[KIAA0825]] | +0.50 | +0.47 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACS2]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DTNBP1]] | -0.54 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[RBFA]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[UNC13B]] | -0.54 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[ABCA3]] | -0.53 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[DOP1B]] | -0.53 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[PSEN2]] | -0.52 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[SPIRE1]] | -0.52 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[PKN1]] | -0.51 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[EPS15]] | -0.51 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[VPS8]] | -0.51 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[GALNT11]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | ABCA3 activity lowers KLHL3's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.49× higher at baseline in the lines without ABCA3 | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VPS37C]] | B | KLHL3 activity raises VPS37C's level | lines that do not express KLHL3 (12) vs lines expressing it (38) | 1.13× lower at baseline in the lines without KLHL3 | 0.063 | ⚠ within organs, on part of the lines; also absent: PKD2L2-DT, CLIP4, ZNF550 |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **-** arm (projection on the module's main direction -0.191). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-4.4, -24.0); signed map (34.1, -26.9). **Vector** length 61.6, 11.0% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +3.0 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | -2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -11.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -16.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:137,617,500-137,736,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1129 |
| Gene groups (HGNC) | Kelch like; BTB domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH77](https://www.uniprot.org/uniprotkb/Q9UH77) (Kelch-like protein 3):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that acts as a regulator of ion transport in the distal nephron. The BCR(KLHL3) complex acts by mediating ubiquitination and degradation of WNK1 and WNK4, two activators of Na-Cl cotransporter SLC12A3/NCC in distal convoluted tubule cells of kidney, thereby regulating NaCl reabsorption. The BCR(KLHL3) complex also mediates ubiquitination and degradation of WNK3. The BCR(KLHL3) complex also mediates ubiquitination of …

**Summary**, from NCBI Gene [26249](https://www.ncbi.nlm.nih.gov/gene/26249):

> This gene is ubiquitously expressed and encodes a full-length protein which has an N-terminal BTB domain followed by a BACK domain and six kelch-like repeats in the C-terminus. These kelch-like repeats promote substrate ubiquitination of bound proteins via interaction of the BTB domain with the CUL3 (cullin 3) component of a cullin-RING E3 ubiquitin ligase (CRL) complex. Muatations in this gene cause pseudohypoaldosteronism type IID (PHA2D); a rare Mendelian syndrome featuring hypertension, …

**Accessions** — [HGNC:6354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6354) · Entrez [26249](https://www.ncbi.nlm.nih.gov/gene/26249) · UniProt [Q9UH77](https://www.uniprot.org/uniprotkb/Q9UH77) · Ensembl [ENSG00000146021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146021)

## Data

Gene col 7054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7054); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7054]; `tensor/DDL_lfc|DDL_z.npy` [7054]; `embed/gene_vectors.npy` [7054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7054 or target_col == 7054). Every well: [[KLHL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
