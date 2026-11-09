---
symbol: "SAP30L-AS1"
type: "gene"
col: 14425
ensembl_id: "ENSG00000245275"
name: "SAP30L and GALNT10 antisense RNA 1"
location: "5q33.2"
module: 15
arm: "+"
pooled_cpm: 12.97
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SAP30L-AS1

*SAP30L and GALNT10 antisense RNA 1* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.22× (z +32.0, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.536× (z -7.4, q 6e-11, down in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.427× (z -5.5, q 1e-05, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF460-AS1]] (+0.76, fdr 7e-06), [[SEC24B-AS1]] (+0.71, fdr 1e-05), [[BCL2L2-PABPN1]] (+0.70, fdr 1e-05); moves opposite to [[SNAPIN]] (-0.62, fdr 7e-05), [[DHRS2]] (-0.61, fdr 2e-04), [[DPF1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC01139]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.22×** | +32.0 | 0e+00 | 45/45 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.04×** | +19.2 | 0e+00 | 45/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.57×** | +15.1 | 0e+00 | 44/47 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.87×** | +11.0 | 6e-26 | 34/48 (A-172, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.75×** | +6.6 | 4e-09 | 27/40 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +6.3 | 3e-08 | 23/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 26/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.53×** | +5.3 | 1e-05 | 23/47 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.31×** | +4.7 | 2e-04 | 21/48 (CFPAC-1, A498, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 2e-04 | 18/48 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.5 | 4e-04 | 22/46 (A498, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 5e-04 | 18/47 (HOP62, C-33 A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.41×** | +4.3 | 8e-04 | 16/47 (A549, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 16/48 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.41×** | +3.9 | 0.003 | 11/47 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.005 | 17/47 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.012 | 15/48 (SW1417, A-172, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.012 | 12/47 (A-427, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.017 | 10/48 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.536×** | -7.4 | 6e-11 | 30/46 (NCI-H1792, A-427, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.427×** | -5.5 | 1e-05 | 27/48 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.654×** | -5.3 | 3e-05 | 21/47 (NCI-H1573, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.701×** | -4.4 | 0.001 | 20/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -4.3 | 0.002 | 22/44 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -4.0 | 0.007 | 7/48 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.742×** | -3.7 | 0.017 | 18/46 (A-427, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.761×** | -3.4 | 0.046 | 17/46 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.762×** | -3.4 | 0.046 | 11/48 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.837× | -3.1 | 0.10 | 17/47 (PANC-1, A549, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.779× | -3.1 | 0.12 | 11/47 (C-33 A, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.8 | 2 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +15.2) | [[Harringtonine (drug)]] 5 µM 0.234× (z -10.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 14.3 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +18.0) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 14.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.89× (z +19.2) | — |
| [[HOP62 (line)]] | alt | 11.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.39× (z +15.6) | — |
| [[LoVo (line)]] | wt | 16.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 16.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.99× (z +18.0) | — |
| [[SW480 (line)]] | alt | 13.7 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.94× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 12.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.04× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 10.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.64× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -11.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H460 (line)]] | wt | 11.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +16.5) | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +17.0) | — |
| [[RKO (line)]] | wt | 12.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.53× (z +13.9) | — |
| [[A498 (line)]] | wt | 13.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +15.1) | — |
| [[A549 (line)]] | wt | 13.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 9.81 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.56× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 18.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +9.4) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.100× (z -9.7) |
| [[H4 (line)]] | wt | 10.7 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 17.7× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +12.2) | [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.0576× (z -12.5) |
| [[Hs 766T (line)]] | wt | 15.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.25 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +14.3) | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 12.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.0398× (z -14.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H23 (line)]] | alt | 14.4 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 13.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 5.01 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.05× (z +10.9) | — |
| [[A-427 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -13.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 7.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.97× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 9.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.79× (z +12.6) | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0969× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 9.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +13.0) | — |
| [[HCT15 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +10.5) | — |
| [[J82 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +12.0) | — |
| [[KATO III (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 6.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 9.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +12.1) | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +10.6) | — |
| [[SW48 (line)]] | wt | 8.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.50× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF460-AS1]] | +0.76 | +0.64 / +0.61 | both halves | 7e-06 | same gene group |
| [[SEC24B-AS1]] | +0.71 | +0.64 / +0.49 | both halves | 1e-05 | same gene group |
| [[BCL2L2-PABPN1]] | +0.70 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RNF217-AS1]] | +0.70 | +0.62 / +0.40 | both halves | 5e-05 | same gene group |
| [[ANXA2R-OT1]] | +0.70 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[SLC25A53]] | +0.69 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ZNF213-AS1]] | +0.69 | +0.60 / +0.56 | both halves | 1e-05 | same gene group |
| [[SPESP1]] | +0.68 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[FKBP14-AS1]] | +0.68 | +0.57 / +0.49 | both halves | 1e-05 | same gene group |
| [[DARS1-AS1]] | +0.68 | +0.64 / +0.45 | both halves | 3e-05 | same gene group |
| [[PHC2-AS1]] | +0.67 | +0.62 / +0.44 | both halves | 3e-05 | same gene group |
| [[VPS13B-DT]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPIN]] | -0.62 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[DHRS2]] | -0.61 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[DPF1]] | -0.58 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NTHL1]] | -0.58 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[WDR7]] | -0.58 | -0.20 / -0.56 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TTC26]] | -0.58 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[TBC1D19]] | -0.58 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[GPATCH11]] | -0.57 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[THEM6]] | -0.57 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[ZNF22]] | -0.57 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[NDUFA8]] | -0.56 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CEP290]] | -0.56 | -0.24 / -0.46 | both halves | 4e-04 |  |
| [[MIDEAS]] | -0.56 | -0.46 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01139]] | B | LINC01139 activity raises SAP30L-AS1's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.29× lower at baseline in the lines without LINC01139 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |
| [[TOP2A]] | B | TOP2A activity lowers SAP30L-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR4A1]] | B | NR4A1 activity lowers SAP30L-AS1's level | lines that do not express NR4A1 (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without NR4A1 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[MAP2K1]] | B | MAP2K1 activity lowers SAP30L-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.813). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.3, 21.8); signed map (18.3, -4.6). **Vector** length 86.0, 19.0% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +19.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +32.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +15.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +11.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.3 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.2 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SAP30L and GALNT10 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q33.2 — chr5:154,325,568-154,445,850 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ38109, GALNT10-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26760) · Entrez [386627](https://www.ncbi.nlm.nih.gov/gene/386627) · Ensembl [ENSG00000245275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245275)

## Data

Gene col 14425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14425); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14425]; `tensor/DDL_lfc|DDL_z.npy` [14425]; `embed/gene_vectors.npy` [14425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14425 or target_col == 14425). Every well: [[SAP30L-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAP30L-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
