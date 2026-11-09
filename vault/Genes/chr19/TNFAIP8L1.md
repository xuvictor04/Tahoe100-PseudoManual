---
symbol: "TNFAIP8L1"
type: "gene"
col: 11669
ensembl_id: "ENSG00000185361"
name: "TNF alpha induced protein 8 like 1"
location: "19p13.3"
module: 85
arm: "+"
pooled_cpm: 10.22
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 32
n_dd_up_clean: 14
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# TNFAIP8L1

*TNF alpha induced protein 8 like 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.60× (z +11.4, q 2e-27, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.443× (z -13.7, q 3e-40, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNF]] (+0.76, fdr 7e-06), [[GPSM2]] (+0.72, fdr 1e-05), [[SAPCD2]] (+0.69, fdr 1e-05); moves opposite to [[EFCAB2]] (-0.65, fdr 1e-04), [[VPS52]] (-0.65, fdr 4e-05), [[PBLD]] (-0.64, fdr 0.001, ⚠ one half only (not replicated)), [[DECR1]] (-0.63, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[THRB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.60×** | +11.4 | 2e-27 | 41/46 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.49×** | +10.9 | 3e-25 | 41/46 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +10.7 | 2e-24 | 38/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.93×** | +7.9 | 4e-13 | 30/39 (NCI-H2030, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +6.3 | 3e-08 | 25/46 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.3 | 8e-06 | 22/47 (A498, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +5.1 | 3e-05 | 18/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +4.4 | 8e-04 | 8/45 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.014 | 9/46 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.015 | 11/46 (A549, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.020 | 13/47 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.024 | 11/42 (HepG2/C3A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.026 | 10/47 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.067 | 4/43 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.1 | 0.069 | 10/45 (NCI-H23, HS-578T, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.080 | 9/43 (RPMI-7951, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11669.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.443×** | -13.7 | 3e-40 | 39/45 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.502×** | -11.6 | 7e-29 | 32/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.466×** | -9.1 | 1e-17 | 30/44 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.467×** | -8.8 | 3e-16 | 29/45 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -7.7 | 2e-12 | 31/44 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.529×** | -7.3 | 3e-11 | 31/44 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.557×** | -7.0 | 2e-10 | 30/46 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.608×** | -5.9 | 2e-07 | 20/34 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.635×** | -5.4 | 4e-06 | 21/46 (SW480, A-172, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.654×** | -5.1 | 2e-05 | 21/46 (J82, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.656×** | -5.0 | 2e-05 | 22/46 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.645×** | -5.0 | 2e-05 | 19/45 (C32, SW48, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.661×** | -4.9 | 4e-05 | 22/46 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -4.7 | 1e-04 | 21/46 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.680×** | -4.6 | 2e-04 | 19/46 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.482×** | -4.6 | 2e-04 | 17/45 (LOX-IMVI, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.775×** | -4.3 | 5e-04 | 20/47 (A-427, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.507×** | -4.2 | 6e-04 | 18/41 (LS 180, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.720×** | -3.9 | 0.002 | 10/46 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.762×** | -3.2 | 0.029 | 11/46 (HS-578T, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.780×** | -3.0 | 0.062 | 17/46 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -14.2) |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -14.5) |
| [[SW480 (line)]] | alt | 11.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0963× (z -19.4) |
| [[PANC-1 (line)]] | alt | 7.76 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -12.2) |
| [[A-427 (line)]] | wt | 22.0 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.291× (z -10.0) |
| [[C32 (line)]] | wt | 5.31 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0570× (z -9.0) ⚠ cell-cycle shift, explains ~59% of this change |
| [[H4 (line)]] | wt | 13.1 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0942× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.7) |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 6.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -8.7) |
| [[J82 (line)]] | alt | 8.62 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -8.5) |
| [[LoVo (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 9.62 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0625× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -8.8) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNF]] | +0.76 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[GPSM2]] | +0.72 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[SAPCD2]] | +0.69 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PAK4]] | +0.68 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SLC27A1]] | +0.66 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[PSRC1]] | +0.65 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[NEURL1B]] | +0.64 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[MAST3]] | +0.63 | +0.53 / +0.28 | both halves | 3e-04 |  |
| [[DNAAF3]] | +0.62 | +0.43 / +0.30 | both halves | 2e-04 |  |
| [[ANKRD27]] | +0.62 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[PBX4]] | +0.61 | +0.52 / +0.33 | both halves | 1e-04 |  |
| [[KIAA1328]] | +0.61 | +0.51 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.65 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[VPS52]] | -0.65 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[PBLD]] | -0.64 | -0.53 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[DECR1]] | -0.63 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.63 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PEF1]] | -0.61 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[IRAK4]] | -0.61 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MFF-DT]] | -0.60 | -0.47 / -0.08 | ⚠ not reproduced | 0.003 |  |
| [[PNISR-AS1]] | -0.60 | -0.47 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[C8orf33]] | -0.60 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.60 | -0.51 / -0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[MMADHC-DT]] | -0.59 | -0.53 / -0.01 | ⚠ one half (not replicated) | 0.008 |  |
| [[SETD7]] | -0.59 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[CRPPA]] | -0.59 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[RNF6]] | -0.59 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[ARFGAP2]] | -0.59 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[UBE3B]] | -0.59 | -0.53 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THRB]] | B | THRB activity lowers TNFAIP8L1's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.63× higher at baseline in the lines without THRB | 0.008 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[FCHO1]] | B | FCHO1 activity raises TNFAIP8L1's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without FCHO1 | 0.034 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TNFAIP8L1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-34.9, -59.2); signed map (-51.0, -39.0). **Vector** length 110, 27.3% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.5 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.0 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.8 | +11.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.6 | +5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +0.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -13.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.5 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -4.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | TNF alpha induced protein 8 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,639,516-4,655,568 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17791; previously TNFAIP8L1 |
| Gene groups (HGNC) | TIPE family |
| Reactome | 3 pathways, smallest: PI Metabolism; Phospholipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVP5](https://www.uniprot.org/uniprotkb/Q8WVP5) (Tumor necrosis factor alpha-induced protein 8-like protein 1):

> Acts as a negative regulator of mTOR activity.

**Summary**, from NCBI Gene [126282](https://www.ncbi.nlm.nih.gov/gene/126282):

> Enables identical protein binding activity. Predicted to be involved in negative regulation of TOR signaling. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28279) · Entrez [126282](https://www.ncbi.nlm.nih.gov/gene/126282) · UniProt [Q8WVP5](https://www.uniprot.org/uniprotkb/Q8WVP5) · Ensembl [ENSG00000185361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185361)

## Data

Gene col 11669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11669); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11669]; `tensor/DDL_lfc|DDL_z.npy` [11669]; `embed/gene_vectors.npy` [11669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11669 or target_col == 11669). Every well: [[TNFAIP8L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFAIP8L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
