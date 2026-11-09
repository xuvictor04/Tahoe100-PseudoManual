---
symbol: "UBR3"
type: "gene"
col: 6869
ensembl_id: "ENSG00000144357"
name: "ubiquitin protein ligase E3 component n-recognin 3"
location: "2q31.1"
module: 72
arm: "+"
pooled_cpm: 172.26
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# UBR3

*ubiquitin protein ligase E3 component n-recognin 3* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.92× (z +22.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.579× (z -11.5, q 1e-27, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.813× (z -4.4, q 0.001, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB4]] (+0.62, fdr 1e-05), [[TNKS]] (+0.61, fdr 1e-05), [[UBE4B]] (+0.60, fdr 1e-05); moves opposite to [[ZNF697]] (-0.48, fdr 6e-05), [[ZSCAN9]] (-0.45, fdr 2e-04), [[PPP1R18]] (-0.44, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.92×** | +22.4 | 0e+00 | 48/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.83×** | +21.8 | 0e+00 | 48/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.90×** | +18.7 | 0e+00 | 48/48 (LOX-IMVI, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +16.3 | 0e+00 | 48/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +16.3 | 0e+00 | 41/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +13.1 | 3e-37 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +12.2 | 2e-32 | 45/48 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +10.6 | 2e-24 | 43/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +9.2 | 3e-18 | 43/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.90×** | +7.3 | 1e-11 | 44/49 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +7.1 | 9e-11 | 34/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.41×** | +6.9 | 3e-10 | 32/48 (LOX-IMVI, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.7 | 8e-10 | 32/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +6.6 | 2e-09 | 39/45 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +6.4 | 7e-09 | 35/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +6.0 | 8e-08 | 35/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +5.8 | 3e-07 | 39/49 (LOX-IMVI, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.3 | 4e-06 | 23/48 (A-172, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.579×** | -11.5 | 1e-27 | 45/49 (HCT15, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -10.0 | 6e-21 | 38/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.645×** | -8.5 | 3e-15 | 35/45 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **0.744×** | -6.2 | 7e-08 | 40/48 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -5.5 | 5e-06 | 26/47 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -4.4 | 0.001 | 27/48 (SW480, RPMI-7951, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.830×** | -3.9 | 0.007 | 23/47 (C32, NCI-H460, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.847× | -3.5 | 0.033 | 19/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.895× | -3.3 | 0.057 | 10/49 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.757×** | -3.2 | 0.075 | 21/48 (NCI-H1792, RPMI-7951, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.857× | -3.1 | 0.083 | 18/47 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.862× | -3.1 | 0.083 | 16/47 (SW 900, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 102 | 16 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.71× (z +25.3) | — |
| [[SW480 (line)]] | alt | 221 | 12 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +24.5) | [[Auranofin (drug)]] 5 µM 0.462× (z -13.6) |
| [[SW1417 (line)]] | alt | 205 | 9 (1 ⚠) | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.86× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 214 | 10 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -12.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 182 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +19.7) | — |
| [[A498 (line)]] | wt | 164 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.9) | — |
| [[HEC-1-A (line)]] | alt | 170 | 9 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 253 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.04× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 132 | 9 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.58× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 147 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.5) | — |
| [[NCI-H1792 (line)]] | alt | 168 | 7 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.72× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 170 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +20.4) | — |
| [[NCI-H460 (line)]] | wt | 213 | 8 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.91× (z +22.4) | — |
| [[A549 (line)]] | wt | 156 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +15.5) | — |
| [[AsPC-1 (line)]] | alt | 78.2 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 5.69× (z +17.3) | — |
| [[HS-578T (line)]] | alt | 145 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.39× (z +16.3) | — |
| [[KATO III (line)]] | alt | 194 | 3 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.69× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 150 | 7 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.09× (z +24.2) | — |
| [[NCI-H2347 (line)]] | alt | 99.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 133 | 6 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 185 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.03× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -11.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 178 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -15.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 218 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.97× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 144 | 4 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.83× (z +11.9) | [[Docetaxel (drug)]] 0.05 µM 0.526× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~20% of this change |
| [[H4 (line)]] | wt | 247 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.97× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 191 | 3 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.86× (z +17.6) | [[Auranofin (drug)]] 5 µM 0.457× (z -10.3) |
| [[J82 (line)]] | alt | 130 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 126 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 190 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.3) | — |
| [[SNU-423 (line)]] | alt | 144 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.93× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -11.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 203 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 159 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 160 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.40× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -11.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 164 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.98× (z +17.1) | — |
| [[NCI-H2030 (line)]] | alt | 225 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +14.2) | — |
| [[Panc 03.27 (line)]] | alt | 156 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +13.1) | [[Lonafarnib (drug)]] 5 µM 0.0976× (z -13.2) ⚠ toxic |
| [[RKO (line)]] | wt | 174 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 197 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +13.6) | [[Auranofin (drug)]] 5 µM 0.400× (z -11.5) |
| [[SW48 (line)]] | wt | 218 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 160 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 289 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -13.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 181 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.62× (z +17.4) | — |
| [[Hs 766T (line)]] | wt | 112 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.48× (z +14.0) | — |
| [[CHP-212 (line)]] | wt | 217 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 307 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB4]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[TNKS]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[UBE4B]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ZNF148]] | +0.59 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[SNX13]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MBD5]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TAS2R14]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[DCTN4]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SOD1]] | +0.53 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[CDKAL1]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[CLASP1]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[USP47]] | +0.52 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF697]] | -0.48 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[ZSCAN9]] | -0.45 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[PPP1R18]] | -0.44 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[DUSP7]] | -0.44 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.44 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[GJC1]] | -0.43 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[LINC01128]] | -0.43 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[GOLGA7B]] | -0.42 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[N4BP3]] | -0.42 | -0.50 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.475). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, -11.4); signed map (-21.6, 3.7). **Vector** length 110, 41.6% of its response variance represented; |z| ≥ 3 in 1,468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.4 | +18.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.5 | +22.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.1 | +21.8 |
|  | [[NG25 (drug)]] 5 µM |  | +5.2 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.5 | +7.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.3 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -8.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | -5.5 | -6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.4 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.9 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3 component n-recognin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,827,454-170,084,131 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA2024, DKFZp434P117, FLJ37422; previously ZNF650 |
| Gene groups (HGNC) | Ubiquitin protein ligase E3 component n-recognins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZT12](https://www.uniprot.org/uniprotkb/Q6ZT12) (E3 ubiquitin-protein ligase UBR3):

> E3 ubiquitin-protein ligase which is a component of the N-end rule pathway (By similarity). Does not bind to proteins bearing specific N-terminal residues that are destabilizing according to the N-end rule, leading to their ubiquitination and subsequent degradation (By similarity). May play a role in Shh signaling by mediating the ubiquitination of Kif7 (By similarity). May be important for MYH9 function in certain tissues, possibly by regulating the ubiquitination of MYH9 and consequently …

**Summary**, from NCBI Gene [130507](https://www.ncbi.nlm.nih.gov/gene/130507):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in several processes, including sensory perception of smell; suckling behavior; and ubiquitin-dependent protein catabolic process via the N-end rule pathway. Predicted to act upstream of or within in utero embryonic development and olfactory behavior. Predicted to be located in membrane. Predicted to be part of ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:30467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30467) · Entrez [130507](https://www.ncbi.nlm.nih.gov/gene/130507) · UniProt [Q6ZT12](https://www.uniprot.org/uniprotkb/Q6ZT12) · Ensembl [ENSG00000144357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144357)

## Data

Gene col 6869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6869); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6869]; `tensor/DDL_lfc|DDL_z.npy` [6869]; `embed/gene_vectors.npy` [6869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6869 or target_col == 6869). Every well: [[UBR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
