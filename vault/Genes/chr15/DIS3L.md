---
symbol: "DIS3L"
type: "gene"
col: 9392
ensembl_id: "ENSG00000166938"
name: "DIS3 like exosome 3'-5' exoribonuclease"
location: "15q22.31"
module: 1
arm: "+"
pooled_cpm: 14.09
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 20
n_dd_up_clean: 17
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DIS3L

*DIS3 like exosome 3'-5' exoribonuclease* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +9.2, q 3e-17, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.450× (z -11.8, q 3e-29, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF280D]] (+0.78, fdr 7e-06), [[MTPAP]] (+0.76, fdr 7e-06), [[ZNF507]] (+0.75, fdr 7e-06); moves opposite to [[MYO9B]] (-0.69, fdr 1e-05), [[F11R]] (-0.67, fdr 2e-05), [[GUK1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IL1RAP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +9.2 | 3e-17 | 24/45 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.0 | 7e-17 | 21/37 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +8.5 | 5e-15 | 17/26 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +8.1 | 1e-13 | 36/46 (SW480, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +7.2 | 5e-11 | 28/45 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +5.9 | 3e-07 | 14/29 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +5.4 | 5e-06 | 22/46 (LoVo, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +5.0 | 3e-05 | 18/46 (SW480, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 4e-05 | 19/46 (LOX-IMVI, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.4 | 5e-04 | 19/47 (NCI-H2347, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +4.4 | 6e-04 | 15/47 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +4.1 | 0.002 | 16/46 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 6/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.005 | 14/46 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.7 | 0.009 | 16/40 (RPMI-7951, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.012 | 7/46 (A549, NCI-H2030, …) | top dose only | position effect removed |
| [[Afatinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.018 | 8/47 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.024 | 10/46 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.032 | 6/45 (RKO, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.450×** | -11.8 | 3e-29 | 30/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.482×** | -10.8 | 2e-24 | 30/46 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.495×** | -10.4 | 6e-23 | 29/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.553×** | -8.7 | 4e-16 | 28/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -7.7 | 2e-12 | 28/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -5.6 | 2e-06 | 23/46 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -5.5 | 4e-06 | 23/46 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.697×** | -5.3 | 8e-06 | 22/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.699×** | -5.0 | 4e-05 | 17/46 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.742×** | -4.4 | 6e-04 | 20/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.782×** | -3.6 | 0.016 | 19/46 (AN3 CA, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.591×** | -3.5 | 0.022 | 12/46 (SHP-77, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -3.5 | 0.023 | 13/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.727×** | -3.3 | 0.033 | 8/47 (NCI-H1573, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.777×** | -3.3 | 0.034 | 13/46 (SW48, LoVo, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.609×** | -3.3 | 0.034 | 13/45 (SW48, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.057 | 10/46 (CHP-212, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.628×** | -3.1 | 0.057 | 14/44 (HepG2/C3A, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -10.2) |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.225× (z -13.1) |
| [[SW480 (line)]] | alt | 17.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -13.6) |
| [[LoVo (line)]] | wt | 24.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -12.3) |
| [[A-172 (line)]] | wt | 12.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +10.8) | [[Belinostat (drug)]] 5 µM 0.182× (z -9.9) |
| [[A-427 (line)]] | wt | 20.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.71× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.174× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -10.4) |
| [[KATO III (line)]] | alt | 14.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +9.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.209× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 7.04 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -10.0) |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -10.3) |
| [[SW48 (line)]] | wt | 26.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.141× (z -9.9) |
| [[A498 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0654× (z -8.9) |
| [[COLO 205 (line)]] | alt | 9.07 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0919× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -10.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 5.64 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0595× (z -8.9) |
| [[A549 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF280D]] | +0.78 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.76 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.75 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.74 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[TXNRD2]] | +0.72 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.69 | +0.77 / +0.45 | both halves | 3e-05 |  |
| [[DPH5]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.68 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[ZC3H7B]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[YTHDC2]] | +0.66 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[PEX1]] | +0.66 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[ZFP30]] | +0.66 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | -0.69 | -0.76 / -0.49 | both halves | 1e-05 |  |
| [[F11R]] | -0.67 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[GUK1]] | -0.65 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[TRPT1]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[UBA6]] | -0.63 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[CYTH1]] | -0.63 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[GNB2]] | -0.62 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.62 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[QSOX1]] | -0.62 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[NDRG1]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[CIB1]] | -0.62 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[VRK3]] | -0.61 | -0.64 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1RAP]] | B | IL1RAP activity lowers DIS3L's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.15× higher at baseline in the lines without IL1RAP | 0.024 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[FAXC]] | B | FAXC activity raises DIS3L's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without FAXC | 0.029 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[FAM169A]] | B | FAM169A activity raises DIS3L's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without FAM169A | 0.032 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.7, 5.5); signed map (10.3, -35.2). **Vector** length 92.6, 19.6% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +9.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.8 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +5.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.4 | +5.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +3.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.4 | -10.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -10.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.9 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DIS3 like exosome 3'-5' exoribonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:66,293,217-66,333,898 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4562, FLJ38088, KIAA1955, DIS3L1 |
| Gene groups (HGNC) | Exosome complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF46](https://www.uniprot.org/uniprotkb/Q8TF46) (DIS3-like exonuclease 1):

> Catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the cytoplasm, the RNA exosome complex is involved in general mRNA turnover and specifically degrades inherently unstable mRNAs containing AU-rich elements (AREs) within their 3' untranslated regions, and in RNA surveillance pathways, preventing translation of aberrant mRNAs. It seems to be involved in degradation of …

**Summary**, from NCBI Gene [115752](https://www.ncbi.nlm.nih.gov/gene/115752):

> The cytoplasmic RNA exosome complex degrades unstable mRNAs and is involved in the regular turnover of other mRNAs. The protein encoded by this gene contains 3'-5' exoribonuclease activity and is a catalytic component of this complex. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:28698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28698) · Entrez [115752](https://www.ncbi.nlm.nih.gov/gene/115752) · UniProt [Q8TF46](https://www.uniprot.org/uniprotkb/Q8TF46) · Ensembl [ENSG00000166938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166938)

## Data

Gene col 9392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9392); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9392]; `tensor/DDL_lfc|DDL_z.npy` [9392]; `embed/gene_vectors.npy` [9392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9392 or target_col == 9392). Every well: [[DIS3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIS3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
