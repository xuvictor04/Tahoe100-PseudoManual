---
symbol: "PLCB1"
type: "gene"
col: 11308
ensembl_id: "ENSG00000182621"
name: "phospholipase C beta 1"
location: "20p12.3"
module: 9
arm: "+"
pooled_cpm: 194.95
n_lines_expressing: 31
n_dd_up: 10
n_dd_down: 37
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PLCB1

*phospholipase C beta 1* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +11.4, q 2e-27, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (21 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.452× (z -17.4, q 0e+00, down in 28 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01611]] (+0.61, fdr 1e-05), [[ELAPOR2]] (+0.58, fdr 1e-05), [[SYT1]] (+0.56, fdr 3e-05); moves opposite to [[RARS2]] (-0.48, fdr 4e-05), [[RAB43]] (-0.46, fdr 7e-05), [[RECQL5]] (-0.46, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PPARGC1A]] → it (grade B ⚠); 6 go from it, the strongest it → [[GLDN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +11.4 | 2e-27 | 20/29 (J82, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.5 | 2e-08 | 21/30 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.009 | 17/29 (KATO III, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.009 | 17/29 (KATO III, SW480, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.014 | 13/30 (HT-29, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.014 | 15/28 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.014 | 15/29 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.015 | 5/30 (A-427, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.015 | 12/30 (SW480, SW48, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.042 | 12/29 (CHP-212, COLO 205, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.076 | 15/29 (KATO III, HS-578T, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.12 | 8/30 (A-427, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.452×** | -17.4 | 0e+00 | 28/30 (HepG2/C3A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.318×** | -9.3 | 5e-18 | 28/30 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -9.0 | 4e-17 | 24/28 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.578×** | -8.5 | 3e-15 | 26/29 (HT-29, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.592×** | -8.1 | 5e-14 | 18/29 (COLO 205, HT-29, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.623×** | -7.1 | 2e-10 | 24/29 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.728×** | -7.0 | 3e-10 | 21/29 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.640×** | -6.9 | 3e-10 | 18/29 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.665×** | -6.3 | 2e-08 | 19/29 (HT-29, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -6.3 | 2e-08 | 21/29 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.669×** | -6.2 | 3e-08 | 18/29 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.679×** | -6.0 | 1e-07 | 18/29 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -5.8 | 3e-07 | 20/29 (COLO 205, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.497×** | -5.7 | 6e-07 | 18/29 (LS 180, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.695×** | -5.4 | 2e-06 | 24/31 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.706×** | -5.4 | 3e-06 | 19/29 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -4.5 | 2e-04 | 22/29 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -4.2 | 8e-04 | 18/30 (HT-29, CHP-212, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.628×** | -3.8 | 0.004 | 18/29 (SHP-77, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.787×** | -3.7 | 0.004 | 14/28 (HT-29, LOX-IMVI, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.789×** | -3.5 | 0.008 | 14/29 (SW480, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.744×** | -3.3 | 0.019 | 10/29 (SW48, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.862× | -3.3 | 0.019 | 11/30 (LS 180, HEC-1-A, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.799×** | -3.2 | 0.021 | 13/28 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 379 | 0 | 21 (15 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.135× (z -20.4) |
| [[HT-29 (line)]] | alt | 169 | 0 | 14 (8 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.144× (z -19.0) |
| [[HepG2_C3A (line)]] | wt | 2,461 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -32.4) |
| [[SW480 (line)]] | alt | 103 | 2 | 10 (7 ⚠) | [[Binimetinib (drug)]] 0.05 µM 2.33× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.198× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 1,250 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -21.8) |
| [[LS 180 (line)]] | wt | 296 | 2 | 8 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -18.0) |
| [[LOX-IMVI (line)]] | wt | 312 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -18.7) |
| [[RPMI-7951 (line)]] | alt | 257 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 93.1 | 0 | 6 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.349× (z -11.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 98.8 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SW1417 (line)]] | alt | 97.1 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -11.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -11.2) |
| [[C32 (line)]] | wt | 384 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -16.8) |
| [[KATO III (line)]] | alt | 77.8 | 3 | 1 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 4.47× (z +11.3) | [[Digitoxin (drug)]] 0.5 µM 0.262× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 157 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.12× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -14.2) |
| [[A-427 (line)]] | wt | 104 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 121 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -11.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.141× (z -8.9) |
| [[SW 900 (line)]] | alt | 340 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -18.8) |
| [[CHP-212 (line)]] | wt | 435 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -11.3) |
| [[SHP-77 (line)]] | alt | 759 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -25.2) |
| [[SW48 (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.172× (z -9.2) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.195× (z -8.5) |
| [[BT-474 (line)]] | alt | 252 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.0) |
| [[HS-578T (line)]] | alt | 223 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -16.4) |
| [[hTERT-HPNE (line)]] | wt | 164 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -8.8) |
| [[A-172 (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 45.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 29.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 35.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.5 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 41.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01611]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ELAPOR2]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SYT1]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 | pathway: Neuronal System |
| [[TNFRSF19]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ADGRV1]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[LINC01748]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[CSRNP3]] | +0.53 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[ADGRL3]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[HS3ST5]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[AFF2]] | +0.53 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[CHRM3]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 | pathway: Acetylcholine regulates insulin secretion; STRING 607 |
| [[ARHGAP25]] | +0.51 | +0.41 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARS2]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[RAB43]] | -0.46 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[RECQL5]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[OGFOD1]] | -0.46 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[CDR2L]] | -0.45 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[TOP3A]] | -0.45 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[FBH1]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[SRD5A1]] | -0.45 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[ZFYVE21]] | -0.44 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[ZCCHC17]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[GLE1]] | -0.44 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[RNF139-DT]] | -0.43 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPARGC1A]] | B | PPARGC1A activity raises PLCB1's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 3.06× lower at baseline in the lines without PPARGC1A | 0.018 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[GLDN]] | B | GLDN activity raises PLCB1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without GLDN | 0.030 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[CSRNP3]] | B | CSRNP3 activity raises PLCB1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CSRNP3 | 0.032 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[PROX1]] | B | PROX1 activity raises PLCB1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without PROX1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[SYT1]] | B | SYT1 activity raises PLCB1's level | lines that do not express SYT1 (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without SYT1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EDIL3, LAYN, PRRX1 |
| [[ST18]] | B | ST18 activity raises PLCB1's level | lines that do not express ST18 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without ST18 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent |
| [[POU6F2]] | B | POU6F2 activity raises PLCB1's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 2.26× lower at baseline in the lines without POU6F2 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[ADGRV1]] | B | ADGRV1 activity raises PLCB1's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 3.01× lower at baseline in the lines without ADGRV1 | 0.087 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[CHN2]] | C | CHN2 activity raises PLCB1's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.57× lower at baseline in the lines without CHN2 | 0.052 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLDN]] | B | PLCB1 activity raises GLDN's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without PLCB1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[LINC02466]] | B | PLCB1 activity raises LINC02466's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without PLCB1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[DLEU1]] | B | PLCB1 activity raises DLEU1's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without PLCB1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[GRIK2]] | B | PLCB1 activity raises GRIK2's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 2.73× lower at baseline in the lines without PLCB1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[SYT1]] | B | PLCB1 activity raises SYT1's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without PLCB1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[CHN2]] | C | PLCB1 activity raises CHN2's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without PLCB1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 39.3); signed map (47.3, 37.2). **Vector** length 92.4, 24.6% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.7 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.1 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +9.5 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +4.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.0 | -5.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.3 | -4.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.1 | -3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.0 | +0.2 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:8,077,251-8,968,360 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0581, PLC-I, PLC154 |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 24 pathways, smallest: Fatty Acids bound to GPR40 (FFAR1) regulate insulin secretion; Acetylcholine regulates insulin secretion; Free fatty acids regulate insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ66](https://www.uniprot.org/uniprotkb/Q9NQ66) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase beta-1):

