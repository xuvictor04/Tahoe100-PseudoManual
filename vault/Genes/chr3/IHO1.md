---
symbol: "IHO1"
type: "gene"
col: 10382
ensembl_id: "ENSG00000173421"
name: "interactor of HORMAD1 1"
location: "3p21.31"
module: 108
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 14
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 19
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# IHO1

*interactor of HORMAD1 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.56× (z +16.2, q 0e+00, up in 2 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0744×, SK-MEL-2 0.213×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.118×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.236×); [[Canagliflozin (drug)]] 5 µM in 1 line (C32 0.0874×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01242]] (+0.63, fdr 1e-05), [[KC6]] (+0.62, fdr 1e-05), [[ZNF521]] (+0.60, fdr 1e-05); moves opposite to [[ICA1]] (-0.42, fdr 2e-04), [[PATJ]] (-0.39, fdr 6e-05), [[LPIN3]] (-0.39, fdr 9e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PCDHGA2]] → it (grade B ⚠); 19 go from it, the strongest it → [[OBI1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.56×** | +16.2 | 0e+00 | 2/9 (HEC-1-A, NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.76×** | +13.6 | 2e-39 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.38×** | +13.3 | 2e-38 | 1/7 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.49×** | +11.2 | 8e-27 | 3/6 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +10.1 | 6e-22 | 3/9 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.69×** | +8.9 | 4e-17 | 3/9 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.8 | 5e-07 | 1/7 (A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.3 | 9e-06 | 1/8 (HEC-1-A) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.5 | 4e-04 | 1/9 (HEC-1-A) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.5 | 5e-04 | 1/7 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.78×** | +4.3 | 9e-04 | 0/7 | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.001 | 0/9 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +3.8 | 0.005 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.8 | 0.005 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +3.6 | 0.011 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.021 | 1/9 (SK-MEL-2) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.048 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.058 | 0/9 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +2.9 | 0.087 | 1/9 (hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +2.9 | 0.087 | 0/7 | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.087 | 1/9 (C32) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.40×** | +2.8 | 0.100 | 0/9 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10382.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0744×, SK-MEL-2 0.213×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.118×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.236×); [[Canagliflozin (drug)]] 5 µM in 1 line (C32 0.0874×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.676× | -3.4 | 0.41 | 0/9 | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.709× | -3.2 | 0.46 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 43.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -9.7) |
| [[C32 (line)]] | wt | 7.02 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0874× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0744× (z -10.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.518 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01242]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[KC6]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZNF521]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[FAM106A]] | +0.57 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[LINC02267]] | +0.55 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[PAX3]] | +0.55 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[AEBP1]] | +0.54 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[CNRIP1]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[RHOJ]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[LINC02226]] | +0.52 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[NAV1]] | +0.51 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[MSC-AS1]] | +0.51 | +0.45 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICA1]] | -0.42 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[PATJ]] | -0.39 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[LPIN3]] | -0.39 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[DLEU1]] | -0.39 | -0.23 / -0.37 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHGA2]] | B | PCDHGA2 activity raises IHO1's level | lines that do not express PCDHGA2 (7) vs lines expressing it (43) | 1.15× lower at baseline in the lines without PCDHGA2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF134, SYDE1, SIX1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers IHO1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01242]] | C | LINC01242 activity raises IHO1's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 1.93× lower at baseline in the lines without LINC01242 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |
| [[LINC02109]] | C | LINC02109 activity raises IHO1's level | lines that do not express LINC02109 (40) vs lines expressing it (10) | 2.26× lower at baseline in the lines without LINC02109 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287474, ENSG00000253642, LINC00879; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises IHO1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 2.40× lower at baseline in the lines without AEBP1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[MIR548XHG]] | C | MIR548XHG activity raises IHO1's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 1.70× lower at baseline in the lines without MIR548XHG | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises IHO1's level | lines that do not express CARMN (40) vs lines expressing it (10) | 1.40× lower at baseline in the lines without CARMN | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises IHO1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without EDNRB | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises IHO1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 2.99× lower at baseline in the lines without FCRLA | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 2, C 17. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OBI1-AS1]] | B | IHO1 activity raises OBI1-AS1's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 1.67× lower at baseline in the lines without IHO1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent |
| [[KIF14]] | B | IHO1 activity lowers KIF14's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 1.06× higher at baseline in the lines without IHO1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent |
| [[CARMN]] | C | IHO1 activity raises CARMN's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 1.77× lower at baseline in the lines without IHO1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[EDNRB]] | C | IHO1 activity raises EDNRB's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 2.27× lower at baseline in the lines without IHO1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[COL1A2]] | C | IHO1 activity raises COL1A2's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 6.07× lower at baseline in the lines without IHO1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[LHFPL3-AS1]] | C | IHO1 activity raises LHFPL3-AS1's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 3.62× lower at baseline in the lines without IHO1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[CTTNBP2]] | C | IHO1 activity raises CTTNBP2's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 2.91× lower at baseline in the lines without IHO1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[FCRLA]] | C | IHO1 activity raises FCRLA's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 2.69× lower at baseline in the lines without IHO1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[A2M]] | C | IHO1 activity raises A2M's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 3.04× lower at baseline in the lines without IHO1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[TDRD9]] | C | IHO1 activity raises TDRD9's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 1.69× lower at baseline in the lines without IHO1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[SOX10]] | C | IHO1 activity raises SOX10's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 3.04× lower at baseline in the lines without IHO1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[TYR]] | C | IHO1 activity raises TYR's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 2.35× lower at baseline in the lines without IHO1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.9, 25.8); signed map (31.5, 43.5). **Vector** length 24.5, 6.80% of its response variance represented; |z| ≥ 3 in 201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +16.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.5 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.5 | -0.3 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.5 | -0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.5 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.5 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | interactor of HORMAD1 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,198,428-49,258,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25320, CT74, LELA1; previously CCDC36 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYA8](https://www.uniprot.org/uniprotkb/Q8IYA8) (Interactor of HORMAD1 protein 1):

> Required for DNA double-strand breaks (DSBs) formation in unsynapsed regions during meiotic recombination. Probably acts by forming a complex with MEI4 and REC114, which activates DSBs formation in unsynapsed regions, an essential step to ensure completion of synapsis. Not required for HORMAD1 functions in pairing-independent synaptonemal complex formation, ATR recruitment to unsynapsed axes, meiotic silencing of unsynapsed chromatin (MSUC) or meiotic surveillance.

**Summary**, from NCBI Gene [339834](https://www.ncbi.nlm.nih.gov/gene/339834):

> Predicted to be involved in several processes, including meiosis I cell cycle process; regulation of homologous chromosome segregation; and spermatogenesis. Predicted to be located in chromosome. Predicted to be active in condensed nuclear chromosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27945) · Entrez [339834](https://www.ncbi.nlm.nih.gov/gene/339834) · UniProt [Q8IYA8](https://www.uniprot.org/uniprotkb/Q8IYA8) · Ensembl [ENSG00000173421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173421)

## Data

Gene col 10382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10382); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10382]; `tensor/DDL_lfc|DDL_z.npy` [10382]; `embed/gene_vectors.npy` [10382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10382 or target_col == 10382). Every well: [[IHO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IHO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
