---
symbol: "CFAP58"
type: "gene"
col: 4152
ensembl_id: "ENSG00000120051"
name: "cilia and flagella associated protein 58"
location: "10q25.1"
module: 137
arm: "+"
pooled_cpm: 2.91
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# CFAP58

*cilia and flagella associated protein 58* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.06× (z +23.7, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.606× (z -5.2, q 1e-04, down in 16 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.184×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.211×); [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 0.0622×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INSYN2A]] (+0.61, fdr 3e-05), [[MEI1]] (+0.58, fdr 4e-05), [[PHC2-AS1]] (+0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[AOX1]] → it (grade B ⚠); 5 go from it, the strongest it → [[ARHGAP31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.06×** | +23.7 | 0e+00 | 22/26 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +12.9 | 1e-35 | 2/4 (SNU-423, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +9.1 | 3e-17 | 15/32 (SW480, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +7.3 | 4e-11 | 8/19 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +7.0 | 4e-10 | 12/36 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +6.5 | 6e-09 | 14/38 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +6.3 | 2e-08 | 14/29 (SW480, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +6.2 | 5e-08 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.2 | 1e-05 | 1/9 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.2 | 0.001 | 2/13 (SNU-423, HS-578T) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.003 | 6/31 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.003 | 4/37 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.008 | 10/36 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.6 | 0.013 | 1/9 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.014 | 5/28 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.023 | 3/37 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.047 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.063 | 5/37 (A-427, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.069 | 0/21 | inconsistent across doses | position effect removed |
| [[Brimonidine (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.069 | 1/28 (A-172) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4152.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.184×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.211×); [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 0.0622×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.606×** | -5.2 | 1e-04 | 16/39 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.698×** | -3.6 | 0.099 | 10/33 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.795× | -3.4 | 0.15 | 10/36 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.733× | -3.2 | 0.19 | 6/37 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.5) |
| [[A-172 (line)]] | wt | 3.66 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +11.1) | — |
| [[A498 (line)]] | wt | 1.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.30× (z +14.0) | — |
| [[RKO (line)]] | wt | 5.74 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0681× (z -8.7) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SW480 (line)]] | alt | 0.993 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +10.2) | — |
| [[A-427 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.960 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSYN2A]] | +0.61 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[MEI1]] | +0.58 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[PHC2-AS1]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SAXO1]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[SLC37A2]] | +0.57 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[FRMD6-AS2]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CCDC26]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[RDUR]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ARHGEF35-AS1]] | +0.56 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[RYR1]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[TMLHE-AS1]] | +0.55 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[DELEC1]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AOX1]] | B | AOX1 activity raises CFAP58's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.50× lower at baseline in the lines without AOX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[TMEM156]] | B | TMEM156 activity raises CFAP58's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.63× lower at baseline in the lines without TMEM156 | 0.009 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[DNAH11]] | B | DNAH11 activity raises CFAP58's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without DNAH11 | 0.023 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[ARHGAP31]] | B | ARHGAP31 activity raises CFAP58's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 1.58× lower at baseline in the lines without ARHGAP31 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[TOP2A]] | B | TOP2A activity lowers CFAP58's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LAMA1]] | B | LAMA1 activity raises CFAP58's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.51× lower at baseline in the lines without LAMA1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises CFAP58's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.50× lower at baseline in the lines without ITGB1-DT | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[CDK6-AS1]] | B | CDK6-AS1 activity raises CFAP58's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without CDK6-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[LTBP2]] | B | LTBP2 activity raises CFAP58's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without LTBP2 | 0.084 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[LNCOG]] | B | LNCOG activity strengthens CFAP58's drug response | lines that do not express LNCOG (25) vs lines expressing it (14) | the lines without LNCOG respond 0.71× as strongly (z diff +0.38); strongest at Doxorubicin (hydrochloride) 5 µM: 1.27x vs 4.31x (z diff +3.5) | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP31]] | B | CFAP58 activity raises ARHGAP31's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 1.90× lower at baseline in the lines without CFAP58 | 0.042 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |
| [[CDK6-AS1]] | B | CFAP58 activity raises CDK6-AS1's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without CFAP58 | 0.068 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |
| [[TMLHE-AS1]] | B | CFAP58 activity raises TMLHE-AS1's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 1.12× lower at baseline in the lines without CFAP58 | 0.079 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |
| [[SAXO1]] | B | CFAP58 activity raises SAXO1's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CFAP58 | 0.094 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |
| [[RASSF8-AS1]] | B | CFAP58 activity raises RASSF8-AS1's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without CFAP58 | 0.097 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.207). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (48.3, -7.8); signed map (23.6, 13.4). **Vector** length 48.3, 6.53% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +23.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.5 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 58 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:104,353,833-104,455,102 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35908, bA554P13.1; previously C10orf80, CCDC147 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T655](https://www.uniprot.org/uniprotkb/Q5T655) (Cilia- and flagella-associated protein 58):

> Has an essential role in the assembly and organization of the sperm flagellar axoneme. Required for the elongation of the primary cilium and sperm flagellar midpiece via modulation of the Notch signaling pathway (By similarity).

**Summary**, from NCBI Gene [159686](https://www.ncbi.nlm.nih.gov/gene/159686):

> Involved in protein localization to motile cilium; sperm axoneme assembly; and sperm mitochondrial sheath assembly. Located in sperm midpiece and sperm principal piece. Implicated in spermatogenic failure 49. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26676) · Entrez [159686](https://www.ncbi.nlm.nih.gov/gene/159686) · UniProt [Q5T655](https://www.uniprot.org/uniprotkb/Q5T655) · Ensembl [ENSG00000120051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120051)

## Data

Gene col 4152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4152); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4152]; `tensor/DDL_lfc|DDL_z.npy` [4152]; `embed/gene_vectors.npy` [4152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4152 or target_col == 4152). Every well: [[CFAP58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
