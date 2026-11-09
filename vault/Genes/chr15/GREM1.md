---
symbol: "GREM1"
type: "gene"
col: 9390
ensembl_id: "ENSG00000166923"
name: "gremlin 1, DAN family BMP antagonist"
location: "15q13.3"
module: 13
arm: "+"
pooled_cpm: 15.39
n_lines_expressing: 12
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 21
direction_downstream: 17
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GREM1

*gremlin 1, DAN family BMP antagonist* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.41× (z +12.1, q 1e-30, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.83× (z +9.9, q 6e-21, up in 1 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.505× (z -4.6, q 0.002, down in 4 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.142×; ⚠ cell-cycle shift, explains ~86% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.132×; ⚠ cell-cycle shift, explains ~56% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (hTERT-HPNE 0.139×; ⚠ cell-cycle shift, explains ~57% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.184×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL6]] (+0.68, fdr 1e-05), [[INHBA]] (+0.65, fdr 1e-05), [[FGF5]] (+0.61, fdr 1e-05); moves opposite to [[SLC35A1]] (-0.46, fdr 1e-04), [[ANAPC4]] (-0.43, fdr 9e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[EVC2]] → it (grade C ⚠); 17 go from it, the strongest it → [[ZNF469]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.41×** | +12.1 | 1e-30 | 5/6 (A-427, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.01×** | +10.9 | 4e-25 | 6/7 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +9.9 | 6e-21 | 1/8 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +7.4 | 2e-11 | 3/6 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.12×** | +3.6 | 0.027 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **2.10×** | +3.6 | 0.027 | 3/8 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.027 | 1/8 (C-33 A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.88×** | +3.5 | 0.027 | 1/5 (SNU-423) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.67×** | +3.5 | 0.033 | 0/9 | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.057 | 2/8 (hTERT-HPNE, RPMI-7951) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.2 | 0.066 | 1/8 (A549) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.94×** | +3.2 | 0.068 | 1/9 (NCI-H1792) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.1 | 0.069 | 3/7 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +3.1 | 0.069 | 6/8 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +3.0 | 0.098 | 1/9 (RPMI-7951) | two highest doses | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9390.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.142×; ⚠ cell-cycle shift, explains ~86% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.132×; ⚠ cell-cycle shift, explains ~56% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (hTERT-HPNE 0.139×; ⚠ cell-cycle shift, explains ~57% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.184×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.505×** | -4.6 | 0.002 | 4/8 (RPMI-7951, SNU-423, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.718× | -3.2 | 0.27 | 6/10 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.631× | -3.1 | 0.27 | 4/9 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.609× | -3.1 | 0.27 | 0/8 | inconsistent across doses | position effect removed |
| [[Captopril (drug)]] 0.05 µM |  | 0.638× | -3.0 | 0.27 | 2/8 (C-33 A, A549) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 636 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -11.6) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.184× (z -9.7) |
| [[A-427 (line)]] | wt | 99.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.4) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A-172 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL6]] | +0.68 | +0.55 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[INHBA]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 410 |
| [[FGF5]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[BAALC]] | +0.58 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[SHISAL1]] | +0.58 | +0.39 / +0.66 | both halves | 6e-05 |  |
| [[VEGFC]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[LINC01411]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[DSE]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[STEAP1B-AS1]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[KIRREL3]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[VSTM4]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NTNG2]] | +0.56 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A1]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ANAPC4]] | -0.43 | -0.36 / -0.38 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVC2]] | C | EVC2 activity raises GREM1's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.33× lower at baseline in the lines without EVC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises GREM1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 4.05× lower at baseline in the lines without LINC01411 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[COL5A3]] | C | COL5A3 activity raises GREM1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without COL5A3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises GREM1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.77× lower at baseline in the lines without APCDD1L | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[GCG]] | C | GCG activity raises GREM1's level | lines that do not express GCG (46) vs lines expressing it (4) | 6.03× lower at baseline in the lines without GCG | 0.021 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises GREM1's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.38× lower at baseline in the lines without TCF4 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises GREM1's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 2.63× lower at baseline in the lines without TRPC4 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[DIRAS3]] | C | DIRAS3 activity raises GREM1's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 4.20× lower at baseline in the lines without DIRAS3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises GREM1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.77× lower at baseline in the lines without ITGA11 | 0.035 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises GREM1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 3.49× lower at baseline in the lines without GDNF | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises GREM1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.04× lower at baseline in the lines without CDH13 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[PLEKHG4B]] | C | PLEKHG4B activity raises GREM1's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.85× lower at baseline in the lines without PLEKHG4B | 0.042 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF469]] | B | GREM1 activity raises ZNF469's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 2.43× lower at baseline in the lines without GREM1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP |
| [[COL5A3]] | C | GREM1 activity raises COL5A3's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 3.10× lower at baseline in the lines without GREM1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[MIR493HG]] | C | GREM1 activity raises MIR493HG's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 3.25× lower at baseline in the lines without GREM1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[EVC2]] | C | GREM1 activity raises EVC2's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 4.67× lower at baseline in the lines without GREM1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[MEG3]] | C | GREM1 activity raises MEG3's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 4.12× lower at baseline in the lines without GREM1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[PAPPA]] | C | GREM1 activity raises PAPPA's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 4.11× lower at baseline in the lines without GREM1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[PRRX1]] | C | GREM1 activity raises PRRX1's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 3.28× lower at baseline in the lines without GREM1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[ITGA11]] | C | GREM1 activity raises ITGA11's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 3.28× lower at baseline in the lines without GREM1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[IL1B]] | C | GREM1 activity raises IL1B's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 3.10× lower at baseline in the lines without GREM1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[COL1A1]] | C | GREM1 activity raises COL1A1's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 3.30× lower at baseline in the lines without GREM1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[P3H2]] | C | GREM1 activity raises P3H2's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 2.30× lower at baseline in the lines without GREM1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[ABI3BP]] | C | GREM1 activity raises ABI3BP's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 2.28× lower at baseline in the lines without GREM1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.1, 14.5); signed map (19.9, 50.3). **Vector** length 27.1, 7.53% of its response variance represented; |z| ≥ 3 in 248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +9.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -4.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | gremlin 1, DAN family BMP antagonist |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:32,718,004-32,745,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRM, gremlin, DAND2, HMPS; previously CKTSF1B1, CRAC1 |
| Gene groups (HGNC) | DAN family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: Formation of the ureteric bud; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [O60565](https://www.uniprot.org/uniprotkb/O60565) (Gremlin-1):

> Cytokine that may play an important role during carcinogenesis and metanephric kidney organogenesis, as a BMP antagonist required for early limb outgrowth and patterning in maintaining the FGF4-SHH feedback loop. Down-regulates the BMP4 signaling in a dose-dependent manner (By similarity). Antagonist of BMP2; inhibits BMP2-mediated differentiation of osteoblasts (in vitro). Acts as inhibitor of monocyte chemotaxis. Can inhibit the growth or viability of normal cells but not transformed cells …

**Summary**, from NCBI Gene [26585](https://www.ncbi.nlm.nih.gov/gene/26585):

> This gene encodes a member of the BMP (bone morphogenic protein) antagonist family. Like BMPs, BMP antagonists contain cystine knots and typically form homo- and heterodimers. The CAN (cerberus and dan) subfamily of BMP antagonists, to which this gene belongs, is characterized by a C-terminal cystine knot with an eight-membered ring. The antagonistic effect of the secreted glycosylated protein encoded by this gene is likely due to its direct binding to BMP proteins. As an antagonist of BMP, …

**Accessions** — [HGNC:2001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2001) · Entrez [26585](https://www.ncbi.nlm.nih.gov/gene/26585) · UniProt [O60565](https://www.uniprot.org/uniprotkb/O60565) · Ensembl [ENSG00000166923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166923)

## Data

Gene col 9390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9390); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9390]; `tensor/DDL_lfc|DDL_z.npy` [9390]; `embed/gene_vectors.npy` [9390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9390 or target_col == 9390). Every well: [[GREM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GREM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
