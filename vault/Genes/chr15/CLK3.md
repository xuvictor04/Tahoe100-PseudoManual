---
symbol: "CLK3"
type: "gene"
col: 11021
ensembl_id: "ENSG00000179335"
name: "CDC like kinase 3"
location: "15q24.1"
module: 180
arm: "+"
pooled_cpm: 42.94
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# CLK3

*CDC like kinase 3* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.08× (z +9.2, q 2e-17, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.567× (z -8.5, q 8e-15, down in 30 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.787× (z -3.7, q 0.027, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.138×, KATO III 0.277×, RPMI-7951 0.254×, CFPAC-1 0.316×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LOX-IMVI 0.243×, A-172 0.278×, NCI-H2347 0.350×, Panc 03.27 0.249×, …; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0426×; ⚠ cell-cycle shift, explains ~22% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (SW 1271 0.0710×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 1271 0.0986×); [[OTS514 (drug)]] 5 µM in 1 line (HCT15 0.0976×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG1]] (+0.65, fdr 7e-06), [[ENO2]] (+0.64, fdr 7e-06), [[UBE2O]] (+0.63, fdr 1e-05); moves opposite to [[POGLUT1]] (-0.61, fdr 7e-06), [[ANAPC7]] (-0.58, fdr 1e-05), [[CTPS1]] (-0.58, fdr 1e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.08×** | +9.2 | 2e-17 | 44/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +6.8 | 3e-09 | 30/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +6.4 | 3e-08 | 36/48 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.2 | 8e-08 | 36/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +5.5 | 4e-06 | 29/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 1e-05 | 34/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.3 | 0.002 | 21/36 (NCI-H1573, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.1 | 0.003 | 22/43 (J82, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.016 | 21/48 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.029 | 16/49 (PANC-1, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.068 | 15/48 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.15× | +3.1 | 0.092 | 14/48 (KATO III, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.21× | +3.0 | 0.11 | 16/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11021.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.138×, KATO III 0.277×, RPMI-7951 0.254×, CFPAC-1 0.316×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LOX-IMVI 0.243×, A-172 0.278×, NCI-H2347 0.350×, Panc 03.27 0.249×, …; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0426×; ⚠ cell-cycle shift, explains ~22% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (SW 1271 0.0710×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 1271 0.0986×); [[OTS514 (drug)]] 5 µM in 1 line (HCT15 0.0976×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -8.5 | 8e-15 | 30/38 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.593×** | -8.2 | 9e-14 | 36/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.776×** | -3.8 | 0.027 | 24/47 (H4, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.787×** | -3.7 | 0.027 | 21/48 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.795×** | -3.6 | 0.039 | 21/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.812× | -3.2 | 0.10 | 18/48 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.814× | -3.2 | 0.10 | 18/48 (SHP-77, NCI-H2347, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.815× | -3.2 | 0.10 | 16/49 (hTERT-HPNE, SW480, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 0.813× | -3.1 | 0.12 | 20/47 (HEC-1-A, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 51.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0426× (z -14.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 2 (2 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.111× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 49.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 40.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -15.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 33.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 58.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 57.5 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0710× (z -10.0) |
| [[A-172 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 41.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.10× (z +10.6) | — |
| [[C32 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -9.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 47.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -8.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 65.0 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0976× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[NCI-H23 (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +8.5) | — |
| [[A-427 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ENO2]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LRP1]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[EIF1AD]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[JMJD6]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ALKBH5]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[DEDD2]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[XAB2]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT1]] | -0.61 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.57 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[DMAC2L]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[OXCT1]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ADGRA3]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ABCE1]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[NHLRC2]] | -0.52 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[RNASEH2B]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GCFC2]] | -0.52 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CLN6]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity raises CLK3's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.27× lower at baseline in the lines without NDRG1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[PRAF2]] | C | PRAF2 activity raises CLK3's level | lines that do not express PRAF2 (4) vs lines expressing it (46) | 1.39× lower at baseline in the lines without PRAF2 | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286511, LINC02343, CCDC110; maybe low, not absent |
| [[SH3D21]] | C | SH3D21 activity raises CLK3's level | lines that do not express SH3D21 (4) vs lines expressing it (46) | 1.31× lower at baseline in the lines without SH3D21 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286677; maybe low, not absent; its own permutation p |
| [[DDIT4]] | C | DDIT4 activity raises CLK3's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 1.37× lower at baseline in the lines without DDIT4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |
| [[SLC2A1]] | C | SLC2A1 activity raises CLK3's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 1.23× lower at baseline in the lines without SLC2A1 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.7, -14.6); signed map (-35.4, 26.1). **Vector** length 97.4, 24.0% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.9 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.9 | +6.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -3.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.4 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -3.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | CDC like kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,598,500-74,645,414 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CDC like kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P49761](https://www.uniprot.org/uniprotkb/P49761) (Dual specificity protein kinase CLK3):

> Dual specificity kinase acting on both serine/threonine and tyrosine-containing substrates. Phosphorylates serine- and arginine-rich (SR) proteins of the spliceosomal complex. May be a constituent of a network of regulatory mechanisms that enable SR proteins to control RNA splicing and can cause redistribution of SR proteins from speckles to a diffuse nucleoplasmic distribution. Phosphorylates SRSF1 and SRSF3. Regulates the alternative splicing of tissue factor (F3) pre-mRNA in endothelial …

**Summary**, from NCBI Gene [1198](https://www.ncbi.nlm.nih.gov/gene/1198):

> This gene encodes a protein belonging to the serine/threonine type protein kinase family. This protein is a nuclear dual-specificity kinase that regulates the intranuclear distribution of the serine/arginine-rich (SR) family of splicing factors. Two transcript variants encoding different isoforms have been found for this gene. Related pseudogenes are located on chromosomes 1 and 9. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2071) · Entrez [1198](https://www.ncbi.nlm.nih.gov/gene/1198) · UniProt [P49761](https://www.uniprot.org/uniprotkb/P49761) · Ensembl [ENSG00000179335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179335)

## Data

Gene col 11021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11021); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11021]; `tensor/DDL_lfc|DDL_z.npy` [11021]; `embed/gene_vectors.npy` [11021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11021 or target_col == 11021). Every well: [[CLK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
