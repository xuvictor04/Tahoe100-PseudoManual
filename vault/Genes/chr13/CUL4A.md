---
symbol: "CUL4A"
type: "gene"
col: 6350
ensembl_id: "ENSG00000139842"
name: "cullin 4A"
location: "13q34"
module: 5
arm: "+"
pooled_cpm: 149.19
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CUL4A

*cullin 4A* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.70× (z +14.6, q 1e-45, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.459× (z -21.5, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.465× (z -21.1, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC14L1]] (+0.60, fdr 3e-05), [[TRMT1]] (+0.60, fdr 1e-05), [[THAP4]] (+0.60, fdr 1e-05); moves opposite to [[LCA5]] (-0.57, fdr 2e-05), [[MIER1]] (-0.56, fdr 5e-05), [[PSME2]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +14.6 | 1e-45 | 44/48 (PANC-1, Panc 03.27, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +5.2 | 5e-05 | 29/48 (Hs 766T, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.19× | +4.5 | 0.001 | 18/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.9 | 0.012 | 20/44 (LoVo, C-33 A, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.16× | +3.8 | 0.012 | 18/47 (RPMI-7951, NCI-H2030, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.8 | 0.012 | 0/50 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.044 | 22/49 (C-33 A, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.11 | 12/47 (SW 900, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.11 | 9/48 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.14 | 2/49 (LoVo, CFPAC-1) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.459×** | -21.5 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.465×** | -21.1 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.552×** | -16.4 | 0e+00 | 45/48 (SW480, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.558×** | -15.5 | 0e+00 | 43/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.674×** | -15.4 | 0e+00 | 39/48 (LOX-IMVI, C32, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.761×** | -10.7 | 1e-24 | 34/48 (SW480, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.782×** | -9.6 | 8e-20 | 30/49 (NCI-H460, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -9.4 | 4e-19 | 34/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.725×** | -8.9 | 5e-17 | 38/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.730×** | -8.7 | 2e-16 | 37/48 (HOP62, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.766×** | -7.3 | 1e-11 | 32/49 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.770×** | -6.9 | 2e-10 | 28/50 (C32, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.790×** | -6.2 | 2e-08 | 28/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.810×** | -5.8 | 3e-07 | 24/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.833×** | -5.1 | 2e-05 | 24/48 (KATO III, SW480, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.730×** | -4.5 | 2e-04 | 27/49 (SW1417, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.871× | -3.8 | 0.005 | 14/48 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.913× | -3.6 | 0.010 | 5/48 (J82, HOP62, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 5 µM |  | 0.857× | -3.1 | 0.040 | 13/48 (NCI-H460, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.051 | 11/48 (CHP-212, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.888× | -3.0 | 0.058 | 13/47 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 171 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -22.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -13.8) |
| [[SW480 (line)]] | alt | 239 | 1 | 8 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.84× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.355× (z -18.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.372× (z -17.9) |
| [[A-172 (line)]] | wt | 223 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 136 | 1 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.15× (z +11.3) | [[Harringtonine (drug)]] 5 µM 0.339× (z -15.3) |
| [[A-427 (line)]] | wt | 146 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.01× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.409× (z -12.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.462× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 146 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.457× (z -13.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.465× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 165 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -22.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.374× (z -14.7) |
| [[RKO (line)]] | wt | 151 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.415× (z -11.2) |
| [[HOP62 (line)]] | alt | 142 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -20.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -16.0) |
| [[HS-578T (line)]] | alt | 85.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -18.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.372× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 165 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -14.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 181 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.463× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 279 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -18.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.272× (z -18.0) |
| [[SW1417 (line)]] | alt | 90.8 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.98× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.367× (z -13.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -11.9) |
| [[BT-474 (line)]] | alt | 169 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -15.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -12.9) |
| [[HT-29 (line)]] | alt | 168 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.98× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.490× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.625× (z -9.9) |
| [[LoVo (line)]] | wt | 122 | 2 (1 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.96× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -11.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.504× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 144 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.16× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.434× (z -11.8) |
| [[PANC-1 (line)]] | alt | 117 | 2 (1 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.94× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.484× (z -14.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.501× (z -14.2) |
| [[A549 (line)]] | wt | 123 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -12.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -11.9) |
| [[Hs 766T (line)]] | wt | 176 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -11.9) |
| [[J82 (line)]] | alt | 214 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.403× (z -14.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.436× (z -12.8) |
| [[KATO III (line)]] | alt | 140 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.461× (z -11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.519× (z -9.7) |
| [[SNU-423 (line)]] | alt | 104 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.12× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -9.8) |
| [[A498 (line)]] | wt | 132 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.462× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 116 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.394× (z -12.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.465× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.415× (z -10.3) |
| [[LS 180 (line)]] | wt | 178 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.473× (z -11.2) |
| [[SW 900 (line)]] | alt | 91.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -11.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.397× (z -10.4) |
| [[C-33 A (line)]] | alt | 99.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.57× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.435× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 71.7 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.04× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.519× (z -9.4) |
| [[SW48 (line)]] | wt | 153 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -10.7) |
| [[H4 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.619× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 321 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.54× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 143 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.05× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 1088 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC14L1]] | +0.60 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[TRMT1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[THAP4]] | +0.60 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ERICH1]] | +0.58 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[SMG1P6]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MORC2]] | +0.57 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[BRD9]] | +0.57 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[RBM19]] | +0.57 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[HSF1]] | +0.56 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[POMT2]] | +0.56 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[MCM3AP]] | +0.55 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[DHX34]] | +0.55 | +0.30 / +0.57 | both halves | 2e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCA5]] | -0.57 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[MIER1]] | -0.56 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[PSME2]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 | same gene group |
| [[RNF114]] | -0.53 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[COMMD3]] | -0.51 | -0.47 / -0.58 | both halves | 2e-05 | pathway: Neddylation; STRING 510 |
| [[SVIP]] | -0.51 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[MIEN1]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[TMEM205]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SLC50A1]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[IFI27L2]] | -0.51 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[RAB30]] | -0.50 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[C15orf48]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CUL4A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.3, -31.5); signed map (-0.4, -52.5). **Vector** length 108, 31.5% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.5 | +14.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.3 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.0 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -3.2 | -8.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cullin 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,208,193-113,267,108 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cullins; MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 16 pathways, smallest: Recognition of DNA damage by PCNA-containing replication complex; DNA Damage Recognition in GG-NER; Dual Incision in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13619](https://www.uniprot.org/uniprotkb/Q13619) (Cullin-4A):

> Core component of multiple cullin-RING-based E3 ubiquitin-protein ligase complexes which mediate the ubiquitination of target proteins. As a scaffold protein may contribute to catalysis through positioning of the substrate and the ubiquitin-conjugating enzyme. The E3 ubiquitin-protein ligase activity of the complex is dependent on the neddylation of the cullin subunit and is inhibited by the association of the deneddylated cullin subunit with TIP120A/CAND1. The functional specificity of the E3 …

**Summary**, from NCBI Gene [8451](https://www.ncbi.nlm.nih.gov/gene/8451):

> CUL4A is the ubiquitin ligase component of a multimeric complex involved in the degradation of DNA damage-response proteins (Liu et al., 2009 [PubMed 19481525]).[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:2554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2554) · Entrez [8451](https://www.ncbi.nlm.nih.gov/gene/8451) · UniProt [Q13619](https://www.uniprot.org/uniprotkb/Q13619) · Ensembl [ENSG00000139842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139842)

## Data

Gene col 6350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6350); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6350]; `tensor/DDL_lfc|DDL_z.npy` [6350]; `embed/gene_vectors.npy` [6350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6350 or target_col == 6350). Every well: [[CUL4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUL4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
