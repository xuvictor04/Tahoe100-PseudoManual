---
symbol: "TEC"
type: "gene"
col: 5729
ensembl_id: "ENSG00000135605"
name: "tec protein tyrosine kinase"
location: "4p12-p11"
module: 99
arm: "+"
pooled_cpm: 40.02
n_lines_expressing: 42
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# TEC

*tec protein tyrosine kinase* — 4p12-p11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +15.4, q 0e+00, up in 30 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.452× (z -14.3, q 1e-43, down in 28 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.769× (z -4.7, q 3e-04, down in 20 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHIP1A]] (+0.69, fdr 1e-05), [[GPR160]] (+0.63, fdr 4e-05), [[CNNM4]] (+0.61, fdr 1e-05); moves opposite to [[AGAP6]] (-0.63, fdr 1e-05), [[SSU72]] (-0.60, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.58, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RASAL1]] → it (grade B ⚠); 3 go from it, the strongest it → [[MSANTD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +15.4 | 0e+00 | 30/40 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +12.7 | 1e-34 | 34/40 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +11.8 | 9e-30 | 32/40 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +11.6 | 7e-29 | 31/40 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +11.0 | 5e-26 | 34/40 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +8.7 | 2e-16 | 29/40 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +6.7 | 2e-09 | 25/40 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +5.8 | 4e-07 | 23/40 (RKO, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +5.0 | 4e-05 | 18/40 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.19× | +4.5 | 4e-04 | 17/40 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.14× | +3.4 | 0.034 | 15/39 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.042 | 10/40 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.054 | 12/40 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5729.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.452×** | -14.3 | 1e-43 | 28/39 (CFPAC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -13.3 | 1e-37 | 27/33 (HCT15, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.467×** | -12.7 | 1e-34 | 27/34 (KATO III, A549, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.739×** | -5.4 | 8e-06 | 23/38 (HT-29, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.769×** | -4.7 | 3e-04 | 20/40 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.834× | -4.6 | 4e-04 | 25/40 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.794×** | -4.2 | 0.003 | 14/39 (NCI-H1792, C-33 A, …) | inconsistent across doses |  |
| [[DT-061 (drug)]] 5 µM |  | **0.687×** | -3.5 | 0.029 | 13/38 (C32, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -3.4 | 0.041 | 14/33 (NCI-H1792, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.829×** | -3.4 | 0.041 | 18/40 (NCI-H1573, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 164 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.343× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 23.2 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.265× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 99.6 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -19.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.8 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.98× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0858× (z -20.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -8.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 74.0 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.340× (z -11.2) |
| [[SW1417 (line)]] | alt | 57.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -14.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 41.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -11.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 80.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0813× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.329× (z -9.4) |
| [[HT-29 (line)]] | alt | 55.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -11.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 64.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 89.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0836× (z -17.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 34.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 27.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0653× (z -19.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 87.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -13.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 26.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 32.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.332× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[OTS514 (drug)]] 5 µM 0.0856× (z -9.2) |
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -19.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0553× (z -8.9) ⚠ cell-cycle shift, explains ~69% of this change |
| [[COLO 205 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.127× (z -8.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0806× (z -16.4) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.2) | — |
| [[RKO (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -12.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.273× (z -11.9) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SW 1271 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0615× (z -9.1) ⚠ toxic; unreliable plate only |
| [[SW 900 (line)]] | alt | 46.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.4) | — |
| [[SW48 (line)]] | wt | 98.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.253× (z -9.3) |
| [[A-172 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP1A]] | +0.69 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[GPR160]] | +0.63 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[CNNM4]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[BIK]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[RAB11FIP1]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[KBTBD3]] | +0.56 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[RYBP]] | +0.55 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[NOS1AP]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[FRRS1]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SEPTIN6]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R2]] | +0.54 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[ANKMY2]] | +0.54 | +0.55 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP6]] | -0.63 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SSU72]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[MTOR]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.54 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ZMYND11]] | -0.53 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[CDK11A]] | -0.53 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[MCM3AP]] | -0.53 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[TSTD2]] | -0.53 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[DPH5-DT]] | -0.52 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[MAPKAP1]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DPP8]] | -0.52 | -0.30 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASAL1]] | B | RASAL1 activity raises TEC's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without RASAL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TEC's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TEC's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSANTD2]] | B | TEC activity lowers MSANTD2's level | lines that do not express TEC (8) vs lines expressing it (42) | 1.40× higher at baseline in the lines without TEC | 0.060 | ⚠ within organs, on part of the lines; also absent: TXK; maybe low, not absent; its own permutation p |
| [[XRCC5]] | B | TEC activity lowers XRCC5's level | lines that do not express TEC (8) vs lines expressing it (42) | 1.09× higher at baseline in the lines without TEC | 0.060 | ⚠ within organs, on part of the lines; also absent: TXK; maybe low, not absent; its own permutation p |
| [[FHIP1A]] | B | TEC activity raises FHIP1A's level | lines that do not express TEC (8) vs lines expressing it (42) | 2.03× lower at baseline in the lines without TEC | 0.097 | ⚠ within organs, on part of the lines; also absent: TXK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.7, -11.0); signed map (-31.9, 22.1). **Vector** length 91.2, 21.3% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.6 | +4.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.9 | +5.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tec protein tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12-p11 — chr4:48,135,783-48,269,838 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSCTK4 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing; Tec family tyrosine kinases; SH3 domain containing |
| Reactome | 8 pathways, smallest: FCERI mediated Ca+2 mobilization; Signaling by SCF-KIT; Interleukin-3, Interleukin-5 and GM-CSF signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P42680](https://www.uniprot.org/uniprotkb/P42680) (Tyrosine-protein kinase Tec):

> Non-receptor tyrosine kinase that contributes to signaling from many receptors and participates as a signal transducer in multiple downstream pathways, including regulation of the actin cytoskeleton. Plays a redundant role to ITK in regulation of the adaptive immune response. Regulates the development, function and differentiation of conventional T-cells and nonconventional NKT-cells. Required for TCR-dependent IL2 gene induction. Phosphorylates DOK1, one CD28-specific substrate, and …

**Summary**, from NCBI Gene [7006](https://www.ncbi.nlm.nih.gov/gene/7006):

> The protein encoded by this gene belongs to the Tec family of non-receptor protein-tyrosine kinases containing a pleckstrin homology domain. Tec family kinases are involved in the intracellular signaling mechanisms of cytokine receptors, lymphocyte surface antigens, heterotrimeric G-protein coupled receptors, and integrin molecules. They are also key players in the regulation of the immune functions. Tec kinase is an integral component of T cell signaling and has a distinct role in T cell …

**Accessions** — [HGNC:11719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11719) · Entrez [7006](https://www.ncbi.nlm.nih.gov/gene/7006) · UniProt [P42680](https://www.uniprot.org/uniprotkb/P42680) · Ensembl [ENSG00000135605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135605)

## Data

Gene col 5729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5729); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5729]; `tensor/DDL_lfc|DDL_z.npy` [5729]; `embed/gene_vectors.npy` [5729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5729 or target_col == 5729). Every well: [[TEC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
