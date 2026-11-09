---
symbol: "PLPP3"
type: "gene"
col: 8510
ensembl_id: "ENSG00000162407"
name: "phospholipid phosphatase 3"
location: "1p32.2"
module: 14
arm: "+"
pooled_cpm: 52.38
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 25
n_dd_up_clean: 29
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PLPP3

*phospholipid phosphatase 3* — 1p32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.68× (z +17.9, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.483× (z -11.5, q 7e-28, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP3]] (+0.61, fdr 1e-05), [[CXCL2]] (+0.60, fdr 3e-05), [[BASP1]] (+0.58, fdr 1e-05); moves opposite to [[TPD52L2]] (-0.61, fdr 1e-05), [[DIP2A]] (-0.58, fdr 1e-05), [[MTHFD2]] (-0.58, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CFH]] → it (grade B ⚠); 5 go from it, the strongest it → [[PDGFRL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.68×** | +17.9 | 0e+00 | 42/44 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +12.2 | 8e-32 | 27/42 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.46×** | +10.3 | 2e-22 | 29/41 (SNU-1, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +10.0 | 2e-21 | 25/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +9.5 | 2e-19 | 28/42 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.68×** | +7.9 | 2e-13 | 22/42 (SW 900, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.7 | 2e-09 | 24/43 (LS 180, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +5.9 | 2e-07 | 25/43 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.7 | 6e-07 | 19/43 (A-172, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.6 | 1e-06 | 16/41 (SNU-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.4 | 4e-06 | 20/43 (SNU-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 2e-05 | 21/43 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 2e-05 | 21/43 (SNU-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 4e-05 | 18/42 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 2e-04 | 14/43 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 2e-04 | 16/42 (SNU-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.483×** | -11.5 | 7e-28 | 28/43 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.524×** | -10.2 | 5e-22 | 29/43 (hTERT-HPNE, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.598×** | -8.1 | 9e-14 | 29/43 (HepG2/C3A, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.628×** | -7.3 | 3e-11 | 23/40 (Panc 03.27, SW1417, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.626×** | -7.1 | 1e-10 | 25/34 (Panc 03.27, SW1417, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -6.9 | 6e-10 | 21/43 (hTERT-HPNE, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.624×** | -6.7 | 1e-09 | 22/34 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.669×** | -6.3 | 2e-08 | 23/43 (hTERT-HPNE, SW480, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.680×** | -6.1 | 7e-08 | 22/43 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.683×** | -6.0 | 1e-07 | 22/42 (J82, HepG2/C3A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.779×** | -5.5 | 2e-06 | 27/44 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.781×** | -5.4 | 3e-06 | 23/43 (hTERT-HPNE, SNU-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -5.3 | 5e-06 | 20/43 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.722×** | -5.1 | 1e-05 | 20/42 (A-427, C32, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.727×** | -4.8 | 5e-05 | 20/41 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.743×** | -4.5 | 2e-04 | 21/42 (A-172, A-427, …) | two highest doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.822×** | -4.3 | 5e-04 | 16/44 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.780×** | -3.9 | 0.003 | 17/42 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.784×** | -3.7 | 0.006 | 15/43 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.850× | -3.6 | 0.009 | 16/43 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.802×** | -3.3 | 0.022 | 17/43 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.865× | -3.2 | 0.030 | 9/44 (SK-MEL-2, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 186 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.58× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.6) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.334× (z -9.1) |
| [[A498 (line)]] | wt | 128 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +14.7) | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 208 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0742× (z -14.3) |
| [[HS-578T (line)]] | alt | 68.1 | 6 | 1 | [[Harringtonine (drug)]] 0.5 µM 8.35× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -8.7) |
| [[BT-474 (line)]] | alt | 90.2 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 52.8× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.215× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 112 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 19.7× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -15.5) |
| [[Hs 766T (line)]] | wt | 75.8 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 35.0× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.180× (z -12.2) |
| [[SW 900 (line)]] | alt | 85.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.241× (z -9.7) |
| [[SW1417 (line)]] | alt | 67.2 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.68× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 17.0 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.41× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +11.9) | — |
| [[J82 (line)]] | alt | 95.3 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 18.3× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.242× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 51.5 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 34.1× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.238× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 69.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 50.8 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 85.7× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 63.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.187× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 36.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +14.4) | — |
| [[KATO III (line)]] | alt | 22.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -13.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 54.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -18.3) |
| [[SNU-423 (line)]] | alt | 97.0 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.121× (z -9.5) |
| [[C32 (line)]] | wt | 65.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HT-29 (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 71.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.04× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 34.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.6× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[RPMI-7951 (line)]] | alt | 39.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 49.1× (z +11.0) | — |
| [[A549 (line)]] | wt | 90.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -9.1) |
| [[COLO 205 (line)]] | alt | 64.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.0) | — |
| [[H4 (line)]] | wt | 15.4 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0420× (z -11.3) |
| [[LoVo (line)]] | wt | 37.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 52.7× (z +15.1) | — |
| [[NCI-H1792 (line)]] | alt | 79.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.18× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.302× (z -8.5) |
| [[SW48 (line)]] | wt | 41.2 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0562× (z -9.3) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.35 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP3]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CXCL2]] | +0.60 | +0.46 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BASP1]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[KYNU]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DENND2B]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[NFKBIA]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ARHGAP24]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[HNRNPH2]] | +0.56 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[CSF1]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CFH]] | +0.54 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ZNF462]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[CEBPD]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.61 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[DIP2A]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MTHFD2]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SGTB]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CAPN10]] | -0.54 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CARS1]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZFYVE21]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[C11orf80]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[RARS2]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[EIF4EBP1]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[GDI2]] | -0.49 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[SARS1]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFH]] | B | CFH activity raises PLPP3's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without CFH | 0.069 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[CSGALNACT1]] | B | CSGALNACT1 activity raises PLPP3's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without CSGALNACT1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[TFAP2C]] | B | TFAP2C activity raises PLPP3's level | lines that do not express TFAP2C (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without TFAP2C | 0.086 | ⚠ within organs, on part of the lines; also absent: LYPD1, SETBP1, SAA1 |
| [[RSPO3]] | B | RSPO3 activity raises PLPP3's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 1.56× lower at baseline in the lines without RSPO3 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PLPP3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFRL]] | B | PLPP3 activity raises PDGFRL's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without PLPP3 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |
| [[NCOA7]] | B | PLPP3 activity raises NCOA7's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without PLPP3 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |
| [[ZC3H12C]] | B | PLPP3 activity raises ZC3H12C's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 2.64× lower at baseline in the lines without PLPP3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |
| [[CEBPD]] | B | PLPP3 activity raises CEBPD's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 1.31× lower at baseline in the lines without PLPP3 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |
| [[METTL18]] | B | PLPP3 activity raises METTL18's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 1.28× lower at baseline in the lines without PLPP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 9.3); signed map (45.3, 16.1). **Vector** length 113, 29.4% of its response variance represented; |z| ≥ 3 in 1,385 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.8 | +17.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.1 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +12.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +7.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.9 | -11.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.7 | -6.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -5.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -3.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid phosphatase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.2 — chr1:56,494,761-56,645,301 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAP-2b, LPP3; previously PPAP2B |
| Gene groups (HGNC) | Phospholipid phosphatases |
| Hallmark sets | UV_RESPONSE_DN, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O14495](https://www.uniprot.org/uniprotkb/O14495) (Phospholipid phosphatase 3):

> Magnesium-independent phospholipid phosphatase of the plasma membrane that catalyzes the dephosphorylation of a variety of glycerolipid and sphingolipid phosphate esters including phosphatidate/PA, lysophosphatidate/LPA, diacylglycerol pyrophosphate/DGPP, sphingosine 1-phosphate/S1P and ceramide 1-phosphate/C1P. Also acts on N-oleoyl ethanolamine phosphate/N-(9Z-octadecenoyl)-ethanolamine phosphate, a potential physiological compound. Has both an extracellular and an intracellular phosphatase …

**Summary**, from NCBI Gene [8613](https://www.ncbi.nlm.nih.gov/gene/8613):

> The protein encoded by this gene is a member of the phosphatidic acid phosphatase (PAP) family. PAPs convert phosphatidic acid to diacylglycerol, and function in de novo synthesis of glycerolipids as well as in receptor-activated signal transduction mediated by phospholipase D. This protein is a membrane glycoprotein localized at the cell plasma membrane. It has been shown to actively hydrolyze extracellular lysophosphatidic acid and short-chain phosphatidic acid. The expression of this gene is …

**Accessions** — [HGNC:9229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9229) · Entrez [8613](https://www.ncbi.nlm.nih.gov/gene/8613) · UniProt [O14495](https://www.uniprot.org/uniprotkb/O14495) · Ensembl [ENSG00000162407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162407)

## Data

Gene col 8510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8510); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8510]; `tensor/DDL_lfc|DDL_z.npy` [8510]; `embed/gene_vectors.npy` [8510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8510 or target_col == 8510). Every well: [[PLPP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLPP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
