---
symbol: "PRUNE1"
type: "gene"
col: 6721
ensembl_id: "ENSG00000143363"
name: "prune exopolyphosphatase 1"
location: "1q21.3"
module: 30
arm: "+"
pooled_cpm: 11.05
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PRUNE1

*prune exopolyphosphatase 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.11× (z +11.8, q 1e-29, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.607× (z -11.2, q 3e-26, down in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.556× (z -8.9, q 7e-17, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYPOP]] (+0.74, fdr 7e-06), [[IFT172]] (+0.72, fdr 7e-06), [[ZFP14]] (+0.72, fdr 7e-06); moves opposite to [[ITPR2-AS1]] (-0.64, fdr 1e-05), [[DGKH]] (-0.63, fdr 2e-05), [[PSMD6-AS1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +11.8 | 1e-29 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +11.7 | 2e-29 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +8.4 | 8e-15 | 33/47 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +6.2 | 6e-08 | 16/41 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +6.2 | 6e-08 | 18/48 (HOP62, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.8 | 2e-04 | 8/47 (PANC-1, A-172, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +4.6 | 3e-04 | 14/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.21×** | +4.4 | 9e-04 | 13/48 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.003 | 4/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.007 | 6/41 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.009 | 4/47 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.011 | 8/47 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.027 | 10/47 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.050 | 9/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.22×** | +3.2 | 0.060 | 9/46 (NCI-H2347, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.607×** | -11.2 | 3e-26 | 30/46 (A498, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.483×** | -10.7 | 5e-24 | 22/28 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.547×** | -9.6 | 2e-19 | 22/33 (MIA PaCa-2, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.556×** | -8.9 | 7e-17 | 28/46 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.597×** | -8.2 | 4e-14 | 26/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -7.6 | 3e-12 | 23/39 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.619×** | -7.6 | 3e-12 | 27/43 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.663×** | -6.5 | 6e-09 | 20/47 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -5.3 | 7e-06 | 20/46 (C-33 A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.727×** | -5.0 | 3e-05 | 17/46 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.815×** | -4.6 | 3e-04 | 13/43 (NCI-H2347, NCI-H1792, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.596×** | -4.3 | 9e-04 | 14/44 (A498, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.772×** | -4.1 | 0.002 | 15/45 (SK-MEL-2, COLO 205, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.620×** | -3.9 | 0.003 | 14/42 (A498, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.787×** | -3.8 | 0.006 | 11/46 (NCI-H460, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.014 | 9/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.808×** | -3.4 | 0.024 | 5/48 (CFPAC-1, J82, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | **0.802×** | -3.2 | 0.038 | 12/43 (HepG2/C3A, HCT15, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.681×** | -3.2 | 0.043 | 10/45 (NCI-H460, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.813×** | -3.1 | 0.056 | 10/46 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.691×** | -3.0 | 0.059 | 11/45 (SW 900, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -3.0 | 0.066 | 11/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.282× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 11.6 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 16.2 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -10.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 15.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0597× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 8.98 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -12.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.0980× (z -9.0) |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0906× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 7.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0594× (z -10.3) |
| [[KATO III (line)]] | alt | 9.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 7.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0555× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYPOP]] | +0.74 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[IFT172]] | +0.72 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ZFP14]] | +0.72 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[USP30]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.70 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[NCK1]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PCTP]] | +0.69 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[ZNF559]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[DPY30]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[C12orf76]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.67 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPR2-AS1]] | -0.64 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[DGKH]] | -0.63 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[PSMD6-AS1]] | -0.62 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[FLG-AS1]] | -0.62 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NR2F1-AS1]] | -0.62 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[LINC01934]] | -0.62 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[NEK10]] | -0.62 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[MSRA]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ST7L]] | -0.61 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[TRIP12]] | -0.61 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[CYREN]] | -0.61 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[SLC2A9]] | -0.60 | -0.58 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.1, -10.3); signed map (-30.4, -9.3). **Vector** length 75.4, 13.1% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.1 | -11.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.0 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.8 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -4.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | prune exopolyphosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,008,420-151,035,713 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRES-17, HTCD37, H-PRUNE; previously PRUNE |
| Gene groups (HGNC) | PRUNE family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TP1](https://www.uniprot.org/uniprotkb/Q86TP1) (Exopolyphosphatase PRUNE1):

> Exopolyphosphatase that catalyzes the hydrolysis of inorganic polyphosphates, with preference for short-chain substrates, as well as nucleoside 5'-tetraphosphates, releasing terminal phosphate residues. Also exhibits phosphodiesterase activity toward cyclic nucleotides, hydrolyzing cAMP and cGMP to their corresponding 5'-monophosphates. Requires divalent metal ions for activity. Plays a role in cell proliferation, migration and differentiation, and acts as a negative regulator of NME1. Plays a …

**Summary**, from NCBI Gene [58497](https://www.ncbi.nlm.nih.gov/gene/58497):

> This gene encodes a member of the DHH protein superfamily of phosphoesterases. This protein has been found to function as both a nucleotide phosphodiesterase and an exopolyphosphatase. This protein is believed to stimulate cancer progression and metastases through the induction of cell motility. A pseuodgene has been identified on chromosome 13. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:13420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13420) · Entrez [58497](https://www.ncbi.nlm.nih.gov/gene/58497) · UniProt [Q86TP1](https://www.uniprot.org/uniprotkb/Q86TP1) · Ensembl [ENSG00000143363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143363)

## Data

Gene col 6721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6721); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6721]; `tensor/DDL_lfc|DDL_z.npy` [6721]; `embed/gene_vectors.npy` [6721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6721 or target_col == 6721). Every well: [[PRUNE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRUNE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
