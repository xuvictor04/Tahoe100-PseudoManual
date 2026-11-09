---
symbol: "EPPK1"
type: "gene"
col: 15328
ensembl_id: "ENSG00000261150"
name: "epiplakin 1"
location: "8q24.3"
module: 15
arm: "-"
pooled_cpm: 8.65
n_lines_expressing: 25
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 22
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# EPPK1

*epiplakin 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.34× (z +18.8, q 0e+00, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.560× (z -5.0, q 3e-04, down in 17 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.261×, HT-29 0.287×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.0524×); [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0455×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0764×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPL]] (+0.69, fdr 7e-06), [[ADAMTSL5]] (+0.62, fdr 5e-05), [[PLEKHO2]] (+0.59, fdr 2e-05); moves opposite to [[PDSS2]] (-0.57, fdr 1e-05), [[MFSD8]] (-0.56, fdr 2e-05), [[TIAL1]] (-0.54, fdr 2e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CDC42BPG]] → it (grade C ⚠); 22 go from it, the strongest it → [[FAM83H]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.34×** | +18.8 | 0e+00 | 16/23 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.66×** | +13.9 | 2e-41 | 21/23 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.84×** | +12.2 | 9e-32 | 20/23 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +10.3 | 1e-22 | 8/17 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +9.2 | 3e-18 | 6/13 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +8.8 | 1e-16 | 21/23 (SW480, SW1417, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.57×** | +8.5 | 1e-15 | 12/22 (SW1417, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.53×** | +8.4 | 3e-15 | 16/23 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +6.7 | 1e-09 | 7/21 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +6.6 | 2e-09 | 2/14 (J82, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +5.9 | 2e-07 | 13/23 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +4.8 | 6e-05 | 15/23 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +4.7 | 1e-04 | 10/23 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +4.0 | 0.003 | 12/23 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.49×** | +3.6 | 0.011 | 3/23 (HCT15, SW480, …) | inconsistent across doses | position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.094 | 4/22 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15328.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.261×, HT-29 0.287×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.0524×); [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0455×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0764×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.560×** | -5.0 | 3e-04 | 17/23 (KATO III, BT-474, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.883× | -3.7 | 0.061 | 3/23 (J82, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.694× | -3.3 | 0.20 | 11/23 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.90 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.99× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 9.31 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +9.5) | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0764× (z -11.4) |
| [[J82 (line)]] | alt | 5.65 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.106× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 47.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 5.55 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +10.2) | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0455× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 9.73 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0524× (z -13.3) |
| [[BT-474 (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 5.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 28.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.77× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 4.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 2.60 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 13.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.89× (z +9.1) | — |
| [[A-172 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPL]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 | same gene group; STRING 692 |
| [[ADAMTSL5]] | +0.62 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[PLEKHO2]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ARHGDIA]] | +0.59 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[CSRNP1]] | +0.58 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[C15orf39]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[FAAP100]] | +0.58 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[JUNB]] | +0.57 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[TMEM185B]] | +0.57 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[TRNP1]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TPPP]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MAPK11]] | +0.56 | +0.29 / +0.57 | both halves | 2e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDSS2]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[MFSD8]] | -0.56 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TIAL1]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TRAPPC13]] | -0.54 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ZNF248]] | -0.53 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[ORMDL1]] | -0.53 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[TCEANC2]] | -0.53 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[GLUD1P3]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ISY1]] | -0.52 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[PUS10]] | -0.51 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[PMS2P4-1]] | -0.51 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[NUP133]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42BPG]] | C | CDC42BPG activity raises EPPK1's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 4.43× lower at baseline in the lines without CDC42BPG | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[SLC52A3]] | C | SLC52A3 activity raises EPPK1's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 4.38× lower at baseline in the lines without SLC52A3 | 0.002 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7; co-absent with the target |
| [[SH2D3A]] | C | SH2D3A activity raises EPPK1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.84× lower at baseline in the lines without SH2D3A | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; co-absent with the target |
| [[PPL]] | C | PPL activity raises EPPK1's level | lines that do not express PPL (19) vs lines expressing it (31) | 3.80× lower at baseline in the lines without PPL | 0.014 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6; co-absent with the target |
| [[TRIM15]] | C | TRIM15 activity raises EPPK1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 3.52× lower at baseline in the lines without TRIM15 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680; co-absent with the target |
| [[KCNK5]] | C | KCNK5 activity raises EPPK1's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 3.15× lower at baseline in the lines without KCNK5 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2; co-absent with the target |
| [[NRARP]] | C | NRARP activity raises EPPK1's level | lines that do not express NRARP (14) vs lines expressing it (36) | 3.60× lower at baseline in the lines without NRARP | 0.045 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A; co-absent with the target |
| [[MISP]] | C | MISP activity raises EPPK1's level | lines that do not express MISP (23) vs lines expressing it (27) | 3.27× lower at baseline in the lines without MISP | 0.048 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B; co-absent with the target |
| [[MUC5AC]] | C | MUC5AC activity raises EPPK1's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.91× lower at baseline in the lines without MUC5AC | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |
| [[AREG]] | C | AREG activity raises EPPK1's level | lines that do not express AREG (26) vs lines expressing it (24) | 3.24× lower at baseline in the lines without AREG | 0.091 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 16, C 6. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83H]] | B | EPPK1 activity raises FAM83H's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 3.34× lower at baseline in the lines without EPPK1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[ALAS1]] | B | EPPK1 activity raises ALAS1's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without EPPK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[NAPRT]] | B | EPPK1 activity raises NAPRT's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without EPPK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[TRAF4]] | B | EPPK1 activity raises TRAF4's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.43× lower at baseline in the lines without EPPK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[AQP3]] | B | EPPK1 activity raises AQP3's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 2.17× lower at baseline in the lines without EPPK1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[MYORG]] | B | EPPK1 activity raises MYORG's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.49× lower at baseline in the lines without EPPK1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[LAMA5]] | B | EPPK1 activity raises LAMA5's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without EPPK1 | 0.044 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[CPLX1]] | B | EPPK1 activity raises CPLX1's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.69× lower at baseline in the lines without EPPK1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[ABHD11]] | B | EPPK1 activity raises ABHD11's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.96× lower at baseline in the lines without EPPK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| cells under [[Pitavastatin (Calcium) (drug)]] 5 µM | B | EPPK1 activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express EPPK1 (25) vs lines expressing it (23) | the lines without EPPK1: 0.80× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[TRNP1]] | B | EPPK1 activity raises TRNP1's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.90× lower at baseline in the lines without EPPK1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[MYO15B]] | B | EPPK1 activity raises MYO15B's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without EPPK1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.474). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.6, 26.4); signed map (-7.8, 29.3). **Vector** length 61.2, 14.7% of its response variance represented; |z| ≥ 3 in 638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +18.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.0 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | epiplakin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,857,324-143,878,467 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPIPL1 |
| Gene groups (HGNC) | Plakins |
| Matched by | ensembl_id |

