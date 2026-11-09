---
symbol: "ERMARD"
type: "gene"
col: 5016
ensembl_id: "ENSG00000130023"
name: "ER membrane associated RNA degradation"
location: "6q27"
module: 28
arm: "+"
pooled_cpm: 18.81
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ERMARD

*ER membrane associated RNA degradation* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.34× (z +4.0, q 0.033, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.359× (z -14.1, q 2e-42, down in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.488× (z -9.9, q 1e-20, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM128]] (+0.75, fdr 7e-06), [[RAD52]] (+0.65, fdr 1e-05), [[MTHFSD]] (+0.64, fdr 1e-05); moves opposite to [[EDA]] (-0.58, fdr 1e-05), [[ABAT]] (-0.54, fdr 8e-05), [[TIAM1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.033 | 15/48 (KATO III, NCI-H1792, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.071 | 10/47 (C-33 A, KATO III, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.071 | 15/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.071 | 13/48 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.31× | +3.3 | 0.13 | 10/48 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.26× | +3.2 | 0.14 | 9/48 (LoVo, KATO III, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.26× | +3.1 | 0.14 | 10/47 (KATO III, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -14.1 | 2e-42 | 41/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.449×** | -11.0 | 9e-26 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -9.9 | 1e-20 | 40/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.493×** | -9.4 | 1e-18 | 31/43 (PANC-1, J82, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.531×** | -8.7 | 4e-16 | 32/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.577×** | -7.6 | 4e-12 | 32/47 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.594×** | -7.2 | 6e-11 | 30/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.597×** | -7.1 | 9e-11 | 33/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.425×** | -6.2 | 5e-08 | 28/44 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.647×** | -6.0 | 1e-07 | 27/47 (PANC-1, C-33 A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.665×** | -5.3 | 6e-06 | 27/47 (SNU-423, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.772×** | -5.0 | 2e-05 | 24/47 (J82, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.505×** | -4.9 | 4e-05 | 25/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.702×** | -4.9 | 4e-05 | 23/48 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.716×** | -4.4 | 4e-04 | 20/47 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.821×** | -3.8 | 0.004 | 17/48 (A549, CHP-212, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.798×** | -2.9 | 0.090 | 10/47 (J82, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 56.6 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -10.6) |
| [[SW480 (line)]] | alt | 18.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.317× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.173× (z -12.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0965× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 16.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 22.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 7.85 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0667× (z -11.5) |
| [[HCT15 (line)]] | alt | 31.8 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.102× (z -9.2) |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -16.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.310× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM128]] | +0.75 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[RAD52]] | +0.65 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.64 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[COG4]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[BPHL]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[DDX59]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.63 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[RPAP2]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ZBTB37]] | +0.62 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ZNF25]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GIN1]] | +0.62 | +0.64 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDA]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ABAT]] | -0.54 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[TIAM1]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TMEM92]] | -0.52 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[CYTH1]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[CMIP]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[RAB39A]] | -0.50 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[MAGI3]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[EGFL7]] | -0.50 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[LMTK3]] | -0.50 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.7, 21.7); signed map (16.4, -41.3). **Vector** length 63.1, 10.8% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.3 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.6 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -3.3 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane associated RNA degradation |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:169,751,622-169,781,600 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11152, dJ266L20.3; previously C6orf70 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T6L9](https://www.uniprot.org/uniprotkb/Q5T6L9) (Endoplasmic reticulum membrane-associated RNA degradation protein):

> May play a role in neuronal migration during embryonic development.

**Summary**, from NCBI Gene [55780](https://www.ncbi.nlm.nih.gov/gene/55780):

> The protein encoded by this gene contains 2 transmembrane domains near the C-terminus and is localized in the endoplasmic reticulum. Knockout of this gene in developing rat brain showed that it may be involved in neuronal migration. Mutations in this gene are associated with periventricular nodular heterotopia-6 (PVNH6). Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:21056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21056) · Entrez [55780](https://www.ncbi.nlm.nih.gov/gene/55780) · UniProt [Q5T6L9](https://www.uniprot.org/uniprotkb/Q5T6L9) · Ensembl [ENSG00000130023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130023)

## Data

Gene col 5016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5016); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5016]; `tensor/DDL_lfc|DDL_z.npy` [5016]; `embed/gene_vectors.npy` [5016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5016 or target_col == 5016). Every well: [[ERMARD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERMARD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
