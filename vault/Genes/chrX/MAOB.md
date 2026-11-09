---
symbol: "MAOB"
type: "gene"
col: 922
ensembl_id: "ENSG00000069535"
name: "monoamine oxidase B"
location: "Xp11.3"
module: 34
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 16
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 31
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# MAOB

*monoamine oxidase B* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.24× (z +11.5, q 6e-28, up in 3 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW48 0.127×, KATO III 0.136×; ⚠ cell-cycle shift, explains ~12% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.180×, Hs 766T 0.211×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYPD3]] (+0.61, fdr 1e-05), [[SERPINB5]] (+0.60, fdr 1e-05), [[ANO1]] (+0.59, fdr 1e-05); moves opposite to [[ZNF785]] (-0.46, fdr 6e-05), [[WHAMM]] (-0.45, fdr 1e-04), [[STAP2]] (-0.44, fdr 8e-04, ⚠ not reproduced).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LYPD3]] → it (grade B ⚠); 31 go from it, the strongest it → [[NECTIN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +11.5 | 6e-28 | 3/10 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.01×** | +11.2 | 1e-26 | 5/9 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.19×** | +11.0 | 7e-26 | 4/6 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.37×** | +9.1 | 2e-17 | 2/6 (KATO III, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.42×** | +8.7 | 6e-16 | 10/12 (SW480, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.7 | 8e-07 | 2/10 (AsPC-1, SW480) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +4.7 | 2e-04 | 0/10 | top dose only | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +4.4 | 6e-04 | 8/11 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.45×** | +4.4 | 6e-04 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +4.3 | 0.001 | 2/12 (AsPC-1, SW480) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.1 | 0.002 | 1/10 (HT-29) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.9 | 0.004 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +3.8 | 0.007 | 2/11 (SW480, AsPC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.5 | 0.018 | 1/10 (SW480) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.65×** | +3.5 | 0.020 | 4/13 (LS 180, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.029 | 4/12 (AsPC-1, LS 180, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.92×** | +3.2 | 0.041 | 2/10 (LS 180, SW480) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 922.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW48 0.127×, KATO III 0.136×; ⚠ cell-cycle shift, explains ~12% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.180×, Hs 766T 0.211×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | 0.621× | -3.2 | 0.74 | 5/12 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 23.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.58× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[SW48 (line)]] | wt | 82.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -13.1) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -10.9) |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -9.5) |
| [[LS 180 (line)]] | wt | 3.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.16× (z +9.4) | — |
| [[SW480 (line)]] | alt | 3.88 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.16× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.852 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.571 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPD3]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SERPINB5]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ANO1]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ATG16L1]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.56 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[SCEL]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[RAP1GAP2]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CAPG]] | +0.55 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[ACOT7]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[IGSF9]] | +0.54 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PKP1]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TNS4]] | +0.53 | +0.54 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF785]] | -0.46 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[WHAMM]] | -0.45 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[STAP2]] | -0.44 | -0.46 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[MTUS1-DT]] | -0.43 | -0.52 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD3]] | B | LYPD3 activity raises MAOB's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without LYPD3 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[HPGD]] | C | HPGD activity raises MAOB's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without HPGD | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5; co-absent with the target |
| [[LAMA3]] | C | LAMA3 activity raises MAOB's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without LAMA3 | 0.033 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B; co-absent with the target |
| [[LINC00659]] | C | LINC00659 activity raises MAOB's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without LINC00659 | 0.054 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises MAOB's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without SERPINB5 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[KIAA0040]] | C | KIAA0040 activity raises MAOB's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without KIAA0040 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1; co-absent with the target |
| [[SCEL]] | C | SCEL activity raises MAOB's level | lines that do not express SCEL (35) vs lines expressing it (15) | 2.30× lower at baseline in the lines without SCEL | 0.067 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1; co-absent with the target |
| [[ANO1]] | C | ANO1 activity raises MAOB's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without ANO1 | 0.073 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises MAOB's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without P2RY2 | 0.075 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |
| [[SDR16C5]] | C | SDR16C5 activity raises MAOB's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 2.24× lower at baseline in the lines without SDR16C5 | 0.081 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH; co-absent with the target |
| [[ITGB4]] | C | ITGB4 activity raises MAOB's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without ITGB4 | 0.084 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3; co-absent with the target |
| [[KLK11]] | C | KLK11 activity raises MAOB's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.56× lower at baseline in the lines without KLK11 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 13, C 18. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NECTIN1]] | B | MAOB activity raises NECTIN1's level | lines that do not express MAOB (34) vs lines expressing it (16) | 3.09× lower at baseline in the lines without MAOB | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[EPHA2-AS1]] | B | MAOB activity raises EPHA2-AS1's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.15× lower at baseline in the lines without MAOB | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[ENDOD1]] | B | MAOB activity raises ENDOD1's level | lines that do not express MAOB (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without MAOB | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[ITPK1]] | B | MAOB activity raises ITPK1's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without MAOB | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[MTUS1-DT]] | B | MAOB activity raises MTUS1-DT's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without MAOB | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[KRT8]] | B | MAOB activity raises KRT8's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without MAOB | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[LYPD3]] | B | MAOB activity raises LYPD3's level | lines that do not express MAOB (34) vs lines expressing it (16) | 1.97× lower at baseline in the lines without MAOB | 0.046 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[IGSF9]] | B | MAOB activity raises IGSF9's level | lines that do not express MAOB (34) vs lines expressing it (16) | 1.84× lower at baseline in the lines without MAOB | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[NGEF]] | B | MAOB activity raises NGEF's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.54× lower at baseline in the lines without MAOB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[ITGA6]] | B | MAOB activity raises ITGA6's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.83× lower at baseline in the lines without MAOB | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[CDC42BPB]] | B | MAOB activity raises CDC42BPB's level | lines that do not express MAOB (34) vs lines expressing it (16) | 1.34× lower at baseline in the lines without MAOB | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[ARHGAP8]] | B | MAOB activity raises ARHGAP8's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.03× lower at baseline in the lines without MAOB | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.8, 53.1); signed map (2.3, 38.6). **Vector** length 32.3, 8.37% of its response variance represented; |z| ≥ 3 in 298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.7 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.7 | +2.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -0.7 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.6 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -1.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | monoamine oxidase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:43,766,610-43,882,450 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins; Monoamine oxidase family |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Amine Oxidase reactions; Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P27338](https://www.uniprot.org/uniprotkb/P27338) (Amine oxidase):

