---
symbol: "HSPH1"
type: "gene"
col: 4207
ensembl_id: "ENSG00000120694"
name: "heat shock protein family H (Hsp110) member 1"
location: "13q12.3"
module: 60
arm: "+"
pooled_cpm: 116.34
n_lines_expressing: 50
n_dd_up: 60
n_dd_down: 2
n_dd_up_clean: 33
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSPH1

*heat shock protein family H (Hsp110) member 1* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 60 drug-doses (27 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 32.2× (z +36.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.677× (z -3.7, q 0.068, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.611×, MIA PaCa-2 0.596×; ⚠ position not correctable); [[Cabozantinib (S-malate) (drug)]] 5 µM in 1 line (KATO III 0.268×); [[Ponatinib (drug)]] 5 µM in 1 line (KATO III 0.301×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHORDC1]] (+0.74, fdr 7e-06), [[DNAJA4]] (+0.68, fdr 7e-06), [[HSP90AA1]] (+0.67, fdr 7e-06); moves opposite to [[DOP1A]] (-0.59, fdr 9e-05), [[C6orf89]] (-0.53, fdr 1e-05), [[YY1AP1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 27 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 60 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 27 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **32.2×** | +36.0 | 0e+00 | 48/48 (HT-29, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **21.1×** | +31.6 | 0e+00 | 48/48 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **15.4×** | +25.7 | 0e+00 | 48/48 (HT-29, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **9.87×** | +22.4 | 0e+00 | 48/48 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **7.03×** | +19.5 | 0e+00 | 47/47 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.35×** | +17.7 | 0e+00 | 45/48 (A498, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **15.8×** | +15.0 | 0e+00 | 44/44 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **7.43×** | +14.8 | 0e+00 | 48/49 (HT-29, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.17×** | +12.0 | 4e-31 | 45/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.12×** | +11.8 | 3e-30 | 44/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.99×** | +11.4 | 4e-28 | 47/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.83×** | +10.8 | 2e-25 | 43/49 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.84×** | +10.4 | 1e-23 | 43/48 (HS-578T, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +10.2 | 1e-22 | 46/49 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.64×** | +9.7 | 2e-20 | 37/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Infigratinib (drug)]] 5 µM |  | **5.12×** | +8.9 | 3e-17 | 47/48 (HT-29, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **3.92×** | +7.4 | 4e-12 | 46/47 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +6.8 | 2e-10 | 38/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.8 | 2e-07 | 36/48 (HOP62, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.73×** | +5.4 | 1e-06 | 29/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.68×** | +5.3 | 2e-06 | 37/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.44×** | +5.3 | 2e-06 | 39/49 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.67×** | +5.1 | 7e-06 | 39/48 (MIA PaCa-2, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4207.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.611×, MIA PaCa-2 0.596×; ⚠ position not correctable); [[Cabozantinib (S-malate) (drug)]] 5 µM in 1 line (KATO III 0.268×); [[Ponatinib (drug)]] 5 µM in 1 line (KATO III 0.301×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.677×** | -3.7 | 0.068 | 30/48 (COLO 205, A-172, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.694×** | -3.7 | 0.068 | 31/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.717× | -3.3 | 0.15 | 25/50 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.707× | -3.3 | 0.15 | 19/48 (SW1417, SW 900, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.801× | -3.2 | 0.15 | 23/48 (NCI-H23, Hs 766T, …) | all doses, flat |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.731× | -3.1 | 0.16 | 21/48 (COLO 205, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.812× | -3.1 | 0.16 | 22/48 (LS 180, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 95.5 | 20 (14 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 26.0× (z +26.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 140 | 14 (6 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 39.4× (z +25.7) | [[Adagrasib (drug)]] 0.05 µM 0.596× (z -12.8) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 79.6 | 15 (9 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 23.8× (z +27.4) | — |
| [[SW480 (line)]] | alt | 202 | 15 (10 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 54.1× (z +31.3) | — |
| [[C-33 A (line)]] | alt | 84.4 | 14 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 51.0× (z +25.3) | — |
| [[A549 (line)]] | wt | 73.5 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +19.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 21.7× (z +18.6) | — |
| [[HOP62 (line)]] | alt | 64.6 | 13 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 125× (z +29.1) | — |
| [[HT-29 (line)]] | alt | 214 | 13 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 96.3× (z +33.4) | — |
| [[LS 180 (line)]] | wt | 76.6 | 13 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 22.6× (z +23.0) | — |
| [[SNU-423 (line)]] | alt | 62.8 | 13 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 125× (z +30.3) | — |
| [[SW1417 (line)]] | alt | 154 | 13 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 20.7× (z +26.2) | — |
| [[hTERT-HPNE (line)]] | wt | 63.0 | 12 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 89.5× (z +25.3) | — |
| [[KATO III (line)]] | alt | 148 | 10 (4 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 29.7× (z +24.7) | [[Cabozantinib (S-malate) (drug)]] 5 µM 0.268× (z -9.6) |
| [[LoVo (line)]] | wt | 101 | 12 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 39.5× (z +26.2) | — |
| [[SW 900 (line)]] | alt | 122 | 12 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 37.4× (z +26.6) | — |
| [[A-172 (line)]] | wt | 67.8 | 11 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 148× (z +29.7) | — |
| [[A498 (line)]] | wt | 191 | 11 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.8× (z +25.4) | — |
| [[CHP-212 (line)]] | wt | 148 | 11 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.6× (z +16.2) | — |
| [[HS-578T (line)]] | alt | 89.9 | 11 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 43.0× (z +22.7) | — |
| [[NCI-H1573 (line)]] | alt | 50.8 | 11 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 17.3× (z +18.1) | — |
| [[H4 (line)]] | wt | 41.5 | 10 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 80.8× (z +20.1) | — |
| [[HEC-1-A (line)]] | alt | 59.9 | 10 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 54.1× (z +24.1) | — |
| [[Hs 766T (line)]] | wt | 157 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 31.1× (z +25.7) | — |
| [[RKO (line)]] | wt | 62.2 | 10 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 25.4× (z +21.4) | — |
| [[SK-MEL-2 (line)]] | alt | 94.7 | 10 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 55.9× (z +29.8) | — |
| [[CFPAC-1 (line)]] | alt | 55.0 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 41.7× (z +18.8) | — |
| [[Panc 03.27 (line)]] | alt | 114 | 9 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 51.1× (z +27.3) | — |
| [[SNU-1 (line)]] | wt | 257 | 9 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 17.8× (z +24.3) | — |
| [[AsPC-1 (line)]] | alt | 220 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.7× (z +16.2) | — |
| [[C32 (line)]] | wt | 78.5 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 150× (z +23.8) | — |
| [[COLO 205 (line)]] | alt | 124 | 8 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 138× (z +19.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 75.1× (z +17.9) | — |
| [[NCI-H1792 (line)]] | alt | 29.3 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +16.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 12.0× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 188 | 6 (2 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 20.4× (z +23.9) | [[Adagrasib (drug)]] 0.05 µM 0.611× (z -13.6) ⚠ position not correctable |
| [[HepG2_C3A (line)]] | wt | 165 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.5× (z +13.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 9.34× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 137 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 39.5× (z +24.6) | — |
| [[NCI-H2347 (line)]] | alt | 86.3 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 37.0× (z +21.6) | — |
| [[A-427 (line)]] | wt | 153 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 26.4× (z +27.7) | — |
| [[BT-474 (line)]] | alt | 121 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 53.7× (z +31.4) | — |
| [[J82 (line)]] | alt | 206 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.7× (z +18.9) | — |
| [[RPMI-7951 (line)]] | alt | 92.0 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 58.2× (z +22.4) | — |
| [[SHP-77 (line)]] | alt | 191 | 6 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 19.5× (z +19.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 16.2× (z +18.7) | — |
| [[HCT15 (line)]] | alt | 106 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 30.0× (z +18.5) | — |
| [[NCI-H2030 (line)]] | alt | 62.7 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +18.5) | — |
| [[SW 1271 (line)]] | alt | 187 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 47.9× (z +16.8) | — |
| [[SW48 (line)]] | wt | 105 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 35.1× (z +22.9) | — |
| [[NCI-H661 (line)]] | alt | 148 | 4 | 0 | [[Auranofin (drug)]] 5 µM 15.4× (z +10.9) | — |
| [[SW 1088 (line)]] | alt | 82.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 71.5× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 83.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 29.3× (z +14.4) | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHORDC1]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 | STRING 666 |
| [[DNAJA4]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 | STRING 817 |
| [[HSP90AA1]] | +0.67 | +0.74 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 938 |
| [[CACYBP]] | +0.67 | +0.66 / +0.77 | both halves | 7e-06 | STRING 471 |
| [[HSPE1]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 | STRING 870 |
| [[AHSA1]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 | STRING 728 |
| [[HSP90AA2P]] | +0.65 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CCT4]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 | STRING 484 |
| [[STIP1]] | +0.63 | +0.69 / +0.67 | both halves | 7e-06 | STRING 928 |
| [[SOD1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[FKBP4]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 | pathway: Attenuation phase; STRING 525 |
| [[SERPINH1]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 | pathway: Attenuation phase |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | -0.59 | -0.37 / -0.53 | both halves | 9e-05 |  |
| [[C6orf89]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[PHPT1]] | -0.53 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[ABHD16A]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[HCFC2]] | -0.50 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[DPM3]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[LSM14B]] | -0.48 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[SEC22A]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[NDUFS7]] | -0.48 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PEX13]] | -0.48 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZBTB48]] | -0.47 | -0.39 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.4, -11.1); signed map (-25.7, -28.9). **Vector** length 89.2, 34.4% of its response variance represented; |z| ≥ 3 in 1,998 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand* (reactome, mean cos +0.52 to 12); *mTORC1 signaling* (hallmark, mean cos +0.54 to 13); *AUF1 (hnRNP D0) binds and destabilizes mRNA* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.6 | +36.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.7 | +6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.5 | +22.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.9 | +15.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +31.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +25.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +14.8 |
|  | [[Infigratinib (drug)]] 5 µM |  | +3.7 | +8.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.8 | +11.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.4 | +7.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -4.3 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | +0.4 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family H (Hsp110) member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:31,134,973-31,162,388 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSP105B, KIAA0201, HSP105A, NY-CO-25 |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 10 pathways, smallest: Scavenging by Class F Receptors; Attenuation phase; HSF1 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92598](https://www.uniprot.org/uniprotkb/Q92598) (Heat shock protein 105 kDa):

> Acts as a nucleotide-exchange factor (NEF) for chaperone proteins HSPA1A and HSPA1B, promoting the release of ADP from HSPA1A/B thereby triggering client/substrate protein release. Prevents the aggregation of denatured proteins in cells under severe stress, on which the ATP levels decrease markedly. Inhibits HSPA8/HSC70 ATPase and chaperone activities (By similarity).

**Summary**, from NCBI Gene [10808](https://www.ncbi.nlm.nih.gov/gene/10808):

> This gene encodes a member of the heat shock protein 70 family of proteins. The encoded protein functions as a nucleotide exchange factor for the molecular chaperone heat shock cognate 71 kDa protein (Hsc70). In addition, this protein plays a distinct but related role as a holdase that inhibits the aggregation of misfolded proteins, including the cystic fibrosis transmembrane conductance regulator (CFTR) protein. Elevated expression of this protein has been observed in numerous human cancers. …

**Accessions** — [HGNC:16969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16969) · Entrez [10808](https://www.ncbi.nlm.nih.gov/gene/10808) · UniProt [Q92598](https://www.uniprot.org/uniprotkb/Q92598) · Ensembl [ENSG00000120694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120694)

## Data

Gene col 4207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4207); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4207]; `tensor/DDL_lfc|DDL_z.npy` [4207]; `embed/gene_vectors.npy` [4207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4207 or target_col == 4207). Every well: [[HSPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
