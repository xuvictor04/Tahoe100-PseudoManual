---
symbol: "GGA1"
type: "gene"
col: 1861
ensembl_id: "ENSG00000100083"
name: "golgi associated, gamma adaptin ear containing, ARF binding protein 1"
location: "22q13.1"
module: 85
arm: "+"
pooled_cpm: 25.85
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# GGA1

*golgi associated, gamma adaptin ear containing, ARF binding protein 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.47× (z +9.1, q 4e-17, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.613× (z -16.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (67 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 35 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STUB1]] (+0.64, fdr 2e-04), [[PI4KA]] (+0.64, fdr 2e-04), [[VPS37C]] (+0.63, fdr 1e-05); moves opposite to [[LINC00880]] (-0.62, fdr 3e-04), [[DERA]] (-0.62, fdr 4e-05), [[GIPC2]] (-0.62, fdr 9e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +9.1 | 4e-17 | 27/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +8.8 | 2e-16 | 27/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +8.8 | 2e-16 | 28/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +6.4 | 3e-08 | 26/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.9 | 1e-04 | 14/48 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.15 | 3/48 (NCI-H460, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -16.5 | 0e+00 | 44/48 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -11.0 | 1e-25 | 35/48 (BT-474, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -9.0 | 4e-17 | 29/46 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -7.9 | 4e-13 | 27/48 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.802×** | -5.3 | 2e-05 | 18/45 (Panc 03.27, C-33 A, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -4.9 | 9e-05 | 19/48 (PANC-1, H4, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **0.805×** | -4.8 | 1e-04 | 19/40 (HCT15, HS-578T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **0.818×** | -4.6 | 3e-04 | 13/35 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.826×** | -4.6 | 3e-04 | 21/47 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.722×** | -4.1 | 0.003 | 13/31 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.730×** | -3.9 | 0.005 | 13/42 (NCI-H1573, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.9 | 0.005 | 9/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.738×** | -3.8 | 0.006 | 9/46 (H4, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.012 | 7/48 (SNU-423, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.751×** | -3.6 | 0.013 | 10/46 (HS-578T, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.865× | -3.5 | 0.018 | 11/48 (HEC-1-A, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.047 | 13/48 (NCI-H2030, NCI-H1573, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 34.9 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.343× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -9.5) |
| [[A-172 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.201× (z -10.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.212× (z -10.1) |
| [[C-33 A (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.2) |
| [[KATO III (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[LoVo (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[LS 180 (line)]] | wt | 32.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 40.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0976× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[PANC-1 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.557× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.201× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~55% of this change |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.323× (z -8.9) |
| [[SW480 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[A498 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 16 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | +0.64 | +0.41 / +0.32 | both halves | 2e-04 |  |
| [[PI4KA]] | +0.64 | +0.57 / +0.32 | both halves | 2e-04 |  |
| [[VPS37C]] | +0.63 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DVL1]] | +0.60 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[KCTD20]] | +0.60 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[POLM]] | +0.60 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[TECPR1]] | +0.59 | +0.44 / +0.25 | both halves | 4e-04 |  |
| [[KRI1]] | +0.59 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[RNF41]] | +0.59 | +0.50 / +0.22 | both halves | 6e-04 |  |
| [[NAA40]] | +0.59 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[TNFAIP8L1]] | +0.58 | +0.54 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[CEP131]] | +0.58 | +0.35 / +0.16 | ⚠ not reproduced | 0.001 |  |
| [[DNAJC16]] | +0.57 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[RHPN1]] | +0.56 | +0.44 / +0.21 | both halves | 7e-04 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00880]] | -0.62 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[DERA]] | -0.62 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[GIPC2]] | -0.62 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[CCT6B]] | -0.59 | -0.44 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[LINC02955]] | -0.59 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[MALINC1]] | -0.59 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[LSMEM1]] | -0.58 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[DIPK2A]] | -0.57 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CIBAR1-DT]] | -0.57 | -0.37 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[PSMD7-DT]] | -0.57 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[AP5M1]] | -0.56 | -0.40 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[PNISR-AS1]] | -0.56 | -0.27 / -0.26 | both halves | 3e-04 |  |
| [[PXDNL]] | -0.56 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[PRDM6]] | -0.55 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[MYLK4]] | -0.54 | -0.33 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GGA1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises GGA1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-12.3, 13.5); signed map (-33.2, 1.6). **Vector** length 75.3, 12.5% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +8.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.1 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -11.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | golgi associated, gamma adaptin ear containing, ARF binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,608,474-37,633,564 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Golgi associated, gamma adaptin ear containing, ARF binding proteins |
| Reactome | 5 pathways, smallest: TBC/RABGAPs; Amyloid fiber formation; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJY5](https://www.uniprot.org/uniprotkb/Q9UJY5) (ADP-ribosylation factor-binding protein GGA1):

> Plays a role in protein sorting and trafficking between the trans-Golgi network (TGN) and endosomes. Mediates the ARF-dependent recruitment of clathrin to the TGN and binds ubiquitinated proteins and membrane cargo molecules with a cytosolic acidic cluster-dileucine (DXXLL) motif. Mediates export of the GPCR receptor ADRA2B to the cell surface. Required for targeting PKD1:PKD2 complex from the trans-Golgi network to the cilium membrane (By similarity). Regulates retrograde transport of proteins …

**Summary**, from NCBI Gene [26088](https://www.ncbi.nlm.nih.gov/gene/26088):

> This gene encodes a member of the Golgi-localized, gamma adaptin ear-containing, ARF-binding (GGA) protein family. Members of this family are ubiquitous coat proteins that regulate the trafficking of proteins between the trans-Golgi network and the lysosome. These proteins share an amino-terminal VHS domain which mediates sorting of the mannose 6-phosphate receptors at the trans-Golgi network. They also contain a carboxy-terminal region with homology to the ear domain of gamma-adaptins. …

**Accessions** — [HGNC:17842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17842) · Entrez [26088](https://www.ncbi.nlm.nih.gov/gene/26088) · UniProt [Q9UJY5](https://www.uniprot.org/uniprotkb/Q9UJY5) · Ensembl [ENSG00000100083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100083)

## Data

Gene col 1861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1861); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1861]; `tensor/DDL_lfc|DDL_z.npy` [1861]; `embed/gene_vectors.npy` [1861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1861 or target_col == 1861). Every well: [[GGA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
