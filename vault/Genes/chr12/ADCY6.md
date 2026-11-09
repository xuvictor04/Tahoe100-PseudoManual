---
symbol: "ADCY6"
type: "gene"
col: 10476
ensembl_id: "ENSG00000174233"
name: "adenylate cyclase 6"
location: "12q13.12"
module: 126
arm: "+"
pooled_cpm: 19.97
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# ADCY6

*adenylate cyclase 6* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.32× (z +5.3, q 8e-05, up in 20 of 41 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 2.20×; ⚠ cell-cycle shift, explains ~16% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.427× (z -16.0, q 0e+00, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH24]] (+0.67, fdr 1e-05), [[PLXNB1]] (+0.63, fdr 7e-06), [[ERBB2]] (+0.62, fdr 1e-05); moves opposite to [[ZNF438]] (-0.46, fdr 5e-05), [[BTG1]] (-0.44, fdr 1e-04), [[FER]] (-0.42, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPC4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10476.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 2.20×; ⚠ cell-cycle shift, explains ~16% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.3 | 8e-05 | 20/41 (LoVo, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Gemcitabine (drug)]] 5 µM |  | 1.24× | +3.0 | 0.53 | 4/45 (SW480, COLO 205, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.427×** | -16.0 | 0e+00 | 36/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.582×** | -14.3 | 3e-44 | 34/46 (A-172, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.516×** | -12.4 | 5e-33 | 35/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.531×** | -11.9 | 2e-30 | 34/46 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.615×** | -9.1 | 1e-17 | 34/46 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.639×** | -8.4 | 5e-15 | 29/46 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.595×** | -8.3 | 6e-15 | 30/46 (COLO 205, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -8.0 | 8e-14 | 28/46 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -7.4 | 1e-11 | 27/46 (HT-29, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.686×** | -7.1 | 1e-10 | 26/46 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.689×** | -7.0 | 2e-10 | 23/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.690×** | -6.9 | 2e-10 | 25/46 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.700×** | -6.3 | 1e-08 | 26/47 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.557×** | -5.7 | 4e-07 | 21/43 (SW 900, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.759×** | -5.2 | 9e-06 | 17/46 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.650×** | -4.2 | 8e-04 | 16/47 (A-427, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.814×** | -3.8 | 0.004 | 9/46 (HEC-1-A, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -3.7 | 0.007 | 14/47 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.007 | 6/47 (COLO 205, NCI-H1573, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 39.8 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -12.8) |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0603× (z -13.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -8.6) |
| [[A-172 (line)]] | wt | 19.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -10.4) |
| [[HT-29 (line)]] | alt | 27.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -12.6) |
| [[SW480 (line)]] | alt | 26.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -10.8) |
| [[KATO III (line)]] | alt | 23.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -9.6) |
| [[LS 180 (line)]] | wt | 31.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -8.8) |
| [[A-427 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.4) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0719× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0923× (z -9.8) |
| [[HOP62 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -8.8) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -8.5) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.271× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.280× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -12.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SW48 (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH24]] | +0.67 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PLXNB1]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ERBB2]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 | same gene group; pathway: Intracellular signaling by second messengers |
| [[INPPL1]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[GRK2]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 | pathway: Ca-dependent events |
| [[AKT2]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 | same gene group; pathway: Intracellular signaling by second messengers; STRING 678 |
| [[OTUD3]] | +0.54 | +0.49 / +0.38 | both halves | 6e-05 | pathway: Intracellular signaling by second messengers |
| [[PCGF2]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[LDB1]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[RAB15]] | +0.53 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[MAN2A2]] | +0.53 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[TLE5]] | +0.53 | +0.53 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF438]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[BTG1]] | -0.44 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[FER]] | -0.42 | -0.50 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPC4]] | B | GPC4 activity raises ADCY6's level | lines that do not express GPC4 (19) vs lines expressing it (31) | 1.56× lower at baseline in the lines without GPC4 | 0.051 | ⚠ within organs, on part of the lines; also absent: KCNK5, NTN1, FUT3 |
| [[TLCD4]] | B | TLCD4 activity raises ADCY6's level | lines that do not express TLCD4 (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without TLCD4 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.5, -23.4); signed map (-11.2, -33.9). **Vector** length 71.3, 12.5% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.6 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -16.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.3 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | adenylate cyclase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:48,766,194-48,789,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AC6 |
| Gene groups (HGNC) | Adenylate cyclases; MicroRNA protein coding host genes |
| Hallmark sets | DNA_REPAIR, ADIPOGENESIS |
| Reactome | 45 pathways, smallest: Adenylate cyclase activating pathway; Adenylate cyclase inhibitory pathway; PKA activation in glucagon signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [O43306](https://www.uniprot.org/uniprotkb/O43306) (Adenylate cyclase type 6):

> Catalyzes the formation of the signaling molecule cAMP downstream of G protein-coupled receptors. Functions in signaling cascades downstream of beta-adrenergic receptors in the heart and in vascular smooth muscle cells. Functions in signaling cascades downstream of the vasopressin receptor in the kidney and has a role in renal water reabsorption. Functions in signaling cascades downstream of PTH1R and plays a role in regulating renal phosphate excretion. Functions in signaling cascades …

**Summary**, from NCBI Gene [112](https://www.ncbi.nlm.nih.gov/gene/112):

> This gene encodes a member of the adenylyl cyclase family of proteins, which are required for the synthesis of cyclic AMP. All members of this family have an intracellular N-terminus, a tandem repeat of six transmembrane domains separated by a cytoplasmic loop, and a C-terminal cytoplasmic domain. The two cytoplasmic regions bind ATP and form the catalytic core of the protein. Adenylyl cyclases are important effectors of transmembrane signaling pathways and are regulated by the activity of G …

**Accessions** — [HGNC:237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:237) · Entrez [112](https://www.ncbi.nlm.nih.gov/gene/112) · UniProt [O43306](https://www.uniprot.org/uniprotkb/O43306) · Ensembl [ENSG00000174233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174233)

## Data

Gene col 10476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10476); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10476]; `tensor/DDL_lfc|DDL_z.npy` [10476]; `embed/gene_vectors.npy` [10476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10476 or target_col == 10476). Every well: [[ADCY6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCY6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
