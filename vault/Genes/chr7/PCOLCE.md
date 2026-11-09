---
symbol: "PCOLCE"
type: "gene"
col: 2745
ensembl_id: "ENSG00000106333"
name: "procollagen C-endopeptidase enhancer"
location: "7q22.1"
module: 45
arm: "+"
pooled_cpm: 8.38
n_lines_expressing: 43
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PCOLCE

*procollagen C-endopeptidase enhancer* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.52× (z +9.9, q 2e-20, up in 13 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +5.7, q 2e-06, up in 15 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.363× (z -10.8, q 1e-24, down in 29 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REEP2]] (+0.60, fdr 1e-05), [[PBXIP1]] (+0.60, fdr 1e-05), [[MANBA]] (+0.59, fdr 2e-05); moves opposite to [[PIGL]] (-0.64, fdr 1e-05), [[MRPS16]] (-0.57, fdr 4e-05), [[ANAPC7]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[THY1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Tomivosertib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +9.9 | 2e-20 | 13/24 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.1 | 3e-10 | 8/12 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.7 | 2e-06 | 15/35 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +4.7 | 4e-04 | 8/14 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.4 | 0.001 | 7/41 (LoVo, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.0 | 0.006 | 10/26 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[LJI308 (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.100 | 5/37 (H4, HS-578T, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.77× | +3.2 | 0.11 | 1/14 (PANC-1) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.363×** | -10.8 | 1e-24 | 29/34 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.496×** | -10.6 | 1e-23 | 25/33 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.402×** | -9.7 | 4e-20 | 26/39 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.425×** | -9.1 | 1e-17 | 27/40 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -8.0 | 1e-13 | 23/39 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.532×** | -6.7 | 2e-09 | 27/39 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.553×** | -6.3 | 2e-08 | 22/39 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.573×** | -5.9 | 2e-07 | 18/38 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.593×** | -5.6 | 2e-06 | 20/34 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -5.5 | 2e-06 | 18/40 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -4.9 | 5e-05 | 12/39 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.643×** | -4.7 | 1e-04 | 12/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.694×** | -3.9 | 0.004 | 12/38 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -3.8 | 0.005 | 13/39 (HS-578T, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.788×** | -3.6 | 0.013 | 10/39 (CFPAC-1, H4, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.747×** | -3.1 | 0.067 | 10/38 (C-33 A, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.738×** | -3.1 | 0.075 | 14/37 (CHP-212, A498, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 66.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -16.1) |
| [[PANC-1 (line)]] | alt | 4.99 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0919× (z -12.3) |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0641× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 3.76 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0688× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 6.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0974× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 9.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0886× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 3.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -9.3) |
| [[RKO (line)]] | wt | 7.12 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0595× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 97.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.7) |
| [[A-172 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.821 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REEP2]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PBXIP1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[MANBA]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[JAK3]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A23]] | +0.55 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[IGSF3]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[CCDC115]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.53 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[CTSF]] | +0.53 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[GALM]] | +0.52 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[DOC2A]] | +0.52 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[RNASET2]] | +0.52 | +0.36 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGL]] | -0.64 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[MRPS16]] | -0.57 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ANAPC7]] | -0.56 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[EEFSEC]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[RNASEH1]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HLCS]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ATP6V0A2]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PPIL1]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[PUS1]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NIP7]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[METTL2B]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PUM3]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THY1]] | B | THY1 activity raises PCOLCE's level | lines that do not express THY1 (38) vs lines expressing it (12) | 5.40× lower at baseline in the lines without THY1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1 |
| [[MXRA8]] | B | MXRA8 activity raises PCOLCE's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without MXRA8 | 0.032 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[HLA-DRB1]] | B | HLA-DRB1 activity raises PCOLCE's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.97× lower at baseline in the lines without HLA-DRB1 | 0.089 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tomivosertib (drug)]] 5 µM | C | PCOLCE activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express PCOLCE (7) vs lines expressing it (41) | the lines without PCOLCE: 0.80× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; also absent: SLC25A43; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.5, -22.6); signed map (-21.4, 7.7). **Vector** length 46.4, 6.55% of its response variance represented; |z| ≥ 3 in 707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.5 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -10.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -9.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -8.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | procollagen C-endopeptidase enhancer |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,602,363-100,608,175 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCPE, PCPE1 |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: Crosslinking of collagen fibrils; Assembly of collagen fibrils and other multimeric structures; Collagen biosynthesis and modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15113](https://www.uniprot.org/uniprotkb/Q15113) (Procollagen C-endopeptidase enhancer 1):

> Binds to the C-terminal propeptide of type I procollagen and enhances procollagen C-proteinase activity.; C-terminal processed part of PCPE (CT-PCPE) may have an metalloproteinase inhibitory activity.

**Summary**, from NCBI Gene [5118](https://www.ncbi.nlm.nih.gov/gene/5118):

> Fibrillar collagen types I-III are synthesized as precursor molecules known as procollagens. These precursors contain amino- and carboxyl-terminal peptide extensions known as N- and C-propeptides, respectively, which are cleaved, upon secretion of procollagen from the cell, to yield the mature triple helical, highly structured fibrils. This gene encodes a glycoprotein which binds and drives the enzymatic cleavage of type I procollagen and heightens C-proteinase activity. [provided by RefSeq, …

**Accessions** — [HGNC:8738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8738) · Entrez [5118](https://www.ncbi.nlm.nih.gov/gene/5118) · UniProt [Q15113](https://www.uniprot.org/uniprotkb/Q15113) · Ensembl [ENSG00000106333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106333)

## Data

Gene col 2745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2745); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2745]; `tensor/DDL_lfc|DDL_z.npy` [2745]; `embed/gene_vectors.npy` [2745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2745 or target_col == 2745). Every well: [[PCOLCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCOLCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
