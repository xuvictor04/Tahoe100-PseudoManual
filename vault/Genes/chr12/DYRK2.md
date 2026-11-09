---
symbol: "DYRK2"
type: "gene"
col: 4802
ensembl_id: "ENSG00000127334"
name: "dual specificity tyrosine phosphorylation regulated kinase 2"
location: "12q15"
module: 55
arm: "+"
pooled_cpm: 32.72
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# DYRK2

*dual specificity tyrosine phosphorylation regulated kinase 2* — 12q15

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.620× (z -12.9, q 3e-35, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP2S1]] (+0.51, fdr 1e-05), [[ANOS1]] (+0.47, fdr 7e-05), [[MINPP1]] (+0.47, fdr 1e-04); moves opposite to [[DNAAF9]] (-0.48, fdr 5e-05), [[FAM193A]] (-0.47, fdr 4e-05), [[STX12]] (-0.45, fdr 4e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | 1.21× | +3.7 | 0.13 | 13/46 (J82, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | 1.40× | +3.4 | 0.14 | 17/49 (A-427, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.14 | 9/48 (COLO 205, SW1417, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.27 | 4/48 (MIA PaCa-2, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -12.9 | 3e-35 | 31/47 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.604×** | -9.6 | 2e-19 | 35/48 (LoVo, AsPC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.668×** | -7.7 | 3e-12 | 27/48 (KATO III, AsPC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.673×** | -7.5 | 6e-12 | 32/48 (HT-29, COLO 205, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.729×** | -6.0 | 2e-07 | 23/46 (KATO III, SNU-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.740×** | -5.7 | 9e-07 | 21/43 (C32, SW48, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.755×** | -5.4 | 6e-06 | 23/48 (COLO 205, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.748×** | -5.3 | 7e-06 | 25/47 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.759×** | -5.2 | 1e-05 | 23/48 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.768×** | -5.0 | 3e-05 | 21/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.843× | -4.6 | 2e-04 | 21/48 (HT-29, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.778×** | -4.6 | 2e-04 | 20/46 (HT-29, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.785×** | -4.3 | 8e-04 | 18/40 (SHP-77, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.813×** | -3.9 | 0.003 | 17/46 (H4, A549, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.834× | -3.5 | 0.021 | 18/47 (A498, NCI-H1573, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.880× | -3.4 | 0.021 | 12/48 (NCI-H1573, SW 900, …) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.794×** | -3.1 | 0.053 | 13/47 (A498, KATO III, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.846× | -3.1 | 0.066 | 10/48 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.858× | -2.9 | 0.092 | 18/47 (HT-29, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 66.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -17.2) |
| [[LoVo (line)]] | wt | 67.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.8) |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.5) |
| [[HT-29 (line)]] | alt | 73.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 37.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -18.3) |
| [[RKO (line)]] | wt | 34.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -15.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.7) |
| [[C32 (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0617× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[CHP-212 (line)]] | wt | 55.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.103× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.163× (z -9.4) |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0665× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 52.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 46.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.3) |
| [[SHP-77 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0871× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[A-172 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP2S1]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[ANOS1]] | +0.47 | +0.50 / +0.37 | both halves | 7e-05 |  |
| [[MINPP1]] | +0.47 | +0.50 / +0.32 | both halves | 1e-04 |  |
| [[AMIGO2]] | +0.47 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[PLS1]] | +0.46 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[CPOX]] | +0.46 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PIK3C2B]] | +0.45 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[RNF2]] | +0.45 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[ENC1]] | +0.45 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[TNFRSF21]] | +0.44 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[FAT1]] | +0.44 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[LYSMD2]] | +0.44 | +0.47 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[FAM193A]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[STX12]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[AACS]] | -0.44 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[FBXL9P]] | -0.43 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[LRCH3]] | -0.43 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[TRNAU1AP]] | -0.43 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[TRPC1]] | -0.42 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[PROSER3]] | -0.42 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[PAFAH1B1]] | -0.41 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[TMEM91]] | -0.41 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[RBX1]] | -0.41 | -0.47 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises DYRK2's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without NR3C2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[SLC40A1]] | B | SLC40A1 activity raises DYRK2's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.39× lower at baseline in the lines without SLC40A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[TOX3]] | B | TOX3 activity raises DYRK2's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.48× lower at baseline in the lines without TOX3 | 0.026 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[UGT1A6]] | B | UGT1A6 activity raises DYRK2's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 1.39× lower at baseline in the lines without UGT1A6 | 0.060 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises DYRK2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 1.48× lower at baseline in the lines without TMPRSS2 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TC2N]] | B | TC2N activity raises DYRK2's level | lines that do not express TC2N (28) vs lines expressing it (22) | 1.38× lower at baseline in the lines without TC2N | 0.075 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[IGSF9]] | B | IGSF9 activity raises DYRK2's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without IGSF9 | 0.079 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.6, 46.0); signed map (52.3, -3.3). **Vector** length 87.4, 17.7% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +1.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -12.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.1 | -4.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.1 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity tyrosine phosphorylation regulated kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:67,648,338-67,665,406 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Dual-specificity tyrosine-regulated kinase family |
| Hallmark sets | COMPLEMENT |
| Reactome | 3 pathways, smallest: Regulation of TP53 Activity through Phosphorylation; Regulation of TP53 Activity; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92630](https://www.uniprot.org/uniprotkb/Q92630) (Dual specificity tyrosine-phosphorylation-regulated kinase 2):

> Serine/threonine-protein kinase involved in the regulation of the mitotic cell cycle, cell proliferation, apoptosis, organization of the cytoskeleton and neurite outgrowth. Phosphorylates CRMP2/DPYSL2, CRMP4/DPYSL3, DCX, EIF2B5, EIF4EBP1, GLI2, GLI3, GYS1, JUN, MDM2, MYC, NFATC1, p53/TP53, TAU/MAPT and KATNA1. Can phosphorylate histone H1, histone H3 and histone H2B (in vitro). Can phosphorylate CARHSP1 (in vitro). Functions in part via its role in ubiquitin-dependent proteasomal protein …

**Summary**, from NCBI Gene [8445](https://www.ncbi.nlm.nih.gov/gene/8445):

> DYRK2 belongs to a family of protein kinases whose members are presumed to be involved in cellular growth and/or development. The family is defined by structural similarity of their kinase domains and their capability to autophosphorylate on tyrosine residues. DYRK2 has demonstrated tyrosine autophosphorylation and catalyzed phosphorylation of histones H3 and H2B in vitro. Two isoforms of DYRK2 have been isolated. The predominant isoform, isoform 1, lacks a 5' terminal insert. [provided by …

**Accessions** — [HGNC:3093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3093) · Entrez [8445](https://www.ncbi.nlm.nih.gov/gene/8445) · UniProt [Q92630](https://www.uniprot.org/uniprotkb/Q92630) · Ensembl [ENSG00000127334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127334)

## Data

Gene col 4802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4802); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4802]; `tensor/DDL_lfc|DDL_z.npy` [4802]; `embed/gene_vectors.npy` [4802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4802 or target_col == 4802). Every well: [[DYRK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYRK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
