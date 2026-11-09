---
symbol: "CDIPT"
type: "gene"
col: 2375
ensembl_id: "ENSG00000103502"
name: "CDP-diacylglycerol--inositol 3-phosphatidyltransferase"
location: "16p11.2"
module: 29
arm: "+"
pooled_cpm: 13.31
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CDIPT

*CDP-diacylglycerol--inositol 3-phosphatidyltransferase* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.24× (z +24.6, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.665× (z -7.0, q 2e-09, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRN]] (+0.68, fdr 7e-06), [[PCMTD1]] (+0.67, fdr 1e-05), [[KIAA1191]] (+0.62, fdr 1e-05); moves opposite to [[CAAP1]] (-0.56, fdr 3e-05), [[ACSF3]] (-0.55, fdr 3e-05), [[METTL2A]] (-0.51, fdr 5e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.24×** | +24.6 | 0e+00 | 45/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +14.3 | 3e-44 | 24/26 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +14.2 | 3e-43 | 34/35 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +9.0 | 3e-17 | 38/47 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +8.9 | 6e-17 | 36/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.97×** | +7.5 | 5e-12 | 27/31 (HS-578T, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.77×** | +6.9 | 6e-10 | 33/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +6.2 | 4e-08 | 29/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.2 | 1e-05 | 26/41 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.53×** | +5.1 | 2e-05 | 28/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.0 | 3e-05 | 26/48 (PANC-1, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.48×** | +4.7 | 1e-04 | 24/47 (HEC-1-A, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.4 | 4e-04 | 21/43 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.84×** | +4.3 | 9e-04 | 14/45 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.002 | 18/47 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.028 | 9/48 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.043 | 9/42 (A-427, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.043 | 13/45 (SW1417, SW480, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.086 | 6/47 (A549, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.665×** | -7.0 | 2e-09 | 28/47 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -5.9 | 8e-07 | 27/45 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.624×** | -5.7 | 3e-06 | 23/47 (PANC-1, CHP-212, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -5.4 | 8e-06 | 31/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.639×** | -5.4 | 8e-06 | 29/47 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.653×** | -5.1 | 3e-05 | 24/47 (HepG2/C3A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.708×** | -3.9 | 0.007 | 16/48 (PANC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.722×** | -3.8 | 0.012 | 19/47 (SNU-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -3.7 | 0.014 | 21/46 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.749×** | -3.5 | 0.028 | 17/47 (LOX-IMVI, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.581×** | -3.4 | 0.033 | 12/48 (MIA PaCa-2, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.039 | 12/48 (NCI-H661, SHP-77, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.045 | 19/46 (HepG2/C3A, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.27 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +16.5) | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 13.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.7) |
| [[PANC-1 (line)]] | alt | 13.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +14.9) | — |
| [[SW480 (line)]] | alt | 10.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +16.8) | — |
| [[A-172 (line)]] | wt | 21.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +14.4) | — |
| [[A498 (line)]] | wt | 30.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +13.8) | — |
| [[A549 (line)]] | wt | 14.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +15.8) | — |
| [[HOP62 (line)]] | alt | 7.01 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 11.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.5) | — |
| [[KATO III (line)]] | alt | 20.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +17.4) | — |
| [[LOX-IMVI (line)]] | wt | 7.47 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 9.28 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 20.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +14.5) | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +10.4) | — |
| [[C32 (line)]] | wt | 8.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 10.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.120× (z -8.6) |
| [[Hs 766T (line)]] | wt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +10.7) | — |
| [[J82 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +11.3) | — |
| [[LoVo (line)]] | wt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.71× (z +15.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +9.8) | — |
| [[RKO (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.65× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 8.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +8.7) | — |
| [[SW48 (line)]] | wt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +9.2) | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRN]] | +0.68 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[PCMTD1]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[KIAA1191]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[RNF167]] | +0.62 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[UROD]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NCOA2]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ITM2B]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.61 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[TMEM59]] | +0.60 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[SLC39A6]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MAF1]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PCYOX1]] | +0.59 | +0.57 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAAP1]] | -0.56 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ACSF3]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[METTL2A]] | -0.51 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[PGBD1]] | -0.51 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[MPHOSPH6]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[NSRP1]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[EIF5B]] | -0.48 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[RAD23A]] | -0.48 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[JPX]] | -0.48 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[PIGL]] | -0.48 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[NDUFB9]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[PILRB]] | -0.48 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[EEFSEC]] | -0.48 | -0.33 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDIPT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-17.8, -17.4); signed map (-22.2, -31.0). **Vector** length 68.8, 12.9% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +24.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.1 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CDP-diacylglycerol--inositol 3-phosphatidyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,858,357-29,863,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIS1, PIS |
| Reactome | 4 pathways, smallest: Synthesis of PI; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14735](https://www.uniprot.org/uniprotkb/O14735) (CDP-diacylglycerol--inositol 3-phosphatidyltransferase):

> Catalyzes the biosynthesis of phosphatidylinositol (PtdIns) as well as PtdIns:inositol exchange reaction. May thus act to reduce an excessive cellular PtdIns content. The exchange activity is due to the reverse reaction of PtdIns synthase and is dependent on CMP, which is tightly bound to the enzyme.

**Summary**, from NCBI Gene [10423](https://www.ncbi.nlm.nih.gov/gene/10423):

> Phosphatidylinositol breakdown products are ubiquitous second messengers that function downstream of many G protein-coupled receptors and tyrosine kinases regulating cell growth, calcium metabolism, and protein kinase C activity. Two enzymes, CDP-diacylglycerol synthase and phosphatidylinositol synthase, are involved in the biosynthesis of phosphatidylinositol. Phosphatidylinositol synthase, a member of the CDP-alcohol phosphatidyl transferase class-I family, is an integral membrane protein …

**Accessions** — [HGNC:1769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1769) · Entrez [10423](https://www.ncbi.nlm.nih.gov/gene/10423) · UniProt [O14735](https://www.uniprot.org/uniprotkb/O14735) · Ensembl [ENSG00000103502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103502)

## Data

Gene col 2375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2375); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2375]; `tensor/DDL_lfc|DDL_z.npy` [2375]; `embed/gene_vectors.npy` [2375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2375 or target_col == 2375). Every well: [[CDIPT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDIPT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
