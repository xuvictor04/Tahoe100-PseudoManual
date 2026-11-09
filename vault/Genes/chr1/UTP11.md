---
symbol: "UTP11"
type: "gene"
col: 11414
ensembl_id: "ENSG00000183520"
name: "UTP11 small subunit processome component"
location: "1p34.3"
module: 4
arm: "+"
pooled_cpm: 31.08
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# UTP11

*UTP11 small subunit processome component* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (21 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.18× (z +13.7, q 4e-40, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.349×; ⚠ cell-cycle shift, explains ~66% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.200×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD12]] (+0.72, fdr 7e-06), [[EIPR1]] (+0.68, fdr 1e-05), [[CCT6A]] (+0.68, fdr 7e-06); moves opposite to [[ZNF821]] (-0.67, fdr 1e-05), [[AKAP1-DT]] (-0.61, fdr 4e-05), [[RCOR3]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 22 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.18×** | +13.7 | 4e-40 | 47/48 (C32, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.66×** | +11.6 | 1e-28 | 41/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.44×** | +10.2 | 5e-22 | 30/37 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.79×** | +9.7 | 3e-20 | 38/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.01×** | +8.2 | 2e-14 | 45/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.99×** | +8.1 | 4e-14 | 42/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.99×** | +8.1 | 4e-14 | 41/48 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.98×** | +8.1 | 4e-14 | 42/48 (HOP62, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +8.1 | 4e-14 | 37/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.83×** | +7.1 | 5e-11 | 39/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.88×** | +6.9 | 3e-10 | 29/42 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.6 | 9e-07 | 31/48 (J82, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.59×** | +5.5 | 2e-06 | 32/48 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +5.3 | 6e-06 | 34/48 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.54×** | +4.9 | 4e-05 | 27/47 (A-172, RPMI-7951, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.003 | 25/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.017 | 20/48 (RKO, HT-29, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.037 | 21/47 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +2.9 | 0.060 | 10/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11414.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.349×; ⚠ cell-cycle shift, explains ~66% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.200×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.759× | -3.0 | 0.73 | 19/48 (NCI-H23, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.778× | -3.0 | 0.73 | 15/48 (NCI-H460, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 50.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.63× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 20.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.56× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 19.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.71× (z +9.3) | — |
| [[SW480 (line)]] | alt | 39.1 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.96× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 22.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.23× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 32.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.78× (z +10.8) | — |
| [[LoVo (line)]] | wt | 32.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.73× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.64× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.3) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H23 (line)]] | alt | 55.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.09× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 41.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.75× (z +8.7) | — |
| [[A549 (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[C32 (line)]] | wt | 21.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.60× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.1) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 26.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.200× (z -8.8) |
| [[Hs 766T (line)]] | wt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.98× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[HT-29 (line)]] | alt | 28.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.69× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.9) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[SW48 (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -9.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD12]] | +0.72 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[CCT6A]] | +0.68 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[NUDC]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CCT2]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[TRMT6]] | +0.65 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[LSG1]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | STRING 529 |
| [[VCP]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CCT5]] | +0.63 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SETX]] | +0.61 | +0.66 / +0.54 | both halves | 1e-05 | same gene group |
| [[CCT4]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | -0.67 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[AKAP1-DT]] | -0.61 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[RCOR3]] | -0.61 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.61 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ABCA5]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[LNX2]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[IST1]] | -0.58 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.58 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[ELF2]] | -0.57 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.57 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[CERT1]] | -0.57 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[PHPT1]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.5, -31.5); signed map (-11.9, -45.8). **Vector** length 76.7, 19.6% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +8.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.4 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[Thymol (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +1.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.4 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -2.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | UTP11 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:38,009,258-38,024,820 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-94; previously UTP11L |
| Gene groups (HGNC) | SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3A2](https://www.uniprot.org/uniprotkb/Q9Y3A2) (Probable U3 small nucleolar RNA-associated protein 11):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Involved in nucleolar processing of pre-18S ribosomal RNA.

**Summary**, from NCBI Gene [51118](https://www.ncbi.nlm.nih.gov/gene/51118):

> Enables RNA binding activity. Involved in nervous system development; positive regulation of apoptotic process; and ribosomal small subunit biogenesis. Located in cytoplasm; nucleolus; and obsolete extracellular space. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24329) · Entrez [51118](https://www.ncbi.nlm.nih.gov/gene/51118) · UniProt [Q9Y3A2](https://www.uniprot.org/uniprotkb/Q9Y3A2) · Ensembl [ENSG00000183520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183520)

## Data

Gene col 11414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11414); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11414]; `tensor/DDL_lfc|DDL_z.npy` [11414]; `embed/gene_vectors.npy` [11414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11414 or target_col == 11414). Every well: [[UTP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
