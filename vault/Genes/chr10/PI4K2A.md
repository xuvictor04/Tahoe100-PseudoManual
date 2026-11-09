---
symbol: "PI4K2A"
type: "gene"
col: 7878
ensembl_id: "ENSG00000155252"
name: "phosphatidylinositol 4-kinase type 2 alpha"
location: "10q24.2"
module: 34
arm: "+"
pooled_cpm: 25.42
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PI4K2A

*phosphatidylinositol 4-kinase type 2 alpha* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.66× (z +22.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.713× (z -5.8, q 4e-06, down in 24 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 0.807× (z -3.7, q 0.023, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.140×, MIA PaCa-2 0.144×, AsPC-1 0.206×, A498 0.272×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.0950×, LS 180 0.118×, RKO 0.246×, NCI-H2347 0.313×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.315×); [[Tucidinostat (drug)]] 5 µM in 1 line (NCI-H2347 0.505×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMC1]] (+0.57, fdr 3e-05), [[ABTB1]] (+0.56, fdr 5e-05), [[WNT7B]] (+0.54, fdr 4e-05); moves opposite to [[MTREX]] (-0.59, fdr 1e-05), [[SNX5]] (-0.52, fdr 2e-04), [[ARMCX5-GPRASP2]] (-0.51, fdr 6e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C7orf57]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.66×** | +22.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.31×** | +20.5 | 0e+00 | 46/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +20.0 | 0e+00 | 42/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.15×** | +19.7 | 0e+00 | 47/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.46×** | +15.5 | 0e+00 | 44/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +13.6 | 4e-40 | 39/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +12.5 | 3e-34 | 38/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +10.7 | 5e-25 | 37/47 (PANC-1, A-427, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +10.3 | 4e-23 | 37/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.82×** | +10.3 | 6e-23 | 40/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +9.3 | 8e-19 | 39/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +9.0 | 1e-17 | 31/48 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +9.0 | 1e-17 | 35/47 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.69×** | +9.0 | 1e-17 | 35/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.70×** | +8.9 | 2e-17 | 34/47 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +8.5 | 5e-16 | 32/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7878.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.140×, MIA PaCa-2 0.144×, AsPC-1 0.206×, A498 0.272×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.0950×, LS 180 0.118×, RKO 0.246×, NCI-H2347 0.313×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.315×); [[Tucidinostat (drug)]] 5 µM in 1 line (NCI-H2347 0.505×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -5.8 | 4e-06 | 24/43 (NCI-H1573, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.713×** | -5.6 | 7e-06 | 20/31 (Panc 03.27, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.720×** | -5.2 | 4e-05 | 17/38 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.852× | -3.9 | 0.014 | 18/48 (AsPC-1, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.807×** | -3.7 | 0.023 | 15/47 (AsPC-1, J82, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.807×** | -3.7 | 0.023 | 18/48 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.837× | -3.1 | 0.16 | 7/47 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.712× | -3.0 | 0.16 | 12/46 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.2 | 11 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.12× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.57× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 22.6 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.36× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0950× (z -19.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.0 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +12.3) | — |
| [[SW480 (line)]] | alt | 15.9 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.36× (z +16.2) | — |
| [[AsPC-1 (line)]] | alt | 42.5 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 36.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.1 | 4 | 0 | [[Belinostat (drug)]] 5 µM 4.60× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 11.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.57× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 54.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.505× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 38.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +18.6) | — |
| [[A549 (line)]] | wt | 24.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.57× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 13.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.84× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.69× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 36.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.54× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.6) | — |
| [[A498 (line)]] | wt | 48.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 35.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 11.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.5) | [[Docetaxel (drug)]] 0.05 µM 0.147× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~70% of this change |
| [[KATO III (line)]] | alt | 12.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.12× (z +9.4) | — |
| [[C32 (line)]] | wt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.3) | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0994× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 45.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.0) | — |
| [[J82 (line)]] | alt | 30.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +8.5) | — |
| [[RKO (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.9) | — |
| [[A-427 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMC1]] | +0.57 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ABTB1]] | +0.56 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[WNT7B]] | +0.54 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ATG2A]] | +0.52 | +0.43 / +0.38 | both halves | 7e-05 |  |
| [[BAK1]] | +0.52 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[FAM89B]] | +0.51 | +0.38 / +0.33 | both halves | 1e-04 |  |
| [[ARMC9]] | +0.51 | +0.47 / +0.27 | both halves | 3e-04 |  |
| [[SIGIRR]] | +0.51 | +0.34 / +0.33 | both halves | 1e-04 |  |
| [[PIM1]] | +0.50 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[NATD1]] | +0.49 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[PLEKHM1P1]] | +0.49 | +0.39 / +0.36 | both halves | 1e-04 |  |
| [[CRIPT]] | +0.49 | +0.39 / +0.41 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTREX]] | -0.59 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SNX5]] | -0.52 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.51 | -0.22 / -0.44 | both halves | 6e-04 |  |
| [[PM20D2]] | -0.49 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[RBM26]] | -0.49 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[MAIP1]] | -0.49 | -0.39 / -0.29 | both halves | 3e-04 |  |
| [[DDX39B]] | -0.47 | -0.35 / -0.21 | both halves | 6e-04 |  |
| [[KLRA1P]] | -0.47 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[TAF15]] | -0.47 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[ECHDC1]] | -0.47 | -0.25 / -0.32 | both halves | 4e-04 |  |
| [[BATF]] | -0.46 | -0.26 / -0.36 | both halves | 4e-04 |  |
| [[MAILR]] | -0.45 | -0.29 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C7orf57]] | B | C7orf57 activity raises PI4K2A's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 1.55× lower at baseline in the lines without C7orf57 | 0.050 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN |
| [[ABTB3]] | B | ABTB3 activity raises PI4K2A's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.23× lower at baseline in the lines without ABTB3 | 0.065 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, -1.4); signed map (-20.4, 12.7). **Vector** length 71.2, 15.7% of its response variance represented; |z| ≥ 3 in 1,288 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +20.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +22.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +19.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.6 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +10.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +6.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.4 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol 4-kinase type 2 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:97,640,671-97,676,434 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PI4KII, DKFZP761G1923, PIK42A |
| Gene groups (HGNC) | Phosphatidylinositol 4-kinase type 2 family |
| Reactome | 6 pathways, smallest: Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the Golgi membrane; Synthesis of PIPs at the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTU6](https://www.uniprot.org/uniprotkb/Q9BTU6) (Phosphatidylinositol 4-kinase type 2-alpha):

> Membrane-bound phosphatidylinositol-4 kinase (PI4-kinase) that catalyzes the phosphorylation of phosphatidylinositol (PI) to phosphatidylinositol 4-phosphate (PI4P), a lipid that plays important roles in endocytosis, Golgi function, protein sorting and membrane trafficking and is required for prolonged survival of neurons. Besides, phosphorylation of phosphatidylinositol (PI) to phosphatidylinositol 4-phosphate (PI4P) is the first committed step in the generation of phosphatidylinositol …

**Summary**, from NCBI Gene [55361](https://www.ncbi.nlm.nih.gov/gene/55361):

> Phosphatidylinositolpolyphosphates (PtdInsPs) are centrally involved in many biologic processes, ranging from cell growth and organization of the actin cytoskeleton to endo- and exocytosis. PI4KII phosphorylates PtdIns at the D-4 position, an essential step in the biosynthesis of PtdInsPs (Barylko et al., 2001 [PubMed 11244087]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30031) · Entrez [55361](https://www.ncbi.nlm.nih.gov/gene/55361) · UniProt [Q9BTU6](https://www.uniprot.org/uniprotkb/Q9BTU6) · Ensembl [ENSG00000155252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155252)

## Data

Gene col 7878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7878); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7878]; `tensor/DDL_lfc|DDL_z.npy` [7878]; `embed/gene_vectors.npy` [7878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7878 or target_col == 7878). Every well: [[PI4K2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PI4K2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
