---
symbol: "DNAJC16"
type: "gene"
col: 3766
ensembl_id: "ENSG00000116138"
name: "DnaJ heat shock protein family (Hsp40) member C16"
location: "1p36.21"
module: 36
arm: "+"
pooled_cpm: 25.4
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# DNAJC16

*DnaJ heat shock protein family (Hsp40) member C16* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.18× (z +12.7, q 4e-34, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.496× (z -11.4, q 2e-27, down in 34 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.414× (z -7.5, q 9e-12, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENTPD5]] (+0.61, fdr 2e-05), [[MTOR]] (+0.61, fdr 1e-05), [[AP3S2]] (+0.58, fdr 2e-05); moves opposite to [[C2CD6]] (-0.54, fdr 5e-04), [[CCDC26]] (-0.54, fdr 3e-04), [[SORCS3]] (-0.53, fdr 8e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +12.7 | 4e-34 | 44/48 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +12.5 | 3e-33 | 43/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +10.4 | 3e-23 | 41/48 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +4.4 | 0.002 | 18/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.034 | 13/48 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.047 | 13/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.15 | 4/48 (A-427, Hs 766T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.15 | 11/48 (SK-MEL-2, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.22× | +3.0 | 0.15 | 7/48 (NCI-H23, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.496×** | -11.4 | 2e-27 | 34/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.533×** | -10.3 | 3e-22 | 32/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -8.1 | 1e-13 | 28/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -7.5 | 9e-12 | 33/48 (PANC-1, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.669×** | -6.5 | 7e-09 | 25/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -6.4 | 2e-08 | 27/48 (SW 900, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.530×** | -5.4 | 5e-06 | 24/47 (A-427, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.803×** | -5.1 | 3e-05 | 24/47 (AN3 CA, SNU-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.815×** | -4.7 | 2e-04 | 21/47 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.759×** | -4.5 | 4e-04 | 22/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.747×** | -4.4 | 6e-04 | 18/40 (PANC-1, SW480, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.765×** | -4.4 | 6e-04 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.811×** | -3.4 | 0.029 | 19/44 (SK-MEL-2, HCT15, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.818×** | -3.3 | 0.045 | 17/48 (C32, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.2 | 0.045 | 14/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.821×** | -3.2 | 0.046 | 14/48 (SW 1088, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.5 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 27.8 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -19.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 36.4 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 22.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.89× (z +10.7) | — |
| [[LoVo (line)]] | wt | 29.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 2 (2 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.238× (z -9.4) ⚠ toxic |
| [[A549 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.107× (z -9.1) ⚠ toxic |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 23.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 24.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -9.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.116× (z -12.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTPD5]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MTOR]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[GGA1]] | +0.57 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[ACSF3]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[C5orf22]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[CIAO1]] | +0.55 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[RNF41]] | +0.54 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[CIAO3]] | +0.54 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[EXOC2]] | +0.54 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[NEK4]] | +0.53 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[VPS13D]] | +0.52 | +0.41 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD6]] | -0.54 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[CCDC26]] | -0.54 | -0.29 / -0.44 | both halves | 3e-04 |  |
| [[SORCS3]] | -0.53 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[SLC4A10]] | -0.53 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[MALINC1]] | -0.53 | -0.18 / -0.46 | ⚠ not reproduced | 9e-04 |  |
| [[ESR2]] | -0.53 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[RELN]] | -0.52 | -0.24 / -0.43 | both halves | 5e-04 |  |
| [[LINC01579]] | -0.52 | -0.06 / -0.48 | ⚠ not reproduced | 0.004 |  |
| [[LINC00393]] | -0.51 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[LINC02955]] | -0.51 | -0.17 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[GRM8]] | -0.51 | -0.16 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[SYT16]] | -0.51 | -0.15 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[SLC8A1-AS1]] | -0.50 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[FAM184A]] | -0.50 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[LRP2BP]] | -0.49 | -0.21 / -0.42 | both halves | 7e-04 |  |
| [[DISP3]] | -0.49 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[DIPK2A]] | -0.49 | -0.36 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DNAJC16's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LHFPL6]] | B | LHFPL6 activity raises DNAJC16's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.08× lower at baseline in the lines without LHFPL6 | 0.061 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.4, -30.0); signed map (-18.3, -53.6). **Vector** length 65.6, 11.8% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +12.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +12.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +10.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.1 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.3 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,526,813-15,592,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0962 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G8](https://www.uniprot.org/uniprotkb/Q9Y2G8) (DnaJ homolog subfamily C member 16):

> Plays an important role in regulating the size of autophagosomes during the formation process.

**Summary**, from NCBI Gene [23341](https://www.ncbi.nlm.nih.gov/gene/23341):

> Involved in regulation of autophagosome size. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29157) · Entrez [23341](https://www.ncbi.nlm.nih.gov/gene/23341) · UniProt [Q9Y2G8](https://www.uniprot.org/uniprotkb/Q9Y2G8) · Ensembl [ENSG00000116138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116138)

## Data

Gene col 3766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3766); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3766]; `tensor/DDL_lfc|DDL_z.npy` [3766]; `embed/gene_vectors.npy` [3766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3766 or target_col == 3766). Every well: [[DNAJC16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
