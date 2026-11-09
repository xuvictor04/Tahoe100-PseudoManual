---
symbol: "UBTD1"
type: "gene"
col: 9199
ensembl_id: "ENSG00000165886"
name: "ubiquitin domain containing 1"
location: "10q24.1-q24.2"
module: 3
arm: "+"
pooled_cpm: 20.92
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# UBTD1

*ubiquitin domain containing 1* — 10q24.1-q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +17.9, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.518× (z -9.6, q 3e-19, down in 23 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.647× (z -6.6, q 5e-09, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD13D]] (+0.72, fdr 7e-06), [[PDXP]] (+0.72, fdr 7e-06), [[TRIM62]] (+0.70, fdr 7e-06); moves opposite to [[TRMT13]] (-0.68, fdr 7e-06), [[ZNF480]] (-0.66, fdr 7e-06), [[ZXDB]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPB41L4B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +17.9 | 0e+00 | 42/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.39×** | +13.2 | 2e-37 | 46/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.26×** | +12.4 | 6e-33 | 40/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.93×** | +10.0 | 4e-21 | 40/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +9.3 | 2e-18 | 43/47 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +9.0 | 2e-17 | 44/48 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.4 | 2e-08 | 22/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +6.1 | 6e-08 | 31/48 (PANC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.47×** | +5.6 | 1e-06 | 25/45 (NCI-H460, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +5.4 | 4e-06 | 24/48 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.1 | 2e-05 | 23/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +4.2 | 0.001 | 19/47 (A549, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +3.8 | 0.007 | 15/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.013 | 9/47 (HEC-1-A, J82, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.27×** | +3.6 | 0.013 | 13/47 (J82, SW48, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.047 | 15/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.1 | 0.052 | 11/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.15× | +3.1 | 0.062 | 9/48 (Panc 03.27, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.065 | 17/45 (C32, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.065 | 2/47 (PANC-1, NCI-H460) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -9.6 | 3e-19 | 23/30 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.536×** | -9.5 | 7e-19 | 33/41 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.615×** | -6.9 | 1e-09 | 20/35 (NCI-H2347, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -6.6 | 5e-09 | 25/46 (NCI-H2347, SW 900, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.690×** | -5.7 | 2e-06 | 26/48 (LOX-IMVI, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.699×** | -5.4 | 5e-06 | 23/47 (NCI-H1573, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.813×** | -4.5 | 7e-04 | 22/48 (C32, H4, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.748×** | -4.3 | 0.001 | 20/47 (NCI-H2347, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -4.2 | 0.001 | 22/48 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.770×** | -3.7 | 0.013 | 17/47 (KATO III, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.845× | -3.6 | 0.014 | 14/48 (H4, BT-474, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.028 | 14/48 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.806×** | -3.3 | 0.042 | 16/48 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.670×** | -3.2 | 0.057 | 9/47 (A-427, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.816×** | -3.1 | 0.071 | 10/48 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.822×** | -3.0 | 0.090 | 7/48 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.871× | -3.0 | 0.090 | 12/48 (NCI-H661, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 25.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -9.5) |
| [[SW480 (line)]] | alt | 20.4 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.04× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.3) | — |
| [[C32 (line)]] | wt | 51.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 25.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.3) | — |
| [[A549 (line)]] | wt | 16.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -9.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 13.7 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.04× (z +8.9) | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 2 (1 ⚠) | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0751× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 17.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 18.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0933× (z -14.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -10.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -9.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.112× (z -11.3) |
| [[LoVo (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 8.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -12.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD13D]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[PDXP]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[TRIM62]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[CARD19]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.69 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[MED26]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[LRP5L]] | +0.68 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[AGAP3]] | +0.68 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[TMEM38A]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[MPG]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[STK32C]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[METRN]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | -0.68 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[ZNF480]] | -0.66 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.66 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[USP40]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[ICE2]] | -0.65 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[TTC27]] | -0.65 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[UTP20]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[ATRX]] | -0.65 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.64 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[RPL7L1]] | -0.64 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[NOL8]] | -0.64 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[EIF2B5]] | -0.64 | -0.67 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L4B]] | B | EPB41L4B activity lowers UBTD1's level | lines that do not express EPB41L4B (9) vs lines expressing it (41) | 1.41× higher at baseline in the lines without EPB41L4B | 0.060 | ⚠ within organs, on part of the lines; also absent: MYRF, GRTP1, MARVELD2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.1, -3.7); signed map (-32.4, 17.2). **Vector** length 106, 26.5% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +7.1 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +17.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.9 | +9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +13.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.5 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.9 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.8 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -9.1 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1-q24.2 — chr10:97,498,924-97,571,206 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11807 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAC8](https://www.uniprot.org/uniprotkb/Q9HAC8) (Ubiquitin domain-containing protein 1):

> May be involved in the regulation of cellular senescence through a positive feedback loop with TP53. Is a TP53 downstream target gene that increases the stability of TP53 protein by promoting the ubiquitination and degradation of MDM2.

**Summary**, from NCBI Gene [80019](https://www.ncbi.nlm.nih.gov/gene/80019):

> The degradation of many proteins is carried out by the ubiquitin pathway in which proteins are targeted for degradation by covalent conjugation of the polypeptide ubiquitin. This gene encodes a protein that belongs to the ubiquitin family of proteins. The encoded protein is thought to regulate E2 ubiquitin conjugating enzymes belonging to the UBE2D family. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:25683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25683) · Entrez [80019](https://www.ncbi.nlm.nih.gov/gene/80019) · UniProt [Q9HAC8](https://www.uniprot.org/uniprotkb/Q9HAC8) · Ensembl [ENSG00000165886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165886)

## Data

Gene col 9199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9199); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9199]; `tensor/DDL_lfc|DDL_z.npy` [9199]; `embed/gene_vectors.npy` [9199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9199 or target_col == 9199). Every well: [[UBTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
