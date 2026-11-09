---
symbol: "MAP4K5"
type: "gene"
col: 263
ensembl_id: "ENSG00000012983"
name: "mitogen-activated protein kinase kinase kinase kinase 5"
location: "14q22.1"
module: 17
arm: "+"
pooled_cpm: 237.1
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MAP4K5

*mitogen-activated protein kinase kinase kinase kinase 5* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +14.2, q 5e-43, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.93× (z +11.5, q 3e-28, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.411× (z -18.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC73]] (+0.60, fdr 1e-05), [[COMMD7]] (+0.59, fdr 1e-05), [[SLC25A12]] (+0.57, fdr 1e-05); moves opposite to [[PSEN1]] (-0.58, fdr 1e-05), [[EIF4EBP2]] (-0.56, fdr 5e-05), [[PDCD6]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.63×** | +14.2 | 5e-43 | 37/48 (COLO 205, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.93×** | +11.5 | 3e-28 | 46/49 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +11.1 | 4e-26 | 41/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.65×** | +10.4 | 3e-23 | 45/48 (SW48, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +9.0 | 3e-17 | 39/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +8.0 | 1e-13 | 34/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +7.6 | 2e-12 | 41/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +6.7 | 1e-09 | 33/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.5 | 5e-09 | 34/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.39×** | +6.5 | 5e-09 | 33/48 (COLO 205, KATO III, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +5.7 | 7e-07 | 23/49 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.4 | 4e-06 | 30/38 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +5.2 | 7e-06 | 27/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.7 | 1e-04 | 30/45 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +4.6 | 1e-04 | 29/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 6e-04 | 32/49 (PANC-1, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.005 | 24/48 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.025 | 20/48 (NCI-H2030, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.1 | 0.048 | 5/48 (CHP-212, SNU-423, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.048 | 13/48 (A-172, HCT15, …) | rises with dose | plate-row cell shift |
| [[EX229 (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.078 | 20/48 (CFPAC-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.080 | 18/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.411×** | -18.3 | 0e+00 | 47/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.461×** | -16.0 | 0e+00 | 48/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -14.2 | 1e-43 | 43/49 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.610×** | -10.2 | 3e-22 | 45/48 (AN3 CA, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -6.9 | 6e-10 | 28/44 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -6.7 | 2e-09 | 29/48 (AN3 CA, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.731×** | -6.2 | 4e-08 | 39/48 (SW480, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.732×** | -6.2 | 4e-08 | 34/47 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.741×** | -5.9 | 2e-07 | 37/50 (SW480, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **0.758×** | -5.7 | 6e-07 | 33/49 (NCI-H2347, NCI-H2030, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.768×** | -5.5 | 2e-06 | 29/48 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.816×** | -4.2 | 0.001 | 25/48 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.821×** | -4.1 | 0.002 | 24/48 (A549, SHP-77, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.830×** | -3.9 | 0.004 | 24/48 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.834× | -3.8 | 0.006 | 23/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.842× | -3.6 | 0.012 | 22/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.852× | -3.3 | 0.027 | 16/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.856× | -3.2 | 0.036 | 15/48 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.857× | -3.2 | 0.039 | 18/48 (SNU-423, LoVo, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.860× | -3.1 | 0.046 | 15/49 (C-33 A, SHP-77, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.867× | -3.0 | 0.067 | 14/48 (SW 900, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 210 | 10 (4 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -17.5) |
| [[KATO III (line)]] | alt | 149 | 12 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +24.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -12.6) |
| [[LoVo (line)]] | wt | 262 | 8 (4 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +22.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.30× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -13.6) |
| [[SW48 (line)]] | wt | 390 | 6 (1 ⚠) | 6 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.40× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -14.1) |
| [[LS 180 (line)]] | wt | 238 | 8 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -13.9) |
| [[C32 (line)]] | wt | 241 | 3 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.97× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 320 | 7 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.32× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 184 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 296 | 3 (2 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.70× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -11.4) |
| [[J82 (line)]] | alt | 287 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.394× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 533 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -16.2) |
| [[RKO (line)]] | wt | 402 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -22.4) |
| [[SW 900 (line)]] | alt | 291 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -10.0) |
| [[A-172 (line)]] | wt | 170 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 179 | 3 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.356× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 127 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.04× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 293 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.14× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -12.4) |
| [[A549 (line)]] | wt | 233 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -16.7) |
| [[COLO 205 (line)]] | alt | 178 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +25.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 109 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +22.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 251 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.32× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -13.5) |
| [[PANC-1 (line)]] | alt | 133 | 1 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.78× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -13.3) |
| [[SHP-77 (line)]] | alt | 281 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.358× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -10.8) |
| [[A498 (line)]] | wt | 172 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -11.5) |
| [[AN3 CA (line)]] | alt | 381 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.267× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 165 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.0) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.377× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 217 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -15.9) |
| [[HOP62 (line)]] | alt | 271 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 4.64× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 278 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 287 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 177 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.15× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -11.8) |
| [[C-33 A (line)]] | alt | 278 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 302 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.89× (z +9.8) | — |
| [[A-427 (line)]] | wt | 166 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.444× (z -13.1) |
| [[BT-474 (line)]] | alt | 148 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.01× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 424 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -16.8) |
| [[SNU-423 (line)]] | alt | 211 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.6) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -9.9) |
| [[HCT15 (line)]] | alt | 233 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.94× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 196 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 243 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -8.5) |
| [[SNU-1 (line)]] | wt | 287 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -21.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 172 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.462× (z -10.2) |
| [[CHP-212 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 255 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC73]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[COMMD7]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SLC25A12]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[FAM133B]] | +0.57 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[QDPR]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[EPHA10]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[AQP11]] | +0.55 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[WDSUB1]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ESD]] | +0.54 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[DUSP12]] | +0.53 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[REV1]] | +0.52 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[OSBPL1A]] | +0.52 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSEN1]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[EIF4EBP2]] | -0.56 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[PDCD6]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[SEC16A]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[PIGG]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ODF2]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SENP5]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PPP1CA]] | -0.52 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[MAPKAPK2]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[LYPLA2]] | -0.51 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[PMPCA]] | -0.50 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[CYTH2]] | -0.50 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MAP4K5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRP3]] | B | LRP3 activity raises MAP4K5's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without LRP3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[PITPNA]] | C | PITPNA's natural level strengthens MAP4K5's drug response | PITPNA's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.01; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.4, -3.0); signed map (-23.9, -13.2). **Vector** length 98.7, 37.6% of its response variance represented; |z| ≥ 3 in 1,479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.2 | +14.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.8 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | +6.8 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.0 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.4 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.8 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.6 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.4 | +8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.9 | +4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | +9.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -1.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Rimonabant (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:50,418,501-50,561,126 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KHS1, GCKR, KHS |
| Gene groups (HGNC) | MAP4K family (GCK-I subfamily) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4K4](https://www.uniprot.org/uniprotkb/Q9Y4K4) (Mitogen-activated protein kinase kinase kinase kinase 5):

> May play a role in the response to environmental stress. Appears to act upstream of the JUN N-terminal pathway.

**Summary**, from NCBI Gene [11183](https://www.ncbi.nlm.nih.gov/gene/11183):

> This gene encodes a member of the serine/threonine protein kinase family, that is highly similar to yeast SPS1/STE20 kinase. Yeast SPS1/STE20 functions near the beginning of the MAP kinase signal cascades that is essential for yeast pheromone response. This kinase was shown to activate Jun kinase in mammalian cells, which suggested a role in stress response. Two alternatively spliced transcript variants encoding the same protein have been described for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6867) · Entrez [11183](https://www.ncbi.nlm.nih.gov/gene/11183) · UniProt [Q9Y4K4](https://www.uniprot.org/uniprotkb/Q9Y4K4) · Ensembl [ENSG00000012983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012983)

## Data

Gene col 263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 263); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 263]; `tensor/DDL_lfc|DDL_z.npy` [263]; `embed/gene_vectors.npy` [263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 263 or target_col == 263). Every well: [[MAP4K5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP4K5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
