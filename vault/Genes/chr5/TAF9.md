---
symbol: "TAF9"
type: "gene"
col: 15804
ensembl_id: "ENSG00000273841"
name: "TATA-box binding protein associated factor 9"
location: "5q13.2"
module: 77
arm: "-"
pooled_cpm: 23.36
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TAF9

*TATA-box binding protein associated factor 9* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.28× (z +25.0, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.750× (z -4.3, q 0.010, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZXDA]] (+0.70, fdr 1e-05), [[NCOA4]] (+0.69, fdr 7e-06), [[ZXDB]] (+0.69, fdr 1e-05); moves opposite to [[LPCAT4]] (-0.65, fdr 3e-05), [[CSNK1G2]] (-0.64, fdr 1e-05), [[UQCRH]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BMI1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.28×** | +25.0 | 0e+00 | 45/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.63×** | +19.2 | 0e+00 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.46×** | +17.8 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +14.5 | 1e-45 | 32/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.57×** | +14.1 | 6e-43 | 40/43 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.23×** | +12.0 | 5e-31 | 41/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.20×** | +11.7 | 7e-30 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +10.5 | 6e-24 | 33/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +10.3 | 3e-23 | 31/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +9.0 | 1e-17 | 38/44 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.78×** | +8.6 | 5e-16 | 32/47 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +6.7 | 8e-10 | 27/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.4 | 7e-09 | 30/47 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.45×** | +5.5 | 1e-06 | 31/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +5.2 | 7e-06 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 3e-05 | 23/48 (LS 180, NCI-H460, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +4.2 | 9e-04 | 20/48 (A-172, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +4.2 | 9e-04 | 17/48 (PANC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.001 | 18/47 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.68×** | +4.0 | 0.001 | 17/48 (NCI-H460, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.004 | 20/47 (LS 180, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.58×** | +3.6 | 0.008 | 7/44 (SW48, SW480, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.010 | 11/44 (LoVo, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.011 | 10/47 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15804.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.750×** | -4.3 | 0.010 | 24/48 (HCT15, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.781×** | -3.7 | 0.059 | 16/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.714×** | -3.6 | 0.059 | 18/45 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **0.789×** | -3.5 | 0.059 | 16/47 (HS-578T, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | 0.791× | -3.2 | 0.14 | 14/47 (KATO III, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.7 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +22.2) | — |
| [[PANC-1 (line)]] | alt | 38.4 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +24.3) | — |
| [[SW480 (line)]] | alt | 24.9 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 18.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.03× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 17.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +16.2) | — |
| [[A-172 (line)]] | wt | 18.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +21.4) | — |
| [[A498 (line)]] | wt | 21.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +20.1) | — |
| [[LS 180 (line)]] | wt | 17.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 30.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +20.8) | — |
| [[COLO 205 (line)]] | alt | 15.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +10.8) | [[Allantoin (drug)]] 0.5 µM 0.181× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 17.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +15.3) | — |
| [[LoVo (line)]] | wt | 19.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +14.5) | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.4) | — |
| [[A549 (line)]] | wt | 25.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.55× (z +9.6) | — |
| [[C32 (line)]] | wt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 24.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +17.2) | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +11.9) | — |
| [[J82 (line)]] | alt | 29.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +12.7) | — |
| [[KATO III (line)]] | alt | 21.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 30.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 30.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[RKO (line)]] | wt | 34.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 20.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.4) | — |
| [[A-427 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -9.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.144× (z -8.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 7.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | +0.70 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.69 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.69 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.69 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[GMFB]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CCDC90B]] | +0.67 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[LACC1]] | +0.67 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[C17orf75]] | +0.66 | +0.69 / +0.31 | both halves | 2e-04 |  |
| [[THAP9]] | +0.66 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ZNF181]] | +0.66 | +0.70 / +0.39 | both halves | 6e-05 |  |
| [[RWDD2B]] | +0.66 | +0.70 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT4]] | -0.65 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[CSNK1G2]] | -0.64 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.63 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[UBE2G1]] | -0.62 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[TSEN54]] | -0.61 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD13D]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FOXK2]] | -0.61 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[COX6C]] | -0.61 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP2]] | -0.61 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[DRD4]] | -0.61 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[MARK4]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.60 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TAF9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MNX1]] | B | MNX1 activity raises TAF9's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without MNX1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMI1]] | C | TAF9's natural level weakens BMI1's drug response | TAF9's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.01; direction clear | 0.030 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-9.9, 1.6); signed map (12.1, -26.0). **Vector** length 73.6, 15.9% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +19.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +25.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +17.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.8 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | -0.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,362,026-69,370,013 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII31, TAFII32, TAFIID32, MGC5067, CGI-137, MGC1603, MGC3647, AD-004; previously TAF2G |
| Gene groups (HGNC) | General transcription factor IID complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 23 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16594](https://www.uniprot.org/uniprotkb/Q16594) (Transcription initiation factor TFIID subunit 9):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. TAF9 is also a component …

**Summary**, from NCBI Gene [6880](https://www.ncbi.nlm.nih.gov/gene/6880):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11542) · Entrez [6880](https://www.ncbi.nlm.nih.gov/gene/6880) · UniProt [Q16594](https://www.uniprot.org/uniprotkb/Q16594) · Ensembl [ENSG00000273841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273841)

## Data

Gene col 15804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15804); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15804]; `tensor/DDL_lfc|DDL_z.npy` [15804]; `embed/gene_vectors.npy` [15804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15804 or target_col == 15804). Every well: [[TAF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
