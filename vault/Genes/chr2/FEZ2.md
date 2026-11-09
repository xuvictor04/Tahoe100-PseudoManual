---
symbol: "FEZ2"
type: "gene"
col: 10044
ensembl_id: "ENSG00000171055"
name: "fasciculation and elongation protein zeta 2"
location: "2p22.2"
module: 116
arm: "+"
pooled_cpm: 141.67
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# FEZ2

*fasciculation and elongation protein zeta 2* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.45× (z +9.4, q 3e-18, up in 33 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.24× (z +5.5, q 8e-06, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.670× (z -14.4, q 6e-44, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB3B]] (+0.56, fdr 1e-05), [[MARCHF4]] (+0.53, fdr 2e-05), [[DENR]] (+0.52, fdr 1e-05); moves opposite to [[THBS3-AS1]] (-0.48, fdr 4e-05), [[HIPK1]] (-0.45, fdr 6e-05), [[NSD3]] (-0.44, fdr 2e-04).
> It is in [[Module 116]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +9.4 | 3e-18 | 33/49 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +7.1 | 4e-10 | 30/44 (SHP-77, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +5.5 | 8e-06 | 27/48 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.7 | 3e-04 | 28/47 (A-427, A549, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.004 | 22/46 (LS 180, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.16× | +3.8 | 0.012 | 14/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.7 | 0.017 | 5/49 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.026 | 21/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.15× | +3.5 | 0.030 | 17/48 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.035 | 16/48 (MIA PaCa-2, A-172, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.036 | 18/47 (AsPC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.044 | 12/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.090 | 18/48 (C-33 A, SW1417, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.13× | +3.1 | 0.090 | 15/47 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Radotinib (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.090 | 5/48 (NCI-H2030, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.670×** | -14.4 | 6e-44 | 35/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.589×** | -7.0 | 4e-10 | 33/48 (LoVo, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.590×** | -7.0 | 4e-10 | 35/49 (AsPC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.759×** | -7.0 | 4e-10 | 35/48 (LoVo, C32, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -5.3 | 1e-05 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.823×** | -4.9 | 8e-05 | 21/48 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | **0.832×** | -4.7 | 3e-04 | 24/48 (LoVo, A-427, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.835× | -4.5 | 4e-04 | 23/48 (A-427, NCI-H460, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.732×** | -4.1 | 0.002 | 19/49 (NCI-H460, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.849× | -4.0 | 0.004 | 22/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.895× | -3.9 | 0.004 | 17/49 (RKO, PANC-1, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.859× | -3.8 | 0.006 | 10/48 (SHP-77, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.853× | -3.6 | 0.011 | 18/50 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.866× | -3.6 | 0.011 | 20/48 (RKO, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.772×** | -3.4 | 0.023 | 20/49 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.792×** | -3.1 | 0.065 | 9/49 (RPMI-7951, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.796×** | -3.0 | 0.072 | 12/49 (HOP62, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 204 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -27.8) |
| [[RKO (line)]] | wt | 397 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -23.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.446× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 202 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +11.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 207 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -20.8) |
| [[A-427 (line)]] | wt | 319 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.476× (z -11.0) ⚠ cell-cycle shift, explains ~14% of this change |
| [[AsPC-1 (line)]] | alt | 202 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -13.8) |
| [[HOP62 (line)]] | alt | 121 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.617× (z -10.1) |
| [[J82 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.471× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.531× (z -10.4) |
| [[LoVo (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.492× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 98.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.569× (z -8.6) |
| [[A498 (line)]] | wt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +10.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 181 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 174 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -20.5) |
| [[NCI-H1792 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 189 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -23.2) |
| [[NCI-H23 (line)]] | alt | 145 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 83.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -13.6) |
| [[SHP-77 (line)]] | alt | 66.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 87.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 253 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 232 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 169 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 86.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3B]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[DENR]] | +0.52 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[BCAR3]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[KIFC3]] | +0.51 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MEAK7]] | +0.51 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ESM1]] | +0.50 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[PDCD1LG2]] | +0.49 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[BCLAF3]] | +0.48 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[ARHGAP29]] | +0.48 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[BTBD10]] | +0.48 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[MICU2]] | +0.47 | +0.51 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THBS3-AS1]] | -0.48 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[HIPK1]] | -0.45 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[NSD3]] | -0.44 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[SP1]] | -0.44 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[AK7]] | -0.43 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[CDKN1B]] | -0.43 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[CPLX2]] | -0.42 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[SNED1-AS1]] | -0.41 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CNOT1]] | -0.41 | -0.38 / -0.32 | both halves | 1e-04 |  |
| [[DVL2]] | -0.40 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[LY6E-DT]] | -0.40 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[APOLD1]] | -0.40 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.9, 10.7); signed map (12.5, 44.0). **Vector** length 100.0, 25.4% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.2 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.0 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | fasciculation and elongation protein zeta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:36,531,805-36,646,087 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fasciculation and elongation protein zeta family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHY8](https://www.uniprot.org/uniprotkb/Q9UHY8) (Fasciculation and elongation protein zeta-2):

> Involved in axonal outgrowth and fasciculation.

**Summary**, from NCBI Gene [9637](https://www.ncbi.nlm.nih.gov/gene/9637):

> This gene is an ortholog of the C. elegans unc-76 gene, which is necessary for normal axonal bundling and elongation within axon bundles. Other orthologs include the rat gene that encodes zygin II, which can bind to synaptotagmin. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3660) · Entrez [9637](https://www.ncbi.nlm.nih.gov/gene/9637) · UniProt [Q9UHY8](https://www.uniprot.org/uniprotkb/Q9UHY8) · Ensembl [ENSG00000171055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171055)

## Data

Gene col 10044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10044); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10044]; `tensor/DDL_lfc|DDL_z.npy` [10044]; `embed/gene_vectors.npy` [10044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10044 or target_col == 10044). Every well: [[FEZ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FEZ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
