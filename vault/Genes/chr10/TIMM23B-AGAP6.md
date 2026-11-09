---
symbol: "TIMM23B-AGAP6"
type: "gene"
col: 10928
ensembl_id: "ENSG00000178440"
name: "TIMM23B-AGAP6 readthrough (NMD candidate)"
location: "10q11.23"
module: 5
arm: "+"
pooled_cpm: 4.91
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TIMM23B-AGAP6

*TIMM23B-AGAP6 readthrough (NMD candidate)* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.54× (z +9.1, q 4e-17, up in 38 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 0.118×, A498 0.144×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.114×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[DT-061 (drug)]] 0.05 µM in 1 line (NCI-H23 0.0559×); [[Decitabine (drug)]] 0.5 µM in 1 line (NCI-H23 0.0931×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGAP6]] (+0.84, fdr 7e-06, ⚠ same locus), [[NPIPB11]] (+0.71, fdr 7e-06), [[TIMM23B]] (+0.69, fdr 7e-06, ⚠ read-through risk), [[TRNT1]] (+0.69, fdr 7e-06), [[TOMM40]] (+0.69, fdr 7e-06); moves opposite to [[RYBP]] (-0.69, fdr 7e-06), [[RAB30]] (-0.67, fdr 1e-05), [[MYLIP]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ABI1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.54×** | +9.1 | 4e-17 | 38/43 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +8.4 | 9e-15 | 25/40 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.70×** | +7.0 | 4e-10 | 24/37 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.98×** | +7.0 | 4e-10 | 26/47 (SW480, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.98×** | +6.7 | 3e-09 | 17/36 (SW480, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.85×** | +6.2 | 4e-08 | 22/45 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +6.0 | 2e-07 | 22/46 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +5.9 | 3e-07 | 18/45 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.8 | 3e-07 | 18/39 (HCT15, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.74×** | +5.4 | 4e-06 | 16/40 (SW480, Panc 03.27, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.69×** | +5.3 | 6e-06 | 17/45 (SW480, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.66×** | +5.1 | 1e-05 | 20/45 (SW480, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.62×** | +4.9 | 4e-05 | 16/45 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 1e-04 | 14/38 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +4.5 | 3e-04 | 17/43 (H4, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.008 | 13/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.013 | 12/44 (PANC-1, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.015 | 10/45 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.052 | 8/44 (C-33 A, NCI-H460, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.086 | 2/46 (AsPC-1, NCI-H1573) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +2.8 | 0.099 | 7/46 (CFPAC-1, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 0.118×, A498 0.144×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.114×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[DT-061 (drug)]] 0.05 µM in 1 line (NCI-H23 0.0559×); [[Decitabine (drug)]] 0.5 µM in 1 line (NCI-H23 0.0931×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | 0.708× | -3.6 | 0.17 | 11/28 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.792× | -3.4 | 0.17 | 14/45 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.729× | -3.3 | 0.21 | 13/44 (Panc 03.27, AsPC-1, …) | top dose only |  |
| [[Drospirenone (drug)]] 0.05 µM |  | 0.740× | -3.1 | 0.25 | 10/45 (HOP62, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.746× | -3.0 | 0.28 | 5/46 (KATO III, A-172, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 5.11 | 0 | 2 | — | [[DT-061 (drug)]] 0.05 µM 0.0559× (z -9.7) |
| [[PANC-1 (line)]] | alt | 6.98 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[A498 (line)]] | wt | 5.91 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 6.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP6]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NPIPB11]] | +0.71 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[TIMM23B]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of TIMM23B on the same strand (can correlate by spillover, not regulation) |
| [[TRNT1]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.69 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ATR]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[WDR4]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ARIH2]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ALG8]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[KANSL1L-AS1]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PRDM15]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[GTPBP4]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | -0.69 | -0.59 / -0.73 | both halves | 7e-06 |  |
| [[RAB30]] | -0.67 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[MYLIP]] | -0.65 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[SNX2]] | -0.64 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[LCA5]] | -0.64 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[DBP]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[BIK]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MAPRE2]] | -0.61 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[LINC01273]] | -0.60 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[HPF1]] | -0.60 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.59 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[CYRIA]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TIMM23B-AGAP6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TCN2]] | B | TCN2 activity lowers TIMM23B-AGAP6's level | lines that do not express TCN2 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without TCN2 | 0.057 | ⚠ within organs, on part of the lines; also absent: PRSS23, TMSB4X, ARHGAP23; maybe low, not absent |
| [[MTHFD1L]] | C | MTHFD1L activity raises TIMM23B-AGAP6's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABI1]] | C | TIMM23B-AGAP6's natural level strengthens ABI1's drug response | TIMM23B-AGAP6's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.09; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.6, -29.4); signed map (2.8, -53.8). **Vector** length 53.7, 6.88% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +8.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.2 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.2 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | TIMM23B-AGAP6 readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 10q11.23 — chr10:49,942,056-50,011,654 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LINC00843 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [113218477](https://www.ncbi.nlm.nih.gov/gene/113218477):

> This locus represents naturally-occurring readthrough transcription between the adjacent TIMM23B (translocase of inner mitochondrial membrane 23 homolog B) and AGAP6 (ArfGAP with GTPase domain, ankyrin repeat and PH domain 6) genes. Readthrough transcripts contain portions of the coding sequence for both genes and are predicted to be candidates for nonsense-mediated decay (NMD). [provided by RefSeq, Sep 2018]

**Accessions** — [HGNC:45009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45009) · Entrez [113218477](https://www.ncbi.nlm.nih.gov/gene/113218477) · Ensembl [ENSG00000178440](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178440)

## Data

Gene col 10928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10928); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10928]; `tensor/DDL_lfc|DDL_z.npy` [10928]; `embed/gene_vectors.npy` [10928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10928 or target_col == 10928). Every well: [[TIMM23B-AGAP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM23B-AGAP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
