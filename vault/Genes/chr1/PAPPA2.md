---
symbol: "PAPPA2"
type: "gene"
col: 3771
ensembl_id: "ENSG00000116183"
name: "pappalysin 2"
location: "1q25.2"
module: 19
arm: "+"
pooled_cpm: 11.38
n_lines_expressing: 22
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PAPPA2

*pappalysin 2* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 9.14× (z +19.3, q 0e+00, up in 17 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.637× (z -4.0, q 0.043, down in 9 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (H4 0.0729×, NCI-H460 0.304×); [[Harringtonine (drug)]] 0.05 µM in 2 lines (H4 0.0844×, hTERT-HPNE 0.0527×); [[Ouabain (Octahydrate) (drug)]] 0.05 µM in 2 lines (H4 0.103×, NCI-H460 0.212×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COP1-DT]] (+0.90, fdr 7e-06, ⚠ same locus), [[TTTY14]] (+0.65, fdr 7e-06), [[CDH7]] (+0.63, fdr 2e-05), [[GLP2R]] (+0.59, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[COP1-DT]] → it (grade B ⚠); 12 go from it, the strongest it → [[COP1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **9.14×** | +19.3 | 0e+00 | 17/17 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +13.1 | 2e-36 | 7/14 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.14×** | +9.2 | 5e-18 | 2/7 (LOX-IMVI, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +8.8 | 2e-16 | 2/6 (HOP62, LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +8.5 | 2e-15 | 5/9 (LOX-IMVI, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +6.3 | 3e-08 | 3/12 (HCT15, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.03×** | +6.2 | 6e-08 | 10/15 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +6.0 | 1e-07 | 2/14 (LS 180, C-33 A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.56×** | +5.4 | 3e-06 | 10/19 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.53×** | +5.2 | 1e-05 | 6/18 (NCI-H460, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.1 | 2e-05 | 6/14 (LOX-IMVI, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.0 | 3e-05 | 3/19 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +4.8 | 8e-05 | 6/15 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +4.5 | 2e-04 | 3/17 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.002 | 11/18 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.005 | 3/13 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.51×** | +3.6 | 0.012 | 4/18 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.021 | 2/17 (H4, NCI-H1573) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3771.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (H4 0.0729×, NCI-H460 0.304×); [[Harringtonine (drug)]] 0.05 µM in 2 lines (H4 0.0844×, hTERT-HPNE 0.0527×); [[Ouabain (Octahydrate) (drug)]] 0.05 µM in 2 lines (H4 0.103×, NCI-H460 0.212×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -4.0 | 0.043 | 9/16 (H4, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.668× | -3.5 | 0.11 | 11/18 (NCI-H460, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.704× | -3.1 | 0.39 | 9/16 (H4, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 123 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0729× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 125 | 1 | 8 (5 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.68× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.171× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 10.7× (z +9.1) | [[Harringtonine (drug)]] 0.05 µM 0.0527× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 23.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 2.91 | 1 | 0 | [[Auranofin (drug)]] 5 µM 20.1× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -8.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SK-MEL-2 (line)]] | alt | 3.16 | 1 | 0 | [[Auranofin (drug)]] 5 µM 28.8× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COP1-DT]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | ⚠ same locus (15.3 kb, same strand: neighbours can correlate without regulation) |
| [[TTTY14]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CDH7]] | +0.63 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[GLP2R]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[VLDLR-AS1]] | +0.59 | +0.43 / +0.62 | both halves | 4e-05 |  |
| [[NMRAL2P-1]] | +0.58 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[KCNMB2]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[DOK6]] | +0.57 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[LINC01684]] | +0.57 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[NMRAL2P]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[TDO2]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[CTNND2]] | +0.55 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[LINC03000]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COP1-DT]] | B | COP1-DT activity raises PAPPA2's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without COP1-DT | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PAPPA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PDE3A]] | C | PDE3A activity raises PAPPA2's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without PDE3A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[TDO2]] | C | TDO2 activity raises PAPPA2's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without TDO2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises PAPPA2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without KCNE4 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises PAPPA2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.96× lower at baseline in the lines without KCNH5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises PAPPA2's level | lines that do not express TBXT (47) vs lines expressing it (3) | 6.26× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[CTNND2]] | C | CTNND2 activity raises PAPPA2's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 3.28× lower at baseline in the lines without CTNND2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[EPB41L3]] | C | EPB41L3 activity raises PAPPA2's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without EPB41L3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[LINC01684]] | C | LINC01684 activity raises PAPPA2's level | lines that do not express LINC01684 (30) vs lines expressing it (20) | 2.30× lower at baseline in the lines without LINC01684 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IRAG2, COL3A1, LINC01592; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 7, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COP1-DT]] | B | PAPPA2 activity raises COP1-DT's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.86× lower at baseline in the lines without PAPPA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[ANO3]] | B | PAPPA2 activity weakens ANO3's drug response | lines that do not express PAPPA2 (26) vs lines expressing it (17) | the lines without PAPPA2 respond 5.51× as strongly (z diff -1.46); strongest at Homoharringtonine 5 µM: 2.45x vs 0.53x (z diff -6.5) | 0.010 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ARHGEF6]] | B | PAPPA2 activity raises ARHGEF6's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without PAPPA2 | 0.025 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[DDR2]] | B | PAPPA2 activity raises DDR2's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without PAPPA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[SLCO1C1]] | B | PAPPA2 activity raises SLCO1C1's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 1.73× lower at baseline in the lines without PAPPA2 | 0.056 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[BMPER]] | B | PAPPA2 activity raises BMPER's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without PAPPA2 | 0.071 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| cells under [[ULK-101 (drug)]] 5 µM | B | PAPPA2 activity lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | lines that do not express PAPPA2 (28) vs lines expressing it (20) | the lines without PAPPA2: 1.20× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[KCNK2]] | C | PAPPA2 activity raises KCNK2's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without PAPPA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | PAPPA2 activity raises KCNE4's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 3.30× lower at baseline in the lines without PAPPA2 | 0.036 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; co-absent with the target |
| [[EPB41L3]] | C | PAPPA2 activity raises EPB41L3's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without PAPPA2 | 0.091 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; co-absent with the target |
| [[SIRLNT]] | C | PAPPA2 activity raises SIRLNT's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without PAPPA2 | 0.092 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; co-absent with the target |
| [[ACSS3]] | C | PAPPA2 activity raises ACSS3's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without PAPPA2 | 0.094 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.6, 36.6); signed map (41.3, 41.6). **Vector** length 50.6, 13.2% of its response variance represented; |z| ≥ 3 in 473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | pappalysin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:176,463,171-176,845,601 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAPPE, PAPP-A2; previously PLAC3 |
| Gene groups (HGNC) | Pappalysins; Sushi domain containing |
| Reactome | 1 pathways, smallest: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXP8](https://www.uniprot.org/uniprotkb/Q9BXP8) (Pappalysin-2):

> Metalloproteinase which specifically cleaves insulin-like growth factor binding protein (IGFBP)-5 at the '163-Ser-|-Lys-164' bond. Shows limited proteolysis toward IGFBP-3.

**Summary**, from NCBI Gene [60676](https://www.ncbi.nlm.nih.gov/gene/60676):

> This gene encodes a member of the pappalysin family of metzincin metalloproteinases. The encoded protein cleaves insulin-like growth factor-binding protein 5 and is thought to be a local regulator of insulin-like growth factor (IGF) bioavailability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:14615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14615) · Entrez [60676](https://www.ncbi.nlm.nih.gov/gene/60676) · UniProt [Q9BXP8](https://www.uniprot.org/uniprotkb/Q9BXP8) · Ensembl [ENSG00000116183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116183)

## Data

Gene col 3771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3771); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3771]; `tensor/DDL_lfc|DDL_z.npy` [3771]; `embed/gene_vectors.npy` [3771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3771 or target_col == 3771). Every well: [[PAPPA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAPPA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
