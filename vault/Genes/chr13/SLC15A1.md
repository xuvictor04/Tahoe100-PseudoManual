---
symbol: "SLC15A1"
type: "gene"
col: 1532
ensembl_id: "ENSG00000088386"
name: "solute carrier family 15 member 1"
location: "13q32.2-q32.3"
module: 8
arm: "+"
pooled_cpm: 5.38
n_lines_expressing: 10
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 28
direction_downstream: 22
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC15A1

*solute carrier family 15 member 1* — 13q32.2-q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.78× (z +13.6, q 2e-39, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.75× (z +11.5, q 2e-28, up in 1 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (Panc 03.27 0.131×, CFPAC-1 0.248×, AsPC-1 0.407×, NCI-H1573 0.258×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.167×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.102×; ⚠ toxic); [[Panobinostat (drug)]] 5 µM in 1 line (CFPAC-1 0.119×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRSS51]] (+0.75, fdr 7e-06), [[SLC34A2]] (+0.69, fdr 7e-06), [[MUC16]] (+0.64, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[RAPGEF5]] → it (grade B ⚠); 22 go from it, the strongest it → [[YWHAEP7-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.78×** | +13.6 | 2e-39 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.85×** | +12.7 | 9e-35 | 1/6 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.75×** | +11.5 | 2e-28 | 1/7 (NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +11.2 | 4e-27 | 1/7 (SW480) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.67×** | +9.7 | 3e-20 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +8.5 | 3e-15 | 6/7 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +5.5 | 4e-06 | 1/7 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.9 | 7e-05 | 0/7 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.9 | 7e-05 | 0/6 | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +4.6 | 3e-04 | 6/7 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.3 | 0.001 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.43×** | +3.7 | 0.009 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.038 | 1/7 (NCI-H1573) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.77×** | +3.3 | 0.038 | 1/6 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.073 | 1/7 (SW480) | top dose only |  |
| [[Tranilast (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.076 | 0/7 | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.079 | 1/7 (Panc 03.27) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.079 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.44×** | +2.9 | 0.090 | 1/7 (Panc 03.27) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1532.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (Panc 03.27 0.131×, CFPAC-1 0.248×, AsPC-1 0.407×, NCI-H1573 0.258×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.167×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.102×; ⚠ toxic); [[Panobinostat (drug)]] 5 µM in 1 line (CFPAC-1 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.660× | -3.2 | 0.64 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 85.2 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 2.10 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +13.4) | [[Clobetasol propionate (drug)]] 0.5 µM 0.0655× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 80.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -13.1) |
| [[A-172 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.783 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.794 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRSS51]] | +0.75 | +0.64 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SLC34A2]] | +0.69 | +0.68 / +0.73 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |
| [[MUC16]] | +0.64 | +0.51 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[GABRP]] | +0.64 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ALOX5]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MUC4]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TTC22]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ADAM28]] | +0.58 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[ST8SIA6]] | +0.58 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[PTPRR]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 2, C 26. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | RAPGEF5 activity raises SLC15A1's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without RAPGEF5 | 0.071 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity raises SLC15A1's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 1.66× lower at baseline in the lines without SAMD12-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[ITGB6]] | C | ITGB6 activity raises SLC15A1's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.34× lower at baseline in the lines without ITGB6 | 0.005 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises SLC15A1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without TMPRSS4 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[CATSPERB]] | C | CATSPERB activity raises SLC15A1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without CATSPERB | 0.007 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises SLC15A1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without TMEM45B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[RNF39]] | C | RNF39 activity raises SLC15A1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without RNF39 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises SLC15A1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without CDH1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises SLC15A1's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.91× lower at baseline in the lines without WFDC2 | 0.011 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises SLC15A1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.60× lower at baseline in the lines without ADGRF1 | 0.013 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises SLC15A1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without TJP3 | 0.019 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[FAAH2]] | C | FAAH2 activity raises SLC15A1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.91× lower at baseline in the lines without FAAH2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 1, C 21. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YWHAEP7-1]] | B | SLC15A1 activity raises YWHAEP7-1's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 2.12× lower at baseline in the lines without SLC15A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT |
| [[ADGRF1]] | C | SLC15A1 activity raises ADGRF1's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 7.17× lower at baseline in the lines without SLC15A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[CDH1]] | C | SLC15A1 activity raises CDH1's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 4.77× lower at baseline in the lines without SLC15A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[TC2N]] | C | SLC15A1 activity raises TC2N's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 4.21× lower at baseline in the lines without SLC15A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[SDR16C5]] | C | SLC15A1 activity raises SDR16C5's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 3.93× lower at baseline in the lines without SLC15A1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[CATSPERB]] | C | SLC15A1 activity raises CATSPERB's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 3.35× lower at baseline in the lines without SLC15A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[TACSTD2]] | C | SLC15A1 activity raises TACSTD2's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 6.47× lower at baseline in the lines without SLC15A1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[RNF39]] | C | SLC15A1 activity raises RNF39's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 2.30× lower at baseline in the lines without SLC15A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[TMEM45B]] | C | SLC15A1 activity raises TMEM45B's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 3.22× lower at baseline in the lines without SLC15A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[STEAP4]] | C | SLC15A1 activity raises STEAP4's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 5.47× lower at baseline in the lines without SLC15A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[ADCY4]] | C | SLC15A1 activity raises ADCY4's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 2.52× lower at baseline in the lines without SLC15A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |
| [[KRT23]] | C | SLC15A1 activity raises KRT23's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 2.25× lower at baseline in the lines without SLC15A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, 55.3); signed map (61.2, 1.2). **Vector** length 37.7, 15.7% of its response variance represented; |z| ≥ 3 in 198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.7 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.7 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | +1.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.6 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.6 | -0.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 15 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.2-q32.3 — chr13:98,683,801-98,752,672 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEPT1, HPECT1, HPEPT1 |
| Gene groups (HGNC) | Solute carrier family 15 |
| Reactome | 4 pathways, smallest: Proton/oligopeptide cotransporters; SLC-mediated transport of oligopeptides; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P46059](https://www.uniprot.org/uniprotkb/P46059) (Solute carrier family 15 member 1):

> Electrogenic proton-coupled amino-acid transporter that transports oligopeptides of 2 to 4 amino acids with a preference for dipeptides. Transports neutral and monovalently charged peptides with a proton to peptide stoichiometry of 1:1 or 2:1 (By similarity). Primarily responsible for the absorption of dietary di- and tripeptides from the small intestinal lumen (By similarity). Mediates transepithelial transport of muramyl and N-formylated bacterial dipeptides contributing to recognition of …

**Summary**, from NCBI Gene [6564](https://www.ncbi.nlm.nih.gov/gene/6564):

> This gene encodes an intestinal hydrogen peptide cotransporter that is a member of the solute carrier family 15. The encoded protein is localized to the brush border membrane of the intestinal epithelium and mediates the uptake of di- and tripeptides from the lumen into the enterocytes. This protein plays an important role in the uptake and digestion of dietary proteins. This protein also facilitates the absorption of numerous peptidomimetic drugs. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:10920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10920) · Entrez [6564](https://www.ncbi.nlm.nih.gov/gene/6564) · UniProt [P46059](https://www.uniprot.org/uniprotkb/P46059) · Ensembl [ENSG00000088386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088386)

## Data

Gene col 1532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1532); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1532]; `tensor/DDL_lfc|DDL_z.npy` [1532]; `embed/gene_vectors.npy` [1532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1532 or target_col == 1532). Every well: [[SLC15A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC15A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
