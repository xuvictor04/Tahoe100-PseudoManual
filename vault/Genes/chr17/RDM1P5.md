---
symbol: "RDM1P5"
type: "gene"
col: 15427
ensembl_id: "ENSG00000263818"
name: "RDM1 pseudogene 5"
location: "17q12"
module: 10
arm: "+"
pooled_cpm: 4.25
n_lines_expressing: 43
n_dd_up: 9
n_dd_down: 34
n_dd_up_clean: 6
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 12
direction_downstream: 25
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# RDM1P5

*RDM1 pseudogene 5* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.74× (z +5.9, q 2e-06, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.67× (z +5.7, q 4e-06, up in 16 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.229× (z -16.2, q 0e+00, down in 36 of 40 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ID2-AS1]] (+0.57, fdr 3e-05), [[ANKRD20A21P]] (+0.57, fdr 1e-05), [[TLCD3B]] (+0.55, fdr 1e-05); moves opposite to [[BICDL1]] (-0.49, fdr 7e-04), [[LRRFIP1]] (-0.46, fdr 3e-05), [[EIF6]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[LINC00466]] → it (grade B ⚠); 25 go from it, the strongest it → [[B4GAT1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.9 | 2e-06 | 3/5 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +5.7 | 4e-06 | 16/39 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +5.2 | 4e-05 | 11/37 (KATO III, BT-474, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 9e-04 | 8/38 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.3 | 0.002 | 4/14 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.6 | 0.030 | 4/20 (NCI-H1573, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.030 | 5/35 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.030 | 5/36 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.089 | 4/40 (KATO III, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.22× | +3.1 | 0.10 | 6/30 (BT-474, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.229×** | -16.2 | 0e+00 | 36/40 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.327×** | -12.2 | 5e-32 | 26/37 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.358×** | -11.3 | 4e-27 | 27/37 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.420×** | -9.2 | 8e-18 | 21/36 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.442×** | -9.0 | 4e-17 | 23/35 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.457×** | -8.6 | 8e-16 | 25/39 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -7.9 | 2e-13 | 19/26 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.499×** | -7.6 | 2e-12 | 21/37 (BT-474, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.482×** | -7.5 | 3e-12 | 19/32 (A498, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.506×** | -7.5 | 5e-12 | 16/29 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.650×** | -6.7 | 1e-09 | 17/36 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.539×** | -6.5 | 4e-09 | 19/24 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -5.5 | 2e-06 | 15/36 (SW480, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.406×** | -5.2 | 9e-06 | 16/34 (HEC-1-A, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.406×** | -5.2 | 9e-06 | 15/26 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.630×** | -5.0 | 2e-05 | 12/35 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -4.9 | 3e-05 | 14/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.662×** | -4.5 | 2e-04 | 17/31 (HT-29, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 26.3 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0720× (z -14.9) |
| [[SW480 (line)]] | alt | 7.12 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0285× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0387× (z -18.5) |
| [[A-427 (line)]] | wt | 11.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0622× (z -14.8) |
| [[A498 (line)]] | wt | 5.10 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0633× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 13.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +9.4) ⚠ position not correctable | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -9.2) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.158× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 5.38 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0497× (z -12.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0702× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 5.15 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.149× (z -9.2) |
| [[PANC-1 (line)]] | alt | 2.26 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0457× (z -12.2) |
| [[A549 (line)]] | wt | 5.54 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0632× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 8.65 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.59 | 0 | 1 | — | [[Temsirolimus (drug)]] 5 µM 0.0878× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 4.40 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0372× (z -8.9) |
| [[A-172 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ID2-AS1]] | +0.57 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[ANKRD20A21P]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TLCD3B]] | +0.55 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ADAMTS13]] | +0.53 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[FAM66C]] | +0.52 | +0.61 / +0.37 | both halves | 7e-05 |  |
| [[FBXO15]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[NUDT7]] | +0.52 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[TESMIN]] | +0.52 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[LINC02026]] | +0.51 | +0.62 / +0.32 | both halves | 2e-04 |  |
| [[PPP1CB-DT]] | +0.48 | +0.58 / +0.36 | both halves | 1e-04 |  |
| [[KAZALD1]] | +0.48 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[PUM2]] | +0.48 | +0.29 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICDL1]] | -0.49 | -0.44 / -0.21 | both halves | 7e-04 |  |
| [[LRRFIP1]] | -0.46 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[EIF6]] | -0.44 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[LINC02109]] | -0.43 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[NPC1]] | -0.40 | -0.39 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00466]] | B | LINC00466 activity raises RDM1P5's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without LINC00466 | 0.004 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[SSPOP]] | B | SSPOP activity raises RDM1P5's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without SSPOP | 0.006 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[KSR2]] | B | KSR2 activity raises RDM1P5's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without KSR2 | 0.041 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises RDM1P5's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without SYT9-AS1 | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises RDM1P5's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without MIR1915HG | 0.057 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[FGF20]] | B | FGF20 activity raises RDM1P5's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.56× lower at baseline in the lines without FGF20 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[LINC00173]] | B | LINC00173 activity raises RDM1P5's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.35× lower at baseline in the lines without LINC00173 | 0.068 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[LINC02026]] | B | LINC02026 activity raises RDM1P5's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without LINC02026 | 0.077 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |
| [[FAM66C]] | B | FAM66C activity raises RDM1P5's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without FAM66C | 0.091 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[TRPM2-AS]] | B | TRPM2-AS activity raises RDM1P5's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.57× lower at baseline in the lines without TRPM2-AS | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[ID2-AS1]] | C | ID2-AS1 activity raises RDM1P5's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 2.30× lower at baseline in the lines without ID2-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5; co-absent with the target |
| [[TLCD3B]] | C | TLCD3B activity raises RDM1P5's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without TLCD3B | 0.025 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 24, C 1. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GAT1-DT]] | B | RDM1P5 activity raises B4GAT1-DT's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without RDM1P5 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[C21orf58]] | B | RDM1P5 activity raises C21orf58's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without RDM1P5 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[TESMIN]] | B | RDM1P5 activity raises TESMIN's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without RDM1P5 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[PRSS16]] | B | RDM1P5 activity raises PRSS16's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without RDM1P5 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[CHKB-DT]] | B | RDM1P5 activity raises CHKB-DT's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without RDM1P5 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[ARHGEF39]] | B | RDM1P5 activity raises ARHGEF39's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without RDM1P5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[H3-3A-DT]] | B | RDM1P5 activity raises H3-3A-DT's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without RDM1P5 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[CASC2]] | B | RDM1P5 activity raises CASC2's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 2.11× lower at baseline in the lines without RDM1P5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[BRPF3-AS1]] | B | RDM1P5 activity raises BRPF3-AS1's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without RDM1P5 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[DOC2A]] | B | RDM1P5 activity raises DOC2A's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.91× lower at baseline in the lines without RDM1P5 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[TMEM143]] | B | RDM1P5 activity raises TMEM143's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without RDM1P5 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[CYB5RL]] | B | RDM1P5 activity raises CYB5RL's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.93× lower at baseline in the lines without RDM1P5 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.352). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.8, 30.5); signed map (37.6, -10.1). **Vector** length 53.4, 8.41% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +1.4 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.4 | +3.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.0 | +4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +5.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +0.9 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -11.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -9.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | RDM1 pseudogene 5 |
| Locus type | pseudogene |
| Location | 17q12 — chr17:39,057,064-39,058,036 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53921) · Entrez [100131347](https://www.ncbi.nlm.nih.gov/gene/100131347) · Ensembl [ENSG00000263818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263818)

## Data

Gene col 15427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15427); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15427]; `tensor/DDL_lfc|DDL_z.npy` [15427]; `embed/gene_vectors.npy` [15427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15427 or target_col == 15427). Every well: [[RDM1P5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RDM1P5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
