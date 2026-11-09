---
symbol: "CCR3"
type: "gene"
col: 11427
ensembl_id: "ENSG00000183625"
name: "C-C motif chemokine receptor 3"
location: "3p21.31"
module: 27
arm: "+"
pooled_cpm: 3.62
n_lines_expressing: 15
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 29
direction_downstream: 36
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CCR3

*C-C motif chemokine receptor 3* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.03× (z +11.6, q 3e-28, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.89× (z +11.1, q 2e-26, up in 2 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.561× (z -4.4, q 0.008, down in 10 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 0.182×, COLO 205 0.118×, NCI-H2347 0.154×, SW1417 0.254×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0223×, SW480 0.166×, SW1417 0.237×); [[Panobinostat (drug)]] 5 µM in 3 lines (SW480 0.0359×, COLO 205 0.0902×, SW1417 0.151×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT23]] (+0.68, fdr 1e-05), [[SLC30A10]] (+0.63, fdr 1e-05), [[B3GAT1-DT]] (+0.62, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[YWHAEP7-1]] → it (grade B ⚠); 36 go from it, the strongest it → [[MUC20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.03×** | +11.6 | 3e-28 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +11.1 | 2e-26 | 2/12 (HOP62, NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.98×** | +10.3 | 2e-22 | 1/8 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.04×** | +9.6 | 1e-19 | 1/4 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.16×** | +5.7 | 1e-06 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.2 | 0.002 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +4.2 | 0.003 | 1/12 (HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.03×** | +3.8 | 0.012 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.017 | 5/10 (SW1417, RPMI-7951, …) | all doses, flat |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.4 | 0.038 | 0/11 | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.048 | 0/12 | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +3.3 | 0.052 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.060 | 1/12 (BT-474) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.062 | 3/12 (SW1417, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +3.1 | 0.078 | 1/3 (SW1417) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.078 | 3/12 (BT-474, COLO 205, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.085 | 5/11 (SW1417, SNU-423, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.34×** | +3.0 | 0.096 | 3/12 (SW1417, Panc 03.27, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 0.182×, COLO 205 0.118×, NCI-H2347 0.154×, SW1417 0.254×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0223×, SW480 0.166×, SW1417 0.237×); [[Panobinostat (drug)]] 5 µM in 3 lines (SW480 0.0359×, COLO 205 0.0902×, SW1417 0.151×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.561×** | -4.4 | 0.008 | 10/12 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.647× | -3.3 | 0.19 | 4/12 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.647× | -3.3 | 0.19 | 8/12 (COLO 205, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.672× | -3.0 | 0.34 | 1/12 (HOP62) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 31.8 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0223× (z -23.5) |
| [[SW480 (line)]] | alt | 25.0 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0359× (z -18.8) |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -12.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -11.5) |
| [[BT-474 (line)]] | alt | 8.16 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0386× (z -10.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 4.14 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0336× (z -9.6) |
| [[A-172 (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.913 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.584 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT23]] | +0.68 | +0.65 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[SLC30A10]] | +0.63 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[B3GAT1-DT]] | +0.62 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[PROM1]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 | same gene group |
| [[VWA2]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PKHD1]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TMPRSS3]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[APCDD1]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TACSTD2]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[FGD5]] | +0.60 | +0.59 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 2, C 27. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YWHAEP7-1]] | B | YWHAEP7-1 activity raises CCR3's level | lines that do not express YWHAEP7-1 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without YWHAEP7-1 | 0.064 | ⚠ within organs, on part of the lines; also absent: OCA2, ALK, SPDYE10; maybe low, not absent |
| [[C11orf52]] | B | C11orf52 activity raises CCR3's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without C11orf52 | 0.081 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[WFDC2]] | C | WFDC2 activity raises CCR3's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.04× lower at baseline in the lines without WFDC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises CCR3's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.78× lower at baseline in the lines without KRT23 | 0.002 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises CCR3's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.78× lower at baseline in the lines without TNFRSF14-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[CARD11]] | C | CARD11 activity raises CCR3's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without CARD11 | 0.010 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises CCR3's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 2.65× lower at baseline in the lines without VWA2 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises CCR3's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without SKAP1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[MACC1]] | C | MACC1 activity raises CCR3's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.41× lower at baseline in the lines without MACC1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises CCR3's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.34× lower at baseline in the lines without ITGB6 | 0.018 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises CCR3's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.79× lower at baseline in the lines without TMPRSS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[TACSTD2]] | C | TACSTD2 activity raises CCR3's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without TACSTD2 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 12, C 24. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | CCR3 activity raises MUC20's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 2.47× lower at baseline in the lines without CCR3 | 0.009 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[BCL2L15]] | B | CCR3 activity raises BCL2L15's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.68× lower at baseline in the lines without CCR3 | 0.028 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[LASTR]] | B | CCR3 activity raises LASTR's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without CCR3 | 0.030 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[SAMD12-AS1]] | B | CCR3 activity raises SAMD12-AS1's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 2.03× lower at baseline in the lines without CCR3 | 0.046 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[STS]] | B | CCR3 activity raises STS's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 2.54× lower at baseline in the lines without CCR3 | 0.046 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[YWHAEP7-1]] | B | CCR3 activity raises YWHAEP7-1's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.61× lower at baseline in the lines without CCR3 | 0.055 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[MAP2K6]] | B | CCR3 activity raises MAP2K6's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.89× lower at baseline in the lines without CCR3 | 0.057 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[C11orf52]] | B | CCR3 activity raises C11orf52's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.65× lower at baseline in the lines without CCR3 | 0.058 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[FGD3]] | B | CCR3 activity raises FGD3's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.72× lower at baseline in the lines without CCR3 | 0.059 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[ZNF503-AS1]] | B | CCR3 activity raises ZNF503-AS1's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.60× lower at baseline in the lines without CCR3 | 0.079 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[LGALS9]] | B | CCR3 activity raises LGALS9's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.89× lower at baseline in the lines without CCR3 | 0.080 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[B4GALT5]] | B | CCR3 activity raises B4GALT5's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.44× lower at baseline in the lines without CCR3 | 0.097 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 45.5); signed map (61.5, 14.7). **Vector** length 43.4, 14.1% of its response variance represented; |z| ≥ 3 in 338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +1.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -1.5 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | C-C motif chemokine receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:46,130,890-46,266,706 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CC-CKR-3, CKR3, CD193; previously CMKBR3 |
| Gene groups (HGNC) | CD molecules; C-C motif chemokine receptors |
| Reactome | 7 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P51677](https://www.uniprot.org/uniprotkb/P51677) (C-C chemokine receptor type 3):

> G protein-coupled receptor (GPCR) that plays a key role in the immune system by regulating the migration and activation of white blood cells in response to chemokines. Selectively interacts with eosinophil-attracting chemokines such as eotaxin/CCL11, eotaxin-2/CCL24 and eotaxin-3/CCL26. Ligand binding triggers intracellular signaling that leads to chemotaxis of immune cells. Mechanistically, signals through GNA14 or GNA16 to induce stimulation of phospholipase Cbeta/PLCB2 and subsequently …

**Summary**, from NCBI Gene [1232](https://www.ncbi.nlm.nih.gov/gene/1232):

> The protein encoded by this gene is a receptor for C-C type chemokines. It belongs to family 1 of the G protein-coupled receptors. This receptor binds and responds to a variety of chemokines, including eotaxin (CCL11), eotaxin-3 (CCL26), MCP-3 (CCL7), MCP-4 (CCL13), and RANTES (CCL5). It is highly expressed in eosinophils and basophils, and is also detected in TH1 and TH2 cells, as well as in airway epithelial cells. This receptor may contribute to the accumulation and activation of eosinophils …

**Accessions** — [HGNC:1604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1604) · Entrez [1232](https://www.ncbi.nlm.nih.gov/gene/1232) · UniProt [P51677](https://www.uniprot.org/uniprotkb/P51677) · Ensembl [ENSG00000183625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183625)

## Data

Gene col 11427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11427); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11427]; `tensor/DDL_lfc|DDL_z.npy` [11427]; `embed/gene_vectors.npy` [11427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11427 or target_col == 11427). Every well: [[CCR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
