---
symbol: "CCDC148"
type: "gene"
col: 7706
ensembl_id: "ENSG00000153237"
name: "coiled-coil domain containing 148"
location: "2q24.1"
module: 14
arm: "+"
pooled_cpm: 13.37
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 15
n_dd_up_clean: 29
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CCDC148

*coiled-coil domain containing 148* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.12× (z +29.9, q 0e+00, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.393× (z -10.9, q 8e-25, down in 30 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.426× (z -9.9, q 9e-21, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DZIP3]] (+0.66, fdr 1e-05), [[SGO1-AS1]] (+0.64, fdr 1e-05), [[FBXO48]] (+0.64, fdr 1e-05); moves opposite to [[ADPGK]] (-0.68, fdr 7e-06), [[WDR5]] (-0.64, fdr 1e-05), [[AHSA1]] (-0.63, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MARCKS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 3 with an alert ⚠; shown: the 15 strongest. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.12×** | +29.9 | 0e+00 | 40/41 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **7.06×** | +22.8 | 0e+00 | 45/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.98×** | +20.8 | 0e+00 | 45/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.61×** | +20.1 | 0e+00 | 45/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.18×** | +19.0 | 0e+00 | 40/42 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.31×** | +16.4 | 0e+00 | 44/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.60×** | +14.9 | 0e+00 | 41/41 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.15×** | +12.9 | 6e-36 | 37/43 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +11.9 | 1e-30 | 38/45 (NCI-H2347, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.34×** | +9.9 | 2e-21 | 36/44 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.92×** | +9.7 | 1e-20 | 41/46 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.29×** | +9.6 | 3e-20 | 35/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.6 | 1e-12 | 32/45 (A498, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +7.6 | 1e-12 | 25/41 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +5.4 | 3e-06 | 25/45 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.393×** | -10.9 | 8e-25 | 30/42 (SK-MEL-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.426×** | -9.9 | 9e-21 | 36/45 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -8.5 | 4e-15 | 33/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.509×** | -7.9 | 6e-13 | 27/45 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.541×** | -7.2 | 9e-11 | 33/45 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.582×** | -6.3 | 3e-08 | 29/44 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.600×** | -5.6 | 2e-06 | 28/44 (HT-29, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -5.2 | 1e-05 | 22/40 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -4.7 | 1e-04 | 19/44 (HT-29, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.684×** | -4.3 | 0.001 | 18/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.715×** | -3.9 | 0.005 | 15/45 (SW1417, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -3.8 | 0.006 | 13/45 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.735×** | -3.5 | 0.024 | 14/45 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.821×** | -3.2 | 0.047 | 11/46 (HEC-1-A, COLO 205, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.760×** | -3.0 | 0.096 | 12/45 (SNU-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.1 | 7 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +14.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -14.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.135× (z -13.1) |
| [[LoVo (line)]] | wt | 5.78 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +16.8) | — |
| [[LS 180 (line)]] | wt | 6.86 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.7× (z +18.5) | — |
| [[A-172 (line)]] | wt | 13.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +20.3) | — |
| [[HT-29 (line)]] | alt | 34.9 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +16.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.233× (z -9.4) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.245× (z -8.9) |
| [[PANC-1 (line)]] | alt | 7.94 | 7 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 17.7× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +21.6) | [[Digitoxin (drug)]] 5 µM 0.188× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 20.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +18.0) | — |
| [[NCI-H460 (line)]] | wt | 3.59 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 27.1 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +13.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -10.3) |
| [[A-427 (line)]] | wt | 18.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +11.7) | — |
| [[A498 (line)]] | wt | 16.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +13.6) | — |
| [[A549 (line)]] | wt | 12.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 3 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.4) | [[Ixazomib citrate (drug)]] 0.5 µM 0.204× (z -9.7) |
| [[J82 (line)]] | alt | 17.4 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +18.5) | [[Bortezomib (drug)]] 0.05 µM 0.209× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 18.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +15.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0718× (z -16.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 16.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.7× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 7.00 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +12.4) | — |
| [[KATO III (line)]] | alt | 9.61 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +15.7) | — |
| [[HCT15 (line)]] | alt | 25.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.118× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.119× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 8.40 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 6.08 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +14.7) | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 34.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.36× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.252× (z -8.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 9.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +15.4) | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0521× (z -12.0) |
| [[SNU-423 (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 21.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.27× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +14.7) | — |
| [[HS-578T (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 21.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 4.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +8.6) | — |
| [[RKO (line)]] | wt | 4.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.2× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 5.98 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM 0.0544× (z -8.7) |
| [[SHP-77 (line)]] | alt | 13.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZIP3]] | +0.66 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | +0.64 | +0.83 / +0.52 | both halves | 1e-05 |  |
| [[FBXO48]] | +0.64 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[KLRC2]] | +0.63 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[GASAL1]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[ZFHX2]] | +0.63 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[POGZ]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NUAK2]] | +0.62 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[LIMA1]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[NOTCH2NLA]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NR3C1]] | +0.60 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[NFKBIE]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADPGK]] | -0.68 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[WDR5]] | -0.64 | -0.74 / -0.52 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.62 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[DCUN1D2]] | -0.60 | -0.73 / -0.30 | both halves | 2e-04 |  |
| [[HERC2P3]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[UFD1]] | -0.59 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[HERC2P9]] | -0.58 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[PDS5A]] | -0.58 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[RPUSD4]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[HSF1]] | -0.58 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[CMTM4]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCKS]] | B | MARCKS activity raises CCDC148's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without MARCKS | 0.038 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[VAV1]] | B | VAV1 activity raises CCDC148's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without VAV1 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CCDC148's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RPS6KA6]] | B | RPS6KA6 activity raises CCDC148's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without RPS6KA6 | 0.067 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |
| [[IL18]] | B | IL18 activity strengthens CCDC148's drug response | lines that do not express IL18 (18) vs lines expressing it (28) | the lines without IL18 respond 0.74× as strongly (z diff +1.36); strongest at Harringtonine 5 µM: 2.29x vs 3.67x (z diff +2.5) | 0.070 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3; target measured in part of the lines; artifact flags |
| [[GRIK4]] | B | GRIK4 activity raises CCDC148's level | lines that do not express GRIK4 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without GRIK4 | 0.076 | ⚠ within organs, on part of the lines; also absent: PRKAA2, RADIL, CHN1; maybe low, not absent |
| [[CHRM3]] | B | CHRM3 activity raises CCDC148's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 1.63× lower at baseline in the lines without CHRM3 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[TEX9]] | C | TEX9 activity raises CCDC148's level | lines that do not express TEX9 (3) vs lines expressing it (47) | 3.26× lower at baseline in the lines without TEX9 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: ZMAT3, PDE4C, LCA5; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, 8.4); signed map (44.1, 2.8). **Vector** length 74.7, 16.9% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +29.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +11.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +14.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -9.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.1 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -3.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.8 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 148 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.1 — chr2:158,171,073-158,456,753 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC125588 |
| Matched by | ensembl_id |

UniProt [Q8NFR7](https://www.uniprot.org/uniprotkb/Q8NFR7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25191) · Entrez [130940](https://www.ncbi.nlm.nih.gov/gene/130940) · UniProt [Q8NFR7](https://www.uniprot.org/uniprotkb/Q8NFR7) · Ensembl [ENSG00000153237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153237)

## Data

Gene col 7706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7706); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7706]; `tensor/DDL_lfc|DDL_z.npy` [7706]; `embed/gene_vectors.npy` [7706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7706 or target_col == 7706). Every well: [[CCDC148 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC148.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
