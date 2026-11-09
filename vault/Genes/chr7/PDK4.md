---
symbol: "PDK4"
type: "gene"
col: 54
ensembl_id: "ENSG00000004799"
name: "pyruvate dehydrogenase kinase 4"
location: "7q21.3"
module: 106
arm: "+"
pooled_cpm: 21.59
n_lines_expressing: 25
n_dd_up: 39
n_dd_down: 13
n_dd_up_clean: 36
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# PDK4

*pyruvate dehydrogenase kinase 4* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (3 with an alert ⚠); the strongest is [[Mifepristone (drug)]] 0.5 µM: 2.71× (z +9.1, q 8e-17, up in 19 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.497× (z -6.4, q 1e-07, down in 17 of 23 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.727× (z -4.0, q 0.014, down in 16 of 23 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC7A2]] (+0.62, fdr 1e-05), [[GAREM1]] (+0.61, fdr 1e-05), [[TIPARP]] (+0.60, fdr 2e-05); moves opposite to [[CAPN2]] (-0.52, fdr 3e-05), [[ADCY7]] (-0.49, fdr 3e-05), [[BMAL2]] (-0.45, fdr 4e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PBX1]] → it (grade C ⚠); 15 go from it, the strongest it → [[MICALL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 54.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mifepristone (drug)]] 0.5 µM |  | **2.71×** | +9.1 | 8e-17 | 19/23 (CFPAC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.60×** | +8.7 | 1e-15 | 11/23 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Mifepristone (drug)]] 5 µM |  | **2.48×** | +7.9 | 4e-13 | 18/23 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.12×** | +6.8 | 1e-09 | 10/23 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **2.10×** | +6.7 | 2e-09 | 16/23 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Rosiglitazone (drug)]] 5 µM |  | **2.15×** | +6.7 | 2e-09 | 18/23 (Hs 766T, LoVo, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.03×** | +6.4 | 1e-08 | 13/23 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +5.4 | 4e-06 | 7/23 (AN3 CA, SHP-77, …) | rises with dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.80×** | +5.4 | 5e-06 | 16/23 (SNU-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.83×** | +5.3 | 6e-06 | 12/23 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.50×** | +5.1 | 1e-05 | 13/23 (LoVo, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +5.1 | 1e-05 | 15/23 (SHP-77, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 0.05 µM |  | **1.79×** | +4.9 | 4e-05 | 17/23 (BT-474, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.71×** | +4.9 | 5e-05 | 10/23 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.6 | 2e-04 | 3/21 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.001 | 8/23 (SHP-77, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 54.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.497×** | -6.4 | 1e-07 | 17/23 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.727×** | -4.0 | 0.014 | 16/23 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.640×** | -3.9 | 0.014 | 15/23 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.652×** | -3.9 | 0.014 | 14/23 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.741×** | -3.7 | 0.023 | 16/23 (SHP-77, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.467×** | -3.6 | 0.029 | 12/23 (BT-474, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.682×** | -3.5 | 0.037 | 18/23 (SHP-77, LS 180, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.683×** | -3.5 | 0.037 | 12/23 (NCI-H2030, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.684×** | -3.4 | 0.037 | 13/23 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.688×** | -3.4 | 0.037 | 14/22 (SNU-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.674×** | -3.4 | 0.037 | 2/23 (LoVo, SW480) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.496×** | -3.3 | 0.041 | 16/23 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -3.2 | 0.062 | 9/23 (SHP-77, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 54. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 185 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -28.1) |
| [[NCI-H460 (line)]] | wt | 50.2 | 2 (1 ⚠) | 6 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.25× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 4.66× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -12.9) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.185× (z -9.3) |
| [[AN3 CA (line)]] | alt | 300 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0402× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.160× (z -14.8) |
| [[A-427 (line)]] | wt | 298 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 18.9 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 5.42× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.131× (z -8.9) |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 50.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -8.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.5) |
| [[LS 180 (line)]] | wt | 6.50 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0489× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0677× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.115× (z -9.0) |
| [[A-172 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 54), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC7A2]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[GAREM1]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[TIPARP]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[BCL6]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[AKR1C2]] | +0.55 | +0.45 / +0.48 | both halves | 3e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[FGG]] | +0.54 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[CCND3]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[IRS2]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 | STRING 453 |
| [[HOPX]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[LINC00511]] | +0.53 | +0.44 / +0.39 | both halves | 6e-05 |  |
| [[FGL1]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN2]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ADCY7]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[BMAL2]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MICALL1]] | -0.45 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[C6orf141]] | -0.45 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[DPP9]] | -0.44 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[KCTD13]] | -0.44 | -0.21 / -0.53 | both halves | 6e-04 |  |
| [[ZNF83]] | -0.43 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[PVR]] | -0.43 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[KLC1]] | -0.43 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[PLEKHG5]] | -0.43 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[MYH16]] | -0.43 | -0.39 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBX1]] | C | PBX1 activity raises PDK4's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without PBX1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9; co-absent with the target |
| [[MTUS1]] | C | MTUS1 activity raises PDK4's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.77× lower at baseline in the lines without MTUS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICALL1]] | B | PDK4 activity lowers MICALL1's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 1.56× higher at baseline in the lines without PDK4 | 0.011 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[PDE4D]] | B | PDK4 activity raises PDE4D's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without PDK4 | 0.016 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[RHOU]] | B | PDK4 activity raises RHOU's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without PDK4 | 0.043 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[IRS2]] | B | PDK4 activity raises IRS2's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 1.62× lower at baseline in the lines without PDK4 | 0.058 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[PELI2]] | B | PDK4 activity raises PELI2's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without PDK4 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[ALDH3B1]] | B | PDK4 activity strengthens ALDH3B1's drug response | lines that do not express PDK4 (20) vs lines expressing it (19) | the lines without PDK4 respond 0.60× as strongly (z diff +2.07); strongest at Digitoxin 5 µM: 0.47x vs 0.23x (z diff +3.4) | 0.063 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA; target measured in part of the lines; artifact flags |
| [[EPS8]] | B | PDK4 activity raises EPS8's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without PDK4 | 0.066 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[AKR1C3]] | B | PDK4 activity raises AKR1C3's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.38× lower at baseline in the lines without PDK4 | 0.067 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[GAREM1]] | B | PDK4 activity raises GAREM1's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without PDK4 | 0.072 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[PELI1]] | B | PDK4 activity raises PELI1's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without PDK4 | 0.075 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[RORA]] | B | PDK4 activity raises RORA's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 1.68× lower at baseline in the lines without PDK4 | 0.077 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| cells under [[Isocorydine (drug)]] 5 µM | B | PDK4 activity raises the cells' numbers under Isocorydine 5 µM (protects the cells) | lines that do not express PDK4 (25) vs lines expressing it (23) | the lines without PDK4: 0.89× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.7, 18.5); signed map (52.0, 11.9). **Vector** length 76.3, 18.9% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.3 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.9 | -2.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +6.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +8.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +6.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.7 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.6 | -2.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.5 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:95,583,499-95,596,516 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pyruvate dehydrogenase kinase family |
| Hallmark sets | XENOBIOTIC_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 11 pathways, smallest: Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism; Signaling by Retinoic Acid |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16654](https://www.uniprot.org/uniprotkb/Q16654) ([Pyruvate dehydrogenase (acetyl-transferring)] kinase isozyme 4, mitochondrial):

> Kinase that plays a key role in regulation of glucose and fatty acid metabolism and homeostasis via phosphorylation of the pyruvate dehydrogenase subunits PDHA1 and PDHA2. This inhibits pyruvate dehydrogenase activity, and thereby regulates metabolite flux through the tricarboxylic acid cycle, down-regulates aerobic respiration and inhibits the formation of acetyl-coenzyme A from pyruvate. Inhibition of pyruvate dehydrogenase decreases glucose utilization and increases fat metabolism in …

**Summary**, from NCBI Gene [5166](https://www.ncbi.nlm.nih.gov/gene/5166):

> This gene is a member of the PDK/BCKDK protein kinase family and encodes a mitochondrial protein with a histidine kinase domain. This protein is located in the matrix of the mitrochondria and inhibits the pyruvate dehydrogenase complex by phosphorylating one of its subunits, thereby contributing to the regulation of glucose metabolism. Expression of this gene is regulated by glucocorticoids, retinoic acid and insulin. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8812) · Entrez [5166](https://www.ncbi.nlm.nih.gov/gene/5166) · UniProt [Q16654](https://www.uniprot.org/uniprotkb/Q16654) · Ensembl [ENSG00000004799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004799)

## Data

Gene col 54: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 54); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 54, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 54]; `tensor/DDL_lfc|DDL_z.npy` [54]; `embed/gene_vectors.npy` [54]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 54 or target_col == 54). Every well: [[PDK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
