---
symbol: "EID3"
type: "gene"
col: 14922
ensembl_id: "ENSG00000255150"
name: "EP300 interacting inhibitor of differentiation 3"
location: "12q23.3"
module: 117
arm: "+"
pooled_cpm: 6.09
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# EID3

*EP300 interacting inhibitor of differentiation 3* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.99× (z +10.0, q 1e-20, up in 25 of 31 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.69× (z +9.4, q 2e-18, up in 33 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.0442×, SHP-77 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.0505×, NCI-H2347 0.0748×; ⚠ toxic; cell-cycle shift, explains ~35% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.0617×, NCI-H23 0.138×; ⚠ cell-cycle shift, would explain all of this change); [[Entecavir (monohydrate) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0472×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 0.179×); [[Pimozide (drug)]] 0.05 µM in 1 line (A498 0.0894×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNRD1]] (+0.89, fdr 7e-06, ⚠ read-through risk), [[AKR1C1]] (+0.64, fdr 7e-06), [[GCLM]] (+0.64, fdr 7e-06), [[SLC7A11]] (+0.62, fdr 7e-06); moves opposite to [[RSPRY1]] (-0.48, fdr 3e-05), [[HNRNPLL]] (-0.48, fdr 5e-05), [[ICAM3]] (-0.47, fdr 3e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTSS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.99×** | +10.0 | 1e-20 | 25/31 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.69×** | +9.4 | 2e-18 | 33/44 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.37×** | +8.2 | 5e-14 | 32/43 (LS 180, LoVo, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.28×** | +7.2 | 8e-11 | 9/14 (NCI-H1573, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.1 | 1e-07 | 6/12 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +6.1 | 1e-07 | 19/42 (LoVo, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +6.0 | 2e-07 | 20/42 (LoVo, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +5.5 | 2e-06 | 20/38 (SK-MEL-2, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +4.8 | 1e-04 | 20/43 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.6 | 3e-04 | 9/34 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.5 | 3e-04 | 8/47 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 5e-04 | 13/43 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +4.4 | 5e-04 | 11/36 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.1 | 0.001 | 5/20 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +4.1 | 0.002 | 13/46 (AsPC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.002 | 9/45 (NCI-H460, HT-29, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.003 | 18/46 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.004 | 12/44 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.004 | 9/42 (BT-474, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.49×** | +3.8 | 0.004 | 10/42 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.005 | 10/38 (HT-29, LoVo, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.005 | 10/46 (HT-29, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14922.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.0442×, SHP-77 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.0505×, NCI-H2347 0.0748×; ⚠ toxic; cell-cycle shift, explains ~35% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.0617×, NCI-H23 0.138×; ⚠ cell-cycle shift, would explain all of this change); [[Entecavir (monohydrate) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0472×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 0.179×); [[Pimozide (drug)]] 0.05 µM in 1 line (A498 0.0894×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.766× | -3.6 | 0.19 | 19/39 (NCI-H23, AsPC-1, …) | top dose only | position effect removed |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.706× | -3.3 | 0.26 | 5/44 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |
| [[AT7519 (drug)]] 0.05 µM |  | 0.700× | -3.2 | 0.26 | 9/44 (H4, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 26.5 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.42× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0442× (z -23.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.179× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 5.01 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0894× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0472× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 5.10 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0617× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0505× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 5.37 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0748× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNRD1]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | STRING 689; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of TXNRD1 on the same strand (can correlate by spillover, not regulation) |
| [[AKR1C1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[GCLM]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SLC7A11]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CYP4F11]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[NMRAL2P-1]] | +0.54 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PIR]] | +0.54 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MYO5B]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PTGR1]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SEL1L3]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[NMRAL2P]] | +0.52 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[GSR]] | +0.51 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[LINC01564]] | +0.51 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSPRY1]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[HNRNPLL]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ICAM3]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ZNF451]] | -0.47 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[NPHP3]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ARHGAP1]] | -0.46 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[INTS6L]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[GCAT]] | -0.45 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MTR]] | -0.45 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[MTSS1]] | -0.44 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PIK3R1]] | -0.44 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[CRLS1]] | -0.44 | -0.32 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTSS1]] | B | MTSS1 activity lowers EID3's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.53× higher at baseline in the lines without MTSS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[BEND6]] | B | BEND6 activity lowers EID3's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 1.37× higher at baseline in the lines without BEND6 | 0.098 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.8, 48.0); signed map (51.7, -10.3). **Vector** length 73.9, 12.7% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.54 to 8); *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.54 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.7 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.7 | +10.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.5 | -0.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | EP300 interacting inhibitor of differentiation 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:104,303,739-104,305,205 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25832, NSMCE4B, NSE4B |
| Reactome | 3 pathways, smallest: SUMOylation of DNA damage response and repair proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N140](https://www.uniprot.org/uniprotkb/Q8N140) (EP300-interacting inhibitor of differentiation 3):

> Tissue-specific component of the SMC5-SMC6 complex, a complex involved in repair of DNA double-strand breaks by homologous recombination. The complex may promote sister chromatid homologous recombination by recruiting the SMC1-SMC3 cohesin complex to double-strand breaks. The complex is required for telomere maintenance via recombination and mediates sumoylation of shelterin complex (telosome) components.; Acts as a repressor of nuclear receptor-dependent transcription possibly by interfering …

**Summary**, from NCBI Gene [493861](https://www.ncbi.nlm.nih.gov/gene/493861):

> Predicted to be involved in DNA repair. Located in nucleolus and nucleoplasm. Part of Smc5-Smc6 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32961) · Entrez [493861](https://www.ncbi.nlm.nih.gov/gene/493861) · UniProt [Q8N140](https://www.uniprot.org/uniprotkb/Q8N140) · Ensembl [ENSG00000255150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255150)

## Data

Gene col 14922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14922); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14922]; `tensor/DDL_lfc|DDL_z.npy` [14922]; `embed/gene_vectors.npy` [14922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14922 or target_col == 14922). Every well: [[EID3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EID3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
