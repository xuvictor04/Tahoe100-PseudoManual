---
symbol: "HCG11"
type: "gene"
col: 13629
ensembl_id: "ENSG00000228223"
name: "HLA complex group 11"
location: "6p22.2"
module: 88
arm: "+"
pooled_cpm: 5.38
n_lines_expressing: 29
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# HCG11

*HLA complex group 11* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.34× (z +4.4, q 0.005, up in 8 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.242× (z -15.0, q 0e+00, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF747]] (+0.77, fdr 8e-06), [[ZNF764]] (+0.73, fdr 1e-05), [[ZNF181]] (+0.72, fdr 7e-06); moves opposite to [[UQCRH]] (-0.64, fdr 5e-05), [[COG5]] (-0.64, fdr 3e-05), [[WASF3]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C1orf21]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SDHAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +4.4 | 0.005 | 8/25 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.1 | 0.010 | 6/27 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.019 | 4/24 (LoVo, MIA PaCa-2, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.37× | +3.3 | 0.12 | 5/24 (A-427, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.39× | +3.2 | 0.14 | 5/16 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.33× | +3.1 | 0.20 | 3/25 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.48× | +3.0 | 0.20 | 0/20 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.242×** | -15.0 | 0e+00 | 24/26 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.268×** | -13.9 | 2e-41 | 24/27 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.312×** | -12.3 | 2e-32 | 23/27 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -6.7 | 3e-09 | 14/22 (RPMI-7951, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.540×** | -6.5 | 9e-09 | 15/27 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -5.4 | 7e-06 | 15/27 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.605×** | -5.3 | 9e-06 | 11/26 (SW480, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.640×** | -4.7 | 2e-04 | 12/23 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.626×** | -4.7 | 2e-04 | 16/24 (SW480, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.446×** | -4.5 | 5e-04 | 10/15 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.468×** | -4.2 | 0.001 | 14/24 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.686×** | -4.0 | 0.004 | 10/27 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.724×** | -3.4 | 0.031 | 11/27 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.560×** | -3.2 | 0.057 | 6/21 (SW480, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.575×** | -3.1 | 0.085 | 10/25 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.9 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0858× (z -20.4) |
| [[A-427 (line)]] | wt | 10.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -9.7) |
| [[LoVo (line)]] | wt | 12.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.144× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -13.4) |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -9.5) |
| [[A549 (line)]] | wt | 8.42 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -8.6) |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.102× (z -8.7) |
| [[Hs 766T (line)]] | wt | 5.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0820× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 7.70 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0994× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 4.43 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -8.9) |
| [[SW 900 (line)]] | alt | 9.90 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0151× (z -18.2) |
| [[A-172 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.541 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF747]] | +0.77 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[ZNF764]] | +0.73 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.72 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[METTL18]] | +0.70 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ST7L]] | +0.70 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.69 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[INO80D]] | +0.69 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ZNF518A]] | +0.69 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.68 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LIG4]] | +0.68 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.67 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZNF155]] | +0.67 | +0.60 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.64 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[COG5]] | -0.64 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[WASF3]] | -0.64 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.63 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[SDHAP1]] | -0.63 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[RPA1]] | -0.63 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[RGS10]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.61 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[QSOX1]] | -0.61 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[C1orf21]] | -0.60 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[SDHAP2]] | -0.60 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[TMEM120B]] | -0.60 | -0.52 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf21]] | B | C1orf21 activity lowers HCG11's level | lines that do not express C1orf21 (9) vs lines expressing it (41) | 2.11× higher at baseline in the lines without C1orf21 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, GALNT8 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP1]] | B | HCG11 activity raises SDHAP1's level | lines that do not express HCG11 (21) vs lines expressing it (29) | 1.14× lower at baseline in the lines without HCG11 | 0.061 | ⚠ within organs, on part of the lines; also absent: HEYL, GAL, PDLIM4 |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-29.1, 9.1); signed map (8.1, -20.7). **Vector** length 50.7, 10.2% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.2 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.1 | -12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -13.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -15.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | HLA complex group 11 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p22.2 — chr6:26,521,709-26,527,404 (+) |
| Ensembl biotype | lncRNA |
| Also known as | bK14H9.3, FLJ14049, FLJ30357 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:17707](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17707) · Entrez [493812](https://www.ncbi.nlm.nih.gov/gene/493812) · Ensembl [ENSG00000228223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228223)

## Data

Gene col 13629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13629); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13629]; `tensor/DDL_lfc|DDL_z.npy` [13629]; `embed/gene_vectors.npy` [13629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13629 or target_col == 13629). Every well: [[HCG11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCG11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
