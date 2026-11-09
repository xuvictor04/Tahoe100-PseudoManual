---
symbol: "ABI2"
type: "gene"
col: 6178
ensembl_id: "ENSG00000138443"
name: "abl interactor 2"
location: "2q33.2"
module: 12
arm: "-"
pooled_cpm: 136.29
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ABI2

*abl interactor 2* — 2q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.63× (z +11.7, q 5e-29, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.803× (z -5.1, q 2e-04, down in 25 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 0.849× (z -3.9, q 0.016, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A549 0.539×, C32 0.525×, C-33 A 0.541×, SNU-1 0.550×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.240×, A-427 0.524×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.467×, HS-578T 0.587×; ⚠ cell-cycle shift, explains ~21% of this change); [[Belzutifan (drug)]] 5 µM in 1 line (HCT15 0.257×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 0.523×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA6]] (+0.58, fdr 2e-05), [[BTBD3]] (+0.56, fdr 3e-05), [[ITM2C]] (+0.56, fdr 1e-05); moves opposite to [[FNBP4]] (-0.59, fdr 1e-05), [[CCDC59]] (-0.55, fdr 1e-05), [[XBP1]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[AKT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +11.7 | 5e-29 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.9 | 1e-16 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +7.6 | 5e-12 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +6.8 | 1e-09 | 32/48 (LoVo, LS 180, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +6.7 | 2e-09 | 32/48 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +6.7 | 2e-09 | 29/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +6.4 | 1e-08 | 34/49 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.4 | 1e-08 | 23/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +6.3 | 2e-08 | 28/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +6.0 | 1e-07 | 27/48 (LoVo, LS 180, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +5.9 | 2e-07 | 30/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 26/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.046 | 15/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +3.2 | 0.049 | 13/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.081 | 14/48 (A498, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6178.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A549 0.539×, C32 0.525×, C-33 A 0.541×, SNU-1 0.550×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.240×, A-427 0.524×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.467×, HS-578T 0.587×; ⚠ cell-cycle shift, explains ~21% of this change); [[Belzutifan (drug)]] 5 µM in 1 line (HCT15 0.257×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 0.523×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.803×** | -5.1 | 2e-04 | 25/47 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -4.9 | 2e-04 | 21/49 (A549, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.849× | -3.9 | 0.016 | 16/47 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.857× | -3.7 | 0.029 | 17/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.859× | -3.7 | 0.029 | 17/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.861× | -3.6 | 0.030 | 15/48 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.791×** | -3.4 | 0.046 | 19/48 (NCI-H23, LOX-IMVI, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 0.774× | -3.2 | 0.11 | 15/47 (HCT15, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.913× | -3.1 | 0.11 | 8/49 (NCI-H23, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.879× | -3.1 | 0.11 | 21/48 (C32, RKO, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.811× | -3.1 | 0.11 | 17/48 (hTERT-HPNE, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | 0.784× | -3.0 | 0.11 | 15/46 (NCI-H23, HCT15, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 54.4 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.9) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.87× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 38.1 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.80× (z +11.1) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.93× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 164 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 135 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +16.5) | — |
| [[C32 (line)]] | wt | 218 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -14.0) ⚠ cell-cycle shift, explains ~21% of this change |
| [[H4 (line)]] | wt | 129 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.64× (z +10.6) | — |
| [[SW480 (line)]] | alt | 171 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +18.7) | — |
| [[SNU-1 (line)]] | wt | 178 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 148 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 212 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.516× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 82.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +14.9) | — |
| [[C-33 A (line)]] | alt | 262 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 247 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 230 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +13.0) | — |
| [[A549 (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.330× (z -9.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 78.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.65× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 162 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.257× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 131 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 238 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -9.2) ⚠ cell-cycle shift, explains ~21% of this change |
| [[MIA PaCa-2 (line)]] | alt | 170 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.1) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.523× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 91.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.166× (z -11.3) ⚠ toxic |
| [[SW48 (line)]] | wt | 98.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +8.5) | — |
| [[A-172 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 215 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 144 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 159 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 97.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA6]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[BTBD3]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ITM2C]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TWSG1]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[GOLM2]] | +0.55 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[BRK1]] | +0.52 | +0.60 / +0.37 | both halves | 9e-05 | same gene group; pathway: FCGR3A-mediated phagocytosis; STRING 999 |
| [[EML4]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[PHC1]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[LPCAT2]] | +0.50 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[HDAC1]] | +0.50 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[PHTF2]] | +0.50 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[FAM102B]] | +0.50 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNBP4]] | -0.59 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CCDC59]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[XBP1]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CCDC174]] | -0.54 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[GOSR1]] | -0.53 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[GCC1]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[WHAMM]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[NRBF2]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[DNAJC2]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SRP19]] | -0.49 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[BTN2A1]] | -0.49 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[CNPY2]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKT3]] | B | AKT3 activity raises ABI2's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without AKT3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ABI2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ABI2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CEP170]] | C | CEP170 activity raises ABI2's level | lines that do not express CEP170 (4) vs lines expressing it (46) | 2.52× lower at baseline in the lines without CEP170 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, DNAJB5, SPAG17; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.404). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.9, 20.5); signed map (-29.7, -36.6). **Vector** length 122, 36.5% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.8 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -7.7 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.0 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.5 | -5.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.8 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | abl interactor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.2 — chr2:203,328,280-203,447,728 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ABI-2, AIP-1, ABI2B, AblBP3, argBPIA, SSH3BP2 |
| Gene groups (HGNC) | SCAR/WAVE complex; ABI family; SH3 domain containing |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYB9](https://www.uniprot.org/uniprotkb/Q9NYB9) (Abl interactor 2):

> Regulator of actin cytoskeleton dynamics underlying cell motility and adhesion. Functions as a component of the WAVE complex, which activates actin nucleating machinery Arp2/3 to drive lamellipodia formation. Acts as a regulator and substrate of nonreceptor tyrosine kinases ABL1 and ABL2 involved in processes linked to cell growth and differentiation. Positively regulates ABL1-mediated phosphorylation of ENAH, which is required for proper polymerization of nucleated actin filaments at the …

**Summary**, from NCBI Gene [10152](https://www.ncbi.nlm.nih.gov/gene/10152):

> Enables identical protein binding activity; signaling adaptor activity; and ubiquitin protein ligase binding activity. Contributes to small GTPase binding activity. Involved in several processes, including Rac protein signal transduction; positive regulation of cellular component organization; and zonula adherens assembly. Acts upstream of or within peptidyl-tyrosine phosphorylation. Located in several cellular components, including actin filament; filopodium tip; and lamellipodium. Part of …

**Accessions** — [HGNC:24011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24011) · Entrez [10152](https://www.ncbi.nlm.nih.gov/gene/10152) · UniProt [Q9NYB9](https://www.uniprot.org/uniprotkb/Q9NYB9) · Ensembl [ENSG00000138443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138443)

## Data

Gene col 6178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6178); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6178]; `tensor/DDL_lfc|DDL_z.npy` [6178]; `embed/gene_vectors.npy` [6178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6178 or target_col == 6178). Every well: [[ABI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
