---
symbol: "CHEK1"
type: "gene"
col: 7387
ensembl_id: "ENSG00000149554"
name: "checkpoint kinase 1"
location: "11q24.2"
module: 6
arm: "+"
pooled_cpm: 49.44
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CHEK1

*checkpoint kinase 1* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +14.6, q 3e-45, up in 35 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.05× (z +7.1, q 3e-10, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.755× (z -5.8, q 3e-06, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 0.842× (z -5.3, q 4e-05, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM2]] (+0.82, fdr 7e-06), [[FANCD2]] (+0.80, fdr 7e-06), [[GINS1]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.00×** | +14.6 | 3e-45 | 35/40 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.86×** | +13.5 | 2e-39 | 36/47 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +7.1 | 3e-10 | 28/48 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.42×** | +7.0 | 3e-10 | 26/44 (A-172, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.7 | 2e-09 | 1/48 (SW 1271) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.29×** | +5.6 | 2e-06 | 25/48 (SW480, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +5.1 | 3e-05 | 23/48 (HT-29, RKO, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.27×** | +5.1 | 3e-05 | 23/47 (PANC-1, SW480, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.17× | +4.7 | 2e-04 | 14/48 (Panc 03.27, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.003 | 14/48 (LOX-IMVI, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.13× | +3.8 | 0.008 | 8/49 (HT-29, COLO 205, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.010 | 11/48 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.20× | +3.6 | 0.016 | 5/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.018 | 10/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.4 | 0.028 | 16/48 (J82, RKO, …) | two highest doses | composition shift |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.073 | 7/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7387.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.755×** | -5.8 | 3e-06 | 29/48 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.842× | -5.3 | 4e-05 | 21/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.786×** | -5.1 | 7e-05 | 21/47 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -5.0 | 1e-04 | 20/48 (HOP62, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.796×** | -4.5 | 6e-04 | 23/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.808×** | -4.5 | 6e-04 | 19/48 (A-172, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.826×** | -4.2 | 0.002 | 17/48 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.828×** | -4.1 | 0.002 | 19/48 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.796×** | -3.9 | 0.005 | 14/48 (A-427, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.880× | -3.8 | 0.008 | 14/48 (Hs 766T, A-427, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.848× | -3.6 | 0.016 | 14/48 (HOP62, RKO, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.850× | -3.4 | 0.035 | 11/48 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.716×** | -3.3 | 0.042 | 9/47 (KATO III, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.848× | -3.3 | 0.042 | 15/48 (SW 1271, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.2 | 0.053 | 16/48 (HEC-1-A, SHP-77, …) | inconsistent across doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.903× | -3.1 | 0.058 | 7/48 (Hs 766T, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 106 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.442× (z -10.2) |
| [[PANC-1 (line)]] | alt | 64.1 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.06× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 31.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 77.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | [[Bortezomib (drug)]] 0.05 µM 0.294× (z -10.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 50.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.515× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[AN3 CA (line)]] | alt | 61.6 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.148× (z -9.9) |
| [[CHP-212 (line)]] | wt | 38.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.105× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.139× (z -9.0) |
| [[J82 (line)]] | alt | 53.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +17.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.414× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 53.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 50.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 53.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.328× (z -8.9) |
| [[SNU-423 (line)]] | alt | 32.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SW 1271 (line)]] | alt | 64.7 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0787× (z -9.5) |
| [[SW480 (line)]] | alt | 90.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM2]] | +0.82 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 870 |
| [[FANCD2]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 | pathway: TP53 Regulates Transcription of DNA Repair Genes; STRING 958 |
| [[GINS1]] | +0.79 | +0.74 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 599 |
| [[MCM4]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 978 |
| [[SKA3]] | +0.79 | +0.78 / +0.77 | both halves | 7e-06 | STRING 441 |
| [[POLD3]] | +0.78 | +0.73 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 468 |
| [[NCAPG2]] | +0.77 | +0.73 / +0.82 | both halves | 7e-06 | STRING 635 |
| [[WDHD1]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 | STRING 712 |
| [[ZWINT]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 722 |
| [[EXO1]] | +0.77 | +0.74 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 973 |
| [[PLK4]] | +0.76 | +0.77 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 670 |
| [[ZGRF1]] | +0.76 | +0.77 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CHEK1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.801). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.4, -45.7); signed map (-39.5, -46.2). **Vector** length 122, 33.6% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.65 to 28); *DNA Replication* (reactome, mean cos +0.63 to 40); *E2F G1/S* (control, mean cos +0.63 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +4.9 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +4.3 | +13.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +3.4 | +7.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +2.2 | +1.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.2 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | checkpoint kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,625,163-125,676,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHK1 |
| Gene groups (HGNC) | Checkpoint kinase 1 family |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 28 pathways, smallest: Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex; Transcriptional Regulation by E2F6; Activation of ATR in response to replication stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O14757](https://www.uniprot.org/uniprotkb/O14757) (Serine/threonine-protein kinase Chk1):

> Serine/threonine-protein kinase which is required for checkpoint-mediated cell cycle arrest and activation of DNA repair in response to the presence of DNA damage or unreplicated DNA. May also negatively regulate cell cycle progression during unperturbed cell cycles. This regulation is achieved by a number of mechanisms that together help to preserve the integrity of the genome. Recognizes the substrate consensus sequence [R-X-X-S/T]. Binds to and phosphorylates CDC25A, CDC25B and CDC25C. …

**Summary**, from NCBI Gene [1111](https://www.ncbi.nlm.nih.gov/gene/1111):

> The protein encoded by this gene belongs to the Ser/Thr protein kinase family. It is required for checkpoint mediated cell cycle arrest in response to DNA damage or the presence of unreplicated DNA. This protein acts to integrate signals from ATM and ATR, two cell cycle proteins involved in DNA damage responses, that also associate with chromatin in meiotic prophase I. Phosphorylation of CDC25A protein phosphatase by this protein is required for cells to delay cell cycle progression in response …

**Accessions** — [HGNC:1925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1925) · Entrez [1111](https://www.ncbi.nlm.nih.gov/gene/1111) · UniProt [O14757](https://www.uniprot.org/uniprotkb/O14757) · Ensembl [ENSG00000149554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149554)

## Data

Gene col 7387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7387); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7387]; `tensor/DDL_lfc|DDL_z.npy` [7387]; `embed/gene_vectors.npy` [7387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7387 or target_col == 7387). Every well: [[CHEK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHEK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
