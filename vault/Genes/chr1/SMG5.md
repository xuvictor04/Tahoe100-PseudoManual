---
symbol: "SMG5"
type: "gene"
col: 12754
ensembl_id: "ENSG00000198952"
name: "SMG5 nonsense mediated mRNA decay factor"
location: "1q22"
module: 36
arm: "+"
pooled_cpm: 72.15
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SMG5

*SMG5 nonsense mediated mRNA decay factor* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.03× (z +17.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.810× (z -7.4, q 6e-11, down in 30 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB3]] (+0.64, fdr 1e-05), [[ECSIT]] (+0.63, fdr 1e-05), [[CCDC12]] (+0.62, fdr 1e-05); moves opposite to [[SGO1-AS1]] (-0.57, fdr 1e-05), [[CGGBP1]] (-0.49, fdr 1e-04), [[RO60]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.03×** | +17.6 | 0e+00 | 47/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +15.4 | 0e+00 | 45/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +14.4 | 6e-45 | 42/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +13.3 | 3e-38 | 45/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +12.1 | 2e-31 | 43/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +10.9 | 1e-25 | 42/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +9.9 | 3e-21 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +9.3 | 1e-18 | 38/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +8.2 | 2e-14 | 33/49 (SW480, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +7.2 | 4e-11 | 35/43 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +7.1 | 5e-11 | 36/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.8 | 4e-07 | 31/48 (Hs 766T, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +5.3 | 6e-06 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 27/48 (HCT15, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.4 | 5e-04 | 7/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.012 | 11/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.021 | 11/48 (CHP-212, SW48, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.029 | 12/48 (NCI-H460, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.040 | 6/48 (J82, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -7.4 | 6e-11 | 30/49 (NCI-H23, SHP-77, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -7.3 | 8e-11 | 28/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -7.2 | 1e-10 | 28/48 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.751×** | -7.1 | 1e-10 | 27/48 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.791×** | -5.9 | 5e-07 | 26/49 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.808×** | -5.3 | 9e-06 | 26/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.675×** | -5.1 | 2e-05 | 28/49 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.821×** | -4.9 | 6e-05 | 23/48 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.821×** | -4.9 | 6e-05 | 23/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.6 | 3e-04 | 22/50 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 0.865× | -3.6 | 0.014 | 10/48 (KATO III, NCI-H1573, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.860× | -3.6 | 0.014 | 11/47 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.857× | -3.6 | 0.015 | 17/45 (SK-MEL-2, SW480, …) | inconsistent across doses | composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.874× | -3.4 | 0.032 | 10/49 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.885× | -3.1 | 0.081 | 5/49 (NCI-H2122, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.885× | -3.0 | 0.081 | 6/48 (NCI-H23, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.6 | 9 (5 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.79× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 62.5 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +15.7) | — |
| [[SW480 (line)]] | alt | 73.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.536× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 69.7 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +14.9) | — |
| [[LS 180 (line)]] | wt | 56.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.6) | — |
| [[A-427 (line)]] | wt | 67.9 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +9.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.8) |
| [[BT-474 (line)]] | alt | 139 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.44× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 56.9 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.48× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 62.0 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.00× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 72.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 57.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 69.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +9.9) | — |
| [[LoVo (line)]] | wt | 60.7 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.619× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 73.1 | 0 | 2 | — | [[Oxaprozin (drug)]] 5 µM 0.129× (z -14.7) |
| [[RKO (line)]] | wt | 78.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 135 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 82.5 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 87.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.7) |
| [[A498 (line)]] | wt | 74.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.93× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.433× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 59.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +8.5) | — |
| [[KATO III (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.31× (z +9.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 63.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -11.2) |
| [[SW48 (line)]] | wt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB3]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.63 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CCDC12]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ZNF496]] | +0.61 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[L3MBTL2]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[METTL16]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TMEM161A]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[HSF1]] | +0.59 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[NMRAL1]] | +0.58 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[TIMM50]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[HSPBP1]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[FBXL19]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1-AS1]] | -0.57 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.49 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[RO60]] | -0.49 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[UACA]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SMG5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CMTM8]] | B | CMTM8 activity raises SMG5's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without CMTM8 | 0.060 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SMG5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SMG5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-33.4, -8.3); signed map (-13.5, -20.5). **Vector** length 79.3, 18.4% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.8 | +17.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.0 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.8 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +7.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | -2.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -7.3 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.5 | +0.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | SMG5 nonsense mediated mRNA decay factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,249,224-156,282,825 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1089, LPTS-RP1, LPTSRP1, RP11-54H19.7, SMG-5, EST1B |
| Reactome | 3 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPR3](https://www.uniprot.org/uniprotkb/Q9UPR3) (Nonsense-mediated mRNA decay factor SMG5):

> Plays a role in nonsense-mediated mRNA decay. Does not have RNase activity by itself. Promotes dephosphorylation of UPF1. Together with SMG7 is thought to provide a link to the mRNA degradation machinery involving exonucleolytic pathways, and to serve as an adapter for UPF1 to protein phosphatase 2A (PP2A), thereby triggering UPF1 dephosphorylation. Necessary for TERT activity.

**Summary**, from NCBI Gene [23381](https://www.ncbi.nlm.nih.gov/gene/23381):

> SMG5 is involved in nonsense-mediated mRNA decay (Ohnishi et al., 2003 [PubMed 14636577]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24644) · Entrez [23381](https://www.ncbi.nlm.nih.gov/gene/23381) · UniProt [Q9UPR3](https://www.uniprot.org/uniprotkb/Q9UPR3) · Ensembl [ENSG00000198952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198952)

## Data

Gene col 12754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12754); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12754]; `tensor/DDL_lfc|DDL_z.npy` [12754]; `embed/gene_vectors.npy` [12754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12754 or target_col == 12754). Every well: [[SMG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
