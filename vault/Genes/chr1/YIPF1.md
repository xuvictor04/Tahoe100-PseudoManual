---
symbol: "YIPF1"
type: "gene"
col: 667
ensembl_id: "ENSG00000058799"
name: "Yip1 domain family member 1"
location: "1p32.3"
module: 68
arm: "-"
pooled_cpm: 17.89
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# YIPF1

*Yip1 domain family member 1* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.09× (z +14.0, q 1e-41, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.474× (z -21.0, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.495× (z -14.0, q 5e-42, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIKFYVE]] (+0.68, fdr 7e-06), [[RNF41]] (+0.66, fdr 2e-05), [[ZCCHC17]] (+0.64, fdr 1e-05); moves opposite to [[ANKRD18B]] (-0.65, fdr 4e-05), [[MZF1-AS1]] (-0.63, fdr 2e-04), [[ANKRD18A]] (-0.63, fdr 5e-05).
> It sits in the **-** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +14.0 | 1e-41 | 41/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +9.9 | 1e-20 | 33/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +7.7 | 2e-12 | 27/47 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.4 | 1e-05 | 16/48 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.26×** | +4.3 | 0.002 | 17/47 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.015 | 3/47 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.075 | 6/47 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.14 | 9/46 (SW480, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 667.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.474×** | -21.0 | 0e+00 | 39/47 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.460×** | -14.8 | 0e+00 | 36/47 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.495×** | -14.0 | 5e-42 | 34/47 (HCT15, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.563×** | -11.4 | 4e-28 | 33/45 (LoVo, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.586×** | -10.6 | 3e-24 | 34/48 (LoVo, H4, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -10.4 | 3e-23 | 37/47 (NCI-H2030, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -9.8 | 8e-21 | 31/44 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.390×** | -9.8 | 9e-21 | 31/45 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -8.2 | 1e-14 | 29/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.652×** | -8.0 | 5e-14 | 27/48 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -7.3 | 2e-11 | 24/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.678×** | -7.1 | 8e-11 | 22/37 (NCI-H2030, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.698×** | -6.8 | 6e-10 | 24/47 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.730×** | -6.2 | 2e-08 | 22/41 (NCI-H1573, A-427, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -4.1 | 0.002 | 18/47 (A-427, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.680×** | -4.0 | 0.002 | 10/44 (HCT15, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.687×** | -3.9 | 0.003 | 14/47 (LOX-IMVI, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.832×** | -3.6 | 0.008 | 15/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.837× | -3.4 | 0.020 | 9/48 (A498, NCI-H1792, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.723×** | -3.4 | 0.020 | 11/44 (A549, RKO, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.837× | -3.3 | 0.022 | 9/48 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.731×** | -3.2 | 0.026 | 8/46 (HepG2/C3A, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.035 | 9/48 (Hs 766T, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.744×** | -3.1 | 0.044 | 11/45 (COLO 205, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.857× | -2.9 | 0.065 | 6/47 (Hs 766T, LS 180, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.818×** | -2.8 | 0.085 | 4/48 (NCI-H661, RKO, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 26.5 | 0 | 5 (3 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0996× (z -12.1) |
| [[A-427 (line)]] | wt | 22.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -15.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -11.3) |
| [[LoVo (line)]] | wt | 14.1 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -17.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -13.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 17.6 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.276× (z -9.5) ⚠ cell-cycle shift, explains ~96% of this change |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 17.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.325× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 25.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0427× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0867× (z -11.4) |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.196× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0720× (z -12.9) |
| [[J82 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0583× (z -19.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.247× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.208× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIKFYVE]] | +0.68 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[RNF41]] | +0.66 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ZCCHC17]] | +0.64 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.63 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[CALCOCO2]] | +0.63 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[SLC9A6]] | +0.61 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[TANGO2]] | +0.61 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[USP35]] | +0.61 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[INPP5B]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[TECPR1]] | +0.61 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[VRK3]] | +0.61 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[FBXW2]] | +0.59 | +0.61 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18B]] | -0.65 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MZF1-AS1]] | -0.63 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[ANKRD18A]] | -0.63 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[LEKR1]] | -0.63 | -0.65 / -0.32 | both halves | 1e-04 |  |
| [[WARS2-AS1]] | -0.62 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[PCNX4-DT]] | -0.62 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[APLF]] | -0.62 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[ZNF462]] | -0.62 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[SEPTIN7-DT]] | -0.62 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[PATL2]] | -0.61 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[NANOS3]] | -0.61 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[ANKRD31]] | -0.61 | -0.64 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers YIPF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **-** arm (projection on the module's main direction -0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (0.5, -2.7); signed map (-35.8, -1.0). **Vector** length 75.0, 13.7% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +14.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | +5.1 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +9.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.2 | -0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.1 | -21.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.6 | -14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -14.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -3.5 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -9.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 domain family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,851,719-53,889,798 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DJ167A19.1, FinGER1, Yip5a, YIPFbeta3A |
| Gene groups (HGNC) | Yip1 domain containing |
| Matched by | ensembl_id |

UniProt [Q9Y548](https://www.uniprot.org/uniprotkb/Q9Y548) carries no function annotation.

**Summary**, from NCBI Gene [54432](https://www.ncbi.nlm.nih.gov/gene/54432):

> Predicted to enable small GTPase binding activity. Predicted to be involved in vesicle-mediated transport. Located in Golgi apparatus and transport vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25231) · Entrez [54432](https://www.ncbi.nlm.nih.gov/gene/54432) · UniProt [Q9Y548](https://www.uniprot.org/uniprotkb/Q9Y548) · Ensembl [ENSG00000058799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058799)

## Data

Gene col 667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 667); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 667]; `tensor/DDL_lfc|DDL_z.npy` [667]; `embed/gene_vectors.npy` [667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 667 or target_col == 667). Every well: [[YIPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
