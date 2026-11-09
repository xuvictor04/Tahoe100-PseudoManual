---
symbol: "SPC25"
type: "gene"
col: 7609
ensembl_id: "ENSG00000152253"
name: "SPC25 component of NDC80 kinetochore complex"
location: "2q31.1"
module: 67
arm: "+"
pooled_cpm: 27.38
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 35
n_dd_up_clean: 4
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# SPC25

*SPC25 component of NDC80 kinetochore complex* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.65× (z +7.3, q 8e-11, up in 27 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM: 1.31× (z +3.3, q 0.031, up in 7 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.378× (z -20.2, q 0e+00, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD51AP1]] (+0.92, fdr 7e-06), [[MELK]] (+0.92, fdr 7e-06), [[SPC24]] (+0.91, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.65×** | +7.3 | 8e-11 | 27/43 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.68×** | +7.3 | 8e-11 | 29/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.61×** | +6.7 | 4e-09 | 21/36 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.34×** | +6.2 | 1e-07 | 28/47 (HS-578T, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.47×** | +5.5 | 5e-06 | 22/47 (SW480, SW1417, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.29×** | +5.3 | 1e-05 | 19/47 (SW480, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.43×** | +5.2 | 1e-05 | 23/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.42×** | +5.2 | 2e-05 | 23/46 (PANC-1, HS-578T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.43×** | +4.9 | 6e-05 | 21/41 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +4.8 | 1e-04 | 19/47 (KATO III, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.26×** | +4.7 | 1e-04 | 20/46 (Panc 03.27, SW480, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.38×** | +4.7 | 1e-04 | 15/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +4.2 | 0.001 | 19/46 (KATO III, SHP-77, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.34×** | +3.5 | 0.016 | 15/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.5 | 0.020 | 20/47 (C32, NCI-H23, …) | all doses, flat |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.031 | 7/47 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.033 | 8/47 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.080 | 11/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.32×** | +2.9 | 0.086 | 7/47 (SW480, HOP62, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.378×** | -20.2 | 0e+00 | 36/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.270×** | -19.2 | 0e+00 | 41/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.457×** | -11.0 | 4e-26 | 38/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.534×** | -9.2 | 5e-18 | 35/47 (SNU-1, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.552×** | -8.7 | 3e-16 | 35/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.493×** | -8.4 | 3e-15 | 34/47 (HCT15, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.464×** | -8.0 | 8e-14 | 35/47 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.728×** | -6.6 | 3e-09 | 24/47 (LS 180, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -6.4 | 8e-09 | 28/47 (SW480, HOP62, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.737×** | -6.3 | 1e-08 | 29/47 (RKO, A-172, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.746×** | -6.1 | 6e-08 | 30/47 (HCT15, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.685×** | -5.6 | 1e-06 | 25/47 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.484×** | -5.5 | 2e-06 | 22/41 (NCI-H23, A-172, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.650×** | -5.2 | 7e-06 | 23/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.515×** | -5.0 | 2e-05 | 22/47 (A498, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.788×** | -4.9 | 3e-05 | 23/47 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.570×** | -4.3 | 6e-04 | 17/46 (SW480, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.818×** | -4.2 | 8e-04 | 17/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.755×** | -4.1 | 1e-03 | 22/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.842× | -3.6 | 0.009 | 18/47 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.843× | -3.6 | 0.009 | 10/47 (A-172, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.82 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 40.1 | 0 | 9 (5 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.119× (z -11.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 25.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.9) |
| [[A498 (line)]] | wt | 25.5 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.187× (z -15.6) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.8) |
| [[H4 (line)]] | wt | 40.6 | 0 | 7 (4 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0592× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.172× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 25.6 | 0 | 7 (4 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.190× (z -13.4) |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -17.1) |
| [[SW480 (line)]] | alt | 42.0 | 2 (2 ⚠) | 5 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +11.0) ⚠ cell-cycle shift, explains ~63% of this change | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -22.1) |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 1 (1 ⚠) | 4 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +8.9) ⚠ cell-cycle shift, explains ~63% of this change | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -15.1) |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.175× (z -10.8) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.212× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 83.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -19.9) |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.0) |
| [[A-427 (line)]] | wt | 49.7 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.243× (z -14.3) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.6) |
| [[HCT15 (line)]] | alt | 45.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.7) |
| [[HOP62 (line)]] | alt | 40.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 26.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.6) ⚠ cell-cycle shift, explains ~81% of this change | [[Selinexor (drug)]] 5 µM 0.309× (z -10.9) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 46.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.0) |
| [[KATO III (line)]] | alt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -9.0) |
| [[RKO (line)]] | wt | 26.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.168× (z -9.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.197× (z -9.0) |
| [[SW48 (line)]] | wt | 28.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -15.1) |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -8.8) |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.3) |
| [[J82 (line)]] | alt | 42.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 8.84 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0705× (z -8.5) |
| [[PANC-1 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -10.0) |
| [[A549 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD51AP1]] | +0.92 | +0.92 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 582 |
| [[MELK]] | +0.92 | +0.93 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 724 |
| [[SPC24]] | +0.91 | +0.93 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[CENPK]] | +0.89 | +0.92 / +0.87 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 649 |
| [[TICRR]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[POLQ]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 |  |
| [[PBK]] | +0.89 | +0.91 / +0.89 | both halves | 7e-06 | STRING 877 |
| [[FANCI]] | +0.88 | +0.89 / +0.86 | both halves | 7e-06 | STRING 424 |
| [[C21orf58]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[KIF22]] | +0.88 | +0.88 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 458 |
| [[NCAPG2]] | +0.88 | +0.89 / +0.88 | both halves | 7e-06 | STRING 556 |
| [[KIFC1]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 | STRING 477 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 7, C 9. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises SPC25's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.27× lower at baseline in the lines without E2F8 | 0.029 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises SPC25's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without TCF19 | 0.036 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises SPC25's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without PIMREG | 0.036 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers SPC25's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises SPC25's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without CDC25A | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises SPC25's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without FAM111B | 0.077 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises SPC25's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without TLCD3B | 0.078 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[E2F8]] | C | E2F8 activity strengthens SPC25's drug response | lines that do not express E2F8 (4) vs lines expressing it (43) | the lines without E2F8 respond 0.35× as strongly (z diff +2.37); strongest at Homoharringtonine 0.5 µM: 1.00x vs 0.26x (z diff +6.4) | 0.011 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises SPC25's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.46× lower at baseline in the lines without DSCC1 | 0.016 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises SPC25's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.79× lower at baseline in the lines without AURKB | 0.047 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises SPC25's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.15× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[SHMT1]] | C | SHMT1 activity raises SPC25's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.903). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.1, -47.7); signed map (-40.6, -43.6). **Vector** length 151, 50.3% of its response variance represented; |z| ≥ 3 in 1,353 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.82 to 9); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.72 to 4); *Nucleosome assembly* (reactome, mean cos +0.72 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | +5.5 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +5.3 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.0 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +4.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +3.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.3 | +3.3 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.3 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.9 | -19.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -20.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -7.1 | -8.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -6.9 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -6.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.9 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | SPC25 component of NDC80 kinetochore complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:168,834,132-168,913,371 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22228, AD024; previously SPBC25 |
| Gene groups (HGNC) | NDC80 kinetochore complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBM1](https://www.uniprot.org/uniprotkb/Q9HBM1) (Kinetochore protein Spc25):

> Acts as a component of the essential kinetochore-associated NDC80 complex, which is required for chromosome segregation and spindle checkpoint activity. Required for kinetochore integrity and the organization of stable microtubule binding sites in the outer plate of the kinetochore. The NDC80 complex synergistically enhances the affinity of the SKA1 complex for microtubules and may allow the NDC80 complex to track depolymerizing microtubules.

**Summary**, from NCBI Gene [57405](https://www.ncbi.nlm.nih.gov/gene/57405):

> This gene encodes a protein that may be involved in kinetochore-microtubule interaction and spindle checkpoint activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24031) · Entrez [57405](https://www.ncbi.nlm.nih.gov/gene/57405) · UniProt [Q9HBM1](https://www.uniprot.org/uniprotkb/Q9HBM1) · Ensembl [ENSG00000152253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152253)

## Data

Gene col 7609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7609); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7609]; `tensor/DDL_lfc|DDL_z.npy` [7609]; `embed/gene_vectors.npy` [7609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7609 or target_col == 7609). Every well: [[SPC25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPC25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
