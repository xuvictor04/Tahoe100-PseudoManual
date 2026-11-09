---
symbol: "HLA-V-1"
type: "gene"
col: 16499
ensembl_id: "ENSG00000290710"
name: ""
location: ""
module: 23
arm: "+"
pooled_cpm: 7.06
n_lines_expressing: 29
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 15
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# HLA-V-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.84× (z +11.9, q 1e-29, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.336× (z -12.4, q 1e-32, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX19]] (+0.61, fdr 4e-05), [[BTN2A3P]] (+0.61, fdr 2e-05), [[ARMCX5-GPRASP2]] (+0.60, fdr 3e-05); moves opposite to [[NUP93]] (-0.65, fdr 1e-05), [[SLC25A39]] (-0.58, fdr 4e-05), [[MFSD14B]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MTUS1-DT]] → it (grade B ⚠); 15 go from it, the strongest it → [[SLC2A1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.84×** | +11.9 | 1e-29 | 22/26 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +8.8 | 3e-16 | 16/24 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.0 | 7e-10 | 10/24 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.7 | 2e-06 | 13/24 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +5.5 | 4e-06 | 12/26 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.4 | 6e-06 | 11/26 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.8 | 1e-04 | 7/20 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.002 | 7/26 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.006 | 5/23 (SW480, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.9 | 0.006 | 2/17 (LoVo, HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.25×** | +3.6 | 0.015 | 8/26 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.4 | 0.033 | 2/18 (AsPC-1, HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.041 | 10/26 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.69×** | +3.1 | 0.074 | 6/25 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.336×** | -12.4 | 1e-32 | 23/26 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.381×** | -11.0 | 1e-25 | 21/26 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.440×** | -9.3 | 2e-18 | 22/26 (Panc 03.27, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.581×** | -6.2 | 9e-08 | 15/25 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -4.4 | 0.001 | 10/26 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.679×** | -4.2 | 0.002 | 13/22 (HCT15, HT-29, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.694×** | -4.2 | 0.003 | 6/26 (KATO III, NCI-H1573, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.711×** | -3.9 | 0.007 | 8/26 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.700×** | -3.8 | 0.008 | 10/26 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.533×** | -3.8 | 0.010 | 10/26 (HT-29, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.577×** | -3.3 | 0.053 | 12/23 (Panc 03.27, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.754×** | -3.1 | 0.093 | 12/26 (NCI-H1573, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 22.9 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0620× (z -23.4) |
| [[Panc 03.27 (line)]] | alt | 49.2 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.74× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.198× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 51.7 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.223× (z -12.6) |
| [[KATO III (line)]] | alt | 18.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 14.5 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +10.0) | [[Belinostat (drug)]] 5 µM 0.207× (z -9.7) |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -12.3) |
| [[SW480 (line)]] | alt | 8.26 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -16.0) |
| [[LoVo (line)]] | wt | 7.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +13.2) | — |
| [[A498 (line)]] | wt | 2.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 2.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.7× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 5.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 8.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0827× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 9.19 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -8.9) |
| [[PANC-1 (line)]] | alt | 2.02 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0682× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 7.02 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0775× (z -10.0) |
| [[A-172 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.973 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX19]] | +0.61 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[BTN2A3P]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ARMCX5-GPRASP2]] | +0.60 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[RNF103-CHMP3]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[GPRASP1]] | +0.60 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[LGALSL-DT]] | +0.59 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[NPHS1]] | +0.59 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[NSMCE1-DT]] | +0.57 | +0.48 / +0.38 | both halves | 7e-05 |  |
| [[ARMCX3]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[TCEAL3]] | +0.57 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[LINC01186]] | +0.56 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PIWIL2]] | +0.56 | +0.52 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | -0.65 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SLC25A39]] | -0.58 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MFSD14B]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PARN]] | -0.55 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[IPO11]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[DROSHA]] | -0.54 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[TATDN2]] | -0.54 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[NOMO3]] | -0.53 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[NTAQ1]] | -0.53 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[FAR1]] | -0.53 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[RSU1]] | -0.53 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[WDR5]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1-DT]] | B | MTUS1-DT activity raises HLA-V-1's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without MTUS1-DT | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[FAM149A]] | B | FAM149A activity raises HLA-V-1's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 2.08× lower at baseline in the lines without FAM149A | 0.033 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[LINC01186]] | B | LINC01186 activity raises HLA-V-1's level | lines that do not express LINC01186 (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without LINC01186 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01836, STXBP2, EEPD1 |
| [[MPZL3]] | C | MPZL3 activity raises HLA-V-1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 3.05× lower at baseline in the lines without MPZL3 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1; co-absent with the target |
| [[DAPP1]] | C | DAPP1 activity raises HLA-V-1's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.72× lower at baseline in the lines without DAPP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A1-DT]] | B | HLA-V-1 activity raises SLC2A1-DT's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without HLA-V-1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[LINC00857]] | B | HLA-V-1 activity raises LINC00857's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 2.46× lower at baseline in the lines without HLA-V-1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[TNK1]] | B | HLA-V-1 activity raises TNK1's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without HLA-V-1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[RNF103-CHMP3]] | B | HLA-V-1 activity raises RNF103-CHMP3's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 2.31× lower at baseline in the lines without HLA-V-1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[WDR5]] | B | HLA-V-1 activity lowers WDR5's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.28× higher at baseline in the lines without HLA-V-1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[COL28A1]] | B | HLA-V-1 activity raises COL28A1's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.30× lower at baseline in the lines without HLA-V-1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | HLA-V-1 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express HLA-V-1 (21) vs lines expressing it (27) | the lines without HLA-V-1: 1.18× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[MARVELD2]] | B | HLA-V-1 activity raises MARVELD2's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without HLA-V-1 | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[NUP93]] | B | HLA-V-1 activity lowers NUP93's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.37× higher at baseline in the lines without HLA-V-1 | 0.056 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[DNAH12]] | B | HLA-V-1 activity raises DNAH12's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.37× lower at baseline in the lines without HLA-V-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| cells under [[MK-3903 (drug)]] 0.05 µM | B | HLA-V-1 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express HLA-V-1 (21) vs lines expressing it (27) | the lines without HLA-V-1: 0.85× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[DIAPH2-AS1]] | B | HLA-V-1 activity raises DIAPH2-AS1's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.68× lower at baseline in the lines without HLA-V-1 | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (18.3, 7.9); signed map (17.5, -14.0). **Vector** length 64.2, 14.2% of its response variance represented; |z| ≥ 3 in 641 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.6 | -11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -12.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.3 | -9.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -2.0 | -4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.2 | -4.2 |

## What is on record

> [!warning] No registry record
> HLA-V-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16499); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16499]; `tensor/DDL_lfc|DDL_z.npy` [16499]; `embed/gene_vectors.npy` [16499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16499 or target_col == 16499). Every well: [[HLA-V-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-V-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
