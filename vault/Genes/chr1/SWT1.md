---
symbol: "SWT1"
type: "gene"
col: 3816
ensembl_id: "ENSG00000116668"
name: "SWT1 RNA endoribonuclease homolog"
location: "1q25.3"
module: 1
arm: "-"
pooled_cpm: 32.26
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 14
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SWT1

*SWT1 RNA endoribonuclease homolog* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +12.2, q 2e-31, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.554× (z -10.1, q 5e-21, down in 37 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.487× (z -6.4, q 2e-08, down in 30 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A53]] (+0.69, fdr 1e-05), [[YPEL5]] (+0.65, fdr 1e-05), [[RAB22A]] (+0.64, fdr 1e-05); moves opposite to [[RIOK1]] (-0.64, fdr 7e-06), [[HNRNPD]] (-0.64, fdr 7e-06), [[ZNHIT6]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +12.2 | 2e-31 | 42/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +7.5 | 2e-11 | 30/48 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 9e-08 | 27/48 (SNU-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 8e-06 | 27/47 (HOP62, RKO, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 9e-06 | 27/48 (HT-29, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.39×** | +5.3 | 9e-06 | 26/48 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +5.2 | 2e-05 | 28/47 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.73×** | +4.9 | 8e-05 | 22/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.66×** | +4.5 | 5e-04 | 21/49 (SW480, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +4.4 | 5e-04 | 17/48 (HT-29, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +4.3 | 7e-04 | 18/49 (C32, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +3.9 | 0.004 | 18/48 (A498, A-172, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.008 | 10/48 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.009 | 10/49 (NCI-H460, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.010 | 20/48 (C32, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.011 | 21/46 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.016 | 14/47 (C32, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.017 | 18/48 (LoVo, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.554×** | -10.1 | 5e-21 | 37/44 (A-427, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.569×** | -8.9 | 2e-16 | 32/41 (HCT15, H4, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.583×** | -8.8 | 2e-16 | 24/38 (LOX-IMVI, A-172, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.670×** | -6.6 | 7e-09 | 33/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -6.4 | 2e-08 | 30/49 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.811×** | -5.0 | 4e-05 | 21/47 (NCI-H23, SNU-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **0.777×** | -4.3 | 0.001 | 24/46 (KATO III, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.624×** | -4.2 | 0.002 | 21/48 (LOX-IMVI, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.788×** | -4.1 | 0.003 | 17/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.789×** | -4.0 | 0.003 | 18/47 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -4.0 | 0.004 | 21/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.020 | 15/48 (SHP-77, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.688×** | -3.3 | 0.040 | 15/46 (COLO 205, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~76% of this change | **0.818×** | -3.3 | 0.040 | 20/47 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.836× | -3.1 | 0.083 | 19/47 (LS 180, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 35.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HT-29 (line)]] | alt | 33.0 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 53.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 35.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[C32 (line)]] | wt | 57.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 46.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0992× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 29.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.121× (z -9.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 34.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 47.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW480 (line)]] | alt | 24.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A498 (line)]] | wt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.111× (z -9.6) |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0873× (z -9.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 36.6 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0883× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[HS-578T (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -10.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW 900 (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A53]] | +0.69 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[YPEL5]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[RAB22A]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CAB39L]] | +0.61 | +0.64 / +0.37 | both halves | 9e-05 |  |
| [[BBIP1]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[EIF1]] | +0.57 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[BORCS7-ASMT]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[MICU1]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[HIGD2A]] | +0.57 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PRDM10]] | +0.57 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[C9orf153]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MAP1LC3B]] | +0.56 | +0.46 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOK1]] | -0.64 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[HNRNPD]] | -0.64 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[ZNHIT6]] | -0.63 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[SAAL1]] | -0.61 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[COG2]] | -0.60 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[FARSB]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[DHX9]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[AGK]] | -0.58 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[DLAT]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PDSS1]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PAK1IP1]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.58 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.432). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.5, -38.1); signed map (-12.5, 13.8). **Vector** length 101, 24.2% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.2 | +6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.8 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +3.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +5.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.9 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.4 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SWT1 RNA endoribonuclease homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:185,157,080-185,291,781 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20121, HsSwt1; previously C1orf26 |
| Gene groups (HGNC) | Endoribonucleases; PIN-like domain superfamily |
| Matched by | ensembl_id |

UniProt [Q5T5J6](https://www.uniprot.org/uniprotkb/Q5T5J6) carries no function annotation.

**Summary**, from NCBI Gene [54823](https://www.ncbi.nlm.nih.gov/gene/54823):

> Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16785) · Entrez [54823](https://www.ncbi.nlm.nih.gov/gene/54823) · UniProt [Q5T5J6](https://www.uniprot.org/uniprotkb/Q5T5J6) · Ensembl [ENSG00000116668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116668)

## Data

Gene col 3816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3816); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3816]; `tensor/DDL_lfc|DDL_z.npy` [3816]; `embed/gene_vectors.npy` [3816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3816 or target_col == 3816). Every well: [[SWT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SWT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
