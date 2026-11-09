---
symbol: "TMEM38B"
type: "gene"
col: 1738
ensembl_id: "ENSG00000095209"
name: "transmembrane protein 38B"
location: "9q31.2"
module: 45
arm: "+"
pooled_cpm: 42.21
n_lines_expressing: 50
n_dd_up: 51
n_dd_down: 0
n_dd_up_clean: 37
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# TMEM38B

*transmembrane protein 38B* — 9q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.02× (z +19.7, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +17.7, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.0671×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (AsPC-1 0.224×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIBAR1]] (+0.58, fdr 3e-05), [[SGCE]] (+0.57, fdr 1e-04), [[ACO1]] (+0.57, fdr 2e-05); moves opposite to [[SAP30BP]] (-0.51, fdr 2e-05), [[TUBB4B]] (-0.51, fdr 9e-05), [[FBXL18]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STEAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.02×** | +19.7 | 0e+00 | 46/48 (LoVo, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +17.7 | 0e+00 | 46/48 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.70×** | +17.7 | 0e+00 | 48/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.54×** | +16.6 | 0e+00 | 46/48 (LS 180, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.31×** | +14.9 | 0e+00 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +13.8 | 4e-41 | 43/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +13.7 | 7e-41 | 43/48 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.03×** | +12.6 | 2e-34 | 42/48 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +12.4 | 1e-33 | 43/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.03×** | +12.3 | 8e-33 | 32/45 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.93×** | +11.7 | 6e-30 | 41/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.41×** | +11.4 | 2e-28 | 43/49 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.88×** | +11.3 | 7e-28 | 41/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.73×** | +9.8 | 6e-21 | 40/47 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +9.7 | 2e-20 | 38/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +9.6 | 2e-20 | 37/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +9.4 | 1e-19 | 36/48 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +8.7 | 1e-16 | 36/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.29×** | +7.7 | 3e-13 | 40/48 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +7.7 | 3e-13 | 35/48 (KATO III, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1738.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.0671×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (AsPC-1 0.224×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | 0.817× | -3.6 | 0.10 | 14/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.819× | -3.6 | 0.10 | 9/48 (COLO 205, SHP-77, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.763× | -3.4 | 0.11 | 16/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.876× | -3.3 | 0.12 | 15/48 (CFPAC-1, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.9 | 17 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.63× (z +16.6) | — |
| [[NCI-H1573 (line)]] | alt | 15.2 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.36× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +15.9) | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.2) | [[Docetaxel (drug)]] 0.05 µM 0.224× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 33.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +14.7) | — |
| [[COLO 205 (line)]] | alt | 29.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +13.0) | — |
| [[H4 (line)]] | wt | 34.2 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.24× (z +10.4) | — |
| [[LoVo (line)]] | wt | 38.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +15.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.00× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 39.4 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +11.5) | — |
| [[A-427 (line)]] | wt | 16.2 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.99× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.98× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 69.6 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.30× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 24.8 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.80× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 36.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.8) | — |
| [[J82 (line)]] | alt | 86.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.7) | — |
| [[KATO III (line)]] | alt | 41.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 39.8 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.43× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 84.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.6) | — |
| [[SW480 (line)]] | alt | 60.3 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.27× (z +10.1) | — |
| [[A-172 (line)]] | wt | 43.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +19.0) | — |
| [[A549 (line)]] | wt | 28.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 18.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 36.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 38.6 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.40× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 17.8 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.82× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 39.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.63× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 20.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 26.6 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.65× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.58× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 43.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +9.9) | — |
| [[A498 (line)]] | wt | 80.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0671× (z -18.5) ⚠ toxic |
| [[C-33 A (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.54× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 92.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 47.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.39× (z +9.4) | — |
| [[C32 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIBAR1]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[SGCE]] | +0.57 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[ACO1]] | +0.57 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[ARL8B]] | +0.54 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ASAH1]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CIAO2A]] | +0.53 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[CHPT1]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[BBS7]] | +0.52 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[RCBTB1]] | +0.52 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SOAT1]] | +0.52 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[PCGF5]] | +0.51 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[RHOQ]] | +0.51 | +0.54 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP30BP]] | -0.51 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TUBB4B]] | -0.51 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[FBXL18]] | -0.50 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[FAM32A]] | -0.49 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[ZNF324]] | -0.49 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[ZC3H18]] | -0.48 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[SETX]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[GON4L]] | -0.48 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[C11orf91]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[GCDH]] | -0.47 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[POLG]] | -0.47 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP2]] | B | STEAP2 activity lowers TMEM38B's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 1.37× higher at baseline in the lines without STEAP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT |
| [[RRAGD]] | B | RRAGD activity raises TMEM38B's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without RRAGD | 0.088 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.0, -10.3); signed map (-27.3, -7.7). **Vector** length 70.2, 18.8% of its response variance represented; |z| ≥ 3 in 1,490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +5.0 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +4.8 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +8.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +5.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | +17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.9 | +19.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.4 | +16.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 38B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.2 — chr9:105,694,541-105,776,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10493, bA219P18.1, D4Ertd89e, TRIC-B; previously C9orf87 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVV0](https://www.uniprot.org/uniprotkb/Q9NVV0) (Trimeric intracellular cation channel type B):

> Intracellular monovalent cation channel required for maintenance of rapid intracellular calcium release. Acts as a potassium counter-ion channel that functions in synchronization with calcium release from intracellular stores (By similarity). Activated by increased cytosolic Ca(2+) levels (By similarity).

**Summary**, from NCBI Gene [55151](https://www.ncbi.nlm.nih.gov/gene/55151):

> This gene encodes an intracellular monovalent cation channel that functions in maintenance of intracellular calcium release. Mutations in this gene may be associated with autosomal recessive osteogenesis. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:25535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25535) · Entrez [55151](https://www.ncbi.nlm.nih.gov/gene/55151) · UniProt [Q9NVV0](https://www.uniprot.org/uniprotkb/Q9NVV0) · Ensembl [ENSG00000095209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095209)

## Data

Gene col 1738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1738); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1738]; `tensor/DDL_lfc|DDL_z.npy` [1738]; `embed/gene_vectors.npy` [1738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1738 or target_col == 1738). Every well: [[TMEM38B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM38B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
