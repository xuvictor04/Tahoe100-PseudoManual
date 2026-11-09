---
symbol: "EXOSC10"
type: "gene"
col: 10169
ensembl_id: "ENSG00000171824"
name: "exosome component 10"
location: "1p36.22"
module: 153
arm: "+"
pooled_cpm: 49.58
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# EXOSC10

*exosome component 10* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.52× (z +10.5, q 5e-23, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.690× (z -11.4, q 4e-27, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NELFCD]] (+0.67, fdr 1e-05), [[ZNF280D]] (+0.66, fdr 3e-05), [[ZNF507]] (+0.65, fdr 5e-05); moves opposite to [[ANKRD37]] (-0.65, fdr 4e-05), [[BBLN]] (-0.63, fdr 6e-05), [[SLC25A29]] (-0.62, fdr 3e-05).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +10.5 | 5e-23 | 44/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.32×** | +9.6 | 3e-19 | 40/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +8.8 | 4e-16 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +8.7 | 6e-16 | 30/48 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.5 | 2e-15 | 30/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +7.8 | 4e-13 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +6.9 | 4e-10 | 35/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.1 | 6e-08 | 32/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.6 | 1e-06 | 29/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 6e-06 | 26/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.3 | 6e-06 | 19/35 (NCI-H2030, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +5.2 | 1e-05 | 24/47 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.7 | 9e-05 | 21/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +4.7 | 1e-04 | 23/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.22×** | +4.3 | 6e-04 | 23/48 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.010 | 16/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.012 | 17/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.3 | 0.028 | 9/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.050 | 7/49 (HOP62, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -11.4 | 4e-27 | 32/48 (SNU-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.599×** | -11.1 | 4e-26 | 40/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.635×** | -9.8 | 2e-20 | 43/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.639×** | -9.7 | 4e-20 | 39/48 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.677×** | -8.5 | 3e-15 | 41/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -7.4 | 1e-11 | 31/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.719×** | -7.1 | 8e-11 | 31/48 (SW48, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.636×** | -5.1 | 2e-05 | 31/48 (SNU-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.819×** | -4.3 | 1e-03 | 22/48 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.820×** | -4.3 | 0.001 | 23/48 (A549, hTERT-HPNE, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.8 | 0.006 | 19/48 (SW480, SW1417, …) | rises with dose |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.898× | -3.3 | 0.048 | 6/49 (SW480, SW48, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.753×** | -3.2 | 0.059 | 10/48 (C32, RKO, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.6 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +14.8) | — |
| [[SW480 (line)]] | alt | 59.0 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +12.2) | [[Belinostat (drug)]] 5 µM 0.549× (z -8.6) |
| [[HOP62 (line)]] | alt | 56.6 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.0) |
| [[RKO (line)]] | wt | 55.9 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -8.6) |
| [[J82 (line)]] | alt | 61.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.7) |
| [[LoVo (line)]] | wt | 48.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 69.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -17.4) |
| [[A-427 (line)]] | wt | 51.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 37.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.9) |
| [[A549 (line)]] | wt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.103× (z -8.7) |
| [[HCT15 (line)]] | alt | 76.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 65.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -10.2) |
| [[Hs 766T (line)]] | wt | 57.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 72.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 50.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 70.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 38.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 64.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.339× (z -10.2) |
| [[SW48 (line)]] | wt | 57.5 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.279× (z -10.1) |
| [[A-172 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NELFCD]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[ZNF280D]] | +0.66 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[ZNF507]] | +0.65 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[SF3B4]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.65 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ANKRD40]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[UTP20]] | +0.64 | +0.43 / +0.64 | both halves | 3e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 963 |
| [[ZNF532]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[POMK]] | +0.63 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PIGO]] | +0.63 | +0.40 / +0.68 | both halves | 5e-05 |  |
| [[NNT]] | +0.63 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.62 | +0.39 / +0.61 | both halves | 5e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD37]] | -0.65 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[BBLN]] | -0.63 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[SLC25A29]] | -0.62 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[PNPLA8]] | -0.62 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[CIAO2B]] | -0.62 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MPG]] | -0.61 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[TPTEP2-CSNK1E]] | -0.61 | -0.46 / -0.69 | both halves | 2e-05 |  |
| [[SEC61G]] | -0.61 | -0.33 / -0.68 | both halves | 1e-04 |  |
| [[COMMD6]] | -0.61 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[CIB1]] | -0.61 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[RABGEF1]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ELL]] | -0.60 | -0.43 / -0.58 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.9, 4.5); signed map (9.7, -34.0). **Vector** length 86.1, 19.3% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.8 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,066,618-11,099,869 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PM-Scl, PM/Scl-100, Rrp6p, RRP6, p2, p3, p4; previously PMSCL2 |
| Gene groups (HGNC) | Exosome complex |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 9 pathways, smallest: Nuclear RNA decay; Somatic hypermutation of immunoglobulin genes; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01780](https://www.uniprot.org/uniprotkb/Q01780) (Exosome complex component 10):

> Catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [5394](https://www.ncbi.nlm.nih.gov/gene/5394):

> Enables 3'-5'-RNA exonuclease activity and telomerase RNA binding activity. Involved in several processes, including RNA catabolic process; negative regulation of telomere maintenance via telomerase; and ribosome biogenesis. Located in cytosol; euchromatin; and nuclear lumen. Part of nuclear exosome (RNase complex) and small-subunit processome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9138) · Entrez [5394](https://www.ncbi.nlm.nih.gov/gene/5394) · UniProt [Q01780](https://www.uniprot.org/uniprotkb/Q01780) · Ensembl [ENSG00000171824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171824)

## Data

Gene col 10169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10169); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10169]; `tensor/DDL_lfc|DDL_z.npy` [10169]; `embed/gene_vectors.npy` [10169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10169 or target_col == 10169). Every well: [[EXOSC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
