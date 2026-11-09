---
symbol: "RIF1"
type: "gene"
col: 1279
ensembl_id: "ENSG00000080345"
name: "replication timing regulatory factor 1"
location: "2q23.3"
module: 1
arm: "+"
pooled_cpm: 196.74
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RIF1

*replication timing regulatory factor 1* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +16.9, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.696× (z -13.7, q 4e-40, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCLRE1A]] (+0.78, fdr 7e-06), [[TASOR]] (+0.73, fdr 7e-06), [[NOL11]] (+0.69, fdr 7e-06); moves opposite to [[TMEM50B]] (-0.67, fdr 7e-06), [[GUK1]] (-0.66, fdr 8e-06), [[COX7A2L]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +16.9 | 0e+00 | 38/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +14.7 | 0e+00 | 41/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +11.6 | 1e-28 | 42/48 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +10.2 | 4e-22 | 43/49 (AsPC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +10.0 | 2e-21 | 38/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +8.2 | 2e-14 | 42/48 (Panc 03.27, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +7.3 | 3e-11 | 32/48 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +7.1 | 8e-11 | 29/48 (NCI-H1792, AsPC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +5.9 | 3e-07 | 33/48 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.20×** | +4.9 | 6e-05 | 24/48 (NCI-H1792, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.4 | 6e-04 | 19/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +4.3 | 1e-03 | 19/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.7 | 0.010 | 11/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.2 | 0.055 | 16/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.12× | +3.0 | 0.087 | 17/48 (NCI-H1792, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -13.7 | 4e-40 | 38/49 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.714×** | -9.0 | 6e-17 | 39/48 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.742×** | -8.0 | 2e-13 | 37/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.752×** | -7.6 | 4e-12 | 35/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.712×** | -6.5 | 1e-08 | 42/48 (A498, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.795×** | -6.2 | 7e-08 | 27/48 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -5.7 | 8e-07 | 30/50 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -5.2 | 1e-05 | 27/48 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -5.0 | 3e-05 | 24/49 (BT-474, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.881× | -4.8 | 1e-04 | 12/48 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.842× | -4.6 | 2e-04 | 17/48 (A-427, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.847× | -4.4 | 4e-04 | 17/49 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.853× | -4.3 | 9e-04 | 16/48 (NCI-H23, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.850× | -4.2 | 0.001 | 21/47 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -4.2 | 0.001 | 20/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.817×** | -3.9 | 0.004 | 28/48 (HEC-1-A, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.871× | -3.7 | 0.007 | 13/48 (NCI-H23, SNU-1, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.890× | -3.1 | 0.052 | 11/48 (SW1417, A-427, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.062 | 12/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 297 | 4 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +20.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -14.5) |
| [[A498 (line)]] | wt | 274 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +21.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -21.0) |
| [[NCI-H23 (line)]] | alt | 312 | 2 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.84× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 327 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.437× (z -14.2) |
| [[A549 (line)]] | wt | 199 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +21.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 176 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.547× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 137 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +21.0) | — |
| [[SW480 (line)]] | alt | 228 | 2 | 4 | [[Harringtonine (drug)]] 0.5 µM 1.77× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 235 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 158 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.55× (z +12.9) | — |
| [[A-172 (line)]] | wt | 242 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -13.4) |
| [[C32 (line)]] | wt | 199 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -11.2) |
| [[HOP62 (line)]] | alt | 214 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.593× (z -9.1) |
| [[HS-578T (line)]] | alt | 153 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +16.2) | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 203 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 220 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +15.0) | [[Belinostat (drug)]] 5 µM 0.617× (z -8.8) |
| [[RKO (line)]] | wt | 251 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 203 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.487× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.524× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 204 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.09× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 75.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +17.7) | — |
| [[RPMI-7951 (line)]] | alt | 202 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 162 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -8.8) |
| [[C-33 A (line)]] | alt | 297 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -9.5) |
| [[HCT15 (line)]] | alt | 279 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.500× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -8.5) |
| [[HT-29 (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 208 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 192 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 142 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 214 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +8.9) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.4) |
| [[SNU-1 (line)]] | wt | 232 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.7) |
| [[SW 900 (line)]] | alt | 140 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 183 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 194 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -14.7) |
| [[COLO 205 (line)]] | alt | 123 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.55× (z +9.2) | — |
| [[H4 (line)]] | wt | 176 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 203 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +9.0) | — |
| [[SW48 (line)]] | wt | 240 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.5) |
| [[A-427 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 250 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 104 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 129 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 152 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 238 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | +0.78 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[TASOR]] | +0.73 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NOL11]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[UTP20]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 | same gene group |
| [[COA7]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SF3B3]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[CEP41]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[DDX20]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[U2SURP]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TFAM]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50B]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[GUK1]] | -0.66 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[COX7A2L]] | -0.65 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[TMED9]] | -0.64 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[TMEM165]] | -0.64 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[APTR]] | -0.63 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[SERF2]] | -0.63 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[RAB6A]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[UBTD1]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[TBC1D22A-DT]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[RAB5B]] | -0.61 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.61 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RIF1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HSF2BP]] | C | HSF2BP activity raises RIF1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without HSF2BP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.0, -37.3); signed map (3.0, -39.7). **Vector** length 134, 46.1% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.6 | +14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.1 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.8 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +16.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +11.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.5 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.8 | +2.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.1 | +2.4 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -6.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.5 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -13.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.8 | -1.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.7 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.3 | -2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | replication timing regulatory factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:151,409,883-151,508,013 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12870, FLJ10599 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 3 pathways, smallest: Nonhomologous End-Joining (NHEJ); DNA Double-Strand Break Repair; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5UIP0](https://www.uniprot.org/uniprotkb/Q5UIP0) (Telomere-associated protein RIF1):

> Key regulator of TP53BP1 that plays a key role in the repair of double-strand DNA breaks (DSBs) in response to DNA damage: acts by promoting non-homologous end joining (NHEJ)-mediated repair of DSBs. In response to DNA damage, interacts with ATM-phosphorylated TP53BP1. Interaction with TP53BP1 leads to dissociate the interaction between NUDT16L1/TIRR and TP53BP1, thereby unmasking the tandem Tudor-like domain of TP53BP1 and allowing recruitment to DNA DSBs. Once recruited to DSBs, RIF1 and …

**Summary**, from NCBI Gene [55183](https://www.ncbi.nlm.nih.gov/gene/55183):

> This gene encodes a protein that shares homology with the yeast teleomere binding protein, Rap1 interacting factor 1. This protein localizes to aberrant telomeres may be involved in DNA repair. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:23207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23207) · Entrez [55183](https://www.ncbi.nlm.nih.gov/gene/55183) · UniProt [Q5UIP0](https://www.uniprot.org/uniprotkb/Q5UIP0) · Ensembl [ENSG00000080345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080345)

## Data

Gene col 1279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1279); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1279]; `tensor/DDL_lfc|DDL_z.npy` [1279]; `embed/gene_vectors.npy` [1279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1279 or target_col == 1279). Every well: [[RIF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
