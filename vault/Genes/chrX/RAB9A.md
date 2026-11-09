---
symbol: "RAB9A"
type: "gene"
col: 4446
ensembl_id: "ENSG00000123595"
name: "RAB9A, member RAS oncogene family"
location: "Xp22.2"
module: 59
arm: "+"
pooled_cpm: 41.66
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# RAB9A

*RAB9A, member RAS oncogene family* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +14.0, q 8e-42, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.35× (z +10.9, q 3e-25, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.572× (z -6.4, q 8e-08, down in 27 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (CFPAC-1 0.128×, Panc 03.27 0.100×, LS 180 0.101×, NCI-H2347 0.246×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.227×, A-172 0.186×, CFPAC-1 0.265×, SNU-423 0.240×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.164×; ⚠ cell-cycle shift, explains ~33% of this change); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H661 0.0474×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAMP2]] (+0.71, fdr 7e-06), [[SAT2]] (+0.69, fdr 7e-06), [[PIM3]] (+0.68, fdr 7e-06); moves opposite to [[GCN1]] (-0.65, fdr 8e-06), [[BCAP31]] (-0.65, fdr 8e-06), [[ARHGAP4]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NEURL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.18×** | +14.0 | 8e-42 | 41/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +12.2 | 7e-32 | 43/46 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.35×** | +10.9 | 3e-25 | 42/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.10×** | +9.1 | 1e-17 | 41/48 (NCI-H460, HS-578T, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.85×** | +7.8 | 6e-13 | 38/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +7.3 | 3e-11 | 34/49 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +6.9 | 4e-10 | 37/48 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.69×** | +6.7 | 2e-09 | 33/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.8 | 4e-07 | 29/45 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 2e-06 | 28/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 6e-04 | 26/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.2 | 0.001 | 29/47 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.006 | 22/48 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +3.5 | 0.019 | 20/47 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.061 | 16/48 (SW480, NCI-H2347, …) | top dose only | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.072 | 12/48 (BT-474, HS-578T, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.097 | 11/47 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.097 | 12/48 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.097 | 11/49 (NCI-H2030, SNU-423, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.097 | 12/49 (NCI-H1792, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4446.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (CFPAC-1 0.128×, Panc 03.27 0.100×, LS 180 0.101×, NCI-H2347 0.246×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.227×, A-172 0.186×, CFPAC-1 0.265×, SNU-423 0.240×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.164×; ⚠ cell-cycle shift, explains ~33% of this change); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H661 0.0474×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.572×** | -6.4 | 8e-08 | 27/46 (NCI-H2347, A-172, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -5.7 | 3e-06 | 22/36 (CFPAC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.779× | -3.2 | 0.22 | 19/48 (NCI-H1573, CFPAC-1, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.840× | -3.2 | 0.22 | 23/49 (NCI-H1573, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.5 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.66× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 80.0 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.80× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 96.8 | 2 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.35× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 72.4 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 49.8 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +17.2) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -11.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 29.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +13.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 70.7 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 96.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -19.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 68.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.289× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 48.1 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.77× (z +14.2) | — |
| [[LS 180 (line)]] | wt | 37.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.08× (z +9.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.101× (z -17.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 60.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.58× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.3 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +11.4) | — |
| [[SW480 (line)]] | alt | 38.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +12.5) | — |
| [[A498 (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +13.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 39.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 24.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.77× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 50.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -17.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 72.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.8) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.303× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -11.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 47.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 34.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +10.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 27.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 54.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 73.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -8.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H23 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.19× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0474× (z -8.7) |
| [[SW 900 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP2]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[SAT2]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[PIM3]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[XPA]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CLN8-AS1]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.66 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CHMP2B]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LINC01273]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[EFNA1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SPPL3]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCN1]] | -0.65 | -0.58 / -0.68 | both halves | 8e-06 |  |
| [[BCAP31]] | -0.65 | -0.58 / -0.67 | both halves | 8e-06 |  |
| [[ARHGAP4]] | -0.65 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[TPM3]] | -0.65 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[PTDSS1]] | -0.64 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.63 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.62 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[RNPS1]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.62 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.61 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[ACOT7]] | -0.61 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL3]] | B | NEURL3 activity raises RAB9A's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without NEURL3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[PTGES]] | B | PTGES activity raises RAB9A's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.57× lower at baseline in the lines without PTGES | 0.008 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[RHOV]] | B | RHOV activity raises RAB9A's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without RHOV | 0.025 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[GBP2]] | B | GBP2 activity raises RAB9A's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without GBP2 | 0.025 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[MPZL3]] | B | MPZL3 activity raises RAB9A's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.41× lower at baseline in the lines without MPZL3 | 0.085 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[BMF]] | C | BMF activity raises RAB9A's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.36× lower at baseline in the lines without BMF | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.806). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.9, -4.1); signed map (-8.1, 1.8). **Vector** length 112, 32.7% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.6 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +6.2 | +14.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.9 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.7 | +9.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.6 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.5 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +2.7 |
|  | [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +1.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB9A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:13,689,128-13,710,504 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAB9 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 9 pathways, smallest: RHOBTB3 ATPase cycle; Retrograde transport at the Trans-Golgi-Network; RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P51151](https://www.uniprot.org/uniprotkb/P51151) (Ras-related protein Rab-9A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB9A is involved in the transport of proteins between the endosomes and the trans-Golgi network (TGN). …

**Summary**, from NCBI Gene [9367](https://www.ncbi.nlm.nih.gov/gene/9367):

> Enables G protein activity; GDP binding activity; and GTP binding activity. Involved in positive regulation of exocytosis; receptor-mediated endocytosis; and regulation of protein localization. Located in late endosome; lysosome; and phagocytic vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9792) · Entrez [9367](https://www.ncbi.nlm.nih.gov/gene/9367) · UniProt [P51151](https://www.uniprot.org/uniprotkb/P51151) · Ensembl [ENSG00000123595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123595)

## Data

Gene col 4446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4446); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4446]; `tensor/DDL_lfc|DDL_z.npy` [4446]; `embed/gene_vectors.npy` [4446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4446 or target_col == 4446). Every well: [[RAB9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
