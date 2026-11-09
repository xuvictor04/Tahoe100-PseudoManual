---
symbol: "EPS8L2"
type: "gene"
col: 10792
ensembl_id: "ENSG00000177106"
name: "EPS8 signaling adaptor L2"
location: "11p15.5"
module: 31
arm: "+"
pooled_cpm: 30.26
n_lines_expressing: 31
n_dd_up: 7
n_dd_down: 37
n_dd_up_clean: 3
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 23
direction_downstream: 39
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# EPS8L2

*EPS8 signaling adaptor L2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.73× (z +9.4, q 2e-18, up in 20 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.30× (z +4.5, q 8e-04, up in 15 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.389× (z -16.1, q 0e+00, down in 28 of 29 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.578× (z -9.3, q 8e-19, down in 24 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSH3]] (+0.59, fdr 1e-05), [[KIAA1522]] (+0.59, fdr 1e-05), [[TCEA3]] (+0.58, fdr 3e-05); moves opposite to [[TMEM168]] (-0.46, fdr 3e-05), [[GLIS3]] (-0.45, fdr 6e-05), [[CNRIP1]] (-0.44, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); 39 go from it, the strongest it → [[KIAA1522]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +9.4 | 2e-18 | 20/28 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.5 | 4e-15 | 16/24 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +5.1 | 7e-05 | 14/26 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 8e-04 | 15/28 (SW480, LoVo, …) | two highest doses | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.001 | 11/28 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.7 | 0.017 | 10/27 (HepG2/C3A, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.018 | 11/28 (HOP62, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimitespib (drug)]] 5 µM |  | 1.42× | +3.2 | 0.11 | 6/28 (HT-29, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.13 | 5/28 (Hs 766T, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.389×** | -16.1 | 0e+00 | 28/29 (AsPC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.416×** | -15.0 | 0e+00 | 29/29 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.479×** | -12.6 | 6e-34 | 27/29 (A-172, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.634×** | -11.0 | 6e-26 | 23/28 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.574×** | -9.5 | 3e-19 | 22/28 (Hs 766T, J82, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.578×** | -9.3 | 8e-19 | 24/29 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -9.3 | 8e-19 | 24/29 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -8.5 | 1e-15 | 20/28 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -8.0 | 6e-14 | 24/28 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.645×** | -7.2 | 3e-11 | 18/29 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.668×** | -6.9 | 3e-10 | 18/29 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -6.4 | 7e-09 | 23/29 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.694×** | -6.0 | 9e-08 | 19/28 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -5.9 | 1e-07 | 20/29 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.528×** | -5.7 | 5e-07 | 20/27 (HepG2/C3A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.719×** | -5.6 | 6e-07 | 14/28 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -5.3 | 3e-06 | 16/29 (MIA PaCa-2, Hs 766T, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.745×** | -5.0 | 2e-05 | 16/28 (HCT15, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.747×** | -5.0 | 2e-05 | 17/29 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.590×** | -4.7 | 6e-05 | 17/28 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.625×** | -4.2 | 7e-04 | 14/28 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.782×** | -4.0 | 0.002 | 15/28 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -3.9 | 0.002 | 14/29 (CFPAC-1, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -11.4) |
| [[PANC-1 (line)]] | alt | 33.0 | 2 (2 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +11.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.310× (z -13.3) |
| [[SW480 (line)]] | alt | 35.6 | 1 (1 ⚠) | 7 (6 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.32× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -13.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.422× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 42.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.9) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 29.1 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -15.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.448× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 37.3 | 1 (1 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.22× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.4) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -12.6) |
| [[HT-29 (line)]] | alt | 86.2 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -17.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -11.7) |
| [[A498 (line)]] | wt | 56.0 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 45.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 32.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -9.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 40.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.5) ⚠ cell-cycle shift, explains ~2% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[HEC-1-A (line)]] | alt | 73.9 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -12.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 22.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.8) ⚠ cell-cycle shift, explains ~2% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 72.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.8) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.383× (z -9.1) |
| [[SNU-423 (line)]] | alt | 31.8 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 87.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.491× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 61.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 88.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -8.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.4) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[SW48 (line)]] | wt | 48.1 | 0 | 1 | — | [[Tranilast (drug)]] 0.05 µM 0.171× (z -9.9) |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSH3]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[KIAA1522]] | +0.59 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TCEA3]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[CDC42BPG]] | +0.58 | +0.27 / +0.56 | both halves | 3e-04 |  |
| [[PLXNB2]] | +0.57 | +0.42 / +0.65 | both halves | 4e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[SYTL1]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 | STRING 437 |
| [[ANXA11]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[MAPK3]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MYO18A]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SH3BP2]] | +0.54 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[EVPL]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 | same gene group |
| [[PLCD3]] | +0.52 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM168]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[GLIS3]] | -0.45 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[CNRIP1]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[ABL1]] | -0.43 | -0.27 / -0.43 | both halves | 3e-04 | same gene group |
| [[PTPRD]] | -0.43 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[ST3GAL3]] | -0.43 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SIPA1L1]] | -0.43 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[NPAS2]] | -0.43 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[POLR1G]] | -0.42 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[MRPS12]] | -0.42 | -0.32 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 11, C 12. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises EPS8L2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without SEMA3B | 0.002 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[JUP]] | B | JUP activity raises EPS8L2's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.86× lower at baseline in the lines without JUP | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[CACNG4]] | B | CACNG4 activity raises EPS8L2's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without CACNG4 | 0.028 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N |
| [[ARHGAP30]] | B | ARHGAP30 activity raises EPS8L2's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without ARHGAP30 | 0.047 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises EPS8L2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NOXA1]] | B | NOXA1 activity raises EPS8L2's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 3.45× lower at baseline in the lines without NOXA1 | 0.055 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[SH3BP2]] | B | SH3BP2 activity raises EPS8L2's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.93× lower at baseline in the lines without SH3BP2 | 0.057 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ALDH3B1]] | B | ALDH3B1 activity raises EPS8L2's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 3.40× lower at baseline in the lines without ALDH3B1 | 0.064 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[TMEM184A]] | B | TMEM184A activity raises EPS8L2's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 3.46× lower at baseline in the lines without TMEM184A | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent; its own permutation p |
| [[GABRP]] | B | GABRP activity raises EPS8L2's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.60× lower at baseline in the lines without GABRP | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[PRR36]] | B | PRR36 activity raises EPS8L2's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.89× lower at baseline in the lines without PRR36 | 0.095 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[ITGB4]] | C | ITGB4 activity raises EPS8L2's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 4.21× lower at baseline in the lines without ITGB4 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 28, C 11. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1522]] | B | EPS8L2 activity raises KIAA1522's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 3.22× lower at baseline in the lines without EPS8L2 | 0.002 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[ANXA11]] | B | EPS8L2 activity raises ANXA11's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.69× lower at baseline in the lines without EPS8L2 | 0.002 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[INF2]] | B | EPS8L2 activity raises INF2's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without EPS8L2 | 0.003 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[NOXA1]] | B | EPS8L2 activity raises NOXA1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without EPS8L2 | 0.004 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[FAM102A]] | B | EPS8L2 activity raises FAM102A's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without EPS8L2 | 0.006 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[JUP]] | B | EPS8L2 activity raises JUP's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 4.00× lower at baseline in the lines without EPS8L2 | 0.007 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[MYO18A]] | B | EPS8L2 activity raises MYO18A's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without EPS8L2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[CAPN1]] | B | EPS8L2 activity raises CAPN1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without EPS8L2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[SH3BP2]] | B | EPS8L2 activity raises SH3BP2's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without EPS8L2 | 0.010 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[CACFD1]] | B | EPS8L2 activity raises CACFD1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without EPS8L2 | 0.019 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[SEMA3B]] | B | EPS8L2 activity raises SEMA3B's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without EPS8L2 | 0.020 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[SYTL1]] | B | EPS8L2 activity raises SYTL1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without EPS8L2 | 0.024 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.425). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.4, 56.2); signed map (-6.5, 17.7). **Vector** length 86.6, 24.8% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +3.8 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | EPS8 signaling adaptor L2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:694,438-727,727 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21935, FLJ22171, MGC3088 |
| Gene groups (HGNC) | EPS8 signaling adaptor family; SH3 domain containing |
| Hallmark sets | P53_PATHWAY |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6S3](https://www.uniprot.org/uniprotkb/Q9H6S3) (Epidermal growth factor receptor kinase substrate 8-like protein 2):

> Stimulates guanine exchange activity of SOS1. May play a role in membrane ruffling and remodeling of the actin cytoskeleton. In the cochlea, is required for stereocilia maintenance in adult hair cells (By similarity).

**Summary**, from NCBI Gene [64787](https://www.ncbi.nlm.nih.gov/gene/64787):

> This gene encodes a member of the EPS8 gene family. The encoded protein, like other members of the family, is thought to link growth factor stimulation to actin organization, generating functional redundancy in the pathways that regulate actin cytoskeletal remodeling. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:21296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21296) · Entrez [64787](https://www.ncbi.nlm.nih.gov/gene/64787) · UniProt [Q9H6S3](https://www.uniprot.org/uniprotkb/Q9H6S3) · Ensembl [ENSG00000177106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177106)

## Data

Gene col 10792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10792); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10792]; `tensor/DDL_lfc|DDL_z.npy` [10792]; `embed/gene_vectors.npy` [10792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10792 or target_col == 10792). Every well: [[EPS8L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPS8L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
