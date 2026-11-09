---
symbol: "NBPF1"
type: "gene"
col: 13297
ensembl_id: "ENSG00000219481"
name: "NBPF member 1"
location: "1p36.13"
module: 30
arm: "+"
pooled_cpm: 16.21
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# NBPF1

*NBPF member 1* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.93× (z +9.4, q 3e-18, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.568× (z -8.0, q 8e-13, down in 31 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 0.674× (z -4.0, q 0.006, down in 15 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF3]] (+0.70, fdr 7e-06), [[TMEM185A]] (+0.67, fdr 7e-06), [[PLD2]] (+0.63, fdr 1e-05); moves opposite to [[SLC20A2]] (-0.57, fdr 3e-05), [[CSNK1A1]] (-0.54, fdr 2e-05), [[TRIP12]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +9.4 | 3e-18 | 39/48 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +7.9 | 9e-13 | 33/48 (HT-29, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +7.7 | 3e-12 | 34/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.7 | 3e-04 | 18/48 (HS-578T, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.25×** | +4.5 | 6e-04 | 23/48 (LOX-IMVI, HCT15, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.4 | 0.001 | 17/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.014 | 14/48 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.043 | 6/46 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.2 | 0.097 | 5/48 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.25× | +3.1 | 0.12 | 9/46 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.24× | +3.0 | 0.12 | 3/48 (HS-578T, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13297.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.568×** | -8.0 | 8e-13 | 31/40 (A-427, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.631×** | -6.2 | 1e-07 | 15/30 (MIA PaCa-2, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.628×** | -6.1 | 2e-07 | 20/36 (Hs 766T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.721×** | -4.6 | 6e-04 | 19/46 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.725×** | -4.5 | 7e-04 | 23/46 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.581×** | -4.0 | 0.006 | 16/48 (MIA PaCa-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.674×** | -4.0 | 0.006 | 15/46 (MIA PaCa-2, HCT15, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.764×** | -3.8 | 0.011 | 21/48 (NCI-H1573, Hs 766T, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.776×** | -3.6 | 0.023 | 17/48 (NCI-H460, SW 1088, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.785×** | -3.4 | 0.036 | 16/48 (MIA PaCa-2, J82, …) | two highest doses |  |
| [[Arbutin (drug)]] 5 µM |  | **0.786×** | -3.3 | 0.057 | 15/46 (CHP-212, SW 900, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.854× | -3.1 | 0.086 | 12/48 (SW480, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 2 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0680× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -10.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 32.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -13.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -10.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 8.58 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0953× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0959× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 7.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.241× (z -9.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0919× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 18.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.118× (z -9.2) |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 | same gene group; STRING 726 |
| [[TMEM185A]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[PLD2]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PRKAB2]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[CNEP1R1]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[UBAC1]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[MRI1]] | +0.59 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[STX7]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TRAF6]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD36B]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CAT]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[UNC119]] | +0.57 | +0.46 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC20A2]] | -0.57 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CSNK1A1]] | -0.54 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TRIP12]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[NFE2L2]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[HCG18]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[COMMD10]] | -0.49 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[P2RY11]] | -0.48 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[TENM3]] | -0.48 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[DNAJB12]] | -0.48 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[ZNF407]] | -0.47 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[CUX1]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.47 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NBPF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.9, -7.9); signed map (-31.1, -8.4). **Vector** length 65.5, 10.3% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +2.4 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.1 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -2.7 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,562,319-16,613,562 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20719, KIAA1693 |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [Q3BBV0](https://www.uniprot.org/uniprotkb/Q3BBV0) carries no function annotation.

**Summary**, from NCBI Gene [55672](https://www.ncbi.nlm.nih.gov/gene/55672):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region …

**Accessions** — [HGNC:26088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26088) · Entrez [55672](https://www.ncbi.nlm.nih.gov/gene/55672) · UniProt [Q3BBV0](https://www.uniprot.org/uniprotkb/Q3BBV0) · Ensembl [ENSG00000219481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000219481)

## Data

Gene col 13297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13297); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13297]; `tensor/DDL_lfc|DDL_z.npy` [13297]; `embed/gene_vectors.npy` [13297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13297 or target_col == 13297). Every well: [[NBPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
