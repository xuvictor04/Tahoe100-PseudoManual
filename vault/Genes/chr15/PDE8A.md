---
symbol: "PDE8A"
type: "gene"
col: 1049
ensembl_id: "ENSG00000073417"
name: "phosphodiesterase 8A"
location: "15q25.3"
module: 7
arm: "-"
pooled_cpm: 292.77
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PDE8A

*phosphodiesterase 8A* — 15q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.26× (z +6.3, q 2e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.330× (z -29.4, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.445× (z -22.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALGPS1]] (+0.59, fdr 2e-05), [[DCUN1D4]] (+0.57, fdr 1e-05), [[SLC25A29]] (+0.57, fdr 2e-05); moves opposite to [[ZNF268]] (-0.59, fdr 1e-05), [[ZNF614]] (-0.58, fdr 1e-05), [[ZNF252P]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +6.3 | 2e-07 | 26/48 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +5.5 | 9e-06 | 27/49 (SNU-423, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.22×** | +5.1 | 6e-05 | 23/48 (SNU-1, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.2 | 0.003 | 18/48 (SW48, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +4.0 | 0.008 | 14/47 (HEC-1-A, LOX-IMVI, …) | two highest doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.012 | 20/48 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.054 | 17/49 (PANC-1, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.09× | +3.4 | 0.054 | 8/49 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.13× | +3.3 | 0.055 | 5/49 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Tirabrutinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.055 | 2/48 (AsPC-1, BT-474) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.071 | 15/47 (LoVo, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.330×** | -29.4 | 0e+00 | 43/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.349×** | -29.0 | 0e+00 | 49/49 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.501×** | -26.9 | 0e+00 | 44/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.445×** | -22.3 | 0e+00 | 46/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.453×** | -21.8 | 0e+00 | 46/48 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.490×** | -19.6 | 0e+00 | 45/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.492×** | -18.0 | 0e+00 | 39/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -17.4 | 0e+00 | 46/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.548×** | -16.6 | 0e+00 | 42/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.590×** | -14.5 | 1e-45 | 42/48 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.788×** | -9.3 | 1e-18 | 30/49 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.788×** | -9.2 | 1e-18 | 28/48 (NCI-H2347, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -8.3 | 3e-15 | 38/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.735×** | -8.1 | 2e-14 | 30/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.570×** | -8.1 | 3e-14 | 28/49 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -5.2 | 4e-06 | 16/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.895× | -4.3 | 4e-04 | 15/48 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.862× | -4.1 | 0.001 | 18/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.871× | -3.8 | 0.003 | 21/48 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.876× | -3.6 | 0.005 | 12/47 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.005 | 22/47 (H4, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.881× | -3.5 | 0.009 | 19/48 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 493 | 0 | 22 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -28.9) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.286× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 211 | 0 | 17 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -33.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.484× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 343 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -27.2) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.264× (z -19.5) |
| [[HOP62 (line)]] | alt | 337 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -30.1) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.350× (z -16.3) |
| [[hTERT-HPNE (line)]] | wt | 671 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -25.7) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.205× (z -14.3) |
| [[A-172 (line)]] | wt | 193 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -24.1) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -17.2) |
| [[A549 (line)]] | wt | 625 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -29.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -21.3) |
| [[NCI-H2347 (line)]] | alt | 267 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.562× (z -13.2) |
| [[SW 900 (line)]] | alt | 282 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -22.4) ⚠ position correction uncertain · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -14.6) |
| [[LoVo (line)]] | wt | 446 | 1 | 9 (5 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.60× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -27.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 598 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -25.3) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.365× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 258 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -19.9) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.414× (z -15.6) |
| [[Panc 03.27 (line)]] | alt | 318 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.341× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 293 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -12.2) |
| [[SNU-423 (line)]] | alt | 215 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.356× (z -12.7) |
| [[HS-578T (line)]] | alt | 267 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.3) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.236× (z -13.0) |
| [[KATO III (line)]] | alt | 198 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.497× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 216 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -20.5) ⚠ position correction uncertain · without an alert: [[TAK-901 (drug)]] 5 µM 0.281× (z -10.4) |
| [[PANC-1 (line)]] | alt | 262 | 1 | 7 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.59× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.549× (z -11.1) |
| [[SW1417 (line)]] | alt | 248 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.503× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 237 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -17.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.538× (z -9.4) |
| [[LS 180 (line)]] | wt | 253 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -15.7) |
| [[NCI-H1792 (line)]] | alt | 325 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -25.1) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.402× (z -12.6) |
| [[RKO (line)]] | wt | 167 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -24.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.339× (z -14.7) |
| [[SHP-77 (line)]] | alt | 360 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.317× (z -16.5) |
| [[SK-MEL-2 (line)]] | alt | 268 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.322× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 293 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.5) ⚠ position correction uncertain | [[Panobinostat (drug)]] 5 µM 0.320× (z -16.6) |
| [[H4 (line)]] | wt | 291 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.385× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 285 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.325× (z -12.0) |
| [[Hs 766T (line)]] | wt | 197 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -16.9) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -10.6) |
| [[HT-29 (line)]] | alt | 207 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -11.6) |
| [[J82 (line)]] | alt | 198 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -23.7) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.579× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 262 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -28.1) ⚠ position correction uncertain · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -12.7) |
| [[SW48 (line)]] | wt | 164 | 1 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.76× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -15.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 391 | 2 (1 ⚠) | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.56× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -29.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 181 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.486× (z -11.2) |
| [[A498 (line)]] | wt | 256 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.325× (z -15.0) |
| [[C32 (line)]] | wt | 158 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -21.5) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.431× (z -11.2) |
| [[C-33 A (line)]] | alt | 281 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.453× (z -9.6) |
| [[SNU-1 (line)]] | wt | 211 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -16.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 263 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -8.7) |
| [[HCT15 (line)]] | alt | 223 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.469× (z -9.4) |
| [[SW 1271 (line)]] | alt | 503 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.8) ⚠ position correction uncertain |
| [[AN3 CA (line)]] | alt | 252 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.177× (z -8.5) |
| [[BT-474 (line)]] | alt | 102 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -12.2) |
| [[COLO 205 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -16.2) ⚠ position correction uncertain |
| [[NCI-H2122 (line)]] | alt | 317 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 203 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGPS1]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[DCUN1D4]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[SLC25A29]] | +0.57 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[TRIM62]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[MGAT5]] | +0.55 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP44]] | +0.54 | +0.52 / +0.36 | both halves | 9e-05 |  |
| [[CDS1]] | +0.53 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[ZNRF1]] | +0.53 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.53 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[RAD9A]] | +0.53 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[PGAP1]] | +0.52 | +0.58 / +0.36 | both halves | 1e-04 |  |
| [[PTMA]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF268]] | -0.59 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[ZNF614]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ZNF252P]] | -0.58 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[ZNF543]] | -0.56 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[GUF1]] | -0.54 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[ZNF252P-1]] | -0.54 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[ZBED9]] | -0.54 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[IL6ST]] | -0.53 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[SSU72]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TRMT6]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ZNF528]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers PDE8A's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NMB]] | B | NMB activity raises PDE8A's level | lines that do not express NMB (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without NMB | 0.060 | ⚠ within organs, on part of the lines; also absent: ENO2, ARFGEF3, STAT5A; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.396). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-29.5, 14.5); signed map (-32.9, 18.2). **Vector** length 106, 35.3% of its response variance represented; |z| ≥ 3 in 1,813 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | +5.9 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.4 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | -0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.5 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -3.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.3 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | -7.0 | -19.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -14.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.6 | -9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -3.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -4.4 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | -4.4 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | -4.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 8A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.3 — chr15:84,980,440-85,139,145 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT19550 |
| Gene groups (HGNC) | Phosphodiesterases; PAS domain containing |
| Reactome | 3 pathways, smallest: G alpha (s) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [O60658](https://www.uniprot.org/uniprotkb/O60658) (High affinity cAMP-specific and IBMX-insensitive 3',5'-cyclic phosphodiesterase 8A):

> Hydrolyzes the second messenger cAMP, which is a key regulator of many important physiological processes. May be involved in maintaining basal levels of the cyclic nucleotide and/or in the cAMP regulation of germ cell development. Binding to RAF1 reduces RAF1 'Ser-259' inhibitory-phosphorylation and stimulates RAF1-dependent EGF-activated ERK-signaling. Protects against cell death induced by hydrogen peroxide and staurosporine.

**Summary**, from NCBI Gene [5151](https://www.ncbi.nlm.nih.gov/gene/5151):

> The protein encoded by this gene belongs to the cyclic nucleotide phosphodiesterase (PDE) family, and PDE8 subfamily. This PDE hydrolyzes the second messenger, cAMP, which is a regulator and mediator of a number of cellular responses to extracellular signals. Thus, by regulating the cellular concentration of cAMP, this protein plays a key role in many important physiological processes. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided …

**Accessions** — [HGNC:8793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8793) · Entrez [5151](https://www.ncbi.nlm.nih.gov/gene/5151) · UniProt [O60658](https://www.uniprot.org/uniprotkb/O60658) · Ensembl [ENSG00000073417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073417)

## Data

Gene col 1049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1049); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1049]; `tensor/DDL_lfc|DDL_z.npy` [1049]; `embed/gene_vectors.npy` [1049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1049 or target_col == 1049). Every well: [[PDE8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
