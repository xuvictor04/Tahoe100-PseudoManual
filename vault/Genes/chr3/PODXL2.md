---
symbol: "PODXL2"
type: "gene"
col: 3568
ensembl_id: "ENSG00000114631"
name: "podocalyxin like 2"
location: "3q21.3"
module: 176
arm: "+"
pooled_cpm: 8.84
n_lines_expressing: 36
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 27
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# PODXL2

*podocalyxin like 2* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.06× (z +13.6, q 4e-39, up in 14 of 14 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.66× (z +7.2, q 4e-11, up in 26 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.367× (z -14.2, q 3e-43, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLB1L2]] (+0.79, fdr 7e-06), [[AIF1L]] (+0.78, fdr 7e-06), [[C20orf27]] (+0.73, fdr 1e-05); moves opposite to [[ATE1OSP]] (-0.70, fdr 4e-05), [[CCDC122]] (-0.67, fdr 1e-04), [[CCDC59]] (-0.64, fdr 1e-04).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CELSR2]] → it (grade B ⚠); 27 go from it, the strongest it → [[GGCT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.06×** | +13.6 | 4e-39 | 14/14 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.83×** | +13.5 | 4e-39 | 22/23 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.26×** | +11.0 | 8e-26 | 17/17 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.44×** | +9.0 | 5e-17 | 26/33 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.23×** | +8.1 | 9e-14 | 26/33 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +7.5 | 5e-12 | 22/34 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +7.2 | 4e-11 | 26/33 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.95×** | +6.7 | 2e-09 | 24/33 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.53×** | +4.3 | 0.001 | 14/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.2 | 0.001 | 6/14 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.002 | 10/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +3.8 | 0.006 | 12/33 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.45×** | +3.8 | 0.007 | 10/27 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.367×** | -14.2 | 3e-43 | 27/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.321×** | -11.4 | 1e-27 | 28/30 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.322×** | -11.0 | 1e-25 | 28/31 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.482×** | -7.3 | 3e-11 | 23/32 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.560×** | -5.8 | 6e-07 | 20/33 (NCI-H460, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.558×** | -5.5 | 3e-06 | 18/31 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.743×** | -4.2 | 0.002 | 17/33 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.662×** | -4.1 | 0.002 | 15/33 (SNU-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -4.1 | 0.003 | 19/33 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.700×** | -3.6 | 0.020 | 14/31 (NCI-H460, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -3.5 | 0.026 | 13/33 (LoVo, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.709×** | -3.5 | 0.026 | 15/33 (AN3 CA, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.528×** | -3.4 | 0.034 | 12/30 (MIA PaCa-2, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.32 | 4 (4 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0374× (z -28.8) |
| [[NCI-H460 (line)]] | wt | 9.53 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 6.23× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 27.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.60 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 8.95× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.5) |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0649× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.111× (z -9.9) |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -16.6) |
| [[C-33 A (line)]] | alt | 8.57 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0578× (z -9.4) |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -14.0) |
| [[KATO III (line)]] | alt | 23.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -9.1) |
| [[LS 180 (line)]] | wt | 27.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -9.6) |
| [[RKO (line)]] | wt | 17.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -9.7) |
| [[A-427 (line)]] | wt | 23.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -11.9) |
| [[A498 (line)]] | wt | 4.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0613× (z -12.2) |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -11.6) |
| [[LoVo (line)]] | wt | 8.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 5.95 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 9.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -13.5) |
| [[SHP-77 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 6.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -11.1) |
| [[SW48 (line)]] | wt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0416× (z -12.5) |
| [[SW480 (line)]] | alt | 8.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -12.1) |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.758 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1L2]] | +0.79 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[AIF1L]] | +0.78 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[C20orf27]] | +0.73 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[PARP1]] | +0.71 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[METAP1]] | +0.71 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MEST]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CGREF1]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[HPSE]] | +0.69 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ASIC1]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[AHCY]] | +0.67 | +0.64 / +0.59 | both halves | 7e-06 | pathway: Biological oxidations |
| [[PPAT]] | +0.67 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[LRRC20]] | +0.67 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1OSP]] | -0.70 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[CCDC122]] | -0.67 | -0.64 / -0.34 | both halves | 1e-04 |  |
| [[CCDC59]] | -0.64 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[ZNF181]] | -0.63 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[KRCC1]] | -0.63 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.63 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[SNRNP27]] | -0.62 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | -0.62 | -0.56 / -0.26 | both halves | 4e-04 |  |
| [[ZNF764]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[THAP2]] | -0.62 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[N4BP2L2]] | -0.62 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[UBXN4]] | -0.62 | -0.64 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR2]] | B | CELSR2 activity raises PODXL2's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.86× lower at baseline in the lines without CELSR2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[FZD4]] | B | FZD4 activity raises PODXL2's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 2.12× lower at baseline in the lines without FZD4 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADGRL1]] | B | ADGRL1 activity raises PODXL2's level | lines that do not express ADGRL1 (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without ADGRL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3BP5, DSCC1, NDC80; maybe low, not absent; its own permutation p |
| [[CKMT1A]] | B | CKMT1A activity raises PODXL2's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without CKMT1A | 0.095 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |
| [[AIF1L]] | B | AIF1L activity raises PODXL2's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.77× lower at baseline in the lines without AIF1L | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GGCT]] | B | PODXL2 activity raises GGCT's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without PODXL2 | 0.001 | ⚠ within organs, on part of the lines |
| [[POLD2]] | B | PODXL2 activity raises POLD2's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without PODXL2 | 0.001 | ⚠ within organs, on part of the lines |
| [[NME6]] | B | PODXL2 activity raises NME6's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without PODXL2 | 0.003 | ⚠ within organs, on part of the lines |
| [[PPAT]] | B | PODXL2 activity raises PPAT's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without PODXL2 | 0.005 | ⚠ within organs, on part of the lines |
| [[CGREF1]] | B | PODXL2 activity raises CGREF1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without PODXL2 | 0.018 | ⚠ within organs, on part of the lines |
| [[EXOSC5]] | B | PODXL2 activity raises EXOSC5's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.52× lower at baseline in the lines without PODXL2 | 0.019 | ⚠ within organs, on part of the lines |
| [[GUSB]] | B | PODXL2 activity raises GUSB's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without PODXL2 | 0.020 | ⚠ within organs, on part of the lines |
| [[GTPBP3]] | B | PODXL2 activity raises GTPBP3's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without PODXL2 | 0.020 | ⚠ within organs, on part of the lines |
| [[KIF9-AS1]] | B | PODXL2 activity raises KIF9-AS1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without PODXL2 | 0.022 | ⚠ within organs, on part of the lines |
| [[CDCA7L]] | B | PODXL2 activity raises CDCA7L's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without PODXL2 | 0.024 | ⚠ within organs, on part of the lines |
| [[C20orf27]] | B | PODXL2 activity raises C20orf27's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.56× lower at baseline in the lines without PODXL2 | 0.035 | ⚠ within organs, on part of the lines |
| [[RBBP7]] | B | PODXL2 activity raises RBBP7's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without PODXL2 | 0.037 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.6, 41.3); signed map (-7.6, -57.1). **Vector** length 70.2, 15.7% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.1 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.7 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.2 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | +0.9 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -11.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -14.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | podocalyxin like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:127,629,185-127,672,802 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PODLX2, endoglycan, EG |
| Reactome | 3 pathways, smallest: Cytosolic sulfonation of small molecules; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ53](https://www.uniprot.org/uniprotkb/Q9NZ53) (Podocalyxin-like protein 2):

> Acts as a ligand for vascular selectins. Mediates rapid rolling of leukocytes over vascular surfaces through high affinity divalent cation-dependent interactions with E-, P- and L-selectins.

**Summary**, from NCBI Gene [50512](https://www.ncbi.nlm.nih.gov/gene/50512):

> This gene is a member of the CD34 family of cell surface transmembrane proteins, which are characterized by an N-terminal extracellular mucin domain, globular and stalk domains, a single pass transmembrane region, and a charged cytoplasmic tail. The encoded protein is a ligand for vascular selectins. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:17936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17936) · Entrez [50512](https://www.ncbi.nlm.nih.gov/gene/50512) · UniProt [Q9NZ53](https://www.uniprot.org/uniprotkb/Q9NZ53) · Ensembl [ENSG00000114631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114631)

## Data

Gene col 3568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3568); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3568]; `tensor/DDL_lfc|DDL_z.npy` [3568]; `embed/gene_vectors.npy` [3568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3568 or target_col == 3568). Every well: [[PODXL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PODXL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
