---
symbol: "SPINK5"
type: "gene"
col: 5469
ensembl_id: "ENSG00000133710"
name: "serine peptidase inhibitor Kazal type 5"
location: "5q32"
module: 27
arm: "+"
pooled_cpm: 10.5
n_lines_expressing: 15
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 26
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SPINK5

*serine peptidase inhibitor Kazal type 5* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.61× (z +11.1, q 5e-26, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +9.5, q 3e-19, up in 2 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.471× (z -5.5, q 2e-05, down in 10 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.166×, SK-MEL-2 0.0939×); [[Belinostat (drug)]] 5 µM in 2 lines (LoVo 0.177×, Panc 03.27 0.0896×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01611]] (+0.60, fdr 2e-05), [[LINC02315]] (+0.59, fdr 2e-05), [[DACH1]] (+0.59, fdr 4e-05); moves opposite to [[TPST2]] (-0.56, fdr 7e-05), [[GNA12]] (-0.49, fdr 4e-04), [[TPD52L2]] (-0.49, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 26 go from it, the strongest it → [[LINC00578]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.61×** | +11.1 | 5e-26 | 4/7 (Hs 766T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.17×** | +10.0 | 4e-21 | 2/3 (LoVo, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +9.5 | 3e-19 | 2/13 (LS 180, KATO III) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.69×** | +8.8 | 2e-16 | 3/4 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.20×** | +8.1 | 6e-14 | 6/12 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.96×** | +4.7 | 2e-04 | 4/13 (LoVo, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +4.6 | 3e-04 | 3/12 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.79×** | +4.2 | 0.002 | 3/13 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.67×** | +3.7 | 0.012 | 4/12 (LoVo, LS 180, …) | rises with dose |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.60×** | +3.4 | 0.035 | 3/13 (SHP-77, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.039 | 5/13 (KATO III, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.3 | 0.048 | 1/13 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.053 | 1/13 (KATO III) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.080 | 0/13 | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.24×** | +3.1 | 0.080 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.0 | 0.087 | 1/11 (Hs 766T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5469.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.166×, SK-MEL-2 0.0939×); [[Belinostat (drug)]] 5 µM in 2 lines (LoVo 0.177×, Panc 03.27 0.0896×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.471×** | -5.5 | 2e-05 | 10/13 (LoVo, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.555×** | -4.3 | 0.005 | 13/13 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.630× | -3.4 | 0.14 | 8/13 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.647× | -3.2 | 0.16 | 6/13 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.437× | -3.2 | 0.16 | 4/13 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.651× | -3.1 | 0.16 | 5/13 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | 0.656× | -3.1 | 0.16 | 0/13 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 140 | 3 (3 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 8.85× (z +13.4) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.109× (z -14.1) |
| [[Hs 766T (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0896× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0939× (z -9.6) |
| [[A-172 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.992 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.988 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.974 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01611]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[LINC02315]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[DACH1]] | +0.59 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[SLC44A5]] | +0.58 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[PKHD1]] | +0.58 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[ADGRV1]] | +0.58 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[BANK1]] | +0.58 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[UNC80]] | +0.57 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[LINC02466]] | +0.57 | +0.45 / +0.36 | both halves | 9e-05 |  |
| [[MIR325HG]] | +0.57 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[LINC01091]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[AGMO]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.56 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[GNA12]] | -0.49 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[TPD52L2]] | -0.49 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[PIGF]] | -0.48 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[ARHGEF18]] | -0.48 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[FBH1]] | -0.47 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[PIP4K2A]] | -0.46 | -0.35 / -0.32 | both halves | 1e-04 |  |
| [[PWWP3A]] | -0.46 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[LIMK1]] | -0.46 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[DCUN1D2]] | -0.46 | -0.37 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SPINK5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers SPINK5's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GUCY1A1]] | C | GUCY1A1 activity raises SPINK5's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without GUCY1A1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046; co-absent with the target |
| [[F5]] | C | F5 activity raises SPINK5's level | lines that do not express F5 (39) vs lines expressing it (11) | 2.29× lower at baseline in the lines without F5 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 13, C 13. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00578]] | B | SPINK5 activity raises LINC00578's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.83× lower at baseline in the lines without SPINK5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[DIP2C-AS1]] | B | SPINK5 activity raises DIP2C-AS1's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.68× lower at baseline in the lines without SPINK5 | 0.007 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[GRM7]] | B | SPINK5 activity raises GRM7's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 2.14× lower at baseline in the lines without SPINK5 | 0.014 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[ATL1]] | B | SPINK5 activity raises ATL1's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without SPINK5 | 0.026 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[UNC80]] | B | SPINK5 activity raises UNC80's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without SPINK5 | 0.035 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[PNPLA4]] | B | SPINK5 activity raises PNPLA4's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.63× lower at baseline in the lines without SPINK5 | 0.041 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[C11orf52]] | B | SPINK5 activity raises C11orf52's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.85× lower at baseline in the lines without SPINK5 | 0.055 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[PER2]] | B | SPINK5 activity raises PER2's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without SPINK5 | 0.069 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[LINC00298]] | B | SPINK5 activity raises LINC00298's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.41× lower at baseline in the lines without SPINK5 | 0.072 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[PATL2]] | B | SPINK5 activity strengthens PATL2's drug response | lines that do not express SPINK5 (35) vs lines expressing it (12) | the lines without SPINK5 respond 0.75× as strongly (z diff +1.26); strongest at Harringtonine 5 µM: 7.85x vs 12x (z diff +2.0) | 0.076 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588; target measured in part of the lines; artifact flags |
| [[ELAPOR2]] | B | SPINK5 activity raises ELAPOR2's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 2.23× lower at baseline in the lines without SPINK5 | 0.079 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[LINC01091]] | B | SPINK5 activity raises LINC01091's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 2.18× lower at baseline in the lines without SPINK5 | 0.094 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.4, 42.5); signed map (47.6, 32.9). **Vector** length 31.7, 7.75% of its response variance represented; |z| ≥ 3 in 274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.3 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.1 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | serine peptidase inhibitor Kazal type 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:148,025,683-148,137,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VAKTI, LEKTI, LETKI, NETS, NS, FLJ21544, FLJ97536, FLJ97596 |
| Gene groups (HGNC) | Serine peptidase inhibitors, Kazal type |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ38](https://www.uniprot.org/uniprotkb/Q9NQ38) (Serine protease inhibitor Kazal-type 5):

> Serine protease inhibitor, probably important for the anti-inflammatory and/or antimicrobial protection of mucous epithelia. Contribute to the integrity and protective barrier function of the skin by regulating the activity of defense-activating and desquamation-involved proteases. Inhibits KLK5, its major target, in a pH-dependent manner. Inhibits KLK7, KLK14 CASP14, and trypsin.

**Summary**, from NCBI Gene [11005](https://www.ncbi.nlm.nih.gov/gene/11005):

> This gene encodes a multidomain serine protease inhibitor that contains 15 potential inhibitory domains. The encoded preproprotein is proteolytically processed to generate multiple protein products, which may exhibit unique activities and specificities. These proteins may play a role in skin and hair morphogenesis, as well as anti-inflammatory and antimicrobial protection of mucous epithelia. Mutations in this gene may result in Netherton syndrome, a disorder characterized by ichthyosis, …

**Accessions** — [HGNC:15464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15464) · Entrez [11005](https://www.ncbi.nlm.nih.gov/gene/11005) · UniProt [Q9NQ38](https://www.uniprot.org/uniprotkb/Q9NQ38) · Ensembl [ENSG00000133710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133710)

## Data

Gene col 5469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5469); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5469]; `tensor/DDL_lfc|DDL_z.npy` [5469]; `embed/gene_vectors.npy` [5469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5469 or target_col == 5469). Every well: [[SPINK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPINK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
