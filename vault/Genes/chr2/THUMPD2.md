---
symbol: "THUMPD2"
type: "gene"
col: 6114
ensembl_id: "ENSG00000138050"
name: "THUMP domain 2 tRNA and snRNA guanosine methyltransferase"
location: "2p22.1"
module: 16
arm: "+"
pooled_cpm: 48.33
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 15
n_dd_up_clean: 23
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# THUMPD2

*THUMP domain 2 tRNA and snRNA guanosine methyltransferase* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.56× (z +24.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.396× (z -23.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COIL]] (+0.76, fdr 7e-06), [[ZC3HC1]] (+0.74, fdr 7e-06), [[LIPT1]] (+0.73, fdr 7e-06); moves opposite to [[SETD3]] (-0.64, fdr 1e-05), [[RECQL]] (-0.60, fdr 1e-05), [[EHBP1L1]] (-0.60, fdr 8e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +24.1 | 0e+00 | 48/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.09×** | +20.4 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +11.6 | 1e-28 | 44/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +8.7 | 5e-16 | 40/48 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +8.4 | 6e-15 | 37/48 (NCI-H1573, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +8.1 | 5e-14 | 33/47 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +7.4 | 1e-11 | 34/48 (NCI-H1573, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.44×** | +6.5 | 4e-09 | 35/48 (Panc 03.27, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 5e-09 | 33/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +6.5 | 5e-09 | 34/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.1 | 6e-08 | 30/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.0 | 7e-08 | 31/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.4 | 2e-06 | 25/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.73×** | +5.2 | 7e-06 | 29/48 (PANC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.67×** | +4.9 | 5e-05 | 24/47 (A498, RKO, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.60×** | +4.5 | 3e-04 | 24/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +4.4 | 3e-04 | 28/48 (SW1417, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 4e-04 | 23/47 (hTERT-HPNE, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.396×** | -23.7 | 0e+00 | 48/48 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.410×** | -16.1 | 0e+00 | 42/47 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.412×** | -16.1 | 0e+00 | 45/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.447×** | -14.6 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -13.9 | 1e-41 | 35/43 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.479×** | -12.8 | 1e-35 | 37/47 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.519×** | -11.4 | 3e-28 | 41/49 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.573×** | -10.1 | 5e-22 | 38/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.794×** | -5.9 | 2e-07 | 29/48 (SW1417, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.712×** | -5.7 | 8e-07 | 27/45 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -5.4 | 3e-06 | 25/47 (SNU-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.757×** | -5.1 | 2e-05 | 26/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.777×** | -4.6 | 2e-04 | 26/47 (SW480, LS 180, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.787×** | -4.2 | 0.001 | 20/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.015 | 15/48 (SW48, A549, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.886× | -3.1 | 0.066 | 6/49 (NCI-H2030, HCT15, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.845× | -3.0 | 0.079 | 11/48 (RKO, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 70.5 | 2 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -18.4) |
| [[SW480 (line)]] | alt | 53.9 | 3 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -16.9) |
| [[NCI-H23 (line)]] | alt | 59.5 | 2 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -27.2) |
| [[RKO (line)]] | wt | 75.1 | 3 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -23.7) |
| [[NCI-H2347 (line)]] | alt | 41.9 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 71.3 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.370× (z -12.6) |
| [[SW1417 (line)]] | alt | 49.2 | 2 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.251× (z -13.9) |
| [[KATO III (line)]] | alt | 51.7 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 53.4 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0952× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -18.1) |
| [[PANC-1 (line)]] | alt | 60.7 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -15.1) |
| [[A-427 (line)]] | wt | 80.6 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 81.3 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 45.4 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 62.0 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.5) |
| [[SNU-1 (line)]] | wt | 80.9 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0996× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -10.5) |
| [[A498 (line)]] | wt | 40.7 | 3 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -16.3) |
| [[A549 (line)]] | wt | 52.8 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 52.0 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.64× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -15.3) |
| [[LS 180 (line)]] | wt | 60.4 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.0) |
| [[SW48 (line)]] | wt | 72.9 | 0 | 6 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0743× (z -19.9) |
| [[A-172 (line)]] | wt | 32.6 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -13.6) |
| [[HOP62 (line)]] | alt | 27.4 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -15.5) |
| [[BT-474 (line)]] | alt | 32.8 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.1) | [[Orlistat (drug)]] 0.05 µM 0.267× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 28.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +15.0) | — |
| [[C32 (line)]] | wt | 33.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -13.4) |
| [[COLO 205 (line)]] | alt | 57.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -9.9) |
| [[HT-29 (line)]] | alt | 30.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +18.7) | — |
| [[hTERT-HPNE (line)]] | wt | 34.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -10.3) |
| [[J82 (line)]] | alt | 24.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +15.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.0) |
| [[LoVo (line)]] | wt | 33.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 40.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.5) |
| [[H4 (line)]] | wt | 54.6 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -10.3) |
| [[HCT15 (line)]] | alt | 65.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -17.0) |
| [[Hs 766T (line)]] | wt | 24.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.1) |
| [[HS-578T (line)]] | alt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 51.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -16.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 38.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.7) |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -12.8) |
| [[SW 900 (line)]] | alt | 31.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COIL]] | +0.76 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[LIPT1]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[PLD6]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[POLR3C]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MRPS9]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[MIOS]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TIMM9]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.64 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[RECQL]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[EHBP1L1]] | -0.60 | -0.57 / -0.59 | both halves | 8e-06 |  |
| [[MAPKAPK2]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TMBIM6]] | -0.57 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[IQGAP1]] | -0.57 | -0.55 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises THUMPD2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM169A]] | B | FAM169A activity raises THUMPD2's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without FAM169A | 0.014 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.2, 7.3); signed map (2.9, -22.7). **Vector** length 135, 43.7% of its response variance represented; |z| ≥ 3 in 1,278 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +12.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +12.2 | +24.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.0 | +20.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +11.2 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.0 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +5.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.3 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +5.3 | +5.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.2 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +2.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -23.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -16.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.8 | -1.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.4 | -2.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | THUMP domain 2 tRNA and snRNA guanosine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:39,736,060-39,779,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2454; previously C2orf8 |
| Gene groups (HGNC) | 7BS N2-guanosine RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTF0](https://www.uniprot.org/uniprotkb/Q9BTF0) (U6 snRNA):

> Catalytic subunit of the THUMPD2-TRM112 methyltransferase complex, that specifically mediates the S-adenosyl-L-methionine-dependent N(2)-methylation of guanosine nucleotides, most probably at position 72 (m2G72), in the U6snRNA of the major spliceosome. This modification in the U6 snRNA affects the constitutive splicing efficiency of introns that have suboptimal splice sites and can impact final mRNA levels.

**Summary**, from NCBI Gene [80745](https://www.ncbi.nlm.nih.gov/gene/80745):

> Enables U6 snRNA (guanine-N(2))-methyltransferase activity. Involved in regulation of alternative mRNA splicing, via spliceosome. Part of tRNA methyltransferase complex. Is active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14890) · Entrez [80745](https://www.ncbi.nlm.nih.gov/gene/80745) · UniProt [Q9BTF0](https://www.uniprot.org/uniprotkb/Q9BTF0) · Ensembl [ENSG00000138050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138050)

## Data

Gene col 6114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6114); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6114]; `tensor/DDL_lfc|DDL_z.npy` [6114]; `embed/gene_vectors.npy` [6114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6114 or target_col == 6114). Every well: [[THUMPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THUMPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
