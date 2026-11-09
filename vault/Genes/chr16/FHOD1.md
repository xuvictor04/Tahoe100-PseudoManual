---
symbol: "FHOD1"
type: "gene"
col: 5747
ensembl_id: "ENSG00000135723"
name: "formin homology 2 domain containing 1"
location: "16q22.1"
module: 195
arm: "+"
pooled_cpm: 10.14
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# FHOD1

*formin homology 2 domain containing 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.01× (z +8.4, q 3e-14, up in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.83× (z +7.2, q 7e-11, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.651× (z -4.7, q 0.002, down in 16 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 0.5 µM: 0.716× (z -4.1, q 0.014, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.304×, NCI-H23 0.292×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (BT-474 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.180×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHPN1]] (+0.60, fdr 1e-05), [[LPCAT4]] (+0.57, fdr 4e-05), [[PHC2]] (+0.56, fdr 1e-05); moves opposite to [[PDCD6IP-DT]] (-0.50, fdr 1e-04), [[ZXDA]] (-0.48, fdr 7e-05), [[SENP6]] (-0.48, fdr 1e-04).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.01×** | +8.4 | 3e-14 | 33/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.92×** | +7.8 | 2e-12 | 28/47 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.87×** | +7.5 | 1e-11 | 27/47 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +7.2 | 7e-11 | 29/47 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +7.0 | 2e-10 | 26/41 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.63×** | +5.6 | 2e-06 | 21/36 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.62×** | +5.6 | 2e-06 | 9/20 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.1 | 2e-05 | 21/46 (HOP62, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +5.0 | 4e-05 | 15/39 (HOP62, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.73×** | +4.7 | 2e-04 | 20/44 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 16/47 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +4.4 | 6e-04 | 14/39 (LOX-IMVI, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.44×** | +4.4 | 6e-04 | 21/40 (LS 180, NCI-H1573, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +4.1 | 0.002 | 6/36 (NCI-H1573, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.003 | 8/45 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.004 | 14/45 (SNU-423, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.016 | 12/47 (NCI-H460, A-172, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.048 | 2/45 (RKO, A498) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5747.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.304×, NCI-H23 0.292×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (BT-474 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.180×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.651×** | -4.7 | 0.002 | 16/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.716×** | -4.1 | 0.014 | 15/47 (SW48, LS 180, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.735×** | -3.5 | 0.098 | 10/47 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.755× | -3.3 | 0.13 | 18/46 (HCT15, NCI-H1573, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.825× | -3.2 | 0.13 | 17/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.774× | -3.1 | 0.14 | 10/47 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.770× | -3.1 | 0.14 | 14/46 (HOP62, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.819× | -3.0 | 0.14 | 14/48 (NCI-H460, SW 1271, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.808× | -3.0 | 0.14 | 13/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.765× | -3.0 | 0.14 | 8/41 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.180× (z -8.9) |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.89× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHPN1]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.57 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[PHC2]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PGAP6]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[SLCO4A1]] | +0.54 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[TSPAN9]] | +0.53 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[GBA2]] | +0.52 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[KLHL17]] | +0.52 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[ACTN1]] | +0.51 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[STX1A]] | +0.51 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[SPRY4]] | +0.51 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[VAV2]] | +0.51 | +0.57 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6IP-DT]] | -0.50 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ZXDA]] | -0.48 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[SENP6]] | -0.48 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[TOR1AIP1]] | -0.46 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[GTF2IRD2B]] | -0.46 | -0.52 / -0.23 | both halves | 5e-04 |  |
| [[AIMP1]] | -0.45 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[DDX6]] | -0.45 | -0.45 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises FHOD1's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NIBAN2]] | B | NIBAN2 activity raises FHOD1's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without NIBAN2 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[KCNN4]] | B | KCNN4 activity raises FHOD1's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without KCNN4 | 0.093 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.5, 6.0); signed map (-8.2, 52.9). **Vector** length 80.1, 15.9% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +3.7 | +5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +7.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.7 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +4.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +4.0 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | formin homology 2 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,229,387-67,247,481 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FHOS |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y613](https://www.uniprot.org/uniprotkb/Q9Y613) (FH1/FH2 domain-containing protein 1):

> Required for the assembly of F-actin structures, such as stress fibers. Depends on the Rho-ROCK cascade for its activity. Contributes to the coordination of microtubules with actin fibers and plays a role in cell elongation. Acts synergistically with ROCK1 to promote SRC-dependent non-apoptotic plasma membrane blebbing.

**Summary**, from NCBI Gene [29109](https://www.ncbi.nlm.nih.gov/gene/29109):

> This gene encodes a protein which is a member of the formin/diaphanous family of proteins. The gene is ubiquitously expressed but is found in abundance in the spleen. The encoded protein has sequence homology to diaphanous and formin proteins within the Formin Homology (FH)1 and FH2 domains. It also contains a coiled-coil domain, a collagen-like domain, two nuclear localization signals, and several potential PKC and PKA phosphorylation sites. It is a predominantly cytoplasmic protein and is …

**Accessions** — [HGNC:17905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17905) · Entrez [29109](https://www.ncbi.nlm.nih.gov/gene/29109) · UniProt [Q9Y613](https://www.uniprot.org/uniprotkb/Q9Y613) · Ensembl [ENSG00000135723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135723)

## Data

Gene col 5747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5747); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5747]; `tensor/DDL_lfc|DDL_z.npy` [5747]; `embed/gene_vectors.npy` [5747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5747 or target_col == 5747). Every well: [[FHOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
