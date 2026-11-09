---
symbol: "ETV4"
type: "gene"
col: 10655
ensembl_id: "ENSG00000175832"
name: "ETS variant transcription factor 4"
location: "17q21.31"
module: 92
arm: "+"
pooled_cpm: 25.23
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 36
n_dd_up_clean: 5
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ETV4

*ETS variant transcription factor 4* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.86× (z +9.3, q 8e-18, up in 17 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.33× (z +4.4, q 9e-04, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.181× (z -25.5, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB5]] (+0.79, fdr 7e-06), [[SPRED1]] (+0.76, fdr 7e-06), [[SPRY4-AS1]] (+0.75, fdr 7e-06); moves opposite to [[SNX6]] (-0.51, fdr 2e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.86×** | +9.3 | 8e-18 | 17/31 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.80×** | +9.2 | 1e-17 | 30/42 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.40×** | +4.9 | 2e-04 | 18/37 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.36×** | +4.8 | 3e-04 | 19/41 (HOP62, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +4.6 | 5e-04 | 17/46 (A549, LOX-IMVI, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +4.4 | 9e-04 | 21/46 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.004 | 14/46 (NCI-H460, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.29×** | +3.8 | 0.010 | 13/41 (A-172, CHP-212, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.013 | 9/45 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.019 | 17/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lopinavir (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.023 | 9/45 (A549, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.5 | 0.024 | 14/46 (LoVo, A498, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.23×** | +3.2 | 0.060 | 9/45 (A-172, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10655.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.181×** | -25.5 | 0e+00 | 42/44 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.185×** | -22.5 | 0e+00 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.251×** | -20.6 | 0e+00 | 44/45 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.340×** | -20.2 | 0e+00 | 41/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.276×** | -20.0 | 0e+00 | 43/45 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.261×** | -19.1 | 0e+00 | 43/46 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.327×** | -17.3 | 0e+00 | 39/45 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.383×** | -17.3 | 0e+00 | 43/46 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.342×** | -15.4 | 0e+00 | 40/45 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.488×** | -15.3 | 0e+00 | 41/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.381×** | -12.2 | 1e-32 | 34/45 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.570×** | -11.4 | 3e-28 | 38/46 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.219×** | -6.8 | 4e-10 | 32/46 (SW480, A-427, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[BI-3406 (drug)]] 0.5 µM |  | **0.523×** | -6.5 | 3e-09 | 27/46 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.663×** | -6.3 | 8e-09 | 25/45 (KATO III, A-427, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 68.4 | 0 | 21 (6 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0797× (z -32.8) |
| [[LS 180 (line)]] | wt | 66.6 | 0 | 19 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.151× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 55.5 | 0 | 16 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0846× (z -21.5) |
| [[C32 (line)]] | wt | 46.1 | 0 | 14 | — | [[Binimetinib (drug)]] 0.5 µM 0.0832× (z -20.0) |
| [[A-427 (line)]] | wt | 57.6 | 0 | 13 | — | [[Trametinib (drug)]] 5 µM 0.0963× (z -19.0) |
| [[HOP62 (line)]] | alt | 19.7 | 2 (1 ⚠) | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +10.2) | [[Cobimetinib (drug)]] 0.5 µM 0.147× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 12 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.334× (z -22.0) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0565× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 60.3 | 0 | 12 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0700× (z -20.1) |
| [[HEC-1-A (line)]] | alt | 22.3 | 0 | 11 | — | [[Cobimetinib (drug)]] 5 µM 0.127× (z -14.8) |
| [[KATO III (line)]] | alt | 21.0 | 0 | 11 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.117× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 38.1 | 1 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +14.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Trametinib (drug)]] 0.5 µM 0.206× (z -16.8) |
| [[PANC-1 (line)]] | alt | 7.88 | 0 | 9 | — | [[Cobimetinib (drug)]] 0.5 µM 0.151× (z -11.9) |
| [[A498 (line)]] | wt | 10.2 | 0 | 7 | — | [[Cobimetinib (drug)]] 0.5 µM 0.211× (z -10.3) |
| [[A549 (line)]] | wt | 19.3 | 0 | 7 | — | [[Cobimetinib (drug)]] 5 µM 0.0612× (z -18.2) |
| [[HepG2_C3A (line)]] | wt | 75.9 | 0 | 7 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.158× (z -13.3) |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 6 | — | [[Cobimetinib (drug)]] 5 µM 0.0763× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 6 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.137× (z -13.6) |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 6 | — | [[Binimetinib (drug)]] 0.5 µM 0.122× (z -13.4) |
| [[SW1417 (line)]] | alt | 44.2 | 0 | 5 | — | [[Binimetinib (drug)]] 0.5 µM 0.286× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.128× (z -10.1) |
| [[RKO (line)]] | wt | 28.3 | 0 | 4 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.111× (z -14.8) |
| [[SW48 (line)]] | wt | 15.6 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.0473× (z -12.5) |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 3 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.175× (z -9.8) |
| [[LoVo (line)]] | wt | 26.4 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -9.4) ⚠ unreliable plate only · without an alert: [[Trametinib (drug)]] 5 µM 0.198× (z -8.6) |
| [[J82 (line)]] | alt | 9.63 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.152× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 9.99 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.119× (z -10.9) |
| [[AN3 CA (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 27.2 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0775× (z -8.9) |
| [[COLO 205 (line)]] | alt | 9.74 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0586× (z -10.1) |
| [[HS-578T (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.183× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0929× (z -10.4) |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.0880× (z -8.7) |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.123× (z -9.5) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB5]] | +0.79 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SPRED1]] | +0.76 | +0.76 / +0.79 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[SPRY4-AS1]] | +0.75 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.75 | +0.74 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 638 |
| [[ETV1]] | +0.74 | +0.70 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[LINC01844]] | +0.74 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[MYEOV]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[LINC02320]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SPRED2]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ETV5]] | +0.67 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[DUSP4]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 | pathway: MAPK family signaling cascades; STRING 464 |
| [[EGR3]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX6]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ETV4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTPRZ1]] | B | PTPRZ1 activity raises ETV4's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 1.82× lower at baseline in the lines without PTPRZ1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[DLC1]] | B | DLC1 activity raises ETV4's level | lines that do not express DLC1 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without DLC1 | 0.087 | ⚠ within organs, on part of the lines; also absent: AXL, LGALS1, VCAN |
| [[ASTL]] | B | ASTL activity raises ETV4's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without ASTL | 0.091 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[CRYAB]] | B | CRYAB activity raises ETV4's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 1.45× lower at baseline in the lines without CRYAB | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP |
| [[CRYAB]] | C | CRYAB activity strengthens ETV4's drug response | lines that do not express CRYAB (31) vs lines expressing it (15) | the lines without CRYAB respond 0.93× as strongly (z diff +1.60); strongest at Trametinib (DMSO_TF solvate) 0.05 µM: 0.34x vs 0.31x (z diff +1.9) | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP; target measured in part of the lines; rests on the correction |
| [[TOR4A]] | C | TOR4A activity weakens ETV4's drug response | lines that do not express TOR4A (13) vs lines expressing it (33) | the lines without TOR4A respond 0.90× as strongly (z diff -0.95); strongest at Trametinib (DMSO_TF solvate) 0.05 µM: 0.30x vs 0.35x (z diff -1.8) | 0.081 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33; target measured in part of the lines; rests on the correction |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, 6.7); signed map (8.8, 47.4). **Vector** length 133, 39.5% of its response variance represented; |z| ≥ 3 in 1,347 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Pre-NOTCH Expression and Processing* (reactome, mean cos +0.53 to 5); *Signaling by NOTCH* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +7.6 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +7.3 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +6.0 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +5.5 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -0.5 |
|  | [[OTS514 (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -12.4 | -22.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -11.7 | -20.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -10.7 | -20.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -10.3 | -19.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -10.2 | -25.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -10.1 | -20.6 |

## What is on record

|  |  |
|---|---|
| Name | ETS variant transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,527,844-43,579,620 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E1A-F, E1AF, PEA3 |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING |
| Reactome | 2 pathways, smallest: MAPK6/MAPK4 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [P43268](https://www.uniprot.org/uniprotkb/P43268) (ETS translocation variant 4):

> Transcriptional activator. Regulates the positioning of motor neurons within the lateral medial column of the spinal cord and controls the terminal arborization of specific motor neuron axons within their target muscles (By similarity). Required for the expression of CDH8 and SEMA3E in ETV4-expressing motor neurons and for the exclusion of CDH7 expression from these neurons (By similarity). May play a role in keratinocyte differentiation.; (Microbial infection) Binds to the enhancer of the …

**Summary**, from NCBI Gene [2118](https://www.ncbi.nlm.nih.gov/gene/2118):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in positive regulation of keratinocyte differentiation and positive regulation of transcription by RNA polymerase II. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3493) · Entrez [2118](https://www.ncbi.nlm.nih.gov/gene/2118) · UniProt [P43268](https://www.uniprot.org/uniprotkb/P43268) · Ensembl [ENSG00000175832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175832)

## Data

Gene col 10655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10655); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10655]; `tensor/DDL_lfc|DDL_z.npy` [10655]; `embed/gene_vectors.npy` [10655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10655 or target_col == 10655). Every well: [[ETV4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETV4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
