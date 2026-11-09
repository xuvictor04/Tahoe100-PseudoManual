---
symbol: "STT3B"
type: "gene"
col: 8709
ensembl_id: "ENSG00000163527"
name: "STT3 oligosaccharyltransferase complex catalytic subunit B"
location: "3p23"
module: 29
arm: "+"
pooled_cpm: 180.27
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# STT3B

*STT3 oligosaccharyltransferase complex catalytic subunit B* — 3p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +12.4, q 2e-32, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.781× (z -4.7, q 0.002, down in 32 of 47 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (SW1417 0.491×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.584×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTAP]] (+0.75, fdr 7e-06), [[FKBP9]] (+0.70, fdr 7e-06), [[TMEM123]] (+0.69, fdr 7e-06); moves opposite to [[PDRG1]] (-0.69, fdr 7e-06), [[DNTTIP1]] (-0.69, fdr 9e-06), [[CCDC174]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.4 | 2e-32 | 36/49 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +10.8 | 8e-25 | 44/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +10.0 | 3e-21 | 40/47 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +8.1 | 1e-13 | 38/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +7.7 | 2e-12 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +7.5 | 5e-12 | 43/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.4 | 1e-11 | 33/48 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +6.6 | 2e-09 | 33/48 (SNU-423, RPMI-7951, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 1e-08 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +6.0 | 1e-07 | 40/49 (C32, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.33×** | +5.4 | 3e-06 | 28/44 (HOP62, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +4.7 | 1e-04 | 29/50 (C32, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.25×** | +4.3 | 8e-04 | 29/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +4.2 | 0.001 | 25/48 (SNU-423, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +4.0 | 0.003 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.011 | 21/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.027 | 24/48 (SW 900, SNU-423, …) | two highest doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.069 | 14/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +2.9 | 0.087 | 15/49 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (SW1417 0.491×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.584×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.781×** | -4.7 | 0.002 | 32/47 (SW1417, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.854× | -4.4 | 0.003 | 19/48 (A-427, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.11 | 18/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.772× | -3.3 | 0.14 | 19/48 (SW 1088, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.19 | 13/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.740× | -3.1 | 0.19 | 22/45 (PANC-1, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 133 | 9 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +12.8) | — |
| [[C32 (line)]] | wt | 139 | 7 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.2× (z +16.7) | — |
| [[SNU-423 (line)]] | alt | 191 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 194 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 133 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.39× (z +9.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +8.5) | — |
| [[J82 (line)]] | alt | 165 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +10.0) | — |
| [[LoVo (line)]] | wt | 176 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.25× (z +10.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 133 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 145 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.12× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.8) | — |
| [[A-172 (line)]] | wt | 138 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.1) | — |
| [[A498 (line)]] | wt | 107 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 144 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 125 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.14× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.04× (z +8.6) | — |
| [[RKO (line)]] | wt | 166 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 89.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +16.6) | — |
| [[CFPAC-1 (line)]] | alt | 81.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 149 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 97.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 135 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 384 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 118 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 223 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 133 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 144 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 798 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.491× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 312 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.55× (z +9.8) | — |
| [[SW480 (line)]] | alt | 300 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 1.72× (z +8.8) | — |
| [[A-427 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 185 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 250 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 234 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 193 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 169 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 173 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAP]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TMEM123]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[RBBP7]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | pathway: Co-inhibition by PD-1 |
| [[GMPS]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[HNRNPA3]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[GPC4]] | +0.65 | +0.62 / +0.57 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[ADAM15]] | +0.64 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[CMPK1]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PDIA6]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 | STRING 435 |

## Genes that move opposite

*63 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDRG1]] | -0.69 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[DNTTIP1]] | -0.69 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[CCDC174]] | -0.67 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.67 | -0.57 / -0.69 | both halves | 1e-05 |  |
| [[MED18]] | -0.66 | -0.64 / -0.69 | both halves | 7e-06 |  |
| [[ZNF557]] | -0.66 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[ZNF611]] | -0.66 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[LLPH]] | -0.66 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[LRRC8E]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[R3HCC1]] | -0.65 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[ZCCHC9]] | -0.65 | -0.53 / -0.72 | both halves | 1e-05 |  |
| [[MFAP1]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.8, -21.5); signed map (-22.9, -39.5). **Vector** length 122, 41.1% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +7.7 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +7.7 | +5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.0 | +10.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.4 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.1 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.1 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.3 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | STT3 oligosaccharyltransferase complex catalytic subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p23 — chr3:31,532,638-31,637,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIMP, FLJ90106, STT3-B |
| Gene groups (HGNC) | STT3 oligosaccharyltransferase catalytic subunits; Oligosaccharyltransferase complex subunits |
| Reactome | 21 pathways, smallest: Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition; PD-L1(CD274) glycosylation and translocation to plasma membrane; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCJ2](https://www.uniprot.org/uniprotkb/Q8TCJ2) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit STT3B):

> Catalytic subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates …

**Summary**, from NCBI Gene [201595](https://www.ncbi.nlm.nih.gov/gene/201595):

> The protein encoded by this gene is a catalytic subunit of a protein complex that transfers oligosaccharides onto asparagine residues. Defects in this gene are a cause of congenital disorder of glycosylation Ix (CDG1X). [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:30611](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30611) · Entrez [201595](https://www.ncbi.nlm.nih.gov/gene/201595) · UniProt [Q8TCJ2](https://www.uniprot.org/uniprotkb/Q8TCJ2) · Ensembl [ENSG00000163527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163527)

## Data

Gene col 8709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8709); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8709]; `tensor/DDL_lfc|DDL_z.npy` [8709]; `embed/gene_vectors.npy` [8709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8709 or target_col == 8709). Every well: [[STT3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STT3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
