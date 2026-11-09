---
symbol: "P2RY1"
type: "gene"
col: 9862
ensembl_id: "ENSG00000169860"
name: "purinergic receptor P2Y1"
location: "3q25.2"
module: 61
arm: "+"
pooled_cpm: 4.07
n_lines_expressing: 29
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# P2RY1

*purinergic receptor P2Y1* — 3q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.92× (z +15.0, q 0e+00, up in 22 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.108×; ⚠ toxic; cell-cycle shift, explains ~46% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.235×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLXNC1]] (+0.57, fdr 1e-05), [[PLAAT1]] (+0.57, fdr 1e-05), [[CACNA1E]] (+0.56, fdr 3e-05); moves opposite to [[RNF41]] (-0.51, fdr 2e-04), [[ATF7]] (-0.50, fdr 2e-05), [[DGCR2]] (-0.50, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NYAP2]] → it (grade B ⚠); 5 go from it, the strongest it → [[NIPAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.92×** | +15.0 | 0e+00 | 22/25 (NCI-H460, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +11.4 | 1e-27 | 10/21 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +11.0 | 1e-25 | 10/19 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +10.7 | 1e-24 | 1/5 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +10.1 | 6e-22 | 7/13 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.72×** | +9.9 | 2e-21 | 18/23 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +7.8 | 6e-13 | 3/9 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +7.1 | 9e-11 | 3/26 (J82, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +6.9 | 3e-10 | 4/11 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +5.5 | 2e-06 | 7/25 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.06×** | +5.1 | 2e-05 | 1/7 (LS 180) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.6 | 2e-04 | 9/25 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.5 | 3e-04 | 5/16 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.83×** | +4.3 | 7e-04 | 1/13 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.3 | 7e-04 | 2/10 (J82, LS 180) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.002 | 3/16 (HT-29, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +3.6 | 0.010 | 9/21 (NCI-H1573, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.021 | 11/27 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.033 | 3/19 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.045 | 4/25 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.066 | 8/21 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9862.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.108×; ⚠ toxic; cell-cycle shift, explains ~46% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.235×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.710× | -3.4 | 0.35 | 12/27 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Malotilate (drug)]] 0.5 µM |  | 0.725× | -3.2 | 0.37 | 5/24 (RKO, A-427, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 6.54 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +10.0) | — |
| [[A498 (line)]] | wt | 2.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +10.7) | — |
| [[A549 (line)]] | wt | 1.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 61.5× (z +18.3) | — |
| [[J82 (line)]] | alt | 8.21 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[LS 180 (line)]] | wt | 8.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 1.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.7× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +11.7) | — |
| [[A-172 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.391 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNC1]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PLAAT1]] | +0.57 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CACNA1E]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ERG]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[IKZF3]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[GRIK4]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[CAMK4]] | +0.53 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[ABCA13]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[RASGRP1]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 | pathway: G alpha (q) signalling events |
| [[FABP5]] | +0.52 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[THSD7B]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[LINC01933]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF41]] | -0.51 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[ATF7]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[DGCR2]] | -0.50 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[MIGA2]] | -0.49 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[TSC2]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[POLR2J4]] | -0.45 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[DHTKD1]] | -0.44 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[NUBP2]] | -0.43 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[CBFA2T2]] | -0.43 | -0.46 / -0.23 | both halves | 5e-04 |  |
| [[XKR8]] | -0.42 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[SHARPIN]] | -0.42 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[PSMD9]] | -0.42 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NYAP2]] | B | NYAP2 activity raises P2RY1's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 1.67× lower at baseline in the lines without NYAP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[MECOM]] | B | MECOM activity raises P2RY1's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without MECOM | 0.092 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIPAL1]] | B | P2RY1 activity raises NIPAL1's level | lines that do not express P2RY1 (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without P2RY1 | 0.040 | ⚠ within organs, on part of the lines; also absent: RGS2, FGF14, BASP1-AS1 |
| [[AFF2]] | B | P2RY1 activity lowers AFF2's level | lines that do not express P2RY1 (21) vs lines expressing it (29) | 1.10× higher at baseline in the lines without P2RY1 | 0.066 | ⚠ within organs, on part of the lines; also absent: RGS2, FGF14, BASP1-AS1 |
| [[MECOM]] | B | P2RY1 activity raises MECOM's level | lines that do not express P2RY1 (21) vs lines expressing it (29) | 2.14× lower at baseline in the lines without P2RY1 | 0.076 | ⚠ within organs, on part of the lines; also absent: RGS2, FGF14, BASP1-AS1 |
| cells under [[Mozavaptan (drug)]] 0.5 µM | B | P2RY1 activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express P2RY1 (21) vs lines expressing it (27) | the lines without P2RY1: 1.15× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: RGS2, FGF14, BASP1-AS1 |
| [[CA13]] | B | P2RY1 activity raises CA13's level | lines that do not express P2RY1 (21) vs lines expressing it (29) | 1.77× lower at baseline in the lines without P2RY1 | 0.096 | ⚠ within organs, on part of the lines; also absent: RGS2, FGF14, BASP1-AS1 |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 29.6); signed map (31.4, 21.9). **Vector** length 43.1, 7.17% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -0.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | +3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.0 | +0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -0.8 | +0.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | purinergic receptor P2Y1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.2 — chr3:152,835,131-152,841,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P2Y1, SARCC |
| Gene groups (HGNC) | P2Y receptors |
| Hallmark sets | COAGULATION |
| Reactome | 11 pathways, smallest: P2Y receptors; Nucleotide-like (purinergic) receptors; ADP signalling through P2Y purinoceptor 1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P47900](https://www.uniprot.org/uniprotkb/P47900) (P2Y purinoceptor 1):

> Receptor for extracellular adenine nucleotides such as ADP. In platelets, binding to ADP leads to mobilization of intracellular calcium ions via activation of phospholipase C, a change in platelet shape, and ultimately platelet aggregation.

**Summary**, from NCBI Gene [5028](https://www.ncbi.nlm.nih.gov/gene/5028):

> The product of this gene belongs to the family of G-protein coupled receptors. This family has several receptor subtypes with different pharmacological selectivity, which overlaps in some cases, for various adenosine and uridine nucleotides. This receptor functions as a receptor for extracellular ATP and ADP. In platelets binding to ADP leads to mobilization of intracellular calcium ions via activation of phospholipase C, a change in platelet shape, and probably to platelet aggregation. …

**Accessions** — [HGNC:8539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8539) · Entrez [5028](https://www.ncbi.nlm.nih.gov/gene/5028) · UniProt [P47900](https://www.uniprot.org/uniprotkb/P47900) · Ensembl [ENSG00000169860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169860)

## Data

Gene col 9862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9862); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9862]; `tensor/DDL_lfc|DDL_z.npy` [9862]; `embed/gene_vectors.npy` [9862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9862 or target_col == 9862). Every well: [[P2RY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P2RY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
