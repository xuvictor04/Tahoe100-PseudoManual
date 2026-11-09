---
symbol: "SRSF7"
type: "gene"
col: 3731
ensembl_id: "ENSG00000115875"
name: "serine and arginine rich splicing factor 7"
location: "2p22.1"
module: 93
arm: "+"
pooled_cpm: 72.33
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# SRSF7

*serine and arginine rich splicing factor 7* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +18.3, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.21× (z +11.4, q 7e-28, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.638× (z -6.5, q 4e-08, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.158×, NCI-H1573 0.174×, NCI-H2347 0.353×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.223×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRSF2]] (+0.72, fdr 7e-06), [[TRA2B]] (+0.59, fdr 1e-05), [[NASP]] (+0.57, fdr 9e-06); moves opposite to [[ATP6V1E1]] (-0.54, fdr 1e-04), [[PRDX5]] (-0.50, fdr 2e-05), [[ADD1]] (-0.49, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EFNB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.45×** | +18.3 | 0e+00 | 44/48 (AsPC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +11.4 | 7e-28 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.12×** | +10.4 | 4e-23 | 45/48 (AsPC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.83×** | +8.7 | 4e-16 | 39/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +6.8 | 1e-09 | 38/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.58×** | +6.5 | 6e-09 | 41/48 (NCI-H460, KATO III, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.8 | 4e-07 | 27/48 (SW480, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.5 | 2e-06 | 2/50 (KATO III, CHP-212) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.0 | 3e-05 | 32/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +4.8 | 1e-04 | 29/48 (NCI-H1573, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.5 | 3e-04 | 28/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~71% of this change | **1.38×** | +4.4 | 5e-04 | 29/47 (NCI-H460, SHP-77, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.94×** | +4.4 | 6e-04 | 33/49 (AsPC-1, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.34×** | +4.0 | 0.002 | 28/50 (A-427, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +3.6 | 0.012 | 25/48 (HS-578T, NCI-H1792, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.027 | 20/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.17× | +3.1 | 0.054 | 15/49 (HS-578T, Panc 03.27, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3731.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.158×, NCI-H1573 0.174×, NCI-H2347 0.353×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.223×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.638×** | -6.5 | 4e-08 | 35/48 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.812×** | -4.2 | 0.007 | 26/48 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.600× | -3.4 | 0.13 | 21/49 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.802× | -3.2 | 0.14 | 20/47 (LoVo, Hs 766T, …) | rises with dose | low cells (technical?); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | 0.619× | -3.2 | 0.14 | 15/50 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.750× | -3.1 | 0.14 | 17/50 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.801× | -3.1 | 0.14 | 19/47 (SW 1271, SW480, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.7 | 10 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.91× (z +16.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 57.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +18.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 53.4 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +15.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 39.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +8.9) | — |
| [[KATO III (line)]] | alt | 59.9 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.66× (z +13.7) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[LOX-IMVI (line)]] | wt | 77.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +9.4) | — |
| [[C32 (line)]] | wt | 67.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +16.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.13× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 57.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +15.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 55.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.77× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 54.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.0) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 80.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 78.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +13.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 62.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.10× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 93.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.4) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 94.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.14× (z +9.3) | — |
| [[A-172 (line)]] | wt | 43.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.5) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[A498 (line)]] | wt | 74.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.6) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 70.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.6) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[C-33 A (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 89.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 50.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +15.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 57.4 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +9.2) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[HEC-1-A (line)]] | alt | 70.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +12.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 60.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 60.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +16.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2347 (line)]] | alt | 74.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 82.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.4) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 86.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.95× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~71% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 66.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW 900 (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.4) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW48 (line)]] | wt | 71.4 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.84× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF2]] | +0.72 | +0.76 / +0.68 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 961 |
| [[TRA2B]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 995 |
| [[NASP]] | +0.57 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[NOP56]] | +0.56 | +0.56 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[BZW2]] | +0.54 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SLC16A1]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[THSD8]] ⚠ | +0.53 | +0.52 / +0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FUS]] | +0.52 | +0.65 / +0.44 | both halves | 3e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 686 |
| [[PPIEL-1]] | +0.52 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[PREP]] | +0.51 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[PTBP1]] | +0.50 | +0.57 / +0.42 | both halves | 4e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 933 |
| [[TERT]] | +0.49 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SNHG15]] | +0.49 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1E1]] | -0.54 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[PRDX5]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ADD1]] | -0.49 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[COX7A2L]] | -0.49 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[CDS2]] | -0.47 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PINK1]] | -0.47 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[PFDN5]] | -0.47 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[C11orf54]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[AP2A1]] | -0.46 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[BBS7]] | -0.45 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[CACUL1]] | -0.45 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[NEDD8]] | -0.44 | -0.50 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNB2]] | B | EFNB2 activity lowers SRSF7's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.31× higher at baseline in the lines without EFNB2 | 0.064 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.5, 6.6); signed map (5.6, 18.8). **Vector** length 92.1, 27.3% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.3 | +18.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +11.4 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +2.0 | +0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +1.7 | +0.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +2.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | -4.0 | +6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.9 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -6.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:38,743,599-38,751,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 9G8, ZCRB2, HSSG1, AAG3, RBM37, ZCCHC20; previously SFRS7 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; RNA binding motif containing; Serine and arginine rich splicing factors |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 12 pathways, smallest: mRNA Splicing - Minor Pathway; Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16629](https://www.uniprot.org/uniprotkb/Q16629) (Serine/arginine-rich splicing factor 7):

> Required for pre-mRNA splicing. Can also modulate alternative splicing in vitro. Represses the splicing of MAPT/Tau exon 10. May function as export adapter involved in mRNA nuclear export such as of histone H2A. Binds mRNA which is thought to be transferred to the NXF1-NXT1 heterodimer for export (TAP/NXF1 pathway); enhances NXF1-NXT1 RNA-binding activity. RNA-binding is semi-sequence specific.

**Summary**, from NCBI Gene [6432](https://www.ncbi.nlm.nih.gov/gene/6432):

> The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an N-terminal RNA recognition motif (RRM) for binding RNA and a C-terminal RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different SR splicing factors. In addition to being critical for mRNA splicing, the SR proteins have also …

**Accessions** — [HGNC:10789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10789) · Entrez [6432](https://www.ncbi.nlm.nih.gov/gene/6432) · UniProt [Q16629](https://www.uniprot.org/uniprotkb/Q16629) · Ensembl [ENSG00000115875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115875)

## Data

Gene col 3731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3731); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3731]; `tensor/DDL_lfc|DDL_z.npy` [3731]; `embed/gene_vectors.npy` [3731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3731 or target_col == 3731). Every well: [[SRSF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
