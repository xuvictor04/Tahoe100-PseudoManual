---
symbol: "RANBP3"
type: "gene"
col: 403
ensembl_id: "ENSG00000031823"
name: "RAN binding protein 3"
location: "19p13.3"
module: 153
arm: "+"
pooled_cpm: 37.73
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# RANBP3

*RAN binding protein 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 3.22× (z +7.2, q 2e-10, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.448× (z -9.6, q 7e-19, down in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.714× (z -4.0, q 0.008, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (RKO 0.182×, LOX-IMVI 0.248×, SW48 0.172×, LoVo 0.298×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.127×, Hs 766T 0.0952×, LS 180 0.231×, SW480 0.335×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW 900 0.136×, HS-578T 0.228×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC2]] (+0.68, fdr 7e-06), [[MFN2]] (+0.66, fdr 7e-06), [[KMT2D]] (+0.64, fdr 1e-05); moves opposite to [[GNG5]] (-0.52, fdr 5e-05), [[SYP]] (-0.52, fdr 3e-05), [[SMIM30]] (-0.51, fdr 1e-05).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.22×** | +7.2 | 2e-10 | 45/48 (RKO, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +7.1 | 3e-10 | 42/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +6.6 | 1e-08 | 44/49 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +5.1 | 4e-05 | 29/48 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.014 | 30/48 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +3.8 | 0.014 | 26/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.015 | 25/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.020 | 25/48 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +3.6 | 0.023 | 24/48 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.058 | 21/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 403.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (RKO 0.182×, LOX-IMVI 0.248×, SW48 0.172×, LoVo 0.298×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.127×, Hs 766T 0.0952×, LS 180 0.231×, SW480 0.335×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW 900 0.136×, HS-578T 0.228×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.448×** | -9.6 | 7e-19 | 39/46 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -7.2 | 2e-10 | 32/41 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.662×** | -4.6 | 1e-03 | 28/45 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.714×** | -4.0 | 0.008 | 27/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -4.0 | 0.008 | 24/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 28.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -9.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 39.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.36× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -11.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 53.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -13.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 48.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -12.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 50.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -9.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0952× (z -15.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -10.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -15.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC2]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MFN2]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[KMT2D]] | +0.64 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[NDOR1]] | +0.63 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ATP13A1]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[WASH8P]] ⚠ | +0.59 | +0.55 / +0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SF3B4]] | +0.59 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[MTX1]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TOR1A]] | +0.59 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ZNF304]] | +0.59 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[NAXD]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.58 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MSANTD7]] | +0.58 | +0.32 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG5]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[SYP]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SMIM30]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CHMP2B]] | -0.48 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[UGCG]] | -0.48 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[RAP1B]] | -0.47 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[GABARAPL2]] | -0.47 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[USP53]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.6, -27.6); signed map (-14.4, -32.2). **Vector** length 64.1, 13.0% of its response variance represented; |z| ≥ 3 in 735 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.4 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | -7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | -9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +0.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.6 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | RAN binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,916,139-5,978,142 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6Z4](https://www.uniprot.org/uniprotkb/Q9H6Z4) (Ran-binding protein 3):

> Acts as a cofactor for XPO1/CRM1-mediated nuclear export, perhaps as export complex scaffolding protein. Bound to XPO1/CRM1, stabilizes the XPO1/CRM1-cargo interaction. In the absence of Ran-bound GTP prevents binding of XPO1/CRM1 to the nuclear pore complex. Binds to CHC1/RCC1 and increases the guanine nucleotide exchange activity of CHC1/RCC1. Recruits XPO1/CRM1 to CHC1/RCC1 in a Ran-dependent manner. Negative regulator of TGF-beta signaling through interaction with the R-SMAD proteins, SMAD2 …

**Summary**, from NCBI Gene [8498](https://www.ncbi.nlm.nih.gov/gene/8498):

> This gene encodes a protein with a RanBD1 domain that is found in both the nucleus and cytoplasm. This protein plays a role in nuclear export as part of a heteromeric complex. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9850) · Entrez [8498](https://www.ncbi.nlm.nih.gov/gene/8498) · UniProt [Q9H6Z4](https://www.uniprot.org/uniprotkb/Q9H6Z4) · Ensembl [ENSG00000031823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000031823)

## Data

Gene col 403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 403); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 403]; `tensor/DDL_lfc|DDL_z.npy` [403]; `embed/gene_vectors.npy` [403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 403 or target_col == 403). Every well: [[RANBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
