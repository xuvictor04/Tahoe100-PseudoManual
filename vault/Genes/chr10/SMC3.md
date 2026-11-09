---
symbol: "SMC3"
type: "gene"
col: 2913
ensembl_id: "ENSG00000108055"
name: "structural maintenance of chromosomes 3"
location: "10q25.2"
module: 22
arm: "+"
pooled_cpm: 172.82
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SMC3

*structural maintenance of chromosomes 3* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +10.7, q 6e-24, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~77% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.31× (z +4.3, q 0.001, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (RKO 3.11×, PANC-1 2.48×, J82 2.58×, NCI-H2347 2.38×, …; ⚠ cell-cycle shift, explains ~77% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 2.75×, LOX-IMVI 2.53×; ⚠ cell-cycle shift, explains ~53% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 2.44×; ⚠ cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A549 2.38×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.733× (z -6.9, q 2e-09, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.222×, SNU-1 0.489×, HEC-1-A 0.640×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.229×; ⚠ cell-cycle shift, explains ~77% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (AsPC-1 0.317×; ⚠ cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.538×); [[Binimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.498×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPR]] (+0.71, fdr 7e-06), [[BAZ1B]] (+0.66, fdr 7e-06), [[RAD21]] (+0.64, fdr 1e-05); moves opposite to [[TMEM167A]] (-0.59, fdr 1e-05), [[TIMM10B]] (-0.55, fdr 2e-05), [[SURF4]] (-0.55, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRRCC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2913.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (RKO 3.11×, PANC-1 2.48×, J82 2.58×, NCI-H2347 2.38×, …; ⚠ cell-cycle shift, explains ~77% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 2.75×, LOX-IMVI 2.53×; ⚠ cell-cycle shift, explains ~53% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 2.44×; ⚠ cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A549 2.38×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.61×** | +10.7 | 6e-24 | 40/48 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.78×** | +9.1 | 2e-17 | 40/49 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.77×** | +8.7 | 4e-16 | 44/48 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.61×** | +7.6 | 5e-12 | 37/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +6.8 | 1e-09 | 40/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.56×** | +6.7 | 1e-09 | 42/47 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.50×** | +6.2 | 5e-08 | 28/44 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.35×** | +4.4 | 7e-04 | 29/45 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | **1.32×** | +4.4 | 8e-04 | 33/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 0.001 | 36/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +4.0 | 0.003 | 26/48 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **1.26×** | +3.7 | 0.009 | 26/48 (H4, PANC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | 1.15× | +3.2 | 0.060 | 7/48 (KATO III, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2913.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.222×, SNU-1 0.489×, HEC-1-A 0.640×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.229×; ⚠ cell-cycle shift, explains ~77% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (AsPC-1 0.317×; ⚠ cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.538×); [[Binimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.498×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -6.9 | 2e-09 | 33/49 (AsPC-1, SNU-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.6 | 0.10 | 0/50 | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.861× | -3.3 | 0.18 | 9/48 (HS-578T, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 489 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -25.4) |
| [[A549 (line)]] | wt | 174 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.4) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.38× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 131 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.5) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[SNU-423 (line)]] | alt | 245 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.1) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[HS-578T (line)]] | alt | 116 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.7) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[J82 (line)]] | alt | 157 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.6) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[PANC-1 (line)]] | alt | 217 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.8) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[RKO (line)]] | wt | 197 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +17.2) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[C-33 A (line)]] | alt | 264 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.1) ⚠ cell-cycle shift, explains ~77% of this change | [[Dinaciclib (drug)]] 5 µM 0.413× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[C32 (line)]] | wt | 89.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.4) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[HT-29 (line)]] | alt | 144 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.3) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H1792 (line)]] | alt | 92.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2030 (line)]] | alt | 151 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.1) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H2347 (line)]] | alt | 159 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.5) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[SW1417 (line)]] | alt | 196 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.1) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[A-172 (line)]] | wt | 189 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.1) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[AN3 CA (line)]] | alt | 350 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.6) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[HEC-1-A (line)]] | alt | 225 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -8.8) |
| [[LoVo (line)]] | wt | 122 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.63× (z +10.5) ⚠ toxic; cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H23 (line)]] | alt | 181 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.8) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H460 (line)]] | wt | 149 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.7) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[Panc 03.27 (line)]] | alt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 149 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.4) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[SNU-1 (line)]] | wt | 497 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.0) |
| [[A-427 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 158 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 165 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 163 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPR]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[BAZ1B]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[RAD21]] | +0.64 | +0.57 / +0.68 | both halves | 1e-05 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[RNF214]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[YEATS4]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CDC5L]] | +0.62 | +0.55 / +0.66 | both halves | 1e-05 | STRING 663 |
| [[LSM14A]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SETD2]] | +0.60 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[DEK]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 497 |
| [[KIF20B]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[PHF3]] | +0.58 | +0.47 / +0.65 | both halves | 2e-05 | STRING 423 |
| [[AGGF1]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM167A]] | -0.59 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[TIMM10B]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SURF4]] | -0.55 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[CHPF2]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TMED7-TICAM2]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.51 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[MLF2]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PDCD6]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[RALY-AS1]] | -0.49 | -0.18 / -0.42 | ⚠ not reproduced | 9e-04 |  |
| [[TMEM11-DT]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[CTTN]] | -0.49 | -0.51 / -0.46 | both halves | 2e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[TOR1B]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRCC1]] | C | LRRCC1 activity lowers SMC3's level | lines that do not express LRRCC1 (4) vs lines expressing it (46) | 1.88× higher at baseline in the lines without LRRCC1 | 0.048 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |
| [[LRRCC1]] | C | LRRCC1 activity strengthens SMC3's drug response | lines that do not express LRRCC1 (4) vs lines expressing it (45) | the lines without LRRCC1 respond 0.34× as strongly (z diff +2.46); strongest at Dinaciclib 5 µM: 0.79x vs 1.41x (z diff +5.7) | 0.081 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.1, 5.5); signed map (5.3, -14.3). **Vector** length 123, 44.0% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +6.7 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +6.3 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.0 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.4 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.4 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | structural maintenance of chromosomes 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:110,567,684-110,606,048 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCAP, BAM, SMC3L1, bamacan; previously CSPG6 |
| Gene groups (HGNC) | Proteoglycans; Structural maintenance of chromosomes proteins; Cohesin complex |
| Hallmark sets | MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 21 pathways, smallest: Cohesin Loading onto Chromatin; Establishment of Sister Chromatid Cohesion; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQE7](https://www.uniprot.org/uniprotkb/Q9UQE7) (Structural maintenance of chromosomes protein 3):

> Central component of cohesin, a complex required for chromosome cohesion during the cell cycle. The cohesin complex may form a large proteinaceous ring within which sister chromatids can be trapped. At anaphase, the complex is cleaved and dissociates from chromatin, allowing sister chromatids to segregate. Cohesion is coupled to DNA replication and is involved in DNA repair. The cohesin complex also plays an important role in spindle pole assembly during mitosis and in chromosomes movement.

**Summary**, from NCBI Gene [9126](https://www.ncbi.nlm.nih.gov/gene/9126):

> This gene belongs to the SMC3 subfamily of SMC proteins. The encoded protein occurs in certain cell types as either an intracellular, nuclear protein or a secreted protein. The nuclear form, known as structural maintenance of chromosomes 3, is a component of the multimeric cohesin complex that holds together sister chromatids during mitosis, enabling proper chromosome segregation. Post-translational modification of the encoded protein by the addition of chondroitin sulfate chains gives rise to …

**Accessions** — [HGNC:2468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2468) · Entrez [9126](https://www.ncbi.nlm.nih.gov/gene/9126) · UniProt [Q9UQE7](https://www.uniprot.org/uniprotkb/Q9UQE7) · Ensembl [ENSG00000108055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108055)

## Data

Gene col 2913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2913); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2913]; `tensor/DDL_lfc|DDL_z.npy` [2913]; `embed/gene_vectors.npy` [2913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2913 or target_col == 2913). Every well: [[SMC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
