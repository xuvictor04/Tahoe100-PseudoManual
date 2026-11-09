---
symbol: "UHRF1"
type: "gene"
col: 15865
ensembl_id: "ENSG00000276043"
name: "ubiquitin like with PHD and ring finger domains 1"
location: "19p13.3"
module: 6
arm: "+"
pooled_cpm: 8.89
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# UHRF1

*ubiquitin like with PHD and ring finger domains 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +8.4, q 3e-14, up in 20 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.69× (z +5.0, q 7e-05, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.516× (z -8.9, q 3e-16, down in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.522× (z -6.2, q 1e-07, down in 24 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F1]] (+0.87, fdr 7e-06), [[CDC25A]] (+0.86, fdr 7e-06), [[CDC45]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.41×** | +8.4 | 3e-14 | 20/30 (SNU-423, NCI-H2347, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **2.23×** | +7.1 | 4e-10 | 12/18 (SW480, SW1417, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.94×** | +6.1 | 2e-07 | 11/15 (NCI-H2347, BT-474, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.0 | 7e-05 | 21/43 (NCI-H460, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.64×** | +4.7 | 3e-04 | 16/45 (A-427, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~91% of this change | **1.60×** | +4.3 | 0.002 | 16/32 (SW480, SHP-77, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.54×** | +4.1 | 0.003 | 17/43 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.34×** | +3.9 | 0.006 | 12/46 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +3.5 | 0.034 | 12/45 (LoVo, H4, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.036 | 14/43 (LS 180, C32, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.28×** | +3.3 | 0.044 | 11/46 (HT-29, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +3.2 | 0.052 | 9/45 (SNU-423, HCT15, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.41×** | +3.2 | 0.052 | 8/44 (SW480, SNU-423, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.39×** | +3.1 | 0.067 | 7/42 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +3.0 | 0.094 | 9/44 (NCI-H2030, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.516×** | -8.9 | 3e-16 | 33/46 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.619×** | -6.5 | 3e-08 | 22/45 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -6.2 | 1e-07 | 24/40 (A-427, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.533×** | -6.0 | 3e-07 | 22/42 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.519×** | -5.9 | 4e-07 | 20/42 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.584×** | -5.3 | 1e-05 | 25/46 (A-427, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.580×** | -5.2 | 2e-05 | 23/46 (SW480, KATO III, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.591×** | -5.0 | 4e-05 | 17/44 (A498, HEC-1-A, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.635×** | -4.3 | 9e-04 | 15/45 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.532×** | -4.3 | 1e-03 | 15/46 (MIA PaCa-2, RPMI-7951, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.629×** | -4.3 | 0.001 | 18/42 (HEC-1-A, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.683×** | -4.2 | 0.001 | 18/46 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.650×** | -4.1 | 0.002 | 18/45 (RKO, NCI-H23, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.738×** | -4.1 | 0.002 | 21/46 (CHP-212, HCT15, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.642×** | -4.1 | 0.002 | 20/41 (A-172, HT-29, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.696×** | -3.9 | 0.003 | 15/43 (A-427, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.448×** | -3.9 | 0.003 | 11/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.658×** | -3.8 | 0.004 | 18/43 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.459×** | -3.8 | 0.005 | 11/40 (A-427, HEC-1-A, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.679×** | -3.6 | 0.011 | 15/40 (KATO III, NCI-H23, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.34 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 23.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.7) |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 2 | — | [[Orlistat (drug)]] 0.05 µM 0.0697× (z -10.8) |
| [[LS 180 (line)]] | wt | 6.90 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -8.8) |
| [[SW480 (line)]] | alt | 14.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -11.2) |
| [[H4 (line)]] | wt | 9.45 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0520× (z -8.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0406× (z -10.4) |
| [[KATO III (line)]] | alt | 7.62 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0232× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.102× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0684× (z -14.0) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F1]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | STRING 538 |
| [[CDC25A]] | +0.86 | +0.82 / +0.89 | both halves | 7e-06 | STRING 473 |
| [[CDC45]] | +0.86 | +0.84 / +0.87 | both halves | 7e-06 | STRING 615 |
| [[MCM4]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | STRING 602 |
| [[MCM3]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | STRING 655 |
| [[WDR76]] | +0.85 | +0.82 / +0.88 | both halves | 7e-06 | STRING 525 |
| [[MCM10]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | STRING 588 |
| [[POLE]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | STRING 425 |
| [[E2F2]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 | STRING 507 |
| [[FANCA]] | +0.84 | +0.83 / +0.85 | both halves | 7e-06 |  |
| [[XRCC2]] | +0.83 | +0.80 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises UHRF1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without E2F2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises UHRF1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.83× lower at baseline in the lines without CDC25A | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises UHRF1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib) | 62% of the class's compounds vs 6.7% of all compounds | 0.044 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ZNF367]] | C | ZNF367 activity raises UHRF1's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.88× lower at baseline in the lines without ZNF367 | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent; co-absent with the target |
| [[DSCC1]] | C | DSCC1 activity raises UHRF1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.39× lower at baseline in the lines without DSCC1 | 0.096 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.848). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.5, -44.0); signed map (-37.3, -46.0). **Vector** length 119, 32.0% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *DNA strand elongation* (reactome, mean cos +0.69 to 28); *DNA Replication* (reactome, mean cos +0.68 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +5.0 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +4.1 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~91% of this change | +4.0 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +1.5 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.3 | -8.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.2 | -6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.1 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.9 | -6.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.2 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like with PHD and ring finger domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,903,080-4,962,154 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ICBP90, Np95, FLJ21925, RNF106, TDRD22 |
| Gene groups (HGNC) | Ring finger proteins; PHD finger proteins; Tudor domain containing; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 4 pathways, smallest: DNA methylation; Chromatin modifications during the maternal to zygotic transition (MZT); Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T88](https://www.uniprot.org/uniprotkb/Q96T88) (E3 ubiquitin-protein ligase UHRF1):

> E3 ubiquitin-protein ligase that acts as a key epigenetic regulator by bridging DNA methylation and chromatin modification. Plays a key role in DNA methylation inheritance by promoting recruitment of DNMT1 to hemimethylated DNA and ensure faithful propagation of the DNA methylation patterns through DNA replication. Acts both as a histone reader and writer: specifically recognizes and binds (1) hemimethylated DNA at replication forks and (2) histone H3 trimethylated at 'Lys-9' and unmethylated …

**Summary**, from NCBI Gene [29128](https://www.ncbi.nlm.nih.gov/gene/29128):

> This gene encodes a member of a subfamily of RING-finger type E3 ubiquitin ligases. The protein binds to specific DNA sequences, and recruits a histone deacetylase to regulate gene expression. Its expression peaks at late G1 phase and continues during G2 and M phases of the cell cycle. It plays a major role in the G1/S transition by regulating topoisomerase IIalpha and retinoblastoma gene expression, and functions in the p53-dependent DNA damage checkpoint. It is regarded as a hub protein for …

**Accessions** — [HGNC:12556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12556) · Entrez [29128](https://www.ncbi.nlm.nih.gov/gene/29128) · UniProt [Q96T88](https://www.uniprot.org/uniprotkb/Q96T88) · Ensembl [ENSG00000276043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276043)

## Data

Gene col 15865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15865); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15865]; `tensor/DDL_lfc|DDL_z.npy` [15865]; `embed/gene_vectors.npy` [15865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15865 or target_col == 15865). Every well: [[UHRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UHRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
