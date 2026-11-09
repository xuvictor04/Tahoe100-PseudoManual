---
symbol: "BANF1"
type: "gene"
col: 10597
ensembl_id: "ENSG00000175334"
name: "barrier to autointegration nuclear assembly factor 1"
location: "11q13.1"
module: 29
arm: "+"
pooled_cpm: 20.99
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# BANF1

*barrier to autointegration nuclear assembly factor 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.63× (z +17.5, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.38× (z +3.7, q 0.018, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.707× (z -5.6, q 1e-05, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (COLO 205 0.0654×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.282×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDX3]] (+0.69, fdr 1e-05), [[RBBP7]] (+0.68, fdr 7e-06), [[SUMO3]] (+0.68, fdr 7e-06); moves opposite to [[ATF4]] (-0.72, fdr 7e-06), [[SNHG32]] (-0.69, fdr 7e-06), [[WASHC1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.63×** | +17.5 | 0e+00 | 41/41 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.08×** | +15.5 | 0e+00 | 33/33 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.73×** | +10.6 | 4e-24 | 35/37 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.25×** | +8.9 | 5e-17 | 33/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.71×** | +6.2 | 9e-08 | 31/45 (HT-29, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.42×** | +3.9 | 0.011 | 21/46 (NCI-H1573, LoVo, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.018 | 19/47 (CFPAC-1, A549, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.37×** | +3.6 | 0.025 | 18/46 (NCI-H23, NCI-H460, …) | rises with dose | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.046 | 15/47 (NCI-H2030, A-427, …) | top dose only | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.082 | 13/46 (NCI-H1792, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.082 | 12/48 (PANC-1, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10597.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (COLO 205 0.0654×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.282×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.707×** | -5.6 | 1e-05 | 24/47 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.746× | -3.1 | 0.28 | 16/48 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.752× | -3.1 | 0.28 | 12/48 (SW480, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 19.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 25.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 36.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 23.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HT-29 (line)]] | alt | 20.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 43.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.4× (z +10.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.61× (z +10.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.7) |
| [[C32 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0654× (z -10.2) |
| [[H4 (line)]] | wt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.80× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.72× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SHP-77 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-423 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW 900 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX3]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[RBBP7]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 | STRING 492 |
| [[SUMO3]] | +0.68 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[USP5]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PPT1]] | +0.67 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[PRPS1]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CHID1]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CAPRIN1]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PAICS]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TMX1]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF4]] | -0.72 | -0.73 / -0.61 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[SNHG32]] | -0.69 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[WASHC1]] | -0.68 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[SNHG12]] | -0.68 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.67 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[SNHG11]] | -0.66 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.65 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[SAT2]] | -0.65 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[NPIPP1]] | -0.64 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.64 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[ZNF316]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-38.5, -29.9); signed map (-23.5, -41.3). **Vector** length 52.5, 8.64% of its response variance represented; |z| ≥ 3 in 660 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.7 | +17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | -0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.4 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | barrier to autointegration nuclear assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:66,002,228-66,004,149 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAF |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 21 pathways, smallest: Autointegration results in viral DNA circles; Integration of viral DNA into host genomic DNA; APOBEC3G mediated resistance to HIV-1 infection |
| Matched by | ensembl_id |

**Function**, from UniProt [O75531](https://www.uniprot.org/uniprotkb/O75531) (Barrier-to-autointegration factor):

> Non-specific DNA-binding protein that plays key roles in mitotic nuclear reassembly, chromatin organization, DNA damage response, gene expression and intrinsic immunity against foreign DNA. Contains two non-specific double-stranded DNA (dsDNA)-binding sites which promote DNA cross-bridging. Plays a key role in nuclear membrane reformation at the end of mitosis by driving formation of a single nucleus in a spindle-independent manner. Transiently cross-bridges anaphase chromosomes via its ability …

**Summary**, from NCBI Gene [8815](https://www.ncbi.nlm.nih.gov/gene/8815):

> The protein encoded by this gene was first identified by its ability to protect retroviruses from intramolecular integration and therefore promote intermolecular integration into the host cell genome. The protein forms a homodimer which localizes to both the nucleus and cytoplasm and is specifically associated with chromosomes during mitosis. This protein binds to double stranded DNA in a non-specific manner and also binds to LEM-domain containing proteins of the nuclear envelope. This protein …

**Accessions** — [HGNC:17397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17397) · Entrez [8815](https://www.ncbi.nlm.nih.gov/gene/8815) · UniProt [O75531](https://www.uniprot.org/uniprotkb/O75531) · Ensembl [ENSG00000175334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175334)

## Data

Gene col 10597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10597); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10597]; `tensor/DDL_lfc|DDL_z.npy` [10597]; `embed/gene_vectors.npy` [10597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10597 or target_col == 10597). Every well: [[BANF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BANF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
