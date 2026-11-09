---
symbol: "TRIM4"
type: "gene"
col: 7124
ensembl_id: "ENSG00000146833"
name: "tripartite motif containing 4"
location: "7q22.1"
module: 149
arm: "+"
pooled_cpm: 53.96
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# TRIM4

*tripartite motif containing 4* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.20× (z +10.3, q 6e-22, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.683× (z -9.5, q 8e-19, down in 35 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (COLO 205 0.115×, LoVo 0.255×, SNU-1 0.165×, PANC-1 0.408×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.361×, C32 0.317×, H4 0.225×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.189×, NCI-H1792 0.257×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[OTS514 (drug)]] 5 µM in 1 line (HCT15 0.122×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0996×); [[Silodosin (drug)]] 5 µM in 1 line (SW 1271 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.76, fdr 7e-06), [[ZNF3]] (+0.75, fdr 7e-06), [[ZNF557]] (+0.74, fdr 7e-06); moves opposite to [[HPRT1]] (-0.61, fdr 7e-06), [[TFRC]] (-0.59, fdr 1e-05), [[RBBP7]] (-0.59, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +10.3 | 6e-22 | 32/47 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +10.0 | 6e-21 | 30/45 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +9.8 | 2e-20 | 33/45 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +6.0 | 3e-07 | 25/46 (NCI-H460, HCT15, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +4.6 | 4e-04 | 19/44 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +4.4 | 9e-04 | 15/47 (C32, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.003 | 20/44 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.009 | 6/47 (RKO, Panc 03.27, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.025 | 8/47 (C32, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.030 | 14/46 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.042 | 7/46 (KATO III, HOP62, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.14× | +3.3 | 0.053 | 9/46 (A498, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.2 | 0.054 | 0/47 | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.059 | 7/45 (PANC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.086 | 9/45 (C-33 A, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7124.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (COLO 205 0.115×, LoVo 0.255×, SNU-1 0.165×, PANC-1 0.408×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.361×, C32 0.317×, H4 0.225×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.189×, NCI-H1792 0.257×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[OTS514 (drug)]] 5 µM in 1 line (HCT15 0.122×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0996×); [[Silodosin (drug)]] 5 µM in 1 line (SW 1271 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -9.5 | 8e-19 | 35/46 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.673×** | -9.5 | 8e-19 | 26/40 (PANC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.698×** | -9.0 | 7e-17 | 33/47 (COLO 205, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -8.0 | 2e-13 | 30/44 (A-427, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.768×** | -6.6 | 6e-09 | 27/46 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.774×** | -5.9 | 3e-07 | 23/41 (A-427, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.804×** | -5.4 | 5e-06 | 24/46 (NCI-H460, SW48, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.862× | -3.7 | 0.014 | 6/46 (LoVo, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.862× | -3.7 | 0.014 | 11/46 (KATO III, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.864× | -3.6 | 0.016 | 15/46 (NCI-H460, SW48, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.877× | -3.3 | 0.055 | 14/46 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.884× | -3.1 | 0.087 | 6/47 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.884× | -3.1 | 0.087 | 2/46 (A-427, NCI-H1573) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.917× | -3.1 | 0.087 | 15/47 (A498, CHP-212, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.090 | 5/46 (NCI-H2030, SNU-423, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 116 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 89.9 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -12.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[LoVo (line)]] | wt | 93.6 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.46× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 49.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 77.7 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -11.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 45.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 54.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -10.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 64.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 55.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.1) | [[OTS514 (drug)]] 5 µM 0.122× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 45.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 42.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.459× (z -10.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW 1088 (line)]] | alt | 91.0 | 0 | 2 (1 ⚠) | — | [[5-Azacytidine (drug)]] 0.5 µM 0.123× (z -8.8) |
| [[SW 1271 (line)]] | alt | 77.5 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0996× (z -9.5) |
| [[A549 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.323× (z -10.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -9.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 71.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 69.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 59.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 78.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 77.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.7) | — |
| [[A-172 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.76 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[ZNF557]] | +0.74 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[GOSR1]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[MTERF4]] | +0.73 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SPOP]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[RPP14]] | +0.71 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[TTF1]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[NKAPD1]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPRT1]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[TFRC]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.842). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.7, 4.5); signed map (-4.4, -13.5). **Vector** length 105, 24.6% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -7.0 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -6.9 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.2 | -5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,876,958-99,919,531 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF87 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 17 pathways, smallest: NF-kB activation through FADD/RIP-1 pathway mediated by caspase-8 and -10; TRAF3-dependent IRF activation pathway; TRAF6 mediated IRF7 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C037](https://www.uniprot.org/uniprotkb/Q9C037) (E3 ubiquitin-protein ligase TRIM4):

> E3 ubiquitin-protein ligase. Mediates 'Lys-63'-linked polyubiquitination of the innate immune receptor RIGI, this linkage does not lead to proteasomal degradation but seems to enhance IFN induction.

**Summary**, from NCBI Gene [89122](https://www.ncbi.nlm.nih.gov/gene/89122):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to cytoplasmic bodies. Its function has not been identified. Alternatively spliced transcript variants that encode different isoforms have been described.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:16275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16275) · Entrez [89122](https://www.ncbi.nlm.nih.gov/gene/89122) · UniProt [Q9C037](https://www.uniprot.org/uniprotkb/Q9C037) · Ensembl [ENSG00000146833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146833)

## Data

Gene col 7124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7124); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7124]; `tensor/DDL_lfc|DDL_z.npy` [7124]; `embed/gene_vectors.npy` [7124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7124 or target_col == 7124). Every well: [[TRIM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
