---
symbol: "STON2"
type: "gene"
col: 6368
ensembl_id: "ENSG00000140022"
name: "stonin 2"
location: "14q31.1"
module: 66
arm: "+"
pooled_cpm: 18.5
n_lines_expressing: 31
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 32
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# STON2

*stonin 2* — 14q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.19× (z +27.5, q 0e+00, up in 27 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (C32 0.0871×, NCI-H1573 0.330×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 0.282×, COLO 205 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.340×, NCI-H1792 0.405×; ⚠ cell-cycle shift, explains ~61% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.308×); [[Trametinib (drug)]] 0.5 µM in 1 line (SW480 0.435×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (SW480 0.363×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIAM1]] (+0.55, fdr 3e-05), [[ABLIM1]] (+0.52, fdr 2e-05), [[YWHAG]] (+0.51, fdr 5e-05); moves opposite to [[GLE1]] (-0.48, fdr 8e-05), [[PEX11B]] (-0.46, fdr 8e-05), [[PRRG2]] (-0.46, fdr 2e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[JPH1]] → it (grade B ⚠); 32 go from it, the strongest it → [[ABLIM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.19×** | +27.5 | 0e+00 | 27/28 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.52×** | +25.8 | 0e+00 | 27/28 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.32×** | +25.6 | 0e+00 | 26/29 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **4.24×** | +21.8 | 0e+00 | 26/28 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.12×** | +17.2 | 0e+00 | 25/28 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.36×** | +12.9 | 2e-36 | 20/28 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +11.2 | 3e-27 | 18/28 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.44×** | +9.7 | 1e-20 | 22/29 (NCI-H460, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +9.6 | 4e-20 | 21/28 (SW 900, LoVo, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +8.7 | 3e-16 | 20/28 (LoVo, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.80×** | +8.5 | 1e-15 | 9/21 (A498, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.71×** | +8.1 | 4e-14 | 18/29 (J82, A549, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +7.3 | 1e-11 | 17/28 (LoVo, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +7.3 | 1e-11 | 16/28 (HEC-1-A, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.60×** | +7.1 | 4e-11 | 13/26 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.6 | 1e-09 | 11/29 (A549, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +6.2 | 2e-08 | 13/29 (SHP-77, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6368.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (C32 0.0871×, NCI-H1573 0.330×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 0.282×, COLO 205 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.340×, NCI-H1792 0.405×; ⚠ cell-cycle shift, explains ~61% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.308×); [[Trametinib (drug)]] 0.5 µM in 1 line (SW480 0.435×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (SW480 0.363×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.800× | -3.4 | 0.42 | 14/28 (HepG2/C3A, CFPAC-1, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.868× | -3.0 | 0.64 | 7/29 (A498, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 27.9 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 4.42× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 8.02 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 6.95× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +9.6) | — |
| [[LoVo (line)]] | wt | 30.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 8.43 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.68× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 36.3 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.76× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 15.8 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.84× (z +12.4) | — |
| [[SW480 (line)]] | alt | 60.8 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.435× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.32× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 7.87 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 7.72× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 27.0 | 3 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 5.85× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.64× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 47.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 13.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.73× (z +10.4) | — |
| [[C32 (line)]] | wt | 17.3 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.80× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.0871× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 57.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.91× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[NCI-H1792 (line)]] | alt | 47.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.1) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A549 (line)]] | wt | 7.01 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.11× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 36.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +8.7) | — |
| [[KATO III (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -10.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[RPMI-7951 (line)]] | alt | 9.81 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0764× (z -9.1) |
| [[SHP-77 (line)]] | alt | 41.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.4) | — |
| [[A-172 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIAM1]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[ABLIM1]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[YWHAG]] | +0.51 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[PRRG1]] | +0.51 | +0.32 / +0.56 | both halves | 1e-04 |  |
| [[ULBP3]] | +0.50 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[ANXA2]] | +0.49 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[SERPINB5]] | +0.48 | +0.36 / +0.46 | both halves | 9e-05 |  |
| [[ENDOD1]] | +0.48 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[PCNX2]] | +0.48 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[CRYBG2]] | +0.47 | +0.31 / +0.47 | both halves | 2e-04 |  |
| [[FABP5]] | +0.47 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[CRISPLD2]] | +0.46 | +0.35 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | -0.48 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[PEX11B]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 | pathway: Protein localization |
| [[PRRG2]] | -0.46 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[DICER1-AS1]] | -0.44 | -0.17 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[MLYCD]] | -0.44 | -0.24 / -0.50 | both halves | 4e-04 | pathway: Protein localization |
| [[GID8]] | -0.44 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[RSRP1]] | -0.43 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[ZNF248]] | -0.43 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[PDSS2]] | -0.43 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[PIGZ]] | -0.43 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[ATP6V0D1-DT]] | -0.43 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[JTB]] | -0.42 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[POLR1HASP]] | -0.42 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH1]] | B | JPH1 activity raises STON2's level | lines that do not express JPH1 (15) vs lines expressing it (35) | 3.00× lower at baseline in the lines without JPH1 | 0.009 | ⚠ within organs, on part of the lines; also absent: UGT8, CADPS2, PTPRE |
| [[KITLG]] | B | KITLG activity raises STON2's level | lines that do not express KITLG (10) vs lines expressing it (40) | 3.59× lower at baseline in the lines without KITLG | 0.012 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[TRIM15]] | B | TRIM15 activity raises STON2's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.86× lower at baseline in the lines without TRIM15 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[EHF]] | B | EHF activity raises STON2's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without EHF | 0.038 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[ABLIM1]] | B | ABLIM1 activity raises STON2's level | lines that do not express ABLIM1 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without ABLIM1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EVPL, NUP62CL, CCDC68 |
| [[LCK]] | B | LCK activity raises STON2's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without LCK | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[AREG]] | B | AREG activity raises STON2's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without AREG | 0.057 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[SERPINB5]] | B | SERPINB5 activity raises STON2's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without SERPINB5 | 0.058 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[TOP2A]] | B | TOP2A activity lowers STON2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DSG2]] | B | DSG2 activity raises STON2's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 2.73× lower at baseline in the lines without DSG2 | 0.093 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[CRYBG2]] | C | CRYBG2 activity raises STON2's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without CRYBG2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises STON2's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.34× lower at baseline in the lines without CYP4F11 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 30, C 2. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABLIM1]] | B | STON2 activity raises ABLIM1's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without STON2 | 0.003 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[TAF1B]] | B | STON2 activity lowers TAF1B's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.52× higher at baseline in the lines without STON2 | 0.004 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[GJA3]] | B | STON2 activity lowers GJA3's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.79× higher at baseline in the lines without STON2 | 0.004 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[C15orf39]] | B | STON2 activity raises C15orf39's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without STON2 | 0.009 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[PRRG1]] | B | STON2 activity raises PRRG1's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without STON2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | STON2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express STON2 (19) vs lines expressing it (29) | the lines without STON2: 0.81× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[EHF]] | B | STON2 activity raises EHF's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.82× lower at baseline in the lines without STON2 | 0.028 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[MISP]] | B | STON2 activity raises MISP's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.64× lower at baseline in the lines without STON2 | 0.031 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[GLO1]] | B | STON2 activity lowers GLO1's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.50× higher at baseline in the lines without STON2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[ZNF251]] | B | STON2 activity lowers ZNF251's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.27× higher at baseline in the lines without STON2 | 0.043 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[TRIM15]] | B | STON2 activity raises TRIM15's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.05× lower at baseline in the lines without STON2 | 0.046 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| cells under [[NVP-BHG712 (drug)]] 0.05 µM | B | STON2 activity lowers the cells' numbers under NVP-BHG712 0.05 µM (makes them more sensitive) | lines that do not express STON2 (19) vs lines expressing it (29) | the lines without STON2: 1.15× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.295). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.3, 45.2); signed map (-19.7, 38.4). **Vector** length 87.9, 22.2% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +25.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +12.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.7 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -3.2 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | stonin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.1 — chr14:81,260,652-81,436,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STNB2, STN2 |
| Reactome | 6 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Cotranslational targeting of proteins to the endoplasmic reticulum |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXE9](https://www.uniprot.org/uniprotkb/Q8WXE9) (Stonin-2):

> Adapter protein involved in endocytic machinery. Involved in the synaptic vesicle recycling. May facilitate clathrin-coated vesicle uncoating.

**Summary**, from NCBI Gene [85439](https://www.ncbi.nlm.nih.gov/gene/85439):

> This gene encodes a protein which is a membrane protein involved in regulating endocytotic complexes. The protein product is described as one of the clathrin-associated sorting proteins, adaptor molecules which ensure specific proteins are internalized. The encoded protein has also been shown to participate in synaptic vesicle recycling through interaction with synaptotagmin 1 required for neurotransmission. Multiple transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:30652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30652) · Entrez [85439](https://www.ncbi.nlm.nih.gov/gene/85439) · UniProt [Q8WXE9](https://www.uniprot.org/uniprotkb/Q8WXE9) · Ensembl [ENSG00000140022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140022)

## Data

Gene col 6368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6368); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6368]; `tensor/DDL_lfc|DDL_z.npy` [6368]; `embed/gene_vectors.npy` [6368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6368 or target_col == 6368). Every well: [[STON2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STON2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
