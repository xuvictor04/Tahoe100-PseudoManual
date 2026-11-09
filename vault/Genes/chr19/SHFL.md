---
symbol: "SHFL"
type: "gene"
col: 5132
ensembl_id: "ENSG00000130813"
name: "shiftless antiviral inhibitor of ribosomal frameshifting"
location: "19p13.2"
module: 32
arm: "+"
pooled_cpm: 13.68
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 39
n_dd_up_clean: 13
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 26
direction_downstream: 31
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SHFL

*shiftless antiviral inhibitor of ribosomal frameshifting* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.72× (z +6.8, q 6e-09, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.403× (z -16.8, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2L6]] (+0.86, fdr 7e-06), [[OAS1]] (+0.85, fdr 7e-06), [[IFI35]] (+0.84, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[IFI6]] → it (grade B ⚠); 31 go from it, the strongest it → [[IFIT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.72×** | +6.8 | 6e-09 | 33/43 (CFPAC-1, AsPC-1, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.006 | 12/43 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.006 | 17/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.006 | 19/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.008 | 16/47 (LoVo, RKO, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.018 | 13/48 (NCI-H23, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.023 | 17/45 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.027 | 9/44 (NCI-H1792, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.029 | 11/47 (HS-578T, SK-MEL-2, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.031 | 8/40 (C32, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.035 | 14/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.62×** | +3.2 | 0.070 | 5/42 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +3.2 | 0.070 | 7/48 (HS-578T, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.098 | 7/46 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.403×** | -16.8 | 0e+00 | 42/47 (SNU-423, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.440×** | -15.2 | 0e+00 | 39/45 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.536×** | -11.5 | 2e-28 | 32/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.503×** | -9.0 | 3e-17 | 31/47 (BT-474, C-33 A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -7.8 | 9e-13 | 32/47 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -7.7 | 2e-12 | 27/43 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.666×** | -7.5 | 4e-12 | 27/48 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.564×** | -7.5 | 5e-12 | 27/47 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.592×** | -6.9 | 4e-10 | 26/45 (BT-474, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.606×** | -6.6 | 3e-09 | 25/43 (LoVo, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -6.4 | 9e-09 | 24/46 (BT-474, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.607×** | -6.3 | 1e-08 | 25/46 (NCI-H23, A549, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.622×** | -6.2 | 2e-08 | 24/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.628×** | -5.9 | 2e-07 | 22/42 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -5.7 | 4e-07 | 24/43 (C-33 A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.665×** | -5.4 | 3e-06 | 24/47 (BT-474, C-33 A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -4.5 | 2e-04 | 22/45 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.706×** | -4.3 | 5e-04 | 21/45 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.564×** | -3.7 | 0.004 | 13/41 (BT-474, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.747×** | -3.7 | 0.005 | 12/45 (SHP-77, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 22.4 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 0 | 8 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.287× (z -11.1) |
| [[C-33 A (line)]] | alt | 33.0 | 0 | 7 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0673× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0509× (z -16.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0892× (z -13.0) |
| [[A-172 (line)]] | wt | 32.2 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -10.0) |
| [[A549 (line)]] | wt | 20.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -15.4) |
| [[LoVo (line)]] | wt | 18.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.0) |
| [[SNU-423 (line)]] | alt | 29.9 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -16.6) |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -11.7) |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -14.6) |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0205× (z -16.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -9.8) |
| [[A498 (line)]] | wt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -11.3) |
| [[C32 (line)]] | wt | 12.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 7.43 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -12.5) |
| [[RKO (line)]] | wt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.4) |
| [[H4 (line)]] | wt | 9.05 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0764× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[NCI-H460 (line)]] | wt | 4.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.5) |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.6) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2L6]] | +0.86 | +0.79 / +0.88 | both halves | 7e-06 | STRING 568 |
| [[OAS1]] | +0.85 | +0.80 / +0.89 | both halves | 7e-06 | STRING 544 |
| [[IFI35]] | +0.84 | +0.80 / +0.91 | both halves | 7e-06 | STRING 564 |
| [[PARP12]] | +0.84 | +0.80 / +0.88 | both halves | 7e-06 | STRING 522 |
| [[PARP9]] | +0.82 | +0.76 / +0.89 | both halves | 7e-06 |  |
| [[PML]] | +0.81 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[CMPK2]] | +0.81 | +0.75 / +0.86 | both halves | 7e-06 |  |
| [[MX1]] | +0.81 | +0.73 / +0.85 | both halves | 7e-06 | STRING 539 |
| [[IFI44]] | +0.80 | +0.71 / +0.87 | both halves | 7e-06 | STRING 478 |
| [[RSAD2]] | +0.80 | +0.71 / +0.87 | both halves | 7e-06 | STRING 531 |
| [[IFIT1]] | +0.80 | +0.75 / +0.86 | both halves | 7e-06 | STRING 481 |
| [[SLC15A3]] | +0.80 | +0.71 / +0.90 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 15, C 11. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI6]] | B | IFI6 activity raises SHFL's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.27× lower at baseline in the lines without IFI6 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises SHFL's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without BATF2 | 0.003 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[CD5L]] | B | CD5L activity raises SHFL's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.77× lower at baseline in the lines without CD5L | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[IFITM1]] | B | IFITM1 activity raises SHFL's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without IFITM1 | 0.015 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[SP110]] | B | SP110 activity raises SHFL's level | lines that do not express SP110 (5) vs lines expressing it (45) | 2.41× lower at baseline in the lines without SP110 | 0.018 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises SHFL's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without PARP9 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[HERC6]] | B | HERC6 activity raises SHFL's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without HERC6 | 0.019 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises SHFL's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without TRIM22 | 0.031 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[OAS1]] | B | OAS1 activity raises SHFL's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without OAS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers SHFL's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[PLSCR1]] | B | PLSCR1 activity raises SHFL's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without PLSCR1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity strengthens SHFL's drug response | lines that do not express IFI6 (13) vs lines expressing it (35) | the lines without IFI6 respond 0.37× as strongly (z diff +2.01); rises at some drug-doses, falls at others (25% from rises): Idarubicin (hydrochloride) 5 µM: 0.56x vs 0.37x (z diff +3.9); Fedratinib (hydrochloride hydrate) 5 µM: 0.80x vs 0.45x (z diff +3.0); Cobimetinib 5 µM: 1.44x vs 1.81x (z diff +1.8) | 0.058 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 0, C 31. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT5]] | C | SHFL's natural level strengthens IFIT5's drug response | SHFL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.71; direction not clear | 4e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | SHFL's natural level strengthens ADAR's drug response | SHFL's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.65; direction not clear | 3e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | SHFL's natural level strengthens IRF9's drug response | SHFL's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.63; direction not clear | 8e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | SHFL's natural level strengthens USP18's drug response | SHFL's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.63; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRANK1]] | C | SHFL's natural level strengthens TRANK1's drug response | SHFL's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.57; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | SHFL's natural level strengthens PML's drug response | SHFL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.61; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | SHFL's natural level strengthens TDRD7's drug response | SHFL's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.52; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[OGFR]] | C | SHFL's natural level strengthens OGFR's drug response | SHFL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.57; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[IFI35]] | C | SHFL's natural level strengthens IFI35's drug response | SHFL's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.60; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | SHFL's natural level strengthens PARP12's drug response | SHFL's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.55; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | SHFL's natural level strengthens IFIT1's drug response | SHFL's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.46; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | SHFL's natural level strengthens CMTR1's drug response | SHFL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.55; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.8, 54.1); signed map (66.2, 31.9). **Vector** length 107, 28.0% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.71 to 56); *interferon gamma response* (hallmark, mean cos +0.71 to 60); *interferon* (control, mean cos +0.76 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.2 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +3.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.1 | -11.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.7 | -6.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.7 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -15.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.3 | -5.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.7 | -9.0 |

## What is on record

|  |  |
|---|---|
| Name | shiftless antiviral inhibitor of ribosomal frameshifting |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,086,122-10,093,252 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11286, RyDEN, IRAV, SFL; previously C19orf66 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUL5](https://www.uniprot.org/uniprotkb/Q9NUL5) (Shiftless antiviral inhibitor of ribosomal frameshifting protein):

> Inhibits programmed -1 ribosomal frameshifting (-1PRF) of a variety of mRNAs from viruses, such as HIV1, and cellular genes, such as PEG10. Interacts with the -1PRF signal of target mRNA and translating ribosomes and causes premature translation termination at the frameshifting site. Regulates HIV1 GAG-POL expression by inhibiting -1PRF. Exhibits antiviral activity against dengue virus (DENV) and can inhibit the replication of all DENV serotypes. May block the protein translation of DENV RNA …

**Summary**, from NCBI Gene [55337](https://www.ncbi.nlm.nih.gov/gene/55337):

> This gene is an interferon stimulated gene (ISG) that inhibits viral replication. The encoded protein binds nucleic acids and inhibits programmed -1 ribosomal frameshifting required for translation by many RNA viruses. Viruses inhibited by the protein include Zika virus, dengue virus and the coronaviruses, SARS-CoV and SARS-CoV2. [provided by RefSeq, Aug 2021]

**Accessions** — [HGNC:25649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25649) · Entrez [55337](https://www.ncbi.nlm.nih.gov/gene/55337) · UniProt [Q9NUL5](https://www.uniprot.org/uniprotkb/Q9NUL5) · Ensembl [ENSG00000130813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130813)

## Data

Gene col 5132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5132); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5132]; `tensor/DDL_lfc|DDL_z.npy` [5132]; `embed/gene_vectors.npy` [5132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5132 or target_col == 5132). Every well: [[SHFL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHFL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
