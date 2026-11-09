---
symbol: "POLR2D"
type: "gene"
col: 6858
ensembl_id: "ENSG00000144231"
name: "RNA polymerase II subunit D"
location: "2q14.3"
module: 1
arm: "+"
pooled_cpm: 31.6
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# POLR2D

*RNA polymerase II subunit D* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.89× (z +13.0, q 7e-36, up in 41 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.55× (z +9.3, q 1e-18, up in 33 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.246×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.190×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UMPS]] (+0.65, fdr 7e-06), [[CHAMP1]] (+0.65, fdr 7e-06), [[GEMIN4]] (+0.61, fdr 7e-06); moves opposite to [[CHP1]] (-0.56, fdr 1e-05), [[EPB41]] (-0.56, fdr 2e-05), [[TALAM1]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +13.0 | 7e-36 | 41/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.69×** | +11.1 | 4e-26 | 40/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.62×** | +10.2 | 3e-22 | 37/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +9.5 | 4e-19 | 35/48 (SW480, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +9.3 | 1e-18 | 33/47 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +8.5 | 2e-15 | 27/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +8.4 | 4e-15 | 32/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +8.2 | 2e-14 | 32/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.43×** | +7.6 | 2e-12 | 33/46 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +6.9 | 2e-10 | 27/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +6.2 | 2e-08 | 23/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +5.5 | 2e-06 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 6e-06 | 19/48 (A549, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.29×** | +5.2 | 6e-06 | 24/48 (AsPC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.2 | 9e-06 | 20/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.7 | 0.004 | 12/48 (NCI-H23, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.018 | 11/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.030 | 8/48 (A498, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.032 | 8/48 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.056 | 11/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6858.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.246×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.190×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -6.7 | 2e-08 | 5/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.888× | -3.6 | 0.092 | 8/48 (RKO, A-427, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.893× | -3.4 | 0.11 | 6/48 (A-427, NCI-H460, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.869× | -3.4 | 0.11 | 12/48 (CHP-212, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.0 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +15.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 32.5 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.246× (z -10.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 25.8 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +11.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 31.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +14.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 20.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CHP-212 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0754× (z -10.1) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 32.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 39.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 31.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.190× (z -9.1) |
| [[A-172 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UMPS]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |
| [[CHAMP1]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[GEMIN4]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PALB2]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[NIP7]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[TRMT5]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[NANP]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[EXOSC2]] | +0.57 | +0.62 / +0.56 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[ZNF239]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[TFAM]] | +0.57 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[PRPF4]] | +0.57 | +0.57 / +0.61 | both halves | 9e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TXLNA]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHP1]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[EPB41]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[TALAM1]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ERP29]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SPTBN1-AS2]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[PNKD]] | -0.53 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[SEZ6L2]] | -0.52 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[ST13]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[EFCAB14-AS1]] | -0.51 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[CLIP3]] | -0.51 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[TMEM219]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ALDH2]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-35.9, 14.1); signed map (3.1, -37.3). **Vector** length 82.9, 16.9% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.4 | +13.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +8.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | +3.8 | +7.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.3 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,843,553-127,858,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPB4 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 77 pathways, smallest: Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis; Abortive elongation of HIV-1 transcript in the absence of Tat |
| Matched by | ensembl_id |

**Function**, from UniProt [O15514](https://www.uniprot.org/uniprotkb/O15514) (DNA-directed RNA polymerase II subunit RPB4):

> Core component of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase which synthesizes mRNA precursors and many functional non-coding RNAs using the four ribonucleoside triphosphates as substrates. Pol II is the central component of the basal RNA polymerase II transcription machinery. It is composed of mobile elements that move relative to each other. POLR2D/RPB4 is part of a subcomplex with POLR2G/RPB7 that binds to a pocket formed by POLR2A/RPB1, POLR2B/RPB2 and POLR2F/RPABC2 at the …

**Summary**, from NCBI Gene [5433](https://www.ncbi.nlm.nih.gov/gene/5433):

> This gene encodes the fourth largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. In yeast, this polymerase subunit is associated with the polymerase under suboptimal growth conditions and may have a stress protective role. A sequence for a ribosomal pseudogene is contained within the 3' untranslated region of the transcript from this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9191) · Entrez [5433](https://www.ncbi.nlm.nih.gov/gene/5433) · UniProt [O15514](https://www.uniprot.org/uniprotkb/O15514) · Ensembl [ENSG00000144231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144231)

## Data

Gene col 6858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6858); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6858]; `tensor/DDL_lfc|DDL_z.npy` [6858]; `embed/gene_vectors.npy` [6858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6858 or target_col == 6858). Every well: [[POLR2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