> Catalyzes the hydrolysis of 1-phosphatidylinositol 4,5-bisphosphate into diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3) and mediates intracellular signaling downstream of G protein-coupled receptors. Regulates the function of the endothelial barrier. Once activated by the GnRH receptor through GNAQ/GNA11 proteins, hydrolyzes phosphatidylinositol 4,5-bisphosphate (PIP2) into the second messengers inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) in pituitary gonadotrope …

**Summary**, from NCBI Gene [23236](https://www.ncbi.nlm.nih.gov/gene/23236):

> The protein encoded by this gene catalyzes the formation of inositol 1,4,5-trisphosphate and diacylglycerol from phosphatidylinositol 4,5-bisphosphate. This reaction uses calcium as a cofactor and plays an important role in the intracellular transduction of many extracellular signals. This gene is activated by two G-protein alpha subunits, alpha-q and alpha-11. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15917) · Entrez [23236](https://www.ncbi.nlm.nih.gov/gene/23236) · UniProt [Q9NQ66](https://www.uniprot.org/uniprotkb/Q9NQ66) · Ensembl [ENSG00000182621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182621)

## Data

Gene col 11308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11308); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11308]; `tensor/DDL_lfc|DDL_z.npy` [11308]; `embed/gene_vectors.npy` [11308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11308 or target_col == 11308). Every well: [[PLCB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
