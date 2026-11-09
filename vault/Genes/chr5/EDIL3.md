---
symbol: "EDIL3"
type: "gene"
col: 8893
ensembl_id: "ENSG00000164176"
name: "EGF like and discoidin domains 3"
location: "5q14.3"
module: 19
arm: "+"
pooled_cpm: 84.09
n_lines_expressing: 22
n_dd_up: 12
n_dd_down: 36
n_dd_up_clean: 8
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 18
direction_downstream: 24
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# EDIL3

*EGF like and discoidin domains 3* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +15.3, q 0e+00, up in 14 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +11.5, q 2e-28, up in 6 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.637× (z -10.4, q 2e-22, down in 19 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAF]] (+0.71, fdr 7e-06), [[TRPA1]] (+0.68, fdr 1e-05), [[EDIL3-DT]] (+0.64, fdr 7e-06, ⚠ same locus), [[NHS]] (+0.63, fdr 1e-05); moves opposite to [[OSBPL5]] (-0.51, fdr 2e-05), [[C16orf74]] (-0.47, fdr 6e-05), [[BCL2L1]] (-0.46, fdr 6e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[NFATC4]] → it (grade B ⚠); 24 go from it, the strongest it → [[NFATC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +15.3 | 0e+00 | 14/19 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +12.3 | 4e-32 | 13/18 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +11.5 | 2e-28 | 6/20 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +9.5 | 2e-19 | 7/18 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +8.3 | 8e-15 | 11/20 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.6 | 3e-09 | 0/20 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 8e-07 | 10/20 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.002 | 0/20 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.010 | 14/20 (HOP62, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.024 | 12/20 (HOP62, H4, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.024 | 10/20 (HOP62, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.4 | 0.034 | 4/18 (HOP62, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.036 | 12/20 (HOP62, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.637×** | -10.4 | 2e-22 | 19/20 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.551×** | -9.7 | 1e-19 | 15/20 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.602×** | -8.2 | 3e-14 | 18/20 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.673×** | -6.4 | 2e-08 | 11/20 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.711×** | -5.5 | 3e-06 | 7/20 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.714×** | -5.5 | 4e-06 | 9/20 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.716×** | -5.4 | 5e-06 | 12/20 (A-172, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.804×** | -5.0 | 4e-05 | 11/20 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.744×** | -4.8 | 1e-04 | 8/20 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.747×** | -4.7 | 1e-04 | 11/20 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.752×** | -4.6 | 2e-04 | 14/20 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.584×** | -4.6 | 2e-04 | 17/20 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.758×** | -4.5 | 3e-04 | 13/20 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.759×** | -4.5 | 3e-04 | 17/20 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.760×** | -4.4 | 3e-04 | 10/20 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.598×** | -4.4 | 4e-04 | 16/20 (NCI-H2347, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.756×** | -4.4 | 4e-04 | 16/20 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.609×** | -4.2 | 8e-04 | 12/20 (SHP-77, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 57.9 | 0 | 22 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0589× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 611 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -16.2) |
| [[HOP62 (line)]] | alt | 117 | 6 (1 ⚠) | 0 | [[Cobimetinib (drug)]] 5 µM 4.64× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 52.4 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 1.78× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.334× (z -10.8) |
| [[SNU-423 (line)]] | alt | 753 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.5) |
| [[A-172 (line)]] | wt | 45.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.0) |
| [[PANC-1 (line)]] | alt | 28.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 238 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.269× (z -8.9) ⚠ cell-cycle shift, explains ~3% of this change |
| [[HS-578T (line)]] | alt | 433 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 250 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -12.5) |
| [[SHP-77 (line)]] | alt | 69.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.8) |
| [[A-427 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.69 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 446 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.80 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAF]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[TRPA1]] | +0.68 | +0.55 / +0.73 | both halves | 1e-05 | **novel candidate** |
| [[EDIL3-DT]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NHS]] | +0.63 | +0.71 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[MOXD1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HMCN1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[UPK1B]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[NOVA1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[COL3A1]] | +0.56 | +0.45 / +0.60 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[C5orf46]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RAB27B]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[FBN1]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[PLD1]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL5]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[C16orf74]] | -0.47 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[BCL2L1]] | -0.46 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[SH3TC1]] | -0.46 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[CSF3]] | -0.46 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[ZC3H8]] | -0.45 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[FOXC2]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 3, C 15. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC4]] | B | NFATC4 activity raises EDIL3's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 2.79× lower at baseline in the lines without NFATC4 | 0.043 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[CCDC80]] | B | CCDC80 activity raises EDIL3's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.51× lower at baseline in the lines without CCDC80 | 0.051 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[NR3C1]] | B | NR3C1 activity lowers EDIL3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[IL6]] | C | IL6 activity raises EDIL3's level | lines that do not express IL6 (32) vs lines expressing it (18) | 10.31× lower at baseline in the lines without IL6 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[EDIL3-DT]] | C | EDIL3-DT activity raises EDIL3's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 10.12× lower at baseline in the lines without EDIL3-DT | 0.003 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA; co-absent with the target |
| [[COL8A1]] | C | COL8A1 activity raises EDIL3's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 7.16× lower at baseline in the lines without COL8A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[TGFBI]] | C | TGFBI activity raises EDIL3's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 4.69× lower at baseline in the lines without TGFBI | 0.016 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises EDIL3's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 5.29× lower at baseline in the lines without FOXC2 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[EFEMP1]] | C | EFEMP1 activity raises EDIL3's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 5.65× lower at baseline in the lines without EFEMP1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises EDIL3's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 4.88× lower at baseline in the lines without BICC1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |
| [[CPA4]] | C | CPA4 activity raises EDIL3's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 4.10× lower at baseline in the lines without CPA4 | 0.042 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[SLC4A4]] | C | SLC4A4 activity raises EDIL3's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 2.82× lower at baseline in the lines without SLC4A4 | 0.053 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 6, C 18. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC4]] | B | EDIL3 activity raises NFATC4's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without EDIL3 | 0.003 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[TENT5A]] | B | EDIL3 activity raises TENT5A's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 3.37× lower at baseline in the lines without EDIL3 | 0.025 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[PDE5A]] | B | EDIL3 activity raises PDE5A's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without EDIL3 | 0.035 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[NR3C1]] | B | EDIL3 activity raises NR3C1's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 4.60× lower at baseline in the lines without EDIL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[ARHGEF6]] | B | EDIL3 activity raises ARHGEF6's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without EDIL3 | 0.080 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[CCDC80]] | B | EDIL3 activity raises CCDC80's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without EDIL3 | 0.085 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[IL6]] | C | EDIL3 activity raises IL6's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 7.52× lower at baseline in the lines without EDIL3 | 0.002 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[EFEMP1]] | C | EDIL3 activity raises EFEMP1's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 4.29× lower at baseline in the lines without EDIL3 | 0.006 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[NHS]] | C | EDIL3 activity raises NHS's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 4.67× lower at baseline in the lines without EDIL3 | 0.006 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[EYA1]] | C | EDIL3 activity raises EYA1's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 3.21× lower at baseline in the lines without EDIL3 | 0.007 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[COL1A1]] | C | EDIL3 activity raises COL1A1's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 7.29× lower at baseline in the lines without EDIL3 | 0.013 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[TGFBI]] | C | EDIL3 activity raises TGFBI's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 4.24× lower at baseline in the lines without EDIL3 | 0.014 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.413). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.5, 22.3); signed map (37.5, 46.3). **Vector** length 89.4, 30.8% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.9 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.4 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +11.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -5.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -4.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.1 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | EGF like and discoidin domains 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:83,940,554-84,384,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DEL1 |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition; MITF-M-dependent gene expression; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [O43854](https://www.uniprot.org/uniprotkb/O43854) (EGF-like repeat and discoidin I-like domain-containing protein 3):

> Promotes adhesion of endothelial cells through interaction with the alpha-v/beta-3 integrin receptor. Inhibits formation of vascular-like structures. May be involved in regulation of vascular morphogenesis of remodeling in embryonic development.

**Summary**, from NCBI Gene [10085](https://www.ncbi.nlm.nih.gov/gene/10085):

> The protein encoded by this gene is an integrin ligand. It plays an important role in mediating angiogenesis and may be important in vessel wall remodeling and development. It also influences endothelial cell behavior. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3173) · Entrez [10085](https://www.ncbi.nlm.nih.gov/gene/10085) · UniProt [O43854](https://www.uniprot.org/uniprotkb/O43854) · Ensembl [ENSG00000164176](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164176)

## Data

Gene col 8893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8893); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8893]; `tensor/DDL_lfc|DDL_z.npy` [8893]; `embed/gene_vectors.npy` [8893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8893 or target_col == 8893). Every well: [[EDIL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDIL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
