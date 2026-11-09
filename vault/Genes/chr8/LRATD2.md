---
symbol: "LRATD2"
type: "gene"
col: 9681
ensembl_id: "ENSG00000168672"
name: "LRAT domain containing 2"
location: "8q24.21"
module: 143
arm: "+"
pooled_cpm: 19.7
n_lines_expressing: 34
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 20
direction_downstream: 15
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# LRATD2

*LRAT domain containing 2* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +14.1, q 4e-42, up in 18 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.626× (z -7.7, q 9e-12, down in 19 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLDA2]] (+0.50, fdr 4e-05), [[PRNP]] (+0.50, fdr 5e-05), [[SERPINB8]] (+0.50, fdr 3e-05); moves opposite to [[HSPB11]] (-0.49, fdr 6e-05), [[KHDRBS1]] (-0.47, fdr 2e-04), [[TMEM143]] (-0.46, fdr 5e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[DAPP1]] → it (grade B ⚠); 15 go from it, the strongest it → [[PLEKHG3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +14.1 | 4e-42 | 18/30 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +7.5 | 3e-11 | 13/28 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 9e-06 | 15/31 (AsPC-1, A498, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.4 | 9e-06 | 10/32 (SW480, A-172, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 4e-04 | 15/32 (NCI-H2347, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.003 | 6/30 (RKO, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.003 | 9/32 (NCI-H2347, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.003 | 8/31 (NCI-H2347, KATO III, …) | all doses, flat | position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | 1.18× | +3.8 | 0.009 | 9/32 (KATO III, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.7 | 0.010 | 11/30 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.013 | 10/32 (Panc 03.27, COLO 205, …) | two highest doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.023 | 7/31 (C32, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.023 | 10/32 (A498, A-172, …) | top dose only |  |
| [[Lopinavir (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.024 | 5/32 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.035 | 5/31 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.035 | 3/31 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.070 | 8/32 (KATO III, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9681.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.626×** | -7.7 | 9e-12 | 19/32 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -6.5 | 2e-08 | 6/32 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.746×** | -4.8 | 3e-04 | 17/32 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -4.7 | 4e-04 | 14/32 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.747×** | -4.5 | 7e-04 | 14/31 (SK-MEL-2, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -4.0 | 0.007 | 15/32 (BT-474, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.049 | 15/32 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | **0.800×** | -3.4 | 0.049 | 4/31 (H4, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.815×** | -3.4 | 0.049 | 14/31 (RKO, Panc 03.27, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.049 | 9/31 (C32, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 19.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 102 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -9.5) |
| [[RKO (line)]] | wt | 15.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0729× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[AN3 CA (line)]] | alt | 52.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 5.98 | 0 | 2 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0786× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 62.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.110× (z -8.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 60.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -9.6) |
| [[C32 (line)]] | wt | 16.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0358× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +8.9) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[Hs 766T (line)]] | wt | 7.13 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.107× (z -8.5) |
| [[KATO III (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.307× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1792 (line)]] | alt | 5.91 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0943× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 8.34 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0921× (z -9.1) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.72 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLDA2]] | +0.50 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[PRNP]] | +0.50 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[SERPINB8]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[KCTD12]] | +0.50 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[CDC42EP1]] | +0.49 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[RESF1]] | +0.48 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[ARAP2]] | +0.48 | +0.49 / +0.32 | both halves | 2e-04 |  |
| [[EPHA2]] | +0.48 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SDR16C5]] | +0.48 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[SLC30A1]] | +0.47 | +0.37 / +0.39 | both halves | 8e-05 |  |
| [[PLEKHG3]] | +0.47 | +0.40 / +0.49 | both halves | 4e-05 |  |
| [[KHNYN]] | +0.46 | +0.38 / +0.43 | both halves | 6e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB11]] | -0.49 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[KHDRBS1]] | -0.47 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[TMEM143]] | -0.46 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TENT2]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ORC3]] | -0.46 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[POT1]] | -0.44 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[CDC27]] | -0.43 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[RPS6KC1]] | -0.42 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[MED23]] | -0.42 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[KIAA1328]] | -0.42 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[SLC25A42]] | -0.42 | -0.22 / -0.30 | both halves | 6e-04 |  |
| [[MARCHF6]] | -0.41 | -0.34 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 18, C 2. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAPP1]] | B | DAPP1 activity raises LRATD2's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 4.87× lower at baseline in the lines without DAPP1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[FAM83B]] | B | FAM83B activity raises LRATD2's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.98× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[TMEM30B]] | B | TMEM30B activity raises LRATD2's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.06× lower at baseline in the lines without TMEM30B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[SLC28A3]] | B | SLC28A3 activity raises LRATD2's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without SLC28A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[RASEF]] | B | RASEF activity raises LRATD2's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without RASEF | 0.020 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[SPINT1]] | B | SPINT1 activity raises LRATD2's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.86× lower at baseline in the lines without SPINT1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[PRSS22]] | B | PRSS22 activity raises LRATD2's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 3.10× lower at baseline in the lines without PRSS22 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[TACSTD2]] | B | TACSTD2 activity raises LRATD2's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.96× lower at baseline in the lines without TACSTD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[ESRP2]] | B | ESRP2 activity raises LRATD2's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.94× lower at baseline in the lines without ESRP2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[DUSP4]] | B | DUSP4 activity raises LRATD2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.89× lower at baseline in the lines without DUSP4 | 0.041 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[CEACAM5]] | B | CEACAM5 activity raises LRATD2's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.89× lower at baseline in the lines without CEACAM5 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[FAM83B]] | B | FAM83B activity strengthens LRATD2's drug response | lines that do not express FAM83B (15) vs lines expressing it (17) | the lines without FAM83B respond 0.78× as strongly (z diff +0.30); strongest at Panobinostat 5 µM: 0.74x vs 0.50x (z diff +3.2) | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG3]] | B | LRATD2 activity raises PLEKHG3's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without LRATD2 | 0.002 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[LONRF3]] | B | LRATD2 activity raises LONRF3's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.93× lower at baseline in the lines without LRATD2 | 0.006 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[SDR16C5]] | B | LRATD2 activity raises SDR16C5's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without LRATD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[FAM83B]] | B | LRATD2 activity raises FAM83B's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 4.35× lower at baseline in the lines without LRATD2 | 0.016 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[TNFRSF21]] | B | LRATD2 activity raises TNFRSF21's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.53× lower at baseline in the lines without LRATD2 | 0.036 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[SPINT1]] | B | LRATD2 activity raises SPINT1's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 4.89× lower at baseline in the lines without LRATD2 | 0.037 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[TACSTD2]] | B | LRATD2 activity raises TACSTD2's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 3.34× lower at baseline in the lines without LRATD2 | 0.037 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[RASEF]] | B | LRATD2 activity raises RASEF's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 3.63× lower at baseline in the lines without LRATD2 | 0.045 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[DAPP1]] | B | LRATD2 activity raises DAPP1's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.83× lower at baseline in the lines without LRATD2 | 0.055 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[DUSP4]] | B | LRATD2 activity raises DUSP4's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without LRATD2 | 0.057 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[TMEM30B]] | B | LRATD2 activity raises TMEM30B's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 3.03× lower at baseline in the lines without LRATD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[SLC28A3]] | B | LRATD2 activity raises SLC28A3's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without LRATD2 | 0.082 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.379). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.2, 52.8); signed map (18.1, 20.7). **Vector** length 71.1, 15.5% of its response variance represented; |z| ≥ 3 in 702 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.0 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | LRAT domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.21 — chr8:126,552,443-126,558,478 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCMP101, NSE2; previously FAM84B |
| Gene groups (HGNC) | LRAT domain containing |
| Matched by | ensembl_id |

UniProt [Q96KN1](https://www.uniprot.org/uniprotkb/Q96KN1) carries no function annotation.

**Summary**, from NCBI Gene [157638](https://www.ncbi.nlm.nih.gov/gene/157638):

> Located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24166) · Entrez [157638](https://www.ncbi.nlm.nih.gov/gene/157638) · UniProt [Q96KN1](https://www.uniprot.org/uniprotkb/Q96KN1) · Ensembl [ENSG00000168672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168672)

## Data

Gene col 9681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9681); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9681]; `tensor/DDL_lfc|DDL_z.npy` [9681]; `embed/gene_vectors.npy` [9681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9681 or target_col == 9681). Every well: [[LRATD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRATD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
