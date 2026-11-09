---
symbol: "NEAT1"
type: "gene"
col: 14430
ensembl_id: "ENSG00000245532"
name: "nuclear paraspeckle assembly transcript 1"
location: "11q13.1"
module: 16
arm: "-"
pooled_cpm: 5315.93
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 36
n_dd_up_clean: 22
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# NEAT1

*nuclear paraspeckle assembly transcript 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.01× (z +12.9, q 3e-35, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.274× (z -18.5, q 0e+00, down in 46 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.505× (z -17.8, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALAT1]] (+0.67, fdr 7e-06), [[TALAM1]] (+0.66, fdr 7e-06), [[FTL]] (+0.63, fdr 7e-06); moves opposite to [[DDX20]] (-0.60, fdr 1e-05), [[POGLUT1]] (-0.58, fdr 3e-05), [[SENP1]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.01×** | +12.9 | 3e-35 | 41/47 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.99×** | +12.7 | 2e-34 | 46/47 (HEC-1-A, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +11.1 | 2e-26 | 43/47 (HS-578T, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +10.6 | 3e-24 | 39/47 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.82×** | +10.4 | 3e-23 | 43/47 (HEC-1-A, A498, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +9.9 | 6e-21 | 43/47 (HEC-1-A, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +9.6 | 6e-20 | 38/47 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.61×** | +8.8 | 1e-16 | 42/46 (RKO, NCI-H23, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.69×** | +7.4 | 6e-12 | 42/46 (NCI-H23, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.49×** | +7.3 | 1e-11 | 42/48 (RKO, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +7.0 | 2e-10 | 42/48 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.8 | 4e-10 | 34/47 (HEC-1-A, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.29×** | +6.6 | 2e-09 | 30/47 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.41×** | +6.4 | 9e-09 | 40/47 (A498, H4, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.86×** | +6.0 | 8e-08 | 45/47 (HS-578T, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 8e-06 | 35/48 (HEC-1-A, A498, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 1e-04 | 26/47 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +4.3 | 4e-04 | 18/47 (NCI-H23, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14430.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.274×** | -18.5 | 0e+00 | 46/46 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.503×** | -17.9 | 0e+00 | 35/47 (SHP-77, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.505×** | -17.8 | 0e+00 | 44/48 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.397×** | -17.0 | 0e+00 | 43/47 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.493×** | -13.0 | 9e-37 | 47/47 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.525×** | -11.8 | 2e-30 | 41/48 (hTERT-HPNE, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.531×** | -10.8 | 4e-25 | 38/44 (hTERT-HPNE, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.470×** | -10.7 | 4e-25 | 38/43 (hTERT-HPNE, A-172, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.479×** | -10.5 | 6e-24 | 40/47 (LOX-IMVI, BT-474, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.408×** | -8.6 | 3e-16 | 35/37 (hTERT-HPNE, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -8.4 | 3e-15 | 35/47 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.448×** | -7.7 | 5e-13 | 43/48 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -7.3 | 1e-11 | 41/47 (SK-MEL-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -7.3 | 2e-11 | 29/47 (A-172, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **0.714×** | -6.2 | 2e-08 | 40/47 (HT-29, SW 900, …) | all doses, flat | low cells (technical?); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.578×** | -5.3 | 5e-06 | 39/47 (NCI-H1792, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.762×** | -5.0 | 2e-05 | 29/47 (SW 900, A-427, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.828×** | -4.9 | 3e-05 | 28/47 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.603×** | -4.9 | 3e-05 | 39/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.769×** | -4.8 | 4e-05 | 31/47 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.832×** | -4.8 | 4e-05 | 20/47 (NCI-H1792, J82, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.626×** | -4.5 | 2e-04 | 35/47 (NCI-H1792, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.798×** | -3.9 | 0.002 | 27/46 (HEC-1-A, BT-474, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.865× | -3.8 | 0.003 | 18/48 (HepG2/C3A, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 7,735 | 10 (1 ⚠) | 11 (7 ⚠) | [[Auranofin (drug)]] 5 µM 3.43× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -18.9) |
| [[HOP62 (line)]] | alt | 8,691 | 6 | 13 (8 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.79× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -16.1) |
| [[A498 (line)]] | wt | 3,290 | 12 (3 ⚠) | 6 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.14× (z +20.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -14.9) |
| [[CFPAC-1 (line)]] | alt | 4,474 | 6 | 11 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.71× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -27.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -24.4) |
| [[HT-29 (line)]] | alt | 8,069 | 2 | 15 (10 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.56× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -33.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -29.7) |
| [[HEC-1-A (line)]] | alt | 2,333 | 14 (3 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.19× (z +23.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 4,012 | 7 (1 ⚠) | 8 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +15.5) | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -14.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 5,203 | 5 | 10 (6 ⚠) | [[Auranofin (drug)]] 5 µM 2.34× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -25.8) |
| [[NCI-H1792 (line)]] | alt | 7,934 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -28.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -27.5) |
| [[H4 (line)]] | wt | 4,499 | 9 (3 ⚠) | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.14× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -18.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -12.9) |
| [[SW 900 (line)]] | alt | 7,958 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -29.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -22.4) |
| [[HCT15 (line)]] | alt | 6,382 | 4 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -31.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -20.5) |
| [[hTERT-HPNE (line)]] | wt | 10,389 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -19.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -17.2) |
| [[SNU-423 (line)]] | alt | 9,114 | 1 | 11 (8 ⚠) | [[Auranofin (drug)]] 5 µM 2.01× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -27.6) |
| [[SW480 (line)]] | alt | 4,464 | 6 (1 ⚠) | 6 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.87× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.1) |
| [[A-172 (line)]] | wt | 5,722 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -20.1) |
| [[LOX-IMVI (line)]] | wt | 6,504 | 1 (1 ⚠) | 10 (7 ⚠) | [[Selinexor (drug)]] 5 µM 1.87× (z +9.9) ⚠ cell-cycle shift, explains ~89% of this change | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -20.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -15.1) |
| [[SHP-77 (line)]] | alt | 5,066 | 5 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.43× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -35.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -20.5) |
| [[C-33 A (line)]] | alt | 2,899 | 5 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.13× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -10.7) |
| [[CHP-212 (line)]] | wt | 7,263 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -21.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -19.9) |
| [[J82 (line)]] | alt | 11,310 | 3 (1 ⚠) | 7 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.26× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.12× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -20.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.315× (z -17.7) |
| [[KATO III (line)]] | alt | 3,450 | 5 (1 ⚠) | 5 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.66× (z +16.8) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -11.2) |
| [[PANC-1 (line)]] | alt | 4,984 | 3 (1 ⚠) | 7 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.261× (z -13.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 3,302 | 3 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.60× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -18.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.304× (z -13.4) |
| [[SNU-1 (line)]] | wt | 6,110 | 3 (2 ⚠) | 7 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.00× (z +11.7) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.17× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -17.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -13.6) |
| [[BT-474 (line)]] | alt | 11,484 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -30.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -17.1) |
| [[SW48 (line)]] | wt | 11,156 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -12.0) |
| [[COLO 205 (line)]] | alt | 6,130 | 7 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.06× (z +12.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.221× (z -13.3) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 6,582 | 2 | 6 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.30× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -16.5) |
| [[A-427 (line)]] | wt | 2,538 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -20.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 2,137 | 6 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.48× (z +16.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -10.2) ⚠ toxic |
| [[RKO (line)]] | wt | 2,500 | 6 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 1.95× (z +12.7) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.40× (z +11.8) | [[Radotinib (drug)]] 5 µM 0.620× (z -9.0) |
| [[SW1417 (line)]] | alt | 4,999 | 4 (2 ⚠) | 3 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.84× (z +10.6) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 6,014 | 1 (1 ⚠) | 5 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.61× (z +10.1) ⚠ cell-cycle shift, explains ~89% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.344× (z -12.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.527× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 8,310 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.221× (z -13.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 4,670 | 2 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -15.7) |
| [[C32 (line)]] | wt | 6,558 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.310× (z -16.4) |
| [[LS 180 (line)]] | wt | 2,392 | 1 (1 ⚠) | 4 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.46× (z +13.4) ⚠ cell-cycle shift, explains ~89% of this change | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 5,239 | 1 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.337× (z -13.8) ⚠ unreliable plate only · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.341× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 3,320 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.98× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.382× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 3,186 | 2 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.09× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -10.0) |
| [[SW 1271 (line)]] | alt | 8,033 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.6) |
| [[A549 (line)]] | wt | 5,268 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -14.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.8) |
| [[NCI-H661 (line)]] | alt | 2,176 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -12.3) |
| [[SW 1088 (line)]] | alt | 5,168 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.1) |
| [[AN3 CA (line)]] | alt | 2,044 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3,427 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1,288 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5,997 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6,539 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALAT1]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 | same gene group |
| [[TALAM1]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 | same gene group |
| [[FTL]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ABAT]] | +0.59 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[BLVRB]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SAMD4B]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MKNK2]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PHF1]] | +0.57 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[CALCOCO2]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[HSPA1B]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ULK1]] | +0.57 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[MED31]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX20]] | -0.60 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.58 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[SENP1]] | -0.58 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[KLHL42]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[DIS3L]] | -0.57 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[SLC12A2-DT]] | -0.57 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[CHAMP1]] | -0.56 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[LATS1]] | -0.56 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[DCLRE1A]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SF3B3]] | -0.55 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[LRRC37A4P]] | -0.54 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[OXCT1]] | -0.54 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NEAT1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.341). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-55.7, -5.1); signed map (-20.8, 22.5). **Vector** length 162, 62.7% of its response variance represented; |z| ≥ 3 in 2,582 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +14.9 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.7 | +12.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +12.6 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +12.1 | +12.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.8 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +9.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +6.8 | +8.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +6.8 | +5.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.8 | -17.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.7 | -17.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.3 | -18.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -11.2 | -13.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -9.4 | -7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -8.1 | -7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.6 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -6.1 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear paraspeckle assembly transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.1 — chr11:65,422,774-65,445,540 (+) |
| Ensembl biotype | lncRNA |
| Also known as | TncRNA, MENepsilon/beta, LINC00084, VINC, TP53LC15; previously NCRNA00084 |
| Gene groups (HGNC) | MicroRNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [283131](https://www.ncbi.nlm.nih.gov/gene/283131):

> This gene produces a long non-coding RNA (lncRNA) transcribed from the multiple endocrine neoplasia locus. This lncRNA is retained in the nucleus where it forms the core structural component of the paraspeckle sub-organelles. It may act as a transcriptional regulator for numerous genes, including some genes involved in cancer progression. [provided by RefSeq, Mar 2015]

**Accessions** — [HGNC:30815](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30815) · Entrez [283131](https://www.ncbi.nlm.nih.gov/gene/283131) · Ensembl [ENSG00000245532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245532)

## Data

Gene col 14430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14430); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14430]; `tensor/DDL_lfc|DDL_z.npy` [14430]; `embed/gene_vectors.npy` [14430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14430 or target_col == 14430). Every well: [[NEAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
