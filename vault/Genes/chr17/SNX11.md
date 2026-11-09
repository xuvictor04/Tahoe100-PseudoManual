---
symbol: "SNX11"
type: "gene"
col: 26
ensembl_id: "ENSG00000002919"
name: "sorting nexin 11"
location: "17q21.32"
module: 17
arm: "+"
pooled_cpm: 10.15
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SNX11

*sorting nexin 11* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.27× (z +11.7, q 8e-29, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.585× (z -7.4, q 9e-11, down in 14 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.728× (z -4.6, q 1e-03, down in 18 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2347 0.133×, NCI-H460 0.191×, SW1417 0.124×, SW480 0.226×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.243×, NCI-H2347 0.220×, SK-MEL-2 0.239×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (HS-578T 0.167×); [[Vilanterol (drug)]] 0.5 µM in 1 line (Hs 766T 0.126×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.137×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD6]] (+0.64, fdr 1e-05), [[MED20]] (+0.60, fdr 1e-05), [[POMGNT2]] (+0.59, fdr 3e-05); moves opposite to [[PTPRK]] (-0.52, fdr 2e-04), [[DGKH]] (-0.50, fdr 3e-04), [[LINC02977]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 26.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +11.7 | 8e-29 | 42/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +10.8 | 1e-24 | 42/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +10.2 | 6e-22 | 39/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.30×** | +8.9 | 9e-17 | 36/46 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +8.6 | 1e-15 | 28/45 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.5 | 3e-06 | 21/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.9 | 9e-05 | 16/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 9e-05 | 18/45 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +4.8 | 1e-04 | 17/43 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.0 | 0.004 | 12/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.007 | 12/46 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.009 | 9/45 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.28×** | +3.4 | 0.030 | 12/40 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.030 | 10/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.030 | 7/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.076 | 6/47 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.099 | 9/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 26.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2347 0.133×, NCI-H460 0.191×, SW1417 0.124×, SW480 0.226×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.243×, NCI-H2347 0.220×, SK-MEL-2 0.239×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (HS-578T 0.167×); [[Vilanterol (drug)]] 0.5 µM in 1 line (Hs 766T 0.126×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.137×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -7.4 | 9e-11 | 14/19 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.679×** | -5.6 | 8e-06 | 22/35 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -4.6 | 1e-03 | 18/46 (BT-474, SW1417, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.860× | -3.1 | 0.29 | 8/48 (NCI-H2347, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 26. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.01 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 7.39 | 0 | 2 | — | [[Vilanterol (drug)]] 0.5 µM 0.126× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 9.79 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -11.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 12.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.167× (z -9.3) |
| [[HT-29 (line)]] | alt | 8.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.95 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 26), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD6]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MED20]] | +0.60 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[POMGNT2]] | +0.59 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[TSFM]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[HARS2]] | +0.58 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ESS2]] | +0.57 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[UNC119]] | +0.57 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[CNEP1R1]] | +0.56 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[NOMO3]] | +0.56 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[ALG9]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CGRRF1]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[VPS33B]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | -0.52 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[DGKH]] | -0.50 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[LINC02977]] | -0.50 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[SNX5]] | -0.50 | -0.46 / -0.15 | ⚠ not reproduced | 0.001 | same gene group; STRING 459 |
| [[CCDC90B-AS1]] | -0.50 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[GTF2H1]] | -0.50 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.50 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[TBCE-1]] | -0.49 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[BAALC-AS1]] | -0.49 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[ANGPT2]] | -0.49 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[EFCAB2]] | -0.49 | -0.40 / -0.23 | both halves | 5e-04 |  |
| [[GNG12-AS1]] | -0.49 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[MMADHC-DT]] | -0.49 | -0.29 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.485). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.7, -0.7); signed map (-23.9, -17.5). **Vector** length 51.8, 6.43% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.0 | +10.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.0 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.9 | +10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.8 | +11.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.5 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | +0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,103,357-48,123,601 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5W9](https://www.uniprot.org/uniprotkb/Q9Y5W9) (Sorting nexin-11):

> Phosphoinositide-binding protein involved in protein sorting and membrane trafficking in endosomes. Regulates the levels of TRPV3 by promoting its trafficking from the cell membrane to lysosome for degradation.

**Summary**, from NCBI Gene [29916](https://www.ncbi.nlm.nih.gov/gene/29916):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein does not contain a coiled coil region, like some family members. This gene encodes a protein of unknown function. This gene results in two transcript variants differing in the 5' UTR, but encoding the same protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14975) · Entrez [29916](https://www.ncbi.nlm.nih.gov/gene/29916) · UniProt [Q9Y5W9](https://www.uniprot.org/uniprotkb/Q9Y5W9) · Ensembl [ENSG00000002919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000002919)

## Data

Gene col 26: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 26); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 26, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 26]; `tensor/DDL_lfc|DDL_z.npy` [26]; `embed/gene_vectors.npy` [26]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 26 or target_col == 26). Every well: [[SNX11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
