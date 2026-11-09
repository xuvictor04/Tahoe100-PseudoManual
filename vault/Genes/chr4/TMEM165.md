---
symbol: "TMEM165"
type: "gene"
col: 5612
ensembl_id: "ENSG00000134851"
name: "transmembrane protein 165"
location: "4q12"
module: 49
arm: "+"
pooled_cpm: 226.17
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# TMEM165

*transmembrane protein 165* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +5.1, q 2e-04, up in 26 of 50 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (SHP-77 2.10×, C32 2.11×, AsPC-1 2.12×, LOX-IMVI 2.61×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 5 lines (C32 3.25×, SW480 2.04×, LOX-IMVI 2.86×, SW48 2.80×, …); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 2.35×, SW480 1.92×, SW48 2.65×); [[Auranofin (drug)]] 5 µM in 2 lines (SHP-77 1.97×, SW480 1.77×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.446× (z -16.8, q 0e+00, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.571× (z -15.9, q 0e+00, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APTR]] (+0.68, fdr 7e-06), [[ZFC3H1]] (+0.67, fdr 7e-06), [[PCGF3-AS1]] (+0.67, fdr 7e-06); moves opposite to [[SLX4IP]] (-0.67, fdr 7e-06), [[RIF1]] (-0.64, fdr 7e-06), [[CEP41]] (-0.63, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5612.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (SHP-77 2.10×, C32 2.11×, AsPC-1 2.12×, LOX-IMVI 2.61×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 5 lines (C32 3.25×, SW480 2.04×, LOX-IMVI 2.86×, SW48 2.80×, …); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 2.35×, SW480 1.92×, SW48 2.65×); [[Auranofin (drug)]] 5 µM in 2 lines (SHP-77 1.97×, SW480 1.77×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.1 | 2e-04 | 26/50 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.6 | 0.001 | 23/48 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.011 | 23/49 (SHP-77, C32, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | 1.32× | +3.2 | 0.19 | 14/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +3.1 | 0.19 | 11/49 (Panc 03.27, HT-29, …) | two highest doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.15× | +3.0 | 0.21 | 8/49 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.21 | 1/48 (H4) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -16.8 | 0e+00 | 38/44 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.571×** | -15.9 | 0e+00 | 34/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.499×** | -15.1 | 0e+00 | 45/49 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -12.9 | 4e-36 | 43/48 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.629×** | -10.0 | 1e-21 | 38/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.632×** | -9.9 | 3e-21 | 39/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -9.3 | 1e-18 | 36/47 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.655×** | -9.2 | 3e-18 | 38/48 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.636×** | -9.1 | 7e-18 | 33/45 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -6.7 | 9e-10 | 38/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.770×** | -5.7 | 8e-07 | 30/48 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.795×** | -5.0 | 3e-05 | 26/48 (BT-474, HS-578T, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.802×** | -4.8 | 8e-05 | 28/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.807×** | -4.6 | 1e-04 | 26/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.820×** | -4.3 | 7e-04 | 25/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.822×** | -4.2 | 8e-04 | 22/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.859× | -4.2 | 9e-04 | 16/48 (BT-474, HS-578T, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.849× | -3.5 | 0.012 | 15/49 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.851× | -3.5 | 0.014 | 15/48 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.043 | 10/48 (SW480, C32, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.867× | -3.1 | 0.047 | 14/49 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.867× | -3.1 | 0.047 | 17/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.049 | 20/47 (SW48, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.870× | -3.0 | 0.055 | 17/48 (PANC-1, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 354 | 0 | 14 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -21.8) |
| [[hTERT-HPNE (line)]] | wt | 524 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.4) |
| [[A549 (line)]] | wt | 220 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -32.5) |
| [[A498 (line)]] | wt | 336 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -21.7) |
| [[NCI-H2347 (line)]] | alt | 374 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -17.8) |
| [[SW 900 (line)]] | alt | 543 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -22.2) |
| [[CFPAC-1 (line)]] | alt | 355 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -16.1) |
| [[HOP62 (line)]] | alt | 360 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -20.2) |
| [[HS-578T (line)]] | alt | 400 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -20.5) |
| [[BT-474 (line)]] | alt | 349 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.432× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 552 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -18.5) |
| [[LoVo (line)]] | wt | 260 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.6) |
| [[A-172 (line)]] | wt | 182 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -30.3) |
| [[RPMI-7951 (line)]] | alt | 258 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.6) |
| [[C32 (line)]] | wt | 142 | 3 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +14.7) | [[Harringtonine (drug)]] 0.5 µM 0.425× (z -10.9) |
| [[H4 (line)]] | wt | 230 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.532× (z -8.8) |
| [[Hs 766T (line)]] | wt | 292 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.448× (z -11.0) |
| [[J82 (line)]] | alt | 244 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 291 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.126× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.387× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 185 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.281× (z -14.3) |
| [[PANC-1 (line)]] | alt | 157 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.5) |
| [[SHP-77 (line)]] | alt | 176 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.97× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -10.4) |
| [[SW48 (line)]] | wt | 153 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 295 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.248× (z -17.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 215 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.390× (z -10.3) |
| [[RKO (line)]] | wt | 139 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.446× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 111 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 226 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.6) |
| [[HT-29 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 68.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.513× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 89.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 264 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 129 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.364× (z -10.7) |
| [[SNU-423 (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.9) |
| [[SW 1088 (line)]] | alt | 481 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTR]] | +0.68 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ZFC3H1]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PCGF3-AS1]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | STRING 519 |
| [[SDHAP4-1]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[DPM1]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.63 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CLDN18]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MYDGF]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SRP54]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SWI5]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLX4IP]] | -0.67 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[RIF1]] | -0.64 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[CEP41]] | -0.63 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[BACE1-AS]] | -0.62 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.61 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[PUF60]] | -0.59 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[PIGO]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 | STRING 522 |
| [[DHX9]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[FKTN]] | -0.57 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ZNF512B]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.56 | -0.64 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM165's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Epirubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.1, -28.9); signed map (-45.5, 11.7). **Vector** length 136, 46.5% of its response variance represented; |z| ≥ 3 in 1,338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.7 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.0 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -6.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.1 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 165 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:55,395,957-55,453,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TMPT27, TPARL, GDT1, SLC64A1 |
| Gene groups (HGNC) | Solute carrier family 64 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC07](https://www.uniprot.org/uniprotkb/Q9HC07) (Putative divalent cation/proton antiporter TMEM165):

> Putative divalent cation:proton antiporter that exchanges calcium or manganese ions for protons across the Golgi membrane. Mediates the reversible transport of calcium or manganese to the Golgi lumen driven by the proton gradient and possibly the membrane potential generated by V-ATPase. Provides calcium or manganese cofactors to resident Golgi enzymes and contributes to the maintenance of an acidic luminal Golgi pH required for proper functioning of the secretory pathway (By similarity). …

**Summary**, from NCBI Gene [55858](https://www.ncbi.nlm.nih.gov/gene/55858):

> This gene encodes a predicted transmembrane protein with a perinuclear Golgi-like distribution in fibroblasts. Mutations in this gene are associated with the autosomal recessive disorder congenital disorder of glycosylation, type IIk. Knockdown of this gene's expression causes decreased sialylation in HEK cells and suggests this gene plays a role in terminal Golgi glycosylation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:30760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30760) · Entrez [55858](https://www.ncbi.nlm.nih.gov/gene/55858) · UniProt [Q9HC07](https://www.uniprot.org/uniprotkb/Q9HC07) · Ensembl [ENSG00000134851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134851)

## Data

Gene col 5612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5612); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5612]; `tensor/DDL_lfc|DDL_z.npy` [5612]; `embed/gene_vectors.npy` [5612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5612 or target_col == 5612). Every well: [[TMEM165 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM165.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
