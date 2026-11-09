---
symbol: "KCNG1"
type: "gene"
col: 372
ensembl_id: "ENSG00000026559"
name: "potassium voltage-gated channel modifier subfamily G member 1"
location: "20q13.13"
module: 211
arm: "+"
pooled_cpm: 6.28
n_lines_expressing: 32
n_dd_up: 34
n_dd_down: 10
n_dd_up_clean: 23
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# KCNG1

*potassium voltage-gated channel modifier subfamily G member 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.16× (z +8.5, q 1e-14, up in 20 of 29 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.61× (z +7.4, q 2e-11, up in 17 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.438× (z -12.9, q 2e-35, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPAR3]] (+0.62, fdr 1e-05), [[ST6GALNAC4]] (+0.61, fdr 8e-05), [[PACC1]] (+0.60, fdr 2e-05); moves opposite to [[CDKN1B]] (-0.53, fdr 3e-05), [[CHD3]] (-0.53, fdr 1e-04), [[ATOSA]] (-0.50, fdr 7e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[OSBPL6]] → it (grade B ⚠); 6 go from it, the strongest it → [[OSBPL6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.16×** | +8.5 | 1e-14 | 20/29 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.13×** | +8.3 | 2e-14 | 19/29 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.99×** | +7.5 | 8e-12 | 20/29 (SNU-423, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +7.4 | 2e-11 | 17/28 (SW480, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.91×** | +7.1 | 1e-10 | 20/29 (A549, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +5.6 | 2e-06 | 15/29 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.64×** | +5.5 | 4e-06 | 12/29 (NCI-H460, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 2e-05 | 11/29 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +5.0 | 4e-05 | 10/27 (NCI-H460, HOP62, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.57×** | +5.0 | 4e-05 | 14/27 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.60×** | +4.9 | 4e-05 | 10/27 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +4.9 | 5e-05 | 15/27 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.56×** | +4.9 | 5e-05 | 15/29 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +4.6 | 1e-04 | 10/29 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **1.34×** | +4.5 | 3e-04 | 12/29 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.75×** | +4.4 | 4e-04 | 7/26 (NCI-H460, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.002 | 6/29 (NCI-H460, HOP62, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.002 | 6/25 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.98×** | +3.9 | 0.003 | 8/25 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.007 | 10/27 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.438×** | -12.9 | 2e-35 | 25/27 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -8.9 | 1e-16 | 16/24 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -7.1 | 3e-10 | 16/25 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.535×** | -6.7 | 4e-09 | 16/28 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.318×** | -6.6 | 4e-09 | 17/27 (PANC-1, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -5.1 | 3e-05 | 16/24 (LOX-IMVI, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.647×** | -4.8 | 1e-04 | 12/28 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.657×** | -4.7 | 2e-04 | 15/29 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -4.0 | 0.004 | 9/28 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -3.6 | 0.016 | 15/27 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.12 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -10.9) |
| [[H4 (line)]] | wt | 17.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0765× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 3.78 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0645× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -15.0) |
| [[SW 900 (line)]] | alt | 4.78 | 0 | 2 | — | [[Nafamostat (mesylate) (drug)]] 0.05 µM 0.0599× (z -8.9) |
| [[A498 (line)]] | wt | 4.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.0) |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 1 | — | [[LJI308 (drug)]] 0.5 µM 0.0474× (z -8.6) |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.4) |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -9.2) |
| [[J82 (line)]] | alt | 5.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 22.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -11.6) |
| [[SW480 (line)]] | alt | 3.53 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -9.1) |
| [[A-172 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.528 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPAR3]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.61 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[PACC1]] | +0.60 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ANKS6]] | +0.60 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[ABCC10]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[KIF21B]] | +0.57 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[LINC02693]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TRABD]] | +0.57 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[TBC1D16]] | +0.56 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[CHST10]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TMEM241]] | +0.55 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[LYPLA1]] | +0.55 | +0.54 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN1B]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CHD3]] | -0.53 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ATOSA]] | -0.50 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[FYB1]] | -0.50 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[RBKS]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RARG]] | -0.49 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[SPART-AS1]] | -0.48 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[PAXIP1-AS2]] | -0.48 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[HOXC9]] | -0.48 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | -0.48 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[RBM48]] | -0.48 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[AHI1-DT]] | -0.48 | -0.33 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL6]] | B | OSBPL6 activity raises KCNG1's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 2.61× lower at baseline in the lines without OSBPL6 | 0.012 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[HOXC9]] | B | HOXC9 activity raises KCNG1's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without HOXC9 | 0.093 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2 |
| [[CRMP1]] | C | CRMP1 activity raises KCNG1's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 3.40× lower at baseline in the lines without CRMP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent; co-absent with the target |
| [[GNAO1]] | C | GNAO1 activity raises KCNG1's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 3.21× lower at baseline in the lines without GNAO1 | 0.079 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL6]] | B | KCNG1 activity raises OSBPL6's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 3.25× lower at baseline in the lines without KCNG1 | 0.029 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| [[HOXC9]] | B | KCNG1 activity raises HOXC9's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 2.96× lower at baseline in the lines without KCNG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| [[LINC02693]] | B | KCNG1 activity raises LINC02693's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without KCNG1 | 0.045 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| [[NBPF9]] | B | KCNG1 activity raises NBPF9's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 1.59× lower at baseline in the lines without KCNG1 | 0.065 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| cells under [[Balsalazide (sodium hydrate) (drug)]] 5 µM | B | KCNG1 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express KCNG1 (18) vs lines expressing it (30) | the lines without KCNG1: 0.90× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| [[TRABD]] | B | KCNG1 activity lowers TRABD's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 1.48× higher at baseline in the lines without KCNG1 | 0.090 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.2, -24.3); signed map (-42.0, -8.8). **Vector** length 65.9, 14.2% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.3 | +8.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.2 | +7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -12.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel modifier subfamily G member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:51,003,656-51,023,107 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv6.1, kH2, K13; previously KCNG |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIX4](https://www.uniprot.org/uniprotkb/Q9UIX4) (Voltage-gated potassium channel regulatory subunit KCNG1):

> Regulatory alpha-subunit of the voltage-gated potassium (Kv) channel which, when coassembled with KCNB1 or KCNB2, can modulate their expression and their gating kinetics by acting on deactivation upon repolarization and inactivation during maintained depolarization. Potassium channel subunit that does not form functional channels by itself.

**Summary**, from NCBI Gene [3755](https://www.ncbi.nlm.nih.gov/gene/3755):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a member of the potassium channel, voltage-gated, subfamily G. This gene is abundantly expressed in skeletal muscle. Multiple …

**Accessions** — [HGNC:6248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6248) · Entrez [3755](https://www.ncbi.nlm.nih.gov/gene/3755) · UniProt [Q9UIX4](https://www.uniprot.org/uniprotkb/Q9UIX4) · Ensembl [ENSG00000026559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000026559)

## Data

Gene col 372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 372); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 372]; `tensor/DDL_lfc|DDL_z.npy` [372]; `embed/gene_vectors.npy` [372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 372 or target_col == 372). Every well: [[KCNG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
