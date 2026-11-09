---
symbol: "SIPA1L2"
type: "gene"
col: 3863
ensembl_id: "ENSG00000116991"
name: "signal induced proliferation associated 1 like 2"
location: "1q42.2"
module: 167
arm: "+"
pooled_cpm: 48.82
n_lines_expressing: 40
n_dd_up: 31
n_dd_down: 11
n_dd_up_clean: 24
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 13
direction_downstream: 7
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# SIPA1L2

*signal induced proliferation associated 1 like 2* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +21.4, q 0e+00, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.562× (z -8.3, q 5e-14, down in 20 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.750× (z -4.5, q 0.002, down in 19 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XDH]] (+0.57, fdr 4e-05), [[TCIM]] (+0.54, fdr 3e-05), [[TARID]] (+0.52, fdr 1e-05); moves opposite to [[ZIM2-AS1]] (-0.45, fdr 6e-05), [[PRMT7]] (-0.44, fdr 2e-04), [[ATPAF2]] (-0.44, fdr 1e-04).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[RGS6]] → it (grade B ⚠); 7 go from it, the strongest it → [[NRG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +21.4 | 0e+00 | 32/37 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.08×** | +17.5 | 0e+00 | 33/38 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.00×** | +17.1 | 0e+00 | 30/38 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +14.2 | 1e-43 | 28/39 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.42×** | +13.7 | 6e-41 | 26/38 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +11.6 | 3e-29 | 28/38 (SW480, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +11.3 | 9e-28 | 26/38 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +11.1 | 1e-26 | 28/36 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +10.3 | 3e-23 | 23/37 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.77×** | +8.9 | 3e-17 | 28/39 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.9 | 3e-17 | 24/38 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.50×** | +8.9 | 3e-17 | 28/38 (PANC-1, HEC-1-A, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +8.1 | 2e-14 | 19/37 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +6.2 | 2e-08 | 20/38 (KATO III, NCI-H23, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.47×** | +6.0 | 8e-08 | 18/38 (SW1417, C-33 A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.5 | 1e-06 | 18/38 (A498, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.562×** | -8.3 | 5e-14 | 20/31 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.750×** | -4.5 | 0.002 | 19/37 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.746×** | -4.4 | 0.002 | 16/29 (BT-474, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -4.2 | 0.004 | 15/39 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.004 | 17/38 (HT-29, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~71% of this change | **0.784×** | -3.8 | 0.011 | 16/36 (SW480, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.784×** | -3.8 | 0.011 | 16/36 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.764×** | -3.7 | 0.013 | 16/34 (LS 180, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.781×** | -3.7 | 0.013 | 15/37 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.725×** | -3.6 | 0.018 | 17/37 (SK-MEL-2, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -3.4 | 0.036 | 13/38 (C32, SW 900, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.823× | -3.1 | 0.10 | 9/38 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.691× | -3.0 | 0.11 | 10/28 (SW480, SW 900, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.4 | 11 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0860× (z -20.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.7 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +13.7) | — |
| [[SW480 (line)]] | alt | 21.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +19.2) | — |
| [[J82 (line)]] | alt | 30.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 23.1 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.71× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.22× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 65.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +17.0) | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 94.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -8.8) |
| [[A498 (line)]] | wt | 77.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.5) | — |
| [[C-33 A (line)]] | alt | 15.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 4.94× (z +9.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.125× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 49.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.2) | — |
| [[LoVo (line)]] | wt | 83.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 136 | 0 | 3 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.149× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 37.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 33.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 27.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 30.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.05× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0506× (z -15.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 352 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -8.5) |
| [[H4 (line)]] | wt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0957× (z -9.2) |
| [[HT-29 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +10.0) | — |
| [[KATO III (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 64.2 | 1 | 0 | [[Retinoic acid (drug)]] 5 µM 3.26× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.37× (z +9.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW 900 (line)]] | alt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +10.7) | — |
| [[A-427 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XDH]] | +0.57 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TCIM]] | +0.54 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TARID]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[MAFB]] | +0.52 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[EREG]] | +0.51 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[RASD1]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[LINC01348]] | +0.50 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[RGS6]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[THRB]] | +0.50 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[RORB]] | +0.48 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[GAREM1]] | +0.48 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[TFAP2C]] | +0.47 | +0.53 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZIM2-AS1]] | -0.45 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[PRMT7]] | -0.44 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[ATPAF2]] | -0.44 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[RPGRIP1L]] | -0.44 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[KRBOX4]] | -0.43 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[LRRC27]] | -0.42 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[TRIT1]] | -0.42 | -0.55 / -0.29 | both halves | 3e-04 |  |
| [[IVD]] | -0.42 | -0.21 / -0.38 | both halves | 7e-04 |  |
| [[IFT172]] | -0.42 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[GET1]] | -0.41 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[ZNF461]] | -0.41 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[CRYZL1]] | -0.40 | -0.51 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS6]] | B | RGS6 activity raises SIPA1L2's level | lines that do not express RGS6 (22) vs lines expressing it (28) | 2.68× lower at baseline in the lines without RGS6 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, LIPG, RERG; maybe low, not absent |
| [[PELI2]] | B | PELI2 activity raises SIPA1L2's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 2.84× lower at baseline in the lines without PELI2 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[LINC02015]] | B | LINC02015 activity raises SIPA1L2's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without LINC02015 | 0.014 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN |
| [[THRB]] | B | THRB activity weakens SIPA1L2's drug response | lines that do not express THRB (15) vs lines expressing it (24) | the lines without THRB respond 1.72× as strongly (z diff -2.48); strongest at Idarubicin (hydrochloride) 5 µM: 2.49x vs 1.34x (z diff -3.4) | 0.014 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2; target measured in part of the lines; artifact flags |
| [[TARID]] | B | TARID activity raises SIPA1L2's level | lines that do not express TARID (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without TARID | 0.018 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[NTN4]] | B | NTN4 activity raises SIPA1L2's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without NTN4 | 0.029 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[ADAM28]] | B | ADAM28 activity raises SIPA1L2's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without ADAM28 | 0.034 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[TOP2A]] | B | TOP2A activity lowers SIPA1L2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[THRB]] | B | THRB activity raises SIPA1L2's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.99× lower at baseline in the lines without THRB | 0.054 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[TNFRSF21]] | B | TNFRSF21 activity raises SIPA1L2's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without TNFRSF21 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[FLRT3]] | B | FLRT3 activity raises SIPA1L2's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without FLRT3 | 0.088 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[ST6GAL2]] | B | ST6GAL2 activity raises SIPA1L2's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 2.21× lower at baseline in the lines without ST6GAL2 | 0.0998 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRG1]] | B | SIPA1L2 activity raises NRG1's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without SIPA1L2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[EPAS1]] | B | SIPA1L2 activity raises EPAS1's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without SIPA1L2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[NTN4]] | B | SIPA1L2 activity raises NTN4's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without SIPA1L2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[ATP2B1]] | B | SIPA1L2 activity raises ATP2B1's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without SIPA1L2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| cells under [[Bortezomib (drug)]] 0.05 µM | B | SIPA1L2 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express SIPA1L2 (10) vs lines expressing it (38) | the lines without SIPA1L2: 1.31× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[TARID]] | B | SIPA1L2 activity raises TARID's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without SIPA1L2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[ZNF594-DT]] | C | SIPA1L2 activity raises ZNF594-DT's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without SIPA1L2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.3, 21.7); signed map (51.2, 23.4). **Vector** length 93.5, 22.2% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +10.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.2 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +21.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +6.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +1.0 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | signal induced proliferation associated 1 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:232,397,965-232,630,571 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1389, SPAR2 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

UniProt [Q9P2F8](https://www.uniprot.org/uniprotkb/Q9P2F8) carries no function annotation.

**Summary**, from NCBI Gene [57568](https://www.ncbi.nlm.nih.gov/gene/57568):

> This gene encodes a member of the signal-induced proliferation-associated 1 like family. Members of this family contain a GTPase activating domain, a PDZ domain and a C-terminal coiled-coil domain with a leucine zipper. A similar protein in rat acts as a GTPases for the small GTPase Rap. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:23800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23800) · Entrez [57568](https://www.ncbi.nlm.nih.gov/gene/57568) · UniProt [Q9P2F8](https://www.uniprot.org/uniprotkb/Q9P2F8) · Ensembl [ENSG00000116991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116991)

## Data

Gene col 3863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3863); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3863]; `tensor/DDL_lfc|DDL_z.npy` [3863]; `embed/gene_vectors.npy` [3863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3863 or target_col == 3863). Every well: [[SIPA1L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIPA1L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
