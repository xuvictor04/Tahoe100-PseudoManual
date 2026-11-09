---
symbol: "MPZL3"
type: "gene"
col: 8359
ensembl_id: "ENSG00000160588"
name: "myelin protein zero like 3"
location: "11q23.3"
module: 8
arm: "+"
pooled_cpm: 30.16
n_lines_expressing: 25
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 17
direction_downstream: 63
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MPZL3

*myelin protein zero like 3* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +9.3, q 1e-17, up in 17 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Retinoic acid (drug)]] 0.05 µM: 0.716× (z -4.6, q 0.003, down in 14 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF6]] (+0.60, fdr 1e-05), [[RNF39]] (+0.57, fdr 2e-05), [[GRB7]] (+0.55, fdr 3e-05); moves opposite to [[CHCHD3]] (-0.55, fdr 3e-05), [[TOMM40]] (-0.51, fdr 2e-05), [[TTF2]] (-0.50, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[RASGEF1B]] → it (grade B ⚠); 63 go from it, the strongest it → [[BIK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +9.3 | 1e-17 | 17/23 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +8.6 | 2e-15 | 15/22 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +7.7 | 2e-12 | 14/21 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +7.6 | 4e-12 | 6/19 (A498, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.5 | 7e-12 | 3/22 (C32, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +6.1 | 1e-07 | 14/23 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +5.5 | 3e-06 | 16/22 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 4e-06 | 10/22 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.2 | 1e-05 | 10/23 (SW1417, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.5 | 3e-04 | 9/23 (KATO III, SW480, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.0 | 0.003 | 5/13 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +3.8 | 0.007 | 8/22 (NCI-H2030, A498, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.031 | 11/22 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Vilanterol (drug)]] 5 µM |  | 1.19× | +3.3 | 0.039 | 7/23 (SW1417, SW480, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.039 | 4/22 (AsPC-1, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.057 | 14/23 (A498, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.065 | 10/23 (SW480, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.716×** | -4.6 | 0.003 | 14/23 (CFPAC-1, SW48, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.723×** | -4.1 | 0.011 | 4/22 (SW480, BT-474, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.570×** | -4.0 | 0.011 | 16/22 (NCI-H2347, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.750×** | -3.9 | 0.012 | 13/23 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.753×** | -3.9 | 0.012 | 12/23 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.761×** | -3.7 | 0.017 | 16/22 (NCI-H2347, SW1417, …) | all doses, flat |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.788×** | -3.3 | 0.086 | 14/23 (NCI-H2347, SW48, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.789×** | -3.2 | 0.086 | 2/23 (SW 1088, Panc 03.27) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -3.2 | 0.087 | 6/23 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.798× | -3.1 | 0.10 | 9/23 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.798× | -3.1 | 0.10 | 10/22 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.847× | -3.0 | 0.12 | 7/23 (HCT15, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.657× | -3.0 | 0.12 | 14/22 (NCI-H2347, SW1417, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 76.4 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.260× (z -13.0) ⚠ unreliable plate only · without an alert: [[Belumosudil (drug)]] 5 µM 0.398× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 132 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 89.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 42.2 | 2 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.91× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 81.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 9.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 91.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 106 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +9.9) | — |
| [[LoVo (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.72 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.33 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF6]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[RNF39]] | +0.57 | +0.49 / +0.62 | both halves | 2e-05 |  |
| [[GRB7]] | +0.55 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[RND1]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[BTG1-DT]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PIK3IP1]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[HNRNPD-DT]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[MXD1]] | +0.51 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[DAPP1]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[AFTPH]] | +0.50 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[FHIP1A]] | +0.50 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[NECTIN4]] | +0.50 | +0.36 / +0.57 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD3]] | -0.55 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[TOMM40]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TTF2]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[POLR1A]] | -0.47 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CCT6A]] | -0.47 | -0.37 / -0.53 | both halves | 9e-05 |  |
| [[MCM3AP]] | -0.46 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[DCAF1]] | -0.46 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[LYRM4]] | -0.45 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[EIF2S1]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[NUP155]] | -0.45 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[NAT10]] | -0.44 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1B]] | B | RASGEF1B activity raises MPZL3's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 3.39× lower at baseline in the lines without RASGEF1B | 0.039 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[RND1]] | B | RND1 activity raises MPZL3's level | lines that do not express RND1 (9) vs lines expressing it (41) | 3.28× lower at baseline in the lines without RND1 | 0.068 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[FHIP1A]] | B | FHIP1A activity raises MPZL3's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 3.23× lower at baseline in the lines without FHIP1A | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[BIK]] | B | BIK activity raises MPZL3's level | lines that do not express BIK (15) vs lines expressing it (35) | 3.85× lower at baseline in the lines without BIK | 0.086 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[RNF39]] | C | RNF39 activity raises MPZL3's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 9.73× lower at baseline in the lines without RNF39 | 1e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent; co-absent with the target |
| [[IRF6]] | C | IRF6 activity raises MPZL3's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 9.30× lower at baseline in the lines without IRF6 | 1e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[ELF3]] | C | ELF3 activity raises MPZL3's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 6.24× lower at baseline in the lines without ELF3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3; co-absent with the target |
| [[DAPP1]] | C | DAPP1 activity raises MPZL3's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 7.39× lower at baseline in the lines without DAPP1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[NECTIN4]] | C | NECTIN4 activity raises MPZL3's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 5.86× lower at baseline in the lines without NECTIN4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25; co-absent with the target |
| [[GRB7]] | C | GRB7 activity raises MPZL3's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 6.72× lower at baseline in the lines without GRB7 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP; co-absent with the target |
| [[CNKSR1]] | C | CNKSR1 activity raises MPZL3's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 5.68× lower at baseline in the lines without CNKSR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2; co-absent with the target |
| [[KLF5]] | C | KLF5 activity raises MPZL3's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 4.54× lower at baseline in the lines without KLF5 | 0.003 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 50, C 13. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIK]] | B | MPZL3 activity raises BIK's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 3.22× lower at baseline in the lines without MPZL3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[RASGEF1B]] | B | MPZL3 activity raises RASGEF1B's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.81× lower at baseline in the lines without MPZL3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[MAL2-AS1]] | B | MPZL3 activity raises MAL2-AS1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.40× lower at baseline in the lines without MPZL3 | 1e-03 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[FHIP1A]] | B | MPZL3 activity raises FHIP1A's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 3.20× lower at baseline in the lines without MPZL3 | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[CBR3-AS1]] | B | MPZL3 activity raises CBR3-AS1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.47× lower at baseline in the lines without MPZL3 | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[RND1]] | B | MPZL3 activity raises RND1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without MPZL3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[LYRM4]] | B | MPZL3 activity lowers LYRM4's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.60× higher at baseline in the lines without MPZL3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[YTHDC1]] | B | MPZL3 activity raises YTHDC1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.28× lower at baseline in the lines without MPZL3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[MXD1]] | B | MPZL3 activity raises MXD1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without MPZL3 | 0.007 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[CNNM4]] | B | MPZL3 activity raises CNNM4's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.62× lower at baseline in the lines without MPZL3 | 0.009 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[NUDCD1]] | B | MPZL3 activity lowers NUDCD1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.30× higher at baseline in the lines without MPZL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[PRKDC]] | B | MPZL3 activity lowers PRKDC's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.58× higher at baseline in the lines without MPZL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.280). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.3, 59.6); signed map (54.7, 9.0). **Vector** length 70.8, 23.9% of its response variance represented; |z| ≥ 3 in 427 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | myelin protein zero like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,226,690-118,252,365 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | V-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWV2](https://www.uniprot.org/uniprotkb/Q6UWV2) (Myelin protein zero-like protein 3):

> Mediates homophilic cell-cell adhesion.

**Summary**, from NCBI Gene [196264](https://www.ncbi.nlm.nih.gov/gene/196264):

> Predicted to be involved in cell adhesion. Predicted to act upstream of or within extracellular matrix organization and hair cycle. Predicted to be located in membrane. Predicted to be active in plasma membrane. Implicated in lung cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27279) · Entrez [196264](https://www.ncbi.nlm.nih.gov/gene/196264) · UniProt [Q6UWV2](https://www.uniprot.org/uniprotkb/Q6UWV2) · Ensembl [ENSG00000160588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160588)

## Data

Gene col 8359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8359); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8359]; `tensor/DDL_lfc|DDL_z.npy` [8359]; `embed/gene_vectors.npy` [8359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8359 or target_col == 8359). Every well: [[MPZL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPZL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
