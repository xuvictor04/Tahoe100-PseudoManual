---
symbol: "BAIAP3"
type: "gene"
col: 148
ensembl_id: "ENSG00000007516"
name: "BAI1 associated protein 3"
location: "16p13.3"
module: 161
arm: "+"
pooled_cpm: 6.09
n_lines_expressing: 42
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 15
direction_downstream: 9
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# BAIAP3

*BAI1 associated protein 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 9.84× (z +19.7, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.496× (z -6.0, q 1e-06, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL26]] (+0.74, fdr 7e-06), [[FCHO1]] (+0.71, fdr 1e-05), [[FCHSD1]] (+0.68, fdr 1e-05); moves opposite to [[QRSL1]] (-0.65, fdr 1e-05), [[AP5M1]] (-0.65, fdr 1e-04), [[CPSF2]] (-0.64, fdr 1e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[VSIR]] → it (grade B ⚠); 9 go from it, the strongest it → [[F11R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **9.84×** | +19.7 | 0e+00 | 38/38 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.07×** | +16.8 | 0e+00 | 36/36 (A549, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.55×** | +13.0 | 1e-36 | 34/36 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +9.3 | 2e-18 | 27/38 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.43×** | +7.6 | 3e-12 | 24/37 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.15×** | +4.7 | 2e-04 | 14/29 (HepG2/C3A, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.72×** | +4.5 | 5e-04 | 17/35 (A549, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.99×** | +4.2 | 0.002 | 10/32 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +4.2 | 0.002 | 13/34 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.027 | 9/31 (LS 180, Panc 03.27, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.52×** | +3.4 | 0.034 | 11/38 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.72×** | +3.3 | 0.040 | 9/32 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.065 | 5/36 (HS-578T, SK-MEL-2, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.084 | 6/31 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.496×** | -6.0 | 1e-06 | 22/37 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.522×** | -5.5 | 7e-06 | 19/35 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.524×** | -5.5 | 7e-06 | 18/37 (SW480, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.552×** | -5.1 | 6e-05 | 15/35 (SW480, Panc 03.27, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.365×** | -4.5 | 8e-04 | 14/31 (PANC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.601×** | -4.2 | 0.003 | 16/36 (SW480, RPMI-7951, …) | two highest doses | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -4.1 | 0.004 | 18/32 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -4.0 | 0.004 | 21/32 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.620×** | -3.9 | 0.006 | 19/23 (SK-MEL-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.653×** | -3.6 | 0.017 | 17/39 (SK-MEL-2, Hs 766T, …) | all doses, flat | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -3.5 | 0.025 | 16/29 (SW 900, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.691×** | -3.1 | 0.081 | 18/36 (SW480, A549, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.695×** | -3.1 | 0.089 | 8/37 (SW480, CHP-212, …) | all doses, flat | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.504×** | -3.1 | 0.089 | 6/29 (NCI-H2347, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.679×** | -3.0 | 0.089 | 8/37 (A549, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -10.2) |
| [[SW480 (line)]] | alt | 12.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.30× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 5.58 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.8× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 5.92 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.31× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 3.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0820× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 9.00 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.29× (z +8.6) | — |
| [[LoVo (line)]] | wt | 7.86 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.90× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 5.93 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.1× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 6.72 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0490× (z -10.6) |
| [[PANC-1 (line)]] | alt | 6.38 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0715× (z -10.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0517× (z -11.0) |
| [[SW1417 (line)]] | alt | 4.47 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +8.5) | — |
| [[A-172 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL26]] | +0.74 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[FCHO1]] | +0.71 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.68 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.68 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CBX7]] | +0.67 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ABTB1]] | +0.66 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[MAST3]] | +0.66 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[SLC27A1]] | +0.66 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[KLC3]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.65 | +0.52 / +0.31 | both halves | 2e-04 |  |
| [[EPHB3]] | +0.65 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[FBXL16]] | +0.65 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRSL1]] | -0.65 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[AP5M1]] | -0.65 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[CPSF2]] | -0.64 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[TDRD3]] | -0.64 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[VBP1]] | -0.62 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[DECR1]] | -0.61 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ANGEL2]] | -0.61 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MYLK-AS1]] | -0.60 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[TBC1D5]] | -0.60 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[METTL4]] | -0.59 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[CRPPA]] | -0.59 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ZMYND11]] | -0.59 | -0.39 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSIR]] | B | VSIR activity raises BAIAP3's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without VSIR | 0.005 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[CLMN]] | B | CLMN activity raises BAIAP3's level | lines that do not express CLMN (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without CLMN | 0.025 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[PTGS1]] | B | PTGS1 activity strengthens BAIAP3's drug response | lines that do not express PTGS1 (19) vs lines expressing it (19) | the lines without PTGS1 respond 0.74× as strongly (z diff +0.79); strongest at Panobinostat 0.05 µM: 1.93x vs 2.94x (z diff +1.3) | 0.034 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1; target measured in part of the lines; artifact flags |
| [[ATG9B]] | B | ATG9B activity raises BAIAP3's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.05× lower at baseline in the lines without ATG9B | 0.036 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[EPHB3]] | B | EPHB3 activity raises BAIAP3's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.61× lower at baseline in the lines without EPHB3 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[MLXIPL]] | B | MLXIPL activity raises BAIAP3's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without MLXIPL | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[CCDC120]] | B | CCDC120 activity raises BAIAP3's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.83× lower at baseline in the lines without CCDC120 | 0.052 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[CAMSAP3]] | B | CAMSAP3 activity raises BAIAP3's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without CAMSAP3 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[TINAGL1]] | B | TINAGL1 activity raises BAIAP3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without TINAGL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[MYO15B]] | B | MYO15B activity raises BAIAP3's level | lines that do not express MYO15B (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without MYO15B | 0.060 | ⚠ within organs, on part of the lines; also absent: ID2, ASRGL1, CTNNA3; maybe low, not absent; its own permutation p |
| [[IRF6]] | B | IRF6 activity raises BAIAP3's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.61× lower at baseline in the lines without IRF6 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[F11R]] | B | F11R activity raises BAIAP3's level | lines that do not express F11R (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without F11R | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11R]] | B | BAIAP3 activity raises F11R's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 2.12× lower at baseline in the lines without BAIAP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[LMTK3]] | B | BAIAP3 activity raises LMTK3's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without BAIAP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[CARD10]] | B | BAIAP3 activity raises CARD10's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without BAIAP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[CCDC120]] | B | BAIAP3 activity raises CCDC120's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without BAIAP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[AHDC1]] | B | BAIAP3 activity raises AHDC1's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without BAIAP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[SUN1]] | B | BAIAP3 activity raises SUN1's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.09× lower at baseline in the lines without BAIAP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent |
| [[PDGFB]] | B | BAIAP3 activity raises PDGFB's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 2.76× lower at baseline in the lines without BAIAP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[CAMSAP3]] | B | BAIAP3 activity raises CAMSAP3's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without BAIAP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[TNK2]] | B | BAIAP3 activity raises TNK2's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.23× lower at baseline in the lines without BAIAP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.5, -3.2); signed map (-22.3, 27.6). **Vector** length 86.2, 20.5% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.9 | +19.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.9 | +16.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +4.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | BAI1 associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,333,638-1,349,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAP3, KIAA0734 |
| Gene groups (HGNC) | C2 domain containing; UNC13 homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [O94812](https://www.uniprot.org/uniprotkb/O94812) (BAI1-associated protein 3):

> Functions in endosome to Golgi retrograde transport. In response to calcium influx, may interact with SNARE fusion receptors and membrane phospholipids to mediate endosome fusion with the trans-Golgi network. By promoting the recycling of secretory vesicle transmembrane proteins, it indirectly controls dense-core secretory vesicle biogenesis, maturation and their ability to mediate the constitutive and regulated secretion of neurotransmitters and hormones. May regulate behavior and food intake …

**Summary**, from NCBI Gene [8938](https://www.ncbi.nlm.nih.gov/gene/8938):

> This p53-target gene encodes a brain-specific angiogenesis inhibitor. The protein is a seven-span transmembrane protein and a member of the secretin receptor family. It interacts with the cytoplasmic region of brain-specific angiogenesis inhibitor 1. This protein also contains two C2 domains, which are often found in proteins involved in signal transduction or membrane trafficking. Its expression pattern and similarity to other proteins suggest that it may be involved in synaptic functions. …

**Accessions** — [HGNC:948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:948) · Entrez [8938](https://www.ncbi.nlm.nih.gov/gene/8938) · UniProt [O94812](https://www.uniprot.org/uniprotkb/O94812) · Ensembl [ENSG00000007516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007516)

## Data

Gene col 148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 148); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 148]; `tensor/DDL_lfc|DDL_z.npy` [148]; `embed/gene_vectors.npy` [148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 148 or target_col == 148). Every well: [[BAIAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAIAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
