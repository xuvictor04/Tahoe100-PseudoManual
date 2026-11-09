---
symbol: "COLEC10"
type: "gene"
col: 11528
ensembl_id: "ENSG00000184374"
name: "collectin subfamily member 10"
location: "8q24.12"
module: 9
arm: "+"
pooled_cpm: 9.35
n_lines_expressing: 19
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 11
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# COLEC10

*collectin subfamily member 10* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +10.8, q 2e-24, up in 5 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.05 µM: 0.672× (z -4.3, q 0.007, down in 6 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.137×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.225×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.381×); [[Cobimetinib (drug)]] 5 µM in 1 line (J82 0.112×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.153×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02220]] (+0.64, fdr 7e-06), [[LINC01320]] (+0.63, fdr 1e-05), [[LINC02241]] (+0.63, fdr 1e-05); moves opposite to [[KATNAL1]] (-0.49, fdr 1e-04), [[CERCAM]] (-0.44, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[UCA1]] → it (grade C ⚠); 11 go from it, the strongest it → [[MUC20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +10.8 | 2e-24 | 5/15 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +8.7 | 7e-16 | 2/11 (A-172, HT-29) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +8.0 | 2e-13 | 1/5 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.5 | 9e-12 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.2 | 8e-08 | 3/14 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.8 | 7e-07 | 5/16 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.2 | 1e-05 | 7/16 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +5.1 | 2e-05 | 6/14 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 7e-05 | 2/15 (BT-474, LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.4 | 5e-04 | 2/15 (HT-29, HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.015 | 3/15 (A-172, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.6 | 0.017 | 2/14 (LOX-IMVI, CHP-212) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.020 | 4/15 (KATO III, Panc 03.27, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.26×** | +3.5 | 0.022 | 5/16 (RPMI-7951, KATO III, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.030 | 5/15 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.030 | 0/16 | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.033 | 2/14 (HT-29, A-172) | inconsistent across doses | low cells (technical?) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.044 | 1/14 (SNU-1) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.050 | 3/16 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.052 | 2/14 (Panc 03.27, HT-29) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.061 | 5/16 (KATO III, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11528.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.137×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.225×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.381×); [[Cobimetinib (drug)]] 5 µM in 1 line (J82 0.112×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.153×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.672×** | -4.3 | 0.007 | 6/16 (SNU-423, LOX-IMVI, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.677×** | -4.2 | 0.007 | 10/16 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.755× | -3.0 | 0.39 | 5/16 (SNU-423, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 211 | 2 (2 ⚠) | 5 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 5.94× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.137× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.5) |
| [[A-172 (line)]] | wt | 6.38 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +15.9) | — |
| [[COLO 205 (line)]] | alt | 9.71 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0492× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.153× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 131 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.76× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 45.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.112× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 3.84 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0421× (z -8.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A-427 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.996 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02220]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[LINC01320]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[LINC02241]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SAMD12-AS1]] | +0.61 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[LAMA1]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[INPP4B]] | +0.58 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[MSR1]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SNCAIP]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[DGKI]] | +0.56 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[MUC20]] | +0.55 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[NGF]] | +0.55 | +0.36 / +0.66 | both halves | 9e-05 |  |
| [[ADAMTS1]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL1]] | -0.49 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[CERCAM]] | -0.44 | -0.49 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UCA1]] | C | UCA1 activity raises COLEC10's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 1.16× lower at baseline in the lines without UCA1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ; co-absent with the target |
| [[SAMD12-AS1]] | C | SAMD12-AS1 activity raises COLEC10's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without SAMD12-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises COLEC10's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.66× lower at baseline in the lines without PSG4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[DGKI]] | C | DGKI activity raises COLEC10's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without DGKI | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[TMPRSS15]] | C | TMPRSS15 activity raises COLEC10's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 3.31× lower at baseline in the lines without TMPRSS15 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[SOX11]] | C | SOX11 activity raises COLEC10's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 1.30× lower at baseline in the lines without SOX11 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |
| [[RDUR]] | C | RDUR activity raises COLEC10's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without RDUR | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | COLEC10 activity raises MUC20's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 2.44× lower at baseline in the lines without COLEC10 | 0.002 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1 |
| [[PROM2]] | B | COLEC10 activity raises PROM2's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 1.60× lower at baseline in the lines without COLEC10 | 0.043 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1 |
| [[SAMD12]] | B | COLEC10 activity raises SAMD12's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 1.89× lower at baseline in the lines without COLEC10 | 0.050 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1 |
| [[SPINT1-AS1]] | B | COLEC10 activity raises SPINT1-AS1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 1.25× lower at baseline in the lines without COLEC10 | 0.096 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1 |
| [[SAMD12-AS1]] | C | COLEC10 activity raises SAMD12-AS1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 3.26× lower at baseline in the lines without COLEC10 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1; co-absent with the target |
| [[PDZK1IP1]] | C | COLEC10 activity raises PDZK1IP1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 1.78× lower at baseline in the lines without COLEC10 | 0.010 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1; co-absent with the target |
| [[UCA1]] | C | COLEC10 activity raises UCA1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 2.52× lower at baseline in the lines without COLEC10 | 0.022 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1; co-absent with the target |
| [[BCAS1]] | C | COLEC10 activity raises BCAS1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 2.02× lower at baseline in the lines without COLEC10 | 0.077 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1; co-absent with the target |
| [[AJAP1]] | C | COLEC10 activity raises AJAP1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 2.38× lower at baseline in the lines without COLEC10 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1; co-absent with the target |
| [[PRR15L]] | C | COLEC10 activity raises PRR15L's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 1.41× lower at baseline in the lines without COLEC10 | 0.094 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1; co-absent with the target |
| [[SYNPR-AS1]] | C | COLEC10 activity raises SYNPR-AS1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 1.43× lower at baseline in the lines without COLEC10 | 0.097 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.413). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, 27.2); signed map (37.8, 26.3). **Vector** length 41.4, 9.48% of its response variance represented; |z| ≥ 3 in 424 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +0.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | collectin subfamily member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:118,995,452-119,108,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CL-L1, CL-10 |
| Gene groups (HGNC) | Collectins; C-type lectin domain containing; Complement system activation components |
| Reactome | 5 pathways, smallest: Lectin pathway of complement activation; Creation of C4 and C2 activators; Initial triggering of complement |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Z7](https://www.uniprot.org/uniprotkb/Q9Y6Z7) (Collectin-10):

> Lectin that binds to various sugars: galactose > mannose = fucose > N-acetylglucosamine > N-acetylgalactosamine. Acts as a chemoattractant, probably involved in the regulation of cell migration.

**Summary**, from NCBI Gene [10584](https://www.ncbi.nlm.nih.gov/gene/10584):

> This gene encodes a member of the C-lectin family, proteins that possess collagen-like sequences and carbohydrate recognition domains. The other members of this family are secreted proteins and bind to carbohydrate antigens on microorganisms facilitating their recognition and removal. This gene product is a cytosolic protein, a characteristic that suggests that it may have different biological functions than other C-lectins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2220) · Entrez [10584](https://www.ncbi.nlm.nih.gov/gene/10584) · UniProt [Q9Y6Z7](https://www.uniprot.org/uniprotkb/Q9Y6Z7) · Ensembl [ENSG00000184374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184374)

## Data

Gene col 11528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11528); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11528]; `tensor/DDL_lfc|DDL_z.npy` [11528]; `embed/gene_vectors.npy` [11528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11528 or target_col == 11528). Every well: [[COLEC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COLEC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
