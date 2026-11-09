---
symbol: "CABLES1"
type: "gene"
col: 5570
ensembl_id: "ENSG00000134508"
name: "Cdk5 and Abl enzyme substrate 1"
location: "18q11.2"
module: 46
arm: "+"
pooled_cpm: 28.53
n_lines_expressing: 44
n_dd_up: 41
n_dd_down: 7
n_dd_up_clean: 38
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# CABLES1

*Cdk5 and Abl enzyme substrate 1* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.28× (z +25.1, q 0e+00, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.528× (z -9.6, q 4e-19, down in 29 of 41 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.672× (z -4.3, q 0.002, down in 15 of 42 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT7-DT]] (+0.68, fdr 4e-05), [[NFIB]] (+0.65, fdr 1e-05), [[KLRK1-AS1]] (+0.64, fdr 5e-05); moves opposite to [[KIF21B]] (-0.61, fdr 2e-04), [[ARPC1A]] (-0.55, fdr 3e-04), [[GNAI3]] (-0.54, fdr 7e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); 1 goes from it, the strongest it → [[VPS29]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +25.1 | 0e+00 | 35/41 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +21.5 | 0e+00 | 29/42 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +11.0 | 7e-26 | 24/40 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +10.1 | 1e-21 | 27/39 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +8.0 | 2e-13 | 22/41 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +7.5 | 8e-12 | 30/41 (AsPC-1, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.2 | 6e-11 | 24/40 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +7.0 | 3e-10 | 23/41 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +6.7 | 1e-09 | 20/40 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.4 | 7e-09 | 19/42 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +6.4 | 8e-09 | 20/41 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +5.8 | 2e-07 | 19/42 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[NG25 (drug)]] 5 µM |  | **2.32×** | +5.0 | 3e-05 | 16/38 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +4.8 | 8e-05 | 15/39 (LoVo, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.8 | 8e-05 | 16/39 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.7 | 1e-04 | 20/39 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5570.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.528×** | -9.6 | 4e-19 | 29/41 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.545×** | -9.1 | 2e-17 | 26/41 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.553×** | -8.9 | 1e-16 | 27/41 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -4.6 | 5e-04 | 14/41 (BT-474, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.672×** | -4.3 | 0.002 | 15/42 (PANC-1, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -3.8 | 0.012 | 19/41 (COLO 205, HT-29, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.555×** | -3.5 | 0.039 | 10/39 (BT-474, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.0 | 0.18 | 10/42 (NCI-H460, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 52.0 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 37.2 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 67.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.327× (z -9.3) |
| [[A-172 (line)]] | wt | 11.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +13.6) | — |
| [[C32 (line)]] | wt | 20.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 77.6 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0872× (z -15.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.151× (z -12.2) |
| [[LS 180 (line)]] | wt | 22.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +16.3) | — |
| [[NCI-H1573 (line)]] | alt | 131 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -15.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.206× (z -10.6) |
| [[PANC-1 (line)]] | alt | 56.2 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.293× (z -12.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 24.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 8.40 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +17.4) | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 84.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -14.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 20.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +18.6) | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 35.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +13.2) | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0771× (z -12.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.11× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 8.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +10.4) | — |
| [[J82 (line)]] | alt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 82.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -14.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 4.32× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.0) | — |
| [[A-427 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT7-DT]] | +0.68 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[NFIB]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[KLRK1-AS1]] | +0.64 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[IQCH-AS1]] | +0.63 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[JADE2]] | +0.63 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[GRIP1]] | +0.63 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[HOXB7]] | +0.63 | +0.50 / +0.32 | both halves | 1e-04 |  |
| [[MTUS1-DT]] | +0.60 | +0.58 / +0.36 | both halves | 1e-04 |  |
| [[HOTAIR]] | +0.60 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[LRRN1]] | +0.60 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[ARID1B]] | +0.59 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[SLC25A21]] | +0.59 | +0.53 / +0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[ANXA2R-AS1]] | +0.59 | +0.57 / +0.24 | both halves | 5e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF21B]] | -0.61 | -0.58 / -0.30 | both halves | 2e-04 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[ARPC1A]] | -0.55 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[GNAI3]] | -0.54 | -0.55 / -0.21 | both halves | 7e-04 |  |
| [[PPARD]] | -0.54 | -0.55 / -0.22 | both halves | 6e-04 |  |
| [[EIF4EBP1]] | -0.53 | -0.57 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[YIF1B]] | -0.53 | -0.45 / -0.07 | ⚠ not reproduced | 0.004 |  |
| [[HDAC11]] | -0.53 | -0.54 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[PIGH]] | -0.53 | -0.36 / -0.20 | both halves | 7e-04 |  |
| [[FLNB]] | -0.53 | -0.50 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[AP1M1]] | -0.53 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[HIF1AN]] | -0.52 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[UBA6]] | -0.52 | -0.54 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZDHHC6]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PLEKHM1P1]] | -0.51 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[ZNF215]] | -0.51 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[CLTCL1]] | -0.50 | -0.29 / -0.25 | both halves | 4e-04 |  |
| [[ASCC2]] | -0.50 | -0.34 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity lowers CABLES1's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 2.16× higher at baseline in the lines without ZNF618 | 0.035 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[SYCP2]] | B | SYCP2 activity raises CABLES1's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.98× lower at baseline in the lines without SYCP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CABLES1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CABLES1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF215]] | B | ZNF215 activity lowers CABLES1's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.63× higher at baseline in the lines without ZNF215 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VPS29]] | B | CABLES1 activity raises VPS29's level | lines that do not express CABLES1 (6) vs lines expressing it (44) | 1.34× lower at baseline in the lines without CABLES1 | 0.068 | ⚠ within organs, on part of the lines; also absent: BAIAP2L1, ARMH1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (20.4, 15.3); signed map (32.1, -24.0). **Vector** length 121, 32.0% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.7 | +25.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +10.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.1 | -9.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -6.0 | -9.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.0 | -8.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | -4.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Cdk5 and Abl enzyme substrate 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:23,134,564-23,260,470 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT2563, FLJ35924 |
| Reactome | 9 pathways, smallest: Cyclin E associated events during G1/S transition; Cyclin A:Cdk2-associated events at S phase entry; G1/S Transition |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDN4](https://www.uniprot.org/uniprotkb/Q8TDN4) (CDK5 and ABL1 enzyme substrate 1):

> Cyclin-dependent kinase binding protein. Enhances cyclin-dependent kinase tyrosine phosphorylation by nonreceptor tyrosine kinases, such as that of CDK5 by activated ABL1, which leads to increased CDK5 activity and is critical for neuronal development, and that of CDK2 by WEE1, which leads to decreased CDK2 activity and growth inhibition. Positively affects neuronal outgrowth. Plays a role as a regulator for p53/p73-induced cell death (By similarity).

**Summary**, from NCBI Gene [91768](https://www.ncbi.nlm.nih.gov/gene/91768):

> This gene encodes a protein involved in regulation of the cell cycle through interactions with several cyclin-dependent kinases. One study (PMID: 16177568) reported aberrant splicing of transcripts from this gene which results in removal of the cyclin binding domain only in human cancer cells, and reduction in gene expression was shown in colorectal cancers (PMID: 17982127).Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:25097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25097) · Entrez [91768](https://www.ncbi.nlm.nih.gov/gene/91768) · UniProt [Q8TDN4](https://www.uniprot.org/uniprotkb/Q8TDN4) · Ensembl [ENSG00000134508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134508)

## Data

Gene col 5570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5570); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5570]; `tensor/DDL_lfc|DDL_z.npy` [5570]; `embed/gene_vectors.npy` [5570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5570 or target_col == 5570). Every well: [[CABLES1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CABLES1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
