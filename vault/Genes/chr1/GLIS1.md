---
symbol: "GLIS1"
type: "gene"
col: 10485
ensembl_id: "ENSG00000174332"
name: "GLIS family zinc finger 1"
location: "1p32.3"
module: 13
arm: "+"
pooled_cpm: 9.62
n_lines_expressing: 26
n_dd_up: 29
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 34
direction_downstream: 28
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GLIS1

*GLIS family zinc finger 1* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 8.60× (z +25.0, q 0e+00, up in 21 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.539× (z -6.9, q 2e-09, down in 15 of 22 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.668× (z -4.7, q 6e-04, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR16]] (+0.62, fdr 1e-05), [[SLIT3]] (+0.61, fdr 1e-05), [[NID2]] (+0.60, fdr 1e-05); moves opposite to [[ANK3]] (-0.45, fdr 4e-04), [[SBF2-AS1]] (-0.44, fdr 2e-04), [[SPHK1]] (-0.44, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 34 arrows point to it, the strongest [[GXYLT2]] → it (grade B ⚠); 28 go from it, the strongest it → [[CACNA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **8.60×** | +25.0 | 0e+00 | 21/24 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.19×** | +23.5 | 0e+00 | 9/22 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.03×** | +18.8 | 0e+00 | 18/24 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.84×** | +15.6 | 0e+00 | 18/24 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +11.4 | 8e-28 | 12/24 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +10.5 | 1e-23 | 6/23 (NCI-H23, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +8.9 | 6e-17 | 15/24 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +8.4 | 5e-15 | 0/11 | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.6 | 2e-12 | 3/14 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.9 | 3e-10 | 5/24 (A-172, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.99×** | +6.6 | 2e-09 | 7/24 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.68×** | +5.8 | 4e-07 | 4/19 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +5.6 | 1e-06 | 1/18 (J82) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.54×** | +4.8 | 6e-05 | 3/20 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.002 | 6/21 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.005 | 6/24 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.012 | 6/22 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.013 | 5/23 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.015 | 5/23 (HOP62, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.022 | 7/24 (HOP62, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10485.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.539×** | -6.9 | 2e-09 | 15/22 (RPMI-7951, A498, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -4.7 | 6e-04 | 14/24 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.760×** | -4.6 | 1e-03 | 10/21 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.707×** | -4.1 | 0.007 | 14/24 (SW 900, SHP-77, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -3.5 | 0.059 | 10/23 (A-172, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.821×** | -3.3 | 0.097 | 6/24 (SHP-77, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.767× | -3.1 | 0.14 | 10/20 (A498, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.769× | -3.1 | 0.14 | 11/24 (HS-578T, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 46.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.5) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.270× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 85.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.2) ⚠ cell-cycle shift, explains ~95% of this change |
| [[SW 900 (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -8.5) |
| [[A-172 (line)]] | wt | 7.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0861× (z -9.0) |
| [[A-427 (line)]] | wt | 4.20 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 3.60 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0490× (z -10.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HOP62 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.85× (z +8.9) ⚠ position not correctable | — |
| [[PANC-1 (line)]] | alt | 14.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.02× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -10.8) ⚠ cell-cycle shift, explains ~95% of this change |
| [[A549 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR16]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[SLIT3]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NID2]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PTGFR]] | +0.57 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[FBN1]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[ITGA8]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[HMCN1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ARHGEF6]] | +0.54 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[ITGA4]] | +0.53 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[DAB2]] | +0.53 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CARMN]] | +0.52 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[ADAMTS2]] | +0.51 | +0.36 / +0.59 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANK3]] | -0.45 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[SBF2-AS1]] | -0.44 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[SPHK1]] | -0.44 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[ILDR1]] | -0.43 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[ZSWIM5]] | -0.41 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[SMG9]] | -0.40 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[CEP135]] | -0.39 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[IKBKB]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[CCL3]] | -0.38 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[TIPRL]] | -0.38 | -0.42 / -0.26 | both halves | 3e-04 |  |
| [[CCDC122]] | -0.38 | -0.31 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 4, C 30. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | GXYLT2 activity raises GLIS1's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.68× lower at baseline in the lines without GXYLT2 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[TOP2A]] | B | TOP2A activity lowers GLIS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENPP2]] | B | ENPP2 activity raises GLIS1's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.79× lower at baseline in the lines without ENPP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| [[P2RX7]] | B | P2RX7 activity raises GLIS1's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without P2RX7 | 0.089 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[FBN1]] | C | FBN1 activity raises GLIS1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.39× lower at baseline in the lines without FBN1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[LAYN]] | C | LAYN activity raises GLIS1's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without LAYN | 0.004 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[HTRA3]] | C | HTRA3 activity raises GLIS1's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.05× lower at baseline in the lines without HTRA3 | 0.006 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises GLIS1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.14× lower at baseline in the lines without COL5A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[GRIK2]] | C | GRIK2 activity raises GLIS1's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 3.34× lower at baseline in the lines without GRIK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises GLIS1's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.71× lower at baseline in the lines without MAP1A | 0.009 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[PRR16]] | C | PRR16 activity raises GLIS1's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 3.70× lower at baseline in the lines without PRR16 | 0.009 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises GLIS1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 3.88× lower at baseline in the lines without ITGA4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 6, C 22. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | GLIS1 activity raises CACNA1C's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.44× lower at baseline in the lines without GLIS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[GXYLT2]] | B | GLIS1 activity raises GXYLT2's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.02× lower at baseline in the lines without GLIS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[CCDC102B]] | B | GLIS1 activity raises CCDC102B's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.93× lower at baseline in the lines without GLIS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[DZIP1L]] | B | GLIS1 activity raises DZIP1L's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.59× lower at baseline in the lines without GLIS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | GLIS1 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express GLIS1 (24) vs lines expressing it (24) | the lines without GLIS1: 1.30× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[ADGRA2]] | B | GLIS1 activity raises ADGRA2's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 1.81× lower at baseline in the lines without GLIS1 | 0.0995 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[MAP1A]] | C | GLIS1 activity raises MAP1A's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.58× lower at baseline in the lines without GLIS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[PRR16]] | C | GLIS1 activity raises PRR16's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 7.41× lower at baseline in the lines without GLIS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[BVES-AS1]] | C | GLIS1 activity raises BVES-AS1's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without GLIS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[TSHZ3-AS1]] | C | GLIS1 activity raises TSHZ3-AS1's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without GLIS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[LAYN]] | C | GLIS1 activity raises LAYN's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.22× lower at baseline in the lines without GLIS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[FBN1]] | C | GLIS1 activity raises FBN1's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 5.85× lower at baseline in the lines without GLIS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.329). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.3, 20.9); signed map (27.0, 44.0). **Vector** length 58.4, 14.0% of its response variance represented; |z| ≥ 3 in 645 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +23.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.3 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | GLIS family zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,506,237-53,739,164 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36155 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBF1](https://www.uniprot.org/uniprotkb/Q8NBF1) (Zinc finger protein GLIS1):

> Acts both as a repressor and an activator of transcription. Binds to the consensus sequence 5'-GACCACCCAC-3' (By similarity). By controlling the expression of genes involved in cell differentiation inhibits the lineage commitment of multipotent cells. Prevents, for instance, the differentiation of multipotent mesenchymal cells into adipocyte and osteoblast (By similarity).

**Summary**, from NCBI Gene [148979](https://www.ncbi.nlm.nih.gov/gene/148979):

> GLIS1 is a GLI (MIM 165220)-related Kruppel-like zinc finger protein that functions as an activator and repressor of transcription (Kim et al., 2002 [PubMed 12042312]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29525) · Entrez [148979](https://www.ncbi.nlm.nih.gov/gene/148979) · UniProt [Q8NBF1](https://www.uniprot.org/uniprotkb/Q8NBF1) · Ensembl [ENSG00000174332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174332)

## Data

Gene col 10485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10485); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10485]; `tensor/DDL_lfc|DDL_z.npy` [10485]; `embed/gene_vectors.npy` [10485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10485 or target_col == 10485). Every well: [[GLIS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLIS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