**Function**, from UniProt [P58107](https://www.uniprot.org/uniprotkb/P58107) (Epiplakin):

> Cytoskeletal linker protein that connects to intermediate filaments and controls their reorganization in response to stress. In response to mechanical stress like wound healing, is associated with the machinery for cellular motility by slowing down keratinocyte migration and proliferation and accelerating keratin bundling in proliferating keratinocytes thus contributing to tissue architecture. However in wound healing in corneal epithelium also positively regulates cell differentiation and …

**Summary**, from NCBI Gene [83481](https://www.ncbi.nlm.nih.gov/gene/83481):

> The protein encoded by this gene belongs to the plakin family of proteins, which play a role in the organization of cytoskeletal architecture. This family member is composed of several highly homologous plakin repeats. It may function to maintain the integrity of keratin intermediate filament networks in epithelial cells. Studies of the orthologous mouse protein suggest that it accelerates keratinocyte migration during wound healing. [provided by RefSeq, Oct 2013]

**Accessions** — [HGNC:15577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15577) · Entrez [83481](https://www.ncbi.nlm.nih.gov/gene/83481) · UniProt [P58107](https://www.uniprot.org/uniprotkb/P58107) · Ensembl [ENSG00000261150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261150)

## Data

Gene col 15328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15328); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15328]; `tensor/DDL_lfc|DDL_z.npy` [15328]; `embed/gene_vectors.npy` [15328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15328 or target_col == 15328). Every well: [[EPPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
