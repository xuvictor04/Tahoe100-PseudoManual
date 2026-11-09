---
symbol: "RBPMS"
type: "gene"
col: 8043
ensembl_id: "ENSG00000157110"
name: "RNA binding protein, mRNA processing factor"
location: "8p12"
module: 8
arm: "+"
pooled_cpm: 71.01
n_lines_expressing: 38
n_dd_up: 8
n_dd_down: 31
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 22
direction_downstream: 22
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RBPMS

*RNA binding protein, mRNA processing factor* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.36× (z +4.4, q 0.005, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.157× (z -28.0, q 0e+00, down in 36 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTN4]] (+0.66, fdr 1e-05), [[RARRES1]] (+0.59, fdr 3e-05), [[STS]] (+0.58, fdr 1e-05); moves opposite to [[NBPF3]] (-0.48, fdr 2e-04), [[PAQR5]] (-0.47, fdr 1e-04), [[RPS6KA2]] (-0.47, fdr 6e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[KMO]] → it (grade B ⚠); 22 go from it, the strongest it → [[ZHX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.4 | 0.005 | 23/35 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.3 | 0.005 | 16/36 (AsPC-1, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.037 | 16/36 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.037 | 16/37 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.064 | 14/36 (AsPC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.086 | 14/38 (AsPC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.086 | 14/36 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.27×** | +3.2 | 0.086 | 16/37 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.157×** | -28.0 | 0e+00 | 36/36 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.163×** | -27.3 | 0e+00 | 36/36 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.193×** | -24.8 | 0e+00 | 35/36 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.465×** | -11.6 | 8e-29 | 31/36 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -10.5 | 1e-23 | 25/36 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.607×** | -7.5 | 5e-12 | 29/36 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.607×** | -7.3 | 3e-11 | 26/35 (KATO III, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.694×** | -5.5 | 3e-06 | 21/36 (BT-474, CFPAC-1, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.698×** | -5.4 | 3e-06 | 22/36 (SW 900, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -5.3 | 6e-06 | 20/36 (BT-474, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.696×** | -5.3 | 6e-06 | 23/36 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.513×** | -5.3 | 6e-06 | 25/36 (BT-474, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.523×** | -5.1 | 1e-05 | 23/37 (KATO III, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.789×** | -5.1 | 2e-05 | 19/36 (BT-474, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **0.713×** | -4.9 | 3e-05 | 20/31 (NCI-H2030, KATO III, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.727×** | -4.8 | 5e-05 | 19/36 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -4.7 | 1e-04 | 22/36 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.756×** | -4.2 | 6e-04 | 18/37 (HOP62, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 185 | 0 | 26 (10 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0664× (z -20.4) |
| [[HEC-1-A (line)]] | alt | 191 | 9 (1 ⚠) | 4 | [[Cobimetinib (drug)]] 5 µM 2.72× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.0912× (z -25.2) |
| [[AsPC-1 (line)]] | alt | 85.2 | 7 (1 ⚠) | 4 | [[Trametinib (drug)]] 5 µM 3.68× (z +12.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 2.98× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -19.5) |
| [[KATO III (line)]] | alt | 139 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0465× (z -28.5) |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.110× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 166 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -17.9) |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.124× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -13.7) |
| [[A498 (line)]] | wt | 194 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0968× (z -24.0) |
| [[A549 (line)]] | wt | 202 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0974× (z -21.0) |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -15.2) |
| [[HS-578T (line)]] | alt | 162 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0914× (z -18.2) |
| [[NCI-H1573 (line)]] | alt | 47.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.272× (z -10.0) |
| [[SW 900 (line)]] | alt | 138 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -13.7) |
| [[SW480 (line)]] | alt | 54.5 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0937× (z -27.0) |
| [[A-172 (line)]] | wt | 48.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -17.5) |
| [[COLO 205 (line)]] | alt | 50.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -13.7) |
| [[J82 (line)]] | alt | 53.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -21.2) |
| [[NCI-H2347 (line)]] | alt | 76.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 42.6 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.192× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 59.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -13.9) |
| [[RKO (line)]] | wt | 97.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -22.3) |
| [[C32 (line)]] | wt | 38.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -9.7) |
| [[H4 (line)]] | wt | 60.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.156× (z -13.0) |
| [[HT-29 (line)]] | alt | 33.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -11.8) |
| [[LoVo (line)]] | wt | 63.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -20.5) |
| [[NCI-H1792 (line)]] | alt | 66.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0885× (z -19.6) |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 53.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -13.2) |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -10.6) |
| [[SNU-423 (line)]] | alt | 33.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -12.7) |
| [[SW48 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A-427 (line)]] | wt | 8.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTN4]] | +0.66 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[RARRES1]] | +0.59 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[STS]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RBM47]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |
| [[SAMD12-AS1]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP42]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[FRK]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[CTSS]] | +0.50 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[NRIP1]] | +0.50 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[MMP7]] | +0.50 | +0.44 / +0.37 | both halves | 7e-05 |  |
| [[TMEM217]] | +0.50 | +0.43 / +0.43 | both halves | 4e-05 |  |
| [[TNS3]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.48 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[PAQR5]] | -0.47 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[RPS6KA2]] | -0.47 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[ZFYVE28]] | -0.46 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[FYN]] | -0.46 | -0.31 / -0.39 | both halves | 2e-04 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[ANKRD36B]] | -0.45 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[VPS26C]] | -0.45 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[DDIT4]] | -0.44 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[NUP58]] | -0.44 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[GPT2]] | -0.44 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[IL17RD]] | -0.44 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[PTPDC1]] | -0.44 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 19, C 3. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KMO]] | B | KMO activity raises RBPMS's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.77× lower at baseline in the lines without KMO | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[NRIP1]] | B | NRIP1 activity raises RBPMS's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 4.39× lower at baseline in the lines without NRIP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises RBPMS's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.01× lower at baseline in the lines without CTSS | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers RBPMS's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[NTN4]] | B | NTN4 activity raises RBPMS's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without NTN4 | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[RARRES1]] | B | RARRES1 activity raises RBPMS's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.43× lower at baseline in the lines without RARRES1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[CASP10]] | B | CASP10 activity raises RBPMS's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without CASP10 | 0.031 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[GBP1]] | B | GBP1 activity raises RBPMS's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.30× lower at baseline in the lines without GBP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[VNN1]] | B | VNN1 activity raises RBPMS's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without VNN1 | 0.033 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[HAVCR1]] | B | HAVCR1 activity raises RBPMS's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.93× lower at baseline in the lines without HAVCR1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA |
| [[TNS3]] | B | TNS3 activity raises RBPMS's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 3.90× lower at baseline in the lines without TNS3 | 0.047 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[CP]] | B | CP activity raises RBPMS's level | lines that do not express CP (39) vs lines expressing it (11) | 2.55× lower at baseline in the lines without CP | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZHX2]] | B | RBPMS activity raises ZHX2's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 3.51× lower at baseline in the lines without RBPMS | 0.013 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[GBP1]] | B | RBPMS activity raises GBP1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 3.44× lower at baseline in the lines without RBPMS | 0.023 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[SERPINB9P1]] | B | RBPMS activity raises SERPINB9P1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without RBPMS | 0.032 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[SH3RF1]] | B | RBPMS activity raises SH3RF1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.12× lower at baseline in the lines without RBPMS | 0.033 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[NTN4]] | B | RBPMS activity raises NTN4's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 3.10× lower at baseline in the lines without RBPMS | 0.038 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[CTSS]] | B | RBPMS activity raises CTSS's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.81× lower at baseline in the lines without RBPMS | 0.038 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[PIGF]] | B | RBPMS activity lowers PIGF's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.54× higher at baseline in the lines without RBPMS | 0.052 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[SAMD12-AS1]] | B | RBPMS activity raises SAMD12-AS1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without RBPMS | 0.053 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[ARHGAP42]] | B | RBPMS activity raises ARHGAP42's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.72× lower at baseline in the lines without RBPMS | 0.059 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[TTC6]] | B | RBPMS activity raises TTC6's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without RBPMS | 0.062 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[ITGB8]] | B | RBPMS activity raises ITGB8's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without RBPMS | 0.067 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[ADGRF1]] | B | RBPMS activity raises ADGRF1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.65× lower at baseline in the lines without RBPMS | 0.075 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, 55.1); signed map (58.9, -1.2). **Vector** length 101, 27.6% of its response variance represented; |z| ≥ 3 in 1,212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | +5.1 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.4 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | -10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +3.7 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.1 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -24.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding protein, mRNA processing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,384,511-30,572,256 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HERMES |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93062](https://www.uniprot.org/uniprotkb/Q93062) (RNA-binding protein with multiple splicing):

