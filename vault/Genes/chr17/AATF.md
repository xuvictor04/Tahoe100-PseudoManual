---
symbol: "AATF"
type: "gene"
col: 15856
ensembl_id: "ENSG00000275700"
name: "apoptosis antagonizing transcription factor"
location: "17q12"
module: 4
arm: "+"
pooled_cpm: 156.24
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# AATF

*apoptosis antagonizing transcription factor* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.53× (z +11.7, q 4e-29, up in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.91× (z +9.3, q 3e-18, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.848× (z -6.5, q 5e-08, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (SW48 0.420×, A-427 0.596×, LOX-IMVI 0.592×, RKO 0.591×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.262×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.460×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1A]] (+0.68, fdr 7e-06), [[EFTUD2]] (+0.66, fdr 7e-06), [[MYBBP1A]] (+0.64, fdr 7e-06); moves opposite to [[MBIP]] (-0.57, fdr 1e-05), [[KBTBD3]] (-0.56, fdr 1e-05), [[PNRC1]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +11.7 | 4e-29 | 45/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +9.3 | 3e-18 | 36/49 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.34×** | +8.0 | 2e-13 | 37/48 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +7.5 | 6e-12 | 28/48 (NCI-H1792, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +7.5 | 6e-12 | 39/48 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +7.4 | 1e-11 | 37/48 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +7.3 | 2e-11 | 31/48 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +5.9 | 2e-07 | 0/50 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.25×** | +5.9 | 3e-07 | 32/48 (HT-29, A549, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +5.8 | 5e-07 | 28/48 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.22×** | +5.5 | 2e-06 | 27/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +5.4 | 4e-06 | 24/48 (AsPC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.13× | +4.6 | 2e-04 | 14/49 (Hs 766T, HOP62, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +4.3 | 8e-04 | 14/48 (KATO III, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.2 | 1e-03 | 18/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +4.2 | 1e-03 | 29/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.001 | 24/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.004 | 22/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.017 | 17/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.017 | 17/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.056 | 8/48 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimozide (drug)]] 5 µM |  | 1.12× | +3.0 | 0.063 | 2/48 (AN3 CA, NCI-H1792) | top dose only | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.075 | 10/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15856.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (SW48 0.420×, A-427 0.596×, LOX-IMVI 0.592×, RKO 0.591×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.262×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.460×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -6.5 | 5e-08 | 21/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.838× | -4.9 | 3e-04 | 21/49 (CHP-212, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.809×** | -4.2 | 0.005 | 27/47 (A498, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.878× | -3.6 | 0.045 | 10/49 (SW1417, HS-578T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.841× | -3.4 | 0.072 | 17/48 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.889× | -3.3 | 0.10 | 13/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.891× | -3.2 | 0.10 | 6/48 (SNU-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 5 µM |  | 0.888× | -3.2 | 0.10 | 8/48 (A-172, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 161 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 179 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.82× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 138 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.92× (z +11.8) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 2.48× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 80.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.6) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 187 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.81× (z +9.1) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 2.97× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 198 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +9.8) | [[Lonafarnib (drug)]] 5 µM 0.262× (z -10.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 198 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.460× (z -8.5) |
| [[A-427 (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 209 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.85× (z +8.6) ⚠ unreliable plate only | — |
| [[J82 (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.77× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 194 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 122 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 2.90× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 273 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.645× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 99.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.93× (z +9.4) | — |
| [[RKO (line)]] | wt | 191 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 199 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.82× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.354× (z -8.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.658× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 229 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.76× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 204 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 182 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 203 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 125 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 92.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 201 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 155 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1A]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 | STRING 609 |
| [[EFTUD2]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 | STRING 509 |
| [[TOMM40]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[WDR4]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[DHX37]] | +0.63 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[MTAP]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[UTP4]] | +0.62 | +0.57 / +0.67 | both halves | 1e-05 | STRING 997 |
| [[PUM3]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 | STRING 912 |
| [[EIF2S1]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NOM1]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 | STRING 626 |
| [[ABCF2]] | +0.61 | +0.54 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBIP]] | -0.57 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.56 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[PNRC1]] | -0.55 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[ATP23]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[VAMP2]] | -0.54 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[AFTPH]] | -0.53 | -0.37 / -0.65 | both halves | 8e-05 | same gene group |
| [[CLK1]] | -0.52 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[RSRP1]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PIK3CA]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[LCA5]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[KMT2E]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[KRT10]] ⚠ | -0.51 | -0.43 / -0.55 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HOTAIRM1]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.9, -35.1); signed map (-4.7, -47.2). **Vector** length 109, 28.8% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.6 | +11.7 |
|  | [[EX229 (drug)]] 5 µM |  | +5.7 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.2 | +7.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.6 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -6.1 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | apoptosis antagonizing transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,948,925-37,056,871 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DED, CHE-1, CHE1, BFR2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: NRAGE signals death through JNK; Cell death signalling via NRAGE, NRIF and NADE; p75 NTR receptor-mediated signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY61](https://www.uniprot.org/uniprotkb/Q9NY61) (Protein AATF):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. May function as a general inhibitor of the histone deacetylase …

**Summary**, from NCBI Gene [26574](https://www.ncbi.nlm.nih.gov/gene/26574):

> The protein encoded by this gene was identified on the basis of its interaction with MAP3K12/DLK, a protein kinase known to be involved in the induction of cell apoptosis. This gene product contains a leucine zipper, which is a characteristic motif of transcription factors, and was shown to exhibit strong transactivation activity when fused to Gal4 DNA binding domain. Overexpression of this gene interfered with MAP3K12 induced apoptosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19235) · Entrez [26574](https://www.ncbi.nlm.nih.gov/gene/26574) · UniProt [Q9NY61](https://www.uniprot.org/uniprotkb/Q9NY61) · Ensembl [ENSG00000275700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275700)

## Data

Gene col 15856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15856); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15856]; `tensor/DDL_lfc|DDL_z.npy` [15856]; `embed/gene_vectors.npy` [15856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15856 or target_col == 15856). Every well: [[AATF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AATF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
