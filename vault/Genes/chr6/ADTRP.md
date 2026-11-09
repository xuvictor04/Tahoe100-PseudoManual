---
symbol: "ADTRP"
type: "gene"
col: 3296
ensembl_id: "ENSG00000111863"
name: "androgen dependent TFPI regulating protein"
location: "6p24.1"
module: 116
arm: "+"
pooled_cpm: 11.17
n_lines_expressing: 25
n_dd_up: 33
n_dd_down: 11
n_dd_up_clean: 23
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 20
direction_downstream: 38
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# ADTRP

*androgen dependent TFPI regulating protein* — 6p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.06× (z +19.1, q 0e+00, up in 15 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Triamcinolone (drug)]] 5 µM: 0.740× (z -4.2, q 0.008, down in 8 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAV3]] (+0.78, fdr 7e-06), [[ITGB1-DT]] (+0.75, fdr 7e-06), [[ROBO4]] (+0.74, fdr 7e-06); moves opposite to [[ABHD12]] (-0.55, fdr 2e-05), [[PPP1R12B]] (-0.55, fdr 3e-05), [[MED25]] (-0.53, fdr 3e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[LINC02934]] → it (grade B ⚠); 38 go from it, the strongest it → [[ETS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.06×** | +19.1 | 0e+00 | 15/20 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.00×** | +10.6 | 1e-23 | 17/20 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.6 | 1e-19 | 10/15 (LOX-IMVI, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +9.3 | 2e-18 | 9/12 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.52×** | +8.9 | 8e-17 | 17/22 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.6 | 6e-16 | 4/10 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +7.8 | 6e-13 | 14/20 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.1 | 7e-11 | 10/23 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.06×** | +6.9 | 2e-10 | 16/22 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.78×** | +5.5 | 2e-06 | 13/22 (LOX-IMVI, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +5.4 | 3e-06 | 16/22 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.0 | 2e-05 | 3/21 (MIA PaCa-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +4.9 | 5e-05 | 5/22 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.6 | 2e-04 | 7/17 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.91×** | +4.4 | 3e-04 | 0/22 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +4.4 | 4e-04 | 4/22 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.002 | 10/22 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.8 | 0.004 | 12/20 (AsPC-1, A-172, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +3.8 | 0.005 | 2/22 (MIA PaCa-2, NCI-H1573) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.011 | 8/22 (J82, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Triamcinolone (drug)]] 5 µM |  | **0.740×** | -4.2 | 0.008 | 8/22 (LOX-IMVI, HS-578T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.693×** | -4.1 | 0.008 | 12/23 (RKO, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.635×** | -4.1 | 0.008 | 6/22 (RKO, HS-578T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.665×** | -4.0 | 0.010 | 8/22 (LOX-IMVI, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.695×** | -3.6 | 0.043 | 6/22 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.5 µM |  | **0.706×** | -3.4 | 0.066 | 3/22 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.717×** | -3.3 | 0.071 | 7/22 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.714×** | -3.3 | 0.071 | 6/22 (LOX-IMVI, HS-578T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.714×** | -3.2 | 0.091 | 9/22 (RKO, LOX-IMVI, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.724×** | -3.2 | 0.091 | 6/22 (LOX-IMVI, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.714×** | -3.1 | 0.097 | 10/22 (RKO, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 258 | 0 | 23 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0721× (z -28.2) |
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -12.4) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.190× (z -11.8) |
| [[A-172 (line)]] | wt | 13.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.9× (z +23.3) | — |
| [[HOP62 (line)]] | alt | 5.91 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 6.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +13.9) | — |
| [[HEC-1-A (line)]] | alt | 4.93 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0959× (z -8.6) |
| [[Hs 766T (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +13.8) | — |
| [[J82 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 5.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +13.1) | — |
| [[A-427 (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.890 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAV3]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[ROBO4]] | +0.74 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[KBTBD8]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[TOMM34]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[IL31RA]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LNCOG]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[BCL2A1]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[LINC00973]] | +0.64 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[CXCL8]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.64 | +0.57 / +0.59 | both halves | 9e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD12]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R12B]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MED25]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[GNB2]] | -0.53 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[PACSIN2]] | -0.51 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[IFNGR1]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[SDHAP1]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 3, C 17. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02934]] | B | LINC02934 activity lowers ADTRP's level | lines that do not express LINC02934 (8) vs lines expressing it (42) | 4.19× higher at baseline in the lines without LINC02934 | 0.001 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ADTRP's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[ETS1]] | B | ETS1 activity raises ADTRP's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without ETS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[LINC02509]] | C | LINC02509 activity raises ADTRP's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 3.86× lower at baseline in the lines without LINC02509 | 6e-04 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises ADTRP's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.38× lower at baseline in the lines without ROBO4 | 0.001 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises ADTRP's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 3.01× lower at baseline in the lines without RGS4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[ESM1]] | C | ESM1 activity raises ADTRP's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 3.57× lower at baseline in the lines without ESM1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[FGF5]] | C | FGF5 activity raises ADTRP's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without FGF5 | 0.009 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises ADTRP's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.13× lower at baseline in the lines without LNCOG | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[BNC1]] | C | BNC1 activity raises ADTRP's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without BNC1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337; co-absent with the target |
| [[LINC01812]] | C | LINC01812 activity raises ADTRP's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.83× lower at baseline in the lines without LINC01812 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises ADTRP's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without PDCD1LG2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 20, C 18. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS1]] | B | ADTRP activity raises ETS1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 4.30× lower at baseline in the lines without ADTRP | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[RUNX1]] | B | ADTRP activity raises RUNX1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without ADTRP | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[SPHK1]] | B | ADTRP activity raises SPHK1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without ADTRP | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[ABL2]] | B | ADTRP activity raises ABL2's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.00× lower at baseline in the lines without ADTRP | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[NIPAL1]] | B | ADTRP activity raises NIPAL1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without ADTRP | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[LINC02516]] | B | ADTRP activity raises LINC02516's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without ADTRP | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[MSANTD3]] | B | ADTRP activity raises MSANTD3's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without ADTRP | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[ASB1]] | B | ADTRP activity raises ASB1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.37× lower at baseline in the lines without ADTRP | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[ATP2C2-AS1]] | B | ADTRP activity raises ATP2C2-AS1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without ADTRP | 0.031 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[NABP1]] | B | ADTRP activity raises NABP1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without ADTRP | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[AMPD3]] | B | ADTRP activity raises AMPD3's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without ADTRP | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[TRAF1]] | B | ADTRP activity raises TRAF1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.87× lower at baseline in the lines without ADTRP | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.841). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.8, 11.2); signed map (14.8, 45.0). **Vector** length 73.5, 19.8% of its response variance represented; |z| ≥ 3 in 643 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +19.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +2.1 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -4.1 |
|  | [[NG25 (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | androgen dependent TFPI regulating protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.1 — chr6:11,712,054-11,807,046 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ413H6.1, AIG1L; previously C6orf105 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IZ2](https://www.uniprot.org/uniprotkb/Q96IZ2) (Androgen-dependent TFPI-regulating protein):

> Hydrolyzes bioactive fatty-acid esters of hydroxy-fatty acids (FAHFAs), but not other major classes of lipids. Show a preference for FAHFAs with branching distal from the carboxylate head group of the lipids. Regulates the expression and the cell-associated anticoagulant activity of the inhibitor TFPI in endothelial cells (in vitro).

**Summary**, from NCBI Gene [84830](https://www.ncbi.nlm.nih.gov/gene/84830):

> Enables hydrolase activity. Involved in several processes, including cell migration involved in sprouting angiogenesis; cellular response to oxidised low-density lipoprotein particle stimulus; and negative regulation of secretion by cell. Located in caveola and cell surface. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21214) · Entrez [84830](https://www.ncbi.nlm.nih.gov/gene/84830) · UniProt [Q96IZ2](https://www.uniprot.org/uniprotkb/Q96IZ2) · Ensembl [ENSG00000111863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111863)

## Data

Gene col 3296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3296); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3296]; `tensor/DDL_lfc|DDL_z.npy` [3296]; `embed/gene_vectors.npy` [3296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3296 or target_col == 3296). Every well: [[ADTRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADTRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
