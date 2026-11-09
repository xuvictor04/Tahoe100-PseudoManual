---
symbol: "CCDC150"
type: "gene"
col: 6874
ensembl_id: "ENSG00000144395"
name: "coiled-coil domain containing 150"
location: "2q33.1"
module: 6
arm: "+"
pooled_cpm: 33.61
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CCDC150

*coiled-coil domain containing 150* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.25× (z +15.1, q 0e+00, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.44× (z +6.8, q 1e-09, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.673× (z -10.4, q 9e-23, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCB]] (+0.84, fdr 7e-06), [[BLM]] (+0.84, fdr 7e-06), [[CENPI]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SYTL4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.25×** | +15.1 | 0e+00 | 41/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.00×** | +12.9 | 8e-36 | 40/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.79×** | +10.9 | 3e-25 | 39/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.51×** | +7.7 | 3e-12 | 28/47 (LoVo, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +6.8 | 1e-09 | 29/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +5.6 | 2e-06 | 21/47 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.32×** | +5.2 | 2e-05 | 22/46 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.7 | 1e-04 | 19/47 (A498, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.25×** | +4.1 | 0.003 | 18/45 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.24×** | +3.9 | 0.005 | 17/47 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.7 | 0.012 | 12/47 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.015 | 14/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.21×** | +3.6 | 0.016 | 14/46 (RKO, HT-29, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.21×** | +3.5 | 0.016 | 7/47 (LS 180, RKO, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.024 | 11/47 (HEC-1-A, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.038 | 13/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.038 | 6/47 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.088 | 6/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.12× | +2.9 | 0.093 | 8/47 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.093 | 5/47 (A498, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -10.4 | 9e-23 | 35/47 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.712×** | -8.9 | 1e-16 | 30/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.669×** | -7.5 | 1e-11 | 28/47 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.782×** | -6.5 | 1e-08 | 22/47 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.717×** | -6.2 | 7e-08 | 25/47 (MIA PaCa-2, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.809×** | -5.6 | 2e-06 | 24/47 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -4.7 | 2e-04 | 0/47 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.5 | 5e-04 | 18/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.729×** | -4.2 | 0.002 | 18/47 (SW480, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.652×** | -4.2 | 0.002 | 16/46 (SW480, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.811×** | -3.9 | 0.005 | 16/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.748×** | -3.9 | 0.005 | 15/47 (HOP62, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.817×** | -3.8 | 0.007 | 15/47 (NCI-H2030, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.826×** | -3.5 | 0.016 | 15/47 (A-172, HT-29, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.839× | -3.3 | 0.039 | 9/47 (SW480, NCI-H460, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.782×** | -3.3 | 0.039 | 12/47 (RPMI-7951, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.719×** | -3.2 | 0.043 | 13/47 (SK-MEL-2, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.75 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.8 | 1 (1 ⚠) | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.4) ⚠ cell-cycle shift, explains ~58% of this change | [[Selinexor (drug)]] 5 µM 0.328× (z -15.2) |
| [[H4 (line)]] | wt | 34.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.106× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.264× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.337× (z -10.8) |
| [[A-427 (line)]] | wt | 54.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.351× (z -13.1) |
| [[HOP62 (line)]] | alt | 26.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.5) |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.346× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 59.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 47.5 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.42× (z +8.9) ⚠ cell-cycle shift, explains ~58% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -9.8) |
| [[A-172 (line)]] | wt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -8.8) |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -14.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 1 | — | [[AZD-7648 (drug)]] 5 µM 0.0667× (z -9.3) |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0913× (z -13.7) |
| [[SW48 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.158× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCB]] | +0.84 | +0.78 / +0.86 | both halves | 7e-06 |  |
| [[BLM]] | +0.84 | +0.79 / +0.82 | both halves | 7e-06 |  |
| [[CENPI]] | +0.82 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[POLQ]] | +0.81 | +0.78 / +0.81 | both halves | 7e-06 |  |
| [[PBK]] | +0.81 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[PARPBP]] | +0.80 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[CENPK]] | +0.80 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[MELK]] | +0.80 | +0.77 / +0.81 | both halves | 7e-06 |  |
| [[SKA1]] | +0.80 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[RBL1]] | +0.79 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[SPC24]] | +0.79 | +0.73 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL4]] | B | SYTL4 activity lowers CCDC150's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.34× higher at baseline in the lines without SYTL4 | 0.033 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[KATNAL1]] | B | KATNAL1 activity raises CCDC150's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without KATNAL1 | 0.080 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[PBK]] | C | PBK activity raises CCDC150's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.66× lower at baseline in the lines without PBK | 0.019 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises CCDC150's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.44× lower at baseline in the lines without DSCC1 | 0.023 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.7, -47.2); signed map (-39.0, -41.4). **Vector** length 125, 34.8% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.56 to 65); *DNA strand elongation* (reactome, mean cos +0.58 to 28); *DNA Replication* (reactome, mean cos +0.59 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +4.9 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.2 | +12.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.1 | +15.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.7 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +6.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.0 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -5.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.8 | -8.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.0 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.5 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 150 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:196,639,554-196,763,490 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39660 |
| Matched by | ensembl_id |

UniProt [Q8NCX0](https://www.uniprot.org/uniprotkb/Q8NCX0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26834) · Entrez [284992](https://www.ncbi.nlm.nih.gov/gene/284992) · UniProt [Q8NCX0](https://www.uniprot.org/uniprotkb/Q8NCX0) · Ensembl [ENSG00000144395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144395)

## Data

Gene col 6874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6874); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6874]; `tensor/DDL_lfc|DDL_z.npy` [6874]; `embed/gene_vectors.npy` [6874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6874 or target_col == 6874). Every well: [[CCDC150 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC150.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
