---
symbol: "EPC2"
type: "gene"
col: 5796
ensembl_id: "ENSG00000135999"
name: "enhancer of polycomb 2"
location: "2q23.1"
module: 51
arm: "+"
pooled_cpm: 118.6
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# EPC2

*enhancer of polycomb 2* — 2q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +9.0, q 1e-16, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.253× (z -16.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF644]] (+0.81, fdr 7e-06), [[WARS2]] (+0.78, fdr 7e-06), [[INO80]] (+0.77, fdr 7e-06); moves opposite to [[HDAC3]] (-0.72, fdr 7e-06), [[PMS2P3-1]] (-0.69, fdr 7e-06), [[GMCL1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02656]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +9.0 | 1e-16 | 42/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.003 | 31/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.013 | 29/48 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +3.9 | 0.017 | 29/49 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.22×** | +3.4 | 0.066 | 26/48 (HEC-1-A, HT-29, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.60× | +3.0 | 0.23 | 31/49 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.253×** | -16.7 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.381×** | -16.6 | 0e+00 | 49/49 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.284×** | -15.3 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.304×** | -14.5 | 1e-45 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.386×** | -11.1 | 8e-27 | 47/50 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.412×** | -10.4 | 3e-23 | 45/48 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.443×** | -9.9 | 4e-21 | 48/48 (SW1417, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.447×** | -9.8 | 8e-21 | 47/48 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.465×** | -9.3 | 8e-19 | 47/49 (HCT15, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.475×** | -9.1 | 8e-18 | 44/48 (SW480, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.476×** | -8.7 | 2e-16 | 38/44 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.583×** | -6.3 | 1e-08 | 39/47 (NCI-H1792, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.385×** | -6.1 | 6e-08 | 46/49 (SNU-1, COLO 205, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.543×** | -5.9 | 2e-07 | 37/45 (AN3 CA, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.746×** | -5.0 | 2e-05 | 37/48 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.003 | 30/48 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.757×** | -3.4 | 0.022 | 27/49 (Hs 766T, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.593×** | -3.3 | 0.026 | 33/48 (CFPAC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.755×** | -3.3 | 0.028 | 33/49 (C-33 A, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 109 | 3 | 8 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.76× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.242× (z -12.6) |
| [[SW480 (line)]] | alt | 143 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -19.2) |
| [[PANC-1 (line)]] | alt | 133 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 10 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 177 | 0 | 9 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -15.9) |
| [[HOP62 (line)]] | alt | 122 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 150 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 147 | 1 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 110 | 1 | 8 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.201× (z -14.6) |
| [[RKO (line)]] | wt | 145 | 1 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -17.1) |
| [[A-427 (line)]] | wt | 122 | 1 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.313× (z -12.1) |
| [[KATO III (line)]] | alt | 90.3 | 1 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 142 | 1 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -17.7) |
| [[MIA PaCa-2 (line)]] | alt | 88.1 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 96.1 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0938× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.226× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 128 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -17.4) |
| [[C-33 A (line)]] | alt | 153 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -13.8) |
| [[HepG2_C3A (line)]] | wt | 200 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -14.8) |
| [[HT-29 (line)]] | alt | 140 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -14.7) |
| [[LS 180 (line)]] | wt | 109 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.333× (z -11.2) |
| [[SNU-1 (line)]] | wt | 141 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.251× (z -11.9) |
| [[SNU-423 (line)]] | alt | 106 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -12.9) |
| [[SW 900 (line)]] | alt | 178 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -13.0) |
| [[A498 (line)]] | wt | 84.6 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.268× (z -12.2) |
| [[COLO 205 (line)]] | alt | 139 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.151× (z -16.8) |
| [[HCT15 (line)]] | alt | 129 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0386× (z -28.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.284× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 90.3 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -14.2) |
| [[SK-MEL-2 (line)]] | alt | 112 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -12.1) |
| [[SW48 (line)]] | wt | 106 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -13.7) |
| [[A-172 (line)]] | wt | 85.9 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 123 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -16.0) |
| [[BT-474 (line)]] | alt | 93.2 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.229× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 60.7 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.0) |
| [[SW1417 (line)]] | alt | 144 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -14.1) |
| [[A549 (line)]] | wt | 117 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -10.8) |
| [[AN3 CA (line)]] | alt | 136 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0961× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -9.7) |
| [[J82 (line)]] | alt | 129 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -12.9) |
| [[SHP-77 (line)]] | alt | 65.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -10.5) |
| [[H4 (line)]] | wt | 129 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.2) |
| [[Hs 766T (line)]] | wt | 49.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.249× (z -10.6) |
| [[LoVo (line)]] | wt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -12.2) |
| [[CHP-212 (line)]] | wt | 121 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -12.3) |
| [[HS-578T (line)]] | alt | 66.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -11.8) |
| [[SW 1088 (line)]] | alt | 112 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0575× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 86.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 1271 (line)]] | alt | 152 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -9.9) |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF644]] | +0.81 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[WARS2]] | +0.78 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[INO80]] | +0.77 | +0.70 / +0.77 | both halves | 7e-06 | STRING 563 |
| [[RBM23]] | +0.74 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[COQ7]] | +0.74 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ZNF414]] | +0.73 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.73 | +0.85 / +0.57 | both halves | 8e-06 |  |
| [[TRMO]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[EPC1]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 | same gene group; STRING 809 |
| [[SRCAP]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[TAF2]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC3]] | -0.72 | -0.58 / -0.73 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | -0.69 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.67 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[HEBP1]] | -0.66 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[PIGF]] | -0.65 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[ATP7B]] | -0.64 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[NAPB]] | -0.64 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[UBTD1]] | -0.64 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.63 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[USP3]] | -0.63 | -0.65 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02656]] | C | LINC02656 activity raises EPC2's level | lines that do not express LINC02656 (4) vs lines expressing it (46) | 1.24× lower at baseline in the lines without LINC02656 | 0.052 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, MAP3K8, ENSG00000250842; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.828). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.2, 11.6); signed map (12.1, -30.8). **Vector** length 128, 53.6% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.8 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.9 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.0 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +7.4 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.2 | -2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.5 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.2 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.5 | +1.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +3.1 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.6 | -9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.0 | -9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -10.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -5.4 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.3 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | enhancer of polycomb 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.1 — chr2:148,644,440-148,787,569 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566F2124 |
| Gene groups (HGNC) | Tip60/Nua4 histone acetyltransferase complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q52LR7](https://www.uniprot.org/uniprotkb/Q52LR7) (Enhancer of polycomb homolog 2):

> May play a role in transcription or DNA repair.

**Summary**, from NCBI Gene [26122](https://www.ncbi.nlm.nih.gov/gene/26122):

> Predicted to enable protein-macromolecule adaptor activity. Involved in positive regulation of double-strand break repair via homologous recombination and regulation of cell cycle. Predicted to be located in nucleus. Predicted to be part of NuA4 histone acetyltransferase complex and piccolo histone acetyltransferase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24543) · Entrez [26122](https://www.ncbi.nlm.nih.gov/gene/26122) · UniProt [Q52LR7](https://www.uniprot.org/uniprotkb/Q52LR7) · Ensembl [ENSG00000135999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135999)

## Data

Gene col 5796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5796); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5796]; `tensor/DDL_lfc|DDL_z.npy` [5796]; `embed/gene_vectors.npy` [5796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5796 or target_col == 5796). Every well: [[EPC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
