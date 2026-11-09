---
symbol: "CERS5"
type: "gene"
col: 6322
ensembl_id: "ENSG00000139624"
name: "ceramide synthase 5"
location: "12q13.12"
module: 142
arm: "+"
pooled_cpm: 68.53
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# CERS5

*ceramide synthase 5* — 12q13.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.410× (z -11.8, q 3e-29, down in 43 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.611× (z -6.5, q 7e-09, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP4-1]] (+0.64, fdr 7e-06), [[STARD3]] (+0.63, fdr 7e-06), [[TPTEP2-CSNK1E]] (+0.63, fdr 7e-06); moves opposite to [[ASF1A]] (-0.59, fdr 7e-06), [[BBS10]] (-0.59, fdr 1e-05), [[VEZF1]] (-0.58, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KLF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.410×** | -11.8 | 3e-29 | 43/49 (AN3 CA, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.402×** | -11.6 | 1e-28 | 42/43 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.516×** | -8.4 | 7e-15 | 40/48 (A498, COLO 205, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.657×** | -7.9 | 5e-13 | 34/48 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.559×** | -7.1 | 1e-10 | 38/45 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -6.5 | 7e-09 | 33/48 (SNU-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.632×** | -6.1 | 1e-07 | 37/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.431×** | -5.8 | 4e-07 | 38/49 (NCI-H23, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.660×** | -5.3 | 8e-06 | 37/47 (SNU-423, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.692×** | -4.9 | 6e-05 | 33/48 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -4.5 | 4e-04 | 28/48 (A-172, BT-474, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.742×** | -3.8 | 0.007 | 29/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.752×** | -3.8 | 0.007 | 24/48 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **0.759×** | -3.6 | 0.011 | 26/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.845× | -3.2 | 0.061 | 23/48 (A498, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 79.2 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -12.3) |
| [[A498 (line)]] | wt | 89.1 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -16.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.371× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 62.5 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 77.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.347× (z -9.9) |
| [[AN3 CA (line)]] | alt | 67.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0678× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0740× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 137 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 77.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 70.7 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.261× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 44.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -14.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -8.7) |
| [[HOP62 (line)]] | alt | 88.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 75.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[LoVo (line)]] | wt | 62.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 50.9 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 83.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 75.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.129× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 66.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.261× (z -10.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 60.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.485× (z -8.5) |
| [[SW480 (line)]] | alt | 69.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 55.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.331× (z -8.8) |
| [[H4 (line)]] | wt | 103 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0990× (z -8.8) |
| [[HCT15 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -10.0) ⚠ cell-cycle shift, explains ~71% of this change |
| [[Hs 766T (line)]] | wt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[KATO III (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 67.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0811× (z -17.2) |
| [[SW 900 (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.328× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~75% of this change |
| [[A549 (line)]] | wt | 79.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4-1]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[STARD3]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ASB16-AS1]] | +0.62 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[DPY19L3]] | +0.61 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[RARS2]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[DIP2A]] | +0.60 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ZFYVE27]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[C19orf25]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SLC37A3]] | +0.59 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[SLC39A13]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[IFI27L1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASF1A]] | -0.59 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[BBS10]] | -0.59 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PABIR1]] | -0.57 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[REPIN1]] | -0.57 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPH2]] | -0.56 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.55 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[BHLHE41]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.55 | -0.59 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF4]] | B | KLF4 activity lowers CERS5's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 1.32× higher at baseline in the lines without KLF4 | 0.008 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[MID1]] | B | MID1 activity lowers CERS5's level | lines that do not express MID1 (6) vs lines expressing it (44) | 1.34× higher at baseline in the lines without MID1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: TLE6, ENSG00000132832, ENSG00000243944; maybe low, not absent |
| [[GATA6]] | B | GATA6 activity strengthens CERS5's drug response | lines that do not express GATA6 (18) vs lines expressing it (31) | the lines without GATA6 respond 0.59× as strongly (z diff +1.76); strongest at Homoharringtonine 5 µM: 0.87x vs 0.55x (z diff +4.9) | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3; target measured in part of the lines; artifact flags |
| [[TNFAIP3]] | C | TNFAIP3 activity lowers CERS5's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 1.33× higher at baseline in the lines without TNFAIP3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.3, -2.0); signed map (-44.8, 2.3). **Vector** length 102, 30.4% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.2 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.9 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -3.7 | -7.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ceramide synthase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,129,289-50,167,533 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Trh4, MGC45411, FLJ25304; previously LASS5 |
| Gene groups (HGNC) | CERS class homeoboxes; Ceramide synthases |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5B7](https://www.uniprot.org/uniprotkb/Q8N5B7) (Ceramide synthase 5):

> Ceramide synthase that catalyzes the transfer of the fatty acyl chain from fatty acyl-CoA to a sphingoid base, with high selectivity toward palmitoyl-CoA (hexadecanoyl-CoA; C16:0-CoA). Can use different sphingoid bases as substrates for ceramide synthesis, such as sphinganine in de novo synthesis, and sphing-4E-enine (sphingosine), (4R)-hydroxysphinganine (phytosphingosine) or sphinga-4E,14Z-dienine in salvage pathways. Other fatty acyl-CoAs such as long-chain saturated stearoyl-CoA …

**Summary**, from NCBI Gene [91012](https://www.ncbi.nlm.nih.gov/gene/91012):

> This gene encodes a protein that belongs to the TLC (TRAM, LAG1 and CLN8 homology domains) family of proteins. The encoded protein functions in the synthesis of ceramide, a lipid molecule that is involved in a several cellular signaling pathways. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:23749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23749) · Entrez [91012](https://www.ncbi.nlm.nih.gov/gene/91012) · UniProt [Q8N5B7](https://www.uniprot.org/uniprotkb/Q8N5B7) · Ensembl [ENSG00000139624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139624)

## Data

Gene col 6322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6322); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6322]; `tensor/DDL_lfc|DDL_z.npy` [6322]; `embed/gene_vectors.npy` [6322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6322 or target_col == 6322). Every well: [[CERS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CERS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
