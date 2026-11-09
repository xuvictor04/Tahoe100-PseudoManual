---
symbol: "LAMB1"
type: "gene"
col: 1654
ensembl_id: "ENSG00000091136"
name: "laminin subunit beta 1"
location: "7q31.1"
module: 97
arm: "+"
pooled_cpm: 154.38
n_lines_expressing: 43
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# LAMB1

*laminin subunit beta 1* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.54× (z +16.9, q 0e+00, up in 41 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.22× (z +4.5, q 9e-04, up in 22 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.276× (z -28.7, q 0e+00, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP1A1]] (+0.67, fdr 7e-06), [[TMX3]] (+0.60, fdr 1e-05), [[IL18R1]] (+0.59, fdr 2e-05); moves opposite to [[C15orf48]] (-0.58, fdr 1e-05), [[BBC3]] (-0.57, fdr 1e-05), [[APBA3]] (-0.56, fdr 1e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SLC39A8]] → it (grade B ⚠); 6 go from it, the strongest it → [[GMPS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +16.9 | 0e+00 | 41/42 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +15.1 | 0e+00 | 36/37 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +11.2 | 1e-26 | 31/38 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.5 | 9e-04 | 22/41 (HOP62, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.4 | 0.001 | 19/41 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 0.001 | 26/41 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 0.001 | 26/41 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.003 | 19/42 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.004 | 20/41 (C32, A-172, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.24×** | +3.9 | 0.005 | 21/41 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.20× | +3.8 | 0.006 | 17/41 (A498, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.5 | 0.023 | 19/41 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.040 | 13/41 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.041 | 16/41 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | 1.20× | +3.2 | 0.044 | 15/41 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.054 | 15/41 (A498, A-172, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 1.19× | +3.1 | 0.063 | 17/41 (Hs 766T, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.276×** | -28.7 | 0e+00 | 39/41 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.413×** | -16.0 | 0e+00 | 38/41 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.451×** | -13.8 | 3e-41 | 36/41 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.587×** | -9.6 | 8e-20 | 38/41 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.597×** | -9.3 | 1e-18 | 35/41 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.691×** | -6.4 | 2e-08 | 31/43 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.539×** | -5.8 | 4e-07 | 30/42 (BT-474, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.719×** | -5.7 | 8e-07 | 32/42 (H4, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.734×** | -5.6 | 1e-06 | 32/41 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.747×** | -5.3 | 8e-06 | 28/41 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.575×** | -5.2 | 9e-06 | 30/43 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.634×** | -4.3 | 8e-04 | 21/41 (CHP-212, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.782×** | -4.3 | 9e-04 | 23/40 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.858× | -3.8 | 0.005 | 17/41 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.813×** | -3.8 | 0.005 | 20/42 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.809×** | -3.7 | 0.008 | 22/41 (HepG2/C3A, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 295 | 14 (3 ⚠) | 2 | [[Clobetasol propionate (drug)]] 0.05 µM 2.69× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -12.4) |
| [[Hs 766T (line)]] | wt | 152 | 14 | 2 | [[Dexamethasone (drug)]] 5 µM 4.21× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -22.5) |
| [[RKO (line)]] | wt | 191 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -28.9) |
| [[NCI-H460 (line)]] | wt | 370 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -29.6) |
| [[RPMI-7951 (line)]] | alt | 178 | 8 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Dexamethasone (drug)]] 5 µM 2.44× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -23.5) |
| [[A-172 (line)]] | wt | 299 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -20.0) |
| [[A549 (line)]] | wt | 192 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 2.52× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 185 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -21.8) |
| [[SW48 (line)]] | wt | 183 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -21.7) |
| [[HEC-1-A (line)]] | alt | 84.7 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -15.8) |
| [[HS-578T (line)]] | alt | 234 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +16.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 151 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -16.3) |
| [[SW480 (line)]] | alt | 59.0 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.23× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -12.5) |
| [[HOP62 (line)]] | alt | 170 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Dexamethasone (drug)]] 5 µM 2.07× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.4) |
| [[LoVo (line)]] | wt | 84.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 55.3 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 4.15× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 76.4 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.0) |
| [[PANC-1 (line)]] | alt | 128 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -19.6) |
| [[SNU-423 (line)]] | alt | 197 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 236 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -14.0) |
| [[H4 (line)]] | wt | 282 | 2 | 2 | [[Dexamethasone (drug)]] 5 µM 2.42× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -18.1) |
| [[LS 180 (line)]] | wt | 107 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 341 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -26.5) |
| [[SW 900 (line)]] | alt | 146 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.8) |
| [[COLO 205 (line)]] | alt | 59.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.6) |
| [[hTERT-HPNE (line)]] | wt | 172 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.5) |
| [[J82 (line)]] | alt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -17.4) |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -22.3) |
| [[SK-MEL-2 (line)]] | alt | 233 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -22.1) |
| [[BT-474 (line)]] | alt | 86.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.352× (z -9.2) |
| [[HCT15 (line)]] | alt | 76.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -12.0) |
| [[HT-29 (line)]] | alt | 87.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.45× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 164 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 362 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.9) |
| [[C32 (line)]] | wt | 582 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.448× (z -8.5) |
| [[CHP-212 (line)]] | wt | 141 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -9.1) |
| [[KATO III (line)]] | alt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -16.0) |
| [[SW 1271 (line)]] | alt | 162 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -8.9) |
| [[A-427 (line)]] | wt | 37.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 17.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1A1]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TMX3]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[IL18R1]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[PRKDC]] | +0.58 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[IPO7]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TMEM164]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[LRPPRC]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[CRTAP]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[PRPS2]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[FAH]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ELOVL6]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[WLS]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf48]] | -0.58 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[BBC3]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[APBA3]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[CCDC127]] | -0.56 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[ZFAND2B]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[JUND]] | -0.55 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PIM3]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TUBB2B]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 | pathway: L1CAM interactions |
| [[DUSP8]] | -0.53 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SAT2]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CIR1]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC39A8]] | B | SLC39A8 activity raises LAMB1's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 2.73× lower at baseline in the lines without SLC39A8 | 0.010 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[JCAD]] | B | JCAD activity raises LAMB1's level | lines that do not express JCAD (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without JCAD | 0.010 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[HIPK2]] | B | HIPK2 activity raises LAMB1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 3.37× lower at baseline in the lines without HIPK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[EVA1C]] | B | EVA1C activity raises LAMB1's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without EVA1C | 0.018 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[SRPX]] | B | SRPX activity raises LAMB1's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.61× lower at baseline in the lines without SRPX | 0.023 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[CCBE1]] | B | CCBE1 activity raises LAMB1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without CCBE1 | 0.056 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[MAF]] | B | MAF activity raises LAMB1's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without MAF | 0.064 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[BDKRB2]] | B | BDKRB2 activity strengthens LAMB1's drug response | lines that do not express BDKRB2 (14) vs lines expressing it (29) | the lines without BDKRB2 respond 0.99× as strongly (z diff +0.04); strongest at Dinaciclib 0.05 µM: 1.42x vs 2.07x (z diff +3.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; target measured in part of the lines; both ways; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises LAMB1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NPAS2]] | B | NPAS2 activity raises LAMB1's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without NPAS2 | 0.084 | ⚠ within organs, on part of the lines |
| [[ADGRG6]] | B | ADGRG6 activity raises LAMB1's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.27× lower at baseline in the lines without ADGRG6 | 0.090 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GMPS]] | B | LAMB1 activity lowers GMPS's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 1.64× higher at baseline in the lines without LAMB1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |
| [[TMEM106A]] | B | LAMB1 activity raises TMEM106A's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 2.84× lower at baseline in the lines without LAMB1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |
| [[NUP155]] | B | LAMB1 activity lowers NUP155's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 1.86× higher at baseline in the lines without LAMB1 | 0.055 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |
| [[SLC39A8]] | B | LAMB1 activity raises SLC39A8's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 2.66× lower at baseline in the lines without LAMB1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |
| [[NUDT3]] | B | LAMB1 activity lowers NUDT3's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 1.88× higher at baseline in the lines without LAMB1 | 0.079 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |
| [[HEATR1]] | B | LAMB1 activity lowers HEATR1's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 1.72× higher at baseline in the lines without LAMB1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.9, 13.8); signed map (16.8, 34.8). **Vector** length 128, 41.6% of its response variance represented; |z| ≥ 3 in 1,511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +16.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.1 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.0 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.5 | +1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.1 | +3.1 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -5.9 | -4.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.6 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -13.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.9 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:107,923,799-108,003,213 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CLM |
| Gene groups (HGNC) | Laminin subunits |
| Reactome | 25 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P07942](https://www.uniprot.org/uniprotkb/P07942) (Laminin subunit beta-1):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components. Involved in the organization of the laminar architecture of the cerebral cortex. It is probably required for the integrity of the basement membrane/glia limitans that serves as an anchor point for the endfeet of radial glial cells and as a physical barrier to migrating …

**Summary**, from NCBI Gene [3912](https://www.ncbi.nlm.nih.gov/gene/3912):

> Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectively) and they form a cruciform structure consisting of 3 short arms, each formed by a different …

**Accessions** — [HGNC:6486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6486) · Entrez [3912](https://www.ncbi.nlm.nih.gov/gene/3912) · UniProt [P07942](https://www.uniprot.org/uniprotkb/P07942) · Ensembl [ENSG00000091136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091136)

## Data

Gene col 1654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1654); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1654]; `tensor/DDL_lfc|DDL_z.npy` [1654]; `embed/gene_vectors.npy` [1654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1654 or target_col == 1654). Every well: [[LAMB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
