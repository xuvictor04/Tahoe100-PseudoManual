---
symbol: "CIP2A"
type: "gene"
col: 8702
ensembl_id: "ENSG00000163507"
name: "cellular inhibitor of PP2A"
location: "3q13.13"
module: 22
arm: "+"
pooled_cpm: 60.31
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CIP2A

*cellular inhibitor of PP2A* — 3q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +18.3, q 0e+00, up in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.80× (z +7.9, q 3e-13, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.743× (z -6.5, q 4e-08, down in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~99% of this change. The strongest without an alert is [[palbociclib (drug)]] 5 µM: 0.642× (z -3.6, q 0.031, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG]] (+0.82, fdr 7e-06), [[GEN1]] (+0.82, fdr 7e-06), [[SMC4]] (+0.82, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.31×** | +18.3 | 0e+00 | 39/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **2.28×** | +12.7 | 1e-34 | 43/46 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.24×** | +12.0 | 9e-31 | 34/41 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.15×** | +11.3 | 1e-27 | 42/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.88×** | +9.0 | 3e-17 | 35/43 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +7.9 | 3e-13 | 31/47 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.49×** | +6.2 | 5e-08 | 36/47 (C32, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.40×** | +5.0 | 5e-05 | 25/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.25×** | +4.8 | 1e-04 | 25/47 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.4 | 5e-04 | 26/47 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +4.0 | 0.003 | 24/47 (A549, LoVo, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.29×** | +4.0 | 0.003 | 22/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.31×** | +4.0 | 0.003 | 20/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +4.0 | 0.003 | 23/46 (SW 900, NCI-H23, …) | two highest doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.004 | 23/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.005 | 19/47 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.014 | 19/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.021 | 19/47 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.021 | 22/46 (RKO, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.030 | 20/47 (NCI-H23, RPMI-7951, …) | rises with dose | position effect removed |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.063 | 14/47 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; position effect removed |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.070 | 17/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.071 | 13/47 (NCI-H460, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.743×** | -6.5 | 4e-08 | 30/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -4.9 | 3e-04 | 4/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.720×** | -4.4 | 0.002 | 28/47 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.692×** | -4.1 | 0.007 | 22/47 (SW480, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.787×** | -3.7 | 0.023 | 21/47 (HCT15, SNU-1, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.642×** | -3.6 | 0.031 | 23/46 (COLO 205, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.852× | -3.5 | 0.035 | 18/47 (HCT15, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.035 | 23/47 (A-427, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.793×** | -3.5 | 0.035 | 19/47 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.834× | -3.3 | 0.056 | 18/47 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.864× | -3.2 | 0.069 | 15/47 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.790×** | -3.2 | 0.073 | 16/47 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Alpelisib (drug)]] 5 µM |  | 0.686× | -3.0 | 0.10 | 15/46 (RPMI-7951, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 78.7 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | [[Selinexor (drug)]] 5 µM 0.363× (z -12.1) ⚠ cell-cycle shift, explains ~99% of this change |
| [[HS-578T (line)]] | alt | 53.2 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +16.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.54× (z +10.1) | — |
| [[A-427 (line)]] | wt | 171 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.303× (z -17.2) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.471× (z -10.9) |
| [[A498 (line)]] | wt | 70.2 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.2) ⚠ cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.347× (z -13.8) ⚠ cell-cycle shift, explains ~99% of this change |
| [[LoVo (line)]] | wt | 32.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.4) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C32 (line)]] | wt | 30.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +13.3) ⚠ cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.346× (z -10.1) ⚠ cell-cycle shift, explains ~99% of this change |
| [[LOX-IMVI (line)]] | wt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[NCI-H2347 (line)]] | alt | 56.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +17.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 83.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +17.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A549 (line)]] | wt | 53.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +16.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[AsPC-1 (line)]] | alt | 23.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +16.0) ⚠ cell-cycle shift, explains ~44% of this change | [[Docetaxel (drug)]] 0.05 µM 0.242× (z -9.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 30.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.5) ⚠ cell-cycle shift, explains ~44% of this change | [[AZD2858 (drug)]] 0.5 µM 0.168× (z -8.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1573 (line)]] | alt | 35.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.5) ⚠ cell-cycle shift, explains ~44% of this change | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[NCI-H460 (line)]] | wt | 36.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.6) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[Panc 03.27 (line)]] | alt | 52.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +15.3) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW 900 (line)]] | alt | 40.9 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.18× (z +10.1) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[AN3 CA (line)]] | alt | 94.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -16.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[CFPAC-1 (line)]] | alt | 38.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[H4 (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.311× (z -8.7) ⚠ cell-cycle shift, explains ~99% of this change |
| [[Hs 766T (line)]] | wt | 33.7 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0750× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.1) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[J82 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[LS 180 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.261× (z -11.5) ⚠ cell-cycle shift, explains ~99% of this change |
| [[MIA PaCa-2 (line)]] | alt | 69.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[NCI-H2030 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.3) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[RKO (line)]] | wt | 92.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.0) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[RPMI-7951 (line)]] | alt | 55.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 83.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[SNU-1 (line)]] | wt | 60.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.306× (z -9.6) ⚠ cell-cycle shift, explains ~99% of this change |
| [[SNU-423 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +15.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW1417 (line)]] | alt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C-33 A (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 60.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG]] | +0.82 | +0.82 / +0.83 | both halves | 7e-06 | same gene group; STRING 586 |
| [[GEN1]] | +0.82 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[SMC4]] | +0.82 | +0.85 / +0.82 | both halves | 7e-06 | STRING 570 |
| [[BRCA2]] | +0.81 | +0.84 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SGO1]] | +0.81 | +0.81 / +0.82 | both halves | 7e-06 | STRING 516 |
| [[KIF15]] | +0.79 | +0.78 / +0.80 | both halves | 7e-06 | STRING 564 |
| [[C18orf54]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CENPH]] | +0.78 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[ZWILCH]] | +0.78 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ESCO2]] | +0.78 | +0.81 / +0.76 | both halves | 7e-06 | STRING 453 |
| [[SKA3]] | +0.78 | +0.73 / +0.83 | both halves | 7e-06 | STRING 442 |
| [[DIAPH3]] | +0.78 | +0.76 / +0.82 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity raises CIP2A's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers CIP2A's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[E2F8]] | C | E2F8's natural level weakens CIP2A's drug response | E2F8's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.71, reverse +0.29; direction not clear | 0.032 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NDC80]] | C | NDC80 activity raises CIP2A's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without NDC80 | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.7, -48.3); signed map (-44.3, -47.4). **Vector** length 139, 48.8% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.56 to 60); *DREAM G2/M down* (control, mean cos +0.60 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.57 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.8 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.7 | +18.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +3.7 | +12.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.4 | +3.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.6 | +2.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.6 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -6.9 | -6.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -2.4 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -3.9 | -4.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -3.1 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -2.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cellular inhibitor of PP2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.13 — chr3:108,549,864-108,589,644 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1524 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCG1](https://www.uniprot.org/uniprotkb/Q8TCG1) (Protein CIP2A):

> Acts as an inhibitor of protein phosphatase PP2A. Promotes anchorage-independent cell growth and tumor formation by preventing dephosphorylation of MYC, thereby stabilizing MYC in human malignancies. Together with TOPBP1, plays an essential role in the response to genome instability generated by the presence of acentric chromosome fragments derived from shattered chromosomes within micronuclei. Micronuclei, which are frequently found in cancer cells, consist of chromatin surrounded by their own …

**Summary**, from NCBI Gene [57650](https://www.ncbi.nlm.nih.gov/gene/57650):

> Enables protein homodimerization activity and protein phosphatase inhibitor activity. Involved in broken chromosome clustering. Located in cytosol. Is active in chromosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29302) · Entrez [57650](https://www.ncbi.nlm.nih.gov/gene/57650) · UniProt [Q8TCG1](https://www.uniprot.org/uniprotkb/Q8TCG1) · Ensembl [ENSG00000163507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163507)

## Data

Gene col 8702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8702); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8702]; `tensor/DDL_lfc|DDL_z.npy` [8702]; `embed/gene_vectors.npy` [8702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8702 or target_col == 8702). Every well: [[CIP2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIP2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
