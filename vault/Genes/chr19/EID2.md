---
symbol: "EID2"
type: "gene"
col: 10711
ensembl_id: "ENSG00000176396"
name: "EP300 interacting inhibitor of differentiation 2"
location: "19q13.2"
module: 11
arm: "+"
pooled_cpm: 12.46
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# EID2

*EP300 interacting inhibitor of differentiation 2* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +8.7, q 2e-15, up in 36 of 40 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.76× (z +6.6, q 7e-09, up in 37 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 6.03×, HOP62 5.23×; ⚠ cell-cycle shift, explains ~49% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 4.07×, A549 7.56×; ⚠ cell-cycle shift, explains ~30% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0883×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRFAP1L1]] (+0.81, fdr 7e-06), [[RPP25L]] (+0.80, fdr 7e-06), [[NSMCE3]] (+0.79, fdr 7e-06); moves opposite to [[CRTAP]] (-0.67, fdr 9e-06), [[EIF2S3]] (-0.66, fdr 1e-05), [[TXNDC5]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCDC71L]] → it (grade B ⚠); 15 go from it, the strongest it → [[DUXAP9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10711.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 6.03×, HOP62 5.23×; ⚠ cell-cycle shift, explains ~49% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 4.07×, A549 7.56×; ⚠ cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.59×** | +8.7 | 2e-15 | 36/40 (A549, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.90×** | +8.5 | 7e-15 | 40/42 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.01×** | +6.9 | 1e-09 | 31/33 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.76×** | +6.6 | 7e-09 | 37/43 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.9 | 1e-04 | 29/41 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.05×** | +4.6 | 3e-04 | 25/38 (A549, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.90×** | +4.1 | 0.003 | 20/35 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.70×** | +3.4 | 0.046 | 11/28 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.67×** | +3.2 | 0.090 | 1/12 (NCI-H2030) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | 1.62× | +3.1 | 0.10 | 17/39 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.61× | +3.1 | 0.11 | 16/43 (A549, HS-578T, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10711.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0883×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.580× | -3.6 | 0.21 | 22/45 (PANC-1, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.619× | -3.1 | 0.46 | 17/43 (NCI-H23, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.722× | -3.0 | 0.46 | 17/44 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 13.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +11.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HOP62 (line)]] | alt | 6.03 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +8.8) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 6.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0883× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.07× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRFAP1L1]] | +0.81 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.80 | +0.75 / +0.83 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.79 | +0.76 / +0.81 | both halves | 7e-06 | STRING 424 |
| [[ZNF75A]] | +0.78 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[UTP3]] | +0.77 | +0.82 / +0.77 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.77 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.75 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.74 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[TBCC]] | +0.73 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[PHAX]] | +0.73 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[METTL18]] | +0.73 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[GPATCH8]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAP]] | -0.67 | -0.57 / -0.75 | both halves | 9e-06 |  |
| [[EIF2S3]] | -0.66 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.65 | -0.62 / -0.74 | both halves | 7e-06 |  |
| [[RPA1]] | -0.65 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[AGO1]] | -0.65 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[RPN1]] | -0.65 | -0.59 / -0.77 | both halves | 7e-06 |  |
| [[SMG1P3]] | -0.63 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.63 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[NUTF2]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[TECR]] | -0.63 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[TBCD]] | -0.62 | -0.61 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC71L]] | B | CCDC71L activity lowers EID2's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.80× higher at baseline in the lines without CCDC71L | 0.035 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[TBX3]] | B | TBX3 activity raises EID2's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without TBX3 | 0.076 | ⚠ within organs, on part of the lines |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP9]] | C | EID2 activity raises DUXAP9's level | lines that do not express EID2 (3) vs lines expressing it (47) | 5.67× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |
| [[DUXAP8]] | C | EID2 activity raises DUXAP8's level | lines that do not express EID2 (3) vs lines expressing it (47) | 5.00× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |
| [[ERCC4]] | C | EID2 activity raises ERCC4's level | lines that do not express EID2 (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |
| [[PLPP6]] | C | EID2 activity raises PLPP6's level | lines that do not express EID2 (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TMED7]] | C | EID2 activity lowers TMED7's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.97× higher at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |
| [[KCNIP2]] | C | EID2 activity raises KCNIP2's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |
| [[C1orf131]] | C | EID2 activity raises C1orf131's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |
| [[DDX28]] | C | EID2 activity raises DDX28's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |
| [[OXLD1]] | C | EID2 activity raises OXLD1's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.90× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent |
| [[NAIF1]] | C | EID2 activity raises NAIF1's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.42× lower at baseline in the lines without EID2 | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent |
| [[ZNF830]] | C | EID2 activity raises ZNF830's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.50× lower at baseline in the lines without EID2 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent |
| [[NSMCE3]] | C | EID2 activity raises NSMCE3's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without EID2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.844). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.2, 5.0); signed map (1.7, -19.0). **Vector** length 71.8, 16.9% of its response variance represented; |z| ≥ 3 in 609 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.5 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.0 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.0 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +1.3 | +1.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | -3.3 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | -3.3 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.6 |
|  | [[Lonafarnib (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | EP300 interacting inhibitor of differentiation 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,538,707-39,540,161 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EID-2, MGC20452; previously CRI2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6I1](https://www.uniprot.org/uniprotkb/Q8N6I1) (EP300-interacting inhibitor of differentiation 2):

> Interacts with EP300 and acts as a repressor of MYOD-dependent transcription and muscle differentiation. Inhibits EP300 histone acetyltransferase activity. Acts as a repressor of TGFB/SMAD transcriptional responses. May act as a repressor of the TGFB/SMAD3-dependent signaling by selectively blocking formation of TGFB-induced SMAD3-SMAD4 complex.

**Summary**, from NCBI Gene [163126](https://www.ncbi.nlm.nih.gov/gene/163126):

> Enables SMAD binding activity. Involved in several processes, including negative regulation of transcription by RNA polymerase II; negative regulation of transmembrane receptor protein serine/threonine kinase signaling pathway; and transforming growth factor beta receptor complex assembly. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28292) · Entrez [163126](https://www.ncbi.nlm.nih.gov/gene/163126) · UniProt [Q8N6I1](https://www.uniprot.org/uniprotkb/Q8N6I1) · Ensembl [ENSG00000176396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176396)

## Data

Gene col 10711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10711); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10711]; `tensor/DDL_lfc|DDL_z.npy` [10711]; `embed/gene_vectors.npy` [10711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10711 or target_col == 10711). Every well: [[EID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
