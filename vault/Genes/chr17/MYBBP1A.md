---
symbol: "MYBBP1A"
type: "gene"
col: 5309
ensembl_id: "ENSG00000132382"
name: "MYB binding protein 1a"
location: "17p13.2"
module: 4
arm: "+"
pooled_cpm: 23.19
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MYBBP1A

*MYB binding protein 1a* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.51× (z +17.7, q 0e+00, up in 33 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 3.20× (z +9.0, q 2e-17, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.684× (z -8.1, q 4e-13, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1A]] (+0.83, fdr 7e-06), [[WDR4]] (+0.82, fdr 7e-06), [[PUM3]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +17.7 | 0e+00 | 33/34 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.14×** | +17.0 | 0e+00 | 40/44 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +12.8 | 2e-35 | 36/41 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.20×** | +9.0 | 2e-17 | 32/44 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +8.8 | 2e-16 | 37/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.5 | 4e-12 | 29/46 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.65×** | +7.5 | 6e-12 | 28/47 (NCI-H1573, AsPC-1, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.65×** | +7.1 | 1e-10 | 30/46 (NCI-H1792, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +7.0 | 2e-10 | 31/47 (SHP-77, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.57×** | +6.4 | 1e-08 | 26/44 (A549, NCI-H1792, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.50×** | +6.1 | 7e-08 | 25/47 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.50×** | +5.7 | 7e-07 | 22/43 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 2e-06 | 22/46 (NCI-H1792, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.84×** | +4.7 | 8e-05 | 16/44 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.83×** | +4.7 | 9e-05 | 11/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.6 | 2e-04 | 19/46 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.2 | 8e-04 | 16/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.002 | 15/46 (NCI-H460, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.004 | 17/46 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.005 | 14/45 (NCI-H460, LOX-IMVI, …) | all doses, flat | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.008 | 11/45 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Isocorydine (drug)]] 5 µM |  | 1.18× | +3.5 | 0.010 | 13/47 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.012 | 11/41 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -8.1 | 4e-13 | 30/46 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.804×** | -3.9 | 0.022 | 15/47 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.811×** | -3.9 | 0.022 | 14/47 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.780×** | -3.7 | 0.025 | 11/47 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.807×** | -3.6 | 0.038 | 14/47 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.793×** | -3.5 | 0.041 | 17/46 (RPMI-7951, A498, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.779×** | -3.5 | 0.041 | 8/46 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.787×** | -3.4 | 0.042 | 19/45 (A-427, C-33 A, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.851× | -3.4 | 0.042 | 14/47 (MIA PaCa-2, A-427, …) | all doses, flat | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.806×** | -3.3 | 0.065 | 13/47 (HCT15, NCI-H460, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.672×** | -3.1 | 0.093 | 11/46 (A-427, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.095 | 11/47 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.818× | -3.0 | 0.10 | 14/47 (LoVo, KATO III, …) | rises with dose |  |
| [[Vandetanib (drug)]] 5 µM |  | 0.819× | -3.0 | 0.10 | 15/46 (C-33 A, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Adagrasib (drug)]] 0.05 µM 0.617× (z -13.2) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.273× (z -10.5) |
| [[A-427 (line)]] | wt | 39.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.36× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.306× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 10.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A498 (line)]] | wt | 44.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.2) |
| [[LoVo (line)]] | wt | 19.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 52.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.56× (z +9.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 21.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HOP62 (line)]] | alt | 11.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[PANC-1 (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[RKO (line)]] | wt | 49.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -14.4) |
| [[SNU-423 (line)]] | alt | 9.99 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.85× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 35.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.32× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1A]] | +0.83 | +0.76 / +0.86 | both halves | 7e-06 | pathway: B-WICH complex positively regulates rRNA expression; STRING 964 |
| [[WDR4]] | +0.82 | +0.86 / +0.83 | both halves | 7e-06 | STRING 439 |
| [[PUM3]] | +0.82 | +0.80 / +0.84 | both halves | 7e-06 | STRING 851 |
| [[PFAS]] | +0.81 | +0.79 / +0.82 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 507 |
| [[BOP1]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 | STRING 915 |
| [[NOC2L]] | +0.79 | +0.80 / +0.78 | both halves | 7e-06 | same gene group; STRING 911 |
| [[EXOSC2]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[LETM1]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[FARSB]] | +0.78 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[URB2]] | +0.78 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[MDN1]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MYBBP1A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.4, -36.5); signed map (-5.2, -46.6). **Vector** length 113, 31.0% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.50 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.50 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +8.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.0 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.6 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -3.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | MYB binding protein 1a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,538,897-4,555,386 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P160, PAP2, FLJ37886, Pol5 |
| Gene groups (HGNC) | Armadillo like helical domain containing; B-WICH chromatin-remodelling complex subunits |
| Hallmark sets | MYC_TARGETS_V2, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: B-WICH complex positively regulates rRNA expression; Positive epigenetic regulation of rRNA expression; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQG0](https://www.uniprot.org/uniprotkb/Q9BQG0) (Myb-binding protein 1A):

> May activate or repress transcription via interactions with sequence specific DNA-binding proteins (By similarity). Repression may be mediated at least in part by histone deacetylase activity (HDAC activity) (By similarity). Acts as a corepressor and in concert with CRY1, represses the transcription of the core circadian clock component PER2 (By similarity). Preferentially binds to dimethylated histone H3 'Lys-9' (H3K9me2) on the PER2 promoter (By similarity). Has a role in rRNA biogenesis …

**Summary**, from NCBI Gene [10514](https://www.ncbi.nlm.nih.gov/gene/10514):

> This gene encodes a nucleolar transcriptional regulator that was first identified by its ability to bind specifically to the Myb proto-oncogene protein. The encoded protein is thought to play a role in many cellular processes including response to nucleolar stress, tumor suppression and synthesis of ribosomal DNA. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:7546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7546) · Entrez [10514](https://www.ncbi.nlm.nih.gov/gene/10514) · UniProt [Q9BQG0](https://www.uniprot.org/uniprotkb/Q9BQG0) · Ensembl [ENSG00000132382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132382)

## Data

Gene col 5309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5309); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5309]; `tensor/DDL_lfc|DDL_z.npy` [5309]; `embed/gene_vectors.npy` [5309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5309 or target_col == 5309). Every well: [[MYBBP1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYBBP1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
