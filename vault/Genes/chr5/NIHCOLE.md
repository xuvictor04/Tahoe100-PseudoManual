---
symbol: "NIHCOLE"
type: "gene"
col: 14729
ensembl_id: "ENSG00000251026"
name: "ncRNA involved in NHEJ oncogenic ligation efficiency"
location: "5q21.2"
module: 27
arm: "+"
pooled_cpm: 352.02
n_lines_expressing: 28
n_dd_up: 8
n_dd_down: 59
n_dd_up_clean: 7
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 10
direction_downstream: 21
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# NIHCOLE

*ncRNA involved in NHEJ oncogenic ligation efficiency* — 5q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.41× (z +5.1, q 2e-04, up in 21 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 59 drug-doses (26 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.214× (z -23.8, q 0e+00, down in 26 of 26 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.395× (z -20.2, q 0e+00, down in 27 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01748]] (+0.70, fdr 7e-06), [[FAAH2]] (+0.67, fdr 7e-06), [[LINC01876]] (+0.66, fdr 1e-05); moves opposite to [[ABCC10]] (-0.50, fdr 2e-05), [[CDR2L]] (-0.48, fdr 4e-05), [[MON1A]] (-0.47, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[BANK1]] → it (grade B ⚠); 21 go from it, the strongest it → [[BANK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +5.1 | 2e-04 | 21/25 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.68×** | +4.2 | 0.006 | 18/28 (HEC-1-A, A-427, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.006 | 20/25 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.006 | 14/26 (KATO III, A-427, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.049 | 14/26 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.052 | 15/26 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.26×** | +3.4 | 0.053 | 16/28 (LoVo, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.065 | 13/26 (LoVo, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.069 | 15/27 (LoVo, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.11 | 12/27 (SW48, Hs 766T, …) | all doses, flat |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.12 | 8/27 (HCT15, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.12 | 12/26 (SNU-423, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 27 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 59 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 26 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14729.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.214×** | -23.8 | 0e+00 | 26/26 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.233×** | -22.5 | 0e+00 | 26/26 (HCT15, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.395×** | -20.2 | 0e+00 | 27/27 (HepG2/C3A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.294×** | -18.9 | 0e+00 | 26/26 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.421×** | -18.8 | 0e+00 | 25/26 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.358×** | -15.8 | 0e+00 | 25/26 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.358×** | -15.2 | 0e+00 | 25/25 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.163×** | -14.6 | 0e+00 | 27/27 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.429×** | -13.0 | 6e-37 | 24/26 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.219×** | -12.2 | 1e-32 | 26/26 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.454×** | -12.1 | 4e-32 | 25/26 (HT-29, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.459×** | -11.5 | 4e-29 | 23/26 (SK-MEL-2, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.490×** | -11.0 | 3e-26 | 24/26 (HT-29, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.494×** | -10.9 | 7e-26 | 23/26 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.500×** | -10.7 | 6e-25 | 24/26 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.485×** | -10.5 | 3e-24 | 25/26 (HT-29, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -7.0 | 6e-11 | 19/26 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.424×** | -6.9 | 1e-10 | 19/27 (HepG2/C3A, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.699×** | -5.5 | 8e-07 | 22/26 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.721×** | -4.8 | 2e-05 | 16/25 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.726×** | -4.7 | 4e-05 | 15/26 (NCI-H23, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.569×** | -4.5 | 1e-04 | 21/26 (HEC-1-A, LoVo, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.72 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 562 | 0 | 27 (18 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -25.3) |
| [[SK-MEL-2 (line)]] | alt | 1,361 | 0 | 26 (17 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.1000× (z -27.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -23.6) |
| [[HT-29 (line)]] | alt | 427 | 0 | 25 (17 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.152× (z -20.1) |
| [[SW480 (line)]] | alt | 560 | 0 | 24 (16 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0753× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -20.8) |
| [[NCI-H23 (line)]] | alt | 654 | 0 | 21 (16 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.102× (z -19.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.230× (z -12.5) |
| [[COLO 205 (line)]] | alt | 2,230 | 0 | 19 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -25.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0541× (z -16.4) |
| [[SW48 (line)]] | wt | 920 | 0 | 19 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -17.3) |
| [[HCT15 (line)]] | alt | 694 | 0 | 18 (13 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0894× (z -23.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 2,733 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -29.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -22.5) |
| [[RPMI-7951 (line)]] | alt | 331 | 0 | 18 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -19.2) |
| [[SNU-423 (line)]] | alt | 182 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -21.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -14.2) |
| [[H4 (line)]] | wt | 389 | 0 | 16 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -20.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -13.9) |
| [[Hs 766T (line)]] | wt | 382 | 0 | 16 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -23.6) |
| [[LoVo (line)]] | wt | 469 | 0 | 16 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 814 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -23.6) |
| [[KATO III (line)]] | alt | 202 | 3 | 12 (6 ⚠) | [[Ponatinib (drug)]] 5 µM 2.92× (z +10.2) | [[Auranofin (drug)]] 5 µM 0.283× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 551 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -29.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -20.6) |
| [[A-427 (line)]] | wt | 283 | 1 (1 ⚠) | 12 (8 ⚠) | [[Selinexor (drug)]] 5 µM 1.74× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.259× (z -14.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.149× (z -10.7) |
| [[SW1417 (line)]] | alt | 218 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.7) |
| [[AN3 CA (line)]] | alt | 341 | 0 | 8 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0984× (z -16.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0327× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 137 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -21.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.9) |
| [[SHP-77 (line)]] | alt | 310 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -18.9) |
| [[A-172 (line)]] | wt | 1,398 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -15.9) |
| [[A498 (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 60.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 51.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 60.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 31.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 71.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 34.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 45.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 45.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 34.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 520 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.7 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 54.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 34.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 37.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 41.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01748]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[FAAH2]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[LINC01876]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[LINC02253]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[DLEU1]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 | same gene group |
| [[LINC00299]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RHOXF1-AS1]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LINC02315]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[AXIN2]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PKHD1]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC10]] | -0.50 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[CDR2L]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[MON1A]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[LPCAT1]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[AP1M1]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MPP3]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[LIMK1]] | -0.45 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[GNA12]] | -0.45 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[FAM124A]] | -0.45 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[NT5M]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MAD1L1]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[BVES]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BANK1]] | B | BANK1 activity raises NIHCOLE's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 3.62× lower at baseline in the lines without BANK1 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BVES]] | B | BVES activity lowers NIHCOLE's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.09× higher at baseline in the lines without BVES | 0.068 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[LINC02050]] | B | LINC02050 activity raises NIHCOLE's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 2.45× lower at baseline in the lines without LINC02050 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1 |
| [[LIPC]] | C | LIPC activity raises NIHCOLE's level | lines that do not express LIPC (18) vs lines expressing it (32) | 3.47× lower at baseline in the lines without LIPC | 0.009 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent; co-absent with the target |
| [[TRPM2-AS]] | C | TRPM2-AS activity raises NIHCOLE's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without TRPM2-AS | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1; co-absent with the target |
| [[LINC02428]] | C | LINC02428 activity raises NIHCOLE's level | lines that do not express LINC02428 (32) vs lines expressing it (18) | 3.19× lower at baseline in the lines without LINC02428 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ENSG00000287598, ENSG00000287474; co-absent with the target |
| [[PROM1]] | C | PROM1 activity raises NIHCOLE's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.57× lower at baseline in the lines without PROM1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |
| [[LINC01748]] | C | LINC01748 activity raises NIHCOLE's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 3.53× lower at baseline in the lines without LINC01748 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3; co-absent with the target |
| [[LINC02315]] | C | LINC02315 activity raises NIHCOLE's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without LINC02315 | 0.078 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises NIHCOLE's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without F11-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 13, C 8. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BANK1]] | B | NIHCOLE activity raises BANK1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 2.13× lower at baseline in the lines without NIHCOLE | 0.023 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[SORL1]] | B | NIHCOLE activity raises SORL1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without NIHCOLE | 0.038 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[TSPOAP1-AS1]] | B | NIHCOLE activity raises TSPOAP1-AS1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.47× lower at baseline in the lines without NIHCOLE | 0.040 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[KIF6]] | B | NIHCOLE activity raises KIF6's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without NIHCOLE | 0.043 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[BCAR3-AS1]] | B | NIHCOLE activity raises BCAR3-AS1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without NIHCOLE | 0.044 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[LINC02254]] | B | NIHCOLE activity raises LINC02254's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without NIHCOLE | 0.054 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[LINC00491]] | B | NIHCOLE activity raises LINC00491's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without NIHCOLE | 0.056 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[ABL1]] | B | NIHCOLE activity lowers ABL1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.39× higher at baseline in the lines without NIHCOLE | 0.073 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[DNAH7]] | B | NIHCOLE activity raises DNAH7's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without NIHCOLE | 0.075 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[KCNMB2-AS1]] | B | NIHCOLE activity strengthens KCNMB2-AS1's drug response | lines that do not express NIHCOLE (13) vs lines expressing it (21) | the lines without NIHCOLE respond 1.05× as strongly (z diff -0.28); strongest at Digitoxin 5 µM: 0.88x vs 0.32x (z diff +5.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1; target measured in part of the lines; both ways; artifact flags |
| [[DIP2C-AS1]] | B | NIHCOLE activity raises DIP2C-AS1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without NIHCOLE | 0.087 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[LPCAT1]] | B | NIHCOLE activity lowers LPCAT1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.18× higher at baseline in the lines without NIHCOLE | 0.092 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.5, 46.4); signed map (58.4, 15.3). **Vector** length 99.0, 31.2% of its response variance represented; |z| ≥ 3 in 1,418 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +6.4 | -10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.4 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +6.3 | -8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.3 | -9.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.3 | -11.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.2 | -8.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -8.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.7 | -4.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.1 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -5.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | ncRNA involved in NHEJ oncogenic ligation efficiency |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q21.2 — chr5:104,079,847-104,406,121 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-138J23.1; previously LINC02163 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53024) · Entrez [107986389](https://www.ncbi.nlm.nih.gov/gene/107986389) · Ensembl [ENSG00000251026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251026)

## Data

Gene col 14729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14729); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14729]; `tensor/DDL_lfc|DDL_z.npy` [14729]; `embed/gene_vectors.npy` [14729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14729 or target_col == 14729). Every well: [[NIHCOLE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIHCOLE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
