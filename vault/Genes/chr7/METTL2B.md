---
symbol: "METTL2B"
type: "gene"
col: 9058
ensembl_id: "ENSG00000165055"
name: "methyltransferase 2B, tRNA N3-cytidine"
location: "7q32.1"
module: 5
arm: "+"
pooled_cpm: 41.59
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# METTL2B

*methyltransferase 2B, tRNA N3-cytidine* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.76× (z +14.4, q 2e-44, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +14.2, q 2e-43, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.192×, A-427 0.284×, BT-474 0.311×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.293×, C-33 A 0.349×, HEC-1-A 0.445×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.207×, NCI-H23 0.426×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[GSK1059615 (drug)]] 0.5 µM in 1 line (AN3 CA 0.0524×); [[DT-061 (drug)]] 5 µM in 1 line (H4 0.0530×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP7BP-1]] (+0.74, fdr 7e-06), [[RRP7A]] (+0.70, fdr 7e-06), [[EIF3J]] (+0.70, fdr 7e-06); moves opposite to [[TXNDC16]] (-0.63, fdr 1e-04), [[TMEM59]] (-0.59, fdr 2e-05), [[CHASERR]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BMF]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.76×** | +14.4 | 2e-44 | 37/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +14.2 | 2e-43 | 38/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.71×** | +13.7 | 2e-40 | 37/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +13.3 | 2e-38 | 39/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +12.6 | 3e-34 | 38/48 (SHP-77, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +11.9 | 1e-30 | 40/46 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +10.9 | 9e-26 | 37/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.53×** | +10.9 | 9e-26 | 34/48 (A498, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +10.4 | 2e-23 | 41/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +8.6 | 3e-16 | 32/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +8.2 | 1e-14 | 31/48 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +8.0 | 7e-14 | 30/48 (SW480, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +7.8 | 3e-13 | 31/48 (BT-474, SW480, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.36×** | +7.6 | 1e-12 | 28/48 (SW 900, H4, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +7.6 | 2e-12 | 28/48 (SW 900, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +6.2 | 2e-08 | 21/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.8 | 3e-07 | 22/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +5.8 | 3e-07 | 25/48 (PANC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +4.8 | 4e-05 | 16/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +4.7 | 7e-05 | 13/48 (PANC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.8 | 0.003 | 11/48 (NCI-H2030, A549, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.005 | 10/48 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.008 | 9/48 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9058.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.192×, A-427 0.284×, BT-474 0.311×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.293×, C-33 A 0.349×, HEC-1-A 0.445×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.207×, NCI-H23 0.426×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[GSK1059615 (drug)]] 0.5 µM in 1 line (AN3 CA 0.0524×); [[DT-061 (drug)]] 5 µM in 1 line (H4 0.0530×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.852× | -5.9 | 2e-06 | 18/48 (LoVo, HCT15, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.895× | -4.1 | 0.012 | 18/48 (RKO, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.877× | -3.1 | 0.24 | 10/47 (C32, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.883× | -3.1 | 0.24 | 19/41 (SHP-77, A-427, …) | top dose only | composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.847× | -3.1 | 0.24 | 3/48 (RKO, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 51.1 | 0 | 3 (3 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0860× (z -13.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 40.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +8.6) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.311× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 49.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.418× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 45.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.02× (z +8.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 50.4 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0524× (z -11.0) |
| [[C32 (line)]] | wt | 79.5 | 0 | 1 (1 ⚠) | — | [[NG25 (drug)]] 5 µM 0.141× (z -8.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[H4 (line)]] | wt | 29.4 | 0 | 1 | — | [[DT-061 (drug)]] 5 µM 0.0530× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 45.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 79.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 74.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 45.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.2) | — |
| [[A-172 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP-1]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[RRP7A]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[EIF3J]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[METTL2A]] | +0.69 | +0.68 / +0.74 | both halves | 7e-06 | same gene group |
| [[PUS1]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PIGL]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.63 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[GTPBP4]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ZNG1F]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CRK]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DAP3]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TANGO6]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.63 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[TMEM59]] | -0.59 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[CHASERR]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[H3-3A]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[LMBRD1]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.57 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[BMF]] | -0.57 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[PRCP]] | -0.56 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[CAT]] | -0.56 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[ATF2]] | -0.55 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[HCN3]] | -0.55 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[FOXO4]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMF]] | C | BMF activity lowers METTL2B's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.40× higher at baseline in the lines without BMF | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.4, -30.3); signed map (3.2, -46.0). **Vector** length 85.6, 18.0% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +12.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +10.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +11.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.0 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +6.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -5.5 | -5.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.3 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.8 | -1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 2B, tRNA N3-cytidine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,476,729-128,506,602 (+) |
| Ensembl biotype | protein_coding |
| Also known as | METL, FLJ11350; previously METTL2 |
| Gene groups (HGNC) | 7BS N3-cytosine RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1Q9](https://www.uniprot.org/uniprotkb/Q6P1Q9) (tRNA N(3)-cytidine methyltransferase METTL2B):

> S-adenosyl-L-methionine-dependent methyltransferase that mediates N(3)-methylcytidine modification of residue 32 of the tRNA anticodon loop of tRNA(Thr)(UGU) and tRNA(Arg)(CCU).

**Summary**, from NCBI Gene [55798](https://www.ncbi.nlm.nih.gov/gene/55798):

> This gene is a member of a family of methyltransferases that share homology with, but are distinct from, the UbiE family of methyltransferases. Alternatively spliced variants which encode different protein isoforms have been described; however, not all variants have been fully characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18272) · Entrez [55798](https://www.ncbi.nlm.nih.gov/gene/55798) · UniProt [Q6P1Q9](https://www.uniprot.org/uniprotkb/Q6P1Q9) · Ensembl [ENSG00000165055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165055)

## Data

Gene col 9058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9058); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9058]; `tensor/DDL_lfc|DDL_z.npy` [9058]; `embed/gene_vectors.npy` [9058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9058 or target_col == 9058). Every well: [[METTL2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
