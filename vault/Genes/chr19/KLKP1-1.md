---
symbol: "KLKP1-1"
type: "gene"
col: 16525
ensembl_id: "ENSG00000290915"
name: ""
location: ""
module: 21
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 39
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# KLKP1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 102× (z +22.6, q 0e+00, up in 13 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 9.63× (z +15.6, q 0e+00, up in 23 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Diphenhydramine (drug)]] 0.5 µM: 0.474× (z -3.7, q 0.083, down in 7 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNG2]] (+0.74, fdr 7e-06), [[ABCC11]] (+0.60, fdr 7e-06), [[GDPD4]] (+0.59, fdr 1e-05); moves opposite to [[NPAT]] (-0.49, fdr 6e-05), [[YWHAB]] (-0.46, fdr 4e-05), [[CASP8AP2]] (-0.46, fdr 3e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NRP1]] → it (grade B ⚠); 11 go from it, the strongest it → [[PCSK7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **102×** | +22.6 | 0e+00 | 13/13 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **120×** | +22.5 | 0e+00 | 4/4 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **71.2×** | +19.2 | 0e+00 | 7/7 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **9.63×** | +15.6 | 0e+00 | 23/24 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **28.5×** | +8.5 | 1e-15 | 5/5 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.14×** | +8.0 | 1e-13 | 17/21 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **5.31×** | +7.8 | 4e-13 | 8/11 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.55×** | +7.4 | 1e-11 | 20/31 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.56×** | +6.5 | 6e-09 | 16/31 (NCI-H2347, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.93×** | +6.4 | 8e-09 | 19/29 (J82, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.24×** | +5.7 | 5e-07 | 16/30 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.30×** | +5.7 | 5e-07 | 17/31 (KATO III, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +5.6 | 1e-06 | 8/19 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **4.36×** | +5.1 | 1e-05 | 16/29 (HEC-1-A, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.81×** | +5.0 | 2e-05 | 14/27 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.70×** | +4.6 | 2e-04 | 9/26 (HEC-1-A, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.94×** | +4.6 | 2e-04 | 10/30 (CFPAC-1, SW1417, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.3 | 6e-04 | 9/24 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +3.7 | 0.006 | 5/25 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +3.5 | 0.013 | 9/32 (SW 900, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.89×** | +3.1 | 0.044 | 8/20 (SNU-423, CFPAC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.474×** | -3.7 | 0.083 | 7/33 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.477×** | -3.6 | 0.083 | 11/34 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.497×** | -3.4 | 0.095 | 7/32 (Panc 03.27, J82, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.499×** | -3.4 | 0.095 | 7/34 (LS 180, A-172, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.524× | -3.2 | 0.15 | 7/30 (A498, HOP62, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.532× | -3.1 | 0.15 | 11/28 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.534× | -3.1 | 0.15 | 6/32 (AsPC-1, COLO 205, …) | inconsistent across doses | position effect removed |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.534× | -3.1 | 0.15 | 8/30 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 6.32 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 90.3× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 29.7× (z +8.7) | — |
| [[J82 (line)]] | alt | 4.05 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 5.10 | 2 | 0 | [[Selinexor (drug)]] 5 µM 10.3× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 4.43 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 128× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 20.2× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 31.7× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 1.15 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 97.6× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 8.76 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 29.5× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 1.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 169× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 1.48 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 210× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 1.78 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 109× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.895 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.706 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.765 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.855 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNG2]] | +0.74 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[ABCC11]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[GDPD4]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[KIAA2012]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SLC16A13]] | +0.57 | +0.40 / +0.70 | both halves | 5e-05 |  |
| [[GALNT17]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CDA]] | +0.56 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[LINC00592]] | +0.55 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[LINC02603]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PDE8B]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[BTG1-DT]] | +0.54 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[FEZ1]] | +0.53 | +0.37 / +0.51 | both halves | 7e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPAT]] | -0.49 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[YWHAB]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[CASP8AP2]] | -0.46 | -0.38 / -0.29 | both halves | 3e-04 |  |
| [[PCSK7]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[SNRPB]] | -0.45 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ADAM10]] | -0.45 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[SRGAP2]] | -0.44 | -0.47 / -0.24 | both halves | 4e-04 |  |
| [[FEN1]] | -0.43 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[FANCM]] | -0.43 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[SRGAP2B]] | -0.43 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[TBC1D10B]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP1]] | B | NRP1 activity raises KLKP1-1's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without NRP1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[FUT2]] | B | FUT2 activity raises KLKP1-1's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without FUT2 | 0.041 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[FBLN2]] | B | FBLN2 activity raises KLKP1-1's level | lines that do not express FBLN2 (25) vs lines expressing it (25) | 1.78× lower at baseline in the lines without FBLN2 | 0.053 | ⚠ within organs, on part of the lines; also absent: MME, LINC01411, TLL1 |
| [[CDA]] | B | CDA activity raises KLKP1-1's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.73× lower at baseline in the lines without CDA | 0.071 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[CACNG2]] | B | CACNG2 activity raises KLKP1-1's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without CACNG2 | 0.092 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK7]] | B | KLKP1-1 activity raises PCSK7's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.22× lower at baseline in the lines without KLKP1-1 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[RND1]] | B | KLKP1-1 activity raises RND1's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.97× lower at baseline in the lines without KLKP1-1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[CACNG2]] | B | KLKP1-1 activity raises CACNG2's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without KLKP1-1 | 0.032 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[PALM]] | B | KLKP1-1 activity lowers PALM's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 2.08× higher at baseline in the lines without KLKP1-1 | 0.044 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[ZNF354A]] | B | KLKP1-1 activity lowers ZNF354A's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.45× higher at baseline in the lines without KLKP1-1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[LINC02934]] | B | KLKP1-1 activity raises LINC02934's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without KLKP1-1 | 0.050 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[NRP1]] | B | KLKP1-1 activity raises NRP1's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 4.25× lower at baseline in the lines without KLKP1-1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| cells under [[Belumosudil (drug)]] 5 µM | B | KLKP1-1 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express KLKP1-1 (11) vs lines expressing it (37) | the lines without KLKP1-1: 0.52× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[DLGAP1-AS1]] | B | KLKP1-1 activity lowers DLGAP1-AS1's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.90× higher at baseline in the lines without KLKP1-1 | 0.074 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[GOLGA7B-DT]] | B | KLKP1-1 activity raises GOLGA7B-DT's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without KLKP1-1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[RPLP0P2]] | B | KLKP1-1 activity raises RPLP0P2's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without KLKP1-1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.402). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, 31.9); signed map (37.7, 7.0). **Vector** length 53.2, 11.1% of its response variance represented; |z| ≥ 3 in 608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +19.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +22.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +22.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +15.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +5.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

> [!warning] No registry record
> KLKP1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16525); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16525]; `tensor/DDL_lfc|DDL_z.npy` [16525]; `embed/gene_vectors.npy` [16525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16525 or target_col == 16525). Every well: [[KLKP1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLKP1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
