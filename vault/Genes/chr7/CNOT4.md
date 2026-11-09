---
symbol: "CNOT4"
type: "gene"
col: 1289
ensembl_id: "ENSG00000080802"
name: "CCR4-NOT transcription complex subunit 4"
location: "7q33"
module: 17
arm: "+"
pooled_cpm: 205.55
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CNOT4

*CCR4-NOT transcription complex subunit 4* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.77× (z +17.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.443× (z -13.4, q 4e-38, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.791× (z -5.7, q 2e-06, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHFR2]] (+0.62, fdr 1e-04), [[WAC]] (+0.62, fdr 7e-06), [[ZNF148]] (+0.60, fdr 1e-05); moves opposite to [[ATAD3B]] (-0.54, fdr 3e-05), [[C11orf24]] (-0.53, fdr 7e-05), [[DPP9]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.77×** | +17.4 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +16.6 | 0e+00 | 48/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +12.5 | 2e-33 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.00×** | +11.8 | 3e-30 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.08×** | +11.3 | 1e-27 | 47/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.84×** | +10.4 | 2e-23 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +9.0 | 2e-17 | 46/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.5 | 5e-12 | 41/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.5 | 5e-09 | 40/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +6.2 | 3e-08 | 43/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.43×** | +6.2 | 3e-08 | 35/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.8 | 4e-07 | 41/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +4.9 | 4e-05 | 26/48 (SNU-1, HT-29, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 4e-04 | 30/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.001 | 32/48 (C32, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.003 | 36/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.023 | 31/49 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.064 | 21/48 (SW480, J82, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.443×** | -13.4 | 4e-38 | 42/44 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.471×** | -12.9 | 2e-35 | 47/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -7.2 | 1e-10 | 36/45 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -5.7 | 2e-06 | 33/48 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.733×** | -5.1 | 4e-05 | 40/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -4.8 | 2e-04 | 31/48 (H4, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.771×** | -4.4 | 7e-04 | 30/48 (KATO III, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.841× | -4.2 | 0.002 | 23/49 (NCI-H2347, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -3.9 | 0.007 | 29/49 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.863× | -3.6 | 0.022 | 13/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.043 | 26/47 (HT-29, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.817×** | -3.3 | 0.044 | 26/50 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.768×** | -3.1 | 0.094 | 31/48 (COLO 205, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 183 | 12 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.22× (z +22.5) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -13.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 169 | 10 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +33.1) | [[Dinaciclib (drug)]] 0.5 µM 0.534× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 224 | 9 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -19.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 190 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 418 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -14.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 211 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -13.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 238 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.489× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 282 | 2 | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -23.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 289 | 4 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -14.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 227 | 4 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.71× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 257 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 333 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 194 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +14.6) | — |
| [[SW48 (line)]] | wt | 257 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -13.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 195 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +21.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -14.6) ⚠ cell-cycle shift, explains ~9% of this change |
| [[Hs 766T (line)]] | wt | 192 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -12.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 169 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -12.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 120 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 158 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -9.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 306 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 225 | 5 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 124 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +24.9) | [[Dinaciclib (drug)]] 0.5 µM 0.541× (z -8.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 236 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 243 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -18.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 193 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 155 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 172 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -12.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 234 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 189 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 147 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 202 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 176 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -15.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 177 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 137 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 149 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 177 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 175 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 182 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.0572× (z -32.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 189 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -21.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 204 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 208 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 228 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -12.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 294 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -11.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.3) ⚠ cell-cycle shift, explains ~9% of this change |
| [[HCT15 (line)]] | alt | 217 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 139 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.3) | — |
| [[SW 1088 (line)]] | alt | 245 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.198× (z -9.3) |
| [[SW 1271 (line)]] | alt | 209 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +8.8) | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR2]] | +0.62 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[WAC]] | +0.62 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[ZNF148]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NDUFS4]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[RAB3GAP1]] | +0.59 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[CDC73]] | +0.58 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SPPL3]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DMXL1]] | +0.57 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[TLK2]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[RBM33]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 | same gene group |
| [[IFTAP]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[SPACA9]] | +0.56 | +0.44 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD3B]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[C11orf24]] | -0.53 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[DPP9]] | -0.53 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[TOP3A]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZNF276]] | -0.49 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[EHBP1L1]] | -0.49 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[TMEM104]] | -0.49 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[KLHL29]] | -0.49 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[MAPKAPK2]] | -0.48 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[ST3GAL1]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[CARS2]] | -0.47 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[VASP]] | -0.47 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.397). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-17.4, 1.1); signed map (10.0, -26.4). **Vector** length 66.5, 24.8% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +8.1 | +4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.6 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | -12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | -13.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -4.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +6.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | +1.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:135,361,795-135,510,145 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLONE243, NOT4H; previously NOT4 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers CCCH-type; RNA binding motif containing; CCR4-NOT transcription complex; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O95628](https://www.uniprot.org/uniprotkb/O95628) (CCR4-NOT transcription complex subunit 4):

> Has E3 ubiquitin ligase activity, promoting ubiquitination and degradation of target proteins. Involved in activation of the JAK/STAT pathway. Catalyzes ubiquitination of methylated RBM15. Plays a role in quality control of translation of mitochondrial outer membrane-localized mRNA. As part of the PINK1-regulated signaling, upon mitochondria damage, ubiquitinates ABCE1 and thereby recruits autophagy receptors to the mitochondrial outer membrane to initiate mitophagy.

**Summary**, from NCBI Gene [4850](https://www.ncbi.nlm.nih.gov/gene/4850):

> The protein encoded by this gene is a subunit of the CCR4-NOT complex, a global transcriptional regulator. The encoded protein interacts with CNOT1 and has E3 ubiquitin ligase activity. Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:7880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7880) · Entrez [4850](https://www.ncbi.nlm.nih.gov/gene/4850) · UniProt [O95628](https://www.uniprot.org/uniprotkb/O95628) · Ensembl [ENSG00000080802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080802)

## Data

Gene col 1289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1289); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1289]; `tensor/DDL_lfc|DDL_z.npy` [1289]; `embed/gene_vectors.npy` [1289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1289 or target_col == 1289). Every well: [[CNOT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
