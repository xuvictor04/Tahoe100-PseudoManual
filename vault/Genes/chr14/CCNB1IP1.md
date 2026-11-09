---
symbol: "CCNB1IP1"
type: "gene"
col: 2027
ensembl_id: "ENSG00000100814"
name: "cyclin B1 interacting protein 1"
location: "14q11.2"
module: 40
arm: "+"
pooled_cpm: 35.46
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 2
n_dd_up_clean: 28
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CCNB1IP1

*cyclin B1 interacting protein 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.43× (z +13.6, q 2e-39, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.754× (z -4.2, q 0.016, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.555×, AN3 CA 0.299×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.254×, HEC-1-A 0.335×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.221×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0976×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF3M]] (+0.69, fdr 1e-05), [[ST6GALNAC6]] (+0.68, fdr 1e-05), [[RPIA]] (+0.66, fdr 1e-05); moves opposite to [[TIA1]] (-0.61, fdr 2e-05), [[FAM111A]] (-0.61, fdr 3e-05), [[CGGBP1]] (-0.60, fdr 8e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +13.6 | 2e-39 | 47/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +12.0 | 6e-31 | 44/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +11.1 | 3e-26 | 45/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +8.7 | 4e-16 | 44/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +8.1 | 7e-14 | 38/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +7.9 | 4e-13 | 42/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.62×** | +7.4 | 1e-11 | 29/45 (NCI-H460, LoVo, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.0 | 1e-10 | 35/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.39×** | +7.0 | 2e-10 | 35/43 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +6.9 | 2e-10 | 32/48 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +6.8 | 5e-10 | 35/48 (NCI-H460, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +6.5 | 5e-09 | 34/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +6.3 | 1e-08 | 33/46 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +5.7 | 5e-07 | 32/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.46×** | +5.4 | 3e-06 | 30/44 (NCI-H460, HT-29, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.93×** | +5.3 | 5e-06 | 31/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +4.9 | 3e-05 | 27/48 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.78×** | +4.6 | 1e-04 | 27/48 (HEC-1-A, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +4.4 | 3e-04 | 23/48 (SK-MEL-2, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.69×** | +4.2 | 8e-04 | 18/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.004 | 19/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.555×, AN3 CA 0.299×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.254×, HEC-1-A 0.335×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.221×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0976×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.754×** | -4.2 | 0.016 | 19/47 (SW480, LoVo, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.785×** | -3.6 | 0.097 | 15/48 (NCI-H2347, SW 1271, …) | top dose only | plate-row cell shift |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.799× | -3.3 | 0.21 | 13/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.815× | -3.2 | 0.22 | 19/48 (Hs 766T, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 33.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.73× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 27.2 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.55× (z +9.9) | — |
| [[LoVo (line)]] | wt | 50.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[AN3 CA (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[HEC-1-A (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H1792 (line)]] | alt | 32.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.82× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 33.5 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.96× (z +8.8) | — |
| [[NCI-H661 (line)]] | alt | 55.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0976× (z -8.5) |
| [[SW480 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3M]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.68 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RPIA]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[CTU1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CSNK2A1]] | +0.63 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[DUXAP10]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TBCB]] | +0.62 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[WDR59]] | +0.61 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[RPS24]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SLC15A4]] | +0.61 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[EIF3L]] | +0.61 | +0.68 / +0.37 | both halves | 7e-05 |  |
| [[SHQ1]] | +0.61 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.61 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[FAM111A]] | -0.61 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CGGBP1]] | -0.60 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[HMGN2]] | -0.59 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.58 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[RO60]] | -0.57 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ATXN7]] | -0.56 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[AKT1S1]] | -0.55 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[SCRN1]] | -0.55 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PNRC2]] | -0.54 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[DDX6]] | -0.54 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[LRRC57]] | -0.54 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.463). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-8.5, -15.5); signed map (-54.7, -4.9). **Vector** length 92.0, 22.7% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +6.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +3.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | +1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin B1 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,311,368-20,333,312 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HEI10; previously C14orf18 |
| Gene groups (HGNC) | Ring finger proteins; Small nucleolar RNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPC3](https://www.uniprot.org/uniprotkb/Q9NPC3) (E3 ubiquitin-protein ligase CCNB1IP1):

> Ubiquitin E3 ligase that acts as a limiting factor for crossing-over during meiosis: required during zygonema to limit the colocalization of RNF212 with MutS-gamma-associated recombination sites and thereby establish early differentiation of crossover and non-crossover sites. Later, it is directed by MutL-gamma to stably accumulate at designated crossover sites. Probably promotes the dissociation of RNF212 and MutS-gamma to allow the progression of recombination and the implementation of the …

**Summary**, from NCBI Gene [57820](https://www.ncbi.nlm.nih.gov/gene/57820):

> HEI10 is a member of the E3 ubiquitin ligase family and functions in progression of the cell cycle through G(2)/M.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:19437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19437) · Entrez [57820](https://www.ncbi.nlm.nih.gov/gene/57820) · UniProt [Q9NPC3](https://www.uniprot.org/uniprotkb/Q9NPC3) · Ensembl [ENSG00000100814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100814)

## Data

Gene col 2027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2027); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2027]; `tensor/DDL_lfc|DDL_z.npy` [2027]; `embed/gene_vectors.npy` [2027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2027 or target_col == 2027). Every well: [[CCNB1IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNB1IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
