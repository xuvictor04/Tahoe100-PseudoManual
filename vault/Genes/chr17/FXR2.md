---
symbol: "FXR2"
type: "gene"
col: 4959
ensembl_id: "ENSG00000129245"
name: "FMR1 autosomal homolog 2"
location: "17p13.1"
module: 3
arm: "+"
pooled_cpm: 24.4
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# FXR2

*FMR1 autosomal homolog 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.93× (z +10.0, q 7e-21, up in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.70× (z +8.1, q 8e-14, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.771× (z -4.0, q 0.035, down in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (AN3 CA 0.0986×; ⚠ cell-cycle shift, explains ~16% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC34]] (+0.65, fdr 1e-05), [[YTHDF1]] (+0.64, fdr 1e-05), [[SDHAP1-1]] (+0.60, fdr 2e-05); moves opposite to [[PTGR2]] (-0.55, fdr 2e-05), [[LRPPRC]] (-0.55, fdr 1e-05), [[PAICS]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +10.0 | 7e-21 | 39/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.52×** | +9.0 | 8e-17 | 33/46 (HOP62, SW480, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +8.1 | 8e-14 | 36/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.63×** | +7.4 | 2e-11 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +6.0 | 2e-07 | 30/46 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.47×** | +5.8 | 5e-07 | 23/44 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.7 | 1e-06 | 1/47 (COLO 205) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.3 | 7e-06 | 26/46 (SW480, HCT15, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +5.2 | 2e-05 | 27/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 2e-05 | 28/44 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +4.9 | 6e-05 | 28/47 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.37×** | +4.6 | 2e-04 | 22/47 (SW480, NCI-H460, …) | top dose only | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +4.5 | 3e-04 | 19/47 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.34×** | +4.5 | 3e-04 | 20/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.4 | 4e-04 | 21/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.003 | 18/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.004 | 21/46 (HepG2/C3A, A498, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.011 | 17/47 (J82, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.014 | 19/47 (LS 180, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.025 | 14/46 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.028 | 11/47 (Hs 766T, A549, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.034 | 13/43 (HCT15, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.061 | 9/46 (HepG2/C3A, LoVo, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.061 | 7/47 (Hs 766T, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4959.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (AN3 CA 0.0986×; ⚠ cell-cycle shift, explains ~16% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.771×** | -4.0 | 0.035 | 13/47 (LoVo, SHP-77, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.8 | 6 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.63× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 21.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.97× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 26.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.85× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 17.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.99× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0986× (z -9.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +8.5) | — |
| [[A-172 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[YTHDF1]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 | STRING 505 |
| [[SDHAP1-1]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[MIGA2]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MAP2K2]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[SIRT7]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[HOTAIRM1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PIAS4]] | +0.57 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ZFAND2B]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SAT2]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 | ⚠ same locus (11.3 kb, same strand: neighbours can correlate without regulation) |
| [[BRI3]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ENKD1]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[FHIP2B]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGR2]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[LRPPRC]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[PAICS]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 | STRING 408 |
| [[XRCC5]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[IPO5]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[DARS2]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.51 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[IPO7]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[YWHAE]] | -0.49 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[HNRNPC]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 | STRING 709 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-7.6, -54.9); signed map (-27.9, 3.1). **Vector** length 62.0, 10.8% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | +2.7 | +5.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +2.2 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.1 | +9.0 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.0 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +3.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
| fall | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.5 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.3 | +0.2 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | FMR1 autosomal homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,591,230-7,614,897 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FMR1L2 |
| Gene groups (HGNC) | FMR1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [P51116](https://www.uniprot.org/uniprotkb/P51116) (RNA-binding protein FXR2):

> mRNA-binding protein that acts as a regulator of mRNAs translation and/or stability, and which is required for adult hippocampal neurogenesis (By similarity). Specifically binds to AU-rich elements (AREs) in the 3'-UTR of target mRNAs (By similarity). Promotes formation of some phase-separated membraneless compartment by undergoing liquid-liquid phase separation upon binding to AREs-containing mRNAs: mRNAs storage into membraneless compartments regulates their translation and/or stability (By …

**Summary**, from NCBI Gene [9513](https://www.ncbi.nlm.nih.gov/gene/9513):

> The protein encoded by this gene is a RNA binding protein containing two KH domains and one RCG box, which is similar to FMRP and FXR1. It associates with polyribosomes, predominantly with 60S large ribosomal subunits. This encoded protein may self-associate or interact with FMRP and FXR1. It may have a role in the development of fragile X cognitive disability syndrome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4024) · Entrez [9513](https://www.ncbi.nlm.nih.gov/gene/9513) · UniProt [P51116](https://www.uniprot.org/uniprotkb/P51116) · Ensembl [ENSG00000129245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129245)

## Data

Gene col 4959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4959); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4959]; `tensor/DDL_lfc|DDL_z.npy` [4959]; `embed/gene_vectors.npy` [4959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4959 or target_col == 4959). Every well: [[FXR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FXR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
