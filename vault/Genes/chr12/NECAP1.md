---
symbol: "NECAP1"
type: "gene"
col: 1600
ensembl_id: "ENSG00000089818"
name: "NECAP endocytosis associated 1"
location: "12p13.31"
module: 17
arm: "+"
pooled_cpm: 26.6
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NECAP1

*NECAP endocytosis associated 1* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.59× (z +13.7, q 6e-40, up in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.54× (z +13.4, q 1e-38, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.664× (z -8.4, q 3e-14, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RKO 0.203×, SW480 0.492×, LOX-IMVI 0.361×, NCI-H460 0.426×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.121×, RPMI-7951 0.112×, SW1417 0.230×; ⚠ toxic; transcription drop); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (BT-474 0.153×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.190×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF114]] (+0.72, fdr 1e-05), [[PIGH]] (+0.68, fdr 9e-06), [[MRPL22]] (+0.65, fdr 7e-06); moves opposite to [[ZNF124]] (-0.60, fdr 4e-05), [[PARD6G-AS1]] (-0.60, fdr 5e-05), [[FKBP4]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIP4P1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +13.7 | 6e-40 | 45/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.54×** | +13.4 | 1e-38 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +12.9 | 5e-36 | 39/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.32×** | +9.0 | 3e-17 | 41/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +8.8 | 1e-16 | 43/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.69×** | +7.6 | 4e-12 | 35/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +7.3 | 2e-11 | 36/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.66×** | +7.0 | 2e-10 | 37/48 (A-427, SW480, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +6.9 | 3e-10 | 38/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +6.8 | 5e-10 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.6 | 2e-09 | 34/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.9 | 2e-07 | 31/47 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +4.7 | 1e-04 | 24/47 (SW480, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.008 | 15/48 (NCI-H2030, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +3.6 | 0.014 | 20/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.021 | 16/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.030 | 17/48 (LOX-IMVI, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.051 | 12/46 (H4, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.062 | 13/48 (A-427, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1600.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RKO 0.203×, SW480 0.492×, LOX-IMVI 0.361×, NCI-H460 0.426×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.121×, RPMI-7951 0.112×, SW1417 0.230×; ⚠ toxic; transcription drop); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (BT-474 0.153×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.190×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -8.4 | 3e-14 | 37/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -6.1 | 2e-07 | 22/35 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.9 | 0.017 | 5/48 (HCT15, BT-474, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.086 | 13/48 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.805× | -3.0 | 0.23 | 15/48 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.9 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.32× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 29.2 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 29.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.56× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 16.5 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.03× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +12.1) | — |
| [[KATO III (line)]] | alt | 33.9 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.39× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 26.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.6 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 25.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +9.1) | — |
| [[LoVo (line)]] | wt | 24.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 15.8 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.37× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.5) |
| [[A549 (line)]] | wt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.153× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.177× (z -8.6) |
| [[HOP62 (line)]] | alt | 23.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 46.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.6) | — |
| [[RKO (line)]] | wt | 30.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -12.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.190× (z -9.3) |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -9.0) |
| [[SW 1271 (line)]] | alt | 42.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -9.4) |
| [[SW1417 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF114]] | +0.72 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[PIGH]] | +0.68 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[MRPL22]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[METTL17]] | +0.65 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[PRPF39]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | +0.61 | +0.52 / +0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EDF1]] | +0.61 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TTC38]] | +0.61 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[WRAP73]] | +0.61 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[KBTBD3]] | +0.60 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[NDUFS4]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[NDUFA12]] | +0.59 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[GPATCH11]] | +0.58 | +0.39 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF124]] | -0.60 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[PARD6G-AS1]] | -0.60 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[FKBP4]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.58 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[E2F3]] | -0.58 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SECISBP2]] | -0.57 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[ATP11C]] | -0.56 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[EPM2A]] | -0.56 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[POC1B]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SUV39H2]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[C17orf80]] | -0.55 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ADSS2]] | -0.54 | -0.38 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIP4P1]] | C | PIP4P1's natural level weakens NECAP1's drug response | PIP4P1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.25; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (3.4, -5.6); signed map (-30.0, 1.4). **Vector** length 84.0, 19.6% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +8.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +6.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +1.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | NECAP endocytosis associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:8,076,939-8,097,881 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566B183 |
| Reactome | 6 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Cargo recognition for clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC96](https://www.uniprot.org/uniprotkb/Q8NC96) (Adaptin ear-binding coat-associated protein 1):

> Involved in endocytosis.

**Summary**, from NCBI Gene [25977](https://www.ncbi.nlm.nih.gov/gene/25977):

> This gene encodes a protein containing two characteristic WXXF motifs. The encoded protein localizes to clathrin-coated vesicles, where it binds components of the adapter protein complexes and aids in endocytosis. Loss of function of this gene results in early infantile epileptic encephalopathy-21. There is a pseudogene for this gene on chromosome 7. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:24539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24539) · Entrez [25977](https://www.ncbi.nlm.nih.gov/gene/25977) · UniProt [Q8NC96](https://www.uniprot.org/uniprotkb/Q8NC96) · Ensembl [ENSG00000089818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089818)

## Data

Gene col 1600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1600); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1600]; `tensor/DDL_lfc|DDL_z.npy` [1600]; `embed/gene_vectors.npy` [1600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1600 or target_col == 1600). Every well: [[NECAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NECAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
