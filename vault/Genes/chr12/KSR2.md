---
symbol: "KSR2"
type: "gene"
col: 10106
ensembl_id: "ENSG00000171435"
name: "kinase suppressor of ras 2"
location: "12q24.22-q24.23"
module: 27
arm: "+"
pooled_cpm: 13.81
n_lines_expressing: 30
n_dd_up: 31
n_dd_down: 11
n_dd_up_clean: 25
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 22
direction_downstream: 22
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# KSR2

*kinase suppressor of ras 2* — 12q24.22-q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.47× (z +16.8, q 0e+00, up in 20 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.564× (z -7.5, q 3e-11, down in 20 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF20]] (+0.63, fdr 7e-06), [[LINC02253]] (+0.62, fdr 1e-05), [[DNAH6]] (+0.61, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[SORL1]] → it (grade B ⚠); 22 go from it, the strongest it → [[RNF43]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.47×** | +16.8 | 0e+00 | 20/25 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +14.3 | 4e-44 | 6/23 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +12.9 | 1e-35 | 5/15 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +10.3 | 1e-22 | 18/25 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +9.0 | 3e-17 | 3/22 (SHP-77, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +7.9 | 2e-13 | 10/20 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +7.8 | 5e-13 | 14/27 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +7.2 | 6e-11 | 15/27 (LoVo, A549, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +5.7 | 7e-07 | 7/24 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 2e-05 | 12/24 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +5.1 | 2e-05 | 13/27 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.8 | 6e-05 | 5/18 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +4.7 | 1e-04 | 17/26 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 3e-04 | 16/24 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.001 | 10/24 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.005 | 8/27 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.008 | 10/24 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.010 | 3/24 (HT-29, COLO 205, …) | top dose only | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -7.5 | 3e-11 | 20/24 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.592×** | -6.6 | 9e-09 | 18/23 (HCT15, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.645×** | -5.8 | 2e-06 | 12/23 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.646×** | -5.7 | 2e-06 | 17/24 (HCT15, A-427, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.684×** | -5.0 | 7e-05 | 13/23 (CFPAC-1, NCI-H2030, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.677×** | -4.9 | 7e-05 | 19/27 (HCT15, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.726×** | -4.2 | 0.002 | 13/24 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.731×** | -4.0 | 0.005 | 9/26 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.753×** | -3.7 | 0.012 | 17/25 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.839× | -3.3 | 0.064 | 17/25 (A-427, SHP-77, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.786×** | -3.2 | 0.079 | 13/27 (C-33 A, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.779×** | -3.1 | 0.079 | 14/24 (A-427, HCT15, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 112 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0696× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0860× (z -16.3) |
| [[A-427 (line)]] | wt | 134 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -16.0) |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -12.5) |
| [[C-33 A (line)]] | alt | 47.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.130× (z -11.2) |
| [[LoVo (line)]] | wt | 21.0 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +10.1) | [[Digitoxin (drug)]] 0.5 µM 0.178× (z -10.7) |
| [[SW48 (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0823× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.9) |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0632× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.214× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0955× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~90% of this change |
| [[SW480 (line)]] | alt | 16.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.267× (z -8.9) |
| [[A-172 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF20]] | +0.63 | +0.66 / +0.60 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[LINC02253]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[DNAH6]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[BMP7]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[AXIN2]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TSPEAR]] | +0.57 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SPTB]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[SORL1]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[KLHL32]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SYT9-AS1]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MPP7]] | +0.55 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[LINC01091]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 16, C 6. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORL1]] | B | SORL1 activity raises KSR2's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without SORL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[LINC02331]] | B | LINC02331 activity raises KSR2's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.97× lower at baseline in the lines without LINC02331 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[FUT9]] | B | FUT9 activity raises KSR2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 1.89× lower at baseline in the lines without FUT9 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[LINC02050]] | B | LINC02050 activity raises KSR2's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 2.64× lower at baseline in the lines without LINC02050 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises KSR2's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.88× lower at baseline in the lines without SLC44A3-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[CDX2]] | B | CDX2 activity raises KSR2's level | lines that do not express CDX2 (27) vs lines expressing it (23) | 2.70× lower at baseline in the lines without CDX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: FAM83F, CKMT1A, ENSG00000225680 |
| [[SLC44A3]] | B | SLC44A3 activity raises KSR2's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.81× lower at baseline in the lines without SLC44A3 | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[FGF20]] | B | FGF20 activity raises KSR2's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 4.29× lower at baseline in the lines without FGF20 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[RNF43]] | B | RNF43 activity raises KSR2's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without RNF43 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[SAMD12]] | B | SAMD12 activity raises KSR2's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.53× lower at baseline in the lines without SAMD12 | 0.070 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[KLHL32]] | B | KLHL32 activity raises KSR2's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.65× lower at baseline in the lines without KLHL32 | 0.079 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[ID2-AS1]] | B | ID2-AS1 activity raises KSR2's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 2.79× lower at baseline in the lines without ID2-AS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 14, C 8. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF43]] | B | KSR2 activity raises RNF43's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without KSR2 | 0.017 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[LINC00992]] | B | KSR2 activity raises LINC00992's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without KSR2 | 0.033 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[PPM1H]] | B | KSR2 activity raises PPM1H's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without KSR2 | 0.035 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[LRP4]] | B | KSR2 activity weakens LRP4's drug response | lines that do not express KSR2 (13) vs lines expressing it (19) | the lines without KSR2 respond 6.81× as strongly (z diff -2.64); strongest at Ixazomib citrate 5 µM: 2.80x vs 1.00x (z diff -4.4) | 0.036 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PPFIBP2]] | B | KSR2 activity raises PPFIBP2's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without KSR2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[SYT9-AS1]] | B | KSR2 activity raises SYT9-AS1's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without KSR2 | 0.041 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[RDM1P5]] | B | KSR2 activity raises RDM1P5's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without KSR2 | 0.041 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[SLAIN1]] | B | KSR2 activity raises SLAIN1's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without KSR2 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[SLC44A3-AS1]] | B | KSR2 activity raises SLC44A3-AS1's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without KSR2 | 0.054 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[AMOT]] | B | KSR2 activity raises AMOT's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.81× lower at baseline in the lines without KSR2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[SORL1]] | B | KSR2 activity raises SORL1's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without KSR2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[LINC02147]] | B | KSR2 activity raises LINC02147's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without KSR2 | 0.082 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 39.9); signed map (55.6, 17.0). **Vector** length 71.7, 19.2% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +4.5 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -7.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | kinase suppressor of ras 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22-q24.23 — chr12:117,453,012-117,968,990 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25965 |
| Gene groups (HGNC) | RAF family; Pseudokinases |
| Reactome | 13 pathways, smallest: Signaling by high-kinase activity BRAF mutants; MAP2K and MAPK activation; Signaling by RAF1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6VAB6](https://www.uniprot.org/uniprotkb/Q6VAB6) (Kinase suppressor of Ras 2):

> Location-regulated scaffold connecting MEK to RAF. Has very low protein kinase activity and can phosphorylate MAP2K1 at several Ser and Thr residues with very low efficiency (in vitro). Acts as MAP2K1/MEK1-dependent allosteric activator of BRAF; upon binding to MAP2K1/MEK1, dimerizes with BRAF and promotes BRAF-mediated phosphorylation of MAP2K1/MEK1. Interaction with BRAF enhances KSR2-mediated phosphorylation of MAP2K1 (in vitro). Blocks MAP3K8 kinase activity and MAP3K8-mediated signaling. …

**Summary**, from NCBI Gene [283455](https://www.ncbi.nlm.nih.gov/gene/283455):

> Enables protein serine/threonine kinase activity. Predicted to be involved in Ras protein signal transduction; calcium-mediated signaling; and positive regulation of cold-induced thermogenesis. Predicted to act upstream of or within positive regulation of MAPK cascade. Predicted to be located in membrane. Predicted to be active in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18610](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18610) · Entrez [283455](https://www.ncbi.nlm.nih.gov/gene/283455) · UniProt [Q6VAB6](https://www.uniprot.org/uniprotkb/Q6VAB6) · Ensembl [ENSG00000171435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171435)

## Data

Gene col 10106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10106); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10106]; `tensor/DDL_lfc|DDL_z.npy` [10106]; `embed/gene_vectors.npy` [10106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10106 or target_col == 10106). Every well: [[KSR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KSR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
