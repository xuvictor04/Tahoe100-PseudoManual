---
symbol: "ZSCAN21"
type: "gene"
col: 9326
ensembl_id: "ENSG00000166529"
name: "zinc finger and SCAN domain containing 21"
location: "7q22.1"
module: 28
arm: "+"
pooled_cpm: 8.49
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ZSCAN21

*zinc finger and SCAN domain containing 21* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.97× (z +14.9, q 0e+00, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.665× (z -6.1, q 5e-07, down in 20 of 38 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H2030 0.0722×, SHP-77 0.0926×, RPMI-7951 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.158×; ⚠ toxic; transcription drop); [[Econazole (drug)]] 0.5 µM in 1 line (AN3 CA 0.0568×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM128]] (+0.74, fdr 7e-06), [[RAD52]] (+0.69, fdr 7e-06), [[IFT46]] (+0.69, fdr 1e-05); moves opposite to [[KIAA1958]] (-0.57, fdr 8e-05), [[SLC25A5]] (-0.57, fdr 3e-05), [[RPS6KA5]] (-0.56, fdr 7e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +14.9 | 0e+00 | 33/44 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +12.7 | 2e-34 | 31/45 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +12.1 | 3e-31 | 32/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +12.0 | 4e-31 | 32/40 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +11.1 | 2e-26 | 23/33 (LoVo, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +11.0 | 3e-26 | 35/45 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +9.9 | 2e-21 | 32/47 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +9.2 | 3e-18 | 18/25 (J82, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +9.1 | 5e-18 | 32/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +9.0 | 1e-17 | 25/48 (A-172, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +8.2 | 2e-14 | 29/47 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +7.5 | 4e-12 | 23/47 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.3 | 9e-12 | 7/17 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +7.3 | 1e-11 | 22/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +6.7 | 8e-10 | 18/47 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +6.6 | 1e-09 | 20/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.0 | 2e-05 | 11/47 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.3 | 5e-04 | 10/42 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +4.0 | 0.002 | 13/42 (C32, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.009 | 10/47 (A-427, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9326.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H2030 0.0722×, SHP-77 0.0926×, RPMI-7951 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.158×; ⚠ toxic; transcription drop); [[Econazole (drug)]] 0.5 µM in 1 line (AN3 CA 0.0568×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -6.1 | 5e-07 | 20/38 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.795×** | -3.6 | 0.086 | 14/45 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.809× | -3.3 | 0.15 | 13/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.812× | -3.3 | 0.15 | 10/48 (SHP-77, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 0.816× | -3.2 | 0.16 | 1/48 (NCI-H1792) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.825× | -3.0 | 0.19 | 10/47 (LS 180, SNU-423, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.826× | -3.0 | 0.19 | 9/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | 0.813× | -3.0 | 0.19 | 14/46 (Panc 03.27, BT-474, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.36 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.19× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 8.11 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.0722× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 1 | — | [[Econazole (drug)]] 0.5 µM 0.0568× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 5.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.27× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 8.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.54× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 8.18 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.6× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 6.78 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.71× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 6.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 9.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0926× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.20× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM128]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[RAD52]] | +0.69 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[IFT46]] | +0.69 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[NDUFAF1]] | +0.68 | +0.82 / +0.46 | both halves | 3e-05 |  |
| [[PYM1]] | +0.67 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[COQ5]] | +0.67 | +0.77 / +0.47 | both halves | 2e-05 |  |
| [[ZNF621]] | +0.67 | +0.75 / +0.42 | both halves | 4e-05 | same gene group |
| [[TYW5]] | +0.66 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[KCTD18]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[ZNF197]] | +0.65 | +0.75 / +0.56 | both halves | 1e-05 | same gene group |
| [[ELAC1]] | +0.65 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[ZBED9]] | +0.65 | +0.76 / +0.45 | both halves | 3e-05 | same gene group; STRING 537 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | -0.57 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[SLC25A5]] | -0.57 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RPS6KA5]] | -0.56 | -0.59 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.1, 6.8); signed map (7.0, -23.2). **Vector** length 64.6, 9.56% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.6 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | +1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.9 | -6.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.9 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,049,774-100,065,040 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434L134, NY-REN-21, Zipro1; previously ZNF38 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5A6](https://www.uniprot.org/uniprotkb/Q9Y5A6) (Zinc finger and SCAN domain-containing protein 21):

> Strong transcriptional activator (By similarity). Plays an important role in spermatogenesis; essential for the progression of meiotic prophase I in spermatocytes (By similarity).

**Summary**, from NCBI Gene [7589](https://www.ncbi.nlm.nih.gov/gene/7589):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in positive regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13104) · Entrez [7589](https://www.ncbi.nlm.nih.gov/gene/7589) · UniProt [Q9Y5A6](https://www.uniprot.org/uniprotkb/Q9Y5A6) · Ensembl [ENSG00000166529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166529)

## Data

Gene col 9326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9326); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9326]; `tensor/DDL_lfc|DDL_z.npy` [9326]; `embed/gene_vectors.npy` [9326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9326 or target_col == 9326). Every well: [[ZSCAN21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
