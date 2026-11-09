---
symbol: "ECHS1"
type: "gene"
col: 4839
ensembl_id: "ENSG00000127884"
name: "enoyl-CoA hydratase, short chain 1"
location: "10q26.3"
module: 25
arm: "+"
pooled_cpm: 30.05
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ECHS1

*enoyl-CoA hydratase, short chain 1* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.02× (z +19.0, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.26× (z +3.2, q 0.084, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.79×, SW480 4.41×, NCI-H460 4.66×, LS 180 4.51×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 4.30×, SNU-423 5.60×, PANC-1 3.65×, SW480 3.40×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.637× (z -6.1, q 5e-07, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.695× (z -4.9, q 2e-04, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLD]] (+0.74, fdr 7e-06), [[BCKDK]] (+0.64, fdr 2e-05), [[GPS1]] (+0.64, fdr 1e-05); moves opposite to [[MAFG]] (-0.66, fdr 3e-05), [[MIA]] (-0.65, fdr 3e-05), [[SPATC1]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4839.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.79×, SW480 4.41×, NCI-H460 4.66×, LS 180 4.51×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 4.30×, SNU-423 5.60×, PANC-1 3.65×, SW480 3.40×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.02×** | +19.0 | 0e+00 | 43/43 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.36×** | +15.9 | 0e+00 | 36/37 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +13.7 | 1e-40 | 37/42 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.29×** | +11.3 | 2e-27 | 46/48 (SW480, PANC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.18×** | +10.7 | 2e-24 | 46/48 (SW480, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.60×** | +6.4 | 1e-08 | 39/48 (SW480, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.6 | 2e-06 | 30/46 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.46×** | +5.1 | 2e-05 | 29/46 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.1 | 0.002 | 2/48 (SNU-1, SW 1088) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.084 | 19/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.18× | +3.1 | 0.096 | 10/48 (SHP-77, LS 180, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.18× | +3.1 | 0.100 | 11/48 (HT-29, CHP-212, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.25×** | +3.0 | 0.100 | 18/48 (NCI-H1573, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4839.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -6.1 | 5e-07 | 30/46 (LS 180, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.695×** | -4.9 | 2e-04 | 30/47 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.696×** | -4.9 | 2e-04 | 29/48 (SW 1088, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.710×** | -4.7 | 5e-04 | 27/48 (SW 900, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.738×** | -4.1 | 0.004 | 26/47 (C-33 A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.595×** | -3.7 | 0.021 | 22/47 (SW480, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.782×** | -3.3 | 0.068 | 20/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.784×** | -3.3 | 0.070 | 18/47 (A498, BT-474, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 26.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 38.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 26.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 32.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 32.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 30.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 60.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.99× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 32.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 24.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C-33 A (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 2 (1 ⚠) | — | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM 0.0689× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 19.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 42.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 21.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-423 (line)]] | alt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 26.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 50.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HCT15 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HS-578T (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H661 (line)]] | alt | 51.0 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0677× (z -10.5) |
| [[SW1417 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | +0.74 | +0.63 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 491 |
| [[BCKDK]] | +0.64 | +0.47 / +0.48 | both halves | 2e-05 | pathway: Branched-chain amino acid catabolism; STRING 509 |
| [[GPS1]] | +0.64 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PDHB]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 527 |
| [[ATP5F1A]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[AP2M1]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[LANCL1]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[AGO1]] | +0.61 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PHF6]] | +0.61 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[TAF6]] | +0.60 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[THYN1]] | +0.60 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[API5]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFG]] | -0.66 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[MIA]] | -0.65 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[SPATC1]] | -0.62 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[KIF9-AS1]] | -0.60 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[LINC00685]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | -0.58 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[DEAF1]] | -0.58 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[EHBP1-AS1]] | -0.58 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[IL12RB2]] | -0.58 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[SPESP1]] | -0.58 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[BIRC6-AS2-1]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ST7-AS2]] | -0.57 | -0.31 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ECHS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.9, -17.3); signed map (-26.4, -44.2). **Vector** length 72.5, 15.9% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.7 | +11.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.5 | +10.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.4 | +6.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +1.7 | +3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +1.4 | +0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +0.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.4 | -0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | enoyl-CoA hydratase, short chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:133,362,485-133,373,354 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCEH |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Enoyl-CoA hydratases |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 13 pathways, smallest: Beta oxidation of butanoyl-CoA to acetyl-CoA; Beta oxidation of lauroyl-CoA to decanoyl-CoA-CoA; Beta oxidation of hexanoyl-CoA to butanoyl-CoA |
| Matched by | ensembl_id |

**Function**, from UniProt [P30084](https://www.uniprot.org/uniprotkb/P30084) (Enoyl-CoA hydratase, mitochondrial):

> Converts unsaturated trans-2-enoyl-CoA species ((2E)-enoyl-CoA) to the corresponding (3S)-3hydroxyacyl-CoA species through addition of a water molecule to the double bond. Catalyzes the hydration of medium- and short-chained fatty enoyl-CoA thioesters from 4 carbons long (C4) up to C16. Has high substrate specificity for crotonyl-CoA ((2E)-butenoyl-CoA) and moderate specificity for acryloyl-CoA, 3-methylcrotonyl-CoA (3-methyl-(2E)-butenoyl-CoA) and methacrylyl-CoA ((2E)-2-methylpropenoyl-CoA). …

**Summary**, from NCBI Gene [1892](https://www.ncbi.nlm.nih.gov/gene/1892):

> The protein encoded by this gene functions in the second step of the mitochondrial fatty acid beta-oxidation pathway. It catalyzes the hydration of 2-trans-enoyl-coenzyme A (CoA) intermediates to L-3-hydroxyacyl-CoAs. The gene product is a member of the hydratase/isomerase superfamily. It localizes to the mitochondrial matrix. Transcript variants utilizing alternative transcription initiation sites have been described in the literature. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3151) · Entrez [1892](https://www.ncbi.nlm.nih.gov/gene/1892) · UniProt [P30084](https://www.uniprot.org/uniprotkb/P30084) · Ensembl [ENSG00000127884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127884)

## Data

Gene col 4839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4839); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4839]; `tensor/DDL_lfc|DDL_z.npy` [4839]; `embed/gene_vectors.npy` [4839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4839 or target_col == 4839). Every well: [[ECHS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECHS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
