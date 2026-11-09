---
symbol: "HRK"
type: "gene"
col: 5657
ensembl_id: "ENSG00000135116"
name: "harakiri, BCL2 interacting protein"
location: "12q24.22"
module: 125
arm: "+"
pooled_cpm: 2.74
n_lines_expressing: 37
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# HRK

*harakiri, BCL2 interacting protein* — 12q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.39× (z +9.5, q 1e-18, up in 23 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.109×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.0570×; ⚠ cell-cycle shift, explains ~39% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEX2]] (+0.58, fdr 1e-05), [[SPINK1]] (+0.57, fdr 3e-05), [[KCP]] (+0.53, fdr 1e-05); moves opposite to [[GTF3C1]] (-0.53, fdr 2e-05), [[MYCBP]] (-0.47, fdr 4e-05), [[PPP1CA]] (-0.46, fdr 7e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ENTREP1]] → it (grade B ⚠); 4 go from it, the strongest it → [[ADAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +9.5 | 1e-18 | 23/30 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.17×** | +8.9 | 2e-16 | 19/27 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.48×** | +7.0 | 5e-10 | 18/27 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +6.6 | 8e-09 | 10/25 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.4 | 2e-08 | 10/25 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +5.9 | 3e-07 | 6/14 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +5.7 | 1e-06 | 14/31 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +5.6 | 1e-06 | 1/1 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.96×** | +5.2 | 1e-05 | 8/29 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +4.1 | 0.002 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.003 | 5/31 (A-172, C-33 A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM |  | **1.65×** | +3.9 | 0.005 | 1/27 (SW480) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.005 | 5/28 (A-172, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.007 | 8/29 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.007 | 7/30 (C-33 A, SNU-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.010 | 6/27 (RKO, A549, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.017 | 5/28 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.017 | 5/22 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5657.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.109×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.0570×; ⚠ cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.645× | -3.4 | 0.39 | 0/31 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.661× | -3.2 | 0.39 | 7/24 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.72 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +10.8) | — |
| [[J82 (line)]] | alt | 4.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +12.0) | — |
| [[A-427 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0570× (z -8.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.748 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.941 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.809 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEX2]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SPINK1]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[KCP]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CEBPB]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[RPLP0P2]] | +0.52 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[LMO4]] | +0.52 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[KCND3]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[DISC1FP1]] | +0.52 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[C11orf96]] | +0.52 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[LINC02154]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[LINC00937]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[PRKAG2]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C1]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MYCBP]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PPP1CA]] | -0.46 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[GPAA1]] | -0.46 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[LRPAP1]] | -0.45 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[DZANK1]] | -0.44 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[PCDHGC3]] | -0.44 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[MORN1]] | -0.44 | -0.19 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[CFL1]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[C2CD3]] | -0.43 | -0.29 / -0.33 | both halves | 3e-04 |  |
| [[SLC30A9]] | -0.43 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[ODF2]] | -0.43 | -0.44 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTREP1]] | B | ENTREP1 activity raises HRK's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.71× lower at baseline in the lines without ENTREP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[KCND3]] | B | KCND3 activity raises HRK's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.73× lower at baseline in the lines without KCND3 | 0.041 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[REEP1]] | B | REEP1 activity raises HRK's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without REEP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[RRAGD]] | B | RRAGD activity raises HRK's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without RRAGD | 0.056 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAP2]] | B | HRK activity raises ADAP2's level | lines that do not express HRK (13) vs lines expressing it (37) | 2.00× lower at baseline in the lines without HRK | 0.009 | ⚠ within organs, on part of the lines; also absent: AP3B2, BSN, ZNF71 |
| [[GNAL]] | B | HRK activity raises GNAL's level | lines that do not express HRK (13) vs lines expressing it (37) | 2.15× lower at baseline in the lines without HRK | 0.011 | ⚠ within organs, on part of the lines; also absent: AP3B2, BSN, ZNF71 |
| [[WDSUB1]] | B | HRK activity raises WDSUB1's level | lines that do not express HRK (13) vs lines expressing it (37) | 1.52× lower at baseline in the lines without HRK | 0.019 | ⚠ within organs, on part of the lines; also absent: AP3B2, BSN, ZNF71 |
| [[BCAS4]] | B | HRK activity raises BCAS4's level | lines that do not express HRK (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without HRK | 0.037 | ⚠ within organs, on part of the lines; also absent: AP3B2, BSN, ZNF71 |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.5, 23.1); signed map (36.1, 23.2). **Vector** length 57.8, 12.4% of its response variance represented; |z| ≥ 3 in 655 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.4 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -0.7 |
|  | [[ML264 (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | harakiri, BCL2 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22 — chr12:116,856,144-116,881,441 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DP5 |
| Gene groups (HGNC) | BCL2 homology region 3 (BH3) only |
| Matched by | ensembl_id |

**Function**, from UniProt [O00198](https://www.uniprot.org/uniprotkb/O00198) (Activator of apoptosis harakiri):

> Promotes apoptosis.

**Summary**, from NCBI Gene [8739](https://www.ncbi.nlm.nih.gov/gene/8739):

> This gene encodes a member of the BCL-2 protein family. Members of this family are involved in activating or inhibiting apoptosis. The encoded protein localizes to intracellular membranes. This protein promotes apoptosis by interacting with the apoptotic inhibitors BCL-2 and BCL-X(L) via its BH3 domain. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:5185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5185) · Entrez [8739](https://www.ncbi.nlm.nih.gov/gene/8739) · UniProt [O00198](https://www.uniprot.org/uniprotkb/O00198) · Ensembl [ENSG00000135116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135116)

## Data

Gene col 5657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5657); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5657]; `tensor/DDL_lfc|DDL_z.npy` [5657]; `embed/gene_vectors.npy` [5657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5657 or target_col == 5657). Every well: [[HRK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HRK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
