---
symbol: "ORC6"
type: "gene"
col: 1674
ensembl_id: "ENSG00000091651"
name: "origin recognition complex subunit 6"
location: "16q11.2"
module: 6
arm: "+"
pooled_cpm: 26.88
n_lines_expressing: 49
n_dd_up: 34
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ORC6

*origin recognition complex subunit 6* — 16q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (27 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +13.3, q 1e-37, up in 44 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.93× (z +7.3, q 2e-11, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.721× (z -5.1, q 2e-04, down in 26 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.752× (z -4.5, q 0.002, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLSPN]] (+0.84, fdr 7e-06), [[WDR62]] (+0.84, fdr 7e-06), [[CHAF1A]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 27 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 27 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.33×** | +13.3 | 1e-37 | 44/46 (A549, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **2.23×** | +8.9 | 1e-16 | 42/46 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **2.23×** | +8.9 | 1e-16 | 41/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.08×** | +8.1 | 5e-14 | 42/47 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.07×** | +8.1 | 7e-14 | 29/42 (SK-MEL-2, HCT15, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **2.02×** | +7.8 | 7e-13 | 38/47 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **2.07×** | +7.8 | 7e-13 | 31/43 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.93×** | +7.3 | 2e-11 | 38/46 (SW480, HOP62, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.95×** | +7.1 | 7e-11 | 23/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.56×** | +7.0 | 1e-10 | 29/47 (C32, A549, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.93×** | +7.0 | 1e-10 | 36/47 (HOP62, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +6.7 | 1e-09 | 33/46 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.81×** | +6.6 | 2e-09 | 32/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | **1.83×** | +6.5 | 4e-09 | 35/46 (J82, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.83×** | +6.5 | 4e-09 | 34/46 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +5.8 | 2e-07 | 28/46 (NCI-H460, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.1 | 1e-05 | 25/47 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.002 | 22/47 (PANC-1, BT-474, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.29×** | +2.8 | 0.082 | 13/47 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +2.8 | 0.082 | 20/47 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.721×** | -5.1 | 2e-04 | 26/47 (A498, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.658×** | -4.6 | 0.001 | 24/47 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.752×** | -4.5 | 0.002 | 27/47 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.730×** | -3.5 | 0.061 | 18/46 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.682×** | -3.4 | 0.061 | 17/47 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -3.4 | 0.061 | 20/47 (A-172, J82, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.543×** | -3.3 | 0.081 | 21/46 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 0.753× | -3.1 | 0.11 | 16/47 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.560× | -3.1 | 0.11 | 15/47 (SHP-77, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.565× | -3.1 | 0.11 | 13/47 (SW480, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.801× | -3.1 | 0.11 | 15/47 (NCI-H661, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.12 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.8 | 5 (4 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.57× (z +10.7) ⚠ toxic; cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +8.7) | — |
| [[A498 (line)]] | wt | 38.1 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.233× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.288× (z -10.0) |
| [[A549 (line)]] | wt | 17.9 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +12.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 15.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 22.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.358× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0225× (z -14.8) |
| [[HS-578T (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 9.16 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.350× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 15.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +9.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.326× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLSPN]] | +0.84 | +0.84 / +0.83 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 636 |
| [[WDR62]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CHAF1A]] | +0.82 | +0.78 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[PSMC3IP]] | +0.82 | +0.81 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PKMYT1]] | +0.82 | +0.77 / +0.83 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 656 |
| [[HAUS8]] | +0.82 | +0.77 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.82 | +0.77 / +0.85 | both halves | 7e-06 |  |
| [[DTL]] | +0.81 | +0.76 / +0.83 | both halves | 7e-06 | STRING 411 |
| [[CDCA5]] | +0.81 | +0.72 / +0.85 | both halves | 7e-06 | pathway: S Phase; STRING 400 |
| [[RAD51AP1]] | +0.81 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 406 |
| [[MCM10]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 907 |
| [[CENPO]] | +0.80 | +0.71 / +0.82 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises ORC6's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.91× lower at baseline in the lines without E2F2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises ORC6's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without CDC25A | 0.010 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ORC6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF367]] | C | ZNF367 activity raises ORC6's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.52× lower at baseline in the lines without ZNF367 | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises ORC6's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without MCM10 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises ORC6's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without DSCC1 | 0.090 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.2, -48.0); signed map (-41.4, -44.3). **Vector** length 102, 32.8% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.63 to 28); *E2F G1/S* (control, mean cos +0.63 to 23); *Homology Directed Repair* (reactome, mean cos +0.62 to 32).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.1 | +13.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.7 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +6.7 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +3.4 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +7.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.9 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.8 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.3 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -4.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -0.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | origin recognition complex subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q11.2 — chr16:46,689,643-46,698,394 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ORC6L |
| Gene groups (HGNC) | Origin recognition complex |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 19 pathways, smallest: CDC6 association with the ORC:origin complex; E2F-enabled inhibition of pre-replication complex formation; E2F mediated regulation of DNA replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5N6](https://www.uniprot.org/uniprotkb/Q9Y5N6) (Origin recognition complex subunit 6):

> Component of the origin recognition complex (ORC) that binds origins of replication. DNA-binding is ATP-dependent. The specific DNA sequences that define origins of replication have not been identified yet. ORC is required to assemble the pre-replication complex necessary to initiate DNA replication. Does not bind histone H3 and H4 trimethylation marks H3K9me3, H3K27me3 and H4K20me3.

**Summary**, from NCBI Gene [23594](https://www.ncbi.nlm.nih.gov/gene/23594):

> The origin recognition complex (ORC) is a highly conserved six subunit protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is a subunit of the ORC complex. Gene silencing studies with small interfering RNA demonstrated that this protein …

**Accessions** — [HGNC:17151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17151) · Entrez [23594](https://www.ncbi.nlm.nih.gov/gene/23594) · UniProt [Q9Y5N6](https://www.uniprot.org/uniprotkb/Q9Y5N6) · Ensembl [ENSG00000091651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091651)

## Data

Gene col 1674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1674); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1674]; `tensor/DDL_lfc|DDL_z.npy` [1674]; `embed/gene_vectors.npy` [1674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1674 or target_col == 1674). Every well: [[ORC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
