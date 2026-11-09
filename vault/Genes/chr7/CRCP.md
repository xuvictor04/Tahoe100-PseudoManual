---
symbol: "CRCP"
type: "gene"
col: 14262
ensembl_id: "ENSG00000241258"
name: "CGRP receptor component"
location: "7q11.21"
module: 11
arm: "+"
pooled_cpm: 60.7
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CRCP

*CGRP receptor component* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +22.8, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.264×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.554×; ⚠ cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.260×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0843×); [[Cytarabine (drug)]] 0.05 µM in 1 line (SW 1088 0.0756×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3C]] (+0.68, fdr 7e-06), [[NOL8]] (+0.66, fdr 7e-06), [[RNF115]] (+0.66, fdr 7e-06); moves opposite to [[TMED4]] (-0.62, fdr 7e-06), [[BSG]] (-0.62, fdr 1e-05), [[MLF2]] (-0.61, fdr 9e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +22.8 | 0e+00 | 46/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +18.6 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +15.5 | 0e+00 | 43/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +13.0 | 1e-36 | 43/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +11.0 | 2e-26 | 40/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +10.3 | 8e-23 | 36/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +9.0 | 2e-17 | 33/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +8.1 | 3e-14 | 36/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +6.9 | 2e-10 | 26/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +6.7 | 8e-10 | 28/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +6.6 | 3e-09 | 28/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +6.5 | 3e-09 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +6.2 | 3e-08 | 28/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +6.1 | 4e-08 | 28/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +4.9 | 4e-05 | 18/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 7e-05 | 17/48 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | 1.16× | +3.6 | 0.011 | 13/48 (Panc 03.27, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.020 | 16/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.022 | 9/47 (SK-MEL-2, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14262.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.264×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.554×; ⚠ cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.260×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0843×); [[Cytarabine (drug)]] 0.05 µM in 1 line (SW 1088 0.0756×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.838× | -4.3 | 0.010 | 21/48 (SNU-423, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -3.6 | 0.079 | 18/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.964× | -3.1 | 0.33 | 0/49 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 102 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +17.8) | — |
| [[PANC-1 (line)]] | alt | 52.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +18.8) | — |
| [[NCI-H460 (line)]] | wt | 50.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +17.8) | — |
| [[A-427 (line)]] | wt | 39.9 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.60× (z +8.9) | — |
| [[A549 (line)]] | wt | 45.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 82.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.511× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HOP62 (line)]] | alt | 46.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +21.6) | — |
| [[LoVo (line)]] | wt | 56.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +17.0) | — |
| [[A-172 (line)]] | wt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.2) | — |
| [[A498 (line)]] | wt | 81.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 77.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +10.2) | — |
| [[KATO III (line)]] | alt | 95.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.509× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.655× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 36.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 72.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 54.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 41.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.8) | — |
| [[SW48 (line)]] | wt | 75.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.85× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[AsPC-1 (line)]] | alt | 71.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C32 (line)]] | wt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.7) | — |
| [[H4 (line)]] | wt | 67.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.264× (z -11.2) |
| [[HS-578T (line)]] | alt | 55.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.0) | — |
| [[J82 (line)]] | alt | 52.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 41.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 58.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 50.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 60.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 79.8 | 0 | 1 | — | [[Cytarabine (drug)]] 0.05 µM 0.0756× (z -8.8) |
| [[SW 1271 (line)]] | alt | 50.2 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0843× (z -9.2) |
| [[AN3 CA (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 94.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3C]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 | same gene group; pathway: Cytosolic sensors of pathogen-associated DNA; STRING 999 |
| [[NOL8]] | +0.66 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[RNF115]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.66 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[DOHH]] | +0.65 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[RPL7L1]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.62 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[PPIG]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZNF830]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[GPATCH8]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ESF1]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED4]] | -0.62 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[BSG]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[MLF2]] | -0.61 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[NAGA]] | -0.60 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ITM2C]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CALM3]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[BRK1]] | -0.57 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[TMBIM6]] | -0.56 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[BPNT2]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CNPY3]] | -0.55 | -0.62 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.8, 6.0); signed map (-0.7, -19.6). **Vector** length 85.0, 18.8% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +18.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +22.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +15.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +13.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +6.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +1.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -1.7 | -4.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.5 | -0.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | CGRP receptor component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:66,114,604-66,154,568 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGRP-RCP, RCP, RCP9, C17, POLR3I |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [O75575](https://www.uniprot.org/uniprotkb/O75575) (DNA-directed RNA polymerase III subunit RPC9):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Specific peripheric component of RNA polymerase III (Pol III) which synthesizes small non-coding RNAs including 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. With POLR3H/RPC8 forms a mobile stalk that protrudes from Pol III core and functions primarily in transcription initiation (By similarity). Pol III plays a key role in sensing and …

**Summary**, from NCBI Gene [27297](https://www.ncbi.nlm.nih.gov/gene/27297):

> This gene encodes a membrane protein that functions as part of a receptor complex for a small neuropeptide that increases intracellular cAMP levels. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17888) · Entrez [27297](https://www.ncbi.nlm.nih.gov/gene/27297) · UniProt [O75575](https://www.uniprot.org/uniprotkb/O75575) · Ensembl [ENSG00000241258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241258)

## Data

Gene col 14262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14262); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14262]; `tensor/DDL_lfc|DDL_z.npy` [14262]; `embed/gene_vectors.npy` [14262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14262 or target_col == 14262). Every well: [[CRCP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRCP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
