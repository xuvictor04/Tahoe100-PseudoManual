---
symbol: "ANAPC10"
type: "gene"
col: 8885
ensembl_id: "ENSG00000164162"
name: "anaphase promoting complex subunit 10"
location: "4q31.21"
module: 185
arm: "+"
pooled_cpm: 61.98
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# ANAPC10

*anaphase promoting complex subunit 10* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.86× (z +11.4, q 3e-27, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.533× (z -11.7, q 5e-29, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.837× (z -4.9, q 2e-04, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.262×, NCI-H2347 0.236×, SNU-1 0.176×, CHP-212 0.109×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (AN3 CA 0.0578×, KATO III 0.284×, SW480 0.399×, SK-MEL-2 0.269×, …; ⚠ toxic; transcription drop); [[Elimusertib hydrochloride (drug)]] 5 µM in 1 line (SK-MEL-2 0.0486×; ⚠ toxic); [[Vilanterol (drug)]] 0.05 µM in 1 line (SW 1088 0.0957×); [[4EGI-1 (drug)]] 5 µM in 1 line (H4 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMM50]] (+0.70, fdr 7e-06), [[OPA1]] (+0.68, fdr 7e-06), [[CDKAL1]] (+0.67, fdr 7e-06); moves opposite to [[ERF]] (-0.65, fdr 7e-06), [[HIVEP2]] (-0.59, fdr 3e-05), [[DLX2]] (-0.58, fdr 1e-05).
> It is in [[Module 185]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +11.4 | 3e-27 | 46/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +10.5 | 1e-23 | 34/45 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +10.0 | 3e-21 | 43/48 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.30×** | +7.3 | 4e-11 | 35/48 (CFPAC-1, KATO III, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +6.9 | 7e-10 | 36/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +6.3 | 3e-08 | 32/49 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +5.9 | 3e-07 | 35/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.9 | 3e-07 | 27/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.8 | 4e-07 | 31/48 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.5 | 2e-06 | 22/36 (HOP62, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.5 | 4e-04 | 23/48 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.53×** | +4.3 | 8e-04 | 26/49 (C32, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.003 | 20/49 (HOP62, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.004 | 16/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.20×** | +3.6 | 0.013 | 22/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.014 | 20/48 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.028 | 10/48 (RKO, SK-MEL-2, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.075 | 17/48 (H4, A-427, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8885.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.262×, NCI-H2347 0.236×, SNU-1 0.176×, CHP-212 0.109×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (AN3 CA 0.0578×, KATO III 0.284×, SW480 0.399×, SK-MEL-2 0.269×, …; ⚠ toxic; transcription drop); [[Elimusertib hydrochloride (drug)]] 5 µM in 1 line (SK-MEL-2 0.0486×; ⚠ toxic); [[Vilanterol (drug)]] 0.05 µM in 1 line (SW 1088 0.0957×); [[4EGI-1 (drug)]] 5 µM in 1 line (H4 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -11.7 | 5e-29 | 36/43 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.568×** | -11.0 | 1e-25 | 40/49 (AN3 CA, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -4.9 | 2e-04 | 22/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.790×** | -4.6 | 7e-04 | 29/48 (CFPAC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -3.9 | 0.013 | 26/48 (SW 1088, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.823×** | -3.8 | 0.015 | 21/48 (AsPC-1, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.886× | -3.3 | 0.072 | 18/48 (H4, SW 900, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 75.0 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 76.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.24× (z +21.0) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.14× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.7 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.60× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 49.4 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.39× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.92× (z +15.7) ⚠ toxic; transcription drop | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0486× (z -15.2) ⚠ toxic |
| [[A498 (line)]] | wt | 76.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.01× (z +13.9) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 73.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.19× (z +9.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.311× (z -10.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 96.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -13.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 52.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +8.6) | — |
| [[H4 (line)]] | wt | 90.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.70× (z +9.3) ⚠ toxic; transcription drop | [[4EGI-1 (drug)]] 5 µM 0.121× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 76.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.07× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 52.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.40× (z +13.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.397× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 63.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 89.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.57× (z +17.7) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 73.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 89.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.81× (z +10.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.176× (z -14.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 72.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -18.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 62.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 95.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0578× (z -17.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 59.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.461× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 80.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 76.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.09× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 49.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.34× (z +17.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 88.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.02× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 83.5 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0957× (z -8.6) |
| [[SW 900 (line)]] | alt | 55.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.44× (z +11.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMM50]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[OPA1]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[CDKAL1]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ADPGK]] | +0.66 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[PSMB2]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 445 |
| [[IPO11]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.64 | +0.71 / +0.49 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[SDHD]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SNRPD3]] | +0.63 | +0.65 / +0.43 | both halves | 3e-05 | STRING 589 |
| [[GDAP2]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ZNF875]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | +0.60 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | -0.65 | -0.66 / -0.66 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[HIVEP2]] | -0.59 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[DLX2]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SKIL]] | -0.57 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[HIVEP1]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[GLIS2]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[EPHB2]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[C11orf96]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[C21orf91]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[BMAL1]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[NBPF10]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PDLIM3]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.6, -13.4); signed map (-31.6, -27.2). **Vector** length 91.5, 22.0% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +11.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.4 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +6.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:144,831,908-145,098,541 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APC10, DOC1, DKFZP564L0562 |
| Gene groups (HGNC) | Anaphase promoting complex |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM13](https://www.uniprot.org/uniprotkb/Q9UM13) (Anaphase-promoting complex subunit 10):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [10393](https://www.ncbi.nlm.nih.gov/gene/10393):

> ANAPC10 is a core subunit of the anaphase-promoting complex (APC), or cyclosome, a ubiquitin protein ligase that is essential for progression through the cell cycle. APC initiates sister chromatid separation by ubiquitinating the anaphase inhibitor securin (PTTG1; MIM 604147) and triggers exit from mitosis by ubiquitinating cyclin B (CCNB1; MIM 123836), the activating subunit of cyclin-dependent kinase-1 (CDK1; MIM 116940) (summary by Wendt et al., 2001 [PubMed 11524682]).[supplied by OMIM, Feb …

**Accessions** — [HGNC:24077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24077) · Entrez [10393](https://www.ncbi.nlm.nih.gov/gene/10393) · UniProt [Q9UM13](https://www.uniprot.org/uniprotkb/Q9UM13) · Ensembl [ENSG00000164162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164162)

## Data

Gene col 8885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8885); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8885]; `tensor/DDL_lfc|DDL_z.npy` [8885]; `embed/gene_vectors.npy` [8885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8885 or target_col == 8885). Every well: [[ANAPC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
