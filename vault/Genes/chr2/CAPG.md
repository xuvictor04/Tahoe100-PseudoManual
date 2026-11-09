---
symbol: "CAPG"
type: "gene"
col: 487
ensembl_id: "ENSG00000042493"
name: "capping actin protein, gelsolin like"
location: "2p11.2"
module: 31
arm: "+"
pooled_cpm: 27.33
n_lines_expressing: 33
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 11
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CAPG

*capping actin protein, gelsolin like* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.45× (z +10.3, q 5e-22, up in 25 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.36× (z +5.1, q 6e-05, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.334× (z -17.8, q 0e+00, down in 30 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH1]] (+0.64, fdr 7e-06), [[NDFIP1]] (+0.58, fdr 1e-05), [[DENND2C]] (+0.57, fdr 3e-05); moves opposite to [[SAFB]] (-0.52, fdr 2e-04), [[EFCAB2]] (-0.50, fdr 5e-04), [[RBBP6]] (-0.49, fdr 5e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PROSER2]] → it (grade B ⚠); 11 go from it, the strongest it → [[VSIR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +10.3 | 5e-22 | 25/27 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +8.2 | 7e-14 | 21/22 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +6.7 | 3e-09 | 21/26 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.1 | 6e-05 | 17/31 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.5 | 8e-04 | 0/31 | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.005 | 22/31 (SW480, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.37×** | +3.6 | 0.027 | 14/29 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.082 | 16/31 (HT-29, SW480, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.082 | 13/30 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.11 | 12/30 (NCI-H460, H4, …) | two highest doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM |  | 1.30× | +3.0 | 0.13 | 11/31 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.334×** | -17.8 | 0e+00 | 30/31 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.461×** | -8.9 | 2e-16 | 26/31 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.581×** | -6.2 | 9e-08 | 23/31 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -6.1 | 1e-07 | 24/31 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.603×** | -5.8 | 7e-07 | 19/31 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.643×** | -4.9 | 1e-04 | 20/31 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -4.2 | 0.002 | 21/31 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.704×** | -4.0 | 0.004 | 15/31 (LoVo, SW48, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -3.9 | 0.006 | 19/31 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.712×** | -3.8 | 0.010 | 15/30 (PANC-1, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.012 | 17/31 (A-172, LoVo, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.546×** | -3.6 | 0.014 | 16/31 (A498, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.566×** | -3.4 | 0.029 | 18/31 (HOP62, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.750×** | -3.3 | 0.039 | 13/30 (LS 180, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.580×** | -3.3 | 0.043 | 13/27 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.092 | 15/31 (H4, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.746×** | -3.0 | 0.092 | 13/31 (LoVo, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 37.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -17.6) |
| [[A498 (line)]] | wt | 130 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.8) |
| [[H4 (line)]] | wt | 46.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 28.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.9) |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -15.5) |
| [[HT-29 (line)]] | alt | 39.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 48.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.6) |
| [[SW 900 (line)]] | alt | 28.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.0) |
| [[SW1417 (line)]] | alt | 32.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 84.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -18.7) |
| [[CFPAC-1 (line)]] | alt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -16.3) |
| [[COLO 205 (line)]] | alt | 9.38 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0370× (z -12.2) |
| [[HOP62 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.5) |
| [[HS-578T (line)]] | alt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.5) |
| [[J82 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.7) |
| [[LS 180 (line)]] | wt | 9.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0797× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.2) |
| [[PANC-1 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.8) |
| [[SW480 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.0) |
| [[A-172 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH1]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[NDFIP1]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[DENND2C]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[TWF2]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[JUP]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SPTLC2]] | +0.56 | +0.63 / +0.36 | both halves | 9e-05 |  |
| [[RRAS]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CRYBG2]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SLC66A3]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[AGPAT2]] | +0.56 | +0.65 / +0.37 | both halves | 9e-05 |  |
| [[CBLC]] | +0.55 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[MBOAT2]] | +0.55 | +0.58 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAFB]] | -0.52 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[EFCAB2]] | -0.50 | -0.53 / -0.23 | both halves | 5e-04 |  |
| [[RBBP6]] | -0.49 | -0.56 / -0.24 | both halves | 5e-04 |  |
| [[PHF8]] | -0.48 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ZNF785]] | -0.48 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[GALNT7-DT]] | -0.46 | -0.48 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROSER2]] | B | PROSER2 activity raises CAPG's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without PROSER2 | 0.022 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises CAPG's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.80× lower at baseline in the lines without SEMA3B | 0.033 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[LYPD3]] | B | LYPD3 activity raises CAPG's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.72× lower at baseline in the lines without LYPD3 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[SERPINB5]] | B | SERPINB5 activity raises CAPG's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without SERPINB5 | 0.067 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[KRT15]] | B | KRT15 activity raises CAPG's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without KRT15 | 0.075 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[KLC3]] | B | KLC3 activity raises CAPG's level | lines that do not express KLC3 (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without KLC3 | 0.097 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent |
| [[PRSS3]] | C | PRSS3 activity raises CAPG's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without PRSS3 | 0.074 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSIR]] | B | CAPG activity raises VSIR's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.54× lower at baseline in the lines without CAPG | 0.003 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[PROSER2]] | B | CAPG activity raises PROSER2's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without CAPG | 0.032 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[TMOD2]] | B | CAPG activity lowers TMOD2's level | lines that do not express CAPG (17) vs lines expressing it (33) | 1.60× higher at baseline in the lines without CAPG | 0.033 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[ANXA11]] | B | CAPG activity raises ANXA11's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.31× lower at baseline in the lines without CAPG | 0.052 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[AHNAK2]] | B | CAPG activity raises AHNAK2's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without CAPG | 0.068 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[ATP2B4]] | B | CAPG activity raises ATP2B4's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.12× lower at baseline in the lines without CAPG | 0.074 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[OXSR1]] | B | CAPG activity raises OXSR1's level | lines that do not express CAPG (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without CAPG | 0.077 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[KRT15]] | B | CAPG activity raises KRT15's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.48× lower at baseline in the lines without CAPG | 0.090 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[RAB11FIP1]] | B | CAPG activity raises RAB11FIP1's level | lines that do not express CAPG (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without CAPG | 0.092 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[EIF4E3]] | B | CAPG activity strengthens EIF4E3's drug response | lines that do not express CAPG (14) vs lines expressing it (28) | the lines without CAPG respond 0.56× as strongly (z diff +1.52); strongest at Homoharringtonine 5 µM: 0.41x vs 0.22x (z diff +3.1) | 0.094 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2; target measured in part of the lines; artifact flags |
| [[NGEF]] | C | CAPG activity raises NGEF's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.64× lower at baseline in the lines without CAPG | 0.037 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, 56.2); signed map (-2.3, 39.0). **Vector** length 72.9, 21.2% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.2 | -17.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | capping actin protein, gelsolin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,394,753-85,418,432 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCP; previously AFCP |
| Gene groups (HGNC) | Gelsolin/villins |
| Hallmark sets | ALLOGRAFT_REJECTION, IL2_STAT5_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [P40121](https://www.uniprot.org/uniprotkb/P40121) (Macrophage-capping protein):

> Calcium-sensitive protein which reversibly blocks the barbed ends of actin filaments but does not sever preformed actin filaments. May play an important role in macrophage function. May play a role in regulating cytoplasmic and/or nuclear structures through potential interactions with actin. May bind DNA.

**Summary**, from NCBI Gene [822](https://www.ncbi.nlm.nih.gov/gene/822):

> This gene encodes a member of the gelsolin/villin family of actin-regulatory proteins. The encoded protein reversibly blocks the barbed ends of F-actin filaments in a Ca2+ and phosphoinositide-regulated manner, but does not sever preformed actin filaments. By capping the barbed ends of actin filaments, the encoded protein contributes to the control of actin-based motility in non-muscle cells. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Jan …

**Accessions** — [HGNC:1474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1474) · Entrez [822](https://www.ncbi.nlm.nih.gov/gene/822) · UniProt [P40121](https://www.uniprot.org/uniprotkb/P40121) · Ensembl [ENSG00000042493](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042493)

## Data

Gene col 487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 487); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 487]; `tensor/DDL_lfc|DDL_z.npy` [487]; `embed/gene_vectors.npy` [487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 487 or target_col == 487). Every well: [[CAPG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
