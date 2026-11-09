---
symbol: "RTTN"
type: "gene"
col: 10699
ensembl_id: "ENSG00000176225"
name: "rotatin"
location: "18q22.2"
module: 6
arm: "+"
pooled_cpm: 79.16
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RTTN

*rotatin* — 18q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.77× (z +17.9, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.47× (z +6.8, q 1e-09, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.409× (z -15.1, q 0e+00, down in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.588× (z -13.3, q 6e-38, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLM]] (+0.81, fdr 7e-06), [[FANCB]] (+0.78, fdr 7e-06), [[PRIM2]] (+0.77, fdr 7e-06); moves opposite to [[THAP2]] (-0.66, fdr 6e-05), [[N4BP2L1]] (-0.62, fdr 1e-04), [[ATE1OSP]] (-0.61, fdr 8e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.77×** | +17.9 | 0e+00 | 48/48 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.53×** | +16.4 | 0e+00 | 46/48 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.28×** | +14.5 | 3e-45 | 46/48 (J82, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +6.8 | 1e-09 | 34/48 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +5.3 | 2e-05 | 31/48 (HT-29, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.9 | 1e-04 | 30/48 (SK-MEL-2, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.034 | 20/48 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.063 | 14/48 (J82, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.16 | 12/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -15.1 | 0e+00 | 35/43 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -13.7 | 2e-40 | 43/49 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.588×** | -13.3 | 6e-38 | 38/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.512×** | -10.9 | 1e-25 | 34/45 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -7.7 | 1e-12 | 29/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.650×** | -7.6 | 3e-12 | 31/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -6.1 | 9e-08 | 30/48 (MIA PaCa-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -6.0 | 2e-07 | 27/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.756×** | -4.9 | 5e-05 | 27/48 (NCI-H460, Hs 766T, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.8 | 9e-05 | 24/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | **0.763×** | -4.8 | 9e-05 | 26/48 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.8 | 0.008 | 21/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.869× | -3.5 | 0.018 | 19/48 (A-172, NCI-H460, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.876× | -3.3 | 0.037 | 19/49 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.832×** | -3.3 | 0.041 | 21/48 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.05 µM |  | **0.831×** | -3.0 | 0.087 | 17/48 (COLO 205, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.838× | -3.0 | 0.087 | 16/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.729×** | -2.9 | 0.094 | 13/48 (MIA PaCa-2, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | 0.843× | -2.9 | 0.094 | 12/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.849× | -2.9 | 0.094 | 11/48 (RKO, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 311 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -18.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.8) |
| [[LoVo (line)]] | wt | 81.5 | 5 (4 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.05× (z +14.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 122 | 3 (3 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +10.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.414× (z -16.9) |
| [[NCI-H2347 (line)]] | alt | 63.9 | 3 (3 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +10.9) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.309× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 93.7 | 3 (3 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +10.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -10.1) |
| [[J82 (line)]] | alt | 94.2 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.33× (z +14.0) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 113 | 2 (2 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.0904× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 111 | 2 (2 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +10.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 86.8 | 1 (1 ⚠) | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 76.9 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -28.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.16× (z +12.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.8) |
| [[H4 (line)]] | wt | 81.9 | 2 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 4.29× (z +10.0) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.7) |
| [[RKO (line)]] | wt | 60.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +11.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.5) | — |
| [[SW48 (line)]] | wt | 95.6 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +10.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Bortezomib (drug)]] 5 µM 0.0680× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 57.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +10.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 62.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 49.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.8) |
| [[C32 (line)]] | wt | 44.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.29× (z +14.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HCT15 (line)]] | alt | 83.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +10.0) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.482× (z -8.8) |
| [[Hs 766T (line)]] | wt | 80.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.7) |
| [[HS-578T (line)]] | alt | 44.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +12.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.85× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 100 | 1 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.69× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 35.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.33× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 79.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.8) |
| [[SW480 (line)]] | alt | 55.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.403× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 77.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 68.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.4) |
| [[HOP62 (line)]] | alt | 29.7 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.8) |
| [[HT-29 (line)]] | alt | 35.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 45.2 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.93× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.7) |
| [[SW1417 (line)]] | alt | 96.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -15.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 80.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.6) |
| [[AN3 CA (line)]] | alt | 91.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.7) |
| [[C-33 A (line)]] | alt | 89.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +10.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 50.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.9) |
| [[KATO III (line)]] | alt | 93.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 163 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.0) |
| [[PANC-1 (line)]] | alt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 48.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.14× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW 1271 (line)]] | alt | 93.0 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.101× (z -8.8) |
| [[A-172 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLM]] | +0.81 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[FANCB]] | +0.78 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[PRIM2]] | +0.77 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[CCDC150]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.76 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 | same gene group |
| [[DSCC1]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[DTL]] | +0.74 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[RBL1]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SPC24]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[GINS2]] | +0.74 | +0.66 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.66 | -0.67 / -0.39 | both halves | 6e-05 |  |
| [[N4BP2L1]] | -0.62 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[ATE1OSP]] | -0.61 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[LGALSL-DT]] | -0.61 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | -0.61 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[ATF5]] | -0.60 | -0.62 / -0.24 | both halves | 5e-04 |  |
| [[LHFPL3]] | -0.59 | -0.64 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RTTN's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MIR924HG]] | B | MIR924HG activity lowers RTTN's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.61× higher at baseline in the lines without MIR924HG | 0.086 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.5, -46.4); signed map (-38.1, -40.3). **Vector** length 124, 38.8% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.50 to 65); *DNA strand elongation* (reactome, mean cos +0.55 to 28); *DNA Replication* (reactome, mean cos +0.55 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.6 | +17.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.6 | +14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.2 | +16.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +6.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.7 | +5.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.0 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +1.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.3 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.1 | -13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -8.7 | -7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -7.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | rotatin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.2 — chr18:70,003,031-70,205,726 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434G145 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VV8](https://www.uniprot.org/uniprotkb/Q86VV8) (Rotatin):

> Involved in the genetic cascade that governs left-right specification. Plays a role in the maintenance of a normal ciliary structure. Required for correct asymmetric expression of NODAL, LEFTY and PITX2.

**Summary**, from NCBI Gene [25914](https://www.ncbi.nlm.nih.gov/gene/25914):

> This gene encodes a large protein whose specific function is unknown. Absence of the orthologous protein in mouse results in embryonic lethality with deficient axial rotation, abnormal differentiation of the neural tube, and randomized looping of the heart tube during development. In human, mutations in this gene are associated with polymicrogyria with seizures. In human fibroblasts this protein localizes at the ciliary basal bodies. Given the intracellular localization of this protein and the …

**Accessions** — [HGNC:18654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18654) · Entrez [25914](https://www.ncbi.nlm.nih.gov/gene/25914) · UniProt [Q86VV8](https://www.uniprot.org/uniprotkb/Q86VV8) · Ensembl [ENSG00000176225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176225)

## Data

Gene col 10699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10699); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10699]; `tensor/DDL_lfc|DDL_z.npy` [10699]; `embed/gene_vectors.npy` [10699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10699 or target_col == 10699). Every well: [[RTTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