> [Isoform A]: RNA binding protein that mediates the regulation of pre-mRNA alternative splicing (AS). Acts either as activator (FLNB, HSPG2, LIPA1, MYOCD, PTPRF and PPFIBP1) or repressor (TPM1, ACTN1, ITGA7, PIEZO1, LSM14B, MBNL1 and MBML2) of splicing events on specific pre-mRNA targets (By similarity). Together with RNA binding proteins RBFOX2 and MBNL1/2, activates a splicing program associated with differentiated contractile vascular smooth muscle cells (SMC) by regulating AS of numerous …

**Summary**, from NCBI Gene [11030](https://www.ncbi.nlm.nih.gov/gene/11030):

> This gene encodes a member of the RNA recognition motif family of RNA-binding proteins. The RNA recognition motif is between 80-100 amino acids in length and family members contain one to four copies of the motif. The RNA recognition motif consists of two short stretches of conserved sequence, as well as a few highly conserved hydrophobic residues. The encoded protein has a single, putative RNA recognition motif in its N-terminus. Alternative splicing results in multiple transcript variants …

**Accessions** — [HGNC:19097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19097) · Entrez [11030](https://www.ncbi.nlm.nih.gov/gene/11030) · UniProt [Q93062](https://www.uniprot.org/uniprotkb/Q93062) · Ensembl [ENSG00000157110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157110)

## Data

Gene col 8043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8043); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8043]; `tensor/DDL_lfc|DDL_z.npy` [8043]; `embed/gene_vectors.npy` [8043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8043 or target_col == 8043). Every well: [[RBPMS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBPMS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
