---
symbol: "CSNK1E"
type: "gene"
col: 13149
ensembl_id: "ENSG00000213923"
name: "casein kinase 1 epsilon"
location: "22q13.1"
module: 136
arm: "+"
pooled_cpm: 131.76
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 29
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# CSNK1E

*casein kinase 1 epsilon* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 1.36× (z +4.9, q 7e-04, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.483× (z -16.1, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE28]] (+0.74, fdr 7e-06), [[DNAJC5]] (+0.72, fdr 7e-06), [[ARID3B]] (+0.72, fdr 7e-06); moves opposite to [[NNT]] (-0.64, fdr 1e-05), [[FUBP1]] (-0.63, fdr 2e-05), [[MED12]] (-0.60, fdr 3e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 7e-04 | 35/48 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +4.7 | 7e-04 | 29/49 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.017 | 26/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +3.9 | 0.017 | 27/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.7 | 0.025 | 26/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.025 | 28/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.082 | 27/48 (HT-29, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.22× | +3.1 | 0.13 | 23/48 (RPMI-7951, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.483×** | -16.1 | 0e+00 | 44/48 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.615×** | -7.3 | 8e-11 | 41/48 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.653×** | -6.6 | 6e-09 | 32/48 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.761×** | -6.0 | 3e-07 | 30/48 (J82, C32, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.672×** | -6.0 | 3e-07 | 34/47 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.690×** | -5.8 | 7e-07 | 34/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.694×** | -5.6 | 2e-06 | 33/50 (C32, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.693×** | -5.6 | 2e-06 | 38/47 (C32, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.773×** | -5.2 | 1e-05 | 34/48 (C32, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.768×** | -5.2 | 1e-05 | 33/48 (AsPC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.721×** | -5.1 | 2e-05 | 30/48 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.773×** | -5.1 | 2e-05 | 32/48 (C32, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.713×** | -5.1 | 2e-05 | 29/44 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.706×** | -5.0 | 2e-05 | 40/48 (C32, Hs 766T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.728×** | -4.9 | 3e-05 | 35/48 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.772×** | -4.4 | 3e-04 | 31/49 (C32, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.750×** | -4.3 | 5e-04 | 33/48 (C32, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 276 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -22.0) |
| [[HOP62 (line)]] | alt | 234 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 272 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 134 | 0 | 5 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.490× (z -9.6) |
| [[SW 900 (line)]] | alt | 167 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.1) |
| [[hTERT-HPNE (line)]] | wt | 211 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -19.8) |
| [[NCI-H23 (line)]] | alt | 162 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -19.8) |
| [[CFPAC-1 (line)]] | alt | 215 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -24.4) |
| [[NCI-H1573 (line)]] | alt | 339 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 81.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.9) |
| [[PANC-1 (line)]] | alt | 113 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -13.6) |
| [[RKO (line)]] | wt | 207 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.4) |
| [[A-172 (line)]] | wt | 106 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -15.5) |
| [[H4 (line)]] | wt | 159 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.6) |
| [[Hs 766T (line)]] | wt | 279 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.3) |
| [[J82 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 195 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -23.7) |
| [[A-427 (line)]] | wt | 69.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -24.4) |
| [[A549 (line)]] | wt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -9.7) |
| [[BT-474 (line)]] | alt | 84.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -8.5) |
| [[HCT15 (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -8.5) |
| [[HS-578T (line)]] | alt | 136 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -10.0) |
| [[LoVo (line)]] | wt | 99.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.449× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -13.0) |
| [[A498 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 101 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 94.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE28]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[DNAJC5]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[ARID3B]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[RASA3]] | +0.71 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[STX1A]] | +0.71 | +0.77 / +0.58 | both halves | 8e-06 |  |
| [[KCNN4]] | +0.70 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[PAQR5]] | +0.68 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[TMEM158]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MAP2K1]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TMEM184B]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 | ⚠ same locus (17.7 kb, same strand: neighbours can correlate without regulation) |
| [[FAM131A]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[RAC2]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 | pathway: Signaling by WNT |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | -0.64 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[FUBP1]] | -0.63 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[MED12]] | -0.60 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[STAG2]] | -0.60 | -0.38 / -0.48 | both halves | 7e-05 | pathway: Mitotic Prometaphase |
| [[TNS3]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ARFGAP2]] | -0.57 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TAPBPL]] | -0.57 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ARFGEF2]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[HFE]] | -0.57 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[ADI1]] | -0.56 | -0.56 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises CSNK1E's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.62× lower at baseline in the lines without BCL2A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[TMEM158]] | B | TMEM158 activity raises CSNK1E's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without TMEM158 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[STC1]] | B | STC1 activity raises CSNK1E's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without STC1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[SLC1A1]] | B | SLC1A1 activity raises CSNK1E's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without SLC1A1 | 0.031 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[ROBO3]] | B | ROBO3 activity raises CSNK1E's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without ROBO3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1 |
| [[LRRC8C]] | B | LRRC8C activity raises CSNK1E's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without LRRC8C | 0.067 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[GLRX]] | B | GLRX activity strengthens CSNK1E's drug response | lines that do not express GLRX (10) vs lines expressing it (40) | the lines without GLRX respond 0.87× as strongly (z diff +0.42); strongest at Selinexor 5 µM: 0.84x vs 0.73x (z diff +1.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent; artifact flags |
| [[GALNT18]] | B | GALNT18 activity raises CSNK1E's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without GALNT18 | 0.085 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[MAP2K1]] | B | MAP2K1 activity raises CSNK1E's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SDC3]] | C | SDC3 activity raises CSNK1E's level | lines that do not express SDC3 (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without SDC3 | 0.035 | ⚠ few lines (4 vs 46); across organs |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.2, 2.1); signed map (0.8, 49.3). **Vector** length 126, 43.5% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.8 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.6 | +1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.0 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.6 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +5.4 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.4 | -7.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.4 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -16.1 |
|  | [[NG25 (drug)]] 5 µM |  | -6.1 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.0 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.6 | -5.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.6 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.5 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 1 epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,290,691-38,318,084 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCKIE, CKIE, CKIepsilon |
| Gene groups (HGNC) | Casein kinase 1 family |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 34 pathways, smallest: WNT mediated activation of DVL; AMP and AMPK regulate the circadian clock; Phosphorylation and nuclear translocation of the CRY:PER:kinase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P49674](https://www.uniprot.org/uniprotkb/P49674) (Casein kinase I isoform epsilon):

> Casein kinases are operationally defined by their preferential utilization of acidic proteins such as caseins as substrates (Probable). Participates in Wnt signaling. Phosphorylates DVL1. Phosphorylates DVL2. Phosphorylates NEDD9/HEF1 (By similarity). Central component of the circadian clock. In balance with PP1, determines the circadian period length, through the regulation of the speed and rhythmicity of PER1 and PER2 phosphorylation. Controls PER1 and PER2 nuclear transport and degradation …

**Summary**, from NCBI Gene [1454](https://www.ncbi.nlm.nih.gov/gene/1454):

> The protein encoded by this gene is a serine/threonine protein kinase and a member of the casein kinase I protein family, whose members have been implicated in the control of cytoplasmic and nuclear processes, including DNA replication and repair. The encoded protein is found in the cytoplasm as a monomer and can phosphorylate a variety of proteins, including itself. This protein has been shown to phosphorylate period, a circadian rhythm protein. Two transcript variants encoding the same …

**Accessions** — [HGNC:2453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2453) · Entrez [1454](https://www.ncbi.nlm.nih.gov/gene/1454) · UniProt [P49674](https://www.uniprot.org/uniprotkb/P49674) · Ensembl [ENSG00000213923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213923)

## Data

Gene col 13149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13149); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13149]; `tensor/DDL_lfc|DDL_z.npy` [13149]; `embed/gene_vectors.npy` [13149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13149 or target_col == 13149). Every well: [[CSNK1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
