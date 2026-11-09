---
symbol: "ADAM10"
type: "gene"
col: 6085
ensembl_id: "ENSG00000137845"
name: "ADAM metallopeptidase domain 10"
location: "15q21.3"
module: 11
arm: "-"
pooled_cpm: 286.11
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ADAM10

*ADAM metallopeptidase domain 10* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.22× (z +5.8, q 3e-06, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~5% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RKO 2.22×, HOP62 1.79×, A-172 1.78×, HS-578T 1.74×, …; ⚠ cell-cycle shift, explains ~5% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 1.77×, RKO 1.60×, HOP62 1.41×, NCI-H460 1.40×; ⚠ cell-cycle shift, explains ~10% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 1.91×, RKO 2.10×, HOP62 1.63×; ⚠ cell-cycle shift, explains ~4% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (CFPAC-1 1.47×); [[Cobimetinib (drug)]] 5 µM in 1 line (LoVo 1.53×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.538× (z -27.3, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED4]] (+0.64, fdr 1e-05), [[SETD3]] (+0.61, fdr 1e-05), [[MGAT4A]] (+0.61, fdr 3e-05); moves opposite to [[ZNF197]] (-0.61, fdr 1e-05), [[MRPL58]] (-0.61, fdr 1e-05), [[DNAJC2]] (-0.61, fdr 3e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6085.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RKO 2.22×, HOP62 1.79×, A-172 1.78×, HS-578T 1.74×, …; ⚠ cell-cycle shift, explains ~5% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 1.77×, RKO 1.60×, HOP62 1.41×, NCI-H460 1.40×; ⚠ cell-cycle shift, explains ~10% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 1.91×, RKO 2.10×, HOP62 1.63×; ⚠ cell-cycle shift, explains ~4% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (CFPAC-1 1.47×); [[Cobimetinib (drug)]] 5 µM in 1 line (LoVo 1.53×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +5.8 | 3e-06 | 24/48 (RKO, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.19× | +5.1 | 1e-04 | 22/50 (HT-29, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.09× | +3.9 | 0.021 | 7/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.09× | +3.7 | 0.032 | 17/49 (AsPC-1, RKO, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 1.22× | +3.3 | 0.11 | 21/49 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.12 | 4/48 (A549, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -27.3 | 0e+00 | 43/48 (SNU-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.521×** | -20.3 | 0e+00 | 45/48 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.540×** | -18.5 | 0e+00 | 47/48 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.587×** | -16.0 | 0e+00 | 44/47 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.662×** | -12.8 | 1e-35 | 45/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -10.9 | 1e-25 | 38/48 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -9.5 | 1e-19 | 38/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.765×** | -8.3 | 6e-15 | 35/48 (KATO III, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.772×** | -7.6 | 2e-12 | 34/48 (A498, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.776×** | -7.3 | 2e-11 | 29/45 (SNU-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -6.7 | 8e-10 | 27/48 (SNU-1, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.826×** | -5.9 | 1e-07 | 24/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.828×** | -5.7 | 7e-07 | 22/44 (SNU-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -5.0 | 2e-05 | 22/48 (BT-474, SNU-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change | 0.856× | -4.8 | 5e-05 | 22/49 (SNU-1, LoVo, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.853× | -4.6 | 1e-04 | 18/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.906× | -4.4 | 4e-04 | 6/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.775×** | -4.2 | 9e-04 | 23/48 (HEC-1-A, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.781×** | -4.0 | 0.002 | 22/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.879× | -4.0 | 0.002 | 8/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 1,748 | 0 | 16 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -32.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.275× (z -31.4) |
| [[A498 (line)]] | wt | 500 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -16.6) |
| [[KATO III (line)]] | alt | 386 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -21.6) |
| [[HEC-1-A (line)]] | alt | 408 | 0 | 11 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.419× (z -16.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.589× (z -10.5) |
| [[LS 180 (line)]] | wt | 254 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 591 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -23.3) |
| [[LoVo (line)]] | wt | 314 | 1 | 7 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.53× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -18.8) |
| [[SW 900 (line)]] | alt | 202 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -23.5) |
| [[COLO 205 (line)]] | alt | 485 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -22.2) |
| [[NCI-H1573 (line)]] | alt | 295 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -16.4) |
| [[HOP62 (line)]] | alt | 190 | 2 (2 ⚠) | 4 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.5) ⚠ cell-cycle shift, explains ~5% of this change | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -22.6) |
| [[HT-29 (line)]] | alt | 282 | 2 (2 ⚠) | 4 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +12.6) ⚠ cell-cycle shift, explains ~4% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.542× (z -12.3) |
| [[PANC-1 (line)]] | alt | 280 | 1 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -15.1) |
| [[A-172 (line)]] | wt | 205 | 1 (1 ⚠) | 4 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.8) ⚠ cell-cycle shift, explains ~5% of this change | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -19.8) |
| [[BT-474 (line)]] | alt | 274 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -20.5) |
| [[HS-578T (line)]] | alt | 145 | 1 (1 ⚠) | 4 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.7) ⚠ cell-cycle shift, explains ~5% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.451× (z -12.9) |
| [[J82 (line)]] | alt | 271 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -14.3) |
| [[RKO (line)]] | wt | 214 | 3 (3 ⚠) | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.9) ⚠ cell-cycle shift, explains ~5% of this change | [[Harringtonine (drug)]] 0.5 µM 0.562× (z -9.6) |
| [[SW480 (line)]] | alt | 240 | 1 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.30× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 5 µM 0.574× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.646× (z -9.0) |
| [[A549 (line)]] | wt | 319 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -15.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.618× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 286 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +12.9) ⚠ cell-cycle shift, explains ~10% of this change | [[Dinaciclib (drug)]] 5 µM 0.433× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.587× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 290 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -16.4) |
| [[Hs 766T (line)]] | wt | 389 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 254 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.663× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 294 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -28.1) |
| [[NCI-H2030 (line)]] | alt | 171 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 179 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -20.5) |
| [[NCI-H2347 (line)]] | alt | 210 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 157 | 1 (1 ⚠) | 3 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.7) ⚠ cell-cycle shift, explains ~5% of this change | [[Harringtonine (drug)]] 0.5 µM 0.536× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 412 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -22.2) |
| [[A-427 (line)]] | wt | 180 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -22.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 208 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -16.7) |
| [[hTERT-HPNE (line)]] | wt | 216 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 270 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -10.9) |
| [[SNU-423 (line)]] | alt | 168 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -13.4) |
| [[SW1417 (line)]] | alt | 233 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.635× (z -12.1) |
| [[HCT15 (line)]] | alt | 238 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 259 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -12.7) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW 1271 (line)]] | alt | 308 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.160× (z -9.6) |
| [[SW48 (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.3) |
| [[AN3 CA (line)]] | alt | 238 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 240 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 231 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 220 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 231 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 184 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED4]] | +0.64 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[SETD3]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MGAT4A]] | +0.61 | +0.63 / +0.44 | both halves | 3e-05 | pathway: Post-translational protein phosphorylation |
| [[STAU1]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[G3BP2]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[TMBIM6]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SBNO1]] | +0.58 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[MLEC]] | +0.58 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[KIAA1958]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[SRGAP2]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[STT3B]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PHTF2]] | +0.56 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF197]] | -0.61 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[MRPL58]] | -0.61 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[DNAJC2]] | -0.61 | -0.67 / -0.46 | both halves | 3e-05 |  |
| [[ZC3HC1]] | -0.60 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[YJU2]] | -0.60 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[CCDC43]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[MRPL38]] | -0.58 | -0.65 / -0.40 | both halves | 4e-05 |  |
| [[ZNF181]] | -0.58 | -0.64 / -0.49 | both halves | 2e-05 |  |
| [[NDUFB9]] | -0.58 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[ARL14EP]] | -0.58 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[CCDC102A]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[FASTKD2]] | -0.57 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-31.5, 6.2); signed map (-52.9, -6.7). **Vector** length 126, 38.8% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +5.8 | +5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +5.7 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.5 | -16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.6 | -20.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.7 | -27.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.3 | -10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.1 | -9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -8.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.2 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:58,588,809-58,749,791 (-) |
| Ensembl biotype | protein_coding |
| Also known as | kuz, MADM, HsT18717, CD156C |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing; CD molecules |
| Hallmark sets | APICAL_SURFACE, PROTEIN_SECRETION |
| Reactome | 34 pathways, smallest: Constitutive Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant; Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant; NOTCH4 Activation and Transmission of Signal to the Nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [O14672](https://www.uniprot.org/uniprotkb/O14672) (Disintegrin and metalloproteinase domain-containing protein 10):

> Transmembrane metalloprotease which mediates the ectodomain shedding of a myriad of transmembrane proteins, including adhesion proteins, growth factor precursors and cytokines being essential for development and tissue homeostasis. Associates with six members of the tetraspanin superfamily TspanC8 which regulate its exit from the endoplasmic reticulum and its substrate selectivity. Cleaves the membrane-bound precursor of TNF at '76-Ala-|-Val-77' to its mature soluble form. Responsible for the …

**Summary**, from NCBI Gene [102](https://www.ncbi.nlm.nih.gov/gene/102):

> Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:188) · Entrez [102](https://www.ncbi.nlm.nih.gov/gene/102) · UniProt [O14672](https://www.uniprot.org/uniprotkb/O14672) · Ensembl [ENSG00000137845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137845)

## Data

Gene col 6085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6085); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6085]; `tensor/DDL_lfc|DDL_z.npy` [6085]; `embed/gene_vectors.npy` [6085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6085 or target_col == 6085). Every well: [[ADAM10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
