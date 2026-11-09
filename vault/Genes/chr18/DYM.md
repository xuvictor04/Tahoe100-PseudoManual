---
symbol: "DYM"
type: "gene"
col: 6557
ensembl_id: "ENSG00000141627"
name: "dymeclin"
location: "18q21.1"
module: 40
arm: "+"
pooled_cpm: 164.72
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# DYM

*dymeclin* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.20× (z +4.2, q 0.014, up in 24 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 1.51× (z +4.0, q 0.020, up in 25 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2030 1.87×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.485× (z -21.4, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.377× (z -21.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG5]] (+0.73, fdr 7e-06), [[ZCCHC7]] (+0.69, fdr 7e-06), [[ANO10]] (+0.68, fdr 1e-05); moves opposite to [[PNRC2]] (-0.64, fdr 9e-06), [[SP2]] (-0.61, fdr 2e-05), [[EP300]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6557.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2030 1.87×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +4.2 | 0.014 | 24/48 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.020 | 25/49 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.37× | +3.0 | 0.42 | 16/49 (NCI-H460, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6557.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.485×** | -21.4 | 0e+00 | 46/48 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.377×** | -21.4 | 0e+00 | 47/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.403×** | -20.7 | 0e+00 | 47/49 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.423×** | -18.8 | 0e+00 | 47/47 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.444×** | -17.8 | 0e+00 | 40/44 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.467×** | -16.0 | 0e+00 | 41/45 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -13.5 | 9e-40 | 42/49 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.580×** | -12.4 | 2e-33 | 45/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.631×** | -10.5 | 7e-24 | 38/48 (LS 180, SW48, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.359×** | -9.9 | 2e-21 | 47/49 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -9.9 | 2e-21 | 42/48 (SW48, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.651×** | -9.8 | 7e-21 | 44/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **0.653×** | -9.7 | 1e-20 | 42/48 (SW 1088, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.675×** | -8.9 | 2e-17 | 40/48 (LS 180, KATO III, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -7.1 | 6e-11 | 39/48 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.807×** | -5.9 | 1e-07 | 27/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.756×** | -5.9 | 1e-07 | 35/47 (C32, AN3 CA, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -5.2 | 6e-06 | 27/48 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.850× | -3.4 | 0.014 | 19/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.861× | -3.4 | 0.014 | 11/49 (SNU-423, BT-474, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.865× | -3.1 | 0.047 | 12/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.734×** | -3.0 | 0.056 | 21/48 (CHP-212, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.062 | 16/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 234 | 0 | 14 (7 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.251× (z -20.4) |
| [[HEC-1-A (line)]] | alt | 188 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -19.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.318× (z -17.4) |
| [[KATO III (line)]] | alt | 197 | 0 | 14 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.406× (z -13.6) |
| [[LS 180 (line)]] | wt | 195 | 0 | 13 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -21.9) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.254× (z -17.3) |
| [[HS-578T (line)]] | alt | 242 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -23.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.234× (z -20.9) |
| [[NCI-H460 (line)]] | wt | 174 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.286× (z -18.6) |
| [[SNU-1 (line)]] | wt | 253 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.209× (z -17.4) |
| [[A549 (line)]] | wt | 135 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -23.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.234× (z -19.7) |
| [[hTERT-HPNE (line)]] | wt | 180 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.248× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 199 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.318× (z -15.5) |
| [[PANC-1 (line)]] | alt | 119 | 0 | 10 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -20.3) |
| [[SW480 (line)]] | alt | 104 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.388× (z -15.2) |
| [[A498 (line)]] | wt | 147 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.191× (z -24.0) |
| [[LoVo (line)]] | wt | 240 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.393× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 264 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.333× (z -15.2) |
| [[SNU-423 (line)]] | alt | 178 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -18.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -17.7) |
| [[SW48 (line)]] | wt | 216 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -15.6) |
| [[A-172 (line)]] | wt | 108 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -18.6) |
| [[HT-29 (line)]] | alt | 114 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -13.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.414× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 231 | 1 (1 ⚠) | 7 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.87× (z +8.8) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.323× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.449× (z -10.9) |
| [[A-427 (line)]] | wt | 141 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.370× (z -14.1) |
| [[J82 (line)]] | alt | 165 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 315 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.357× (z -15.5) |
| [[RKO (line)]] | wt | 164 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.303× (z -14.4) |
| [[HOP62 (line)]] | alt | 94.8 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.211× (z -19.4) |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.361× (z -13.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.431× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -19.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.346× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 185 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -34.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.323× (z -13.8) |
| [[H4 (line)]] | wt | 237 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.422× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 201 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.394× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 138 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.438× (z -11.0) |
| [[SW1417 (line)]] | alt | 147 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.279× (z -16.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.385× (z -12.4) |
| [[HCT15 (line)]] | alt | 270 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.375× (z -10.4) |
| [[Hs 766T (line)]] | wt | 148 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.454× (z -9.4) |
| [[C-33 A (line)]] | alt | 256 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 91.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -22.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.366× (z -12.7) |
| [[CHP-212 (line)]] | wt | 217 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[AZD-7648 (drug)]] 5 µM 0.0702× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.443× (z -10.7) |
| [[SW 900 (line)]] | alt | 77.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.378× (z -9.6) |
| [[AN3 CA (line)]] | alt | 213 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.335× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 65.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.386× (z -10.3) |
| [[BT-474 (line)]] | alt | 170 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -17.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.369× (z -12.2) |
| [[COLO 205 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -11.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.386× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.417× (z -9.4) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0418× (z -16.0) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG5]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[ZCCHC7]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ANO10]] | +0.68 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[NBAS]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[WRN]] | +0.63 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[GARNL3]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SGTB]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[URI1]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[SND1]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 | same gene group |
| [[TMEM120B]] | +0.60 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[DUXAP10]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[RACK1]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | -0.64 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[SP2]] | -0.61 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[EP300]] | -0.61 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.57 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[DEDD]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.56 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[MED12]] | -0.55 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[SKIL]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ZNF436]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[DDX6]] | -0.54 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[POGZ]] | -0.54 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.54 | -0.60 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DYM's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLRC4-KLRK1]] | B | KLRC4-KLRK1 activity weakens DYM's drug response | lines that do not express KLRC4-KLRK1 (29) vs lines expressing it (20) | the lines without KLRC4-KLRK1 respond 1.32× as strongly (z diff -1.19); strongest at Idarubicin (hydrochloride) 5 µM: 0.59x vs 0.73x (z diff -2.1) | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B; target measured in part of the lines; artifact flags |
| [[ANK2]] | B | ANK2 activity raises DYM's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.39× lower at baseline in the lines without ANK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.5, -21.0); signed map (-44.7, 6.8). **Vector** length 113, 41.8% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.1 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.9 | +1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +0.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.3 | -18.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -21.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.0 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | dymeclin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:49,036,387-49,461,347 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20071, DMC, SMC |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7RTS9](https://www.uniprot.org/uniprotkb/Q7RTS9) (Dymeclin):

> Necessary for correct organization of Golgi apparatus. Involved in bone development.

**Summary**, from NCBI Gene [54808](https://www.ncbi.nlm.nih.gov/gene/54808):

> This gene encodes a protein which regulates Golgi-associated secretory pathways that are essential to endochondral bone formation during early development. This gene is also believed to play a role in early brain development. This gene is widely expressed in embryos and is particularly abundant in chodrocytes and brain tissues. It encodes a peripheral membrane protein which shuttles between the cytosol and Golgi complex. Mutations in this gene are associated with two types of recessive …

**Accessions** — [HGNC:21317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21317) · Entrez [54808](https://www.ncbi.nlm.nih.gov/gene/54808) · UniProt [Q7RTS9](https://www.uniprot.org/uniprotkb/Q7RTS9) · Ensembl [ENSG00000141627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141627)

## Data

Gene col 6557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6557); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6557]; `tensor/DDL_lfc|DDL_z.npy` [6557]; `embed/gene_vectors.npy` [6557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6557 or target_col == 6557). Every well: [[DYM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
