---
symbol: "ITFG2"
type: "gene"
col: 3200
ensembl_id: "ENSG00000111203"
name: "integrin alpha FG-GAP repeat containing 2"
location: "12p13.33"
module: 114
arm: "+"
pooled_cpm: 42.7
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ITFG2

*integrin alpha FG-GAP repeat containing 2* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.05× (z +13.7, q 5e-40, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.623× (z -12.7, q 2e-34, down in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.327× (z -11.1, q 3e-26, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF586]] (+0.61, fdr 1e-05), [[ZNF785]] (+0.60, fdr 1e-05), [[MZF1]] (+0.58, fdr 4e-05); moves opposite to [[SPTBN1]] (-0.52, fdr 1e-05), [[PTBP3]] (-0.48, fdr 5e-05), [[SNX7]] (-0.46, fdr 3e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +13.7 | 5e-40 | 41/48 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.57×** | +8.6 | 3e-15 | 41/48 (Panc 03.27, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.0 | 4e-07 | 24/47 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 1e-06 | 30/48 (NCI-H1573, SW480, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.69×** | +5.3 | 2e-05 | 25/48 (NCI-H1573, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.003 | 18/48 (HT-29, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.007 | 22/48 (NCI-H1573, AsPC-1, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.7 | 0.013 | 10/48 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.066 | 6/48 (A498, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.623×** | -12.7 | 2e-34 | 33/47 (PANC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.327×** | -11.1 | 3e-26 | 44/49 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.603×** | -9.2 | 4e-18 | 27/47 (C-33 A, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.617×** | -9.2 | 6e-18 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.649×** | -8.2 | 2e-14 | 31/48 (SNU-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.448×** | -8.0 | 1e-13 | 29/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -7.6 | 3e-12 | 31/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.675×** | -7.5 | 6e-12 | 31/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.675×** | -7.2 | 4e-11 | 30/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.714×** | -6.4 | 9e-09 | 27/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -5.9 | 2e-07 | 28/48 (BT-474, HCT15, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.762×** | -5.2 | 1e-05 | 27/48 (Panc 03.27, HCT15, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.787×** | -4.6 | 2e-04 | 20/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.819×** | -3.8 | 0.006 | 18/48 (HCT15, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.824×** | -3.7 | 0.009 | 19/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.696×** | -3.6 | 0.011 | 13/48 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 102 | 1 | 11 (8 ⚠) | [[Auranofin (drug)]] 5 µM 1.79× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -17.8) |
| [[HOP62 (line)]] | alt | 50.9 | 1 | 5 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.81× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.379× (z -10.0) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.406× (z -9.3) |
| [[PANC-1 (line)]] | alt | 27.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -12.3) |
| [[LoVo (line)]] | wt | 62.8 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.39× (z +15.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.410× (z -10.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.469× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 65.0 | 0 | 4 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.103× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 112 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.37× (z +11.5) | [[TAK-901 (drug)]] 5 µM 0.127× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 67.1 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.31× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 94.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A498 (line)]] | wt | 23.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 41.0 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.89× (z +13.5) | [[Ixazomib citrate (drug)]] 0.5 µM 0.260× (z -10.2) |
| [[HT-29 (line)]] | alt | 38.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.60× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 31.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.74× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 17.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.94× (z +14.2) | — |
| [[C-33 A (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -16.9) ⚠ toxic |
| [[C32 (line)]] | wt | 17.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.1× (z +14.8) | — |
| [[H4 (line)]] | wt | 59.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -8.6) |
| [[HCT15 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 59.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.89× (z +15.5) | — |
| [[J82 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -11.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 56.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.386× (z -8.6) |
| [[RKO (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.177× (z -11.1) |
| [[SNU-423 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 27.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.70× (z +10.3) | — |
| [[A549 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF586]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZNF785]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[MZF1]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[PPP5D1P-1]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PLPP5]] | +0.56 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[ZKSCAN2-DT]] | +0.56 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[UBE2CP5]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PCGF3-AS1]] | +0.54 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[XPNPEP3]] | +0.54 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[FBXO10]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[SLC25A53]] | +0.53 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN1]] | -0.52 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PTBP3]] | -0.48 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[SNX7]] | -0.46 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TWSG1]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[AFDN]] | -0.45 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[TP53BP2]] | -0.44 | -0.46 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.3, 25.5); signed map (1.8, -3.9). **Vector** length 90.5, 21.4% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.0 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +4.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +5.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.4 | -8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.2 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.2 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | integrin alpha FG-GAP repeat containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:2,812,622-2,859,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS028, KICS3; previously FGGAP1 |
| Gene groups (HGNC) | KICSTOR complex |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969R8](https://www.uniprot.org/uniprotkb/Q969R8) (KICSTOR complex protein ITFG2):

> As part of the KICSTOR complex functions in the amino acid-sensing branch of the TORC1 signaling pathway. Recruits, in an amino acid-independent manner, the GATOR1 complex to the lysosomal membranes and allows its interaction with GATOR2 and the RAG GTPases. Functions upstream of the RAG GTPases and is required to negatively regulate mTORC1 signaling in absence of amino acids. In absence of the KICSTOR complex mTORC1 is constitutively localized to the lysosome and activated. The KICSTOR complex …

**Summary**, from NCBI Gene [55846](https://www.ncbi.nlm.nih.gov/gene/55846):

> Involved in cellular response to amino acid starvation; cellular response to glucose starvation; and negative regulation of TORC1 signaling. Located in lysosomal membrane. Part of KICSTOR complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30879) · Entrez [55846](https://www.ncbi.nlm.nih.gov/gene/55846) · UniProt [Q969R8](https://www.uniprot.org/uniprotkb/Q969R8) · Ensembl [ENSG00000111203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111203)

## Data

Gene col 3200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3200); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3200]; `tensor/DDL_lfc|DDL_z.npy` [3200]; `embed/gene_vectors.npy` [3200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3200 or target_col == 3200). Every well: [[ITFG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITFG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
