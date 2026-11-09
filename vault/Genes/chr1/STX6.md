---
symbol: "STX6"
type: "gene"
col: 5760
ensembl_id: "ENSG00000135823"
name: "syntaxin 6"
location: "1q25.3"
module: 84
arm: "+"
pooled_cpm: 57.85
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# STX6

*syntaxin 6* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.28× (z +10.3, q 4e-22, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.571× (z -9.3, q 7e-18, down in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.803× (z -4.0, q 0.009, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LOX-IMVI 0.265×, SK-MEL-2 0.303×, NCI-H460 0.356×, C-33 A 0.211×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.209×, NCI-H2347 0.409×, SW 900 0.290×, SK-MEL-2 0.422×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (HOP62 0.0772×; ⚠ toxic); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.292×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM104A]] (+0.60, fdr 1e-05), [[CEP170]] (+0.60, fdr 1e-05), [[ECI2]] (+0.57, fdr 3e-05); moves opposite to [[STAG1]] (-0.53, fdr 3e-05), [[DIO2]] (-0.52, fdr 7e-05), [[HECTD1]] (-0.50, fdr 3e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GLS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.28×** | +10.3 | 4e-22 | 44/49 (NCI-H1573, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.85×** | +10.2 | 5e-22 | 44/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.79×** | +9.7 | 9e-20 | 42/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.70×** | +8.8 | 3e-16 | 41/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +7.7 | 2e-12 | 37/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +7.6 | 4e-12 | 44/48 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +7.4 | 1e-11 | 41/48 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +6.5 | 7e-09 | 36/48 (J82, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.3 | 1e-08 | 31/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.40×** | +5.5 | 2e-06 | 33/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 1e-05 | 30/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.35×** | +4.7 | 1e-04 | 27/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.22×** | +4.7 | 1e-04 | 21/49 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +4.5 | 3e-04 | 28/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.30×** | +4.3 | 6e-04 | 25/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 7e-04 | 25/48 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.001 | 23/49 (AsPC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 25/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.008 | 14/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.5 | 0.012 | 19/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.027 | 17/49 (J82, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.13× | +2.9 | 0.070 | 6/48 (HT-29, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5760.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LOX-IMVI 0.265×, SK-MEL-2 0.303×, NCI-H460 0.356×, C-33 A 0.211×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.209×, NCI-H2347 0.409×, SW 900 0.290×, SK-MEL-2 0.422×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (HOP62 0.0772×; ⚠ toxic); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.292×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.571×** | -9.3 | 7e-18 | 37/47 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.607×** | -8.0 | 4e-13 | 30/42 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -5.7 | 2e-06 | 25/45 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.803×** | -4.0 | 0.009 | 25/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.795×** | -3.7 | 0.025 | 20/50 (NCI-H596, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.736×** | -3.6 | 0.025 | 22/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.872× | -3.2 | 0.10 | 18/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.824× | -3.1 | 0.12 | 21/47 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.825× | -3.1 | 0.12 | 14/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.12 | 14/46 (Hs 766T, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.833× | -3.0 | 0.12 | 15/47 (HS-578T, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 55.2 | 6 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.481× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 89.8 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -11.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 28.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 70.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 5 µM 0.356× (z -11.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 72.1 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0772× (z -11.0) ⚠ toxic |
| [[HS-578T (line)]] | alt | 75.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.16× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 51.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.83× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 93.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 53.7 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.30× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 48.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.7× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 72.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 55.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.20× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 30.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -12.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 60.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1792 (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.342× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 63.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 54.5 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.292× (z -8.6) |
| [[SW 900 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM104A]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CEP170]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ECI2]] | +0.57 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[FAM117B]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[GRB2]] | +0.54 | +0.62 / +0.36 | both halves | 1e-04 |  |
| [[UBA6]] | +0.54 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[FXYD5]] | +0.54 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[TNFRSF10D]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SMAP2]] | +0.53 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[SLC46A3]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[HDAC3]] | +0.52 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[LPCAT2]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG1]] | -0.53 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[DIO2]] | -0.52 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[HECTD1]] | -0.50 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RNF115]] | -0.50 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[FKRP]] | -0.49 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[GTF2IRD2]] | -0.49 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[CUX1]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[NCOA5]] | -0.48 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[PPP3CB-AS1]] | -0.48 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[WARS2-AS1]] | -0.48 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[BRD1]] | -0.48 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[PSMD6-AS1]] | -0.47 | -0.53 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLS2]] | B | GLS2 activity lowers STX6's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.23× higher at baseline in the lines without GLS2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.8, 5.9); signed map (-4.7, 54.1). **Vector** length 101, 28.8% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.9 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | +0.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.4 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.5 | +2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:180,972,712-181,023,121 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Syntaxins |
| Reactome | 5 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [O43752](https://www.uniprot.org/uniprotkb/O43752) (Syntaxin-6):

> SNARE promoting movement of transport vesicles to target membranes. Targets endosomes to the trans-Golgi network, and may therefore function in retrograde trafficking. Together with SNARE STX12, promotes movement of vesicles from endosomes to the cell membrane, and may therefore function in the endocytic recycling pathway.

**Summary**, from NCBI Gene [10228](https://www.ncbi.nlm.nih.gov/gene/10228):

> Predicted to enable SNAP receptor activity and SNARE binding activity. Involved in regulation of protein localization; retrograde transport, endosome to Golgi; and vesicle fusion. Acts upstream of or within endocytic recycling. Located in early endosome; perinuclear region of cytoplasm; and trans-Golgi network. Part of SNARE complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11441) · Entrez [10228](https://www.ncbi.nlm.nih.gov/gene/10228) · UniProt [O43752](https://www.uniprot.org/uniprotkb/O43752) · Ensembl [ENSG00000135823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135823)

## Data

Gene col 5760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5760); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5760]; `tensor/DDL_lfc|DDL_z.npy` [5760]; `embed/gene_vectors.npy` [5760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5760 or target_col == 5760). Every well: [[STX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
