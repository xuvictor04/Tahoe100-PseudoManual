---
symbol: "SYT14"
type: "gene"
col: 6750
ensembl_id: "ENSG00000143469"
name: "synaptotagmin 14"
location: "1q32.2"
module: 121
arm: "+"
pooled_cpm: 13.79
n_lines_expressing: 21
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 29
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# SYT14

*synaptotagmin 14* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.65× (z +24.5, q 0e+00, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.669× (z -5.4, q 3e-05, down in 8 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Panc 03.27 0.254×, NCI-H23 0.264×, C-33 A 0.446×); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.162×, A-172 0.205×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0486×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.128×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPEB1]] (+0.65, fdr 7e-06), [[ITGBL1]] (+0.61, fdr 1e-05), [[LINC02930]] (+0.59, fdr 1e-05); moves opposite to [[SPICE1]] (-0.60, fdr 1e-05), [[WHAMMP1]] (-0.54, fdr 4e-05), [[PDXP]] (-0.53, fdr 2e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITGBL1]] → it (grade C ⚠); 4 go from it, the strongest it → [[SNX9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.65×** | +24.5 | 0e+00 | 16/19 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +15.3 | 0e+00 | 3/19 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +15.2 | 0e+00 | 4/16 (NCI-H2347, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +14.9 | 0e+00 | 4/14 (NCI-H2347, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +10.3 | 5e-23 | 16/19 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +9.5 | 2e-19 | 9/19 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +9.3 | 7e-19 | 13/19 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +7.0 | 1e-10 | 4/18 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +6.9 | 3e-10 | 4/19 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +6.4 | 8e-09 | 9/19 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +5.6 | 8e-07 | 12/19 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.6 | 1e-06 | 13/19 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.5 | 1e-06 | 5/19 (C32, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 2e-06 | 10/19 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +5.4 | 2e-06 | 11/19 (SW 900, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +5.4 | 2e-06 | 7/19 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +5.2 | 8e-06 | 14/19 (SW 900, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +4.7 | 8e-05 | 5/19 (CHP-212, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6750.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Panc 03.27 0.254×, NCI-H23 0.264×, C-33 A 0.446×); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.162×, A-172 0.205×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0486×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.128×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.669×** | -5.4 | 3e-05 | 8/19 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -4.3 | 0.004 | 11/19 (NCI-H23, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.786× | -3.3 | 0.19 | 0/19 | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.790× | -3.2 | 0.19 | 6/19 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.793× | -3.1 | 0.19 | 8/19 (Panc 03.27, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0486× (z -15.6) |
| [[C-33 A (line)]] | alt | 85.7 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -8.6) |
| [[A-172 (line)]] | wt | 47.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 71.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -13.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 39.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +11.7) | — |
| [[H4 (line)]] | wt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 6.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 28.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 7.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +9.8) | — |
| [[A498 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPEB1]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ITGBL1]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LINC02930]] | +0.59 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CD22]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MSR1]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[KIAA0408]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FMN2]] | +0.57 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[CNTN6]] | +0.57 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[NFASC]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ZNF365]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PHACTR1]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PIEZO2]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPICE1]] | -0.60 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[WHAMMP1]] | -0.54 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PDXP]] | -0.53 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[MGAT1]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[IKBIP]] | -0.52 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[CRLS1]] | -0.52 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[KIAA2013]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[APAF1]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[USP37]] | -0.51 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MLEC]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PDE7A]] | -0.50 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[NSFP1]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGBL1]] | C | ITGBL1 activity raises SYT14's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 3.83× lower at baseline in the lines without ITGBL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises SYT14's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 3.45× lower at baseline in the lines without ADAMTS12 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX9]] | B | SYT14 activity lowers SNX9's level | lines that do not express SYT14 (29) vs lines expressing it (21) | 1.05× higher at baseline in the lines without SYT14 | 0.091 | ⚠ within organs, on part of the lines; also absent: ITGA4, MMP2, PHACTR1 |
| [[LINC02241]] | C | SYT14 activity raises LINC02241's level | lines that do not express SYT14 (29) vs lines expressing it (21) | 3.15× lower at baseline in the lines without SYT14 | 0.035 | ⚠ within organs, on part of the lines; also absent: ITGA4, MMP2, PHACTR1; co-absent with the target |
| [[ADAMTS12]] | C | SYT14 activity raises ADAMTS12's level | lines that do not express SYT14 (29) vs lines expressing it (21) | 3.23× lower at baseline in the lines without SYT14 | 0.051 | ⚠ within organs, on part of the lines; also absent: ITGA4, MMP2, PHACTR1; co-absent with the target |
| [[ITGBL1]] | C | SYT14 activity raises ITGBL1's level | lines that do not express SYT14 (29) vs lines expressing it (21) | 3.05× lower at baseline in the lines without SYT14 | 0.094 | ⚠ within organs, on part of the lines; also absent: ITGA4, MMP2, PHACTR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.2, 25.5); signed map (40.3, 25.9). **Vector** length 60.6, 17.3% of its response variance represented; |z| ≥ 3 in 484 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +24.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +4.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -1.8 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:209,900,923-210,171,389 (+) |
| Ensembl biotype | protein_coding |
| Also known as | sytXIV, FLJ34198 |
| Gene groups (HGNC) | Synaptotagmins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB59](https://www.uniprot.org/uniprotkb/Q8NB59) (Synaptotagmin-14):

> May be involved in the trafficking and exocytosis of secretory vesicles in non-neuronal tissues. Is Ca(2+)-independent.

**Summary**, from NCBI Gene [255928](https://www.ncbi.nlm.nih.gov/gene/255928):

> This gene is a member of the synaptotagmin gene family and encodes a protein similar to other family members that mediate membrane trafficking in synaptic transmission. The encoded protein is a calcium-independent synaptotagmin. Mutations in this gene are a cause of autosomal recessive spinocerebellar ataxia-11 (SCAR11), and a t(1;3) translocation of this gene has been associated with neurodevelopmental abnormalities. Alternatively spliced transcript variants encoding multiple isoforms have …

**Accessions** — [HGNC:23143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23143) · Entrez [255928](https://www.ncbi.nlm.nih.gov/gene/255928) · UniProt [Q8NB59](https://www.uniprot.org/uniprotkb/Q8NB59) · Ensembl [ENSG00000143469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143469)

## Data

Gene col 6750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6750); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6750]; `tensor/DDL_lfc|DDL_z.npy` [6750]; `embed/gene_vectors.npy` [6750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6750 or target_col == 6750). Every well: [[SYT14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
