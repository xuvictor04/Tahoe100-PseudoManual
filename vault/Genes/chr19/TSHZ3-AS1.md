---
symbol: "TSHZ3-AS1"
type: "gene"
col: 15566
ensembl_id: "ENSG00000267662"
name: "TSHZ3 antisense RNA 1"
location: "19q12"
module: 13
arm: "+"
pooled_cpm: 3.63
n_lines_expressing: 25
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 36
direction_downstream: 24
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# TSHZ3-AS1

*TSHZ3 antisense RNA 1* — 19q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.37× (z +14.3, q 9e-44, up in 15 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.402× (z -6.8, q 6e-09, down in 18 of 23 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.483× (z -6.1, q 2e-07, down in 19 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSHZ3]] (+0.71, fdr 7e-06, ⚠ same locus), [[GDNF-AS1]] (+0.63, fdr 8e-06), [[DENND2A]] (+0.62, fdr 1e-05), [[UBE2Q2P13]] (+0.60, fdr 3e-05); moves opposite to [[MGMT]] (-0.59, fdr 1e-05), [[MYO5C]] (-0.54, fdr 3e-04), [[DLEU1]] (-0.54, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[NEBL]] → it (grade B ⚠); 24 go from it, the strongest it → [[TRPC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +14.3 | 9e-44 | 15/17 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +10.1 | 2e-21 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +8.3 | 2e-14 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +8.1 | 1e-13 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +4.9 | 1e-04 | 7/15 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.67×** | +4.3 | 0.002 | 1/15 (A549) | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.99×** | +4.1 | 0.003 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.045 | 4/21 (A-427, H4, …) | top dose only |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.051 | 3/17 (NCI-H2030, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.062 | 3/19 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.094 | 1/15 (NCI-H23) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.01× | +3.1 | 0.11 | 0/7 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.402×** | -6.8 | 6e-09 | 18/23 (A-172, HS-578T, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.461×** | -6.4 | 3e-08 | 16/23 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.483×** | -6.1 | 2e-07 | 19/20 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.501×** | -5.8 | 1e-06 | 13/21 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.528×** | -5.3 | 1e-05 | 10/21 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.555×** | -4.9 | 8e-05 | 15/22 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.597×** | -4.3 | 0.001 | 13/21 (LOX-IMVI, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.626×** | -3.9 | 0.007 | 10/23 (PANC-1, H4, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.422×** | -3.8 | 0.011 | 13/19 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.642×** | -3.7 | 0.013 | 9/23 (PANC-1, SW 1088, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.472×** | -3.3 | 0.055 | 8/16 (NCI-H23, HS-578T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -3.2 | 0.063 | 14/20 (SW 900, RPMI-7951, …) | rises with dose |  |
| [[Rucaparib (phosphate) (drug)]] 5 µM |  | **0.654×** | -3.2 | 0.066 | 1/23 (CHP-212) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.496×** | -3.1 | 0.089 | 8/18 (NCI-H2030, SNU-423, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0416× (z -13.3) |
| [[A-172 (line)]] | wt | 23.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0722× (z -19.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.137× (z -10.3) |
| [[H4 (line)]] | wt | 22.7 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0690× (z -10.6) |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0428× (z -19.4) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0290× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 5.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 2.40 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0291× (z -9.4) |
| [[C32 (line)]] | wt | 3.59 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0377× (z -9.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 4.19 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -9.3) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW 900 (line)]] | alt | 6.66 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0436× (z -10.1) |
| [[A-427 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.726 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSHZ3]] | +0.71 | +0.74 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GDNF-AS1]] | +0.63 | +0.62 / +0.57 | both halves | 8e-06 | same gene group |
| [[DENND2A]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[UBE2Q2P13]] | +0.60 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[APCDD1L]] | +0.60 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[IPO9-AS1]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 | same gene group |
| [[LINC01615]] | +0.58 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[WNT5B]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LINC01119]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NAV1]] | +0.58 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[EVC2]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[TWIST2]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGMT]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[MYO5C]] | -0.54 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[DLEU1]] | -0.54 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[MIR4713HG]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[INPP4B]] | -0.49 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ICA1]] | -0.48 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[SEMA4D]] | -0.47 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[ANK3]] | -0.46 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[FAAH2]] | -0.46 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 3, C 33. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEBL]] | B | NEBL activity lowers TSHZ3-AS1's level | lines that do not express NEBL (17) vs lines expressing it (33) | 2.39× higher at baseline in the lines without NEBL | 0.067 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[MYO5C]] | B | MYO5C activity lowers TSHZ3-AS1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 2.92× higher at baseline in the lines without MYO5C | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[ICA1]] | B | ICA1 activity lowers TSHZ3-AS1's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.99× higher at baseline in the lines without ICA1 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises TSHZ3-AS1's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 4.14× lower at baseline in the lines without HS3ST3A1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[MSRB3]] | C | MSRB3 activity raises TSHZ3-AS1's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.76× lower at baseline in the lines without MSRB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises TSHZ3-AS1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.90× lower at baseline in the lines without FBN1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises TSHZ3-AS1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.63× lower at baseline in the lines without DKK3 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[MME]] | C | MME activity raises TSHZ3-AS1's level | lines that do not express MME (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without MME | 0.011 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[NTNG2]] | C | NTNG2 activity raises TSHZ3-AS1's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.28× lower at baseline in the lines without NTNG2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises TSHZ3-AS1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.22× lower at baseline in the lines without COL5A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[GLIS1]] | C | GLIS1 activity raises TSHZ3-AS1's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without GLIS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[MIR137HG]] | C | MIR137HG activity raises TSHZ3-AS1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.89× lower at baseline in the lines without MIR137HG | 0.026 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 4, C 20. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPC1]] | B | TSHZ3-AS1 activity raises TRPC1's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without TSHZ3-AS1 | 0.031 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[LINC01119]] | B | [[TSHZ3]], TSHZ3-AS1 activity raises LINC01119's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 2.03× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent genes |
| [[LOXL1]] | B | TSHZ3-AS1 activity raises LOXL1's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 2.79× lower at baseline in the lines without TSHZ3-AS1 | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[SSC5D]] | B | TSHZ3-AS1 activity raises SSC5D's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 2.09× lower at baseline in the lines without TSHZ3-AS1 | 0.099 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[MSRB3]] | C | TSHZ3-AS1 activity raises MSRB3's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 4.54× lower at baseline in the lines without TSHZ3-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[MRC2]] | C | [[TSHZ3]], TSHZ3-AS1 activity raises MRC2's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 4.87× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |
| [[ARHGAP22]] | C | [[TSHZ3]], TSHZ3-AS1 activity raises ARHGAP22's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 4.73× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |
| [[WIPF1]] | C | [[TSHZ3]], TSHZ3-AS1 activity raises WIPF1's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 5.00× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |
| [[MIR137HG]] | C | TSHZ3-AS1 activity raises MIR137HG's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 4.39× lower at baseline in the lines without TSHZ3-AS1 | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[FBN1]] | C | TSHZ3-AS1 activity raises FBN1's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 4.31× lower at baseline in the lines without TSHZ3-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[DKK3]] | C | TSHZ3-AS1 activity raises DKK3's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 4.82× lower at baseline in the lines without TSHZ3-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[BVES]] | C | TSHZ3-AS1 activity raises BVES's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 2.95× lower at baseline in the lines without TSHZ3-AS1 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.0, 15.9); signed map (25.7, 49.1). **Vector** length 62.0, 18.1% of its response variance represented; |z| ≥ 3 in 569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +0.9 | +1.6 |
|  | [[Saquinavir (drug)]] 5 µM |  | +0.9 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.2 | -6.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.8 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -5.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.3 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | TSHZ3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q12 — chr19:31,348,881-31,417,794 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55288) · Entrez [107985311](https://www.ncbi.nlm.nih.gov/gene/107985311) · Ensembl [ENSG00000267662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267662)

## Data

Gene col 15566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15566); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15566]; `tensor/DDL_lfc|DDL_z.npy` [15566]; `embed/gene_vectors.npy` [15566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15566 or target_col == 15566). Every well: [[TSHZ3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSHZ3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
