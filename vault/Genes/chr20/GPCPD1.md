---
symbol: "GPCPD1"
type: "gene"
col: 4660
ensembl_id: "ENSG00000125772"
name: "glycerophosphocholine phosphodiesterase 1"
location: "20p12.3"
module: 94
arm: "+"
pooled_cpm: 133.79
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# GPCPD1

*glycerophosphocholine phosphodiesterase 1* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.35× (z +15.0, q 0e+00, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.438× (z -10.3, q 6e-22, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.584× (z -9.4, q 8e-19, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A2]] (+0.60, fdr 4e-05), [[CAPN5]] (+0.60, fdr 1e-05), [[GNG2]] (+0.59, fdr 3e-05); moves opposite to [[SFXN5]] (-0.54, fdr 2e-05), [[ZNF876P]] (-0.51, fdr 3e-05), [[KMT2D]] (-0.48, fdr 3e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TREM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +15.0 | 0e+00 | 34/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +9.1 | 4e-17 | 35/48 (PANC-1, C-33 A, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +9.0 | 4e-17 | 40/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.95×** | +8.3 | 2e-14 | 43/49 (HT-29, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.93×** | +8.2 | 3e-14 | 40/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +6.4 | 2e-08 | 38/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +6.2 | 4e-08 | 29/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.58×** | +5.7 | 8e-07 | 40/48 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +5.1 | 2e-05 | 30/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-05 | 31/48 (SW480, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +4.8 | 9e-05 | 32/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.85×** | +4.0 | 0.003 | 30/48 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.85×** | +4.0 | 0.003 | 28/49 (LoVo, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.005 | 28/48 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.016 | 23/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.438×** | -10.3 | 6e-22 | 39/49 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.430×** | -10.1 | 2e-21 | 38/43 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -9.4 | 8e-19 | 33/49 (CFPAC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.513×** | -8.3 | 1e-14 | 42/48 (HOP62, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.636×** | -5.2 | 2e-05 | 27/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -4.7 | 3e-04 | 31/47 (SW 900, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -4.0 | 0.006 | 26/50 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.729×** | -3.9 | 0.006 | 24/48 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.801×** | -3.9 | 0.007 | 30/48 (C32, HS-578T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.739×** | -3.8 | 0.010 | 30/48 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.748×** | -3.6 | 0.016 | 26/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.749×** | -3.3 | 0.041 | 22/48 (NCI-H23, SW 900, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | 0.784× | -3.0 | 0.11 | 17/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 97.6 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +21.1) | — |
| [[SW480 (line)]] | alt | 73.8 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +23.3) | — |
| [[HT-29 (line)]] | alt | 58.7 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +19.1) | — |
| [[SW 900 (line)]] | alt | 341 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -16.9) |
| [[A-427 (line)]] | wt | 40.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +18.0) | — |
| [[CFPAC-1 (line)]] | alt | 350 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 290 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -13.9) |
| [[A-172 (line)]] | wt | 101 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -10.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 68.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 115 | 4 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 5.84× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.42× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.6) |
| [[RKO (line)]] | wt | 98.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +21.6) | — |
| [[hTERT-HPNE (line)]] | wt | 163 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.5) |
| [[LoVo (line)]] | wt | 126 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.317× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 53.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 259 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -12.4) |
| [[SW48 (line)]] | wt | 77.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +14.9) | — |
| [[A549 (line)]] | wt | 306 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 225 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 258 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.0) |
| [[C-33 A (line)]] | alt | 71.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +12.5) | — |
| [[C32 (line)]] | wt | 130 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.207× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 109 | 3 | 0 | [[Selinexor (drug)]] 5 µM 3.35× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 163 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -14.9) |
| [[SHP-77 (line)]] | alt | 240 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -12.5) |
| [[SNU-1 (line)]] | wt | 132 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 103 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -11.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 135 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -12.3) |
| [[H4 (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.175× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 85.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 120 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 88.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.3) | — |
| [[NCI-H460 (line)]] | wt | 91.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 110 | 0 | 2 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0620× (z -11.4) |
| [[A498 (line)]] | wt | 79.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 232 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -12.8) |
| [[HOP62 (line)]] | alt | 138 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.190× (z -13.7) |
| [[Hs 766T (line)]] | wt | 150 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.5) | — |
| [[J82 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 225 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 41.6 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.45× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +16.6) | — |
| [[SK-MEL-2 (line)]] | alt | 61.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 172 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A2]] | +0.60 | +0.41 / +0.69 | both halves | 4e-05 | pathway: Glycerophospholipid biosynthesis |
| [[CAPN5]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[GNG2]] | +0.59 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[PTGES]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[HIF1A]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[TATDN3]] | +0.55 | +0.34 / +0.58 | both halves | 1e-04 | STRING 530 |
| [[NDFIP1]] | +0.55 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[PPDPF]] | +0.54 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[NGFR]] | +0.54 | +0.31 / +0.64 | both halves | 2e-04 |  |
| [[METTL14]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ZNF14]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[GEMIN2]] | +0.53 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFXN5]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ZNF876P]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[KMT2D]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.48 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[PSMD6-AS2]] | -0.48 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MCM9]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[MFSD14CP-1]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[NSD2]] | -0.47 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[METTL4]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZNF8]] | -0.45 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SNRPA]] | -0.45 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[CDR2]] | -0.45 | -0.33 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TREM1]] | B | TREM1 activity raises GPCPD1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without TREM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[ACKR3]] | B | ACKR3 activity raises GPCPD1's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without ACKR3 | 0.018 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1 |
| [[TREM1]] | B | TREM1 activity weakens GPCPD1's drug response | lines that do not express TREM1 (25) vs lines expressing it (24) | the lines without TREM1 respond 1.22× as strongly (z diff -0.46); strongest at Homoharringtonine 5 µM: 3.02x vs 1.42x (z diff -4.8) | 0.032 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF; target measured in part of the lines; both ways; artifact flags |
| [[ACKR3]] | B | ACKR3 activity weakens GPCPD1's drug response | lines that do not express ACKR3 (30) vs lines expressing it (19) | the lines without ACKR3 respond 1.21× as strongly (z diff -0.47); strongest at Homoharringtonine 5 µM: 2.60x vs 1.48x (z diff -3.7) | 0.060 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; target measured in part of the lines; both ways; artifact flags |
| [[FAM229B]] | B | FAM229B activity lowers GPCPD1's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.68× higher at baseline in the lines without FAM229B | 0.088 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[DMXL1]] | C | DMXL1's natural level weakens GPCPD1's drug response | DMXL1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.02; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.8, 25.4); signed map (13.8, -15.4). **Vector** length 118, 42.2% of its response variance represented; |z| ≥ 3 in 1,361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +12.1 | +9.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +9.4 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | -10.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.4 | +8.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.8 | +5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.8 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.9 | +0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -8.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | +5.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | +0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.4 | +0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | glycerophosphocholine phosphodiesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:5,544,439-5,611,006 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1434, GDE5, GDPD6 |
| Reactome | 4 pathways, smallest: Hydrolysis of LPC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPB8](https://www.uniprot.org/uniprotkb/Q9NPB8) (Glycerophosphocholine phosphodiesterase GPCPD1):

> Shows strong preference for glycerophosphocholine. Displays weak activity toward glycerophosphoethanolamine and no detectable activity toward glycerophosphoglycerol, glycerophosphoserine, or glycerophosphoinosito. May be involved in the negative regulation of skeletal muscle differentiation, independently of its glycerophosphocholine phosphodiesterase activity.

**Summary**, from NCBI Gene [56261](https://www.ncbi.nlm.nih.gov/gene/56261):

> Predicted to enable glycerophosphocholine phosphodiesterase activity. Predicted to be involved in glycerophospholipid catabolic process. Predicted to act upstream of or within skeletal muscle tissue development. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26957) · Entrez [56261](https://www.ncbi.nlm.nih.gov/gene/56261) · UniProt [Q9NPB8](https://www.uniprot.org/uniprotkb/Q9NPB8) · Ensembl [ENSG00000125772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125772)

## Data

Gene col 4660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4660); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4660]; `tensor/DDL_lfc|DDL_z.npy` [4660]; `embed/gene_vectors.npy` [4660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4660 or target_col == 4660). Every well: [[GPCPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPCPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
