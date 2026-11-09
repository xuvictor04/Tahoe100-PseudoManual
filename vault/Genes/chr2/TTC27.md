---
symbol: "TTC27"
type: "gene"
col: 309
ensembl_id: "ENSG00000018699"
name: "tetratricopeptide repeat domain 27"
location: "2p22.3"
module: 1
arm: "+"
pooled_cpm: 78.76
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TTC27

*tetratricopeptide repeat domain 27* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.30× (z +25.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.595× (z -15.9, q 0e+00, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP20]] (+0.78, fdr 7e-06), [[INO80]] (+0.76, fdr 7e-06), [[WARS2]] (+0.73, fdr 7e-06); moves opposite to [[UBTD1]] (-0.65, fdr 7e-06), [[PDXP]] (-0.65, fdr 9e-06), [[ARL3]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +25.5 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.08×** | +15.5 | 0e+00 | 44/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +11.7 | 2e-29 | 43/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +10.5 | 2e-23 | 43/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +10.0 | 1e-21 | 39/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +9.3 | 1e-18 | 31/48 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +9.0 | 1e-17 | 36/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +8.6 | 8e-16 | 30/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +8.5 | 1e-15 | 42/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +8.1 | 3e-14 | 39/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +6.9 | 2e-10 | 33/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.44×** | +6.7 | 9e-10 | 34/47 (A-172, A-427, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +6.5 | 3e-09 | 32/48 (HOP62, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 7e-05 | 23/48 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.24×** | +4.7 | 1e-04 | 22/48 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.018 | 19/49 (HOP62, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.034 | 13/48 (AsPC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -15.9 | 0e+00 | 39/49 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.501×** | -14.7 | 0e+00 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.554×** | -12.8 | 4e-35 | 39/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.588×** | -11.5 | 2e-28 | 43/48 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.601×** | -11.0 | 3e-26 | 39/49 (HEC-1-A, SW48, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.597×** | -11.0 | 6e-26 | 37/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.584×** | -10.8 | 3e-25 | 31/45 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.619×** | -10.0 | 1e-21 | 29/44 (HEC-1-A, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.646×** | -9.5 | 2e-19 | 40/48 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -8.1 | 4e-14 | 31/48 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -7.4 | 6e-12 | 32/48 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.8 | 7e-10 | 27/50 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.475×** | -6.7 | 9e-10 | 37/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.735×** | -6.7 | 1e-09 | 31/48 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.749×** | -6.3 | 1e-08 | 29/48 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.802×** | -4.7 | 9e-05 | 24/49 (RKO, SW48, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.830×** | -3.5 | 0.016 | 11/47 (HOP62, hTERT-HPNE, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.897× | -3.3 | 0.025 | 5/48 (RKO, NCI-H23, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.856× | -3.3 | 0.025 | 14/48 (NCI-H2030, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 124 | 3 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +21.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -17.7) |
| [[SW480 (line)]] | alt | 97.3 | 2 | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.0) | [[Belinostat (drug)]] 5 µM 0.330× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 97.7 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.344× (z -13.8) |
| [[HOP62 (line)]] | alt | 71.0 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 87.0 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.395× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 72.4 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 104 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +18.7) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -13.5) |
| [[A549 (line)]] | wt | 121 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -23.6) |
| [[LOX-IMVI (line)]] | wt | 118 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 66.9 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.352× (z -10.6) |
| [[SW48 (line)]] | wt | 87.6 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -13.2) |
| [[A-427 (line)]] | wt | 157 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.470× (z -9.6) |
| [[BT-474 (line)]] | alt | 51.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.32× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 95.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 72.4 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.8) |
| [[LoVo (line)]] | wt | 61.0 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 35.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +17.2) | — |
| [[RKO (line)]] | wt | 110 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -15.9) |
| [[A498 (line)]] | wt | 82.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 44.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +14.4) | — |
| [[CFPAC-1 (line)]] | alt | 64.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 48.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -11.0) |
| [[LS 180 (line)]] | wt | 46.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 76.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 99.0 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 103 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 74.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.21× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 94.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -11.8) |
| [[SW1417 (line)]] | alt | 60.3 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.406× (z -8.9) |
| [[A-172 (line)]] | wt | 33.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 44.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.04× (z +10.7) | — |
| [[H4 (line)]] | wt | 65.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 41.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +14.7) | — |
| [[SK-MEL-2 (line)]] | alt | 84.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.2) |
| [[SNU-423 (line)]] | alt | 64.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.05 µM 0.415× (z -9.3) |
| [[C-33 A (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 76.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 86.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 53.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 51.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 94.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0739× (z -10.7) |
| [[SW 900 (line)]] | alt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | +0.78 | +0.80 / +0.70 | both halves | 7e-06 | STRING 610 |
| [[INO80]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[WARS2]] | +0.73 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PHF14]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[THADA]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 | STRING 458 |
| [[JPX]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.68 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[AFG1L]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[METAP1D]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[FASTKD2]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBTD1]] | -0.65 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[PDXP]] | -0.65 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[ARL3]] | -0.62 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[RAP2A]] | -0.61 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.61 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[APAF1]] | -0.61 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[GTF2IP4]] | -0.60 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ALKBH5]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ABHD12]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PJA2]] | -0.59 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[IDH2]] | -0.59 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[OSTF1]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TTC27's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises TTC27's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.9, 12.9); signed map (6.0, -42.4). **Vector** length 127, 41.6% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +9.8 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +25.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +11.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.7 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +6.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +6.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.9 | -9.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.6 | -11.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.5 | -14.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.4 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -12.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -7.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -2.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:32,628,032-32,821,051 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20272 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q6P3X3](https://www.uniprot.org/uniprotkb/Q6P3X3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25986) · Entrez [55622](https://www.ncbi.nlm.nih.gov/gene/55622) · UniProt [Q6P3X3](https://www.uniprot.org/uniprotkb/Q6P3X3) · Ensembl [ENSG00000018699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000018699)

## Data

Gene col 309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 309); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 309]; `tensor/DDL_lfc|DDL_z.npy` [309]; `embed/gene_vectors.npy` [309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 309 or target_col == 309). Every well: [[TTC27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
