---
symbol: "MC1R"
type: "gene"
col: 15144
ensembl_id: "ENSG00000258839"
name: "melanocortin 1 receptor"
location: "16q24.3"
module: 181
arm: "+"
pooled_cpm: 6.35
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# MC1R

*melanocortin 1 receptor* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +4.5, q 0.004, up in 15 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.472× (z -8.1, q 3e-13, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKT1S1]] (+0.72, fdr 7e-06), [[NLGN3]] (+0.72, fdr 7e-06), [[ZCWPW1]] (+0.71, fdr 2e-05); moves opposite to [[SLC35A1]] (-0.62, fdr 1e-05), [[GCSH]] (-0.62, fdr 2e-04), [[ARL6]] (-0.61, fdr 4e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPOCK2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.5 | 0.004 | 15/42 (NCI-H1792, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.7 | 0.062 | 5/19 (SW1417, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 1.37× | +3.4 | 0.11 | 5/46 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.39× | +3.4 | 0.11 | 3/12 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 1.79× | +3.3 | 0.11 | 4/45 (HOP62, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.34× | +3.0 | 0.22 | 7/29 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.472×** | -8.1 | 3e-13 | 30/45 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.510×** | -7.3 | 1e-10 | 26/40 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.528×** | -6.9 | 1e-09 | 28/46 (SNU-423, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.562×** | -6.2 | 7e-08 | 25/46 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.598×** | -5.5 | 3e-06 | 19/44 (A-427, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.623×** | -5.1 | 3e-05 | 22/43 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.417×** | -4.9 | 6e-05 | 19/43 (HT-29, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.636×** | -4.9 | 8e-05 | 21/44 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -4.8 | 1e-04 | 13/47 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -4.3 | 9e-04 | 16/45 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -3.9 | 0.006 | 15/41 (A549, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.708×** | -3.7 | 0.009 | 16/42 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.550×** | -3.4 | 0.033 | 6/44 (HCT15, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 0.755× | -3.0 | 0.10 | 7/41 (SNU-1, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.31 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0797× (z -12.1) |
| [[C32 (line)]] | wt | 8.95 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0895× (z -9.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 5.82 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0896× (z -8.5) |
| [[KATO III (line)]] | alt | 7.54 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0877× (z -9.2) |
| [[LoVo (line)]] | wt | 5.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 7.87 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0603× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 9.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0774× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 4.60 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0859× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.137× (z -8.5) |
| [[SW1417 (line)]] | alt | 5.21 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0742× (z -10.1) |
| [[A498 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1S1]] | +0.72 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.72 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZCWPW1]] | +0.71 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[CCDC17]] | +0.69 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SLC9A5]] | +0.68 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[YJEFN3]] | +0.68 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[MEPCE]] | +0.68 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[PARD6G-AS1]] | +0.68 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[GPR137]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PTOV1-AS1]] | +0.67 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PIPOX]] | +0.66 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[PCBP1-AS1]] | +0.66 | +0.60 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A1]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[GCSH]] | -0.62 | -0.66 / -0.31 | both halves | 2e-04 |  |
| [[ARL6]] | -0.61 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ATG4C]] | -0.60 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SDHAF3]] | -0.60 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[MRPS31P5-1]] | -0.59 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[LSM2]] | -0.58 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.58 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[SLC9A6]] | -0.58 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[MALSU1]] | -0.57 | -0.48 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCK2]] | B | SPOCK2 activity raises MC1R's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without SPOCK2 | 0.043 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[MPP4]] | C | MPP4 activity raises MC1R's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | MC1R's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | MC1R's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.449 over the table, 0.049 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.7, -13.5); signed map (18.7, 4.1). **Vector** length 57.4, 7.94% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.4 | -8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.0 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.3 | -6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | melanocortin 1 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,912,119-89,920,973 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSH-R |
| Gene groups (HGNC) | Melanocortin receptors |
| Reactome | 8 pathways, smallest: Transcriptional and post-translational regulation of MITF-M expression and activity; Peptide ligand-binding receptors; G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01726](https://www.uniprot.org/uniprotkb/Q01726) (Melanocyte-stimulating hormone receptor):

> G protein-coupled receptor that binds melanocyte-stimulating hormones (alpha, beta, and gamma-MSH) and adrenocorticotropic hormone/ACTH, which are peptide products of the POMC precursor protein. Upon activation, MC1R couples with the G(s) protein, stimulating adenylate cyclase and activating the cAMP-dependent signaling pathway. This activation promotes melanogenesis, resulting in the production of eumelanin (black/brown) and pheomelanin (red/yellow) in melanocytes. MC1R interacts with G …

**Summary**, from NCBI Gene [4157](https://www.ncbi.nlm.nih.gov/gene/4157):

> This intronless gene encodes the receptor protein for melanocyte-stimulating hormone (MSH). The encoded protein, a seven pass transmembrane G protein coupled receptor, controls melanogenesis. Two types of melanin exist: red pheomelanin and black eumelanin. Gene mutations that lead to a loss in function are associated with increased pheomelanin production, which leads to lighter skin and hair color. Eumelanin is photoprotective but pheomelanin may contribute to UV-induced skin damage by …

**Accessions** — [HGNC:6929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6929) · Entrez [4157](https://www.ncbi.nlm.nih.gov/gene/4157) · UniProt [Q01726](https://www.uniprot.org/uniprotkb/Q01726) · Ensembl [ENSG00000258839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258839)

## Data

Gene col 15144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15144); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15144]; `tensor/DDL_lfc|DDL_z.npy` [15144]; `embed/gene_vectors.npy` [15144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15144 or target_col == 15144). Every well: [[MC1R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MC1R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
