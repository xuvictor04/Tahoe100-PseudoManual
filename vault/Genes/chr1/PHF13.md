---
symbol: "PHF13"
type: "gene"
col: 3785
ensembl_id: "ENSG00000116273"
name: "PHD finger protein 13"
location: "1p36.31"
module: 58
arm: "+"
pooled_cpm: 16.71
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# PHF13

*PHD finger protein 13* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.07× (z +14.1, q 2e-42, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.459× (z -15.1, q 0e+00, down in 32 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.735× (z -8.4, q 7e-15, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HTRA2]] (+0.63, fdr 1e-05), [[LRRC42]] (+0.58, fdr 1e-05), [[MARK4]] (+0.56, fdr 2e-05); moves opposite to [[TXNRD2]] (-0.58, fdr 5e-05), [[AIMP1]] (-0.56, fdr 1e-04), [[MCCC2]] (-0.54, fdr 2e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +14.1 | 2e-42 | 39/47 (PANC-1, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.16×** | +11.7 | 6e-29 | 36/48 (PANC-1, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +10.1 | 9e-22 | 32/44 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +8.8 | 1e-16 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +8.7 | 6e-16 | 37/46 (NCI-H2347, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +8.4 | 3e-15 | 26/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.3 | 8e-15 | 27/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +8.1 | 3e-14 | 26/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +7.0 | 1e-10 | 24/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +6.8 | 8e-10 | 25/48 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +6.6 | 2e-09 | 24/46 (SW48, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +6.1 | 5e-08 | 25/47 (NCI-H2347, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.33×** | +5.5 | 2e-06 | 16/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +5.0 | 3e-05 | 16/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.21×** | +3.7 | 0.008 | 11/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.009 | 11/47 (PANC-1, C-33 A, …) | two highest doses |  |
| [[4EGI-1 (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.012 | 7/48 (A-427, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -15.1 | 0e+00 | 32/40 (SNU-423, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -11.9 | 2e-30 | 21/29 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.735×** | -8.4 | 7e-15 | 26/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -7.8 | 8e-13 | 6/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.721×** | -5.9 | 5e-07 | 22/39 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -4.6 | 4e-04 | 16/47 (LS 180, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.848× | -4.5 | 5e-04 | 19/48 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.022 | 13/46 (AN3 CA, A-427, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.038 | 7/46 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.719×** | -3.3 | 0.046 | 10/45 (PANC-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.3 | 0.053 | 19/47 (SW48, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.9 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.35× (z +12.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 6.84× (z +10.5) | — |
| [[A-172 (line)]] | wt | 20.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.279× (z -11.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -12.6) |
| [[HOP62 (line)]] | alt | 22.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0980× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 21.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.45× (z +8.8) ⚠ toxic | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0974× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0304× (z -24.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.87× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.7) |
| [[A498 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 9.18 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -10.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.104× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -15.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 10.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.113× (z -8.5) |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -8.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.07 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.64× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -9.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0878× (z -13.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HTRA2]] | +0.63 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[LRRC42]] | +0.58 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[MARK4]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[EIF1AD]] | +0.56 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[RAP2A]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[BAHD1]] | +0.54 | +0.39 / +0.52 | both halves | 5e-05 | STRING 495 |
| [[BFAR]] | +0.53 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[ZNF250]] | +0.53 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[PAQR4]] | +0.53 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[MEX3D]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[TSEN54]] | +0.53 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[SDHAF1]] | +0.52 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNRD2]] | -0.58 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[AIMP1]] | -0.56 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[MCCC2]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[FUBP1]] | -0.54 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[SUCLG2]] | -0.54 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[OCIAD1]] | -0.52 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[IMPACT]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[YTHDC2]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CCDC25]] | -0.50 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[GUF1]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MRPL30]] | -0.50 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[YIPF6]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.335). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.9, 5.4); signed map (-40.2, 3.2). **Vector** length 89.1, 18.0% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +14.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.5 | +8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | +3.7 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.2 | -15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.5 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.3 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,613,731-6,624,030 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC43399 |
| Gene groups (HGNC) | PHD finger proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YI8](https://www.uniprot.org/uniprotkb/Q86YI8) (PHD finger protein 13):

> Modulates chromatin structure and DNA damage response by regulating key determinants of chromatin compaction and DNA damage response. Binds H3K4me3-containing chromatin and promotes DNA condensation by recruiting corepressors such as TRIM28 and H3K9 methyltransferase SETDB1. Required for normal chromosome condensation during the early stages of mitosis. Required for normal chromosome separation during mitosis. Increases both chromatin-associated levels and activity of H3K9 methyltransferases, …

**Summary**, from NCBI Gene [148479](https://www.ncbi.nlm.nih.gov/gene/148479):

> Enables chromatin binding activity and histone H3K9me2/3 reader activity. Involved in DNA damage response and mitotic chromosome condensation. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22983) · Entrez [148479](https://www.ncbi.nlm.nih.gov/gene/148479) · UniProt [Q86YI8](https://www.uniprot.org/uniprotkb/Q86YI8) · Ensembl [ENSG00000116273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116273)

## Data

Gene col 3785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3785); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3785]; `tensor/DDL_lfc|DDL_z.npy` [3785]; `embed/gene_vectors.npy` [3785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3785 or target_col == 3785). Every well: [[PHF13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
