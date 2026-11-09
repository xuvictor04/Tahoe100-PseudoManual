---
symbol: "PPP2R3C"
type: "gene"
col: 1684
ensembl_id: "ENSG00000092020"
name: "protein phosphatase 2 regulatory subunit B''gamma"
location: "14q13.2"
module: 35
arm: "+"
pooled_cpm: 47.51
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PPP2R3C

*protein phosphatase 2 regulatory subunit B''gamma* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +27.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.675× (z -10.6, q 2e-23, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP4S1]] (+0.75, fdr 1e-05), [[ERCC6L2-AS1]] (+0.70, fdr 2e-04), [[ZNF341-AS1]] (+0.70, fdr 5e-05); moves opposite to [[TRABD]] (-0.62, fdr 3e-04), [[ERCC2]] (-0.61, fdr 3e-04), [[ST6GALNAC4]] (-0.61, fdr 3e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[olaparib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +27.5 | 0e+00 | 46/48 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +13.7 | 2e-40 | 38/48 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +12.7 | 7e-35 | 39/49 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.32×** | +10.6 | 3e-24 | 30/48 (NCI-H2030, NCI-H2347, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +9.8 | 2e-20 | 33/48 (NCI-H2030, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +9.7 | 3e-20 | 37/49 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +8.5 | 2e-15 | 28/48 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +7.5 | 6e-12 | 25/48 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +6.5 | 7e-09 | 24/47 (C32, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.23×** | +5.6 | 2e-06 | 23/48 (KATO III, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.22×** | +5.3 | 5e-06 | 20/48 (COLO 205, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +4.8 | 6e-05 | 20/48 (RKO, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +4.4 | 6e-04 | 20/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.15× | +3.7 | 0.010 | 16/48 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.2 | 0.046 | 12/48 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.675×** | -10.6 | 2e-23 | 33/48 (SNU-423, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.732×** | -8.4 | 2e-14 | 30/48 (SNU-423, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.746×** | -7.9 | 6e-13 | 27/48 (COLO 205, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.782×** | -6.6 | 5e-09 | 29/48 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.783×** | -6.6 | 5e-09 | 25/48 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.836× | -4.6 | 4e-04 | 20/47 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.739×** | -4.2 | 0.002 | 14/49 (NCI-H1792, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.902× | -3.9 | 0.007 | 11/48 (HS-578T, PANC-1, …) | top dose only |  |
| [[Relugolix (drug)]] 5 µM |  | 0.912× | -3.5 | 0.030 | 2/49 (NCI-H1573, RPMI-7951) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.875× | -3.5 | 0.031 | 10/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.919× | -3.2 | 0.065 | 9/48 (NCI-H1573, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 44.4 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +21.8) | — |
| [[SNU-423 (line)]] | alt | 50.8 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.4) | [[Bosentan (hydrate) (drug)]] 5 µM 0.329× (z -11.0) |
| [[A-427 (line)]] | wt | 37.1 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 42.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +17.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.5 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 59.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +21.5) | — |
| [[Panc 03.27 (line)]] | alt | 51.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +14.8) | — |
| [[SW480 (line)]] | alt | 47.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +19.9) | — |
| [[A549 (line)]] | wt | 57.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 42.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 55.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.3) | — |
| [[C32 (line)]] | wt | 37.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 45.3 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +14.1) | — |
| [[J82 (line)]] | alt | 52.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +13.8) | — |
| [[LoVo (line)]] | wt | 37.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 46.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 5 µM 0.419× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H460 (line)]] | wt | 46.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.3) | — |
| [[A-172 (line)]] | wt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.5) | — |
| [[A498 (line)]] | wt | 20.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 76.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 57.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 38.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +14.0) | — |
| [[Hs 766T (line)]] | wt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 38.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.9) | — |
| [[KATO III (line)]] | alt | 47.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 49.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 50.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 61.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 42.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +14.8) | — |
| [[RKO (line)]] | wt | 61.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SNU-1 (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 45.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 43.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +13.5) | — |
| [[SW48 (line)]] | wt | 56.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP4S1]] | +0.75 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ERCC6L2-AS1]] | +0.70 | +0.63 / +0.31 | both halves | 2e-04 |  |
| [[ZNF341-AS1]] | +0.70 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[SENP8]] | +0.66 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[GPAT4-AS1]] | +0.66 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[TP53]] | +0.66 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PBLD]] | +0.65 | +0.56 / +0.26 | both halves | 4e-04 |  |
| [[WAKMAR2]] | +0.64 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[USP34-DT]] | +0.64 | +0.55 / +0.28 | both halves | 3e-04 |  |
| [[MFF-DT]] | +0.63 | +0.58 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SMIM19]] | +0.63 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[NDUFAF1]] | +0.63 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PLCG1-AS1]] | +0.63 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRABD]] | -0.62 | -0.63 / -0.28 | both halves | 3e-04 |  |
| [[ERCC2]] | -0.61 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[ST6GALNAC4]] | -0.61 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[MAST3]] | -0.59 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[RRP1B]] | -0.59 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[NAA40]] | -0.58 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[USP35]] | -0.56 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[TRAF7]] | -0.56 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[SIPA1]] | -0.55 | -0.44 / -0.25 | both halves | 4e-04 |  |
| [[TBC1D24]] | -0.55 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[FBXW2]] | -0.55 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[ARHGAP8]] | -0.55 | -0.54 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[POLRMT]] | -0.55 | -0.51 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPP2R3C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises PPP2R3C's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[olaparib (drug)]] 5 µM | C | PPP2R3C's natural level raises the cells' numbers under olaparib 5 µM (protects the cells) | PPP2R3C's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.287 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | PPP2R3C's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | PPP2R3C's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.405 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (2.7, 14.6); signed map (23.6, -9.6). **Vector** length 102, 23.3% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.2 | +27.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +13.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +0.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit B''gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.2 — chr14:35,085,467-35,122,517 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20644, G4-1, G5PR; previously C14orf10 |
| Gene groups (HGNC) | Protein phosphatase 2 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969Q6](https://www.uniprot.org/uniprotkb/Q969Q6) (Serine/threonine-protein phosphatase 2A regulatory subunit B'' subunit gamma):

> May regulate MCM3AP phosphorylation through phosphatase recruitment (By similarity). May act as a negative regulator of ABCB1 expression and function through the dephosphorylation of ABCB1 by TFPI2/PPP2R3C complex. May play a role in the activation-induced cell death of B-cells (By similarity).

**Summary**, from NCBI Gene [55012](https://www.ncbi.nlm.nih.gov/gene/55012):

> This gene encodes a regulatory subunit of the serine/threonine phosphatase, protein phosphatase 2. This protein is localized to both nuclear and cytoplasmic regions depending on cell cycle phase. Homozygous conditional knockout mice for this gene exhibit reduced numbers and impaired proliferation of immune system B cells. This protein may regulate the expression of the P-glycoprotein ATP-binding cassette transporter through its phosphatase activity. Alternative splicing results in multiple …

**Accessions** — [HGNC:17485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17485) · Entrez [55012](https://www.ncbi.nlm.nih.gov/gene/55012) · UniProt [Q969Q6](https://www.uniprot.org/uniprotkb/Q969Q6) · Ensembl [ENSG00000092020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092020)

## Data

Gene col 1684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1684); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1684]; `tensor/DDL_lfc|DDL_z.npy` [1684]; `embed/gene_vectors.npy` [1684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1684 or target_col == 1684). Every well: [[PPP2R3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
