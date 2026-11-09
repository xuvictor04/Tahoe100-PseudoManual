---
symbol: "KMT5A"
type: "gene"
col: 11474
ensembl_id: "ENSG00000183955"
name: "lysine methyltransferase 5A"
location: "12q24.31"
module: 22
arm: "+"
pooled_cpm: 23.47
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KMT5A

*lysine methyltransferase 5A* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (21 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +15.7, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.681× (z -9.1, q 4e-17, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.737× (z -4.9, q 1e-04, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TACC3]] (+0.76, fdr 7e-06), [[HJURP]] (+0.75, fdr 7e-06), [[GTSE1]] (+0.73, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +15.7 | 0e+00 | 40/47 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.19×** | +13.1 | 5e-37 | 43/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.69×** | +12.3 | 1e-32 | 38/47 (RKO, NCI-H2347, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.08×** | +12.3 | 2e-32 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.86×** | +10.4 | 4e-23 | 39/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.74×** | +9.3 | 1e-18 | 34/47 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +8.8 | 2e-16 | 11/48 (LoVo, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.61×** | +8.0 | 1e-13 | 31/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.56×** | +7.2 | 5e-11 | 27/47 (A549, RKO, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.55×** | +7.1 | 9e-11 | 19/34 (LoVo, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.55×** | +7.1 | 9e-11 | 31/47 (NCI-H23, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.45×** | +6.2 | 2e-08 | 29/48 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 4e-08 | 31/47 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.50×** | +6.0 | 8e-08 | 28/42 (J82, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.8 | 2e-07 | 22/47 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 9e-05 | 21/47 (SW48, SW480, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.002 | 6/48 (SW480, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.012 | 13/47 (SW48, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.024 | 17/47 (SW480, BT-474, …) | top dose only |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.068 | 8/47 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +2.9 | 0.068 | 12/46 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | 1.18× | +2.8 | 0.094 | 4/48 (HT-29, SW1417, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +2.8 | 0.096 | 7/46 (HOP62, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.681×** | -9.1 | 4e-17 | 29/48 (A549, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.719×** | -5.5 | 8e-06 | 27/48 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.729×** | -5.3 | 2e-05 | 20/48 (HT-29, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.737×** | -4.9 | 1e-04 | 22/47 (A549, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.751×** | -4.8 | 2e-04 | 19/47 (NCI-H2347, H4, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.751×** | -4.6 | 3e-04 | 22/47 (RPMI-7951, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.826×** | -4.4 | 8e-04 | 14/48 (A498, SNU-423, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.848× | -3.7 | 0.013 | 16/48 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.818×** | -3.5 | 0.027 | 14/48 (A-427, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.866× | -3.4 | 0.029 | 18/48 (H4, LOX-IMVI, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.794×** | -3.4 | 0.029 | 14/47 (A498, NCI-H23, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.806×** | -3.4 | 0.029 | 13/48 (A498, AN3 CA, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.4 | 0.032 | 9/48 (LoVo, SK-MEL-2, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.833×** | -3.3 | 0.043 | 13/48 (A-427, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.832×** | -3.1 | 0.075 | 9/47 (C32, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.824×** | -3.0 | 0.088 | 9/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.825×** | -3.0 | 0.088 | 9/47 (NCI-H1573, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 23.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.2) | [[Selinexor (drug)]] 5 µM 0.374× (z -9.4) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW480 (line)]] | alt | 26.1 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.54× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.0) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.121× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.7) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.113× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.1) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[NCI-H460 (line)]] | wt | 20.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.541× (z -8.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[RKO (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.2) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[A-172 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TACC3]] | +0.76 | +0.66 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[HJURP]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[GTSE1]] | +0.73 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[KIF14]] | +0.72 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[TROAP]] | +0.72 | +0.63 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[BUB1]] | +0.72 | +0.64 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CDCA8]] | +0.71 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[IQGAP3]] | +0.71 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[NDE1]] | +0.71 | +0.57 / +0.74 | both halves | 9e-06 | **novel candidate** |
| [[PRR11]] | +0.70 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.70 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[SGO2]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises KMT5A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[CDC20]] | C | CDC20 activity raises KMT5A's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 1.76× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.0, -56.5); signed map (-50.1, -41.7). **Vector** length 92.1, 21.6% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.63 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.53 to 48); *E2F targets* (hallmark, mean cos +0.53 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +15.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~85% of this change | +3.3 | +5.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +6.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.5 | +13.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | +2.3 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.8 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | -0.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -7.7 | -9.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.0 | -5.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | -3.8 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.6 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | lysine methyltransferase 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,384,132-123,409,353 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SET8, SET07, PR-Set7; previously SETD8 |
| Gene groups (HGNC) | Histone lysine methyltransferases; SET domain containing |
| Hallmark sets | FATTY_ACID_METABOLISM, G2M_CHECKPOINT |
| Reactome | 20 pathways, smallest: Regulation of TP53 Activity through Methylation; Condensation of Prophase Chromosomes; PKMTs methylate histone lysines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQR1](https://www.uniprot.org/uniprotkb/Q9NQR1) (N-lysine methyltransferase KMT5A):

> Protein-lysine N-methyltransferase that monomethylates both histones and non-histone proteins. Specifically monomethylates 'Lys-20' of histone H4 (H4K20me1). H4K20me1 is enriched during mitosis and represents a specific tag for epigenetic transcriptional repression. Mainly functions in euchromatin regions, thereby playing a central role in the silencing of euchromatic genes. Required for cell proliferation, probably by contributing to the maintenance of proper higher-order structure of DNA …

**Summary**, from NCBI Gene [387893](https://www.ncbi.nlm.nih.gov/gene/387893):

> The protein encoded by this gene is a protein-lysine N-methyltransferase that can monomethylate Lys-20 of histone H4 to effect transcriptional repression of some genes. The encoded protein is required for cell proliferation and plays a role in chromatin condensation. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:29489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29489) · Entrez [387893](https://www.ncbi.nlm.nih.gov/gene/387893) · UniProt [Q9NQR1](https://www.uniprot.org/uniprotkb/Q9NQR1) · Ensembl [ENSG00000183955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183955)

## Data

Gene col 11474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11474); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11474]; `tensor/DDL_lfc|DDL_z.npy` [11474]; `embed/gene_vectors.npy` [11474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11474 or target_col == 11474). Every well: [[KMT5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
