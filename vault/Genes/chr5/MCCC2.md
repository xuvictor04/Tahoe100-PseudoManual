---
symbol: "MCCC2"
type: "gene"
col: 5250
ensembl_id: "ENSG00000131844"
name: "methylcrotonyl-CoA carboxylase subunit 2"
location: "5q13.2"
module: 1
arm: "+"
pooled_cpm: 52.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MCCC2

*methylcrotonyl-CoA carboxylase subunit 2* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +27.5, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.752× (z -9.4, q 4e-18, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUF1]] (+0.77, fdr 7e-06), [[QTRT1]] (+0.76, fdr 7e-06), [[GTF3C6]] (+0.74, fdr 1e-05); moves opposite to [[PLIN3]] (-0.69, fdr 7e-06), [[NDRG1]] (-0.68, fdr 7e-06), [[ENO2]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +27.5 | 0e+00 | 41/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +15.1 | 0e+00 | 43/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +14.6 | 0e+00 | 38/48 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +13.1 | 4e-37 | 44/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +11.8 | 4e-30 | 37/48 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +11.7 | 7e-30 | 32/42 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +9.6 | 5e-20 | 30/48 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.3 | 9e-19 | 32/48 (SNU-423, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.4 | 3e-15 | 32/48 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +7.9 | 2e-13 | 32/48 (SNU-423, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +7.4 | 6e-12 | 26/45 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.5 | 1e-06 | 22/47 (NCI-H1573, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 1e-05 | 20/48 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.7 | 1e-04 | 17/37 (A-427, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.8 | 0.005 | 17/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.005 | 11/47 (BT-474, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.17× | +3.8 | 0.005 | 12/48 (SHP-77, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.8 | 0.005 | 11/48 (HepG2/C3A, HS-578T, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 1.11× | +3.5 | 0.012 | 1/48 (C-33 A) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.038 | 5/49 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.752×** | -9.4 | 4e-18 | 34/48 (KATO III, SW1417, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -7.1 | 4e-10 | 27/48 (SW480, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.764×** | -6.4 | 4e-08 | 27/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.780×** | -5.9 | 6e-07 | 23/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.642×** | -5.5 | 5e-06 | 21/48 (C32, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.805×** | -5.1 | 3e-05 | 23/48 (SW1417, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.831×** | -4.4 | 0.001 | 22/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -4.2 | 0.002 | 19/48 (SNU-1, RKO, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.842× | -3.9 | 0.006 | 14/48 (SW48, CHP-212, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -3.5 | 0.027 | 16/48 (SNU-1, RKO, …) | all doses, flat |  |
| [[γ-Oryzanol (drug)]] 0.05 µM |  | 0.877× | -3.1 | 0.096 | 6/48 (CFPAC-1, AN3 CA, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.879× | -3.1 | 0.10 | 8/48 (NCI-H23, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 38.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.5) | — |
| [[LoVo (line)]] | wt | 60.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +18.8) | — |
| [[PANC-1 (line)]] | alt | 60.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +23.9) | — |
| [[LS 180 (line)]] | wt | 55.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.437× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 54.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 40.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.5) | — |
| [[A-172 (line)]] | wt | 37.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 31.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +16.6) | — |
| [[H4 (line)]] | wt | 39.0 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.21× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 32.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 38.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.1) | [[AZD2858 (drug)]] 0.5 µM 0.196× (z -8.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 46.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 91.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +16.8) | — |
| [[NCI-H460 (line)]] | wt | 51.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.5) | [[Belinostat (drug)]] 5 µM 0.496× (z -8.7) |
| [[SNU-1 (line)]] | wt | 68.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.305× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 49.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +17.8) | — |
| [[SW48 (line)]] | wt | 68.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.7) | — |
| [[A-427 (line)]] | wt | 62.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 73.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 40.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.115× (z -9.9) |
| [[COLO 205 (line)]] | alt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +13.7) | — |
| [[HCT15 (line)]] | alt | 45.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 61.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.3) | — |
| [[J82 (line)]] | alt | 45.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.3) | — |
| [[KATO III (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 59.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 47.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 41.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.7) | — |
| [[SW480 (line)]] | alt | 81.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.509× (z -8.8) |
| [[A498 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 111 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUF1]] | +0.77 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[QTRT1]] | +0.76 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[GTF3C6]] | +0.74 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[SLC5A6]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 | pathway: Biotin transport and metabolism |
| [[POGLUT1]] | +0.71 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[SLC16A9]] | +0.69 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[OXCT1]] | +0.69 | +0.69 / +0.54 | both halves | 1e-05 | STRING 450 |
| [[SNX5]] | +0.68 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[FAIM]] | +0.68 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.68 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[VPS52]] | +0.67 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[USP24]] | +0.67 | +0.41 / +0.68 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLIN3]] | -0.69 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[NDRG1]] | -0.68 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[ENO2]] | -0.67 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.64 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.64 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.63 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[ARID3B]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.62 | -0.60 / -0.57 | both halves | 8e-06 |  |
| [[MAP3K9]] | -0.62 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[ATG4B]] | -0.62 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[MYO9B]] | -0.62 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[SH3GL1]] | -0.62 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MCCC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MCCC2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers MCCC2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GRIN2D]] | B | GRIN2D activity lowers MCCC2's level | lines that do not express GRIN2D (20) vs lines expressing it (30) | 1.19× higher at baseline in the lines without GRIN2D | 0.084 | ⚠ within organs, on part of the lines; also absent: MUC3A, TMEM139, RASSF6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.0, 6.5); signed map (21.2, -31.8). **Vector** length 125, 34.7% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.4 | +15.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +27.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.0 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +14.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.2 | +7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.7 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.2 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | methylcrotonyl-CoA carboxylase subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:71,579,531-71,658,706 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCCB, MCCCβ |
| Gene groups (HGNC) | Methylcrotonyl-CoA carboxylase subunits |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 10 pathways, smallest: Defective HLCS causes multiple carboxylase deficiency; Defects in biotin (Btn) metabolism; Biotin transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCC0](https://www.uniprot.org/uniprotkb/Q9HCC0) (Methylcrotonoyl-CoA carboxylase beta chain, mitochondrial):

> Carboxyltransferase subunit of the 3-methylcrotonyl-CoA carboxylase, an enzyme that catalyzes the conversion of 3-methylcrotonyl-CoA to 3-methylglutaconyl-CoA, a critical step for leucine and isovaleric acid catabolism.

**Summary**, from NCBI Gene [64087](https://www.ncbi.nlm.nih.gov/gene/64087):

> This gene encodes the small subunit of 3-methylcrotonyl-CoA carboxylase. This enzyme functions as a heterodimer and catalyzes the carboxylation of 3-methylcrotonyl-CoA to form 3-methylglutaconyl-CoA. Mutations in this gene are associated with 3-Methylcrotonylglycinuria, an autosomal recessive disorder of leucine catabolism. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, May 2018]

**Accessions** — [HGNC:6937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6937) · Entrez [64087](https://www.ncbi.nlm.nih.gov/gene/64087) · UniProt [Q9HCC0](https://www.uniprot.org/uniprotkb/Q9HCC0) · Ensembl [ENSG00000131844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131844)

## Data

Gene col 5250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5250); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5250]; `tensor/DDL_lfc|DDL_z.npy` [5250]; `embed/gene_vectors.npy` [5250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5250 or target_col == 5250). Every well: [[MCCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
