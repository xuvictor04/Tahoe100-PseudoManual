---
symbol: "NME2"
type: "gene"
col: 14371
ensembl_id: "ENSG00000243678"
name: "NME/NM23 nucleoside diphosphate kinase 2"
location: "17q21.33"
module: 43
arm: "+"
pooled_cpm: 119.95
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# NME2

*NME/NM23 nucleoside diphosphate kinase 2* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.03× (z +9.7, q 2e-19, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 11 lines (LoVo 6.38×, SW480 5.34×, KATO III 4.69×, HOP62 5.40×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 6.49×, SW480 6.34×, KATO III 5.77×, HOP62 6.32×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.389× (z -9.6, q 4e-19, down in 45 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (HT-29 0.174×, NCI-H2030 0.191×, SNU-1 0.208×, SW480 0.232×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL27A]] (+0.81, fdr 7e-06), [[RPLP0]] (+0.80, fdr 7e-06), [[UQCRH]] (+0.78, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.70, fdr 7e-06), [[ZNF764]] (-0.70, fdr 1e-05), [[LARP7]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14371.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 11 lines (LoVo 6.38×, SW480 5.34×, KATO III 4.69×, HOP62 5.40×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 6.49×, SW480 6.34×, KATO III 5.77×, HOP62 6.32×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.03×** | +9.7 | 2e-19 | 43/44 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.45×** | +9.0 | 7e-17 | 49/49 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.95×** | +7.2 | 9e-11 | 44/45 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.7 | 4e-04 | 43/47 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.89×** | +4.6 | 4e-04 | 43/48 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.84×** | +4.4 | 9e-04 | 45/48 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.67×** | +3.6 | 0.026 | 39/47 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.55× | +3.0 | 0.17 | 42/48 (A498, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14371.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (HT-29 0.174×, NCI-H2030 0.191×, SNU-1 0.208×, SW480 0.232×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.389×** | -9.6 | 4e-19 | 45/48 (HT-29, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.473×** | -5.4 | 2e-05 | 37/48 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 134 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.4) |
| [[HOP62 (line)]] | alt | 100 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.2) |
| [[HT-29 (line)]] | alt | 102 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.4) |
| [[LoVo (line)]] | wt | 125 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.38× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.5) |
| [[LS 180 (line)]] | wt | 132 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 58.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.05× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.3) |
| [[SW480 (line)]] | alt | 115 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.7) |
| [[C-33 A (line)]] | alt | 101 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.7) |
| [[C32 (line)]] | wt | 68.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 159 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.63× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.69× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 128 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.6) |
| [[PANC-1 (line)]] | alt | 170 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.2) |
| [[A-172 (line)]] | wt | 94.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 67.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.4) |
| [[BT-474 (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.0) |
| [[COLO 205 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.94× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 171 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 85.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.4) |
| [[J82 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.9) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[RKO (line)]] | wt | 148 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 68.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -8.7) |
| [[SHP-77 (line)]] | alt | 82.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.3) |
| [[SNU-1 (line)]] | wt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -14.0) |
| [[SNU-423 (line)]] | alt | 89.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 1271 (line)]] | alt | 70.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -8.6) |
| [[SW1417 (line)]] | alt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.1) |
| [[A-427 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL27A]] | +0.81 | +0.78 / +0.77 | both halves | 7e-06 | STRING 595 |
| [[RPLP0]] | +0.80 | +0.77 / +0.70 | both halves | 7e-06 | STRING 632 |
| [[UQCRH]] | +0.78 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[RPS24]] | +0.77 | +0.78 / +0.65 | both halves | 7e-06 | STRING 476 |
| [[RPS5]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | STRING 617 |
| [[RPL12]] | +0.76 | +0.71 / +0.73 | both halves | 7e-06 | STRING 611 |
| [[RACK1]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 | STRING 614 |
| [[RPS2]] | +0.74 | +0.61 / +0.73 | both halves | 7e-06 | STRING 729 |
| [[RPL7]] | +0.73 | +0.65 / +0.69 | both halves | 7e-06 | STRING 451 |
| [[RPS14]] | +0.73 | +0.76 / +0.64 | both halves | 7e-06 | STRING 595 |
| [[RPS25]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 | STRING 559 |
| [[RPL39]] | +0.72 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.70 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[ZNF764]] | -0.70 | -0.76 / -0.51 | both halves | 1e-05 |  |
| [[LARP7]] | -0.69 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[MIS12]] | -0.69 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[LZIC]] | -0.67 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[ZNF181]] | -0.67 | -0.73 / -0.42 | both halves | 4e-05 |  |
| [[FAM200A]] | -0.67 | -0.79 / -0.30 | both halves | 2e-04 |  |
| [[SCAF1]] | -0.67 | -0.69 / -0.46 | both halves | 2e-05 |  |
| [[TIA1]] | -0.66 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[CHMP4A]] | -0.65 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[C19orf54]] | -0.65 | -0.71 / -0.34 | both halves | 1e-04 |  |
| [[ZNF620]] | -0.65 | -0.71 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-47.1, -29.3); signed map (-61.8, -5.9). **Vector** length 71.0, 35.5% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.63 to 55); *Peptide chain elongation* (reactome, mean cos +0.63 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.63 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | -1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.1 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.7 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.4 | +2.0 |

## What is on record

|  |  |
|---|---|
| Name | NME/NM23 nucleoside diphosphate kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:51,165,435-51,171,744 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NM23-H2, NDPKB |
| Gene groups (HGNC) | NME/NM23 family |
| Reactome | 7 pathways, smallest: Ribavirin ADME; Azathioprine ADME; Interconversion of nucleotide di- and triphosphates |
| Matched by | ensembl_id |

**Function**, from UniProt [P22392](https://www.uniprot.org/uniprotkb/P22392) (Nucleoside diphosphate kinase B):

> Catalyzes the transfer of a gamma-phosphoryl group from a nucleoside triphosphate, mainly ATP, to a nucleoside diphosphate via a ping-pong mechanism involving a phosphohistidine intermediate, therefore contributing to the nucleoside triphosphate homeostasis. Also functions as a histidine protein kinase by transferring the phosphoryl group from the phosphohistidine intermediate to a histidine residue in target proteins. Phosphorylates the GNB1 subunit of heterotrimeric G proteins at 'His-266', …

**Summary**, from NCBI Gene [4831](https://www.ncbi.nlm.nih.gov/gene/4831):

> Nucleoside diphosphate kinase (NDK) exists as a hexamer composed of 'A' (encoded by NME1) and 'B' (encoded by this gene) isoforms. Multiple alternatively spliced transcript variants have been found for this gene. Read-through transcription from the neighboring upstream gene (NME1) generates naturally-occurring transcripts (NME1-NME2) that encode a fusion protein comprised of sequence sharing identity with each individual gene product. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:7850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7850) · Entrez [4831](https://www.ncbi.nlm.nih.gov/gene/4831) · UniProt [P22392](https://www.uniprot.org/uniprotkb/P22392) · Ensembl [ENSG00000243678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243678)

## Data

Gene col 14371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14371); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14371]; `tensor/DDL_lfc|DDL_z.npy` [14371]; `embed/gene_vectors.npy` [14371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14371 or target_col == 14371). Every well: [[NME2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NME2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
