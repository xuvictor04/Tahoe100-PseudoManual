---
symbol: "RFX7"
type: "gene"
col: 11217
ensembl_id: "ENSG00000181827"
name: "regulatory factor X7"
location: "15q21.3"
module: 169
arm: "+"
pooled_cpm: 163.85
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# RFX7

*regulatory factor X7* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.30× (z +7.2, q 3e-10, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.411× (z -15.7, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.537× (z -11.4, q 3e-28, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF148]] (+0.60, fdr 1e-05), [[ACBD6]] (+0.60, fdr 2e-05), [[TMLHE]] (+0.59, fdr 1e-05); moves opposite to [[HMGA1]] (-0.55, fdr 1e-05), [[CCNYL1]] (-0.51, fdr 2e-05), [[ADGRL1-AS1]] (-0.51, fdr 1e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TET1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +7.2 | 3e-10 | 39/49 (A498, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +4.8 | 4e-04 | 36/48 (SW48, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.003 | 34/47 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.004 | 27/48 (HOP62, RKO, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.7 | 0.020 | 18/48 (hTERT-HPNE, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.16× | +3.5 | 0.038 | 20/48 (A498, LoVo, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.054 | 26/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.10 | 21/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.10 | 6/48 (SW480, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.411×** | -15.7 | 0e+00 | 42/44 (C-33 A, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.432×** | -15.1 | 0e+00 | 46/49 (SW480, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.487×** | -12.2 | 3e-32 | 44/45 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.537×** | -11.4 | 3e-28 | 44/48 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.537×** | -11.4 | 3e-28 | 45/48 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.644×** | -10.5 | 6e-24 | 36/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -9.5 | 2e-19 | 39/49 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.604×** | -9.3 | 1e-18 | 39/48 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -8.6 | 4e-16 | 40/50 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.650×** | -7.9 | 1e-13 | 45/48 (C32, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -6.4 | 1e-08 | 32/48 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.753×** | -5.2 | 9e-06 | 34/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.776×** | -4.7 | 1e-04 | 28/48 (C32, AN3 CA, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.793×** | -4.2 | 0.001 | 28/48 (C32, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.806×** | -3.8 | 0.005 | 24/48 (C32, COLO 205, …) | rises with dose | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.808×** | -3.8 | 0.006 | 30/48 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.818×** | -3.7 | 0.008 | 27/48 (C32, NCI-H2030, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.051 | 20/47 (LOX-IMVI, C32, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.747×** | -3.0 | 0.086 | 22/48 (SK-MEL-2, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.851× | -3.0 | 0.089 | 22/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 457 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -29.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0678× (z -26.0) |
| [[LOX-IMVI (line)]] | wt | 251 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -18.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -14.5) |
| [[SNU-423 (line)]] | alt | 132 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 225 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.409× (z -12.4) |
| [[LS 180 (line)]] | wt | 193 | 2 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.61× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -12.1) |
| [[A-172 (line)]] | wt | 123 | 2 | 5 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.96× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.9) |
| [[HOP62 (line)]] | alt | 119 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -13.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 199 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -22.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.463× (z -9.7) |
| [[SW48 (line)]] | wt | 260 | 2 | 5 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.28× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.310× (z -12.4) |
| [[SW480 (line)]] | alt | 168 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.400× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 162 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -9.5) |
| [[J82 (line)]] | alt | 141 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 132 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 182 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.523× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 172 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -12.9) |
| [[PANC-1 (line)]] | alt | 173 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -13.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.547× (z -8.7) |
| [[SW1417 (line)]] | alt | 195 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.491× (z -10.1) |
| [[A549 (line)]] | wt | 215 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.98× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.1) |
| [[KATO III (line)]] | alt | 146 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.462× (z -9.7) |
| [[LoVo (line)]] | wt | 208 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 124 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 184 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.429× (z -8.8) |
| [[SHP-77 (line)]] | alt | 189 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.469× (z -9.7) |
| [[AN3 CA (line)]] | alt | 295 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -15.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 263 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0470× (z -36.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 294 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0968× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.279× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 201 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.1) |
| [[RKO (line)]] | wt | 238 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -11.3) |
| [[A-427 (line)]] | wt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -13.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.8) |
| [[COLO 205 (line)]] | alt | 139 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -11.6) |
| [[H4 (line)]] | wt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.384× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -8.8) |
| [[SW 1271 (line)]] | alt | 208 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -8.8) |
| [[A498 (line)]] | wt | 104 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.65× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HS-578T (line)]] | alt | 80.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 129 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF148]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ACBD6]] | +0.60 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[TMLHE]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[NDUFAF5]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TNRC6A]] | +0.57 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PANK1]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[IRAK1BP1]] | +0.55 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[GTF2I]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CUEDC2]] | +0.55 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[RAVER2]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RHOT1]] | +0.54 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[TGFBRAP1]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGA1]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[CCNYL1]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ADGRL1-AS1]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.50 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[PPARD]] | -0.49 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[ERN1]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PTPRH]] | -0.48 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[SEPTIN10]] | -0.48 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[KCTD5]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PDE2A]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[MIR22HG]] | -0.46 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[LINC02804]] | -0.46 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TET1]] | B | TET1 activity raises RFX7's level | lines that do not express TET1 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without TET1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[ZNF618]] | B | ZNF618 activity raises RFX7's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without ZNF618 | 0.023 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[SOBP]] | B | SOBP activity raises RFX7's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without SOBP | 0.069 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[ZNF618]] | B | ZNF618 activity strengthens RFX7's drug response | lines that do not express ZNF618 (9) vs lines expressing it (41) | the lines without ZNF618 respond 0.85× as strongly (z diff +1.38); strongest at Dinaciclib 0.5 µM: 0.62x vs 0.40x (z diff +3.7) | 0.076 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.8, 2.5); signed map (-26.5, -17.3). **Vector** length 109, 39.0% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +8.7 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.4 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.8 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.1 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.8 | -10.5 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -11.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.8 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.7 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | regulatory factor X7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:56,087,280-56,245,082 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12994; previously RFXDC2 |
| Gene groups (HGNC) | Regulatory factor X family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2KHR2](https://www.uniprot.org/uniprotkb/Q2KHR2) (DNA-binding protein RFX7):

> Transcription factor. Acts as a transcriptional activator by binding to promoter regions of target genes, such as PDCD4, PIK3IP1, MXD4, PNRC1, and RFX5. Plays a role in natural killer (NK) cell maintenance and immunity. May play a role in the process of ciliogenesis in the neural tube and neural tube closure (By similarity).

**Summary**, from NCBI Gene [64864](https://www.ncbi.nlm.nih.gov/gene/64864):

> RFX7 is a member of the regulatory factor X (RFX) family of transcription factors (see RFX1, MIM 600006) (Aftab et al., 2008 [PubMed 18673564]).[supplied by OMIM, Mar 2009]

**Accessions** — [HGNC:25777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25777) · Entrez [64864](https://www.ncbi.nlm.nih.gov/gene/64864) · UniProt [Q2KHR2](https://www.uniprot.org/uniprotkb/Q2KHR2) · Ensembl [ENSG00000181827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181827)

## Data

Gene col 11217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11217); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11217]; `tensor/DDL_lfc|DDL_z.npy` [11217]; `embed/gene_vectors.npy` [11217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11217 or target_col == 11217). Every well: [[RFX7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFX7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
