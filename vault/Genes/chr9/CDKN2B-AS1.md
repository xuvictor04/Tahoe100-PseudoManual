---
symbol: "CDKN2B-AS1"
type: "gene"
col: 14238
ensembl_id: "ENSG00000240498"
name: "CDKN2B and CDKN2A antisense cis and trans regulatory RNA 1"
location: "9p21.3"
module: 68
arm: "+"
pooled_cpm: 19.48
n_lines_expressing: 32
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# CDKN2B-AS1

*CDKN2B and CDKN2A antisense cis and trans regulatory RNA 1* — 9p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.52× (z +3.9, q 0.050, up in 17 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.194× (z -15.8, q 0e+00, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD6-AS1]] (+0.70, fdr 1e-05), [[LINC02889]] (+0.70, fdr 2e-05), [[KANSL1L]] (+0.65, fdr 7e-05); moves opposite to [[ATG4C]] (-0.67, fdr 1e-05), [[HEATR6]] (-0.65, fdr 1e-05), [[MKRN2]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDKN2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CDKN2A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.050 | 17/29 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.050 | 14/29 (HT-29, J82, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **2.05×** | +3.6 | 0.050 | 14/29 (HOP62, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.050 | 12/30 (HOP62, J82, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.97×** | +3.4 | 0.071 | 15/29 (NCI-H1573, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.17 | 13/30 (CFPAC-1, HT-29, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.84× | +3.1 | 0.17 | 12/28 (Hs 766T, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.194×** | -15.8 | 0e+00 | 27/30 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.224×** | -14.4 | 2e-44 | 26/30 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.244×** | -13.6 | 9e-40 | 27/30 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.563×** | -5.5 | 5e-06 | 18/30 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.613×** | -4.7 | 3e-04 | 15/29 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.619×** | -4.4 | 9e-04 | 22/28 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -4.1 | 0.004 | 17/30 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -3.8 | 0.011 | 15/30 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.662×** | -3.8 | 0.011 | 15/29 (COLO 205, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.687×** | -3.6 | 0.018 | 15/28 (RKO, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.491×** | -3.6 | 0.018 | 12/29 (HT-29, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.704×** | -3.4 | 0.034 | 12/29 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.783×** | -3.3 | 0.038 | 11/30 (C32, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.790×** | -3.2 | 0.054 | 12/30 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.726×** | -3.1 | 0.077 | 8/30 (NCI-H661, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 36.5 | 1 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.32× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.158× (z -11.5) |
| [[HT-29 (line)]] | alt | 36.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0791× (z -18.0) |
| [[SW480 (line)]] | alt | 35.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -18.2) |
| [[C32 (line)]] | wt | 33.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -10.7) |
| [[COLO 205 (line)]] | alt | 44.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0922× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -10.6) |
| [[HS-578T (line)]] | alt | 35.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 37.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0807× (z -14.0) |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -10.1) |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -11.5) |
| [[C-33 A (line)]] | alt | 67.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -11.4) |
| [[Hs 766T (line)]] | wt | 28.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -10.0) |
| [[J82 (line)]] | alt | 42.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.174× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 13.1 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.09× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0794× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 6.36 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0873× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.130× (z -8.9) |
| [[A-172 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS1]] | +0.70 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |
| [[LINC02889]] | +0.70 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[KANSL1L]] | +0.65 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[TTC6]] | +0.64 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PCF11]] | +0.63 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[BAZ2B]] | +0.63 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | +0.63 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[AKT1S1]] | +0.62 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CCDC90B-AS1]] | +0.62 | +0.54 / +0.31 | both halves | 2e-04 | same gene group |
| [[PSMD6-AS2]] | +0.61 | +0.57 / +0.37 | both halves | 9e-05 | same gene group |
| [[GGPS1]] | +0.61 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[ASXL2]] | +0.60 | +0.55 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4C]] | -0.67 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[HEATR6]] | -0.65 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[MKRN2]] | -0.65 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ATP7B]] | -0.63 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[WASF3]] | -0.63 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[POMGNT2]] | -0.62 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[HACE1]] | -0.61 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.60 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[MMS19]] | -0.60 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[SNAPC3]] | -0.59 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[RSAD1]] | -0.59 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ELP1]] | -0.59 | -0.55 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKN2A]] | B | CDKN2A activity strengthens CDKN2B-AS1's drug response | lines that do not express CDKN2A (5) vs lines expressing it (25) | the lines without CDKN2A respond 0.44× as strongly (z diff +2.68); strongest at Panobinostat 5 µM: 0.54x vs 0.20x (z diff +5.6) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE; target measured in part of the lines; artifact flags |
| [[CDKN2A]] | C | CDKN2A activity raises CDKN2B-AS1's level | lines that do not express CDKN2A (22) vs lines expressing it (28) | 4.85× lower at baseline in the lines without CDKN2A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKN2A]] | C | CDKN2B-AS1 activity raises CDKN2A's level | lines that do not express CDKN2B-AS1 (18) vs lines expressing it (32) | 7.41× lower at baseline in the lines without CDKN2B-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDKN2A, SLCO6A1, CDKN2B; co-absent with the target |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (13.9, 13.9); signed map (25.5, 1.1). **Vector** length 78.7, 20.1% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -15.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -13.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -14.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -5.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | CDKN2B and CDKN2A antisense cis and trans regulatory RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9p21.3 — chr9:21,994,139-22,128,103 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ANRIL, RP11-145E5.4, NCRNA00089, p15AS, CDKN2B-AS, PCAT12, 66CTG; previously CDKN2BAS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100048912](https://www.ncbi.nlm.nih.gov/gene/100048912):

> This gene is located within the CDKN2B-CDKN2A gene cluster at chromosome 9p21. The gene product is a functional RNA molecule that interacts with polycomb repressive complex-1 (PRC1) and -2 (PRC2), leading to epigenetic silencing of other genes in this cluster. This region is a significant genetic susceptibility locus for cardiovascular disease, and has also been linked to a number of other pathologies, including several cancers, intracranial aneurysm, type-2 diabetes, periodontitis, Alzheimer's …

**Accessions** — [HGNC:34341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34341) · Entrez [100048912](https://www.ncbi.nlm.nih.gov/gene/100048912) · Ensembl [ENSG00000240498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240498)

## Data

Gene col 14238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14238); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14238]; `tensor/DDL_lfc|DDL_z.npy` [14238]; `embed/gene_vectors.npy` [14238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14238 or target_col == 14238). Every well: [[CDKN2B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN2B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
