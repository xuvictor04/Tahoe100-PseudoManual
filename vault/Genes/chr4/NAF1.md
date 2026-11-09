---
symbol: "NAF1"
type: "gene"
col: 6989
ensembl_id: "ENSG00000145414"
name: "nuclear assembly factor 1 ribonucleoprotein"
location: "4q32.2"
module: 5
arm: "+"
pooled_cpm: 45.35
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NAF1

*nuclear assembly factor 1 ribonucleoprotein* — 4q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.81× (z +17.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.799× (z -5.5, q 3e-05, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.129×, SNU-1 0.198×, AN3 CA 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.246×, NCI-H23 0.194×, RKO 0.298×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (H4 0.220×, SW 900 0.273×; ⚠ transcription drop; cell-cycle shift, explains ~13% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (C32 0.249×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRNT1]] (+0.68, fdr 1e-05), [[ANAPC1]] (+0.68, fdr 7e-06), [[MRPS25]] (+0.63, fdr 3e-05); moves opposite to [[BIK]] (-0.62, fdr 1e-05), [[SNAPIN]] (-0.62, fdr 1e-05), [[SLC9A3R2]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CDC42BPG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.81×** | +17.5 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.32×** | +14.3 | 1e-43 | 46/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +13.6 | 1e-39 | 42/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.04×** | +12.1 | 1e-31 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +12.0 | 3e-31 | 39/48 (Panc 03.27, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +9.5 | 3e-19 | 40/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +8.4 | 4e-15 | 37/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.56×** | +8.3 | 5e-15 | 41/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +7.9 | 1e-13 | 32/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +7.8 | 2e-13 | 39/49 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.2 | 3e-11 | 34/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.8 | 7e-10 | 33/47 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.48×** | +6.7 | 1e-09 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.6 | 2e-09 | 31/48 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +6.4 | 4e-09 | 21/34 (NCI-H1573, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.43×** | +6.1 | 5e-08 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +5.2 | 5e-06 | 21/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.001 | 22/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.043 | 16/48 (BT-474, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.059 | 16/48 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6989.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.129×, SNU-1 0.198×, AN3 CA 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.246×, NCI-H23 0.194×, RKO 0.298×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (H4 0.220×, SW 900 0.273×; ⚠ transcription drop; cell-cycle shift, explains ~13% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (C32 0.249×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -5.5 | 3e-05 | 28/48 (A498, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.0 | 0.016 | 2/49 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.798×** | -3.9 | 0.016 | 23/46 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.730×** | -3.9 | 0.016 | 21/47 (SHP-77, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.815×** | -3.5 | 0.048 | 18/48 (CHP-212, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.834× | -3.1 | 0.17 | 16/47 (H4, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.839× | -3.0 | 0.19 | 11/47 (KATO III, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 46.9 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.55× (z +14.2) | — |
| [[NCI-H460 (line)]] | wt | 47.1 | 9 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.67× (z +19.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +15.2) | — |
| [[LoVo (line)]] | wt | 59.7 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +14.0) | — |
| [[SW480 (line)]] | alt | 56.8 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 39.5 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 33.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.56× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 40.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.10× (z +13.7) | — |
| [[BT-474 (line)]] | alt | 27.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +10.9) | [[Simotinib (drug)]] 5 µM 0.239× (z -8.8) ⚠ toxic |
| [[C32 (line)]] | wt | 35.9 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.3) | [[Canagliflozin (drug)]] 0.05 µM 0.249× (z -9.4) |
| [[HOP62 (line)]] | alt | 45.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 43.0 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.03× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 25.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 31.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.93× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 44.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 36.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -13.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 91.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -12.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.81× (z +9.9) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0744× (z -10.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 69.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 57.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +9.8) | [[Docetaxel (drug)]] 0.05 µM 0.273× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change |
| [[A-427 (line)]] | wt | 52.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.32× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 71.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 96.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +11.6) | — |
| [[H4 (line)]] | wt | 55.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.220× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change |
| [[HT-29 (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 33.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.8) | — |
| [[A-172 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNT1]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ANAPC1]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[MRPS25]] | +0.63 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[PACRGL]] | +0.62 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[ATR]] | +0.62 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[STARD7-AS1]] | +0.62 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[GTF3C2-AS2]] | +0.62 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[MSANTD2]] | +0.61 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[MCM9]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[NDUFAF6]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[SNX5]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIK]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.62 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SLC9A3R2]] | -0.61 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ALAS1]] | -0.60 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[KLF2]] | -0.58 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DNAJB2]] | -0.57 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ARL4D]] | -0.57 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[GDPD5]] | -0.57 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[RAB11FIP1]] | -0.57 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[DHRS2]] | -0.57 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[DLGAP4]] | -0.57 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TUFT1]] | -0.56 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42BPG]] | B | CDC42BPG activity lowers NAF1's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.36× higher at baseline in the lines without CDC42BPG | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[IRF6]] | B | IRF6 activity lowers NAF1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.24× higher at baseline in the lines without IRF6 | 0.027 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TCN2]] | B | TCN2 activity lowers NAF1's level | lines that do not express TCN2 (12) vs lines expressing it (38) | 1.35× higher at baseline in the lines without TCN2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRSS23, TMSB4X, ARHGAP23; maybe low, not absent |
| [[TUBA1A]] | B | TUBA1A activity raises NAF1's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 1.21× lower at baseline in the lines without TUBA1A | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-11.8, -32.5); signed map (-0.6, -50.6). **Vector** length 92.3, 24.9% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.7 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +14.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | -0.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | +5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -3.1 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear assembly factor 1 ribonucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.2 — chr4:163,110,073-163,166,890 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HR8](https://www.uniprot.org/uniprotkb/Q96HR8) (H/ACA ribonucleoprotein complex non-core subunit NAF1):

> RNA-binding protein required for the maturation of box H/ACA snoRNPs complex and ribosome biogenesis. During assembly of the H/ACA snoRNPs complex, it associates with the complex and disappears during maturation of the complex and is replaced by NOLA1/GAR1 to yield mature H/ACA snoRNPs complex. Probably competes with NOLA1/GAR1 for binding with DKC1/NOLA4.

**Summary**, from NCBI Gene [92345](https://www.ncbi.nlm.nih.gov/gene/92345):

> Enables identical protein binding activity and telomerase RNA binding activity. Involved in ribosome biogenesis; telomerase RNA stabilization; and telomerase holoenzyme complex assembly. Acts upstream of or within telomerase RNA localization to Cajal body. Located in cytosol and nucleoplasm. Part of sno(s)RNA-containing ribonucleoprotein complex. Implicated in melanoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25126) · Entrez [92345](https://www.ncbi.nlm.nih.gov/gene/92345) · UniProt [Q96HR8](https://www.uniprot.org/uniprotkb/Q96HR8) · Ensembl [ENSG00000145414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145414)

## Data

Gene col 6989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6989); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6989]; `tensor/DDL_lfc|DDL_z.npy` [6989]; `embed/gene_vectors.npy` [6989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6989 or target_col == 6989). Every well: [[NAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
