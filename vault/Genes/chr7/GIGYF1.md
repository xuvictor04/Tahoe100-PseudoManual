---
symbol: "GIGYF1"
type: "gene"
col: 7123
ensembl_id: "ENSG00000146830"
name: "GRB10 interacting GYF protein 1"
location: "7q22.1"
module: 138
arm: "+"
pooled_cpm: 30.42
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# GIGYF1

*GRB10 interacting GYF protein 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.54× (z +10.4, q 2e-22, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.666× (z -9.9, q 4e-20, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.677× (z -6.7, q 2e-09, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP19]] (+0.67, fdr 7e-06), [[RXRB]] (+0.64, fdr 8e-06), [[STK11]] (+0.63, fdr 3e-05); moves opposite to [[BOLA3]] (-0.65, fdr 1e-05), [[UBA6]] (-0.55, fdr 2e-05), [[MGAT5]] (-0.55, fdr 2e-05).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +10.4 | 2e-22 | 31/48 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +8.9 | 1e-16 | 41/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.3 | 7e-08 | 34/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.0 | 1e-04 | 25/46 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +4.5 | 6e-04 | 24/46 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.4 | 0.001 | 22/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.002 | 19/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.021 | 20/47 (J82, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.089 | 18/48 (RKO, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.11 | 15/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.666×** | -9.9 | 4e-20 | 29/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.607×** | -8.6 | 3e-15 | 39/48 (NCI-H23, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.622×** | -8.1 | 9e-14 | 38/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.638×** | -7.7 | 2e-12 | 34/48 (SW48, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.650×** | -7.4 | 2e-11 | 38/48 (NCI-H23, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -6.7 | 2e-09 | 30/48 (C32, HCT15, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.538×** | -5.5 | 2e-06 | 27/48 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.550×** | -5.3 | 6e-06 | 27/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.561×** | -5.2 | 1e-05 | 27/48 (Hs 766T, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.743×** | -5.1 | 2e-05 | 23/48 (NCI-H23, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.759×** | -4.7 | 1e-04 | 28/48 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.604×** | -4.5 | 3e-04 | 21/48 (NCI-H460, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.621×** | -4.3 | 9e-04 | 24/48 (A-427, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.779×** | -4.1 | 0.002 | 22/48 (RKO, SNU-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.728×** | -3.9 | 0.004 | 19/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -3.5 | 0.016 | 15/48 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.020 | 17/48 (NCI-H460, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.811×** | -3.2 | 0.040 | 12/48 (HT-29, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.778×** | -3.1 | 0.062 | 11/48 (NCI-H661, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.824×** | -2.9 | 0.086 | 14/48 (LoVo, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.888× | -2.9 | 0.098 | 15/48 (LOX-IMVI, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.0) | — |
| [[RKO (line)]] | wt | 52.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -16.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 56.1 | 0 | 1 | — | [[Everolimus (drug)]] 0.05 µM 0.224× (z -9.5) |
| [[C32 (line)]] | wt | 48.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.228× (z -12.0) |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0814× (z -13.0) |
| [[J82 (line)]] | alt | 25.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.3) | — |
| [[KATO III (line)]] | alt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.5) | — |
| [[LoVo (line)]] | wt | 37.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.5) | — |
| [[SW480 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP19]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RXRB]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[STK11]] | +0.63 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[KMT2B]] | +0.63 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[TEPSIN]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[BRD1]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CPT1B]] | +0.59 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[CLCN7]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ZFTRAF1]] | +0.58 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[MEGF8]] | +0.56 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[RNF103]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DCAF8]] | +0.56 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BOLA3]] | -0.65 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[UBA6]] | -0.55 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MGAT5]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[VDAC1]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GRB2]] | -0.54 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[SEC24D]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[PSMD14]] | -0.52 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[MPZL1]] | -0.49 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[DPM2]] | -0.48 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[NBAS]] | -0.48 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[OLA1]] | -0.48 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[ATP2C1]] | -0.48 | -0.49 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.3, -22.0); signed map (3.6, -7.9). **Vector** length 104, 23.9% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.4 | +8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.5 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +4.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.6 | +3.1 |
|  | [[MK-3903 (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -7.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -5.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | GRB10 interacting GYF protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,679,507-100,694,250 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GYF1; previously PERQ1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; GRB10 interacting GYF protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [O75420](https://www.uniprot.org/uniprotkb/O75420) (GRB10-interacting GYF protein 1):

> May act cooperatively with GRB10 to regulate tyrosine kinase receptor signaling. May increase IGF1 receptor phosphorylation under IGF1 stimulation as well as phosphorylation of IRS1 and SHC1 (By similarity).

**Summary**, from NCBI Gene [64599](https://www.ncbi.nlm.nih.gov/gene/64599):

> This gene encodes a member of the gyf family of adaptor proteins. The encoded protein contains a gyf protein interaction domain. It binds growth factor receptor bound 10, another adaptor protein that binds activated insulin-like growth factor 1 and insulin receptors and regulates receptor signaling. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:9126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9126) · Entrez [64599](https://www.ncbi.nlm.nih.gov/gene/64599) · UniProt [O75420](https://www.uniprot.org/uniprotkb/O75420) · Ensembl [ENSG00000146830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146830)

## Data

Gene col 7123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7123); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7123]; `tensor/DDL_lfc|DDL_z.npy` [7123]; `embed/gene_vectors.npy` [7123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7123 or target_col == 7123). Every well: [[GIGYF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIGYF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
