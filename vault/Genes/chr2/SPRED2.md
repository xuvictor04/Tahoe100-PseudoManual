---
symbol: "SPRED2"
type: "gene"
col: 12579
ensembl_id: "ENSG00000198369"
name: "sprouty related EVH1 domain containing 2"
location: "2p14"
module: 92
arm: "+"
pooled_cpm: 239.79
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 46
n_dd_up_clean: 1
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# SPRED2

*sprouty related EVH1 domain containing 2* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.60× (z +5.1, q 2e-04, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 2.29×, Panc 03.27 2.17×, LoVo 1.66×, SNU-1 1.92×, …; ⚠ cell-cycle shift, explains ~4% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (AsPC-1 2.23×, LoVo 1.97×, SW1417 1.93×; ⚠ cell-cycle shift, explains ~7% of this change).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.422× (z -16.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRY4]] (+0.80, fdr 7e-06), [[ITGB5]] (+0.78, fdr 7e-06), [[SPRY4-AS1]] (+0.77, fdr 7e-06).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ASTL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12579.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 2.29×, Panc 03.27 2.17×, LoVo 1.66×, SNU-1 1.92×, …; ⚠ cell-cycle shift, explains ~4% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (AsPC-1 2.23×, LoVo 1.97×, SW1417 1.93×; ⚠ cell-cycle shift, explains ~7% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +5.1 | 2e-04 | 34/49 (C32, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.26× | +3.4 | 0.21 | 27/48 (HEC-1-A, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.422×** | -16.5 | 0e+00 | 48/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.334×** | -16.1 | 0e+00 | 48/50 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.361×** | -16.1 | 0e+00 | 48/49 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.356×** | -15.7 | 0e+00 | 43/44 (NCI-H23, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.359×** | -15.6 | 0e+00 | 46/47 (NCI-H23, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.371×** | -15.1 | 0e+00 | 48/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.393×** | -14.8 | 0e+00 | 48/49 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.443×** | -11.7 | 1e-29 | 47/49 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.579×** | -10.3 | 4e-23 | 46/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.494×** | -10.3 | 4e-23 | 38/45 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.644×** | -9.7 | 3e-20 | 45/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.552×** | -9.4 | 3e-19 | 43/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.526×** | -9.4 | 3e-19 | 47/48 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.561×** | -9.1 | 3e-18 | 39/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.561×** | -9.1 | 3e-18 | 45/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.615×** | -7.7 | 7e-13 | 42/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.592×** | -7.5 | 3e-12 | 45/48 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.750×** | -6.1 | 3e-08 | 38/49 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 357 | 0 | 18 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0393× (z -33.3) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.118× (z -21.5) |
| [[C32 (line)]] | wt | 270 | 0 | 17 (1 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.219× (z -19.8) |
| [[SW480 (line)]] | alt | 298 | 0 | 17 (3 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.266× (z -21.7) |
| [[MIA PaCa-2 (line)]] | alt | 237 | 0 | 16 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.415× (z -29.5) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.204× (z -18.4) |
| [[NCI-H2347 (line)]] | alt | 198 | 0 | 16 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.406× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 184 | 0 | 15 (3 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.321× (z -18.9) |
| [[SHP-77 (line)]] | alt | 206 | 0 | 14 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.277× (z -17.7) |
| [[SW1417 (line)]] | alt | 262 | 1 (1 ⚠) | 13 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +8.5) ⚠ cell-cycle shift, explains ~7% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.424× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 201 | 0 | 13 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.410× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 174 | 1 (1 ⚠) | 12 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +13.8) ⚠ cell-cycle shift, explains ~4% of this change | [[Cobimetinib (drug)]] 5 µM 0.194× (z -18.5) |
| [[Panc 03.27 (line)]] | alt | 103 | 1 (1 ⚠) | 11 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +12.0) ⚠ cell-cycle shift, explains ~4% of this change | [[Dinaciclib (drug)]] 5 µM 0.327× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.290× (z -11.4) |
| [[Hs 766T (line)]] | wt | 107 | 0 | 11 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.254× (z -12.1) |
| [[HT-29 (line)]] | alt | 441 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.285× (z -12.5) |
| [[A-427 (line)]] | wt | 284 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0348× (z -36.4) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.181× (z -17.7) |
| [[H4 (line)]] | wt | 254 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -16.4) |
| [[HepG2_C3A (line)]] | wt | 316 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.365× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 183 | 0 | 10 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.171× (z -18.1) |
| [[PANC-1 (line)]] | alt | 367 | 0 | 10 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.250× (z -11.1) |
| [[A-172 (line)]] | wt | 167 | 0 | 9 (3 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.217× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 283 | 1 (1 ⚠) | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.8) ⚠ cell-cycle shift, explains ~7% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.411× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 314 | 0 | 9 (3 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.366× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 161 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.295× (z -15.4) |
| [[A549 (line)]] | wt | 212 | 0 | 8 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.190× (z -20.7) |
| [[HCT15 (line)]] | alt | 293 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0663× (z -29.0) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.353× (z -11.9) |
| [[SNU-1 (line)]] | wt | 234 | 1 (1 ⚠) | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.2) ⚠ cell-cycle shift, explains ~4% of this change | [[Trametinib (drug)]] 0.5 µM 0.379× (z -11.7) |
| [[COLO 205 (line)]] | alt | 260 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.270× (z -12.1) |
| [[HOP62 (line)]] | alt | 262 | 0 | 7 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.606× (z -11.3) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.249× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 368 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -12.9) |
| [[RKO (line)]] | wt | 407 | 0 | 7 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.415× (z -9.9) |
| [[C-33 A (line)]] | alt | 163 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.355× (z -10.7) |
| [[BT-474 (line)]] | alt | 212 | 0 | 5 | — | [[Trametinib (drug)]] 5 µM 0.351× (z -11.3) |
| [[J82 (line)]] | alt | 131 | 0 | 5 | — | [[Ponatinib (drug)]] 5 µM 0.325× (z -11.2) |
| [[KATO III (line)]] | alt | 180 | 1 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.8) ⚠ cell-cycle shift, explains ~4% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 0.5 µM 0.438× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 241 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.244× (z -12.7) |
| [[SW 900 (line)]] | alt | 292 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.5) |
| [[LoVo (line)]] | wt | 184 | 2 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.2) ⚠ cell-cycle shift, explains ~4% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -11.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 289 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 330 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -15.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 249 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 172 | 0 | 3 | — | [[Cobimetinib (drug)]] 5 µM 0.355× (z -9.4) |
| [[SW48 (line)]] | wt | 313 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -12.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 137 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.456× (z -9.1) |
| [[CHP-212 (line)]] | wt | 137 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.261× (z -11.3) |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 303 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0988× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 160 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY4]] | +0.80 | +0.80 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 709 |
| [[ITGB5]] | +0.78 | +0.78 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4-AS1]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 | pathway: MAPK family signaling cascades; STRING 487 |
| [[SPRED1]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 | same gene group; pathway: FGFRL1 modulation of FGFR1 signaling; STRING 892 |
| [[ETV5]] | +0.70 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[PHC2]] | +0.70 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[ETV4]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[LINC01844]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EGR3]] | +0.67 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[ETV1]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.66 | +0.71 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASTL]] | B | ASTL activity raises SPRED2's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.28× lower at baseline in the lines without ASTL | 0.080 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, 6.3); signed map (8.2, 47.6). **Vector** length 150, 60.2% of its response variance represented; |z| ≥ 3 in 1,851 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +12.7 | +2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | -0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | -0.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.7 | +0.3 |
|  | [[Lonafarnib (drug)]] 0.05 µM |  | +2.6 | +2.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -13.9 | -16.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -13.0 | -16.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -12.8 | -15.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -12.4 | -14.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -12.0 | -15.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -11.9 | -11.7 |

