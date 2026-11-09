---
symbol: "TRIM56"
type: "gene"
col: 9864
ensembl_id: "ENSG00000169871"
name: "tripartite motif containing 56"
location: "7q22.1"
module: 32
arm: "+"
pooled_cpm: 158.08
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM56

*tripartite motif containing 56* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.52× (z +5.9, q 2e-06, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.448× (z -15.9, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAMP1-AS1]] (+0.70, fdr 7e-06), [[SP110]] (+0.69, fdr 7e-06), [[PARP14]] (+0.68, fdr 7e-06); moves opposite to [[AGO1]] (-0.58, fdr 1e-05), [[NDRG3]] (-0.58, fdr 2e-05), [[PIK3R2]] (-0.57, fdr 5e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GBP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.9 | 2e-06 | 33/48 (HEC-1-A, SW 900, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +4.5 | 0.002 | 28/49 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.020 | 30/48 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.035 | 28/47 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.035 | 23/48 (HS-578T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.035 | 21/48 (A498, AsPC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.086 | 26/48 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.093 | 21/48 (Hs 766T, A-172, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.093 | 27/49 (NCI-H2030, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.11 | 24/48 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | 1.26× | +3.1 | 0.11 | 24/49 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.448×** | -15.9 | 0e+00 | 40/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.322×** | -15.9 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.386×** | -13.3 | 3e-38 | 47/48 (COLO 205, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.418×** | -12.2 | 4e-32 | 47/48 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.586×** | -7.5 | 8e-12 | 36/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -6.6 | 5e-09 | 32/48 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -6.4 | 1e-08 | 40/48 (NCI-H460, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -6.1 | 7e-08 | 31/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -6.1 | 7e-08 | 35/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -5.9 | 2e-07 | 33/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -5.8 | 3e-07 | 36/49 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.668×** | -5.3 | 4e-06 | 34/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.691×** | -5.2 | 1e-05 | 37/48 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.692×** | -5.1 | 1e-05 | 39/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.701×** | -5.0 | 3e-05 | 27/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -4.1 | 0.001 | 27/48 (PANC-1, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 150 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -30.3) |
| [[LoVo (line)]] | wt | 244 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.9) |
| [[NCI-H460 (line)]] | wt | 145 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -28.6) |
| [[SW480 (line)]] | alt | 226 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -19.5) |
| [[HEC-1-A (line)]] | alt | 107 | 2 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.35× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -27.3) |
| [[HT-29 (line)]] | alt | 212 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -20.2) |
| [[NCI-H1573 (line)]] | alt | 339 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.5) |
| [[RKO (line)]] | wt | 173 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -22.7) |
| [[A-172 (line)]] | wt | 213 | 3 | 3 | [[Homoharringtonine (drug)]] 0.05 µM 2.48× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.323× (z -13.7) |
| [[A-427 (line)]] | wt | 71.7 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -13.0) |
| [[H4 (line)]] | wt | 200 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 269 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -20.2) |
| [[SHP-77 (line)]] | alt | 58.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -11.6) |
| [[A549 (line)]] | wt | 159 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -23.9) |
| [[KATO III (line)]] | alt | 203 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 156 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -17.9) |
| [[A498 (line)]] | wt | 254 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.385× (z -11.4) |
| [[C32 (line)]] | wt | 154 | 3 | 1 | [[Harringtonine (drug)]] 0.5 µM 3.24× (z +12.2) | [[PH-797804 (drug)]] 5 µM 0.207× (z -8.5) |
| [[COLO 205 (line)]] | alt | 251 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -18.3) |
| [[HCT15 (line)]] | alt | 164 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -16.0) |
| [[HS-578T (line)]] | alt | 138 | 2 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.363× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 95.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.4) |
| [[Panc 03.27 (line)]] | alt | 165 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 205 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 178 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.32× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.7) |
| [[BT-474 (line)]] | alt | 139 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.5) |
| [[SNU-423 (line)]] | alt | 149 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 141 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.320× (z -11.1) |
| [[CHP-212 (line)]] | wt | 148 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.252× (z -9.2) |
| [[J82 (line)]] | alt | 208 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -11.7) |
| [[SW 900 (line)]] | alt | 124 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.65× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.6) |
| [[SW1417 (line)]] | alt | 188 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[C-33 A (line)]] | alt | 61.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -10.8) |
| [[Hs 766T (line)]] | wt | 211 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -9.5) |
| [[LS 180 (line)]] | wt | 78.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.0) |
| [[SNU-1 (line)]] | wt | 83.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -9.0) |
| [[SW48 (line)]] | wt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.1) |
| [[AN3 CA (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 186 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAMP1-AS1]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SP110]] | +0.69 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[PARP14]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PLEKHA4]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ZNFX1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 | same gene group |
| [[SLFN5]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[IFI16]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 | pathway: Cytosolic sensors of pathogen-associated DNA; STRING 616 |
| [[TRIM21]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 | same gene group; pathway: Cytosolic sensors of pathogen-associated DNA; STRING 653 |
| [[CCDC194]] | +0.67 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[TRIM5]] | +0.67 | +0.57 / +0.68 | both halves | 8e-06 | same gene group; STRING 610 |
| [[IFIH1]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 | STRING 502 |
| [[NMI]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO1]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[NDRG3]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PIK3R2]] | -0.57 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[PAPSS1]] | -0.57 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ELP1]] | -0.56 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SKP2]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TCF3]] | -0.55 | -0.54 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | GBP4 activity raises TRIM56's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without GBP4 | 0.013 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TRIM56's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[SLFN5]] | B | SLFN5 activity raises TRIM56's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without SLFN5 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[SAA2-SAA4]] | B | SAA2-SAA4 activity raises TRIM56's level | lines that do not express SAA2-SAA4 (22) vs lines expressing it (28) | 1.45× lower at baseline in the lines without SAA2-SAA4 | 0.073 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SAA2, SAA1, LMO2 |
| [[LINC02577]] | B | LINC02577 activity raises TRIM56's level | lines that do not express LINC02577 (22) vs lines expressing it (28) | 1.44× lower at baseline in the lines without LINC02577 | 0.077 | ⚠ within organs, on part of the lines; also absent: CALB2, LHX1-DT, PTX3 |
| [[RSAD2]] | B | RSAD2 activity raises TRIM56's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.47× lower at baseline in the lines without RSAD2 | 0.098 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[PSMB8]] | C | PSMB8 activity raises TRIM56's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without PSMB8 | 0.073 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.5, 54.7); signed map (61.6, 32.8). **Vector** length 125, 49.1% of its response variance represented; |z| ≥ 3 in 1,384 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.53 to 56); *interferon gamma response* (hallmark, mean cos +0.54 to 60); *interferon* (control, mean cos +0.56 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +3.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.9 | +4.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -7.6 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.0 | -0.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -6.2 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.9 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.6 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.4 | -2.1 |
|  | [[Ixazomib (drug)]] 5 µM |  | -3.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 56 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,085,481-101,097,967 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF109 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Regulation of innate immune responses to cytosolic DNA; Cytosolic sensors of pathogen-associated DNA; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRZ2](https://www.uniprot.org/uniprotkb/Q9BRZ2) (E3 ubiquitin-protein ligase TRIM56):

> E3 ubiquitin-protein ligase that plays a key role in innate antiviral immunity by mediating ubiquitination of CGAS and STING1. In response to pathogen- and host-derived double-stranded DNA (dsDNA), targets STING1 to 'Lys-63'-linked ubiquitination, thereby promoting its homodimerization, a step required for the production of type I interferon IFN-beta (By similarity). Also mediate monoubiquitination of CGAS, thereby promoting CGAS oligomerization and subsequent activation. Promotes also …

**Summary**, from NCBI Gene [81844](https://www.ncbi.nlm.nih.gov/gene/81844):

> Enables ubiquitin protein ligase activity. Involved in defense response to virus; positive regulation of signal transduction; and protein monoubiquitination. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19028) · Entrez [81844](https://www.ncbi.nlm.nih.gov/gene/81844) · UniProt [Q9BRZ2](https://www.uniprot.org/uniprotkb/Q9BRZ2) · Ensembl [ENSG00000169871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169871)

## Data

Gene col 9864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9864); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9864]; `tensor/DDL_lfc|DDL_z.npy` [9864]; `embed/gene_vectors.npy` [9864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9864 or target_col == 9864). Every well: [[TRIM56 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM56.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
