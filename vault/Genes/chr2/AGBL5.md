---
symbol: "AGBL5"
type: "gene"
col: 1407
ensembl_id: "ENSG00000084693"
name: "AGBL carboxypeptidase 5"
location: "2p23.3"
module: 20
arm: "+"
pooled_cpm: 19.81
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# AGBL5

*AGBL carboxypeptidase 5* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +13.5, q 8e-39, up in 37 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.21× (z +4.7, q 3e-04, up in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 3.12×, PANC-1 2.53×, A-172 3.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 4.28×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.26×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.05×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.688× (z -9.1, q 3e-17, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.598× (z -8.6, q 3e-15, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPN1]] (+0.71, fdr 8e-06), [[STT3A]] (+0.68, fdr 7e-06), [[SPTLC1]] (+0.67, fdr 1e-05); moves opposite to [[MRPL36]] (-0.55, fdr 1e-04), [[TMEM70]] (-0.54, fdr 1e-04), [[MRPL46]] (-0.53, fdr 3e-04).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1407.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 3.12×, PANC-1 2.53×, A-172 3.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 4.28×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.26×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.05×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +13.5 | 8e-39 | 37/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +12.6 | 7e-34 | 23/30 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +9.5 | 6e-19 | 13/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +9.4 | 1e-18 | 25/37 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.7 | 3e-04 | 19/47 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.012 | 14/48 (NCI-H2030, SW1417, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +3.6 | 0.031 | 16/44 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.688×** | -9.1 | 3e-17 | 35/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.598×** | -8.6 | 3e-15 | 33/47 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -7.8 | 9e-13 | 31/47 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.646×** | -7.5 | 6e-12 | 35/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -6.7 | 3e-09 | 25/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.708×** | -6.0 | 2e-07 | 24/47 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.716×** | -5.8 | 6e-07 | 22/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.729×** | -5.5 | 3e-06 | 21/47 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.737×** | -5.3 | 8e-06 | 20/47 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -4.8 | 7e-05 | 18/47 (SW 1271, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -4.7 | 1e-04 | 17/48 (NCI-H460, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -4.3 | 7e-04 | 17/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.782×** | -4.3 | 9e-04 | 20/47 (LOX-IMVI, A549, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.784×** | -4.2 | 0.001 | 18/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.793×** | -3.9 | 0.004 | 11/44 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.810×** | -3.4 | 0.018 | 12/48 (SW48, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.052 | 11/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Acetohexamide (drug)]] 5 µM |  | 0.881× | -3.1 | 0.054 | 5/48 (PANC-1, HS-578T, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.832×** | -3.1 | 0.061 | 17/47 (COLO 205, LoVo, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +10.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 23.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -8.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.111× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.26× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.153× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.181× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.272× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -8.8) |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0841× (z -10.8) |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0912× (z -9.2) |
| [[SW480 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | +0.71 | +0.57 / +0.71 | both halves | 8e-06 |  |
| [[STT3A]] | +0.68 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[SPTLC1]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[HDLBP]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[NCSTN]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[COPG1]] | +0.65 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[CA5BP1-1]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ARF1]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LY6G5B]] | +0.63 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[COL20A1]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[GOLGA3]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL36]] | -0.55 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[TMEM70]] | -0.54 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[MRPL46]] | -0.53 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[KRI1]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ERVK3-1]] | -0.52 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[PIGBOS1]] | -0.52 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[CELF1]] | -0.52 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[EIF5B]] | -0.51 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[PUS3]] | -0.51 | -0.27 / -0.60 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-23.0, -24.0); signed map (-18.1, -33.3). **Vector** length 84.2, 16.2% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +4.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.9 | +9.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Ivermectin (drug)]] 5 µM |  | +1.4 | +1.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -8.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.7 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | AGBL carboxypeptidase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,042,364-27,070,622 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21839, CCP5 |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDL9](https://www.uniprot.org/uniprotkb/Q8NDL9) (Cytosolic carboxypeptidase-like protein 5):

> Metallocarboxypeptidase that mediates deglutamylation of tubulin and non-tubulin target proteins. Catalyzes the removal of polyglutamate side chains present on the gamma-carboxyl group of glutamate residues within the C-terminal tail of alpha- and beta-tubulin. Cleaves alpha- and gamma-linked polyglutamate tubulin side-chain, as well as the branching point glutamate. Also catalyzes the removal of alpha-linked glutamate residues from the carboxy-terminus of alpha-tubulin. Mediates …

**Summary**, from NCBI Gene [60509](https://www.ncbi.nlm.nih.gov/gene/60509):

> This gene encodes a metallocarboxypeptidase involved in protein deglutamylation and a member of the peptidase M14 family of proteins. The encoded protein has been described as a "dual-functional" deglutamylase that can remove glutamate residues from both carboxyl termini and side chains of protein substrates. This deglutamylase activity may be important in antiviral immunity. Mutations in this gene are associated with retinitis pigmentosa. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:26147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26147) · Entrez [60509](https://www.ncbi.nlm.nih.gov/gene/60509) · UniProt [Q8NDL9](https://www.uniprot.org/uniprotkb/Q8NDL9) · Ensembl [ENSG00000084693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084693)

## Data

Gene col 1407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1407); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1407]; `tensor/DDL_lfc|DDL_z.npy` [1407]; `embed/gene_vectors.npy` [1407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1407 or target_col == 1407). Every well: [[AGBL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGBL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
