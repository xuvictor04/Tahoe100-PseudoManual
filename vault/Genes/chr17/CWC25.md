---
symbol: "CWC25"
type: "gene"
col: 15790
ensembl_id: "ENSG00000273559"
name: "CWC25 spliceosome associated protein"
location: "17q12"
module: 118
arm: "+"
pooled_cpm: 59.04
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# CWC25

*CWC25 spliceosome associated protein* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.94× (z +23.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.757× (z -6.0, q 1e-06, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK19]] (+0.68, fdr 7e-06), [[TTF1]] (+0.67, fdr 7e-06), [[KLC4]] (+0.66, fdr 7e-06); moves opposite to [[GLO1]] (-0.63, fdr 1e-05), [[IDH3A]] (-0.61, fdr 1e-05), [[NAE1]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.94×** | +23.1 | 0e+00 | 46/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.19×** | +16.7 | 0e+00 | 48/49 (BT-474, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.00×** | +16.6 | 0e+00 | 48/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.85×** | +10.7 | 1e-24 | 40/48 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.04×** | +10.4 | 3e-23 | 45/48 (BT-474, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.96×** | +10.2 | 2e-22 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.82×** | +9.1 | 9e-18 | 41/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +7.1 | 7e-11 | 39/48 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.1 | 6e-08 | 33/49 (BT-474, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.45×** | +5.6 | 1e-06 | 34/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 1e-05 | 31/48 (KATO III, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.41×** | +5.2 | 1e-05 | 34/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.2 | 1e-05 | 33/47 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 31/48 (BT-474, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +5.1 | 1e-05 | 32/48 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.007 | 27/49 (Panc 03.27, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.065 | 17/47 (NCI-H1573, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.757×** | -6.0 | 1e-06 | 35/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.713×** | -5.1 | 8e-05 | 35/48 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.729×** | -4.6 | 8e-04 | 21/41 (CHP-212, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.771×** | -3.9 | 0.012 | 27/48 (J82, PANC-1, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.790×** | -3.6 | 0.039 | 22/48 (SW 1088, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 347 | 9 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +20.2) | [[Tucidinostat (drug)]] 5 µM 0.617× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 39.5 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +20.5) | — |
| [[PANC-1 (line)]] | alt | 33.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +19.6) | — |
| [[SW480 (line)]] | alt | 47.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 44.9 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +18.5) | — |
| [[LS 180 (line)]] | wt | 41.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 54.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +19.1) | — |
| [[A549 (line)]] | wt | 63.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +17.9) | — |
| [[HEC-1-A (line)]] | alt | 44.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +16.6) | — |
| [[KATO III (line)]] | alt | 67.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +15.2) | — |
| [[LoVo (line)]] | wt | 37.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +17.0) | — |
| [[LOX-IMVI (line)]] | wt | 45.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +19.5) | — |
| [[NCI-H1792 (line)]] | alt | 41.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 126 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 63.9 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +16.9) | — |
| [[A-427 (line)]] | wt | 46.5 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 12.1× (z +11.5) | — |
| [[A498 (line)]] | wt | 99.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +20.1) | — |
| [[COLO 205 (line)]] | alt | 79.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 23.9× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 51.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.6) | — |
| [[HT-29 (line)]] | alt | 80.2 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.23× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +11.4) | — |
| [[RKO (line)]] | wt | 38.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 13.6× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 53.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 48.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +14.9) | — |
| [[SW1417 (line)]] | alt | 63.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.26× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 53.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.2) | — |
| [[C32 (line)]] | wt | 40.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +17.3) | — |
| [[CFPAC-1 (line)]] | alt | 100 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.2) | — |
| [[CHP-212 (line)]] | wt | 87.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0946× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 50.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 39.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 58.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 59.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 60.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +16.8) | — |
| [[HCT15 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 34.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.4) | — |
| [[J82 (line)]] | alt | 48.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 40.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 19.1× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 42.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +15.8) | — |
| [[SW48 (line)]] | wt | 45.4 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.65× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK19]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TTF1]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[KLC4]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZNF324]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[OSCP1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[NFKBIL1]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[PI4KB]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SPOP]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[BBOF1]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLO1]] | -0.63 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[IDH3A]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[NAE1]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[RPE]] | -0.60 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[GMPS]] | -0.60 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[IPO5]] | -0.58 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[TMX1]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[EEF1E1]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ICMT]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[METAP1]] | -0.56 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[TUBGCP4]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.685). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.0, -5.2); signed map (-7.7, -2.8). **Vector** length 87.7, 25.1% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +16.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +23.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +6.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | -0.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.9 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | CWC25 spliceosome associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,800,441-38,825,355 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20291; previously CCDC49 |
| Gene groups (HGNC) | NTC associated proteins; Spliceosomal Bact complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXE8](https://www.uniprot.org/uniprotkb/Q9NXE8) (Pre-mRNA-splicing factor CWC25 homolog):

> Involved in pre-mRNA splicing as component of the spliceosome.

**Summary**, from NCBI Gene [54883](https://www.ncbi.nlm.nih.gov/gene/54883):

> This gene encodes a factor that is part of the multi-protein C complex involved in pre-mRNA splicing. Alternatively spliced transcripts have been described for this gene. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:25989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25989) · Entrez [54883](https://www.ncbi.nlm.nih.gov/gene/54883) · UniProt [Q9NXE8](https://www.uniprot.org/uniprotkb/Q9NXE8) · Ensembl [ENSG00000273559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273559)

## Data

Gene col 15790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15790); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15790]; `tensor/DDL_lfc|DDL_z.npy` [15790]; `embed/gene_vectors.npy` [15790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15790 or target_col == 15790). Every well: [[CWC25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CWC25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
