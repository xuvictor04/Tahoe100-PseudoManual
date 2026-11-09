---
symbol: "NAT14"
type: "gene"
col: 1645
ensembl_id: "ENSG00000090971"
name: "N-acetyltransferase 14 (putative)"
location: "19q13.42"
module: 24
arm: "+"
pooled_cpm: 5.0
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NAT14

*N-acetyltransferase 14 (putative)* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +7.1, q 7e-10, up in 20 of 25 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 5.65×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.407× (z -6.5, q 5e-08, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NME3]] (+0.68, fdr 3e-05), [[FLVCR1-DT]] (+0.67, fdr 1e-05), [[HCFC1R1]] (+0.66, fdr 1e-05); moves opposite to [[TTL]] (-0.60, fdr 1e-05), [[ABCF2]] (-0.56, fdr 6e-05), [[PRMT3]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GAMT]] → it (grade B ⚠); 2 go from it, the strongest it → [[DCTN6-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1645.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 5.65×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +7.1 | 7e-10 | 20/25 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +6.1 | 3e-07 | 5/10 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +4.1 | 0.008 | 8/13 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.61×** | +3.5 | 0.071 | 13/37 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.3 | 0.094 | 9/26 (NCI-H1792, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.57×** | +3.3 | 0.094 | 7/21 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.36× | +3.2 | 0.12 | 7/44 (A549, NCI-H23, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.35× | +3.1 | 0.13 | 13/43 (SHP-77, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1645.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.407×** | -6.5 | 5e-08 | 32/43 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.421×** | -5.9 | 9e-07 | 25/40 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.445×** | -5.9 | 9e-07 | 25/44 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.462×** | -5.3 | 2e-05 | 24/41 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.220×** | -5.2 | 2e-05 | 23/34 (NCI-H2030, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.509×** | -4.9 | 1e-04 | 26/43 (SNU-423, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.645×** | -4.5 | 6e-04 | 21/37 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.567×** | -4.1 | 0.003 | 18/42 (H4, HT-29, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.576×** | -3.8 | 0.008 | 20/41 (C32, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.339×** | -3.7 | 0.012 | 18/40 (SHP-77, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.604×** | -3.6 | 0.014 | 17/42 (A-172, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.626×** | -3.4 | 0.032 | 14/34 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.626×** | -3.4 | 0.032 | 17/44 (HT-29, PANC-1, …) | two highest doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.630×** | -3.1 | 0.079 | 8/43 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -3.1 | 0.079 | 17/36 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.418×** | -3.0 | 0.097 | 12/41 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.99 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 6.72 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0815× (z -8.5) |
| [[PANC-1 (line)]] | alt | 7.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.0) |
| [[A-172 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME3]] | +0.68 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[FLVCR1-DT]] | +0.67 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[HCFC1R1]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[LAGE3]] | +0.63 | +0.23 / +0.69 | both halves | 5e-04 |  |
| [[SCRN2]] | +0.62 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[TMEM276]] | +0.62 | +0.38 / +0.65 | both halves | 7e-05 |  |
| [[ATP5PO]] ⚠ | +0.61 | +0.32 / +0.65 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TRIM7-AS2]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[FAM133B]] | +0.61 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[CLN8-AS1]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[DECR2]] | +0.61 | +0.39 / +0.67 | both halves | 6e-05 |  |
| [[SNAPIN]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[AFTPH]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.56 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[PRMT3]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PSME3]] | -0.54 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[HNRNPAB]] | -0.54 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[ZNF731P]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MOB1A]] | -0.53 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[IPO5]] | -0.53 | -0.22 / -0.64 | both halves | 6e-04 |  |
| [[ELK4]] | -0.52 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[NAA50]] | -0.52 | -0.33 / -0.55 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAMT]] | B | GAMT activity raises NAT14's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without GAMT | 0.042 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[FAM229B]] | B | FAM229B activity raises NAT14's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without FAM229B | 0.054 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCTN6-DT]] | C | NAT14 activity lowers DCTN6-DT's level | lines that do not express NAT14 (3) vs lines expressing it (47) | 1.50× higher at baseline in the lines without NAT14 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ODAD4, GGT7, MATN2; maybe low, not absent; its own permutation p |
| [[SUFU]] | C | NAT14 activity raises SUFU's level | lines that do not express NAT14 (3) vs lines expressing it (47) | 1.37× lower at baseline in the lines without NAT14 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ODAD4, GGT7, MATN2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.9, -17.7); signed map (-26.3, 11.2). **Vector** length 46.3, 6.75% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.0 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.1 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | N-acetyltransferase 14 (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,485,188-55,487,568 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KLP1 |
| Gene groups (HGNC) | GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUY8](https://www.uniprot.org/uniprotkb/Q8WUY8) (Probable N-acetyltransferase 14):

> Probable acetyltransferase.; May act as a transcription factor that regulates the expression of coproporphyrinogen oxidase by binding to a promoter regulatory element.

**Summary**, from NCBI Gene [57106](https://www.ncbi.nlm.nih.gov/gene/57106):

> Predicted to enable N-acetyltransferase activity. Predicted to be involved in DNA-templated transcription initiation and positive regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28918) · Entrez [57106](https://www.ncbi.nlm.nih.gov/gene/57106) · UniProt [Q8WUY8](https://www.uniprot.org/uniprotkb/Q8WUY8) · Ensembl [ENSG00000090971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090971)

## Data

Gene col 1645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1645); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1645]; `tensor/DDL_lfc|DDL_z.npy` [1645]; `embed/gene_vectors.npy` [1645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1645 or target_col == 1645). Every well: [[NAT14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAT14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
