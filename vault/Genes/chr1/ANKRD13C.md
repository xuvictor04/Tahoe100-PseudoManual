---
symbol: "ANKRD13C"
type: "gene"
col: 3990
ensembl_id: "ENSG00000118454"
name: "ankyrin repeat domain 13C"
location: "1p31.1"
module: 198
arm: "+"
pooled_cpm: 94.48
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# ANKRD13C

*ankyrin repeat domain 13C* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.43× (z +12.6, q 1e-33, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.637× (z -10.9, q 4e-25, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.716× (z -8.4, q 7e-15, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO9]] (+0.65, fdr 7e-06), [[EBLN2]] (+0.58, fdr 1e-05), [[CWC15]] (+0.57, fdr 1e-05); moves opposite to [[RELT]] (-0.56, fdr 1e-05), [[NOTCH1]] (-0.54, fdr 4e-05), [[PLXNA1]] (-0.53, fdr 4e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.43×** | +12.6 | 1e-33 | 45/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +11.8 | 2e-29 | 34/48 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +8.6 | 1e-15 | 34/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +6.2 | 9e-08 | 29/48 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.9 | 4e-07 | 29/48 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +5.1 | 3e-05 | 30/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.9 | 9e-05 | 23/47 (C-33 A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.20×** | +4.6 | 3e-04 | 22/48 (HS-578T, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.20×** | +4.5 | 5e-04 | 24/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.4 | 7e-04 | 22/48 (BT-474, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.13× | +4.3 | 7e-04 | 16/48 (HS-578T, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +4.0 | 0.004 | 15/49 (HOP62, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.15× | +3.5 | 0.017 | 11/48 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.017 | 21/48 (NCI-H23, C-33 A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -10.9 | 4e-25 | 31/44 (SW48, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.686×** | -9.5 | 7e-19 | 33/49 (SNU-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.716×** | -8.4 | 7e-15 | 33/48 (Panc 03.27, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.703×** | -7.5 | 9e-12 | 36/45 (SW48, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | **0.779×** | -6.3 | 4e-08 | 32/48 (HS-578T, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.871× | -4.9 | 9e-05 | 16/49 (LoVo, A549, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.802×** | -4.0 | 0.006 | 19/48 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.872× | -3.5 | 0.039 | 9/48 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.829×** | -3.4 | 0.048 | 12/48 (NCI-H1792, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.835× | -3.3 | 0.065 | 17/47 (H4, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.882× | -3.2 | 0.072 | 8/47 (A-172, HS-578T, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.882× | -3.2 | 0.072 | 16/48 (RKO, HS-578T, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.840× | -3.1 | 0.072 | 14/48 (A-427, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 79.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +17.3) | — |
| [[H4 (line)]] | wt | 124 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +22.3) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -16.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 111 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.79× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 71.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -8.5) |
| [[HS-578T (line)]] | alt | 97.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.8) | [[Docetaxel (drug)]] 0.05 µM 0.491× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SW48 (line)]] | wt | 75.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -16.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 87.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.6) | — |
| [[LoVo (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -12.5) ⚠ cell-cycle shift, explains ~6% of this change |
| [[NCI-H2030 (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.467× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0823× (z -22.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 77.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -13.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 61.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -10.1) ⚠ cell-cycle shift, explains ~6% of this change |
| [[BT-474 (line)]] | alt | 70.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 55.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 89.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 82.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.607× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 121 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 93.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.90× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 93.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.421× (z -10.4) |
| [[RKO (line)]] | wt | 92.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 92.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 86.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -14.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 76.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.1) | — |
| [[SW 1271 (line)]] | alt | 89.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0926× (z -11.2) |
| [[SW1417 (line)]] | alt | 95.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.6) | — |
| [[A-427 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO9]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[EBLN2]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CWC15]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PRPF4B]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[TFCP2]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[RNF111]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[UBA3]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[STRN3]] | +0.52 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[GNPAT]] | +0.52 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[IWS1]] | +0.52 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CLPX]] | +0.51 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ZC3H13]] | +0.51 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELT]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[NOTCH1]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PLXNA1]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TUBB3]] | -0.52 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[FGFRL1]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[PLEKHO2]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[LINC01128]] | -0.49 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[GRK6]] | -0.48 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[EHD4]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ALDOA]] | -0.47 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PPP1CA]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ACTN1]] | -0.46 | -0.45 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.7, 15.7); signed map (-21.2, -10.1). **Vector** length 81.3, 17.9% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.0 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +12.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.0 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +8.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.2 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 13C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:70,258,999-70,354,734 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566D1346, dJ677H15.3 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6S4](https://www.uniprot.org/uniprotkb/Q8N6S4) (Ankyrin repeat domain-containing protein 13C):

> Acts as a molecular chaperone for G protein-coupled receptors, regulating their biogenesis and exit from the ER.

**Summary**, from NCBI Gene [81573](https://www.ncbi.nlm.nih.gov/gene/81573):

> Enables protein carrier activity and signaling receptor binding activity. Involved in cellular response to prostaglandin D stimulus; protein targeting to membrane; and regulation of anoikis. Located in endoplasmic reticulum and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25374) · Entrez [81573](https://www.ncbi.nlm.nih.gov/gene/81573) · UniProt [Q8N6S4](https://www.uniprot.org/uniprotkb/Q8N6S4) · Ensembl [ENSG00000118454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118454)

## Data

Gene col 3990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3990); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3990]; `tensor/DDL_lfc|DDL_z.npy` [3990]; `embed/gene_vectors.npy` [3990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3990 or target_col == 3990). Every well: [[ANKRD13C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD13C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
