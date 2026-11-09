---
symbol: "TBCB"
type: "gene"
col: 2571
ensembl_id: "ENSG00000105254"
name: "tubulin folding cofactor B"
location: "19q13.12"
module: 30
arm: "+"
pooled_cpm: 32.77
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TBCB

*tubulin folding cofactor B* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +9.7, q 2e-19, up in 41 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.06× (z +4.5, q 0.001, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.492× (z -11.3, q 4e-27, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC45A]] (+0.79, fdr 7e-06), [[MGST3]] (+0.71, fdr 7e-06), [[SLC27A1]] (+0.70, fdr 3e-05); moves opposite to [[PHF8]] (-0.60, fdr 8e-04, ⚠ one half only (not replicated)), [[ERCC6L2]] (-0.57, fdr 4e-04), [[ANKRD18A]] (-0.57, fdr 4e-04), [[ZNF337-AS1]] (-0.57, fdr 4e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MPP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +9.7 | 2e-19 | 41/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.6 | 1e-11 | 31/35 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +5.2 | 4e-05 | 29/40 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.06×** | +4.5 | 0.001 | 30/45 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.46×** | +4.3 | 0.002 | 24/46 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.95×** | +4.1 | 0.004 | 32/48 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.004 | 28/45 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.77×** | +3.5 | 0.031 | 23/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.75×** | +3.5 | 0.035 | 17/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.4 | 0.035 | 1/48 (NCI-H23) | inconsistent across doses | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.69×** | +3.2 | 0.064 | 14/48 (PANC-1, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.492×** | -11.3 | 4e-27 | 39/47 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.523×** | -7.3 | 6e-11 | 37/48 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -6.3 | 5e-08 | 38/48 (BT-474, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.574×** | -6.3 | 5e-08 | 33/47 (SNU-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -5.6 | 3e-06 | 30/48 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -4.7 | 3e-04 | 27/47 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.697×** | -4.1 | 0.004 | 27/47 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -3.9 | 0.006 | 23/46 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.716×** | -3.8 | 0.010 | 28/47 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -3.2 | 0.074 | 22/46 (SNU-1, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.760× | -3.0 | 0.12 | 15/48 (A498, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 46.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 32.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.3) |
| [[SNU-1 (line)]] | wt | 27.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0834× (z -12.4) |
| [[A549 (line)]] | wt | 59.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.2) |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -8.5) |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.5) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -12.1) |
| [[Hs 766T (line)]] | wt | 34.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.7) |
| [[HS-578T (line)]] | alt | 70.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.8) |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.0) |
| [[J82 (line)]] | alt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.4) |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +11.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 73.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +11.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.1) |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -8.6) |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -8.9) |
| [[A-172 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC45A]] | +0.79 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[MGST3]] | +0.71 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.70 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[MRGBP]] | +0.70 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD27]] | +0.69 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[RRAS]] | +0.67 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[TBCE]] | +0.66 | +0.52 / +0.48 | both halves | 2e-05 | pathway: Post-chaperonin tubulin folding pathway; STRING 807 |
| [[STX7]] | +0.66 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[DPY30]] | +0.65 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[IFT52]] | +0.64 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[FAM13B]] | +0.63 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[CARD19]] | +0.63 | +0.58 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF8]] | -0.60 | -0.51 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ERCC6L2]] | -0.57 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[ANKRD18A]] | -0.57 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[SPRY3]] | -0.57 | -0.44 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[ZNF337-AS1]] | -0.57 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[MMADHC-DT]] | -0.56 | -0.49 / -0.02 | ⚠ not reproduced | 0.007 |  |
| [[GALNT7-DT]] | -0.56 | -0.47 / -0.05 | ⚠ not reproduced | 0.005 |  |
| [[ANKRD18B]] | -0.56 | -0.38 / -0.29 | both halves | 3e-04 |  |
| [[CSTF3]] | -0.56 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SNX5]] | -0.55 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[ANKRD17-DT]] | -0.55 | -0.46 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[CCDC90B-AS1]] | -0.54 | -0.47 / -0.04 | ⚠ not reproduced | 0.005 |  |
| [[MPDU1]] | -0.54 | -0.38 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP1]] | B | MPP1 activity raises TBCB's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without MPP1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.5, -4.5); signed map (-34.1, -2.5). **Vector** length 82.8, 24.3% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +1.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.5 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | +0.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | tubulin folding cofactor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,114,289-36,125,947 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CG22, CKAPI; previously CKAP1 |
| Reactome | 2 pathways, smallest: Post-chaperonin tubulin folding pathway; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99426](https://www.uniprot.org/uniprotkb/Q99426) (Tubulin-folding cofactor B):

> Binds to alpha-tubulin folding intermediates after their interaction with cytosolic chaperonin in the pathway leading from newly synthesized tubulin to properly folded heterodimer. Involved in regulation of tubulin heterodimer dissociation. May function as a negative regulator of axonal growth (By similarity).

**Summary**, from NCBI Gene [1155](https://www.ncbi.nlm.nih.gov/gene/1155):

> Predicted to enable microtubule plus-end binding activity. Predicted to be involved in cytoplasmic microtubule organization. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1989) · Entrez [1155](https://www.ncbi.nlm.nih.gov/gene/1155) · UniProt [Q99426](https://www.uniprot.org/uniprotkb/Q99426) · Ensembl [ENSG00000105254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105254)

## Data

Gene col 2571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2571); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2571]; `tensor/DDL_lfc|DDL_z.npy` [2571]; `embed/gene_vectors.npy` [2571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2571 or target_col == 2571). Every well: [[TBCB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
