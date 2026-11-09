---
symbol: "GARNL3"
type: "gene"
col: 5934
ensembl_id: "ENSG00000136895"
name: "GTPase activating Rap/RanGAP domain like 3"
location: "9q33.3"
module: 18
arm: "+"
pooled_cpm: 31.61
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 20
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GARNL3

*GTPase activating Rap/RanGAP domain like 3* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.48× (z +17.6, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.317× (z -31.6, q 0e+00, down in 41 of 43 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.248× (z -26.0, q 0e+00, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLN]] (+0.72, fdr 7e-06), [[NEIL2]] (+0.71, fdr 7e-06), [[ANKRD27]] (+0.71, fdr 7e-06); moves opposite to [[USP11]] (-0.64, fdr 1e-05), [[CGGBP1]] (-0.63, fdr 1e-05), [[NBR1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 20 go from it, the strongest it → [[FXN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +17.6 | 0e+00 | 37/44 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +16.0 | 0e+00 | 35/44 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +14.0 | 5e-42 | 36/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +10.3 | 2e-22 | 34/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +9.0 | 3e-17 | 31/44 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.2 | 6e-11 | 26/44 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +7.2 | 6e-11 | 27/43 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +6.8 | 9e-10 | 27/44 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +6.7 | 1e-09 | 27/44 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +4.9 | 6e-05 | 16/44 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.8 | 8e-05 | 16/44 (A549, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.68×** | +4.6 | 2e-04 | 13/37 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +4.4 | 4e-04 | 10/44 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.25×** | +4.2 | 9e-04 | 18/43 (NCI-H460, A549, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.30×** | +4.2 | 9e-04 | 10/44 (HOP62, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.001 | 14/44 (NCI-H460, J82, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.004 | 11/43 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.008 | 11/43 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.317×** | -31.6 | 0e+00 | 41/43 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.248×** | -26.0 | 0e+00 | 39/44 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.469×** | -14.7 | 0e+00 | 30/43 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.489×** | -13.9 | 7e-42 | 32/43 (J82, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.497×** | -13.6 | 5e-40 | 35/44 (RKO, J82, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.287×** | -11.1 | 7e-27 | 33/44 (RKO, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.583×** | -10.5 | 9e-24 | 30/44 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.633×** | -8.9 | 4e-17 | 25/44 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.643×** | -8.6 | 5e-16 | 27/42 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.673×** | -7.7 | 7e-13 | 24/41 (SK-MEL-2, J82, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -7.0 | 1e-10 | 21/43 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -6.6 | 2e-09 | 23/44 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.713×** | -6.6 | 2e-09 | 23/44 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -6.2 | 2e-08 | 23/42 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.558×** | -5.2 | 7e-06 | 21/44 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.824×** | -3.8 | 0.004 | 13/44 (A-172, SNU-423, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.878× | -3.6 | 0.008 | 7/44 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.884× | -3.4 | 0.016 | 5/44 (LOX-IMVI, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.859× | -3.0 | 0.071 | 13/44 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.863× | -2.9 | 0.088 | 9/44 (PANC-1, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 71.4 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0371× (z -31.8) |
| [[A-172 (line)]] | wt | 40.8 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0540× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.103× (z -18.5) |
| [[J82 (line)]] | alt | 54.3 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -31.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 32.8 | 1 (1 ⚠) | 9 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.88× (z +11.0) ⚠ unreliable plate only | [[Harringtonine (drug)]] 0.5 µM 0.157× (z -19.2) |
| [[RKO (line)]] | wt | 123 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0547× (z -27.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.124× (z -19.5) |
| [[PANC-1 (line)]] | alt | 45.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -36.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.115× (z -25.6) |
| [[C-33 A (line)]] | alt | 71.3 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.280× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 46.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -21.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.178× (z -17.6) |
| [[BT-474 (line)]] | alt | 60.7 | 1 | 6 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.16× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -19.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.189× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 62.9 | 0 | 7 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -14.1) |
| [[SNU-423 (line)]] | alt | 53.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -26.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.149× (z -16.0) |
| [[SW48 (line)]] | wt | 59.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -11.6) |
| [[SW480 (line)]] | alt | 14.1 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.47× (z +12.6) | [[Harringtonine (drug)]] 5 µM 0.308× (z -9.6) |
| [[A498 (line)]] | wt | 31.7 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -17.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.199× (z -13.4) |
| [[HOP62 (line)]] | alt | 20.5 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.51× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.179× (z -12.2) |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0742× (z -19.7) |
| [[LOX-IMVI (line)]] | wt | 40.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.277× (z -11.2) |
| [[A549 (line)]] | wt | 28.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -17.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.244× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 40.6 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0581× (z -21.1) ⚠ toxic; cell-cycle shift, explains ~90% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.276× (z -9.6) |
| [[A-427 (line)]] | wt | 29.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.238× (z -10.6) |
| [[KATO III (line)]] | alt | 16.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.83× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 32.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.206× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -9.4) |
| [[AN3 CA (line)]] | alt | 35.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0666× (z -10.8) |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0633× (z -10.6) |
| [[Hs 766T (line)]] | wt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.159× (z -11.3) |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 10.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.26× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 21.9 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.80× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.248× (z -8.7) |
| [[SW1417 (line)]] | alt | 19.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.71× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -8.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0539× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0643× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.91 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLN]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[NEIL2]] | +0.71 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[DCAF4]] | +0.70 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.68 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SORD]] | +0.67 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[LIMK1]] | +0.67 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PACC1]] | +0.66 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PUS7]] | +0.66 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[TMEM241]] | +0.66 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ANKRD13B]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[C20orf27]] | +0.66 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP11]] | -0.64 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.63 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[NBR1]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SIX5]] | -0.62 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[RC3H2]] | -0.62 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[DECR1]] | -0.62 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.61 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PAN2]] | -0.60 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[THAP9]] | -0.60 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[FBXO8]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[EP300]] | -0.59 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[SMIM14]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises GARNL3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without GNAZ | 0.007 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises GARNL3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.03× lower at baseline in the lines without FAM78B | 0.008 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[ABCA3]] | B | ABCA3 activity raises GARNL3's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without ABCA3 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[BRSK2]] | B | BRSK2 activity raises GARNL3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without BRSK2 | 0.034 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[NCS1]] | B | NCS1 activity raises GARNL3's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 3.07× lower at baseline in the lines without NCS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[NT5M]] | B | NT5M activity raises GARNL3's level | lines that do not express NT5M (7) vs lines expressing it (43) | 3.15× lower at baseline in the lines without NT5M | 0.059 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[MCOLN2]] | B | MCOLN2 activity raises GARNL3's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without MCOLN2 | 0.069 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[MTCL1]] | C | MTCL1's natural level strengthens GARNL3's drug response | MTCL1's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.18; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 0, C 20. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FXN]] | C | GARNL3 activity raises FXN's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.39× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[RNF130]] | C | GARNL3 activity raises RNF130's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[RNF216]] | C | GARNL3 activity raises RNF216's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[NCLN]] | C | GARNL3 activity raises NCLN's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[ANKS6]] | C | GARNL3 activity raises ANKS6's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[EXOC6B]] | C | GARNL3 activity raises EXOC6B's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[SERGEF]] | C | GARNL3 activity raises SERGEF's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[RRP1B]] | C | GARNL3 activity raises RRP1B's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[TOP1MT]] | C | GARNL3 activity raises TOP1MT's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without GARNL3 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |
| [[WRN]] | C | GARNL3 activity raises WRN's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without GARNL3 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |
| [[GEMIN5]] | C | GARNL3 activity raises GEMIN5's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.10× lower at baseline in the lines without GARNL3 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |
| [[VKORC1L1]] | C | GARNL3 activity raises VKORC1L1's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without GARNL3 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.9, -39.3); signed map (-10.1, -54.8). **Vector** length 112, 31.7% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +9.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +6.4 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.2 | +17.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +14.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +16.0 |
|  | [[EX229 (drug)]] 5 µM |  | +5.1 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -26.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.3 | -31.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -14.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | GTPase activating Rap/RanGAP domain like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:127,224,265-127,393,660 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761J1523, bA356B19.1 |
| Matched by | ensembl_id |

UniProt [Q5VVW2](https://www.uniprot.org/uniprotkb/Q5VVW2) carries no function annotation.

**Summary**, from NCBI Gene [84253](https://www.ncbi.nlm.nih.gov/gene/84253):

> Predicted to enable GTPase activator activity. Predicted to be involved in regulation of small GTPase mediated signal transduction. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25425) · Entrez [84253](https://www.ncbi.nlm.nih.gov/gene/84253) · UniProt [Q5VVW2](https://www.uniprot.org/uniprotkb/Q5VVW2) · Ensembl [ENSG00000136895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136895)

## Data

Gene col 5934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5934); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5934]; `tensor/DDL_lfc|DDL_z.npy` [5934]; `embed/gene_vectors.npy` [5934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5934 or target_col == 5934). Every well: [[GARNL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GARNL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
