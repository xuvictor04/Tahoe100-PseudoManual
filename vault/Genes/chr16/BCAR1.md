---
symbol: "BCAR1"
type: "gene"
col: 572
ensembl_id: "ENSG00000050820"
name: "BCAR1 scaffold protein, Cas family member"
location: "16q23.1"
module: 29
arm: "-"
pooled_cpm: 42.98
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# BCAR1

*BCAR1 scaffold protein, Cas family member* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +7.5, q 3e-11, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (HepG2/C3A 2.71×, AsPC-1 2.40×, RPMI-7951 3.02×, A549 2.36×, …).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.394× (z -15.8, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.636× (z -8.0, q 2e-13, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL6]] (+0.60, fdr 2e-05), [[STK10]] (+0.60, fdr 1e-05), [[FAM83G]] (+0.58, fdr 1e-05); moves opposite to [[SH3BGRL]] (-0.57, fdr 1e-05), [[PRDX3]] (-0.55, fdr 2e-05), [[SUMO1]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C11orf91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 572.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (HepG2/C3A 2.71×, AsPC-1 2.40×, RPMI-7951 3.02×, A549 2.36×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +7.5 | 3e-11 | 30/47 (HepG2/C3A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +5.5 | 1e-05 | 27/47 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.394×** | -15.8 | 0e+00 | 40/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -14.3 | 1e-43 | 27/35 (Hs 766T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.532×** | -10.3 | 1e-22 | 30/37 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.636×** | -8.0 | 2e-13 | 34/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.657×** | -7.4 | 1e-11 | 31/48 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.664×** | -6.1 | 1e-07 | 25/46 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -5.5 | 2e-06 | 5/49 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.753×** | -5.0 | 4e-05 | 25/48 (hTERT-HPNE, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.821×** | -4.9 | 6e-05 | 21/48 (J82, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.731×** | -4.7 | 2e-04 | 23/48 (HOP62, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.743×** | -4.4 | 5e-04 | 22/48 (HOP62, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.748×** | -4.3 | 8e-04 | 22/46 (HepG2/C3A, CFPAC-1, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.790×** | -4.1 | 0.002 | 20/48 (H4, A-172, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.767×** | -3.9 | 0.004 | 13/47 (AN3 CA, A-172, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.666×** | -3.7 | 0.007 | 13/47 (SW 1088, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -3.6 | 0.011 | 16/48 (hTERT-HPNE, C32, …) | top dose only |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.019 | 8/47 (NCI-H2347, RKO, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.853× | -3.3 | 0.023 | 12/48 (Hs 766T, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.829×** | -3.2 | 0.038 | 10/47 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.038 | 9/48 (SW 1088, SNU-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.830×** | -3.1 | 0.038 | 15/49 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Allantoin (drug)]] 5 µM |  | 0.882× | -3.1 | 0.045 | 9/48 (HEC-1-A, SW 900, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.855× | -3.1 | 0.046 | 13/48 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.720×** | -3.0 | 0.051 | 17/49 (NCI-H1573, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.835× | -3.0 | 0.055 | 8/48 (NCI-H1573, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 77.6 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.293× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 92.2 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -11.3) |
| [[C32 (line)]] | wt | 93.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.267× (z -10.4) |
| [[Hs 766T (line)]] | wt | 99.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -17.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 85.2 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.308× (z -10.9) |
| [[A-172 (line)]] | wt | 74.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -13.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 75.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -11.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 37.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 39.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 42.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 81.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.207× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[HS-578T (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -11.0) |
| [[SW 1088 (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0677× (z -11.3) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 42.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0871× (z -14.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 44.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -15.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.195× (z -8.5) ⚠ toxic |
| [[A549 (line)]] | wt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 45.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.0) | — |
| [[H4 (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 31.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 45.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL6]] | +0.60 | +0.49 / +0.52 | both halves | 2e-05 |  |
| [[STK10]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[FAM83G]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NACC1]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ORAI1]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SEMA4C]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SLC66A1]] | +0.56 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[LRWD1]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[LRRC8E]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[IL4R]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[DMPK]] | +0.54 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[PHLDB1]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[PRDX3]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[SUMO1]] | -0.54 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[MORF4L1]] | -0.53 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[SH3YL1]] | -0.53 | -0.40 / -0.48 | both halves | 5e-05 | same gene group |
| [[TMEM123]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PPP1CB]] | -0.51 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[SCARB2]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[FAM210B]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[RTN3]] | -0.49 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ERMP1]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CSDE1]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity raises BCAR1's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without C11orf91 | 0.079 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (19.8, -20.0); signed map (-1.1, 33.6). **Vector** length 98.3, 22.8% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +0.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | -1.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -14.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -6.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | BCAR1 scaffold protein, Cas family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,228,181-75,268,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P130Cas, Crkas, CAS, CASS1 |
| Gene groups (HGNC) | Cas scaffold protein family; SH3 domain containing |
| Hallmark sets | XENOBIOTIC_METABOLISM, MITOTIC_SPINDLE |
| Reactome | 13 pathways, smallest: PTK6 Regulates RHO GTPases, RAS GTPase and MAP kinases; p130Cas linkage to MAPK signaling for integrins; Integrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P56945](https://www.uniprot.org/uniprotkb/P56945) (Breast cancer anti-estrogen resistance protein 1):

> Docking protein which plays a central coordinating role for tyrosine kinase-based signaling related to cell adhesion. Implicated in induction of cell migration and cell branching. Involved in the BCAR3-mediated inhibition of TGFB signaling (By similarity).

**Summary**, from NCBI Gene [9564](https://www.ncbi.nlm.nih.gov/gene/9564):

> The protein encoded by this gene is a member of the Crk-associated substrate (CAS) family of scaffold proteins, characterized by the presence of multiple protein-protein interaction domains and many serine and tyrosine phosphorylation sites. The encoded protein contains a Src-homology 3 (SH3) domain, a proline-rich domain, a substrate domain which contains 15 repeat of the YxxP consensus phosphorylation motif for Src family kinases, a serine-rich domain, and a bipartite Src-binding domain, …

**Accessions** — [HGNC:971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:971) · Entrez [9564](https://www.ncbi.nlm.nih.gov/gene/9564) · UniProt [P56945](https://www.uniprot.org/uniprotkb/P56945) · Ensembl [ENSG00000050820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050820)

## Data

Gene col 572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 572); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 572]; `tensor/DDL_lfc|DDL_z.npy` [572]; `embed/gene_vectors.npy` [572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 572 or target_col == 572). Every well: [[BCAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
