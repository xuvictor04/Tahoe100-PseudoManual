---
symbol: "OBSL1"
type: "gene"
col: 4472
ensembl_id: "ENSG00000124006"
name: "obscurin like cytoskeletal adaptor 1"
location: "2q35"
module: 46
arm: "+"
pooled_cpm: 9.19
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# OBSL1

*obscurin like cytoskeletal adaptor 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.37× (z +8.6, q 5e-15, up in 14 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bimiralisib (drug)]] 0.5 µM: 1.57× (z +3.3, q 0.097, up in 10 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.318× (z -16.7, q 0e+00, down in 33 of 39 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF362]] (+0.55, fdr 7e-05), [[LDB1]] (+0.54, fdr 5e-05), [[RAF1]] (+0.53, fdr 1e-04); moves opposite to [[EML6]] (-0.59, fdr 1e-05), [[PAQR5]] (-0.50, fdr 2e-04), [[BMP6]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NCAM1]] → it (grade B ⚠); 3 go from it, the strongest it → [[OTUD7A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.6 | 5e-15 | 14/19 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.8 | 4e-09 | 16/29 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.0 | 1e-04 | 12/21 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.097 | 10/37 (NCI-H2347, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.097 | 11/40 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.097 | 6/37 (HEC-1-A, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.2 | 0.097 | 3/42 (NCI-H23, AN3 CA, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.097 | 12/38 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.35× | +3.2 | 0.10 | 9/40 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.34× | +3.1 | 0.12 | 9/40 (HOP62, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | 1.74× | +3.0 | 0.14 | 5/36 (HOP62, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4472.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.318×** | -16.7 | 0e+00 | 33/39 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.270×** | -13.5 | 4e-39 | 36/41 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.287×** | -12.9 | 1e-35 | 35/41 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.312×** | -12.0 | 5e-31 | 32/41 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.334×** | -11.3 | 1e-27 | 29/34 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.376×** | -10.1 | 6e-22 | 31/41 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.437×** | -8.5 | 1e-15 | 29/41 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.445×** | -8.3 | 5e-15 | 30/40 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.452×** | -7.9 | 2e-13 | 29/40 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -7.5 | 4e-12 | 25/39 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.494×** | -7.3 | 2e-11 | 24/40 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.538×** | -6.4 | 8e-09 | 23/42 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.548×** | -6.2 | 3e-08 | 21/41 (SW480, SHP-77, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.576×** | -5.4 | 3e-06 | 22/39 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.376×** | -5.3 | 5e-06 | 17/37 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -5.2 | 6e-06 | 23/41 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.5 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0956× (z -19.4) |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.159× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -9.4) |
| [[SHP-77 (line)]] | alt | 36.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.9) |
| [[SNU-423 (line)]] | alt | 20.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.1) |
| [[HOP62 (line)]] | alt | 13.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.1) |
| [[H4 (line)]] | wt | 11.3 | 0 | 2 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0523× (z -9.8) |
| [[J82 (line)]] | alt | 6.67 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.37× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.7) |
| [[PANC-1 (line)]] | alt | 3.75 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 8.25 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -11.1) |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0859× (z -9.0) |
| [[A-172 (line)]] | wt | 17.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -9.3) |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.8) |
| [[C-33 A (line)]] | alt | 9.52 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0874× (z -9.2) |
| [[C32 (line)]] | wt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -8.7) |
| [[COLO 205 (line)]] | alt | 6.88 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0556× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 6.30 | 0 | 1 | — | [[Proglumide (drug)]] 0.5 µM 0.0708× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 7.67 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0873× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 5.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 4.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0636× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -9.2) |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.117× (z -9.4) |
| [[A-427 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 14 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | +0.55 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[LDB1]] | +0.54 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[RAF1]] | +0.53 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[SH2B1]] | +0.52 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[DHRS4]] | +0.51 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[PNISR-AS1]] | +0.51 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[FAM13C]] | +0.50 | +0.47 / +0.28 | both halves | 3e-04 |  |
| [[CASD1]] | +0.50 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[TMEM198B]] | +0.50 | +0.38 / +0.29 | both halves | 2e-04 |  |
| [[NEIL1]] | +0.49 | +0.31 / +0.40 | both halves | 2e-04 |  |
| [[SLCO6A1]] | +0.48 | +0.37 / +0.24 | both halves | 5e-04 |  |
| [[ATP1A1-AS1]] | +0.48 | +0.32 / +0.24 | both halves | 4e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML6]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PAQR5]] | -0.50 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[BMP6]] | -0.49 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[SLC35E4]] | -0.49 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[GALNT12]] | -0.49 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[SPIRE1]] | -0.49 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[DGKD]] | -0.46 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[SLC35F3]] | -0.46 | -0.41 / -0.34 | both halves | 1e-04 | same gene group |
| [[OTUD7A]] | -0.45 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ETHE1]] | -0.45 | -0.26 / -0.29 | both halves | 4e-04 |  |
| [[NEURL1]] | -0.44 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[NRIP3]] | -0.44 | -0.31 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCAM1]] | B | NCAM1 activity raises OBSL1's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 1.98× lower at baseline in the lines without NCAM1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11 |
| [[NPAS3]] | B | NPAS3 activity raises OBSL1's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without NPAS3 | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[NRIP3]] | B | NRIP3 activity raises OBSL1's level | lines that do not express NRIP3 (15) vs lines expressing it (35) | 1.74× lower at baseline in the lines without NRIP3 | 0.098 | ⚠ within organs, on part of the lines; also absent: SDK2, DTX3, MCTP1 |
| [[INHA]] | C | INHA activity raises OBSL1's level | lines that do not express INHA (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without INHA | 0.018 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OTUD7A]] | B | OBSL1 activity raises OTUD7A's level | lines that do not express OBSL1 (6) vs lines expressing it (44) | 2.36× lower at baseline in the lines without OBSL1 | 0.049 | ⚠ within organs, on part of the lines; also absent: PHC1, HECTD2, TPST1 |
| [[ZNF362]] | B | OBSL1 activity raises ZNF362's level | lines that do not express OBSL1 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without OBSL1 | 0.066 | ⚠ within organs, on part of the lines; also absent: PHC1, HECTD2, TPST1 |
| [[INHA]] | C | OBSL1 activity raises INHA's level | lines that do not express OBSL1 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without OBSL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PHC1, HECTD2, TPST1; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.7, 33.9); signed map (28.5, -22.4). **Vector** length 59.9, 9.89% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +3.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.0 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.0 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.2 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | -13.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -12.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | obscurin like cytoskeletal adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,550,728-219,571,859 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0657 |
| Gene groups (HGNC) | I-set domain containing; MicroRNA protein coding host genes; 3M complex subunits |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75147](https://www.uniprot.org/uniprotkb/O75147) (Obscurin-like protein 1):

> Core component of the 3M complex, a complex required to regulate microtubule dynamics and genome integrity. It is unclear how the 3M complex regulates microtubules, it could act by controlling the level of a microtubule stabilizer. Acts as a regulator of the Cul7-RING(FBXW8) ubiquitin-protein ligase, playing a critical role in the ubiquitin ligase pathway that regulates Golgi morphogenesis and dendrite patterning in brain. Required to localize CUL7 to the Golgi apparatus in neurons.

**Summary**, from NCBI Gene [23363](https://www.ncbi.nlm.nih.gov/gene/23363):

> Cytoskeletal adaptor proteins function in linking the internal cytoskeleton of cells to the cell membrane. This gene encodes a cytoskeletal adaptor protein, which is a member of the Unc-89/obscurin family. The protein contains multiple N- and C-terminal immunoglobulin (Ig)-like domains and a central fibronectin type 3 domain. Mutations in this gene cause 3M syndrome type 2. Alternatively spliced transcript variants encoding different isoforms have been found in this gene. [provided by RefSeq, …

**Accessions** — [HGNC:29092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29092) · Entrez [23363](https://www.ncbi.nlm.nih.gov/gene/23363) · UniProt [O75147](https://www.uniprot.org/uniprotkb/O75147) · Ensembl [ENSG00000124006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124006)

## Data

Gene col 4472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4472); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4472]; `tensor/DDL_lfc|DDL_z.npy` [4472]; `embed/gene_vectors.npy` [4472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4472 or target_col == 4472). Every well: [[OBSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OBSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
