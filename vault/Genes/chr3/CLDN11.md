---
symbol: "CLDN11"
type: "gene"
col: 267
ensembl_id: "ENSG00000013297"
name: "claudin 11"
location: "3q26.2"
module: 116
arm: "+"
pooled_cpm: 8.91
n_lines_expressing: 24
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# CLDN11

*claudin 11* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.66× (z +17.5, q 0e+00, up in 15 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.619×; ⚠ position not correctable); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0503×); [[Trametinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.296×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLIT2]] (+0.57, fdr 3e-05), [[LTBP2]] (+0.54, fdr 3e-05), [[HHIP]] (+0.53, fdr 4e-05); moves opposite to [[CALCOCO2]] (-0.53, fdr 4e-05), [[UCK1]] (-0.49, fdr 1e-04), [[ZFYVE19]] (-0.47, fdr 7e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[TGIF2-RAB5IF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.66×** | +17.5 | 0e+00 | 15/16 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.83×** | +16.8 | 0e+00 | 12/15 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.12×** | +15.0 | 0e+00 | 7/8 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +14.2 | 3e-43 | 9/17 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.83×** | +11.8 | 3e-30 | 8/9 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +6.7 | 3e-09 | 7/16 (hTERT-HPNE, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +6.5 | 7e-09 | 5/12 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +6.4 | 1e-08 | 8/18 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +6.3 | 2e-08 | 6/18 (CFPAC-1, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +6.0 | 1e-07 | 9/18 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.2 | 1e-05 | 6/18 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.63×** | +4.6 | 2e-04 | 5/17 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.6 | 2e-04 | 5/16 (hTERT-HPNE, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.60×** | +4.3 | 8e-04 | 4/17 (HepG2/C3A, NCI-H1792, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.33×** | +4.2 | 1e-03 | 2/8 (hTERT-HPNE, NCI-H1792) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.005 | 1/18 (LOX-IMVI) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.009 | 5/21 (SW 900, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.011 | 6/17 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.049 | 3/17 (SW 900, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 267.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.619×; ⚠ position not correctable); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0503×); [[Trametinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.296×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | 0.714× | -3.3 | 0.25 | 5/20 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.714× | -3.3 | 0.25 | 0/18 | rises with dose |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.792× | -3.2 | 0.25 | 3/19 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.798× | -3.1 | 0.27 | 3/19 (NCI-H1792, CHP-212, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.730× | -3.0 | 0.27 | 6/17 (Hs 766T, Panc 03.27, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 77.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.95× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 24.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.21× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 88.2 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.619× (z -11.9) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.296× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 6.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 3.01 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0503× (z -9.6) |
| [[Hs 766T (line)]] | wt | 39.8 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.202× (z -8.6) ⚠ cell-cycle shift, explains ~2% of this change |
| [[J82 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 4.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +9.5) | — |
| [[SW480 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.68× (z +9.2) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[A-172 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.978 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLIT2]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 | same gene group; pathway: HALLMARK_APICAL_JUNCTION |
| [[LTBP2]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[HHIP]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[NFE2L3]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CCDC190]] | +0.51 | +0.52 / +0.49 | both halves | 2e-05 |  |
| [[FGF1]] | +0.51 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SCG2]] | +0.51 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SFTA1P]] | +0.50 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[CDH6]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[SOCS2-AS1]] | +0.49 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[RGS4]] | +0.49 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[SLC4A7]] | +0.48 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALCOCO2]] | -0.53 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[UCK1]] | -0.49 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ZFYVE19]] | -0.47 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[AGTRAP]] | -0.46 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[IRAK3]] | -0.46 | -0.48 / -0.41 | both halves | 4e-05 | same gene group |
| [[MRGBP]] | -0.46 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[YIPF1]] | -0.45 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[CIAO3]] | -0.44 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[TLR2]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[EIF2B4]] | -0.43 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ZYG11B]] | -0.43 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[MKRN2]] | -0.43 | -0.46 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLDN11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[B4GALT6]] | B | B4GALT6 activity lowers CLDN11's level | lines that do not express B4GALT6 (9) vs lines expressing it (41) | 2.43× higher at baseline in the lines without B4GALT6 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGIF2-RAB5IF]] | B | CLDN11 activity raises TGIF2-RAB5IF's level | lines that do not express CLDN11 (26) vs lines expressing it (24) | 1.51× lower at baseline in the lines without CLDN11 | 0.062 | ⚠ within organs, on part of the lines; also absent: LAPTM5, SLC25A24P1, CCDC152; maybe low, not absent |
| [[B4GALT6]] | B | CLDN11 activity lowers B4GALT6's level | lines that do not express CLDN11 (26) vs lines expressing it (24) | 1.15× higher at baseline in the lines without CLDN11 | 0.068 | ⚠ within organs, on part of the lines; also absent: LAPTM5, SLC25A24P1, CCDC152; maybe low, not absent |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.7, 14.8); signed map (16.8, 43.5). **Vector** length 35.3, 6.10% of its response variance represented; |z| ≥ 3 in 503 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +15.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +16.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.8 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -1.7 | -0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | claudin 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:170,418,868-170,454,733 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OSP; previously OTM |
| Gene groups (HGNC) | Claudins; MicroRNA protein coding host genes |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O75508](https://www.uniprot.org/uniprotkb/O75508) (Claudin-11):

> Plays a major role in tight junction-specific obliteration of the intercellular space, through calcium-independent cell-adhesion activity.

**Summary**, from NCBI Gene [5010](https://www.ncbi.nlm.nih.gov/gene/5010):

> This gene encodes a member of the claudin family. Claudins are integral membrane proteins and components of tight junction strands. Tight junction strands serve as a physical barrier to prevent solutes and water from passing freely through the paracellular space between epithelial or endothelial cell sheets, and also play critical roles in maintaining cell polarity and signal transductions. The protein encoded by this gene is a major component of central nervous system (CNS) myelin and plays an …

**Accessions** — [HGNC:8514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8514) · Entrez [5010](https://www.ncbi.nlm.nih.gov/gene/5010) · UniProt [O75508](https://www.uniprot.org/uniprotkb/O75508) · Ensembl [ENSG00000013297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013297)

## Data

Gene col 267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 267); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 267]; `tensor/DDL_lfc|DDL_z.npy` [267]; `embed/gene_vectors.npy` [267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 267 or target_col == 267). Every well: [[CLDN11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
