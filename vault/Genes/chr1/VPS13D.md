---
symbol: "VPS13D"
type: "gene"
col: 539
ensembl_id: "ENSG00000048707"
name: "vacuolar protein sorting 13 homolog D"
location: "1p36.22-p36.21"
module: 36
arm: "+"
pooled_cpm: 128.91
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# VPS13D

*vacuolar protein sorting 13 homolog D* — 1p36.22-p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.23× (z +4.3, q 0.007, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.503× (z -20.0, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.755× (z -8.1, q 3e-14, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC2]] (+0.75, fdr 7e-06), [[HERC2]] (+0.69, fdr 1e-05), [[EHMT1]] (+0.67, fdr 7e-06); moves opposite to [[FAM200B]] (-0.58, fdr 2e-05), [[PLEKHA8P1]] (-0.57, fdr 3e-05), [[CLN5]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.3 | 0.007 | 26/48 (CFPAC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.007 | 28/48 (CFPAC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.011 | 24/48 (CFPAC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.22×** | +4.0 | 0.011 | 28/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.7 | 0.025 | 20/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.049 | 23/47 (SNU-423, RKO, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.054 | 19/48 (SW480, HCT15, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~97% of this change | 1.18× | +3.2 | 0.079 | 22/48 (A-427, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.2 | 0.079 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.079 | 22/48 (SW480, HCT15, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.0 | 0.12 | 3/48 (CFPAC-1, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 539.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.503×** | -20.0 | 0e+00 | 42/48 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.481×** | -14.5 | 7e-45 | 44/48 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.557×** | -11.4 | 1e-27 | 42/49 (A-427, RKO, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.576×** | -10.9 | 2e-25 | 34/44 (LS 180, NCI-H1573, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.597×** | -10.6 | 4e-24 | 37/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.584×** | -10.2 | 1e-22 | 38/45 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -10.0 | 1e-21 | 44/47 (HepG2/C3A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.755×** | -8.1 | 3e-14 | 34/48 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.691×** | -7.3 | 2e-11 | 34/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.704×** | -7.2 | 3e-11 | 33/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.706×** | -7.2 | 4e-11 | 31/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -7.1 | 6e-11 | 34/48 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -6.2 | 2e-08 | 27/49 (J82, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.735×** | -6.0 | 9e-08 | 28/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -5.5 | 1e-06 | 30/50 (HS-578T, A-427, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.888× | -3.4 | 0.018 | 4/49 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.895× | -3.2 | 0.038 | 6/48 (SHP-77, C-33 A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.765×** | -2.9 | 0.098 | 21/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 113 | 0 | 13 (12 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.292× (z -18.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.542× (z -9.6) |
| [[J82 (line)]] | alt | 148 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -26.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.506× (z -12.1) |
| [[PANC-1 (line)]] | alt | 139 | 0 | 10 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -19.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[LS 180 (line)]] | wt | 190 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -15.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C32 (line)]] | wt | 171 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.8) ⚠ cell-cycle shift, explains ~40% of this change | [[Harringtonine (drug)]] 0.5 µM 0.323× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.496× (z -11.0) |
| [[LoVo (line)]] | wt | 160 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -17.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.514× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 154 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -11.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HS-578T (line)]] | alt | 157 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -20.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.491× (z -10.1) |
| [[HT-29 (line)]] | alt | 94.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.490× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 179 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -19.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 181 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -21.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 75.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -20.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 159 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -25.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 98.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -15.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 116 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -20.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 83.0 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HepG2_C3A (line)]] | wt | 183 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.241× (z -16.0) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.274× (z -13.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 150 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.448× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 179 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -14.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 116 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -15.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -8.6) |
| [[SW480 (line)]] | alt | 128 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.364× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[BT-474 (line)]] | alt | 145 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -14.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.600× (z -8.8) |
| [[HOP62 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -19.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H596 (line)]] | alt | 119 | 2 (1 ⚠) | 1 | [[Salicylic acid (drug)]] 0.5 µM 3.85× (z +9.0) | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.261× (z -9.0) |
| [[SW48 (line)]] | wt | 147 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.142× (z -9.8) |
| [[AN3 CA (line)]] | alt | 205 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.436× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -10.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -17.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -17.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -17.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-423 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -23.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW1417 (line)]] | alt | 88.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -14.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C-33 A (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.445× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -9.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[H4 (line)]] | wt | 91.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.510× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.464× (z -8.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 75.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.618× (z -8.5) |
| [[SNU-1 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC2]] | +0.75 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[HERC2]] | +0.69 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[EHMT1]] | +0.67 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[EXOC6B]] | +0.66 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[HERC2P9]] | +0.64 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[RNF216]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[EP400]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 | same gene group |
| [[EPS15L1]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[RAB5IF]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[HERC2P2]] | +0.59 | +0.62 / +0.37 | both halves | 9e-05 |  |
| [[DAP3]] | +0.58 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200B]] | -0.58 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[PLEKHA8P1]] | -0.57 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CLN5]] | -0.56 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RAB38]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MALINC1]] | -0.55 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[HCP5]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ATP23]] | -0.51 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[FAM111A-DT]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[LINC00938]] | -0.51 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[FAM117A]] | -0.51 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[MIR181A2HG]] | -0.50 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[ERCC6L2-AS1]] | -0.50 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers VPS13D's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AGTPBP1]] | C | AGTPBP1 activity raises VPS13D's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.36× lower at baseline in the lines without AGTPBP1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-6.7, -31.5); signed map (-16.7, -52.6). **Vector** length 101, 32.4% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~97% of this change | +7.2 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.9 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +3.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.7 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -6.7 | -20.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.9 | -10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 13 homolog D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22-p36.21 — chr1:12,230,030-12,512,047 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10619, KIAA0453, BLTP5D |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5THJ4](https://www.uniprot.org/uniprotkb/Q5THJ4) (Intermembrane lipid transfer protein VPS13D):

> Mediates the transfer of lipids between membranes at organelle contact sites (By similarity). Functions in promoting mitochondrial clearance by mitochondrial autophagy (mitophagy), also possibly by positively regulating mitochondrial fission. Mitophagy plays an important role in regulating cell health and mitochondrial size and homeostasis.

**Summary**, from NCBI Gene [55187](https://www.ncbi.nlm.nih.gov/gene/55187):

> This gene encodes a protein belonging to the vacuolar-protein-sorting-13 gene family. In yeast, vacuolar-protein-sorting-13 proteins are involved in trafficking of membrane proteins between the trans-Golgi network and the prevacuolar compartment. While several transcript variants may exist for this gene, the full-length natures of only two have been described to date. These two represent the major variants of this gene and encode distinct isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23595) · Entrez [55187](https://www.ncbi.nlm.nih.gov/gene/55187) · UniProt [Q5THJ4](https://www.uniprot.org/uniprotkb/Q5THJ4) · Ensembl [ENSG00000048707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048707)

## Data

Gene col 539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 539); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 539]; `tensor/DDL_lfc|DDL_z.npy` [539]; `embed/gene_vectors.npy` [539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 539 or target_col == 539). Every well: [[VPS13D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS13D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
