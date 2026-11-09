---
symbol: "RYBP"
type: "gene"
col: 8725
ensembl_id: "ENSG00000163602"
name: "RING1 and YY1 binding protein"
location: "3p13"
module: 79
arm: "+"
pooled_cpm: 195.6
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 28
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# RYBP

*RING1 and YY1 binding protein* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.47× (z +25.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.383× (z -13.2, q 4e-37, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.771× (z -3.7, q 0.021, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (NCI-H2347 0.160×, SHP-77 0.154×, CFPAC-1 0.207×, NCI-H1573 0.282×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2347 0.214×, SW1417 0.300×, Panc 03.27 0.322×, NCI-H1573 0.339×, …; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADM]] (+0.68, fdr 9e-06), [[RLF]] (+0.65, fdr 8e-06), [[RAB8B]] (+0.65, fdr 1e-05); moves opposite to [[TIMM23B-AGAP6]] (-0.69, fdr 7e-06), [[AGAP6]] (-0.65, fdr 1e-05), [[MCM3AP]] (-0.65, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARIH2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.47×** | +25.1 | 0e+00 | 48/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +13.8 | 1e-40 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.68×** | +13.6 | 1e-39 | 47/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +12.3 | 1e-32 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.35×** | +12.2 | 3e-32 | 45/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.05×** | +12.1 | 1e-31 | 49/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +11.2 | 2e-27 | 46/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +10.5 | 7e-24 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +10.0 | 1e-21 | 44/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +8.5 | 8e-16 | 40/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +8.2 | 2e-14 | 40/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.89×** | +7.9 | 1e-13 | 43/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +7.4 | 4e-12 | 41/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.55×** | +6.0 | 6e-08 | 46/49 (SW 900, HOP62, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 2e-07 | 41/49 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +5.5 | 1e-06 | 32/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (NCI-H2347 0.160×, SHP-77 0.154×, CFPAC-1 0.207×, NCI-H1573 0.282×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2347 0.214×, SW1417 0.300×, Panc 03.27 0.322×, NCI-H1573 0.339×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.383×** | -13.2 | 4e-37 | 44/44 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.421×** | -12.4 | 9e-33 | 47/49 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.689×** | -4.9 | 1e-04 | 27/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.744×** | -4.1 | 0.006 | 34/47 (NCI-H2347, CHP-212, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.771×** | -3.7 | 0.021 | 29/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.792×** | -3.3 | 0.077 | 28/48 (NCI-H1792, SW48, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.796× | -3.2 | 0.10 | 25/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.803× | -3.2 | 0.10 | 27/48 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.803× | -3.1 | 0.10 | 27/48 (NCI-H1573, HCT15, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.807× | -3.1 | 0.10 | 20/48 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.801× | -3.1 | 0.10 | 21/49 (A-172, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 169 | 17 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +24.4) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 117 | 17 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +22.6) | — |
| [[PANC-1 (line)]] | alt | 94.7 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +24.5) | — |
| [[SW1417 (line)]] | alt | 391 | 10 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -14.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 202 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +19.4) | — |
| [[KATO III (line)]] | alt | 145 | 11 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +26.2) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -10.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 185 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +21.1) | — |
| [[SK-MEL-2 (line)]] | alt | 298 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -12.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 161 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +26.4) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 174 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -10.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 267 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -13.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 189 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 405 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -19.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 335 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +24.0) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -13.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 196 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.428× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 189 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +16.1) | — |
| [[C32 (line)]] | wt | 357 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 266 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +23.5) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -15.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 203 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -12.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 173 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +13.4) | — |
| [[A-427 (line)]] | wt | 81.5 | 6 | 0 | [[Harringtonine (drug)]] 5 µM 3.92× (z +14.8) | — |
| [[hTERT-HPNE (line)]] | wt | 186 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 123 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 320 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 136 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +25.0) | — |
| [[HS-578T (line)]] | alt | 220 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +15.2) | — |
| [[HT-29 (line)]] | alt | 165 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.8) | — |
| [[J82 (line)]] | alt | 215 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +19.1) | — |
| [[NCI-H1792 (line)]] | alt | 102 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +17.9) | — |
| [[SHP-77 (line)]] | alt | 154 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -18.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 238 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +15.7) | — |
| [[A498 (line)]] | wt | 121 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +21.7) | — |
| [[CFPAC-1 (line)]] | alt | 223 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -15.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 288 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.66× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 149 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 214 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.88× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -13.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 196 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 242 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 147 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 198 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.68× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 114 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.8) | — |
| [[RKO (line)]] | wt | 204 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 132 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 290 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -12.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +16.9) | — |
| [[SNU-1 (line)]] | wt | 199 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.3) | — |
| [[SW 1088 (line)]] | alt | 249 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.0) | — |
| [[NCI-H2122 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 312 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADM]] | +0.68 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[RLF]] | +0.65 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[RAB8B]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ARL4D]] | +0.64 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[HILPDA]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[PPP1R3C]] | +0.62 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[MIDEAS]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MYLIP]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[GPR160]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MXI1]] | +0.61 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[FHIP1A]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | -0.69 | -0.59 / -0.73 | both halves | 7e-06 |  |
| [[AGAP6]] | -0.65 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[MCM3AP]] | -0.65 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[C1orf159]] | -0.64 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[MCM9]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[TMEM11-DT]] | -0.61 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[ARIH2]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[KMT2D]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 | pathway: Transcriptional regulation by RUNX1 |
| [[LIN52]] | -0.59 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[RCC1L]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ATR]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARIH2]] | C | ARIH2's natural level strengthens RYBP's drug response | ARIH2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.00; direction clear | 0.046 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, -12.9); signed map (-8.7, 16.5). **Vector** length 109, 49.2% of its response variance represented; |z| ≥ 3 in 1,446 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.51 to 16); *hypoxia* (control, mean cos +0.54 to 5); *glycolysis* (hallmark, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.5 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.4 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.3 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.9 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +4.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | +1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.0 | +7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.0 | +5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.1 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +7.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | RING1 and YY1 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:72,371,825-72,446,621 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YEAF1, AAP1, DEDAF |
| Gene groups (HGNC) | Zinc fingers RANBP2-type |
| Reactome | 3 pathways, smallest: Transcriptional Regulation by E2F6; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N488](https://www.uniprot.org/uniprotkb/Q8N488) (RING1 and YY1-binding protein):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1-like complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. Component of a PRC1-like complex that mediates monoubiquitination of histone H2A 'Lys-119' on …

**Summary**, from NCBI Gene [23429](https://www.ncbi.nlm.nih.gov/gene/23429):

> Enables nucleic acid binding activity. Involved in several processes, including negative regulation of proteasomal ubiquitin-dependent protein catabolic process; positive regulation of DNA-templated transcription; and positive regulation of apoptotic process. Located in nucleoplasm. Part of PcG protein complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10480) · Entrez [23429](https://www.ncbi.nlm.nih.gov/gene/23429) · UniProt [Q8N488](https://www.uniprot.org/uniprotkb/Q8N488) · Ensembl [ENSG00000163602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163602)

## Data

Gene col 8725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8725); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8725]; `tensor/DDL_lfc|DDL_z.npy` [8725]; `embed/gene_vectors.npy` [8725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8725 or target_col == 8725). Every well: [[RYBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RYBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