## What is on record

|  |  |
|---|---|
| Name | sprouty related EVH1 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:65,310,851-65,432,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Spred-2, FLJ21897, FLJ31917 |
| Gene groups (HGNC) | Sprouty related EVH1 domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 11 pathways, smallest: FGFRL1 modulation of FGFR1 signaling; RAS signaling downstream of NF1 loss-of-function variants; Signaling by FGFR1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z698](https://www.uniprot.org/uniprotkb/Q7Z698) (Sprouty-related, EVH1 domain-containing protein 2):

> Negatively regulates Ras signaling pathways and downstream activation of MAP kinases. Recruits and translocates NF1 to the cell membrane, thereby enabling NF1-dependent hydrolysis of active GTP-bound Ras to inactive GDP-bound Ras. Inhibits fibroblast growth factor (FGF)-induced retinal lens fiber differentiation, probably by inhibiting FGF-mediated phosphorylation of ERK1/2 (By similarity). Inhibits TGFB-induced epithelial-to-mesenchymal transition in lens epithelial cells (By similarity).

**Summary**, from NCBI Gene [200734](https://www.ncbi.nlm.nih.gov/gene/200734):

> SPRED2 is a member of the Sprouty (see SPRY1; MIM 602465)/SPRED family of proteins that regulate growth factor-induced activation of the MAP kinase cascade (see MAPK1; MIM 176948) (Nonami et al., 2004 [PubMed 15465815]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17722) · Entrez [200734](https://www.ncbi.nlm.nih.gov/gene/200734) · UniProt [Q7Z698](https://www.uniprot.org/uniprotkb/Q7Z698) · Ensembl [ENSG00000198369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198369)

## Data

Gene col 12579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12579); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12579]; `tensor/DDL_lfc|DDL_z.npy` [12579]; `embed/gene_vectors.npy` [12579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12579 or target_col == 12579). Every well: [[SPRED2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRED2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
