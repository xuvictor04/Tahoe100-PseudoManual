---
symbol: "TDRP"
type: "gene"
col: 11086
ensembl_id: "ENSG00000180190"
name: "testis development related protein"
location: "8p23.3"
module: 162
arm: "+"
pooled_cpm: 22.61
n_lines_expressing: 27
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# TDRP

*testis development related protein* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.72× (z +28.8, q 0e+00, up in 20 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.734× (z -8.9, q 2e-16, down in 17 of 25 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD99P1-1]] (+0.64, fdr 1e-05), [[MAST1]] (+0.58, fdr 1e-05), [[CCDC112]] (+0.56, fdr 4e-05); moves opposite to [[C5orf15]] (-0.51, fdr 5e-05), [[PSKH1]] (-0.49, fdr 1e-04), [[PIK3R4]] (-0.49, fdr 1e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +28.8 | 0e+00 | 20/25 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +13.3 | 7e-38 | 19/24 (NCI-H2347, C-33 A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +9.0 | 6e-17 | 19/25 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +8.5 | 3e-15 | 20/24 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +8.3 | 2e-14 | 18/24 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.7 | 2e-09 | 13/24 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +6.5 | 7e-09 | 13/24 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.8 | 4e-07 | 14/24 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +5.6 | 2e-06 | 12/24 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.19× | +5.1 | 2e-05 | 8/25 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.5 | 4e-04 | 12/24 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.002 | 11/24 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.002 | 11/24 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.0 | 0.003 | 8/20 (NCI-H1573, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.6 | 0.011 | 5/25 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.021 | 6/25 (C-33 A, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.084 | 3/24 (NCI-H2347, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -8.9 | 2e-16 | 17/25 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.752×** | -8.2 | 5e-14 | 17/25 (NCI-H2347, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -6.9 | 1e-09 | 12/24 (HOP62, A549, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -6.3 | 5e-08 | 15/24 (NCI-H2030, H4, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -6.2 | 5e-08 | 14/24 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.768×** | -5.4 | 6e-06 | 14/24 (CHP-212, C-33 A, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -4.1 | 0.003 | 7/25 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.821×** | -4.0 | 0.004 | 14/24 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.847× | -3.4 | 0.043 | 4/24 (NCI-H460, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.1 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +36.0) | — |
| [[NCI-H2347 (line)]] | alt | 67.1 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +30.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.8) |
| [[A-427 (line)]] | wt | 104 | 2 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.59× (z +12.0) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.597× (z -9.2) |
| [[A498 (line)]] | wt | 14.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +17.0) | — |
| [[A549 (line)]] | wt | 64.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 103 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.72× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H1573 (line)]] | alt | 49.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +34.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 33.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +31.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.5) |
| [[BT-474 (line)]] | alt | 41.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 38.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H1792 (line)]] | alt | 38.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H23 (line)]] | alt | 35.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.4) |
| [[SHP-77 (line)]] | alt | 69.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.80× (z +10.5) | — |
| [[A-172 (line)]] | wt | 5.71 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0890× (z -9.8) |
| [[CHP-212 (line)]] | wt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0746× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 56.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -10.5) |
| [[HOP62 (line)]] | alt | 23.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -8.8) |
| [[J82 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +15.9) | — |
| [[AN3 CA (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD99P1-1]] | +0.64 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[MAST1]] | +0.58 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CCDC112]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ASMTL]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[NCKAP5L]] | +0.54 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SHF]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[CD99P1]] | +0.54 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[GNG7]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[BCORL1]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CARMIL2]] | +0.51 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[ATP1A3]] | +0.50 | +0.29 / +0.53 | both halves | 2e-04 |  |
| [[DUSP2]] | +0.50 | +0.42 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf15]] | -0.51 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[PSKH1]] | -0.49 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PIK3R4]] | -0.49 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[PGM1]] | -0.49 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ITFG1]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PANK1]] | -0.47 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[ANKFY1]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[NDOR1]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[CASP8AP2]] | -0.45 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[LEMD3]] | -0.44 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[ENTPD3-AS1]] | -0.44 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[ARID1A]] | -0.43 | -0.29 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TDRP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises TDRP's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PTCHD1]] | C | PTCHD1 activity raises TDRP's level | lines that do not express PTCHD1 (32) vs lines expressing it (18) | 3.71× lower at baseline in the lines without PTCHD1 | 0.079 | ⚠ within organs, on part of the lines; also absent: EPGN, ENSG00000260958, DCN; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, -0.7); signed map (-24.0, 27.6). **Vector** length 61.3, 14.1% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +28.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +13.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | +2.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -6.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -8.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | testis development related protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.3 — chr8:489,803-545,781 (-) |
| Ensembl biotype | protein_coding |
| Also known as | INM01, TDRP1, TDRP2; previously C8orf42 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YL5](https://www.uniprot.org/uniprotkb/Q86YL5) (Testis development-related protein):

> Contributes to normal sperm motility, but not essential for male fertility.

**Summary**, from NCBI Gene [157695](https://www.ncbi.nlm.nih.gov/gene/157695):

> Acts upstream of or within spermatogenesis. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26951) · Entrez [157695](https://www.ncbi.nlm.nih.gov/gene/157695) · UniProt [Q86YL5](https://www.uniprot.org/uniprotkb/Q86YL5) · Ensembl [ENSG00000180190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180190)

## Data

Gene col 11086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11086); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11086]; `tensor/DDL_lfc|DDL_z.npy` [11086]; `embed/gene_vectors.npy` [11086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11086 or target_col == 11086). Every well: [[TDRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
