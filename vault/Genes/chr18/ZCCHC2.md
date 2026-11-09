---
symbol: "ZCCHC2"
type: "gene"
col: 6563
ensembl_id: "ENSG00000141664"
name: "zinc finger CCHC-type containing 2"
location: "18q21.33"
module: 32
arm: "+"
pooled_cpm: 61.84
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ZCCHC2

*zinc finger CCHC-type containing 2* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +7.8, q 4e-12, up in 26 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.535× (z -18.6, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFI6]] (+0.62, fdr 7e-06), [[ISG15]] (+0.62, fdr 7e-06), [[IFITM1]] (+0.61, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.8 | 4e-12 | 26/49 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +7.4 | 4e-11 | 34/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +5.4 | 2e-05 | 23/50 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +5.3 | 2e-05 | 26/49 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 2e-05 | 25/48 (MIA PaCa-2, A-427, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +5.0 | 5e-05 | 21/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +4.9 | 9e-05 | 19/48 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +4.7 | 2e-04 | 21/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.17× | +4.6 | 3e-04 | 19/48 (LS 180, SW480, …) | two highest doses | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 3e-04 | 22/49 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +4.0 | 0.003 | 11/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 20/48 (RKO, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 22/48 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.003 | 18/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.003 | 19/47 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.011 | 18/47 (SNU-423, A-172, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.535×** | -18.6 | 0e+00 | 45/48 (NCI-H1792, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.436×** | -17.5 | 0e+00 | 41/47 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -16.0 | 0e+00 | 32/42 (SHP-77, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.476×** | -14.5 | 1e-45 | 35/43 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.551×** | -12.1 | 1e-31 | 37/46 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.703×** | -7.4 | 1e-11 | 35/48 (CHP-212, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -7.2 | 5e-11 | 31/48 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -5.9 | 3e-07 | 27/47 (BT-474, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -5.0 | 4e-05 | 23/48 (A549, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.795×** | -4.8 | 8e-05 | 20/49 (PANC-1, SNU-423, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.675×** | -4.3 | 8e-04 | 15/36 (HS-578T, C32, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.814×** | -4.1 | 0.002 | 18/48 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.003 | 22/48 (HepG2/C3A, BT-474, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.874× | -4.0 | 0.003 | 15/49 (SHP-77, Panc 03.27, …) | all doses, flat |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.828×** | -4.0 | 0.003 | 18/48 (NCI-H1792, MIA PaCa-2, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.830×** | -3.9 | 0.003 | 22/48 (SNU-1, BT-474, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.879× | -3.8 | 0.004 | 17/49 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.841× | -3.6 | 0.009 | 18/49 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.793×** | -3.5 | 0.015 | 13/48 (PANC-1, BT-474, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.844× | -3.4 | 0.017 | 16/49 (A549, A498, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.851× | -3.4 | 0.019 | 17/47 (SNU-423, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 105 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.386× (z -12.8) |
| [[A498 (line)]] | wt | 82.0 | 2 (1 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.33× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.419× (z -8.9) |
| [[SNU-423 (line)]] | alt | 98.4 | 0 | 8 (7 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.367× (z -12.9) |
| [[HS-578T (line)]] | alt | 95.9 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.327× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 144 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.362× (z -15.0) |
| [[A-172 (line)]] | wt | 56.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.0) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.446× (z -10.5) |
| [[A-427 (line)]] | wt | 36.1 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +10.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -15.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[BT-474 (line)]] | alt | 141 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.431× (z -10.3) |
| [[C32 (line)]] | wt | 119 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0757× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.463× (z -9.9) |
| [[SHP-77 (line)]] | alt | 217 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -11.3) |
| [[LoVo (line)]] | wt | 88.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.432× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 59.2 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.414× (z -12.6) |
| [[LS 180 (line)]] | wt | 51.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +16.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 58.6 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.406× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 55.5 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.488× (z -10.7) |
| [[Hs 766T (line)]] | wt | 46.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.399× (z -10.7) |
| [[PANC-1 (line)]] | alt | 50.5 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.521× (z -11.6) |
| [[AN3 CA (line)]] | alt | 56.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -8.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.240× (z -10.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.439× (z -8.6) |
| [[COLO 205 (line)]] | alt | 54.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.256× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 68.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -12.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 44.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.4) ⚠ cell-cycle shift, explains ~15% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 64.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.351× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 51.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.0) ⚠ cell-cycle shift, explains ~15% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.264× (z -12.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 72.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.445× (z -9.4) |
| [[SW480 (line)]] | alt | 18.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.1) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 26.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.407× (z -8.5) |
| [[H4 (line)]] | wt | 71.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 40.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.1) | — |
| [[KATO III (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[NCI-H2347 (line)]] | alt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.02× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 63.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 49.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.327× (z -11.9) |
| [[RKO (line)]] | wt | 35.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -12.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -15.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -9.2) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI6]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ISG15]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[IFITM1]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[UBE2L6]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[IFI27]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TYMP]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[IFITM3]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[GBP4]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[OAS1]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[IFI44L]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[RSAD2]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PARP9]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises ZCCHC2's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.40× lower at baseline in the lines without SAMD9L | 0.038 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ZCCHC2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[OAS2]] | B | OAS2 activity raises ZCCHC2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without OAS2 | 0.074 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS3]] | B | OAS3 activity raises ZCCHC2's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without OAS3 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[IFI44]] | B | IFI44 activity raises ZCCHC2's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.44× lower at baseline in the lines without IFI44 | 0.087 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.7, 51.7); signed map (65.7, 29.3). **Vector** length 130, 38.4% of its response variance represented; |z| ≥ 3 in 1,379 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.55 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.54 to 27); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.51 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +6.3 | +7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.7 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.7 | +4.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -12.9 | -18.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.7 | -7.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.6 | -3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.8 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -7.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:62,523,025-62,587,709 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20281, KIAA1744, FLJ20222; previously C18orf49 |
| Gene groups (HGNC) | Zinc fingers CCHC-type |
| Matched by | ensembl_id |

UniProt [Q9C0B9](https://www.uniprot.org/uniprotkb/Q9C0B9) carries no function annotation.

**Summary**, from NCBI Gene [54877](https://www.ncbi.nlm.nih.gov/gene/54877):

> Predicted to enable nucleic acid binding activity; phosphatidylinositol binding activity; and zinc ion binding activity. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22916) · Entrez [54877](https://www.ncbi.nlm.nih.gov/gene/54877) · UniProt [Q9C0B9](https://www.uniprot.org/uniprotkb/Q9C0B9) · Ensembl [ENSG00000141664](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141664)

## Data

Gene col 6563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6563); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6563]; `tensor/DDL_lfc|DDL_z.npy` [6563]; `embed/gene_vectors.npy` [6563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6563 or target_col == 6563). Every well: [[ZCCHC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
