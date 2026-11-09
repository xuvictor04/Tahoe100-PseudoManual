---
symbol: "STIMATE"
type: "gene"
col: 13111
ensembl_id: "ENSG00000213533"
name: "STIM activating enhancer"
location: "3p21.1"
module: 159
arm: "+"
pooled_cpm: 13.89
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# STIMATE

*STIM activating enhancer* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.38× (z +28.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.789× (z -5.7, q 7e-06, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.282×, A-172 0.211×, RKO 0.324×, HS-578T 0.352×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (Panc 03.27 0.158×, LoVo 0.177×, HT-29 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H23 0.0980×, SNU-423 0.0773×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Tofacitinib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.165×); [[Trimetrexate (drug)]] 0.5 µM in 1 line (HCT15 0.107×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D24]] (+0.76, fdr 7e-06), [[NOMO3]] (+0.69, fdr 1e-05), [[ATRN]] (+0.69, fdr 1e-05); moves opposite to [[N4BP2L1]] (-0.66, fdr 4e-05), [[ABCA10]] (-0.66, fdr 3e-05), [[EIF4EBP3]] (-0.63, fdr 3e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[EXTL3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.38×** | +28.5 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.87×** | +26.8 | 0e+00 | 47/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.17×** | +24.2 | 0e+00 | 47/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +12.4 | 2e-33 | 40/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.89×** | +9.4 | 7e-19 | 38/47 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +8.4 | 3e-15 | 27/46 (A549, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +7.9 | 2e-13 | 29/46 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.39×** | +5.6 | 2e-06 | 15/47 (SW480, LS 180, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.4 | 4e-06 | 15/48 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.38×** | +4.3 | 0.001 | 12/41 (SW480, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.9 | 0.005 | 5/47 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.26×** | +3.9 | 0.005 | 13/47 (HOP62, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.27×** | +3.8 | 0.006 | 14/47 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.037 | 10/48 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.050 | 12/47 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.068 | 5/47 (LS 180, SW48, …) | top dose only |  |
| [[Neratinib (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.082 | 7/47 (A-172, C-33 A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.082 | 6/45 (C-33 A, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13111.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.282×, A-172 0.211×, RKO 0.324×, HS-578T 0.352×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (Panc 03.27 0.158×, LoVo 0.177×, HT-29 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H23 0.0980×, SNU-423 0.0773×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Tofacitinib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.165×); [[Trimetrexate (drug)]] 0.5 µM in 1 line (HCT15 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -5.7 | 7e-06 | 20/48 (A-427, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.781×** | -4.2 | 0.008 | 18/46 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.0 | 0.47 | 5/48 (HOP62, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.41× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[LOX-IMVI (line)]] | wt | 15.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.29× (z +10.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -8.8) ⚠ cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 20.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.40× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[HEC-1-A (line)]] | alt | 29.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 13.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 10.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.97× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[J82 (line)]] | alt | 21.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.27× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 8.57 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.65× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 8.80 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.09× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.07 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 9.48× (z +10.5) | [[Tofacitinib (drug)]] 0.05 µM 0.165× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 10.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.49× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.21× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 8.81 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 15.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +13.4) | — |
| [[RKO (line)]] | wt | 21.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.60× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.99× (z +16.7) | — |
| [[A-172 (line)]] | wt | 17.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 26.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +9.4) | — |
| [[A498 (line)]] | wt | 8.76 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.39× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 4.92 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.97× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0980× (z -11.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.35× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 12.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.55× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0773× (z -10.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 9.00 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.54× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 4.29 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.05× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.107× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 8.61 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.40× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 9.63 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.35× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 18.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 13.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D24]] | +0.76 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[NOMO3]] | +0.69 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ATRN]] | +0.69 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[NUP93]] | +0.67 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.66 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[TEX2]] | +0.66 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[COPG2]] | +0.65 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SEMA4F]] | +0.65 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[EXOC2]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PACC1]] | +0.65 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[SNTA1]] | +0.64 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[NOMO2]] | +0.63 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP2L1]] | -0.66 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ABCA10]] | -0.66 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[EIF4EBP3]] | -0.63 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | -0.63 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ANGPT2]] | -0.63 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ERCC6L2-AS1]] | -0.60 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[HELQ]] | -0.60 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[AK9]] | -0.59 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.59 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[OFD1]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.58 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[PATL2]] | -0.58 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXTL3]] | C | STIMATE's natural level weakens EXTL3's drug response | STIMATE's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.05; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.2, -26.4); signed map (-43.7, -13.8). **Vector** length 76.3, 14.4% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +26.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +24.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +28.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +7.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +9.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.4 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.9 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.2 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | STIM activating enhancer |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,836,219-52,897,548 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC52022; previously TMEM110 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TL2](https://www.uniprot.org/uniprotkb/Q86TL2) (Store-operated calcium entry regulator STIMATE):

> Acts as a regulator of store-operated Ca(2+) entry (SOCE) at junctional sites that connect the endoplasmic reticulum (ER) and plasma membrane (PM), called ER-plasma membrane (ER-PM) junction or cortical ER. SOCE is a Ca(2+) influx following depletion of intracellular Ca(2+) stores. Acts by interacting with STIM1, promoting STIM1 conformational switch. Involved in STIM1 relocalization to ER-PM junctions. Contributes to the maintenance and reorganization of store-dependent ER-PM junctions.

**Summary**, from NCBI Gene [375346](https://www.ncbi.nlm.nih.gov/gene/375346):

> Enables calcium channel regulator activity. Involved in activation of store-operated calcium channel activity and store-operated calcium entry. Located in cortical endoplasmic reticulum; endoplasmic reticulum membrane; and endoplasmic reticulum-plasma membrane contact site. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30526) · Entrez [375346](https://www.ncbi.nlm.nih.gov/gene/375346) · UniProt [Q86TL2](https://www.uniprot.org/uniprotkb/Q86TL2) · Ensembl [ENSG00000213533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213533)

## Data

Gene col 13111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13111); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13111]; `tensor/DDL_lfc|DDL_z.npy` [13111]; `embed/gene_vectors.npy` [13111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13111 or target_col == 13111). Every well: [[STIMATE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STIMATE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
