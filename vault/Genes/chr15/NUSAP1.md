---
symbol: "NUSAP1"
type: "gene"
col: 6067
ensembl_id: "ENSG00000137804"
name: "nucleolar and spindle associated protein 1"
location: "15q14"
module: 22
arm: "+"
pooled_cpm: 88.68
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NUSAP1

*nucleolar and spindle associated protein 1* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (24 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.72× (z +20.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.606× (z -10.5, q 4e-23, down in 35 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.774× (z -5.4, q 1e-05, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG]] (+0.92, fdr 7e-06), [[TPX2]] (+0.91, fdr 7e-06), [[CDK1]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 26 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +20.9 | 0e+00 | 46/48 (AsPC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **2.64×** | +20.3 | 0e+00 | 41/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **2.60×** | +14.1 | 8e-43 | 46/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **2.46×** | +12.7 | 4e-35 | 38/44 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **2.21×** | +11.2 | 3e-27 | 42/48 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **2.10×** | +11.0 | 6e-26 | 41/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +10.8 | 4e-25 | 40/48 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **2.02×** | +10.4 | 2e-23 | 42/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.02×** | +10.0 | 1e-21 | 39/48 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.97×** | +9.2 | 2e-18 | 33/45 (A-172, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.87×** | +9.2 | 2e-18 | 39/48 (A549, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.77×** | +8.4 | 3e-15 | 36/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.63×** | +7.2 | 3e-11 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.60×** | +6.9 | 2e-10 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.58×** | +6.8 | 6e-10 | 25/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.2 | 6e-06 | 25/48 (SW1417, HOP62, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.21×** | +2.8 | 0.088 | 20/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +2.8 | 0.099 | 12/48 (PANC-1, A-172, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.606×** | -10.5 | 4e-23 | 35/48 (A498, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.520×** | -9.7 | 1e-19 | 40/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.690×** | -5.5 | 6e-06 | 31/48 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.774×** | -5.4 | 1e-05 | 32/48 (HCT15, RKO, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.732×** | -4.6 | 4e-04 | 28/48 (SW 1088, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.722×** | -4.6 | 4e-04 | 25/48 (A-172, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.564×** | -4.4 | 7e-04 | 27/48 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.776×** | -3.8 | 0.011 | 23/48 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.704×** | -3.7 | 0.012 | 25/48 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.627×** | -3.6 | 0.016 | 23/47 (H4, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~96% of this change | **0.643×** | -3.4 | 0.028 | 20/45 (SW48, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.850× | -3.4 | 0.028 | 16/48 (COLO 205, HT-29, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.028 | 24/48 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.852× | -3.4 | 0.028 | 15/48 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.033 | 19/47 (RKO, LS 180, …) | two highest doses | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.807×** | -3.2 | 0.045 | 13/48 (SNU-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Futibatinib (drug)]] 5 µM |  | **0.678×** | -3.0 | 0.073 | 17/46 (SNU-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.809×** | -3.0 | 0.076 | 18/48 (AN3 CA, A498, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.821×** | -3.0 | 0.081 | 17/48 (Hs 766T, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.92 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 103 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +21.3) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +13.2) | — |
| [[LoVo (line)]] | wt | 77.4 | 8 (7 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +20.5) | [[Selinexor (drug)]] 5 µM 0.486× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 84.1 | 5 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.325× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 127 | 8 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +21.2) | — |
| [[A498 (line)]] | wt | 104 | 4 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +17.7) ⚠ cell-cycle shift, explains ~75% of this change | [[Selinexor (drug)]] 5 µM 0.205× (z -22.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 63.6 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +20.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.2) | — |
| [[C32 (line)]] | wt | 77.4 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +14.0) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 41.0 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +17.3) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.13× (z +16.0) | — |
| [[J82 (line)]] | alt | 154 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +14.9) | — |
| [[KATO III (line)]] | alt | 111 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.19× (z +14.3) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 70.8 | 2 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +10.2) | [[Selinexor (drug)]] 0.5 µM 0.157× (z -12.9) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.275× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 97.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 66.7 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.7) ⚠ cell-cycle shift, explains ~75% of this change | [[Selinexor (drug)]] 5 µM 0.365× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 95.1 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.130× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.195× (z -12.9) |
| [[HS-578T (line)]] | alt | 46.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.3) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 128 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +10.9) | [[Selinexor (drug)]] 5 µM 0.403× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 65.4 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.293× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 59.9 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 103 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +14.9) | — |
| [[SW480 (line)]] | alt | 95.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 49.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 54.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +13.9) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +12.3) | [[Selinexor (drug)]] 5 µM 0.312× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 84.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 38.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 157 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +20.9) ⚠ cell-cycle shift, explains ~75% of this change | [[Selinexor (drug)]] 5 µM 0.519× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 79.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +18.0) | — |
| [[RKO (line)]] | wt | 87.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +15.6) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +15.3) | — |
| [[A-427 (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.306× (z -15.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 22.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.1× (z +21.5) | — |
| [[CFPAC-1 (line)]] | alt | 76.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +14.9) | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +12.4) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 57.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.0) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.3) | — |
| [[RPMI-7951 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +15.2) | — |
| [[SNU-1 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.284× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 86.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +13.9) | — |
| [[CHP-212 (line)]] | wt | 49.8 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0768× (z -9.0) |
| [[HCT15 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.433× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 53.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[NCI-H1573 (line)]] | alt | 45.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.8) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.491× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 96.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 139 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | STRING 931 |
| [[TPX2]] | +0.91 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 964 |
| [[CDK1]] | +0.90 | +0.91 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 946 |
| [[BIRC5]] | +0.90 | +0.92 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 953 |
| [[KIF11]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 974 |
| [[TOP2A]] | +0.89 | +0.90 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[MKI67]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 943 |
| [[KNL1]] | +0.89 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 672 |
| [[PRC1]] | +0.89 | +0.90 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 936 |
| [[KIF18A]] | +0.88 | +0.88 / +0.89 | both halves | 7e-06 | STRING 713 |
| [[NDC80]] | +0.88 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 918 |
| [[NCAPD2]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | STRING 654 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises NUSAP1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.14× lower at baseline in the lines without PIMREG | 0.007 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NUSAP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYBL1]] | B | MYBL1 activity raises NUSAP1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without MYBL1 | 0.092 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises NUSAP1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without AURKB | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises NUSAP1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without PBK | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises NUSAP1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.31× lower at baseline in the lines without NDC80 | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises NUSAP1's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.86× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises NUSAP1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without CDC20 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises NUSAP1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.60× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[ACBD7]] | C | ACBD7 activity raises NUSAP1's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without ACBD7 | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.907). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.0, -54.9); signed map (-48.9, -44.0). **Vector** length 146, 62.2% of its response variance represented; |z| ≥ 3 in 1,600 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.70 to 48); *E2F targets* (hallmark, mean cos +0.72 to 46); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.69 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +5.6 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +20.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +4.7 | +5.7 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +2.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.4 | +1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.2 | +0.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -10.7 | -10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.0 | -3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -8.9 | -9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -7.8 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.4 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -6.1 | -4.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.7 | -3.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.5 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar and spindle associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:41,320,794-41,381,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13421, LNP, ANKT, SAPL, BM037, PRO0310p1, Q0310 |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXS6](https://www.uniprot.org/uniprotkb/Q9BXS6) (Nucleolar and spindle-associated protein 1):

> Microtubule-associated protein with the capacity to bundle and stabilize microtubules (By similarity). May associate with chromosomes and promote the organization of mitotic spindle microtubules around them.

**Summary**, from NCBI Gene [51203](https://www.ncbi.nlm.nih.gov/gene/51203):

> NUSAP1 is a nucleolar-spindle-associated protein that plays a role in spindle microtubule organization (Raemaekers et al., 2003 [PubMed 12963707]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:18538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18538) · Entrez [51203](https://www.ncbi.nlm.nih.gov/gene/51203) · UniProt [Q9BXS6](https://www.uniprot.org/uniprotkb/Q9BXS6) · Ensembl [ENSG00000137804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137804)

## Data

Gene col 6067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6067); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6067]; `tensor/DDL_lfc|DDL_z.npy` [6067]; `embed/gene_vectors.npy` [6067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6067 or target_col == 6067). Every well: [[NUSAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUSAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
