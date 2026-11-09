---
symbol: "DSC3"
type: "gene"
col: 5601
ensembl_id: "ENSG00000134762"
name: "desmocollin 3"
location: "18q12.1"
module: 62
arm: "+"
pooled_cpm: 6.31
n_lines_expressing: 19
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 27
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# DSC3

*desmocollin 3* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.31× (z +18.0, q 0e+00, up in 11 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM: 0.626× (z -5.0, q 3e-04, down in 3 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.155×, AsPC-1 0.183×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.231×, A-427 0.237×; ⚠ cell-cycle shift, explains ~89% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.183×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTA2]] (+0.66, fdr 2e-05), [[SPATA18]] (+0.62, fdr 1e-05), [[DRAM1]] (+0.62, fdr 3e-05); moves opposite to [[GCDH]] (-0.57, fdr 0.001, ⚠ not reproduced), [[ASL]] (-0.54, fdr 2e-04), [[GGA1]] (-0.54, fdr 8e-04, ⚠ not reproduced), [[ATG4B]] (-0.53, fdr 4e-04), [[NPHP4]] (-0.53, fdr 5e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[APOBEC3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.31×** | +18.0 | 0e+00 | 11/16 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.53×** | +16.1 | 0e+00 | 10/14 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.60×** | +15.4 | 0e+00 | 7/8 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +10.9 | 1e-25 | 7/9 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.93×** | +9.9 | 4e-21 | 13/17 (A549, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +9.1 | 6e-18 | 11/17 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +7.9 | 2e-13 | 10/17 (A549, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +7.6 | 2e-12 | 4/13 (LS 180, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +6.7 | 1e-09 | 8/17 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.3 | 1e-08 | 7/15 (LS 180, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +6.1 | 5e-08 | 8/16 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.16×** | +5.9 | 2e-07 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +5.3 | 6e-06 | 3/11 (A549, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.88×** | +4.8 | 7e-05 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.35×** | +4.7 | 8e-05 | 1/8 (A549) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +4.6 | 1e-04 | 3/16 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.003 | 4/15 (Hs 766T, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.005 | 5/17 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.009 | 1/13 (LS 180) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.014 | 3/17 (CFPAC-1, J82, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.020 | 6/16 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.026 | 5/17 (A549, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5601.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.155×, AsPC-1 0.183×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.231×, A-427 0.237×; ⚠ cell-cycle shift, explains ~89% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.183×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.626×** | -5.0 | 3e-04 | 3/17 (HS-578T, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.690×** | -3.9 | 0.023 | 10/17 (LoVo, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.743× | -3.2 | 0.30 | 3/17 (SNU-423, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 0.753× | -3.0 | 0.37 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 54.7 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 38.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.22× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -10.3) ⚠ cell-cycle shift, explains ~89% of this change |
| [[LS 180 (line)]] | wt | 3.83 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 8.00 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.20× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.972 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.582 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTA2]] | +0.66 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SPATA18]] | +0.62 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[DRAM1]] | +0.62 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PLCL2]] | +0.61 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[ZMAT3]] | +0.61 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ABCA12]] | +0.59 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[FAS]] | +0.59 | +0.39 / +0.39 | both halves | 5e-05 |  |
| [[APOBEC3C]] | +0.59 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[PDIA3P1]] | +0.59 | +0.40 / +0.34 | both halves | 1e-04 |  |
| [[EFCAB5]] | +0.59 | +0.32 / +0.33 | both halves | 2e-04 |  |
| [[TAFA2]] | +0.58 | +0.36 / +0.37 | both halves | 9e-05 |  |
| [[GFRA1]] | +0.57 | +0.36 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCDH]] | -0.57 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[ASL]] | -0.54 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[GGA1]] | -0.54 | -0.41 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[ATG4B]] | -0.53 | -0.29 / -0.26 | both halves | 4e-04 |  |
| [[NPHP4]] | -0.53 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[MIGA2]] | -0.53 | -0.30 / -0.29 | both halves | 3e-04 |  |
| [[PHKA2]] | -0.52 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[TMEM104]] | -0.52 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[PIGU]] | -0.51 | -0.41 / -0.26 | both halves | 3e-04 |  |
| [[SPATA2L]] | -0.51 | -0.33 / -0.29 | both halves | 2e-04 |  |
| [[SIVA1]] | -0.51 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[NAT9]] | -0.51 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[MLXIP]] | -0.50 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[ANKS3]] | -0.50 | -0.34 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DSC3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.1% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[DSG2]] | B | DSG2 activity raises DSC3's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 2.57× lower at baseline in the lines without DSG2 | 0.094 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[TLL1]] | C | TLL1 activity raises DSC3's level | lines that do not express TLL1 (28) vs lines expressing it (22) | 3.04× lower at baseline in the lines without TLL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: GUCY1A1, CDH6, COL1A1; maybe low, not absent; co-absent with the target |
| [[COL12A1]] | C | COL12A1 activity raises DSC3's level | lines that do not express COL12A1 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without COL12A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; co-absent with the target |
| [[ANK1]] | C | ANK1 activity raises DSC3's level | lines that do not express ANK1 (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without ANK1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LHX1, GPR173; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOBEC3C]] | B | DSC3 activity raises APOBEC3C's level | lines that do not express DSC3 (31) vs lines expressing it (19) | 1.56× lower at baseline in the lines without DSC3 | 0.054 | ⚠ within organs, on part of the lines; also absent: TFF2, VGLL3, MUC16 |
| [[PURPL]] | B | DSC3 activity raises PURPL's level | lines that do not express DSC3 (31) vs lines expressing it (19) | 1.42× lower at baseline in the lines without DSC3 | 0.098 | ⚠ within organs, on part of the lines; also absent: TFF2, VGLL3, MUC16 |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.7, 35.7); signed map (41.9, -22.4). **Vector** length 38.4, 8.30% of its response variance represented; |z| ≥ 3 in 410 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +16.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +18.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.7 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -1.5 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.4 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.7 | +0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.6 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | -0.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.6 | -1.5 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -0.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | desmocollin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:30,989,365-31,042,815 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDHF3, DSC, DSC1, DSC2; previously DSC4 |
| Gene groups (HGNC) | Desmosomal cadherins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14574](https://www.uniprot.org/uniprotkb/Q14574) (Desmocollin-3):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion (By similarity). Required for cell-cell adhesion in the epidermis, as a result required for the maintenance of the dermal cohesion and the dermal barrier function. Required for cell-cell adhesion of epithelial cell layers surrounding the telogen hair club, as a result plays an important role in telogen hair shaft anchorage (By similarity). Essential for successful completion of embryo …

**Summary**, from NCBI Gene [1825](https://www.ncbi.nlm.nih.gov/gene/1825):

> The protein encoded by this gene is a calcium-dependent glycoprotein that is a member of the desmocollin subfamily of the cadherin superfamily. These desmosomal family members, along with the desmogleins, are found primarily in epithelial cells where they constitute the adhesive proteins of the desmosome cell-cell junction and are required for cell adhesion and desmosome formation. The desmosomal family members are arranged in two clusters on chromosome 18, occupying less than 650 kb combined. …

**Accessions** — [HGNC:3037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3037) · Entrez [1825](https://www.ncbi.nlm.nih.gov/gene/1825) · UniProt [Q14574](https://www.uniprot.org/uniprotkb/Q14574) · Ensembl [ENSG00000134762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134762)

## Data

Gene col 5601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5601); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5601]; `tensor/DDL_lfc|DDL_z.npy` [5601]; `embed/gene_vectors.npy` [5601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5601 or target_col == 5601). Every well: [[DSC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
