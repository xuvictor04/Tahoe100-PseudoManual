---
symbol: "YWHAZ"
type: "gene"
col: 9031
ensembl_id: "ENSG00000164924"
name: "tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein zeta"
location: "8q22.3"
module: 111
arm: "+"
pooled_cpm: 627.1
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# YWHAZ

*tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein zeta* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +25.9, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.60× (z +5.7, q 1e-06, up in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (PANC-1 3.88×, C32 5.27×, A549 3.98×, NCI-H460 3.55×, …; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 4 lines (C32 4.13×, PANC-1 2.22×, AsPC-1 2.66×, SW1417 2.14×); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 3.82×, C32 4.59×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (C32 1.87×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 1.85×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.627× (z -10.9, q 1e-24, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42]] (+0.74, fdr 7e-06), [[MAPRE1]] (+0.69, fdr 1e-05), [[SPTBN1]] (+0.67, fdr 1e-05); moves opposite to [[LSM7]] (-0.73, fdr 7e-06), [[TMEM101]] (-0.65, fdr 1e-05), [[GLMN]] (-0.65, fdr 7e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[F2RL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9031.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (PANC-1 3.88×, C32 5.27×, A549 3.98×, NCI-H460 3.55×, …; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 4 lines (C32 4.13×, PANC-1 2.22×, AsPC-1 2.66×, SW1417 2.14×); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 3.82×, C32 4.59×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (C32 1.87×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 1.85×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +25.9 | 0e+00 | 49/49 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +22.3 | 0e+00 | 44/44 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +19.0 | 0e+00 | 45/45 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +6.4 | 2e-08 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +6.0 | 2e-07 | 29/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +5.7 | 1e-06 | 45/49 (C32, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.7 | 1e-06 | 40/48 (C32, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +5.4 | 5e-06 | 29/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +4.9 | 5e-05 | 26/48 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.23×** | +4.7 | 1e-04 | 25/48 (C32, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.011 | 21/48 (C32, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | 1.17× | +3.7 | 0.011 | 22/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.5 | 0.021 | 25/38 (A-172, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.15× | +3.2 | 0.058 | 12/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.062 | 8/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.078 | 13/47 (C32, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.083 | 4/49 (SW 1088, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9031.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.627×** | -10.9 | 1e-24 | 45/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.663×** | -9.6 | 3e-19 | 44/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.701×** | -8.3 | 2e-14 | 40/48 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.721×** | -7.3 | 4e-11 | 34/47 (HOP62, LoVo, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.818×** | -6.6 | 4e-09 | 27/48 (A549, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.838× | -5.8 | 5e-07 | 22/49 (HT-29, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.779×** | -5.8 | 5e-07 | 36/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.783×** | -5.7 | 1e-06 | 40/48 (KATO III, BT-474, …) | two highest doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -5.4 | 5e-06 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.795×** | -5.3 | 5e-06 | 32/48 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.810×** | -4.9 | 5e-05 | 29/48 (KATO III, hTERT-HPNE, …) | two highest doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.879× | -4.3 | 1e-03 | 8/48 (HEC-1-A, SNU-423, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.839× | -4.1 | 0.002 | 21/48 (SW 900, HS-578T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.845× | -3.9 | 0.003 | 22/48 (BT-474, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.842× | -3.8 | 0.005 | 22/48 (HT-29, A549, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.896× | -3.6 | 0.011 | 8/48 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.757×** | -3.4 | 0.023 | 25/49 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.866× | -3.3 | 0.027 | 14/48 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.828×** | -3.1 | 0.051 | 24/48 (SK-MEL-2, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.874× | -3.1 | 0.051 | 8/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.879× | -3.0 | 0.069 | 14/48 (HS-578T, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 472 | 16 (11 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +25.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.13× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 336 | 12 (12 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +23.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 591 | 5 (5 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +23.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.548× (z -10.1) |
| [[PANC-1 (line)]] | alt | 479 | 6 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +29.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.22× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.552× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 1,392 | 5 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +18.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.66× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.382× (z -16.5) |
| [[SW480 (line)]] | alt | 484 | 6 (6 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +21.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.574× (z -8.9) |
| [[A-427 (line)]] | wt | 307 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +22.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.532× (z -11.1) |
| [[SW1417 (line)]] | alt | 1,079 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.14× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 558 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +17.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.497× (z -12.4) |
| [[HOP62 (line)]] | alt | 764 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +20.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.556× (z -9.9) |
| [[LS 180 (line)]] | wt | 663 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +13.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -9.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.567× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 660 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +17.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.463× (z -11.8) |
| [[HCT15 (line)]] | alt | 599 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +16.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -10.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 646 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +18.0) ⚠ toxic; transcription drop | [[Ponatinib (drug)]] 5 µM 0.551× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 649 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +18.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.538× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 552 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +15.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.411× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 897 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +15.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -10.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.587× (z -9.4) |
| [[SW 900 (line)]] | alt | 702 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +16.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.503× (z -9.7) |
| [[A-172 (line)]] | wt | 475 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +20.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 853 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +19.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 682 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +15.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.558× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 311 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +11.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 575 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +15.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.586× (z -8.6) |
| [[HT-29 (line)]] | alt | 667 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +14.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -12.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 459 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +17.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.552× (z -9.0) |
| [[LoVo (line)]] | wt | 501 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +13.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.522× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 515 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +18.2) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.539× (z -9.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H1792 (line)]] | alt | 425 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +20.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -11.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 1,305 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +15.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 752 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.614× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 423 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.84× (z +17.0) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 688 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.450× (z -13.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.554× (z -9.9) |
| [[C-33 A (line)]] | alt | 311 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +18.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 405 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +14.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 405 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +17.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 987 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +20.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 623 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +19.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 675 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +19.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 572 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +18.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 556 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +19.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 316 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +21.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 503 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +19.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 472 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +15.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 424 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +17.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 747 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 510 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 525 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 516 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 550 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 530 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 754 |
| [[MAPRE1]] | +0.69 | +0.55 / +0.72 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints; STRING 417 |
| [[SPTBN1]] | +0.67 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[ANXA2]] | +0.67 | +0.67 / +0.74 | both halves | 7e-06 | STRING 630 |
| [[MYH9]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 415 |
| [[WDR1]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation |
| [[ACTR3]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 | pathway: RHO GTPase Effectors; STRING 468 |
| [[CTNNA1]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 914 |
| [[CAPNS1]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 | STRING 418 |
| [[DSG2]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 | pathway: Apoptosis |
| [[FLNA]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 | pathway: GP1b-IX-V activation signalling; STRING 538 |
| [[YWHAE]] | +0.62 | +0.45 / +0.70 | both halves | 3e-05 | same gene group; pathway: Activation of BAD and translocation to mitochondria; STRING 998 |

## Genes that move opposite

*63 of its nearest partners move opposite, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM7]] | -0.73 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[TMEM101]] | -0.65 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[GLMN]] | -0.65 | -0.38 / -0.72 | both halves | 7e-05 |  |
| [[ZNF500]] | -0.65 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[MRPL23]] | -0.65 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.64 | -0.55 / -0.59 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[RPP21]] | -0.64 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[NSFP1]] | -0.63 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[CDK5RAP1]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[CHCHD1]] | -0.62 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[COG7]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MRPL32]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2RL1]] | B | F2RL1 activity raises YWHAZ's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without F2RL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[F2RL1]] | B | F2RL1 activity strengthens YWHAZ's drug response | lines that do not express F2RL1 (20) vs lines expressing it (29) | the lines without F2RL1 respond 0.89× as strongly (z diff +0.46); strongest at Panobinostat 5 µM: 0.70x vs 0.58x (z diff +2.2) | 0.060 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1; target measured in part of the lines; both ways; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises YWHAZ's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.5, -18.6); signed map (-9.1, 34.2). **Vector** length 132, 52.3% of its response variance represented; |z| ≥ 3 in 1,652 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *EPHB-mediated forward signaling* (reactome, mean cos +0.57 to 6); *Leishmania infection* (reactome, mean cos +0.58 to 8); *Parasitic Infection Pathways* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +19.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +25.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +22.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.0 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.2 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | -9.4 | -7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.9 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -5.4 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -4.7 | +3.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.4 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -4.3 | -2.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.2 | -6.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein zeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:100,916,523-100,953,388 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCIP-1, 14-3-3-zeta; previously YWHAD |
| Gene groups (HGNC) | 14-3-3 phospho-serine/phospho-threonine binding proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 49 pathways, smallest: GP1b-IX-V activation signalling; NOTCH4 Activation and Transmission of Signal to the Nucleus; Regulation of localization of FOXO transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P63104](https://www.uniprot.org/uniprotkb/P63104) (14-3-3 protein zeta/delta):

> Adapter protein implicated in the regulation of a large spectrum of both general and specialized signaling pathways. Binds to a large number of partners, usually by recognition of a phosphoserine or phosphothreonine motif. Binding generally results in the modulation of the activity of the binding partner. Promotes cytosolic retention and inactivation of TFEB transcription factor by binding to phosphorylated TFEB. Induces ARHGEF7 activity on RAC1 as well as lamellipodia and membrane ruffle …

**Summary**, from NCBI Gene [7534](https://www.ncbi.nlm.nih.gov/gene/7534):

> This gene product belongs to the 14-3-3 family of proteins which mediate signal transduction by binding to phosphoserine-containing proteins. This highly conserved protein family is found in both plants and mammals, and this protein is 99% identical to the mouse, rat and sheep orthologs. The encoded protein interacts with IRS1 protein, suggesting a role in regulating insulin sensitivity. Several transcript variants that differ in the 5' UTR but that encode the same protein have been identified …

**Accessions** — [HGNC:12855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12855) · Entrez [7534](https://www.ncbi.nlm.nih.gov/gene/7534) · UniProt [P63104](https://www.uniprot.org/uniprotkb/P63104) · Ensembl [ENSG00000164924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164924)

## Data

Gene col 9031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9031); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9031]; `tensor/DDL_lfc|DDL_z.npy` [9031]; `embed/gene_vectors.npy` [9031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9031 or target_col == 9031). Every well: [[YWHAZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YWHAZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
