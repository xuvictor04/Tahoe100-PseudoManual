---
symbol: "EPS8"
type: "gene"
col: 7528
ensembl_id: "ENSG00000151491"
name: "EGFR pathway substrate 8, signaling adaptor"
location: "12p12.3"
module: 106
arm: "+"
pooled_cpm: 415.79
n_lines_expressing: 45
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 25
direction_downstream: 9
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# EPS8

*EGFR pathway substrate 8, signaling adaptor* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +22.2, q 0e+00, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.602× (z -10.1, q 2e-21, down in 31 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.755× (z -5.8, q 1e-06, down in 26 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (LoVo 0.348×, HT-29 0.383×, CFPAC-1 0.408×, KATO III 0.448×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.211×, Panc 03.27 0.250×, SW1417 0.276×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (LoVo 0.336×, Panc 03.27 0.421×, SW1417 0.465×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.263×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GAREM1]] (+0.71, fdr 7e-06), [[FGD4]] (+0.67, fdr 7e-06), [[PELI1]] (+0.67, fdr 7e-06); moves opposite to [[DPP9]] (-0.61, fdr 8e-06), [[NPIPB11]] (-0.53, fdr 1e-05), [[PDCD6]] (-0.53, fdr 2e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[RASSF6]] → it (grade B ⚠); 9 go from it, the strongest it → [[LINC00511]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +22.2 | 0e+00 | 36/43 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +18.8 | 0e+00 | 42/43 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +10.8 | 6e-25 | 32/43 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +9.9 | 4e-21 | 34/43 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +8.9 | 1e-16 | 29/43 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +8.8 | 1e-16 | 27/43 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +7.4 | 2e-11 | 33/44 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +6.3 | 2e-08 | 25/42 (SK-MEL-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.9 | 2e-07 | 25/43 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.9 | 2e-07 | 23/43 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +5.6 | 1e-06 | 20/43 (PANC-1, C-33 A, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 4e-05 | 22/44 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 4e-05 | 22/43 (A-427, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 2e-04 | 24/43 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 21/43 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.15× | +4.1 | 0.001 | 15/43 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.001 | 20/43 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7528.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (LoVo 0.348×, HT-29 0.383×, CFPAC-1 0.408×, KATO III 0.448×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.211×, Panc 03.27 0.250×, SW1417 0.276×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (LoVo 0.336×, Panc 03.27 0.421×, SW1417 0.465×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.263×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -10.1 | 2e-21 | 31/39 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.737×** | -6.3 | 7e-08 | 26/44 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -5.8 | 1e-06 | 26/43 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -5.8 | 1e-06 | 22/44 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.768×** | -5.1 | 5e-05 | 23/40 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.810×** | -4.4 | 0.001 | 24/43 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.854× | -3.0 | 0.20 | 11/43 (C-33 A, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 296 | 16 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +17.3) | — |
| [[A-427 (line)]] | wt | 107 | 12 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +28.7) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -15.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 606 | 9 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -13.0) |
| [[LoVo (line)]] | wt | 2,819 | 1 (1 ⚠) | 11 (8 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.93× (z +10.1) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.211× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -23.8) |
| [[PANC-1 (line)]] | alt | 176 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +31.2) | — |
| [[SK-MEL-2 (line)]] | alt | 339 | 9 (3 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.40× (z +17.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 269 | 9 | 0 | [[Harringtonine (drug)]] 5 µM 6.54× (z +15.0) | — |
| [[SW 900 (line)]] | alt | 560 | 6 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 4.02× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 858 | 3 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 520 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -17.1) |
| [[KATO III (line)]] | alt | 447 | 5 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -15.5) |
| [[SW480 (line)]] | alt | 339 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.605× (z -9.1) |
| [[Hs 766T (line)]] | wt | 236 | 7 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.44× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 111 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 138 | 7 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.63× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 450 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 1,022 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -14.8) |
| [[RKO (line)]] | wt | 132 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +17.0) | — |
| [[SW48 (line)]] | wt | 353 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 822 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -13.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 688 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 443 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.4) |
| [[SNU-423 (line)]] | alt | 311 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.7) | — |
| [[A498 (line)]] | wt | 507 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.1) | — |
| [[HOP62 (line)]] | alt | 134 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.8) | — |
| [[HT-29 (line)]] | alt | 1,004 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 129 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.15× (z +11.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 2.36× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 177 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 243 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +17.4) | — |
| [[HepG2_C3A (line)]] | wt | 568 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.32× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 184 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 163 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 3.99× (z +11.5) | — |
| [[A-172 (line)]] | wt | 162 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.9) | — |
| [[A549 (line)]] | wt | 269 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.71× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 736 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -12.9) |
| [[H4 (line)]] | wt | 125 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.93× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 368 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 91.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 84.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 429 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.3 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 93.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 434 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 175 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAREM1]] | +0.71 | +0.67 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[FGD4]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[PELI1]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[PDLIM1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.60 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[TGFBR3]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SGPP2]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHA7]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[FOXO1]] | +0.58 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[SCNN1A]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 | pathway: Sensory Perception |
| [[SHROOM3]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[DNAJC15]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | -0.61 | -0.58 / -0.64 | both halves | 8e-06 |  |
| [[NPIPB11]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SPRED3]] | -0.50 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[IPPK]] | -0.50 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[SMG1P6]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[XPNPEP3]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CUTC]] | -0.48 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[KCNMA1]] | -0.48 | -0.52 / -0.49 | both halves | 1e-05 | pathway: Sensory Perception |
| [[ADGRL1-AS1]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ST3GAL3]] | -0.48 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF6]] | B | RASSF6 activity raises EPS8's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.92× lower at baseline in the lines without RASSF6 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[LINC00511]] | B | LINC00511 activity raises EPS8's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 2.96× lower at baseline in the lines without LINC00511 | 1e-03 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[TRIM31]] | B | TRIM31 activity raises EPS8's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.31× lower at baseline in the lines without TRIM31 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[DPP4]] | B | DPP4 activity raises EPS8's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.74× lower at baseline in the lines without DPP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[PPARG]] | B | PPARG activity raises EPS8's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without PPARG | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[FRK]] | B | FRK activity raises EPS8's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.62× lower at baseline in the lines without FRK | 0.005 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[LNX1]] | B | LNX1 activity raises EPS8's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without LNX1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[NEDD9]] | B | NEDD9 activity raises EPS8's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without NEDD9 | 0.009 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[TRIM29]] | B | TRIM29 activity raises EPS8's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without TRIM29 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises EPS8's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.94× lower at baseline in the lines without TMPRSS2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[THRB]] | B | THRB activity raises EPS8's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.26× lower at baseline in the lines without THRB | 0.013 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[GRAMD2B]] | B | GRAMD2B activity raises EPS8's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without GRAMD2B | 0.015 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00511]] | B | EPS8 activity raises LINC00511's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 5.24× lower at baseline in the lines without EPS8 | 0.008 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[ETS2]] | B | EPS8 activity raises ETS2's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 4.51× lower at baseline in the lines without EPS8 | 0.010 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[PDLIM1]] | B | EPS8 activity raises PDLIM1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 2.94× lower at baseline in the lines without EPS8 | 0.031 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[MBNL1]] | B | EPS8 activity raises MBNL1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without EPS8 | 0.045 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[PUM1]] | B | EPS8 activity lowers PUM1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 1.40× higher at baseline in the lines without EPS8 | 0.048 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[TES]] | B | EPS8 activity raises TES's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without EPS8 | 0.051 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[PPARG]] | B | EPS8 activity raises PPARG's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 3.56× lower at baseline in the lines without EPS8 | 0.056 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[UBE2E1]] | B | EPS8 activity raises UBE2E1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 1.29× lower at baseline in the lines without EPS8 | 0.074 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[GNAI1]] | B | EPS8 activity raises GNAI1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 2.27× lower at baseline in the lines without EPS8 | 0.082 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, 43.7); signed map (19.5, 27.1). **Vector** length 137, 47.7% of its response variance represented; |z| ≥ 3 in 1,567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.8 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.2 | +7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +18.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +5.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +5.6 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.5 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.1 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.5 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | EGFR pathway substrate 8, signaling adaptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:15,620,134-15,882,329 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EPS8 signaling adaptor family; SH3 domain containing |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12929](https://www.uniprot.org/uniprotkb/Q12929) (Epidermal growth factor receptor kinase substrate 8):

> Signaling adapter that controls various cellular protrusions by regulating actin cytoskeleton dynamics and architecture. Depending on its association with other signal transducers, can regulate different processes. Together with SOS1 and ABI1, forms a trimeric complex that participates in transduction of signals from Ras to Rac by activating the Rac-specific guanine nucleotide exchange factor (GEF) activity. Acts as a direct regulator of actin dynamics by binding actin filaments and has both …

**Summary**, from NCBI Gene [2059](https://www.ncbi.nlm.nih.gov/gene/2059):

> This gene encodes a member of the EPS8 family. This protein contains one PH domain and one SH3 domain. It functions as part of the EGFR pathway, though its exact role has not been determined. Highly similar proteins in other organisms are involved in the transduction of signals from Ras to Rac and growth factor-mediated actin remodeling. Alternate transcriptional splice variants of this gene have been observed but have not been thoroughly characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3420) · Entrez [2059](https://www.ncbi.nlm.nih.gov/gene/2059) · UniProt [Q12929](https://www.uniprot.org/uniprotkb/Q12929) · Ensembl [ENSG00000151491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151491)

## Data

Gene col 7528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7528); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7528]; `tensor/DDL_lfc|DDL_z.npy` [7528]; `embed/gene_vectors.npy` [7528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7528 or target_col == 7528). Every well: [[EPS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
