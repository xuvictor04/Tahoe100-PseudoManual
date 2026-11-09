---
symbol: "ZBTB25"
type: "gene"
col: 1599
ensembl_id: "ENSG00000089775"
name: "zinc finger and BTB domain containing 25"
location: "14q23.3"
module: 144
arm: "+"
pooled_cpm: 56.83
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# ZBTB25

*zinc finger and BTB domain containing 25* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.24× (z +4.7, q 0.001, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (LoVo 3.35×, SW48 3.79×, J82 2.58×, KATO III 3.28×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.53×, SW1417 2.12×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HOP62 2.90×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.333× (z -16.7, q 0e+00, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.485× (z -11.4, q 6e-28, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCL]] (+0.65, fdr 7e-06), [[LINC00938]] (+0.65, fdr 1e-05), [[ATP23]] (+0.61, fdr 1e-05); moves opposite to [[NAPG]] (-0.64, fdr 2e-05), [[SPTLC2]] (-0.57, fdr 4e-05), [[POLR3B]] (-0.55, fdr 3e-05).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1599.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (LoVo 3.35×, SW48 3.79×, J82 2.58×, KATO III 3.28×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.53×, SW1417 2.12×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HOP62 2.90×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.7 | 0.001 | 25/48 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +4.0 | 0.022 | 23/48 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.024 | 23/47 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.21× | +3.0 | 0.34 | 17/48 (LoVo, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1599.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.333×** | -16.7 | 0e+00 | 45/47 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.437×** | -13.0 | 2e-36 | 41/49 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.475×** | -11.7 | 2e-29 | 45/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.485×** | -11.4 | 6e-28 | 45/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.512×** | -10.5 | 6e-24 | 44/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.515×** | -10.0 | 9e-22 | 31/43 (HEC-1-A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -8.0 | 8e-14 | 33/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.609×** | -7.8 | 4e-13 | 41/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.599×** | -7.6 | 1e-12 | 37/48 (NCI-H1573, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -7.4 | 1e-11 | 35/48 (C32, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.447×** | -6.6 | 2e-09 | 39/45 (Hs 766T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.650×** | -6.3 | 1e-08 | 31/44 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.714×** | -5.1 | 1e-05 | 25/48 (NCI-H1792, C32, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.718×** | -5.0 | 2e-05 | 29/47 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.738×** | -4.8 | 6e-05 | 27/47 (CFPAC-1, SW 900, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.751×** | -4.5 | 2e-04 | 26/48 (C32, AN3 CA, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -4.5 | 3e-04 | 26/48 (C32, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.756×** | -4.4 | 3e-04 | 25/47 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.748×** | -4.4 | 3e-04 | 27/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.610×** | -4.1 | 0.001 | 27/47 (SHP-77, C32, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.780×** | -3.9 | 0.002 | 25/48 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.709×** | -3.9 | 0.003 | 23/48 (HCT15, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.784×** | -3.7 | 0.005 | 22/48 (NCI-H1573, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.854× | -3.5 | 0.009 | 17/49 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.681×** | -3.2 | 0.032 | 18/49 (C-33 A, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.699×** | -3.0 | 0.060 | 18/46 (CHP-212, SHP-77, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 84.1 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -20.3) |
| [[NCI-H1573 (line)]] | alt | 141 | 0 | 15 (11 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -19.2) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.298× (z -11.4) |
| [[A549 (line)]] | wt | 90.3 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.536× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 68.2 | 0 | 7 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.305× (z -11.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 77.2 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0405× (z -34.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.447× (z -8.9) |
| [[HOP62 (line)]] | alt | 71.0 | 2 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -16.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.196× (z -15.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.404× (z -8.7) |
| [[SNU-423 (line)]] | alt | 66.4 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.329× (z -10.1) |
| [[PANC-1 (line)]] | alt | 54.0 | 0 | 5 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.252× (z -15.1) |
| [[J82 (line)]] | alt | 52.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.306× (z -11.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 58.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[C-33 A (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.0) |
| [[COLO 205 (line)]] | alt | 42.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.244× (z -9.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 57.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -12.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 61.2 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.160× (z -12.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 52.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 38.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 83.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 16.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Bortezomib (drug)]] 5 µM 0.0817× (z -9.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 53.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 66.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -11.1) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 46.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 93.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.292× (z -10.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 61.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 53.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.334× (z -9.3) |
| [[SW 900 (line)]] | alt | 59.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.285× (z -10.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 30.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.7) | — |
| [[SW480 (line)]] | alt | 36.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 85.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.240× (z -9.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -9.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.8) | — |
| [[KATO III (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +13.3) | — |
| [[LoVo (line)]] | wt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +16.3) | — |
| [[LS 180 (line)]] | wt | 46.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.269× (z -9.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCL]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LINC00938]] | +0.65 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ATP23]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ARRDC3]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R3E]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[GAD1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ZSWIM5]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[C4orf47]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[MTCH2]] | +0.59 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[ZSCAN16-AS1]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[RBPJ]] | +0.57 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[ZNF563]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPG]] | -0.64 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[SPTLC2]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[POLR3B]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[HERC2]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[USP14]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SLC35C1]] | -0.52 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[VKORC1L1]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[NOL10]] | -0.50 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[HERC2P3]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CDC123]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[CCT2]] | -0.49 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[AP4B1]] | -0.49 | -0.48 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -20.6); signed map (-3.8, 4.4). **Vector** length 115, 35.4% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +1.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.5 | -16.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.3 | -11.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -7.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.2 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -7.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.0 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,449,106-64,505,213 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KUP; previously ZNF46, C14orf51 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P24278](https://www.uniprot.org/uniprotkb/P24278) (Zinc finger and BTB domain-containing protein 25):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7597](https://www.ncbi.nlm.nih.gov/gene/7597):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II; regulation of cytokine production; and regulation of immune system process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13112) · Entrez [7597](https://www.ncbi.nlm.nih.gov/gene/7597) · UniProt [P24278](https://www.uniprot.org/uniprotkb/P24278) · Ensembl [ENSG00000089775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089775)

## Data

Gene col 1599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1599); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1599]; `tensor/DDL_lfc|DDL_z.npy` [1599]; `embed/gene_vectors.npy` [1599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1599 or target_col == 1599). Every well: [[ZBTB25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
