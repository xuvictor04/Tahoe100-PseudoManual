---
symbol: "GNL1"
type: "gene"
col: 12895
ensembl_id: "ENSG00000204590"
name: "G protein nucleolar 1"
location: "6p21.33"
module: 109
arm: "+"
pooled_cpm: 47.76
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# GNL1

*G protein nucleolar 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +22.0, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.764× (z -6.2, q 4e-07, down in 37 of 48 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.336×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H661 0.0916×); [[Almonertinib (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.198×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYNGAP1]] (+0.68, fdr 7e-06), [[PLEKHG2]] (+0.59, fdr 1e-05), [[TADA3]] (+0.57, fdr 1e-05); moves opposite to [[SEC24B]] (-0.57, fdr 1e-05), [[FHIP2A]] (-0.53, fdr 1e-05), [[MTM1]] (-0.53, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +22.0 | 0e+00 | 42/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +9.7 | 1e-19 | 30/48 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +9.5 | 6e-19 | 32/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +8.2 | 2e-14 | 30/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +7.8 | 8e-13 | 31/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +7.5 | 8e-12 | 28/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +7.2 | 4e-11 | 28/43 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +7.1 | 6e-11 | 29/45 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.9 | 4e-10 | 26/48 (Hs 766T, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +6.4 | 7e-09 | 26/48 (SW480, SK-MEL-2, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.7 | 1e-04 | 0/49 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +4.3 | 8e-04 | 21/48 (LoVo, SW480, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +4.3 | 8e-04 | 18/48 (NCI-H2030, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.001 | 18/49 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.8 | 0.005 | 12/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.007 | 11/48 (HepG2/C3A, SW1417, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.053 | 7/48 (HOP62, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12895.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.336×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H661 0.0916×); [[Almonertinib (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.198×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.764×** | -6.2 | 4e-07 | 37/48 (A498, A-427, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.796×** | -5.2 | 5e-05 | 22/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.895× | -3.6 | 0.051 | 6/48 (HT-29, AsPC-1, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.6 | 0.051 | 20/48 (SNU-1, RKO, …) | top dose only |  |
| [[Fumaric acid (drug)]] 0.5 µM |  | 0.871× | -3.2 | 0.13 | 5/48 (LoVo, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.13 | 5/49 (A549, A-427, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.869× | -3.1 | 0.13 | 12/47 (NCI-H23, HT-29, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.910× | -3.1 | 0.13 | 2/48 (SNU-423, SW 1088) | rises with dose | position effect removed |
| [[Adenine (drug)]] 5 µM |  | 0.910× | -3.1 | 0.13 | 2/48 (RPMI-7951, AN3 CA) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.1 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +23.0) | — |
| [[PANC-1 (line)]] | alt | 42.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.7) | — |
| [[A-172 (line)]] | wt | 30.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +15.4) | — |
| [[A498 (line)]] | wt | 31.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +18.8) | — |
| [[HEC-1-A (line)]] | alt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 40.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 40.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.9) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.418× (z -8.5) |
| [[J82 (line)]] | alt | 87.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +22.0) | — |
| [[LOX-IMVI (line)]] | wt | 53.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +16.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.407× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 30.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +18.1) | — |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +16.0) | — |
| [[A-427 (line)]] | wt | 63.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -11.4) |
| [[A549 (line)]] | wt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 43.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.6) | — |
| [[C32 (line)]] | wt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 50.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.7) | — |
| [[CHP-212 (line)]] | wt | 60.0 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.198× (z -8.6) |
| [[H4 (line)]] | wt | 60.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.2) | — |
| [[HepG2_C3A (line)]] | wt | 64.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 63.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.8) | — |
| [[LoVo (line)]] | wt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +19.8) | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +18.7) | — |
| [[NCI-H2030 (line)]] | alt | 66.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.0) | — |
| [[NCI-H661 (line)]] | alt | 51.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0916× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 64.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.9) | — |
| [[SW480 (line)]] | alt | 52.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.95× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNGAP1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PLEKHG2]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TADA3]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ASPHD1]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MTRF1L]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ZNF274]] | +0.54 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MYO1C]] | +0.54 | +0.60 / +0.43 | both halves | 4e-05 |  |
| [[RGL2]] | +0.54 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[EGR2]] | +0.54 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[STK19]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[IER2]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[STX10]] | +0.53 | +0.58 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC24B]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MTM1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[INPP4A]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[FAM135A]] | -0.51 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[SPECC1L]] | -0.51 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[TTC13]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[HACD3]] | -0.49 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[PPP2R5E]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[HINT1]] | -0.48 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[BMPR1A]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[WWP1]] | -0.47 | -0.56 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.576). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.2, 0.6); signed map (5.1, 28.8). **Vector** length 102, 23.3% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +22.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +9.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[Oxaliplatin (drug)]] 0.05 µM |  | +1.8 | +2.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | +0.5 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | G protein nucleolar 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,541,381-30,556,489 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSR1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P36915](https://www.uniprot.org/uniprotkb/P36915) (Guanine nucleotide-binding protein-like 1):

> Possible regulatory or functional link with the histocompatibility cluster.

**Summary**, from NCBI Gene [2794](https://www.ncbi.nlm.nih.gov/gene/2794):

> The GNL1 gene, identified in the human major histocompatibility complex class I region, shows a high degree of similarity with its mouse counterpart. The GNL1 gene is located less than 2 kb centromeric to HLA-E, in the same transcriptional orientation. GNL1 is telomeric to HLA-B and HLA-C. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4413) · Entrez [2794](https://www.ncbi.nlm.nih.gov/gene/2794) · UniProt [P36915](https://www.uniprot.org/uniprotkb/P36915) · Ensembl [ENSG00000204590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204590)

## Data

Gene col 12895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12895); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12895]; `tensor/DDL_lfc|DDL_z.npy` [12895]; `embed/gene_vectors.npy` [12895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12895 or target_col == 12895). Every well: [[GNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
