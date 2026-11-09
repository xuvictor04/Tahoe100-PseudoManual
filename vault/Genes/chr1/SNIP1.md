---
symbol: "SNIP1"
type: "gene"
col: 8800
ensembl_id: "ENSG00000163877"
name: "Smad nuclear interacting protein 1"
location: "1p34.3"
module: 41
arm: "+"
pooled_cpm: 36.02
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SNIP1

*Smad nuclear interacting protein 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +18.8, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.462× (z -10.8, q 1e-24, down in 34 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (CFPAC-1 0.198×, PANC-1 0.213×, SHP-77 0.169×, NCI-H2030 0.229×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 0.270×, LS 180 0.200×, SW48 0.112×; ⚠ toxic; transcription drop); [[XRK3F2 (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.126×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.0890×); [[Allantoin (drug)]] 0.5 µM in 1 line (NCI-H661 0.0733×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RECQL5]] (+0.70, fdr 1e-05), [[MED6]] (+0.65, fdr 7e-06), [[CCNT1]] (+0.64, fdr 1e-05); moves opposite to [[TRIM37]] (-0.54, fdr 2e-04), [[NR6A1]] (-0.54, fdr 3e-05), [[BTBD3]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +18.8 | 0e+00 | 45/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **10.7×** | +18.0 | 0e+00 | 48/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **6.29×** | +14.0 | 5e-42 | 47/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +11.9 | 1e-30 | 45/47 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +11.3 | 1e-27 | 40/48 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +10.9 | 9e-26 | 44/47 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.11×** | +10.8 | 2e-25 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.9 | 2e-13 | 38/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +7.8 | 3e-13 | 42/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.66×** | +7.4 | 1e-11 | 36/48 (SW480, LoVo, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.57×** | +6.6 | 3e-09 | 34/48 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +6.5 | 4e-09 | 33/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +6.5 | 4e-09 | 30/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +6.3 | 1e-08 | 35/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +5.6 | 8e-07 | 38/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +5.4 | 3e-06 | 34/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.7 | 9e-05 | 24/48 (J82, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 1e-04 | 26/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8800.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (CFPAC-1 0.198×, PANC-1 0.213×, SHP-77 0.169×, NCI-H2030 0.229×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 0.270×, LS 180 0.200×, SW48 0.112×; ⚠ toxic; transcription drop); [[XRK3F2 (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.126×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.0890×); [[Allantoin (drug)]] 0.5 µM in 1 line (NCI-H661 0.0733×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -10.8 | 1e-24 | 34/37 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.491×** | -10.4 | 8e-23 | 37/47 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 0.799× | -3.2 | 0.21 | 17/47 (LOX-IMVI, HCT15, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.812× | -3.1 | 0.21 | 16/46 (AN3 CA, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 0.812× | -3.1 | 0.21 | 13/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -3.1 | 0.21 | 13/48 (J82, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.1 | 12 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.03× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 35.9 | 10 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 18.2× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -14.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 38.3 | 9 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.5× (z +15.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 6 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 22.3× (z +13.3) | [[Torkinib (drug)]] 5 µM 0.106× (z -9.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 35.7 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.7× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 31.4 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.7× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 47.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +13.5) | — |
| [[A498 (line)]] | wt | 42.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 43.6 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +13.5) | — |
| [[BT-474 (line)]] | alt | 41.3 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 5.16× (z +10.6) | — |
| [[LoVo (line)]] | wt | 33.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 43.0 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.3× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.8 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 10.7× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 35.7 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 14.1× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 38.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 27.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 45.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 34.8 | 2 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +9.8) | [[XRK3F2 (drug)]] 0.5 µM 0.126× (z -9.7) |
| [[Hs 766T (line)]] | wt | 49.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 36.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 33.1 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.04× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 26.0 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 16.0× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 35.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 43.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 35.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.94× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 38.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.5) | — |
| [[A-427 (line)]] | wt | 29.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +10.4) | — |
| [[A549 (line)]] | wt | 31.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 44.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 23.6× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 36.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.7× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 49.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 43.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.38× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 30.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +10.2) | — |
| [[SW48 (line)]] | wt | 26.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.44× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0890× (z -9.6) |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0733× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 28.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +8.7) | — |
| [[RKO (line)]] | wt | 42.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.8× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL5]] | +0.70 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[MED6]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CCNT1]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CCNK]] | +0.63 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[SDE2]] | +0.63 | +0.71 / +0.56 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[YIPF5]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ECD]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TOX4]] | +0.61 | +0.71 / +0.40 | both halves | 5e-05 |  |
| [[TXNL4B]] | +0.60 | +0.57 / +0.38 | both halves | 6e-05 | STRING 434 |
| [[PRPF38A]] | +0.60 | +0.67 / +0.56 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 987 |
| [[EAF1]] | +0.60 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ZNF561]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM37]] | -0.54 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[NR6A1]] | -0.54 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[BTBD3]] | -0.54 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[TNPO1]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[SLC23A2]] | -0.53 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[INPP4A]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NIN]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CLASP2]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ABCD3]] | -0.51 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[VPS13A]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[STRBP]] | -0.51 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[LBR]] | -0.51 | -0.53 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-28.4, -9.3); signed map (-4.8, -6.2). **Vector** length 71.9, 17.7% of its response variance represented; |z| ≥ 3 in 1,253 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.8 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +11.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +18.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +14.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.1 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | +6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Smad nuclear interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,534,449-37,554,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PML1 |
| Gene groups (HGNC) | Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAD8](https://www.uniprot.org/uniprotkb/Q8TAD8) (Smad nuclear-interacting protein 1):

> Required for pre-mRNA splicing as component of the spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable). Down-regulates NF-kappa-B signaling by competing with RELA for CREBBP/EP300 binding. Involved in the microRNA (miRNA) biogenesis. May be involved in cyclin-D1/CCND1 mRNA stability through the SNARP complex which associates with both the 3'end of the CCND1 gene and its mRNA.

**Summary**, from NCBI Gene [79753](https://www.ncbi.nlm.nih.gov/gene/79753):

> This gene encodes a protein that contains a coiled-coil motif and C-terminal forkhead-associated (FHA) domain. The encoded protein functions as a transcriptional coactivator that increases c-Myc activity and inhibits transforming growth factor beta (TGF-beta) and nuclear factor kappa-B (NF-kB) signaling. The encoded protein also regulates the stability of cyclin D1 mRNA, and may play a role in cell proliferation and cancer progression. Mutations in this gene are a cause of psychomotor …

**Accessions** — [HGNC:30587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30587) · Entrez [79753](https://www.ncbi.nlm.nih.gov/gene/79753) · UniProt [Q8TAD8](https://www.uniprot.org/uniprotkb/Q8TAD8) · Ensembl [ENSG00000163877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163877)

## Data

Gene col 8800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8800); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8800]; `tensor/DDL_lfc|DDL_z.npy` [8800]; `embed/gene_vectors.npy` [8800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8800 or target_col == 8800). Every well: [[SNIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
