---
symbol: "RARRES1"
type: "gene"
col: 4021
ensembl_id: "ENSG00000118849"
name: "retinoic acid receptor responder 1"
location: "3q25.32"
module: 70
arm: "+"
pooled_cpm: 8.92
n_lines_expressing: 28
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 17
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# RARRES1

*retinoic acid receptor responder 1* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.24× (z +13.1, q 3e-36, up in 8 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +10.8, q 6e-25, up in 17 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.629× (z -4.3, q 0.008, down in 12 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTC]] (+0.67, fdr 2e-05), [[CFH]] (+0.65, fdr 1e-05), [[PDZK1IP1]] (+0.65, fdr 7e-06); moves opposite to [[ABTB3]] (-0.57, fdr 4e-05), [[PAQR5]] (-0.53, fdr 3e-05), [[PLEKHG5]] (-0.53, fdr 3e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GBP3]] → it (grade B ⚠); 17 go from it, the strongest it → [[GBP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.24×** | +13.1 | 3e-36 | 8/12 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.78×** | +12.5 | 2e-33 | 12/17 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +10.8 | 6e-25 | 17/23 (HOP62, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +9.0 | 2e-17 | 16/25 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +8.5 | 3e-15 | 8/13 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.4 | 7e-06 | 9/23 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.2 | 2e-05 | 6/25 (HOP62, A498, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.69×** | +4.7 | 1e-04 | 15/25 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +4.4 | 7e-04 | 15/24 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +4.3 | 8e-04 | 14/25 (AsPC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 9e-04 | 11/25 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +4.3 | 9e-04 | 13/23 (A498, AsPC-1, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.25×** | +4.0 | 0.003 | 6/15 (LoVo, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.80×** | +3.8 | 0.005 | 5/23 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.005 | 13/25 (AsPC-1, A498, …) | rises with dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **2.04×** | +3.5 | 0.016 | 6/19 (A498, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.94×** | +3.3 | 0.036 | 6/20 (LoVo, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.048 | 15/25 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.057 | 5/17 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4021.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.629×** | -4.3 | 0.008 | 12/25 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.637×** | -4.0 | 0.018 | 3/25 (NCI-H23, SW1417, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.687×** | -3.5 | 0.081 | 3/25 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 246 | 0 | 8 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0177× (z -14.3) |
| [[HOP62 (line)]] | alt | 3.93 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +14.9) | [[Ferulic acid (drug)]] 0.5 µM 0.0724× (z -9.5) |
| [[J82 (line)]] | alt | 16.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +18.3) | — |
| [[KATO III (line)]] | alt | 21.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0428× (z -12.1) |
| [[LoVo (line)]] | wt | 13.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.117× (z -10.4) |
| [[A498 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.212× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 9.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -8.8) |
| [[SNU-423 (line)]] | alt | 2.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +8.9) | — |
| [[A-172 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTC]] | +0.67 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[CFH]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PDZK1IP1]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CFB]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[LINC01503]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SAMD12-AS1]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[GBP1]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TAPBPL]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TNFSF10]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ETV7]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABTB3]] | -0.57 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PAQR5]] | -0.53 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[PLEKHG5]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[THBD]] | -0.52 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[PLEK2]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ARID3B]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.51 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[PWWP3A]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RAC2]] | -0.51 | -0.48 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP3]] | B | GBP3 activity raises RARRES1's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.03× lower at baseline in the lines without GBP3 | 0.074 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers RARRES1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[KMO]] | B | KMO activity raises RARRES1's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without KMO | 0.091 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[CASP10]] | C | CASP10 activity raises RARRES1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without CASP10 | 0.011 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5; co-absent with the target |
| [[PLA2R1]] | C | PLA2R1 activity raises RARRES1's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without PLA2R1 | 0.064 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises RARRES1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.46× lower at baseline in the lines without MUC5B | 0.079 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[MMP7]] | C | MMP7 activity raises RARRES1's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 1.67× lower at baseline in the lines without MMP7 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[SERPINB4]] | C | SERPINB4 activity raises RARRES1's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without SERPINB4 | 0.099 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 13, C 4. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP1]] | B | RARRES1 activity raises GBP1's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.26× lower at baseline in the lines without RARRES1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[HLA-F]] | B | RARRES1 activity raises HLA-F's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.65× lower at baseline in the lines without RARRES1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[B2M]] | B | RARRES1 activity raises B2M's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without RARRES1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[GBP3]] | B | RARRES1 activity raises GBP3's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 3.00× lower at baseline in the lines without RARRES1 | 0.017 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[CTSS]] | B | RARRES1 activity raises CTSS's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.95× lower at baseline in the lines without RARRES1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[RBPMS]] | B | RARRES1 activity raises RBPMS's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.43× lower at baseline in the lines without RARRES1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[GATA3]] | B | RARRES1 activity raises GATA3's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without RARRES1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[ABLIM3]] | B | RARRES1 activity raises ABLIM3's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without RARRES1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[MCFD2]] | B | RARRES1 activity raises MCFD2's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.24× lower at baseline in the lines without RARRES1 | 0.056 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[TNFSF10]] | B | RARRES1 activity raises TNFSF10's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.90× lower at baseline in the lines without RARRES1 | 0.062 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[RAC2]] | B | RARRES1 activity raises RAC2's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.95× lower at baseline in the lines without RARRES1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[FBXO39]] | B | RARRES1 activity raises FBXO39's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without RARRES1 | 0.069 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.8, 55.1); signed map (58.8, -1.3). **Vector** length 72.6, 18.5% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Non-canonical inflammasome activation* (reactome, mean cos +0.52 to 4); *complement* (hallmark, mean cos +0.52 to 8); *CASP4 inflammasome assembly* (reactome, mean cos +0.54 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +12.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +5.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | retinoic acid receptor responder 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:158,696,892-158,732,489 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIG1, LXNL |
| Matched by | ensembl_id |

**Function**, from UniProt [P49788](https://www.uniprot.org/uniprotkb/P49788) (Retinoic acid receptor responder protein 1):

> Inhibitor of the cytoplasmic carboxypeptidase AGBL2, may regulate the alpha-tubulin tyrosination cycle.

**Summary**, from NCBI Gene [5918](https://www.ncbi.nlm.nih.gov/gene/5918):

> This gene was identified as a retinoid acid (RA) receptor-responsive gene. It encodes a type 1 membrane protein. The expression of this gene is upregulated by tazarotene as well as by retinoic acid receptors. The expression of this gene is found to be downregulated in prostate cancer, which is caused by the methylation of its promoter and CpG island. Alternatively spliced transcript variant encoding distinct isoforms have been observed. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9867) · Entrez [5918](https://www.ncbi.nlm.nih.gov/gene/5918) · UniProt [P49788](https://www.uniprot.org/uniprotkb/P49788) · Ensembl [ENSG00000118849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118849)

## Data

Gene col 4021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4021); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4021]; `tensor/DDL_lfc|DDL_z.npy` [4021]; `embed/gene_vectors.npy` [4021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4021 or target_col == 4021). Every well: [[RARRES1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RARRES1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
