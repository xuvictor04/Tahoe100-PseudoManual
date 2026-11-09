---
symbol: "ZC4H2"
type: "gene"
col: 4783
ensembl_id: "ENSG00000126970"
name: "zinc finger C4H2-type containing"
location: "Xq11.2"
module: 17
arm: "+"
pooled_cpm: 18.68
n_lines_expressing: 38
n_dd_up: 22
n_dd_down: 37
n_dd_up_clean: 18
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZC4H2

*zinc finger C4H2-type containing* — Xq11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.62× (z +7.0, q 1e-09, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.377× (z -19.8, q 0e+00, down in 31 of 36 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.347× (z -15.2, q 0e+00, down in 32 of 35 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPN]] (+0.58, fdr 1e-05), [[DYNC2H1]] (+0.58, fdr 2e-05), [[GNPDA2]] (+0.57, fdr 3e-05); moves opposite to [[QRICH2]] (-0.55, fdr 7e-05), [[CPEB2-DT]] (-0.54, fdr 8e-05), [[HIVEP1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SMIM10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +7.0 | 1e-09 | 23/35 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.40×** | +6.9 | 2e-09 | 24/36 (LS 180, KATO III, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 3e-07 | 21/35 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.9 | 6e-07 | 22/36 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +5.3 | 1e-05 | 18/35 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.0 | 5e-05 | 18/35 (HOP62, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 2e-04 | 20/35 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.002 | 10/36 (C-33 A, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +4.2 | 0.002 | 14/36 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.28×** | +3.6 | 0.018 | 6/35 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.018 | 13/35 (HOP62, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.018 | 13/35 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.023 | 14/35 (LS 180, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.023 | 11/35 (AsPC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.028 | 13/36 (C-33 A, LS 180, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.038 | 14/35 (NCI-H1573, HepG2/C3A, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.040 | 6/36 (KATO III, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.377×** | -19.8 | 0e+00 | 31/36 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.347×** | -15.2 | 0e+00 | 32/35 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.381×** | -13.9 | 2e-41 | 30/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.433×** | -11.6 | 9e-29 | 27/35 (NCI-H1792, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.470×** | -10.8 | 3e-25 | 26/34 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.464×** | -10.6 | 3e-24 | 29/34 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -10.2 | 1e-22 | 31/35 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.502×** | -9.9 | 4e-21 | 30/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -9.3 | 1e-18 | 27/36 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -7.6 | 2e-12 | 23/36 (NCI-H1792, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -7.2 | 3e-11 | 19/30 (Panc 03.27, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -7.2 | 4e-11 | 14/23 (HCT15, SW 900, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.621×** | -6.8 | 4e-10 | 25/36 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -5.8 | 3e-07 | 22/36 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.479×** | -5.5 | 1e-06 | 16/35 (RPMI-7951, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -5.4 | 2e-06 | 20/35 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -5.3 | 5e-06 | 18/35 (SW480, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -4.8 | 4e-05 | 16/35 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -4.7 | 7e-05 | 14/35 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -4.5 | 2e-04 | 17/35 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.755×** | -4.0 | 0.002 | 19/35 (C-33 A, RPMI-7951, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.765×** | -3.8 | 0.003 | 16/36 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -17.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -15.4) |
| [[PANC-1 (line)]] | alt | 34.9 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -16.5) |
| [[SNU-423 (line)]] | alt | 64.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -21.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -12.8) |
| [[HCT15 (line)]] | alt | 39.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.207× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 55.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.6) |
| [[HOP62 (line)]] | alt | 31.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 42.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0859× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 37.0 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.109× (z -15.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -10.0) |
| [[RKO (line)]] | wt | 50.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -9.9) |
| [[J82 (line)]] | alt | 25.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 28.0 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -12.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -9.7) |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -8.8) ⚠ toxic · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.118× (z -8.5) |
| [[Hs 766T (line)]] | wt | 6.97 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.127× (z -8.5) |
| [[KATO III (line)]] | alt | 35.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 8.03 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.102× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -8.5) |
| [[SW 1271 (line)]] | alt | 69.5 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.5 µM 0.0883× (z -9.1) |
| [[SW 900 (line)]] | alt | 18.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -9.0) ⚠ toxic |
| [[SW480 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -9.0) |
| [[A-172 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 5.95 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0968× (z -8.5) |
| [[C-33 A (line)]] | alt | 36.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.215× (z -9.1) |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -8.8) ⚠ toxic |
| [[H4 (line)]] | wt | 14.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0483× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0696× (z -10.9) |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 1 | — | [[Captopril (drug)]] 0.5 µM 0.0576× (z -9.2) |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPN]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[DYNC2H1]] | +0.58 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[GNPDA2]] | +0.57 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[ZNF354C]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[BCL9]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ZNF420]] | +0.56 | +0.37 / +0.61 | both halves | 7e-05 |  |
| [[MNAT1]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[IRAK1BP1]] | +0.55 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[DNAJC19]] | +0.54 | +0.29 / +0.46 | both halves | 2e-04 |  |
| [[ALKBH8]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[MAGED1]] | +0.54 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[THYN1]] | +0.53 | +0.25 / +0.55 | both halves | 4e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRICH2]] | -0.55 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[CPEB2-DT]] | -0.54 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[HIVEP1]] | -0.52 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[NFATC1]] | -0.50 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[SMIM12]] | -0.50 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[GCNT4]] | -0.50 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ABR]] | -0.49 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[RGS20]] | -0.49 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[SPESP1]] | -0.48 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[GRK4]] | -0.48 | -0.29 / -0.30 | both halves | 2e-04 |  |
| [[SIAH2-AS1]] | -0.48 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[CHD1-DT]] | -0.47 | -0.31 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM10]] | B | SMIM10 activity raises ZC4H2's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without SMIM10 | 0.062 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ZC4H2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.7, -1.0); signed map (-26.5, -11.4). **Vector** length 66.7, 12.7% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.9 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +4.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.1 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -10.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.3 | -19.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.3 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger C4H2-type containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq11.2 — chrX:64,915,802-65,034,713 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCA127; previously KIAA1166, WWS, MCS, MRXS4 |
| Gene groups (HGNC) | Zinc fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQZ6](https://www.uniprot.org/uniprotkb/Q9NQZ6) (Zinc finger C4H2 domain-containing protein):

> Involved in the development of several major noradrenergic neuron populations, including the locus coeruleus. Involved in neuronal development and in neuromuscular junction formation. Binds Zn(2+) ion with high affinity. The RNF220/ZC4H2 complex monoubiquitinates PHOX2A and PHOX2B to enhance their DNA-binding ability and transactivity (By similarity).

**Summary**, from NCBI Gene [55906](https://www.ncbi.nlm.nih.gov/gene/55906):

> This gene encodes a member of the zinc finger domain-containing protein family. This family member has a C-terminal zinc finger domain that is characterized by four cysteine residues and two histidine residues, and it also includes a coiled-coil region. This protein has been detected as an autoantigen in hepatocellular carcinoma patients. This gene has been identified as a potential candidate for X-linked cognitive disability. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:24931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24931) · Entrez [55906](https://www.ncbi.nlm.nih.gov/gene/55906) · UniProt [Q9NQZ6](https://www.uniprot.org/uniprotkb/Q9NQZ6) · Ensembl [ENSG00000126970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126970)

## Data

Gene col 4783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4783); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4783]; `tensor/DDL_lfc|DDL_z.npy` [4783]; `embed/gene_vectors.npy` [4783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4783 or target_col == 4783). Every well: [[ZC4H2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC4H2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
