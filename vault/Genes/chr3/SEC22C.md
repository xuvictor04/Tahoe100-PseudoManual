---
symbol: "SEC22C"
type: "gene"
col: 1722
ensembl_id: "ENSG00000093183"
name: "SEC22 homolog C, vesicle trafficking protein"
location: "3p22.1"
module: 25
arm: "+"
pooled_cpm: 29.32
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SEC22C

*SEC22 homolog C, vesicle trafficking protein* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +14.7, q 1e-45, up in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.20× (z +4.0, q 0.004, up in 10 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 4.71×, HOP62 3.26×, PANC-1 2.19×, Panc 03.27 3.22×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 2.38×, PANC-1 2.31×, NCI-H1792 3.03×, LoVo 3.23×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 1.88×; ⚠ cell-cycle shift, explains ~63% of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.627× (z -10.9, q 1e-24, down in 31 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.712× (z -7.9, q 7e-13, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCBTB1]] (+0.57, fdr 1e-05), [[SGPL1]] (+0.56, fdr 4e-05), [[GMFB]] (+0.56, fdr 1e-05); moves opposite to [[KCNK6]] (-0.54, fdr 6e-05), [[SDCBP2]] (-0.51, fdr 3e-05), [[DTX2P1-UPK3BP1-PMS2P11]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1722.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 4.71×, HOP62 3.26×, PANC-1 2.19×, Panc 03.27 3.22×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 2.38×, PANC-1 2.31×, NCI-H1792 3.03×, LoVo 3.23×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 1.88×; ⚠ cell-cycle shift, explains ~63% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +14.7 | 1e-45 | 38/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +14.5 | 3e-45 | 28/35 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +11.7 | 2e-29 | 30/42 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.20× | +6.0 | 2e-07 | 21/48 (SW480, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.4 | 0.001 | 1/48 (hTERT-HPNE) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.004 | 17/48 (LS 180, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.20× | +4.1 | 0.004 | 17/47 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +4.0 | 0.004 | 10/48 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.008 | 11/47 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.008 | 12/48 (C32, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.16× | +3.5 | 0.025 | 5/48 (SW 900, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.025 | 6/48 (HS-578T, PANC-1, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.062 | 4/47 (HOP62, H4, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.2 | 0.062 | 6/48 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.068 | 7/48 (SW 1088, NCI-H2347, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.078 | 10/48 (NCI-H2030, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1722.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -10.9 | 1e-24 | 31/47 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -7.9 | 7e-13 | 32/48 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.715×** | -7.8 | 1e-12 | 30/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.722×** | -7.6 | 4e-12 | 28/48 (SW480, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.722×** | -7.6 | 4e-12 | 26/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.745×** | -6.8 | 7e-10 | 25/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.600×** | -6.2 | 4e-08 | 23/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.606×** | -6.1 | 7e-08 | 24/43 (J82, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.618×** | -5.9 | 3e-07 | 23/48 (A-427, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -5.8 | 3e-07 | 20/48 (J82, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.777×** | -5.5 | 2e-06 | 24/48 (HEC-1-A, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.792×** | -5.2 | 8e-06 | 20/48 (LOX-IMVI, HEC-1-A, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.742×** | -5.0 | 3e-05 | 16/48 (HEC-1-A, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.816×** | -4.7 | 1e-04 | 19/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -3.8 | 0.006 | 16/48 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.743×** | -3.6 | 0.010 | 10/48 (LOX-IMVI, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.881× | -2.9 | 0.099 | 14/48 (SW 1088, Hs 766T, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.914× | -2.9 | 0.099 | 4/48 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 41.9 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.443× (z -9.0) |
| [[RKO (line)]] | wt | 32.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.2) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.294× (z -9.2) |
| [[A-427 (line)]] | wt | 50.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.62× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.183× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 48.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -13.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -12.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.378× (z -9.0) |
| [[PANC-1 (line)]] | alt | 28.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -9.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SW480 (line)]] | alt | 32.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +11.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.483× (z -9.4) |
| [[A-172 (line)]] | wt | 46.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -9.4) ⚠ cell-cycle shift, explains ~63% of this change |
| [[COLO 205 (line)]] | alt | 8.35 | 0 | 2 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0645× (z -10.8) |
| [[LoVo (line)]] | wt | 18.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.426× (z -11.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[H4 (line)]] | wt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.41× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.351× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.144× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 29.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.7) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -12.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCBTB1]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SGPL1]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[GMFB]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ATL3]] | +0.55 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[ACAT1]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TMEM237]] | +0.55 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[SLC25A24]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[MTMR6]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[NIPSNAP3A]] | +0.53 | +0.43 / +0.51 | both halves | 4e-05 |  |
| [[ARL6IP6]] | +0.53 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[AIDA]] | +0.53 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[ABCB10]] | +0.53 | +0.33 / +0.64 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNK6]] | -0.54 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[SDCBP2]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[GPRC5C]] | -0.47 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[UBR1]] | -0.46 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[TRAPPC2B]] | -0.46 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[DTX2]] | -0.45 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CLDN4]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[IER5]] | -0.44 | -0.22 / -0.50 | both halves | 6e-04 |  |
| [[COX7A2]] ⚠ | -0.44 | -0.35 / -0.43 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC00958]] | -0.44 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[MIA]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[ZNF503]] | -0.44 | -0.20 / -0.50 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises SEC22C's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without KATNAL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[CERCAM]] | B | CERCAM activity raises SEC22C's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 2.14× lower at baseline in the lines without CERCAM | 0.006 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[CLDN4]] | B | CLDN4 activity lowers SEC22C's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 1.70× higher at baseline in the lines without CLDN4 | 0.029 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[GPRC5C]] | B | GPRC5C activity lowers SEC22C's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.48× higher at baseline in the lines without GPRC5C | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.1, -18.8); signed map (-14.6, -38.3). **Vector** length 85.5, 17.1% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +11.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +2.8 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.5 | +3.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.9 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +3.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -5.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -10.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | SEC22 homolog C, vesicle trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,547,969-42,601,080 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13261, MGC5373; previously SEC22L3 |
| Gene groups (HGNC) | SNAREs |
| Reactome | 6 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRL7](https://www.uniprot.org/uniprotkb/Q9BRL7) (Vesicle-trafficking protein SEC22c):

> May be involved in vesicle transport between the ER and the Golgi complex.

**Summary**, from NCBI Gene [9117](https://www.ncbi.nlm.nih.gov/gene/9117):

> This gene encodes a member of the SEC22 family of vesicle trafficking proteins. The encoded protein is localized to the endoplasmic reticulum and may play a role in the early stages of ER-Golgi protein trafficking. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:16828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16828) · Entrez [9117](https://www.ncbi.nlm.nih.gov/gene/9117) · UniProt [Q9BRL7](https://www.uniprot.org/uniprotkb/Q9BRL7) · Ensembl [ENSG00000093183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000093183)

## Data

Gene col 1722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1722); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1722]; `tensor/DDL_lfc|DDL_z.npy` [1722]; `embed/gene_vectors.npy` [1722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1722 or target_col == 1722). Every well: [[SEC22C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC22C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
