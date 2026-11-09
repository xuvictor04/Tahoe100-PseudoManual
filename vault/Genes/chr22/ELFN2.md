---
symbol: "ELFN2"
type: "gene"
col: 9382
ensembl_id: "ENSG00000166897"
name: "extracellular leucine rich repeat and fibronectin type III domain containing 2"
location: "22q13.1"
module: 78
arm: "+"
pooled_cpm: 7.32
n_lines_expressing: 31
n_dd_up: 5
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ELFN2

*extracellular leucine rich repeat and fibronectin type III domain containing 2* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.28× (z +8.6, q 5e-15, up in 6 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Demeclocycline (drug)]] 5 µM: 1.31× (z +4.1, q 0.005, up in 11 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.398× (z -9.4, q 3e-18, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO15B]] (+0.63, fdr 1e-05), [[STMN3]] (+0.56, fdr 1e-05), [[IDUA]] (+0.54, fdr 2e-04); moves opposite to [[EMC2]] (-0.48, fdr 7e-05), [[MRPS12]] (-0.46, fdr 8e-04, ⚠ not reproduced), [[MBD4]] (-0.45, fdr 4e-05), [[KIAA1143]] (-0.44, fdr 2e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ITGA3]] → it (grade B ⚠); 5 go from it, the strongest it → [[AHNAK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.6 | 5e-15 | 6/13 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +8.4 | 2e-14 | 18/21 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +6.4 | 4e-08 | 10/17 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.005 | 11/28 (SW1417, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.037 | 7/28 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.15 | 6/28 (A549, LoVo, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.35× | +3.1 | 0.15 | 5/26 (KATO III, HS-578T, …) | top dose only | position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.33× | +3.1 | 0.15 | 8/28 (NCI-H2347, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9382.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.398×** | -9.4 | 3e-18 | 23/28 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.430×** | -9.1 | 2e-17 | 21/28 (HOP62, PANC-1, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -8.6 | 1e-15 | 21/27 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.456×** | -8.5 | 3e-15 | 18/28 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.481×** | -7.9 | 3e-13 | 21/27 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.518×** | -7.1 | 1e-10 | 20/28 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.536×** | -6.7 | 1e-09 | 17/28 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.548×** | -6.5 | 5e-09 | 16/28 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.555×** | -6.4 | 1e-08 | 18/27 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -6.4 | 1e-08 | 17/29 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -5.9 | 2e-07 | 18/28 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.584×** | -5.6 | 1e-06 | 18/27 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.599×** | -5.5 | 1e-06 | 13/27 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.615×** | -5.3 | 5e-06 | 19/28 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.714×** | -5.2 | 9e-06 | 18/27 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.429×** | -4.8 | 6e-05 | 15/28 (HOP62, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -4.2 | 1e-03 | 12/26 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.0 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0399× (z -31.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 8.17 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0290× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -12.6) |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.108× (z -11.3) |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 6.43 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -8.5) |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.5) |
| [[A-172 (line)]] | wt | 5.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0781× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -12.9) |
| [[KATO III (line)]] | alt | 3.10 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0513× (z -9.1) |
| [[LoVo (line)]] | wt | 2.69 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0514× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 5.59 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0474× (z -17.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0947× (z -10.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 5.76 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.5 µM 0.0478× (z -10.0) |
| [[A-427 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO15B]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[STMN3]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[IDUA]] | +0.54 | +0.29 / +0.61 | both halves | 2e-04 |  |
| [[LTBP2]] | +0.54 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[CDC42BPG]] | +0.52 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[RMRP]] | +0.51 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[PLEC]] | +0.50 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[MFNG]] | +0.50 | +0.56 / +0.39 | both halves | 6e-05 | ⚠ same locus (41.6 kb, same strand: neighbours can correlate without regulation) |
| [[ALDH1A3]] | +0.49 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[SHANK2]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[RASGEF1A]] | +0.48 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[CCDC9B]] | +0.48 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[AXL]] | +0.48 | +0.33 / +0.52 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC2]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[MRPS12]] | -0.46 | -0.19 / -0.44 | ⚠ not reproduced | 8e-04 |  |
| [[MBD4]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[KIAA1143]] | -0.44 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[EMC6]] | -0.44 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[R3HCC1L]] | -0.44 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[RDH11]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[CHCHD1]] | -0.42 | -0.20 / -0.38 | both halves | 7e-04 |  |
| [[TRAPPC2B]] | -0.42 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[AHCYL2]] | -0.41 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[TBK1]] | -0.41 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[CEP164P1]] | -0.41 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[PUS3]] | -0.41 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA3]] | B | ITGA3 activity raises ELFN2's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.95× lower at baseline in the lines without ITGA3 | 0.009 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[CDC42BPG]] | B | CDC42BPG activity raises ELFN2's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.98× lower at baseline in the lines without CDC42BPG | 0.023 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[CARD10]] | B | CARD10 activity raises ELFN2's level | lines that do not express CARD10 (8) vs lines expressing it (42) | 3.00× lower at baseline in the lines without CARD10 | 0.060 | ⚠ within organs, on part of the lines; also absent: MFNG, LRP5, SDC1; maybe low, not absent; its own permutation p |
| [[CNTNAP3C]] | B | CNTNAP3C activity raises ELFN2's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without CNTNAP3C | 0.080 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA |
| [[DOC2A]] | B | DOC2A activity raises ELFN2's level | lines that do not express DOC2A (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without DOC2A | 0.093 | ⚠ within organs, on part of the lines; also absent: C12orf56, ENSG00000267405; maybe low, not absent |
| [[EPS8L2]] | B | EPS8L2 activity raises ELFN2's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without EPS8L2 | 0.0996 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[ALDH1A3]] | C | ALDH1A3 activity raises ELFN2's level | lines that do not express ALDH1A3 (20) vs lines expressing it (30) | 2.27× lower at baseline in the lines without ALDH1A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SHROOM4, ENSG00000232386, ADAMTS16; co-absent with the target |
| [[ITGB2]] | C | ITGB2 activity raises ELFN2's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without ITGB2 | 0.094 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHNAK2]] | B | ELFN2 activity raises AHNAK2's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 2.92× lower at baseline in the lines without ELFN2 | 0.009 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92 |
| [[PLEC]] | B | ELFN2 activity raises PLEC's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without ELFN2 | 0.023 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92 |
| [[LTBP3]] | B | ELFN2 activity raises LTBP3's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without ELFN2 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92 |
| [[ITGA3]] | B | ELFN2 activity raises ITGA3's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without ELFN2 | 0.065 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92 |
| [[ALDH1A3]] | C | ELFN2 activity raises ALDH1A3's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 4.07× lower at baseline in the lines without ELFN2 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.0, 1.8); signed map (6.2, 52.5). **Vector** length 66.1, 14.6% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.9 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -9.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | extracellular leucine rich repeat and fibronectin type III domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,367,960-37,427,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ63G5.3, KIAA1904; previously LRRC62, PPP1R29 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5R3F8](https://www.uniprot.org/uniprotkb/Q5R3F8) (Protein phosphatase 1 regulatory subunit 29):

> Inhibits phosphatase activity of protein phosphatase 1 (PP1) complexes.

**Summary**, from NCBI Gene [114794](https://www.ncbi.nlm.nih.gov/gene/114794):

> Predicted to enable signaling receptor activity. Predicted to be involved in chemical synaptic transmission. Predicted to act upstream of or within establishment of protein localization and gene expression. Located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29396) · Entrez [114794](https://www.ncbi.nlm.nih.gov/gene/114794) · UniProt [Q5R3F8](https://www.uniprot.org/uniprotkb/Q5R3F8) · Ensembl [ENSG00000166897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166897)

## Data

Gene col 9382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9382); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9382]; `tensor/DDL_lfc|DDL_z.npy` [9382]; `embed/gene_vectors.npy` [9382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9382 or target_col == 9382). Every well: [[ELFN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELFN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
