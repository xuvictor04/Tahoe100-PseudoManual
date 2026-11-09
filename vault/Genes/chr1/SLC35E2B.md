---
symbol: "SLC35E2B"
type: "gene"
col: 12118
ensembl_id: "ENSG00000189339"
name: "solute carrier family 35 member E2B"
location: "1p36.33"
module: 46
arm: "+"
pooled_cpm: 17.48
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# SLC35E2B

*solute carrier family 35 member E2B* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.33× (z +5.0, q 3e-04, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 3.18×; ⚠ cell-cycle shift, explains ~88% of this change).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.494× (z -12.5, q 5e-33, down in 39 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.571× (z -9.9, q 9e-21, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DICER1-AS1]] (+0.65, fdr 1e-05), [[CREBRF]] (+0.63, fdr 1e-05), [[TP53]] (+0.60, fdr 2e-05); moves opposite to [[EHD4]] (-0.66, fdr 1e-05), [[ST6GALNAC4]] (-0.55, fdr 5e-05), [[ENDOD1]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12118.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 3.18×; ⚠ cell-cycle shift, explains ~88% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-04 | 19/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.8 | 4e-04 | 13/46 (HEC-1-A, C32, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.44× | +3.4 | 0.13 | 6/46 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.23 | 4/47 (SW48, HS-578T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.39× | +3.0 | 0.24 | 5/47 (HEC-1-A, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.494×** | -12.5 | 5e-33 | 39/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.571×** | -9.9 | 9e-21 | 38/47 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.621×** | -8.4 | 8e-15 | 34/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.627×** | -8.3 | 2e-14 | 30/48 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.642×** | -7.8 | 5e-13 | 30/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.650×** | -7.6 | 2e-12 | 32/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.674×** | -7.0 | 2e-10 | 27/48 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -6.6 | 2e-09 | 28/48 (SW480, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.691×** | -6.5 | 4e-09 | 23/46 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -6.2 | 4e-08 | 24/47 (RPMI-7951, SNU-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.705×** | -6.0 | 1e-07 | 23/45 (LoVo, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.710×** | -5.7 | 5e-07 | 24/48 (AN3 CA, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.725×** | -5.7 | 5e-07 | 25/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.546×** | -5.6 | 9e-07 | 20/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.746×** | -5.2 | 8e-06 | 18/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.577×** | -5.1 | 1e-05 | 21/45 (Hs 766T, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.701×** | -4.5 | 2e-04 | 11/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.627×** | -4.3 | 4e-04 | 14/44 (SHP-77, RKO, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -4.2 | 6e-04 | 18/44 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.661×** | -3.8 | 0.003 | 11/46 (SNU-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.668×** | -3.7 | 0.004 | 11/45 (NCI-H460, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.806×** | -3.6 | 0.007 | 14/48 (Hs 766T, SNU-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.767×** | -3.4 | 0.016 | 6/48 (HS-578T, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.787×** | -3.0 | 0.044 | 9/47 (LOX-IMVI, SW 1088, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.249× (z -10.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -10.3) |
| [[SW480 (line)]] | alt | 19.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0846× (z -8.6) |
| [[HCT15 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.159× (z -9.3) |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -9.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[LoVo (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.395× (z -8.5) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -9.4) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.0) ⚠ cell-cycle shift, explains ~88% of this change | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.215× (z -8.5) |
| [[SW 900 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -9.6) |
| [[A-172 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DICER1-AS1]] | +0.65 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.63 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TP53]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SIAH1]] | +0.58 | +0.41 / +0.37 | both halves | 9e-05 |  |
| [[ZNF862]] | +0.58 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[APOLD1]] | +0.57 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[NIFK-AS1]] | +0.56 | +0.48 / +0.38 | both halves | 7e-05 |  |
| [[BICRAL]] | +0.56 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[ANAPC16]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TRAF3IP2-AS1]] | +0.56 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[RBM5]] | +0.56 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[RNF146]] | +0.56 | +0.45 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.66 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.55 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[ENDOD1]] | -0.54 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[RALB]] | -0.52 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[RNGTT]] | -0.52 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[GTF2E2]] | -0.51 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[CTNNBL1]] | -0.51 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[PIP4K2A]] | -0.51 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[GPR180]] | -0.50 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[LINC02693]] | -0.50 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[SIPA1]] | -0.50 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[KIF21B]] | -0.50 | -0.33 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (2.4, 19.5); signed map (24.4, -15.7). **Vector** length 56.4, 7.87% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +2.2 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.3 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -12.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.9 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -6.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.8 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.7 | -7.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member E2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,659,529-1,692,795 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [P0CK96](https://www.uniprot.org/uniprotkb/P0CK96) (Solute carrier family 35 member E2B):

> Putative transporter.

**Summary**, from NCBI Gene [728661](https://www.ncbi.nlm.nih.gov/gene/728661):

> Predicted to enable antiporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33941) · Entrez [728661](https://www.ncbi.nlm.nih.gov/gene/728661) · UniProt [P0CK96](https://www.uniprot.org/uniprotkb/P0CK96) · Ensembl [ENSG00000189339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189339)

## Data

Gene col 12118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12118); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12118]; `tensor/DDL_lfc|DDL_z.npy` [12118]; `embed/gene_vectors.npy` [12118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12118 or target_col == 12118). Every well: [[SLC35E2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35E2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
