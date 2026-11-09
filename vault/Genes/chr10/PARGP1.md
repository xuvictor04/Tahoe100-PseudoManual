---
symbol: "PARGP1"
type: "gene"
col: 14215
ensembl_id: "ENSG00000239883"
name: "PARG pseudogene 1"
location: "10q11.22"
module: 36
arm: "+"
pooled_cpm: 31.09
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PARGP1

*PARG pseudogene 1* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.06× (z +13.3, q 8e-38, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.435× (z -15.2, q 0e+00, down in 37 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 0.761× (z -3.6, q 0.039, down in 12 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C2]] (+0.72, fdr 7e-06), [[CDK5RAP1]] (+0.70, fdr 7e-06), [[PCGF6]] (+0.69, fdr 7e-06); moves opposite to [[ATF3]] (-0.63, fdr 1e-05), [[SDCBP]] (-0.60, fdr 1e-05), [[IQCN]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.06×** | +13.3 | 8e-38 | 43/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +12.2 | 1e-31 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.56×** | +12.1 | 2e-31 | 41/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +10.6 | 5e-24 | 43/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.63×** | +8.9 | 5e-17 | 39/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.49×** | +7.3 | 3e-11 | 34/47 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +7.2 | 6e-11 | 23/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +6.3 | 2e-08 | 28/48 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 4e-07 | 26/47 (HOP62, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.5 | 3e-06 | 23/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.3 | 5e-06 | 28/48 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.22×** | +5.2 | 1e-05 | 22/48 (SW48, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.0 | 3e-05 | 23/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 8e-05 | 21/47 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.20× | +4.7 | 1e-04 | 19/48 (SNU-423, RKO, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 3e-04 | 17/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.007 | 15/48 (AsPC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.019 | 15/47 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.041 | 17/48 (SW480, HT-29, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.059 | 12/48 (SW480, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14215.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.435×** | -15.2 | 0e+00 | 37/45 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -11.5 | 5e-28 | 31/36 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.517×** | -11.2 | 1e-26 | 32/43 (NCI-H460, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.755×** | -5.2 | 4e-05 | 25/46 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.761×** | -3.6 | 0.039 | 12/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.770×** | -3.4 | 0.053 | 11/48 (NCI-H661, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.701×** | -3.4 | 0.053 | 14/46 (SNU-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.829×** | -3.3 | 0.079 | 12/48 (Hs 766T, SW 1271, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.794× | -3.0 | 0.15 | 13/48 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.03× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 36.0 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.96× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -15.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 37.8 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.67× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 63.4 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.22× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 41.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0722× (z -24.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 28.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +10.0) | — |
| [[RKO (line)]] | wt | 57.8 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.50× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -15.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -11.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 25.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Pemigatinib (drug)]] 0.05 µM 0.280× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 34.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -19.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 39.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.131× (z -8.6) |
| [[C32 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -9.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0955× (z -10.0) |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -17.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.62× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 33.6 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.01× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0998× (z -15.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C2]] | +0.72 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[PCGF6]] | +0.69 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ORC5]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[DHX57]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PIK3R4]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[DCUN1D5]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TYW1]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DDX55]] | +0.63 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[MRPS11]] | +0.61 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[PGS1]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF3]] | -0.63 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[SDCBP]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[IQCN]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[JUN]] | -0.57 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[SPDYA]] | -0.56 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[PPP1R15B]] | -0.54 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[ARL5B]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[UBE2A]] | -0.52 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[ABLIM1]] | -0.52 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[CHRAC1]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SPTAN1]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-9.8, -17.1); signed map (-17.5, -19.2). **Vector** length 76.4, 15.6% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +13.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +12.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.8 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.2 | +7.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.3 | -15.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | PARG pseudogene 1 |
| Locus type | pseudogene |
| Location | 10q11.22 — chr10:45,888,165-45,972,154 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45008) · Entrez [728407](https://www.ncbi.nlm.nih.gov/gene/728407) · Ensembl [ENSG00000239883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239883)

## Data

Gene col 14215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14215); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14215]; `tensor/DDL_lfc|DDL_z.npy` [14215]; `embed/gene_vectors.npy` [14215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14215 or target_col == 14215). Every well: [[PARGP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARGP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
