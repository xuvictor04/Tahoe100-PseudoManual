---
symbol: "CCDC183"
type: "gene"
col: 13091
ensembl_id: "ENSG00000213213"
name: "coiled-coil domain containing 183"
location: "9q34.3"
module: 21
arm: "+"
pooled_cpm: 4.27
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CCDC183

*coiled-coil domain containing 183* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.21× (z +20.5, q 0e+00, up in 21 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.64× (z +5.6, q 3e-06, up in 17 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.412× (z -10.0, q 1e-20, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK5RAP3]] (+0.64, fdr 1e-05), [[GSTM2]] (+0.63, fdr 1e-05), [[TCEA2]] (+0.61, fdr 5e-05); moves opposite to [[C14orf119]] (-0.58, fdr 1e-05), [[CCDC137]] (-0.58, fdr 3e-05), [[RPL7L1]] (-0.54, fdr 2e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.21×** | +20.5 | 0e+00 | 21/21 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.51×** | +20.2 | 0e+00 | 7/8 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.54×** | +15.7 | 0e+00 | 9/11 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.0 | 3e-07 | 8/21 (NCI-H2347, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +5.6 | 3e-06 | 17/44 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.7 | 2e-04 | 7/34 (HS-578T, HEC-1-A, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.33×** | +4.5 | 5e-04 | 8/41 (LS 180, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.011 | 6/43 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **1.85×** | +3.6 | 0.020 | 3/27 (COLO 205, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.020 | 13/42 (SK-MEL-2, CFPAC-1, …) | two highest doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.030 | 0/43 | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.036 | 10/45 (LoVo, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.052 | 7/40 (HepG2/C3A, LS 180, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.072 | 7/43 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.083 | 2/40 (COLO 205, HCT15) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.093 | 11/43 (CFPAC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.412×** | -10.0 | 1e-20 | 30/42 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.467×** | -8.2 | 6e-14 | 22/38 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.631×** | -5.0 | 9e-05 | 13/41 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -5.0 | 9e-05 | 20/33 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.693×** | -4.1 | 0.004 | 13/45 (HOP62, A-427, …) | top dose only | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.702×** | -4.0 | 0.007 | 8/44 (Panc 03.27, H4, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -3.6 | 0.027 | 8/31 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -3.6 | 0.027 | 9/38 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.718×** | -3.5 | 0.027 | 10/39 (C32, HOP62, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.733×** | -3.5 | 0.027 | 10/41 (HT-29, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.805×** | -3.4 | 0.029 | 15/32 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Clopidogrel (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.055 | 5/43 (HepG2/C3A, CHP-212, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **0.823×** | -3.1 | 0.087 | 8/41 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.765× | -3.0 | 0.11 | 8/41 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.63 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 22.1× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 6.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -10.8) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0861× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 3.99 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0668× (z -9.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.0650× (z -9.0) |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0615× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 6.49 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -13.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H460 (line)]] | wt | 2.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0934× (z -8.6) |
| [[PANC-1 (line)]] | alt | 3.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0761× (z -14.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[SNU-423 (line)]] | alt | 3.63 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0360× (z -10.0) |
| [[SW480 (line)]] | alt | 4.41 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK5RAP3]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GSTM2]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TCEA2]] | +0.61 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[ABCA2]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 | STRING 504 |
| [[CTC1]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PXN-AS1]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[AJM1]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 | ⚠ same locus (34.7 kb, same strand: neighbours can correlate without regulation) |
| [[PNKD]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[NPDC1]] | +0.55 | +0.45 / +0.50 | both halves | 3e-05 | STRING 539 |
| [[ZC3H3]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PRMT5-DT]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SLC16A13]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[COL18A1]] | +0.54 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C14orf119]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.58 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[RPL7L1]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NOL11]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[UTP3]] | -0.52 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[MRM2]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[VPS25]] | -0.51 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[FADD]] | -0.51 | -0.29 / -0.62 | both halves | 3e-04 |  |
| [[TASOR2]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ABRAXAS2]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[EIF6]] | -0.49 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[KIFBP]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.288). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.2, 28.5); signed map (-28.6, -2.8). **Vector** length 64.0, 9.96% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +20.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +20.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 183 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,796,338-136,807,741 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15438, bA216L13.7; previously KIAA1984 |
| Matched by | ensembl_id |

UniProt [Q5T5S1](https://www.uniprot.org/uniprotkb/Q5T5S1) carries no function annotation.

**Summary**, from NCBI Gene [84960](https://www.ncbi.nlm.nih.gov/gene/84960):

> Predicted to act upstream of or within several processes, including centriole assembly; cytoplasm organization; and spermatid development. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28236) · Entrez [84960](https://www.ncbi.nlm.nih.gov/gene/84960) · UniProt [Q5T5S1](https://www.uniprot.org/uniprotkb/Q5T5S1) · Ensembl [ENSG00000213213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213213)

## Data

Gene col 13091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13091); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13091]; `tensor/DDL_lfc|DDL_z.npy` [13091]; `embed/gene_vectors.npy` [13091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13091 or target_col == 13091). Every well: [[CCDC183 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC183.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
