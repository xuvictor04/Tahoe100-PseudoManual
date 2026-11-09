---
symbol: "PTMA"
type: "gene"
col: 11917
ensembl_id: "ENSG00000187514"
name: "prothymosin alpha"
location: "2q37.1"
module: 7
arm: "-"
pooled_cpm: 1080.72
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PTMA

*prothymosin alpha* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.80× (z +7.2, q 3e-10, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H1792 6.24×, SNU-423 4.43×, A549 5.31×, HT-29 4.26×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 3.32×, NCI-H460 3.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1792 8.55×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.630× (z -4.8, q 9e-04, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (SNU-1 0.168×, HCT15 0.172×, MIA PaCa-2 0.213×, LS 180 0.222×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (SNU-1 0.168×, LS 180 0.172×, MIA PaCa-2 0.239×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.300×, SNU-1 0.352×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTMAP5]] (+0.85, fdr 7e-06), [[PTMAP2]] (+0.80, fdr 7e-06, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[A2MP1]] (+0.72, fdr 7e-06), [[SLC25A5]] (+0.63, fdr 1e-05); moves opposite to [[ZXDB]] (-0.69, fdr 7e-06), [[CBLL1]] (-0.63, fdr 2e-05), [[CENPBD1P]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H1792 6.24×, SNU-423 4.43×, A549 5.31×, HT-29 4.26×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 3.32×, NCI-H460 3.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1792 8.55×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.80×** | +7.2 | 3e-10 | 43/44 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.68×** | +7.0 | 8e-10 | 49/49 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.03×** | +5.2 | 4e-05 | 47/48 (KATO III, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **2.00×** | +5.1 | 6e-05 | 48/48 (SW 900, BT-474, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.10×** | +5.0 | 6e-05 | 41/45 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | 1.57× | +3.2 | 0.15 | 36/47 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.55× | +3.1 | 0.17 | 44/48 (SNU-423, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (SNU-1 0.168×, HCT15 0.172×, MIA PaCa-2 0.213×, LS 180 0.222×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (SNU-1 0.168×, LS 180 0.172×, MIA PaCa-2 0.239×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.300×, SNU-1 0.352×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.630×** | -4.8 | 9e-04 | 36/48 (SNU-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -4.4 | 0.003 | 37/48 (SNU-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.423× | -3.3 | 0.18 | 45/49 (C32, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 0.661× | -3.0 | 0.34 | 44/48 (SW 1271, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 2,478 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -12.9) |
| [[SNU-1 (line)]] | wt | 2,868 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.5) |
| [[HT-29 (line)]] | alt | 1,191 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 1,910 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 700 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.24× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 1,030 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 937 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.8) |
| [[A498 (line)]] | wt | 615 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 748 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.31× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C-33 A (line)]] | alt | 824 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.9) |
| [[CHP-212 (line)]] | wt | 1,270 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.6) |
| [[HCT15 (line)]] | alt | 1,468 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 360 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 672 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 1,061 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.32× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SHP-77 (line)]] | alt | 1,193 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.6) |
| [[SNU-423 (line)]] | alt | 613 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 1,069 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.8) |
| [[A-172 (line)]] | wt | 833 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1,085 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 982 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 902 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 534 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1,584 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 664 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 896 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 802 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1,102 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 871 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 762 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 644 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 902 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1,073 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 730 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 780 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 807 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1,052 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1,646 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1,201 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1,393 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1,450 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 689 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 802 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 636 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 838 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1,025 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1,138 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1,899 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2,078 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMAP5]] | +0.85 | +0.90 / +0.72 | both halves | 7e-06 |  |
| [[PTMAP2]] ⚠ | +0.80 | +0.83 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[A2MP1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SLC25A5]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RFX2]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.60 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[IGFBP2]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TESK2]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[AHDC1]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[METRN]] | +0.56 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[COX6A1]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | -0.69 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[CBLL1]] | -0.63 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[CENPBD1P]] | -0.62 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[ZNF518B]] | -0.61 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[EIF6]] | -0.61 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[RNF6]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[ZSCAN29]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[EMG1]] | -0.61 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[RIMOC1]] | -0.60 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ATMIN]] | -0.60 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[ACTR8]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ZNF621]] | -0.59 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-55.4, -16.5); signed map (-39.1, 16.4). **Vector** length 96.9, 53.0% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.5 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -6.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -6.6 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.9 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -0.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | prothymosin alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,706,895-231,713,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TMSA |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P06454](https://www.uniprot.org/uniprotkb/P06454) (Prothymosin alpha):

> Prothymosin alpha may mediate immune function by conferring resistance to certain opportunistic infections.

**Summary**, from NCBI Gene [5757](https://www.ncbi.nlm.nih.gov/gene/5757):

> Enables DNA-binding transcription factor binding activity; calcium ion binding activity; and histone binding activity. Involved in negative regulation of apoptotic process. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9623) · Entrez [5757](https://www.ncbi.nlm.nih.gov/gene/5757) · UniProt [P06454](https://www.uniprot.org/uniprotkb/P06454) · Ensembl [ENSG00000187514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187514)

## Data

Gene col 11917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11917); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11917]; `tensor/DDL_lfc|DDL_z.npy` [11917]; `embed/gene_vectors.npy` [11917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11917 or target_col == 11917). Every well: [[PTMA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTMA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
