---
symbol: "BATF"
type: "gene"
col: 7950
ensembl_id: "ENSG00000156127"
name: "basic leucine zipper ATF-like transcription factor"
location: "14q24.3"
module: 98
arm: "+"
pooled_cpm: 3.14
n_lines_expressing: 17
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 15
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# BATF

*basic leucine zipper ATF-like transcription factor* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.53× (z +7.8, q 3e-12, up in 7 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.0214×); [[Panobinostat (drug)]] 0.5 µM in 1 line (BT-474 0.0740×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1M]] (+0.73, fdr 7e-06), [[TLR2]] (+0.62, fdr 1e-05), [[CEBPD]] (+0.62, fdr 1e-05); moves opposite to [[WNT7B]] (-0.57, fdr 1e-05), [[SUN1]] (-0.55, fdr 2e-05), [[ALDOA]] (-0.54, fdr 1e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SAA2-SAA4]], [[SAA4]] → it (grade B ⚠); 15 go from it, the strongest it → [[TGIF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.53×** | +7.8 | 3e-12 | 7/11 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +7.5 | 1e-11 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.34×** | +6.7 | 5e-09 | 1/6 (SW 900) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +6.2 | 1e-07 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.98×** | +5.8 | 1e-06 | 7/15 (NCI-H2347, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.6 | 4e-04 | 4/8 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **2.01×** | +4.2 | 0.002 | 10/14 (BT-474, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.00×** | +4.1 | 0.002 | 7/13 (CFPAC-1, BT-474, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.002 | 1/10 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.93×** | +3.9 | 0.005 | 5/9 (BT-474, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +3.8 | 0.007 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +3.8 | 0.007 | 2/9 (NCI-H2347, SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.84×** | +3.6 | 0.012 | 8/14 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +3.6 | 0.012 | 9/10 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.6 | 0.014 | 1/11 (KATO III) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.80×** | +3.5 | 0.018 | 8/12 (CFPAC-1, BT-474, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +3.2 | 0.041 | 9/14 (NCI-H2347, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7950.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.0214×); [[Panobinostat (drug)]] 0.5 µM in 1 line (BT-474 0.0740×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.564× | -3.3 | 0.33 | 3/11 (AsPC-1, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.584× | -3.3 | 0.33 | 7/14 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 14.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.0214× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 14.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.82× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0740× (z -10.5) |
| [[A-172 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1M]] | +0.73 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[TLR2]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[CEBPD]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 | pathway: Interleukin-4 and Interleukin-13 signaling; STRING 616 |
| [[NNMT]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TRIM29]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[SAA2-SAA4]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SGPP2]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SAMSN1]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[SH3TC1]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SAA4]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FKBP5]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT7B]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[SUN1]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ALDOA]] | -0.54 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[FAM3C2P]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[FAM107B]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SLC14A1]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[UBA6]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[F11R]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[IDS]] | -0.50 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ADAM19]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ASPH]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[WNT7A]] | -0.48 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises BATF's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.00× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.037 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[PSTPIP2]] | B | PSTPIP2 activity raises BATF's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without PSTPIP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[PON3]] | B | PON3 activity raises BATF's level | lines that do not express PON3 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without PON3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[TRIM29]] | C | TRIM29 activity raises BATF's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without TRIM29 | 0.023 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[SAA1]] | C | SAA1 activity raises BATF's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.63× lower at baseline in the lines without SAA1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[SGPP2]] | C | SGPP2 activity raises BATF's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.31× lower at baseline in the lines without SGPP2 | 0.056 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGIF1]] | B | BATF activity lowers TGIF1's level | lines that do not express BATF (33) vs lines expressing it (17) | 1.30× higher at baseline in the lines without BATF | 0.012 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[F11R]] | B | BATF activity raises F11R's level | lines that do not express BATF (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without BATF | 0.014 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[SH3TC1]] | B | BATF activity raises SH3TC1's level | lines that do not express BATF (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without BATF | 0.017 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[KLHL42]] | B | BATF activity weakens KLHL42's drug response | lines that do not express BATF (33) vs lines expressing it (15) | the lines without BATF respond 0.96× as strongly (z diff +0.08); strongest at Belinostat 5 µM: 0.31x vs 0.44x (z diff -3.1) | 0.033 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2; target measured in part of the lines; both ways; artifact flags |
| cells under [[Amsacrine (drug)]] 5 µM | B | BATF activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express BATF (33) vs lines expressing it (15) | the lines without BATF: 0.84× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[HIF1A]] | B | BATF activity weakens HIF1A's drug response | lines that do not express BATF (33) vs lines expressing it (16) | the lines without BATF respond 1.32× as strongly (z diff -1.59); strongest at Homoharringtonine 0.5 µM: 1.78x vs 1.15x (z diff -3.5) | 0.043 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2; target measured in part of the lines; artifact flags |
| cells under [[Pimozide (drug)]] 0.05 µM | B | BATF activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express BATF (33) vs lines expressing it (15) | the lines without BATF: 0.86× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[CEBPD]] | B | BATF activity raises CEBPD's level | lines that do not express BATF (33) vs lines expressing it (17) | 1.79× lower at baseline in the lines without BATF | 0.047 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[LTBR]] | B | BATF activity weakens LTBR's drug response | lines that do not express BATF (26) vs lines expressing it (14) | the lines without BATF respond 1.12× as strongly (z diff -0.64); strongest at Belinostat 5 µM: 0.28x vs 0.38x (z diff -2.1) | 0.063 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2; target measured in part of the lines; artifact flags |
| [[DIP2C-AS1]] | B | BATF activity raises DIP2C-AS1's level | lines that do not express BATF (33) vs lines expressing it (17) | 1.49× lower at baseline in the lines without BATF | 0.077 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[MARVELD1]] | B | BATF activity lowers MARVELD1's level | lines that do not express BATF (33) vs lines expressing it (17) | 1.47× higher at baseline in the lines without BATF | 0.078 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | BATF activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express BATF (33) vs lines expressing it (15) | the lines without BATF: 0.84× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.9, 15.2); signed map (16.7, 29.5). **Vector** length 43.8, 12.9% of its response variance represented; |z| ≥ 3 in 444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.4 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +7.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.9 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +4.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.7 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.6 | +3.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | -0.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.7 | +0.2 |
|  | [[Pimozide (drug)]] 5 µM |  | -0.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | basic leucine zipper ATF-like transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,522,455-75,546,993 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B-ATF, SFA-2, BATF1 |
| Gene groups (HGNC) | Basic leucine zipper ATF-like transcription factor family |
| Hallmark sets | IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_LATE |
| Reactome | 9 pathways, smallest: Differentiation of naive CD4+ T cells to T helper 2 cells (Th2 cells); Interleukin-4 and Interleukin-13 signaling; Differentiation of T cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16520](https://www.uniprot.org/uniprotkb/Q16520) (Basic leucine zipper transcriptional factor ATF-like):

> AP-1 family transcription factor that controls the differentiation of lineage-specific cells in the immune system: specifically mediates the differentiation of T-helper 17 cells (Th17), follicular T-helper cells (TfH), CD8(+) dendritic cells and class-switch recombination (CSR) in B-cells. Acts via the formation of a heterodimer with JUNB that recognizes and binds DNA sequence 5'-TGA[CG]TCA-3'. The BATF-JUNB heterodimer also forms a complex with IRF4 (or IRF8) in immune cells, leading to …

**Summary**, from NCBI Gene [10538](https://www.ncbi.nlm.nih.gov/gene/10538):

> The protein encoded by this gene is a nuclear basic leucine zipper protein that belongs to the AP-1/ATF superfamily of transcription factors. The leucine zipper of this protein mediates dimerization with members of the Jun family of proteins. This protein is thought to be a negative regulator of AP-1/ATF transcriptional events. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:958) · Entrez [10538](https://www.ncbi.nlm.nih.gov/gene/10538) · UniProt [Q16520](https://www.uniprot.org/uniprotkb/Q16520) · Ensembl [ENSG00000156127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156127)

## Data

Gene col 7950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7950); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7950]; `tensor/DDL_lfc|DDL_z.npy` [7950]; `embed/gene_vectors.npy` [7950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7950 or target_col == 7950). Every well: [[BATF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BATF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
