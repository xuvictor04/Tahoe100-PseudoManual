---
symbol: "B4GALT3"
type: "gene"
col: 8197
ensembl_id: "ENSG00000158850"
name: "beta-1,4-galactosyltransferase 3"
location: "1q23.3"
module: 2
arm: "+"
pooled_cpm: 11.88
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# B4GALT3

*beta-1,4-galactosyltransferase 3* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.71× (z +7.3, q 2e-10, up in 27 of 42 measured lines) ⚠ transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.62× (z +6.6, q 1e-08, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.514× (z -4.6, q 0.003, down in 19 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRABD]] (+0.64, fdr 1e-05), [[CDC34]] (+0.63, fdr 1e-05), [[FCHSD1]] (+0.63, fdr 1e-05); moves opposite to [[MCTS1]] (-0.55, fdr 5e-05), [[PSME3IP1]] (-0.55, fdr 4e-05), [[LINC01138]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +7.3 | 2e-10 | 27/42 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +6.6 | 1e-08 | 30/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.4 | 2e-08 | 28/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +5.8 | 1e-06 | 27/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +4.6 | 4e-04 | 18/47 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.96×** | +4.5 | 5e-04 | 16/45 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 5e-04 | 18/47 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.1 | 0.003 | 19/47 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +4.0 | 0.004 | 15/47 (NCI-H1573, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.004 | 18/46 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.8 | 0.006 | 15/41 (A549, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.8 | 0.008 | 6/30 (NCI-H23, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.7 | 0.008 | 9/34 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.010 | 13/45 (MIA PaCa-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.014 | 4/46 (NCI-H460, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pimitespib (drug)]] 5 µM |  | **1.65×** | +3.4 | 0.025 | 5/37 (C32, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Everolimus (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.056 | 8/46 (NCI-H2347, H4, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.056 | 10/43 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.057 | 6/45 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.057 | 5/45 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.057 | 9/47 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[LJI308 (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.074 | 7/46 (HS-578T, SHP-77, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.514×** | -4.6 | 0.003 | 19/46 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.731×** | -4.1 | 0.014 | 13/45 (HOP62, A-427, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.048 | 19/44 (C-33 A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.776×** | -3.4 | 0.072 | 17/45 (C32, BT-474, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.610×** | -3.4 | 0.072 | 8/43 (RPMI-7951, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.786×** | -3.4 | 0.072 | 13/46 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.087 | 11/47 (NCI-H2347, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.858× | -3.0 | 0.16 | 11/48 (J82, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRABD]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CDC34]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[NFRKB]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TRMT2A]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TMEM259]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[RCE1]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[DOK4]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SDHAP1-1]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ARFGAP1]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[SNN]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.59 | +0.49 / +0.46 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation; STRING 487 |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.55 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[PSME3IP1]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[LINC01138]] | -0.54 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[LEKR1]] | -0.54 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.54 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[SPDL1]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TASOR]] | -0.53 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[COQ5]] | -0.53 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[CTBP1-DT]] | -0.53 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[ARHGEF37]] | -0.52 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[NUCKS1]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[YWHAE]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (4.6, -4.8); signed map (-29.3, 0.4). **Vector** length 64.7, 10.8% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.5 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.3 | +4.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +4.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-galactosyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,171,310-161,177,968 (-) |
| Ensembl biotype | protein_coding |
| Also known as | beta4Gal-T3 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Reactome | 8 pathways, smallest: N-Glycan antennae elongation; Keratan sulfate biosynthesis; N-glycan antennae elongation in the medial/trans-Golgi |
| Matched by | ensembl_id |

**Function**, from UniProt [O60512](https://www.uniprot.org/uniprotkb/O60512) (Beta-1,4-galactosyltransferase 3):

> Responsible for the synthesis of complex-type N-linked oligosaccharides in many glycoproteins as well as the carbohydrate moieties of glycolipids.

**Summary**, from NCBI Gene [8703](https://www.ncbi.nlm.nih.gov/gene/8703):

> This gene is one of seven beta-1,4-galactosyltransferase (beta4GalT) genes. They encode type II membrane-bound glycoproteins that appear to have exclusive specificity for the donor substrate UDP-galactose; all transfer galactose in a beta1,4 linkage to similar acceptor sugars: GlcNAc, Glc, and Xyl. Each beta4GalT has a distinct function in the biosynthesis of different glycoconjugates and saccharide structures. As type II membrane proteins, they have an N-terminal hydrophobic signal sequence …

**Accessions** — [HGNC:926](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:926) · Entrez [8703](https://www.ncbi.nlm.nih.gov/gene/8703) · UniProt [O60512](https://www.uniprot.org/uniprotkb/O60512) · Ensembl [ENSG00000158850](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158850)

## Data

Gene col 8197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8197); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8197]; `tensor/DDL_lfc|DDL_z.npy` [8197]; `embed/gene_vectors.npy` [8197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8197 or target_col == 8197). Every well: [[B4GALT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
