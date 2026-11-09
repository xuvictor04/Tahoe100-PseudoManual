---
symbol: "MTARC2"
type: "gene"
col: 3950
ensembl_id: "ENSG00000117791"
name: "mitochondrial amidoxime reducing component 2"
location: "1q41"
module: 160
arm: "-"
pooled_cpm: 10.14
n_lines_expressing: 42
n_dd_up: 25
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# MTARC2

*mitochondrial amidoxime reducing component 2* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +13.7, q 3e-40, up in 22 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.637× (z -9.7, q 1e-19, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIS3L]] (+0.62, fdr 1e-05), [[AMACR]] (+0.60, fdr 7e-06), [[ISOC1]] (+0.58, fdr 1e-05); moves opposite to [[LRRC8A]] (-0.59, fdr 8e-06), [[SENP5]] (-0.58, fdr 1e-05), [[PDCD6]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +13.7 | 3e-40 | 22/36 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +7.3 | 9e-11 | 24/39 (CFPAC-1, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.3 | 4e-08 | 19/35 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +6.1 | 2e-07 | 22/37 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +5.9 | 5e-07 | 19/39 (KATO III, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +5.0 | 6e-05 | 17/39 (NCI-H460, A498, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 5e-04 | 11/39 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.5 | 6e-04 | 13/40 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.4 | 6e-04 | 12/30 (RPMI-7951, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 6e-04 | 13/39 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +4.4 | 6e-04 | 11/39 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +4.3 | 8e-04 | 10/26 (KATO III, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 8e-04 | 10/40 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.36×** | +4.2 | 9e-04 | 10/39 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 9/40 (AsPC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.008 | 3/36 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.009 | 10/40 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.016 | 9/39 (AsPC-1, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -9.7 | 1e-19 | 26/37 (Hs 766T, KATO III, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -7.0 | 8e-10 | 22/39 (SNU-423, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.653×** | -6.5 | 2e-08 | 20/39 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.690×** | -5.7 | 2e-06 | 18/39 (KATO III, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.502×** | -5.5 | 5e-06 | 18/38 (NCI-H1792, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -5.0 | 4e-05 | 15/39 (SW480, HEC-1-A, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.733×** | -4.7 | 2e-04 | 15/39 (SW480, A549, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -4.0 | 0.004 | 10/35 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -3.9 | 0.005 | 9/37 (HEC-1-A, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.781×** | -3.8 | 0.009 | 15/39 (NCI-H2030, PANC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.785×** | -3.7 | 0.011 | 17/36 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | **0.807×** | -3.3 | 0.049 | 11/39 (KATO III, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.809×** | -3.2 | 0.051 | 15/39 (HepG2/C3A, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.2 | 0.064 | 2/40 (SHP-77, A-427) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.3 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -12.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -16.1) |
| [[KATO III (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -8.8) |
| [[LS 180 (line)]] | wt | 17.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 6.55 | 0 | 2 (1 ⚠) | — | [[Methotrexate (drug)]] 0.05 µM 0.0650× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -16.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0358× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.284× (z -9.5) |
| [[PANC-1 (line)]] | alt | 7.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.267× (z -9.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[RKO (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.8) |
| [[SHP-77 (line)]] | alt | 6.89 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0698× (z -9.1) |
| [[SW48 (line)]] | wt | 19.5 | 0 | 1 | — | [[9-ING-41 (drug)]] 0.5 µM 0.0497× (z -9.7) |
| [[A-172 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[AMACR]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ISOC1]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[HSBP1L1]] | +0.57 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[SLTM]] | +0.56 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[PRPF4B]] | +0.56 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[CNNM1]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SREK1]] | +0.55 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[PM20D2]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[BATF]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZNF280D]] | +0.53 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[SLC22A5]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8A]] | -0.59 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[SENP5]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.56 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CAP1]] | -0.56 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[EHBP1L1]] | -0.54 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[ARPC2]] | -0.53 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[RCOR1]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[GRIN2D]] | -0.52 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[LYPD3]] | -0.51 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[PPARD]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[SAP130]] | -0.51 | -0.47 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MTARC2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[LGALSL-DT]] | C | LGALSL-DT activity raises MTARC2's level | lines that do not express LGALSL-DT (4) vs lines expressing it (46) | 3.10× lower at baseline in the lines without LGALSL-DT | 0.087 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **-** arm (projection on the module's main direction -0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-20.6, 3.4); signed map (10.8, -36.5). **Vector** length 82.2, 17.0% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.9 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +6.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +4.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.0 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.5 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.9 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial amidoxime reducing component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:220,748,225-220,784,815 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20605; previously MOSC2, MARC2 |
| Gene groups (HGNC) | Mitochondrial amidoxime reducing component family |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969Z3](https://www.uniprot.org/uniprotkb/Q969Z3) (Mitochondrial amidoxime reducing component 2):

> Catalyzes the reduction of N-oxygenated molecules, acting as a counterpart of cytochrome P450 and flavin-containing monooxygenases in metabolic cycles. As a component of prodrug-converting system, reduces a multitude of N-hydroxylated prodrugs particularly amidoximes, leading to increased drug bioavailability. May be involved in mitochondrial N(omega)-hydroxy-L-arginine (NOHA) reduction, regulating endogenous nitric oxide levels and biosynthesis. Postulated to cleave the N-OH bond of …

**Summary**, from NCBI Gene [54996](https://www.ncbi.nlm.nih.gov/gene/54996):

> The protein encoded by this gene is an enzyme found in the outer mitochondrial membrane that reduces N-hydroxylated substrates. The encoded protein uses molybdenum as a cofactor and cytochrome b5 type B and NADH cytochrome b5 reductase as accessory proteins. One type of substrate used is N-hydroxylated nucleotide base analogues, which can be toxic to a cell. Other substrates include N(omega)-hydroxy-L-arginine (NOHA) and amidoxime prodrugs, which are activated by the encoded enzyme. Multiple …

**Accessions** — [HGNC:26064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26064) · Entrez [54996](https://www.ncbi.nlm.nih.gov/gene/54996) · UniProt [Q969Z3](https://www.uniprot.org/uniprotkb/Q969Z3) · Ensembl [ENSG00000117791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117791)

## Data

Gene col 3950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3950); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3950]; `tensor/DDL_lfc|DDL_z.npy` [3950]; `embed/gene_vectors.npy` [3950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3950 or target_col == 3950). Every well: [[MTARC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTARC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
