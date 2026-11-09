---
symbol: "AIMP2"
type: "gene"
col: 2742
ensembl_id: "ENSG00000106305"
name: "aminoacyl tRNA synthetase complex interacting multifunctional protein 2"
location: "7p22.1"
module: 1
arm: "+"
pooled_cpm: 18.39
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# AIMP2

*aminoacyl tRNA synthetase complex interacting multifunctional protein 2* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.71× (z +23.4, q 0e+00, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.34× (z +11.4, q 5e-28, up in 38 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.05 µM in 1 line (SNU-423 0.0534×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.350×; ⚠ cell-cycle shift, explains ~54% of this change); [[Cinacalcet (drug)]] 0.5 µM in 1 line (AN3 CA 0.0586×); [[Decitabine (drug)]] 0.05 µM in 1 line (HCT15 0.0673×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOX2]] (+0.72, fdr 7e-06), [[DMAC2L]] (+0.70, fdr 7e-06), [[COA7]] (+0.69, fdr 7e-06); moves opposite to [[NARF]] (-0.57, fdr 1e-05), [[EMSY]] (-0.57, fdr 1e-05), [[TESK2]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.71×** | +23.4 | 0e+00 | 39/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.54×** | +22.1 | 0e+00 | 27/29 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.82×** | +19.6 | 0e+00 | 32/33 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +11.4 | 5e-28 | 38/47 (A-172, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.29×** | +11.1 | 9e-27 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +8.9 | 5e-17 | 38/47 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.75×** | +7.5 | 5e-12 | 30/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +7.5 | 5e-12 | 29/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +6.8 | 9e-10 | 33/42 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +5.6 | 1e-06 | 26/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +5.6 | 1e-06 | 24/47 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.50×** | +5.4 | 3e-06 | 27/44 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +5.3 | 6e-06 | 22/47 (A-172, C32, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +5.2 | 8e-06 | 20/48 (PANC-1, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **2.02×** | +4.9 | 3e-05 | 20/44 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +4.6 | 2e-04 | 21/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.85×** | +4.3 | 5e-04 | 15/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.001 | 14/47 (HT-29, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.007 | 9/46 (HOP62, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.008 | 14/47 (NCI-H2347, KATO III, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.009 | 15/47 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.017 | 13/44 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.05 µM in 1 line (SNU-423 0.0534×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.350×; ⚠ cell-cycle shift, explains ~54% of this change); [[Cinacalcet (drug)]] 0.5 µM in 1 line (AN3 CA 0.0586×); [[Decitabine (drug)]] 0.05 µM in 1 line (HCT15 0.0673×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.0 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.4× (z +17.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 21.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.41× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 26.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.53× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.09× (z +10.0) | — |
| [[A498 (line)]] | wt | 21.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +15.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.3× (z +14.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 16.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.8× (z +11.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 22.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 13.8× (z +16.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 22.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +12.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 18.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.6× (z +22.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 17.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 34.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.0× (z +15.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 27.2× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.12× (z +8.7) ⚠ toxic; transcription drop | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.166× (z -8.5) ⚠ transcription drop; unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 7.75 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +10.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 15.3× (z +13.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 33.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.39× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 9.13 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +10.3) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 0.05 µM 0.0534× (z -11.8) |
| [[A-427 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0586× (z -9.6) |
| [[BT-474 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.25× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 9.37 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.9× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0673× (z -9.2) |
| [[HS-578T (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +8.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 6.74 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.8× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.88× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +9.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.4× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW 900 (line)]] | alt | 9.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOX2]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[DMAC2L]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[COA7]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[TXNRD3]] | +0.65 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[DCAF17]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[DPH5]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MRRF]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[GTF2H3]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[RRP15]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RBM45]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | -0.57 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[EMSY]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[TESK2]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ZNHIT1]] | -0.54 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RASA4B]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SYNJ1]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[GLCCI1]] | -0.52 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[LIN54]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PHF1]] | -0.51 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SBNO1]] | -0.51 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TSC22D4]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.5, -37.5); signed map (0.3, -39.4). **Vector** length 82.9, 17.7% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +19.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +23.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +22.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +4.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -2.6 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | aminoacyl tRNA synthetase complex interacting multifunctional protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,009,255-6,023,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p38, PRO0992, JTV-1, JTV1 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Aminoacyl tRNA synthetase complex interacting multifunctional proteins |
| Hallmark sets | MYC_TARGETS_V2, MYC_TARGETS_V1 |
| Reactome | 7 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13155](https://www.uniprot.org/uniprotkb/Q13155) (Aminoacyl tRNA synthase complex-interacting multifunctional protein 2):

> Required for assembly and stability of the aminoacyl-tRNA synthase complex. Mediates ubiquitination and degradation of FUBP1, a transcriptional activator of MYC, leading to MYC down-regulation which is required for aveolar type II cell differentiation. Blocks MDM2-mediated ubiquitination and degradation of p53/TP53. Functions as a pro-apoptotic factor.

**Summary**, from NCBI Gene [7965](https://www.ncbi.nlm.nih.gov/gene/7965):

> The protein encoded by this gene is part of the aminoacyl-tRNA synthetase complex, which contains nine different aminoacyl-tRNA synthetases and three non-enzymatic factors. The encoded protein is one of the non-enzymatic factors and is required for assembly and stability of the complex. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:20609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20609) · Entrez [7965](https://www.ncbi.nlm.nih.gov/gene/7965) · UniProt [Q13155](https://www.uniprot.org/uniprotkb/Q13155) · Ensembl [ENSG00000106305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106305)

## Data

Gene col 2742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2742); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2742]; `tensor/DDL_lfc|DDL_z.npy` [2742]; `embed/gene_vectors.npy` [2742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2742 or target_col == 2742). Every well: [[AIMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
