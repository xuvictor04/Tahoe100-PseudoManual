---
symbol: "SMPDL3B"
type: "gene"
col: 5122
ensembl_id: "ENSG00000130768"
name: "sphingomyelin phosphodiesterase acid like 3B"
location: "1p35.3"
module: 44
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 27
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 37
direction_downstream: 49
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# SMPDL3B

*sphingomyelin phosphodiesterase acid like 3B* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.74× (z +13.9, q 5e-41, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +10.0, q 2e-21, up in 13 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0951×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.166×; ⚠ cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.287×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGD3]] (+0.61, fdr 1e-05), [[CKMT1B]] (+0.60, fdr 1e-05), [[CKMT1A]] (+0.59, fdr 9e-06); moves opposite to [[MCPH1-AS1]] (-0.43, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[C4orf19]] → it (grade B ⚠); 49 go from it, the strongest it → [[CYP2J2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.74×** | +13.9 | 5e-41 | 2/4 (KATO III, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.81×** | +10.5 | 4e-23 | 2/8 (HEC-1-A, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +10.0 | 2e-21 | 13/24 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +8.5 | 4e-15 | 9/12 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +8.2 | 2e-14 | 10/24 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +6.3 | 3e-08 | 11/23 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +6.2 | 6e-08 | 8/24 (A-427, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.1 | 9e-08 | 5/15 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.7 | 9e-07 | 7/24 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.5 | 3e-04 | 7/24 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +4.4 | 5e-04 | 7/24 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.66×** | +3.9 | 0.004 | 1/12 (NCI-H1573) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.007 | 5/25 (SW480, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.012 | 5/23 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.012 | 2/14 (A-427, NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.029 | 2/24 (HEC-1-A, SW48) | all doses, stronger at high dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.035 | 6/18 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.036 | 6/24 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.34×** | +2.9 | 0.088 | 3/17 (A-427, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5122.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0951×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.166×; ⚠ cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.287×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.733× | -3.4 | 0.17 | 15/20 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.735× | -3.4 | 0.17 | 7/23 (HepG2/C3A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Decitabine (drug)]] 5 µM |  | 0.730× | -3.3 | 0.17 | 4/24 (HEC-1-A, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0951× (z -14.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 6.13 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -11.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A-172 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD3]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CKMT1B]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CKMT1A]] | +0.59 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[F5]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SLC27A2]] | +0.58 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MTMR8]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LARGE2]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SULT1C2]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PELI1]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[VIL1]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.53 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[SEMA4G]] | +0.53 | +0.54 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCPH1-AS1]] | -0.43 | -0.33 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 3, C 34. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4orf19]] | B | C4orf19 activity raises SMPDL3B's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without C4orf19 | 0.023 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[CYP2J2]] | B | CYP2J2 activity raises SMPDL3B's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 1.89× lower at baseline in the lines without CYP2J2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[DMTN]] | B | DMTN activity raises SMPDL3B's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without DMTN | 0.082 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[RAB25]] | C | RAB25 activity raises SMPDL3B's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 4.19× lower at baseline in the lines without RAB25 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[CLDN3]] | C | CLDN3 activity raises SMPDL3B's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 3.65× lower at baseline in the lines without CLDN3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises SMPDL3B's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.82× lower at baseline in the lines without ENPP5 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[ILDR1]] | C | ILDR1 activity raises SMPDL3B's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 3.50× lower at baseline in the lines without ILDR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1; co-absent with the target |
| [[PLEKHG6]] | C | PLEKHG6 activity raises SMPDL3B's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.40× lower at baseline in the lines without PLEKHG6 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises SMPDL3B's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.96× lower at baseline in the lines without TRIM29 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[TMC4]] | C | TMC4 activity raises SMPDL3B's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.73× lower at baseline in the lines without TMC4 | 0.003 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent; co-absent with the target |
| [[RASAL1]] | C | RASAL1 activity raises SMPDL3B's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without RASAL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises SMPDL3B's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.54× lower at baseline in the lines without TMEM139 | 0.006 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |

### Downstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 20, C 29. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP2J2]] | B | SMPDL3B activity raises CYP2J2's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without SMPDL3B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[NSUN7]] | B | SMPDL3B activity raises NSUN7's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 3.08× lower at baseline in the lines without SMPDL3B | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[BCL2L15]] | B | SMPDL3B activity raises BCL2L15's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without SMPDL3B | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[FGFR4]] | B | SMPDL3B activity raises FGFR4's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without SMPDL3B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | SMPDL3B activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| cells under [[Afatinib (drug)]] 5 µM | B | SMPDL3B activity lowers the cells' numbers under Afatinib 5 µM (makes them more sensitive) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 1.16× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[LINC01819]] | B | SMPDL3B activity raises LINC01819's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without SMPDL3B | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[MIR3936HG]] | B | SMPDL3B activity raises MIR3936HG's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without SMPDL3B | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[CTSH]] | B | SMPDL3B activity raises CTSH's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without SMPDL3B | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[C4orf19]] | B | SMPDL3B activity raises C4orf19's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.10× lower at baseline in the lines without SMPDL3B | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[PRSS16]] | B | SMPDL3B activity raises PRSS16's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without SMPDL3B | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | SMPDL3B activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 1.16× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.3, 44.4); signed map (59.4, 14.0). **Vector** length 38.1, 6.18% of its response variance represented; |z| ≥ 3 in 577 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +13.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.5 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.3 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin phosphodiesterase acid like 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,935,000-27,959,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASML3B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92485](https://www.uniprot.org/uniprotkb/Q92485) (Acid sphingomyelinase-like phosphodiesterase 3b):

> Lipid-modulating phosphodiesterase. Active on the surface of macrophages and dendritic cells and strongly influences macrophage lipid composition and membrane fluidity. Acts as a negative regulator of Toll-like receptor signaling (By similarity). Has in vitro phosphodiesterase activity, but the physiological substrate is unknown. Lacks activity with phosphocholine-containing lipids, but can cleave CDP-choline, and can release phosphate from ATP and ADP (in vitro) (By similarity).

**Summary**, from NCBI Gene [27293](https://www.ncbi.nlm.nih.gov/gene/27293):

> Enables phosphoric diester hydrolase activity. Predicted to be involved in negative regulation of inflammatory response; negative regulation of toll-like receptor signaling pathway; and obsolete membrane lipid catabolic process. Located in extracellular exosome and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21416) · Entrez [27293](https://www.ncbi.nlm.nih.gov/gene/27293) · UniProt [Q92485](https://www.uniprot.org/uniprotkb/Q92485) · Ensembl [ENSG00000130768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130768)

## Data

Gene col 5122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5122); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5122]; `tensor/DDL_lfc|DDL_z.npy` [5122]; `embed/gene_vectors.npy` [5122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5122 or target_col == 5122). Every well: [[SMPDL3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMPDL3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
