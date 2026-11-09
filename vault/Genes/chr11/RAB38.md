---
symbol: "RAB38"
type: "gene"
col: 4463
ensembl_id: "ENSG00000123892"
name: "RAB38, member RAS oncogene family"
location: "11q14.2"
module: 120
arm: "+"
pooled_cpm: 7.48
n_lines_expressing: 27
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# RAB38

*RAB38, member RAS oncogene family* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +16.5, q 0e+00, up in 20 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0800×, LS 180 0.223×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2347 0.257×, RPMI-7951 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.105×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (KATO III 0.0861×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCN3]] (+0.60, fdr 3e-05), [[SERTAD4]] (+0.57, fdr 3e-05), [[BHLHE41]] (+0.55, fdr 2e-05); moves opposite to [[DIP2A]] (-0.58, fdr 1e-05), [[VPS13D]] (-0.55, fdr 2e-05), [[RSKR]] (-0.55, fdr 1e-04).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCN3]] → it (grade B ⚠); 3 go from it, the strongest it → [[SYNM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +16.5 | 0e+00 | 20/23 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +12.9 | 1e-35 | 4/22 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +10.8 | 7e-25 | 16/24 (SW 900, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +10.7 | 1e-24 | 13/23 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.26×** | +10.5 | 6e-24 | 19/24 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +10.1 | 4e-22 | 18/24 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.5 | 4e-12 | 6/24 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +7.4 | 1e-11 | 14/24 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.9 | 3e-10 | 9/22 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +6.8 | 5e-10 | 5/17 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +6.6 | 2e-09 | 14/24 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +6.6 | 3e-09 | 10/22 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.52×** | +5.6 | 9e-07 | 2/19 (A498, LOX-IMVI) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.5 | 1e-06 | 7/21 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 5e-04 | 6/24 (SW 900, SHP-77, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.3 | 6e-04 | 11/24 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.001 | 3/24 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.002 | 9/23 (NCI-H460, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +4.0 | 0.002 | 16/24 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4463.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0800×, LS 180 0.223×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2347 0.257×, RPMI-7951 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.105×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (KATO III 0.0861×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.6 | 0.003 | 5/25 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.779× | -3.3 | 0.15 | 8/24 (RPMI-7951, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | 0.781× | -3.3 | 0.15 | 2/24 (RKO, SK-MEL-2) | inconsistent across doses |  |
| [[5-Fluorouracil (drug)]] 0.05 µM |  | 0.786× | -3.2 | 0.15 | 0/24 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.788× | -3.2 | 0.15 | 8/24 (LS 180, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[RMC-6236 (drug)]] 5 µM |  | 0.638× | -3.1 | 0.15 | 2/23 (NCI-H460, HOP62) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.810× | -3.0 | 0.20 | 9/24 (NCI-H460, RKO, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 33.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +17.3) | — |
| [[NCI-H2347 (line)]] | alt | 41.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0800× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 3.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 3.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +10.5) | — |
| [[J82 (line)]] | alt | 8.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +9.6) | — |
| [[KATO III (line)]] | alt | 4.46 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0861× (z -8.8) |
| [[LS 180 (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H460 (line)]] | wt | 7.63 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.105× (z -12.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +10.1) | — |
| [[A-172 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.904 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCN3]] | +0.60 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[SERTAD4]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[BHLHE41]] | +0.55 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[ANOS2P]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[DPY19L2P2]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[EXTL2]] | +0.54 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ZNF462]] | +0.54 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[CD22]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TIFA]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[QPCT]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.52 | +0.42 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.58 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[VPS13D]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RSKR]] | -0.55 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.54 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[SAMD4B]] | -0.53 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[VPS53]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[GSDMB]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[GNB2]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[CHFR]] | -0.51 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ANKS3]] | -0.51 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[DRD4]] | -0.51 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[AP2A1]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN3]] | B | CCN3 activity raises RAB38's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without CCN3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNM]] | B | RAB38 activity lowers SYNM's level | lines that do not express RAB38 (23) vs lines expressing it (27) | 1.08× higher at baseline in the lines without RAB38 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000255102, TMEM154, ENSG00000233539 |
| [[RNF41]] | B | RAB38 activity lowers RNF41's level | lines that do not express RAB38 (23) vs lines expressing it (27) | 1.16× higher at baseline in the lines without RAB38 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000255102, TMEM154, ENSG00000233539 |
| [[MAGEB2]] | C | RAB38 activity raises MAGEB2's level | lines that do not express RAB38 (23) vs lines expressing it (27) | 1.96× lower at baseline in the lines without RAB38 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000255102, TMEM154, ENSG00000233539; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.199). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.6, 6.5); signed map (27.9, 6.5). **Vector** length 49.0, 9.54% of its response variance represented; |z| ≥ 3 in 600 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +16.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +3.2 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | RAB38, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:88,113,251-88,175,443 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-MEL-1 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 5 pathways, smallest: RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P57729](https://www.uniprot.org/uniprotkb/P57729) (Ras-related protein Rab-38):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB38 may be involved in melanosomal transport and docking. Involved in the proper sorting of TYRP1. …

**Summary**, from NCBI Gene [23682](https://www.ncbi.nlm.nih.gov/gene/23682):

> Enables several functions, including AP-1 adaptor complex binding activity; AP-3 adaptor complex binding activity; and BLOC-2 complex binding activity. Involved in several processes, including endosome to melanosome transport; melanosome assembly; and phagosome acidification. Located in several cellular components, including cytoplasmic vesicle; lysosome; and mitochondria-associated endoplasmic reticulum membrane contact site. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9776) · Entrez [23682](https://www.ncbi.nlm.nih.gov/gene/23682) · UniProt [P57729](https://www.uniprot.org/uniprotkb/P57729) · Ensembl [ENSG00000123892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123892)

## Data

Gene col 4463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4463); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4463]; `tensor/DDL_lfc|DDL_z.npy` [4463]; `embed/gene_vectors.npy` [4463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4463 or target_col == 4463). Every well: [[RAB38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
