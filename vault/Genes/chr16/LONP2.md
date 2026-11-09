---
symbol: "LONP2"
type: "gene"
col: 2290
ensembl_id: "ENSG00000102910"
name: "lon peptidase 2, peroxisomal"
location: "16q12.1"
module: 57
arm: "+"
pooled_cpm: 146.92
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# LONP2

*lon peptidase 2, peroxisomal* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.39× (z +7.8, q 5e-12, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.757× (z -9.1, q 3e-17, down in 30 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIGA1]] (+0.73, fdr 7e-06), [[SKIC3]] (+0.69, fdr 7e-06), [[MED23]] (+0.69, fdr 1e-05); moves opposite to [[HIVEP1]] (-0.63, fdr 1e-05), [[ERF]] (-0.63, fdr 1e-05), [[SATB2]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2290.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +7.8 | 5e-12 | 36/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +7.3 | 7e-11 | 37/48 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +7.1 | 2e-10 | 37/49 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +5.2 | 2e-05 | 28/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.2 | 0.003 | 23/48 (SW480, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.17× | +3.5 | 0.042 | 19/48 (A-172, A498, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.096 | 14/48 (NCI-H1792, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -9.1 | 3e-17 | 30/49 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -7.3 | 1e-10 | 33/47 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.754×** | -6.6 | 1e-08 | 29/48 (J82, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.782×** | -5.7 | 2e-06 | 29/48 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.797×** | -5.3 | 2e-05 | 28/49 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.803×** | -4.9 | 9e-05 | 26/48 (A498, COLO 205, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.821×** | -4.6 | 4e-04 | 29/48 (HOP62, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.823×** | -4.3 | 0.001 | 23/44 (A-427, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.893× | -3.7 | 0.012 | 18/48 (A498, C32, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.852× | -3.7 | 0.012 | 20/48 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.6 | 0.014 | 17/49 (LoVo, NCI-H460, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 0.858× | -3.4 | 0.026 | 20/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.747×** | -3.4 | 0.026 | 20/46 (C32, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.768×** | -3.4 | 0.026 | 20/48 (SHP-77, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.901× | -3.4 | 0.026 | 10/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.867× | -3.3 | 0.035 | 12/48 (NCI-H23, NCI-H460, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.777×** | -3.3 | 0.038 | 22/48 (LS 180, C32, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.864× | -3.1 | 0.056 | 15/47 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.910× | -3.1 | 0.059 | 3/48 (Hs 766T, H4, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 117 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -12.2) |
| [[A-427 (line)]] | wt | 101 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +17.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.71× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.0784× (z -32.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 167 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -11.1) |
| [[C32 (line)]] | wt | 175 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 117 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -11.2) |
| [[A498 (line)]] | wt | 195 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -16.9) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 186 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.05× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 112 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 150 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.88× (z +10.3) | — |
| [[A-172 (line)]] | wt | 157 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.02× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -8.6) |
| [[BT-474 (line)]] | alt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.9) |
| [[COLO 205 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.471× (z -8.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HT-29 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.518× (z -9.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[hTERT-HPNE (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.542× (z -8.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 140 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.21× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 187 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.19× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.430× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.657× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 83.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.77× (z +8.9) | — |
| [[RKO (line)]] | wt | 156 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.61× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.513× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 163 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 139 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 187 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 167 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 128 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 165 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIGA1]] | +0.73 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MED23]] | +0.69 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[RNF20]] | +0.67 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ATP5F1C]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[MRS2]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ACP1]] | +0.66 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[MINDY3]] | +0.66 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[SDHB]] | +0.65 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[VTI1B]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 | pathway: Protein localization |
| [[SLC35A3]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[VAMP7]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP1]] | -0.63 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ERF]] | -0.63 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[SATB2]] | -0.60 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TLNRD1]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[NFATC1]] | -0.57 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[GABBR1]] | -0.56 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CEACAM19]] | -0.56 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[EGLN2]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[PHLPP2]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[NPHS1]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[KDM6B]] | -0.54 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.1, -10.7); signed map (-32.2, -14.1). **Vector** length 112, 32.7% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.6 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.6 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | lon peptidase 2, peroxisomal |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:48,244,300-48,363,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4840, LONP, LONPL |
| Gene groups (HGNC) | AAA ATPases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 5 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Peroxisomal protein import; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WA8](https://www.uniprot.org/uniprotkb/Q86WA8) (Lon protease homolog 2, peroxisomal):

> ATP-dependent serine protease that mediates the selective degradation of misfolded and unassembled polypeptides in the peroxisomal matrix. Necessary for type 2 peroxisome targeting signal (PTS2)-containing protein processing and facilitates peroxisome matrix protein import (By similarity). May indirectly regulate peroxisomal fatty acid beta-oxidation through degradation of the self-processed forms of TYSND1.

**Summary**, from NCBI Gene [83752](https://www.ncbi.nlm.nih.gov/gene/83752):

> In human, peroxisomes function primarily to catalyze fatty acid beta-oxidation and, as a by-product, produce hydrogen peroxide and superoxide. The protein encoded by this gene is an ATP-dependent protease that likely plays a role in maintaining overall peroxisome homeostasis as well as proteolytically degrading peroxisomal proteins damaged by oxidation. The protein has an N-terminal Lon N substrate recognition domain, an ATPase domain, a proteolytic domain, and, in some isoforms, a C-terminal …

**Accessions** — [HGNC:20598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20598) · Entrez [83752](https://www.ncbi.nlm.nih.gov/gene/83752) · UniProt [Q86WA8](https://www.uniprot.org/uniprotkb/Q86WA8) · Ensembl [ENSG00000102910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102910)

## Data

Gene col 2290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2290); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2290]; `tensor/DDL_lfc|DDL_z.npy` [2290]; `embed/gene_vectors.npy` [2290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2290 or target_col == 2290). Every well: [[LONP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LONP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
