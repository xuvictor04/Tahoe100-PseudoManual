---
symbol: "CRIPT"
type: "gene"
col: 4129
ensembl_id: "ENSG00000119878"
name: "CXXC repeat containing interactor of PDZ3 domain"
location: "2p21"
module: 76
arm: "+"
pooled_cpm: 29.93
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 18
n_dd_up_clean: 13
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# CRIPT

*CXXC repeat containing interactor of PDZ3 domain* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.43× (z +17.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.313× (z -22.4, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.276× (z -13.0, q 6e-36, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALCOCO1]] (+0.77, fdr 7e-06), [[CCDC28A]] (+0.76, fdr 7e-06), [[ADIPOR1]] (+0.72, fdr 7e-06); moves opposite to [[ANKRD18A]] (-0.55, fdr 2e-05), [[POGLUT1]] (-0.55, fdr 3e-05), [[SLC12A2-DT]] (-0.54, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +17.2 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +16.1 | 0e+00 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +14.8 | 0e+00 | 45/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +8.8 | 2e-16 | 35/48 (NCI-H23, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +6.6 | 5e-09 | 30/48 (HOP62, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +6.4 | 2e-08 | 28/48 (NCI-H1573, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.3 | 2e-08 | 29/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.7 | 9e-07 | 28/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.23×** | +5.4 | 5e-06 | 24/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 2e-04 | 19/48 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 3e-04 | 22/48 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.001 | 23/48 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.2 | 0.001 | 17/48 (SW480, HT-29, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.007 | 17/46 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.21×** | +3.6 | 0.012 | 13/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.026 | 12/48 (SNU-423, PANC-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.027 | 11/48 (NCI-H23, HOP62, …) | all doses, flat | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.313×** | -22.4 | 0e+00 | 47/48 (A498, AsPC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.276×** | -13.0 | 6e-36 | 42/48 (AsPC-1, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.308×** | -11.8 | 5e-30 | 42/47 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.320×** | -11.5 | 3e-28 | 42/48 (AsPC-1, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.351×** | -10.5 | 8e-24 | 38/48 (Panc 03.27, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.359×** | -10.3 | 8e-23 | 40/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.730×** | -8.2 | 2e-14 | 27/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.594×** | -7.2 | 5e-11 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.702×** | -6.6 | 3e-09 | 27/47 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.708×** | -6.3 | 2e-08 | 25/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.644×** | -6.1 | 7e-08 | 28/48 (A498, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.775×** | -4.9 | 5e-05 | 20/47 (AsPC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.784×** | -4.7 | 1e-04 | 20/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.808×** | -3.9 | 0.004 | 18/47 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.766×** | -3.7 | 0.009 | 13/48 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Volasertib (drug)]] 0.5 µM |  | **0.787×** | -3.3 | 0.034 | 11/48 (NCI-H661, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 48.9 | 0 | 7 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.145× (z -17.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 26.3 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +12.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.234× (z -14.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.181× (z -9.0) |
| [[A549 (line)]] | wt | 42.0 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.291× (z -11.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.141× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 64.2 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.202× (z -8.9) |
| [[SW480 (line)]] | alt | 26.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -12.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 22.0 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.71× (z +9.4) | — |
| [[A-427 (line)]] | wt | 45.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.59× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.319× (z -10.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.495× (z -8.8) |
| [[A498 (line)]] | wt | 36.1 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.176× (z -17.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.138× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 32.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.322× (z -9.6) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.40× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -11.9) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0682× (z -9.8) |
| [[PANC-1 (line)]] | alt | 29.2 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -14.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.3) |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 2 | — | [[EX229 (drug)]] 5 µM 0.0394× (z -10.9) |
| [[HOP62 (line)]] | alt | 26.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +9.4) | — |
| [[KATO III (line)]] | alt | 38.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.322× (z -9.5) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.141× (z -15.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 20.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.324× (z -9.8) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 24.5 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0912× (z -15.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 34.9 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -8.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.433× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -12.2) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0978× (z -8.9) |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.260× (z -10.4) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.249× (z -8.9) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.349× (z -9.0) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -11.3) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.228× (z -12.0) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -10.0) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 1 | — | [[Relugolix (drug)]] 5 µM 0.192× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.240× (z -9.9) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -8.7) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -8.7) |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.290× (z -10.9) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALCOCO1]] | +0.77 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CCDC28A]] | +0.76 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SARAF]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.66 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[KLHDC3]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SERINC1]] | +0.65 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[ABTB1]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[CCNDBP1]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[IFT20]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[PAIP2]] | +0.63 | +0.49 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18A]] | -0.55 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[POGLUT1]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SLC12A2-DT]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[SLC16A9]] | -0.54 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ST7L]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[UTP20]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PAXIP1]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.5, -45.5); signed map (-19.2, 10.2). **Vector** length 119, 32.2% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +16.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +6.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +17.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +14.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.8 | +4.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.2 | -22.4 |
|  | [[EX229 (drug)]] 5 µM |  | -9.7 | -13.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.3 | -11.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -8.9 | -11.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.6 | -10.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.7 | -10.3 |

## What is on record

|  |  |
|---|---|
| Name | CXXC repeat containing interactor of PDZ3 domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:46,616,416-46,630,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC139 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P021](https://www.uniprot.org/uniprotkb/Q9P021) (Cysteine-rich PDZ-binding protein):

> As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable). Involved in the cytoskeletal anchoring of DLG4 in excitatory synapses (By similarity).

**Summary**, from NCBI Gene [9419](https://www.ncbi.nlm.nih.gov/gene/9419):

> This gene encodes a protein that binds to the PDZ3 peptide recognition domain. The encoded protein may modulates protein interactions with the cytoskeleton. A mutation in this gene resulted in short stature with microcephaly and distinctive facies. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:14312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14312) · Entrez [9419](https://www.ncbi.nlm.nih.gov/gene/9419) · UniProt [Q9P021](https://www.uniprot.org/uniprotkb/Q9P021) · Ensembl [ENSG00000119878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119878)

## Data

Gene col 4129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4129); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4129]; `tensor/DDL_lfc|DDL_z.npy` [4129]; `embed/gene_vectors.npy` [4129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4129 or target_col == 4129). Every well: [[CRIPT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRIPT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
