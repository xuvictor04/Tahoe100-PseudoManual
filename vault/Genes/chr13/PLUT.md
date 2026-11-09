---
symbol: "PLUT"
type: "gene"
col: 14494
ensembl_id: "ENSG00000247381"
name: "PDX1 associated lncRNA, upregulator of transcription"
location: "13q12.2"
module: 35
arm: "+"
pooled_cpm: 2.25
n_lines_expressing: 27
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PLUT

*PDX1 associated lncRNA, upregulator of transcription* — 13q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.15× (z +24.5, q 0e+00, up in 16 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.568× (z -4.4, q 0.005, down in 14 of 21 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKHD1]] (+0.66, fdr 2e-05), [[LINC01091]] (+0.64, fdr 1e-05), [[BANK1]] (+0.63, fdr 3e-05); moves opposite to [[MOCS1]] (-0.54, fdr 1e-04), [[PLA2G12A]] (-0.50, fdr 1e-04), [[MAST3]] (-0.50, fdr 7e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[LINC01091]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.15×** | +24.5 | 0e+00 | 16/17 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.35×** | +12.6 | 4e-34 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.67×** | +10.2 | 5e-22 | 1/7 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.92×** | +9.9 | 7e-21 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +8.5 | 1e-15 | 8/17 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +8.3 | 1e-14 | 9/15 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +8.2 | 2e-14 | 2/18 (LoVo, HCT15) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +7.1 | 1e-10 | 4/19 (SW480, HT-29, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.51×** | +5.1 | 2e-05 | 1/5 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.1 | 2e-05 | 5/19 (COLO 205, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +4.7 | 1e-04 | 3/21 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.001 | 0/19 | top dose only | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.1 | 0.002 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.99×** | +3.8 | 0.005 | 1/10 (NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.006 | 0/18 | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.009 | 4/21 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +3.6 | 0.010 | 5/17 (LS 180, HCT15, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.4 | 0.024 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.034 | 1/17 (PANC-1) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.043 | 5/19 (SHP-77, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.568×** | -4.4 | 0.005 | 14/21 (KATO III, SHP-77, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -4.0 | 0.015 | 7/19 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.623×** | -3.7 | 0.039 | 9/21 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.639×** | -3.5 | 0.062 | 11/20 (KATO III, SW1417, …) | two highest doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.659× | -3.0 | 0.28 | 2/21 (Panc 03.27, SW480) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0902× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.166× (z -10.7) |
| [[COLO 205 (line)]] | alt | 11.0 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.00× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.0646× (z -13.9) |
| [[KATO III (line)]] | alt | 5.18 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0526× (z -9.9) |
| [[PANC-1 (line)]] | alt | 3.40 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +10.8) | [[Docetaxel (drug)]] 0.05 µM 0.0864× (z -10.2) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 2.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.9× (z +11.1) | — |
| [[LoVo (line)]] | wt | 1.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 3.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.3× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 2.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +10.6) | — |
| [[SW480 (line)]] | alt | 1.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +11.4) | — |
| [[A-172 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.750 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.589 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.638 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.611 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.698 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKHD1]] | +0.66 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[LINC01091]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[BANK1]] | +0.63 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[DIP2C-AS1]] | +0.61 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[THBS4-AS1]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[GAS2]] | +0.60 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[C11orf52]] | +0.60 | +0.56 / +0.27 | both halves | 3e-04 |  |
| [[NINJ2]] | +0.59 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[HOTAIR]] | +0.58 | +0.44 / +0.32 | both halves | 2e-04 | same gene group |
| [[CLVS1]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[CIBAR1-DT]] | +0.57 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[ERICH2-DT]] | +0.57 | +0.50 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOCS1]] | -0.54 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[PLA2G12A]] | -0.50 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[MAST3]] | -0.50 | -0.35 / -0.21 | both halves | 7e-04 |  |
| [[PLPPR2]] | -0.49 | -0.37 / -0.23 | both halves | 5e-04 |  |
| [[SIN3B]] | -0.48 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[AP2A2]] | -0.47 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLUT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HNF4G]] | B | HNF4G activity raises PLUT's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without HNF4G | 0.065 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[C11orf52]] | B | C11orf52 activity raises PLUT's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without C11orf52 | 0.073 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[MGC32805]] | C | MGC32805 activity raises PLUT's level | lines that do not express MGC32805 (32) vs lines expressing it (18) | 1.86× lower at baseline in the lines without MGC32805 | 0.047 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises PLUT's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without HNF1A-AS1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises PLUT's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 1.78× lower at baseline in the lines without KCNB2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | PLUT activity raises LINC01091's level | lines that do not express PLUT (23) vs lines expressing it (27) | 2.15× lower at baseline in the lines without PLUT | 0.026 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent |
| [[SFTA3-1]] | B | PLUT activity raises SFTA3-1's level | lines that do not express PLUT (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without PLUT | 0.046 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent |
| [[NEIL1]] | B | PLUT activity raises NEIL1's level | lines that do not express PLUT (23) vs lines expressing it (27) | 1.45× lower at baseline in the lines without PLUT | 0.058 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent |
| [[DYRK1A]] | B | PLUT activity raises DYRK1A's level | lines that do not express PLUT (23) vs lines expressing it (27) | 1.17× lower at baseline in the lines without PLUT | 0.067 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent |
| [[ZNF503-AS1]] | B | PLUT activity raises ZNF503-AS1's level | lines that do not express PLUT (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without PLUT | 0.079 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent |
| [[SCIN]] | C | PLUT activity raises SCIN's level | lines that do not express PLUT (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without PLUT | 0.028 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent; co-absent with the target |
| [[CRACDL]] | C | PLUT activity raises CRACDL's level | lines that do not express PLUT (23) vs lines expressing it (27) | 2.99× lower at baseline in the lines without PLUT | 0.048 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (28.7, 44.6); signed map (57.9, 16.5). **Vector** length 39.8, 7.64% of its response variance represented; |z| ≥ 3 in 505 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +24.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -1.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.1 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -3.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | PDX1 associated lncRNA, upregulator of transcription |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q12.2 — chr13:27,819,376-27,917,298 (-) |
| Ensembl biotype | lncRNA |
| Also known as | PLUTO, HI-LNC71; previously PDX1-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43698) · Entrez [100861550](https://www.ncbi.nlm.nih.gov/gene/100861550) · Ensembl [ENSG00000247381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247381)

## Data

Gene col 14494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14494); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14494]; `tensor/DDL_lfc|DDL_z.npy` [14494]; `embed/gene_vectors.npy` [14494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14494 or target_col == 14494). Every well: [[PLUT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLUT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