> Catalyzes the oxidative deamination of primary and some secondary amines such as neurotransmitters, and exogenous amines including the tertiary amine, neurotoxin 1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine (MPTP), with concomitant reduction of oxygen to hydrogen peroxide and participates in the metabolism of neuroactive and vasoactive amines in the central nervous system and peripheral tissues. Preferentially degrades benzylamine and phenylethylamine.

**Summary**, from NCBI Gene [4129](https://www.ncbi.nlm.nih.gov/gene/4129):

> The protein encoded by this gene belongs to the flavin monoamine oxidase family. It is a enzyme located in the mitochondrial outer membrane. It catalyzes the oxidative deamination of biogenic and xenobiotic amines and plays an important role in the metabolism of neuroactive and vasoactive amines in the central nervous sysytem and peripheral tissues. This protein preferentially degrades benzylamine and phenylethylamine. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6834) · Entrez [4129](https://www.ncbi.nlm.nih.gov/gene/4129) · UniProt [P27338](https://www.uniprot.org/uniprotkb/P27338) · Ensembl [ENSG00000069535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069535)

## Data

Gene col 922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 922); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 922]; `tensor/DDL_lfc|DDL_z.npy` [922]; `embed/gene_vectors.npy` [922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 922 or target_col == 922). Every well: [[MAOB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAOB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
