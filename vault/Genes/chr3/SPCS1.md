---
symbol: "SPCS1"
type: "gene"
col: 3600
ensembl_id: "ENSG00000114902"
name: "signal peptidase complex subunit 1"
location: "3p21.1"
module: 48
arm: "+"
pooled_cpm: 46.18
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# SPCS1

*signal peptidase complex subunit 1* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.34× (z +9.5, q 1e-18, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +4.9, q 1e-04, up in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (SW480 5.83×, A-172 5.84×, NCI-H1792 8.13×, NCI-H460 6.46×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (KATO III 5.58×, NCI-H460 6.91×, NCI-H1792 7.55×, SW480 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.311× (z -4.0, q 0.042, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (NCI-H661 0.0491×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRQ]] (+0.81, fdr 7e-06, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[ROMO1]] (+0.79, fdr 7e-06), [[SSR4]] (+0.78, fdr 7e-06), [[UBL5]] (+0.78, fdr 7e-06); moves opposite to [[SLC4A2]] (-0.63, fdr 1e-05), [[NRAS]] (-0.63, fdr 5e-05), [[SRSF3]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3600.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (SW480 5.83×, A-172 5.84×, NCI-H1792 8.13×, NCI-H460 6.46×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (KATO III 5.58×, NCI-H460 6.91×, NCI-H1792 7.55×, SW480 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **4.34×** | +9.5 | 1e-18 | 46/46 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.73×** | +8.2 | 6e-14 | 40/40 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.65×** | +5.8 | 1e-06 | 38/43 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.9 | 1e-04 | 43/48 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.92×** | +4.2 | 0.003 | 36/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.5 | 0.037 | 35/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.68×** | +3.4 | 0.059 | 32/47 (NCI-H460, LOX-IMVI, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.43×** | +3.3 | 0.070 | 37/48 (SK-MEL-2, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3600.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (NCI-H661 0.0491×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.311×** | -4.0 | 0.042 | 44/48 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.670×** | -3.7 | 0.068 | 35/48 (NCI-H2347, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Baicalin (drug)]] 5 µM |  | 0.719× | -3.0 | 0.32 | 35/48 (C32, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 58.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HOP62 (line)]] | alt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[KATO III (line)]] | alt | 65.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.58× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.13× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 52.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 46.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A498 (line)]] | wt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A549 (line)]] | wt | 32.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.89× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[CFPAC-1 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HS-578T (line)]] | alt | 62.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LOX-IMVI (line)]] | wt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LS 180 (line)]] | wt | 62.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H661 (line)]] | alt | 57.0 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0491× (z -10.0) |
| [[PANC-1 (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SNU-423 (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-427 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRQ]] ⚠ | +0.81 | +0.70 / +0.83 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.79 | +0.67 / +0.82 | both halves | 7e-06 |  |
| [[SSR4]] | +0.78 | +0.66 / +0.81 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 739 |
| [[UBL5]] | +0.78 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.78 | +0.59 / +0.82 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.77 | +0.53 / +0.85 | both halves | 1e-05 |  |
| [[ATP5PD]] | +0.77 | +0.63 / +0.80 | both halves | 7e-06 |  |
| [[ATP5F1E]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.74 | +0.55 / +0.79 | both halves | 1e-05 |  |
| [[NDUFA1]] | +0.74 | +0.60 / +0.82 | both halves | 7e-06 |  |
| [[COX6C]] | +0.73 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[C4orf48]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A2]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[NRAS]] | -0.63 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[SRSF3]] | -0.62 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SRSF6]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.58 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[GMFB]] | -0.58 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[SF3B4]] | -0.57 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[EWSR1]] | -0.57 | -0.28 / -0.65 | both halves | 3e-04 |  |
| [[UBA1]] | -0.56 | -0.46 / -0.65 | both halves | 2e-05 |  |
| [[ZNF460]] | -0.56 | -0.39 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.819). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.0, -22.1); signed map (-34.5, 9.8). **Vector** length 51.7, 17.5% of its response variance represented; |z| ≥ 3 in 525 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.63 to 31); *Respiratory electron transport* (reactome, mean cos +0.61 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.64 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +2.0 | +3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +0.8 | +1.1 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | +0.8 | +0.7 |
|  | [[Allantoin (drug)]] 0.5 µM |  | +0.8 | +0.7 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +0.8 | +0.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -5.5 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.1 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -4.9 | +9.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | -3.1 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.8 | +2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | signal peptidase complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,704,955-52,711,148 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPC12, HSPC033, YJR010C-A, SPC1 |
| Hallmark sets | PANCREAS_BETA_CELLS, UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 22 pathways, smallest: Synthesis, secretion, and inactivation of Glucose-dependent Insulinotropic Polypeptide (GIP); Synthesis, secretion, and deacylation of Ghrelin; Synthesis, secretion, and inactivation of Glucagon-like Peptide-1 (GLP-1) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6A9](https://www.uniprot.org/uniprotkb/Q9Y6A9) (Signal peptidase complex subunit 1):

> Component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum. Dispensable for SPC enzymatic activity (By similarity).; (Microbial infection) Required for the post-translational processing of proteins involved in virion assembly and secretion from flaviviruses such as West Nile virus (WNV), Japanese encephalitis virus (JEV), Dengue virus type 2 (DENV-2), …

**Summary**, from NCBI Gene [28972](https://www.ncbi.nlm.nih.gov/gene/28972):

> Predicted to enable ribosome binding activity. Involved in obsolete signal peptide processing; viral protein processing; and virion assembly. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23401) · Entrez [28972](https://www.ncbi.nlm.nih.gov/gene/28972) · UniProt [Q9Y6A9](https://www.uniprot.org/uniprotkb/Q9Y6A9) · Ensembl [ENSG00000114902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114902)

## Data

Gene col 3600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3600); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3600]; `tensor/DDL_lfc|DDL_z.npy` [3600]; `embed/gene_vectors.npy` [3600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3600 or target_col == 3600). Every well: [[SPCS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPCS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
