---
symbol: "PARK7"
type: "gene"
col: 3787
ensembl_id: "ENSG00000116288"
name: "Parkinsonism associated deglycase"
location: "1p36.23"
module: 29
arm: "+"
pooled_cpm: 63.76
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# PARK7

*Parkinsonism associated deglycase* — 1p36.23

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.38× (z +16.9, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 5.42×, PANC-1 4.38×, NCI-H460 5.13×, HOP62 5.31×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 5.51×, PANC-1 4.18×, SNU-423 7.27×, HT-29 6.03×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (H4 0.249×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1A]] (+0.61, fdr 1e-05), [[BANF1]] (+0.57, fdr 5e-05), [[LSM4]] (+0.57, fdr 6e-05); moves opposite to [[ZFTA]] (-0.60, fdr 2e-05), [[SNHG12]] (-0.58, fdr 6e-05), [[NPIPP1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 5.42×, PANC-1 4.38×, NCI-H460 5.13×, HOP62 5.31×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 5.51×, PANC-1 4.18×, SNU-423 7.27×, HT-29 6.03×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.38×** | +16.9 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.07×** | +15.5 | 0e+00 | 42/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.78×** | +10.8 | 5e-25 | 44/44 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.56×** | +5.1 | 4e-05 | 37/47 (SW 900, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.41×** | +3.9 | 0.009 | 31/48 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.38×** | +3.7 | 0.021 | 31/48 (SHP-77, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.34×** | +3.4 | 0.052 | 24/48 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.36×** | +3.4 | 0.052 | 26/49 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.3 | 0.058 | 25/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (H4 0.249×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.574× | -3.3 | 0.53 | 26/48 (AN3 CA, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.726× | -3.1 | 0.53 | 26/49 (A-427, CHP-212, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 42.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 62.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 58.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.52× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 37.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Selinexor (drug)]] 5 µM 0.249× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 68.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 71.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 50.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.03× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 66.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 57.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 59.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 77.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 57.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 46.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 65.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 61.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 60.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 86.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 75.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 53.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 34.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 49.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 55.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 42.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 121 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 54.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 40.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 78.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 43.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 41.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 75.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.77× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HCT15 (line)]] | alt | 64.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 65.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 89.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 78.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW48 (line)]] | wt | 46.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.64× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1A]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 | STRING 457 |
| [[BANF1]] | +0.57 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[LSM4]] | +0.57 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[MDH2]] | +0.56 | +0.57 / +0.43 | both halves | 3e-05 | STRING 576 |
| [[PIGK]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[MED14]] | +0.55 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[HNRNPA3]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[PRKDC]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[DNAJC10]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 | STRING 452 |
| [[SRP9]] | +0.52 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[TMED7]] | +0.51 | +0.40 / +0.37 | both halves | 9e-05 |  |
| [[HNRNPR]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFTA]] | -0.60 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SNHG12]] | -0.58 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[NPIPP1]] | -0.58 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[FNBP4]] | -0.57 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[CDK3]] | -0.56 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[EIF4EBP3]] | -0.54 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[MAFG]] | -0.54 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[WHAMM]] | -0.54 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[WASHC1]] | -0.54 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[EGLN2]] | -0.53 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[ARL8A]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SHROOM1]] | -0.53 | -0.33 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-37.7, -30.2); signed map (-25.6, -41.0). **Vector** length 52.2, 12.1% of its response variance represented; |z| ≥ 3 in 550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -0.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.3 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +1.3 | +3.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.3 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +1.2 | -1.4 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.1 | -0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.1 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.9 | +2.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.8 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | Parkinsonism associated deglycase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.23 — chr1:7,954,291-7,985,505 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DJ-1, DJ1, GATD2 |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing |
| Reactome | 9 pathways, smallest: Chaperone Mediated Autophagy; Late endosomal microautophagy; Aggrephagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99497](https://www.uniprot.org/uniprotkb/Q99497) (Parkinson disease protein 7):

> Multifunctional protein with controversial molecular function which plays an important role in cell protection against oxidative stress and cell death acting as oxidative stress sensor and redox-sensitive chaperone and protease. It is involved in neuroprotective mechanisms like the stabilization of NFE2L2 and PINK1 proteins, male fertility as a positive regulator of androgen signaling pathway as well as cell growth and transformation through, for instance, the modulation of NF-kappa-B signaling …

**Summary**, from NCBI Gene [11315](https://www.ncbi.nlm.nih.gov/gene/11315):

> The product of this gene belongs to the peptidase C56 family of proteins. It acts as a positive regulator of androgen receptor-dependent transcription. It may also function as a redox-sensitive chaperone, as a sensor for oxidative stress, and it apparently protects neurons against oxidative stress and cell death. Defects in this gene are the cause of autosomal recessive early-onset Parkinson disease 7. Two transcript variants encoding the same protein have been identified for this gene. …

**Accessions** — [HGNC:16369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16369) · Entrez [11315](https://www.ncbi.nlm.nih.gov/gene/11315) · UniProt [Q99497](https://www.uniprot.org/uniprotkb/Q99497) · Ensembl [ENSG00000116288](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116288)

## Data

Gene col 3787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3787); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3787]; `tensor/DDL_lfc|DDL_z.npy` [3787]; `embed/gene_vectors.npy` [3787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3787 or target_col == 3787). Every well: [[PARK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
