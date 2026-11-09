---
symbol: "GGCT"
type: "gene"
col: 120
ensembl_id: "ENSG00000006625"
name: "gamma-glutamylcyclotransferase"
location: "7p14.3"
module: 6
arm: "+"
pooled_cpm: 27.83
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# GGCT

*gamma-glutamylcyclotransferase* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.30× (z +12.9, q 2e-35, up in 42 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.53× (z +4.4, q 6e-04, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.643× (z -6.5, q 5e-08, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (LoVo 0.252×, RKO 0.230×, MIA PaCa-2 0.238×, NCI-H23 0.237×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RKO 0.163×, MIA PaCa-2 0.199×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.336×; ⚠ cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.356×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSCC1]] (+0.71, fdr 7e-06), [[PRIM1]] (+0.69, fdr 7e-06), [[POLA1]] (+0.67, fdr 7e-06); moves opposite to [[TMEM202-AS1]] (-0.67, fdr 3e-05), [[C11orf71]] (-0.64, fdr 4e-05), [[ZBED5]] (-0.64, fdr 4e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 13 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **4.30×** | +12.9 | 2e-35 | 42/42 (HT-29, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.38×** | +12.1 | 2e-31 | 33/35 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.62×** | +9.2 | 6e-18 | 34/40 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.40×** | +9.1 | 2e-17 | 44/48 (H4, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.32×** | +8.7 | 4e-16 | 44/48 (KATO III, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.30×** | +8.6 | 7e-16 | 42/47 (KATO III, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.66×** | +5.0 | 4e-05 | 30/44 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.58×** | +4.7 | 1e-04 | 35/48 (H4, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.57×** | +4.6 | 2e-04 | 28/45 (Hs 766T, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.56×** | +4.6 | 3e-04 | 30/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.4 | 6e-04 | 29/47 (C32, SK-MEL-2, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | **1.48×** | +3.9 | 0.004 | 25/46 (C32, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +3.6 | 0.012 | 15/48 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.26×** | +3.3 | 0.034 | 20/48 (HT-29, LoVo, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.25×** | +3.3 | 0.035 | 21/48 (HT-29, SW480, …) | rises with dose | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.066 | 16/46 (A498, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 120.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (LoVo 0.252×, RKO 0.230×, MIA PaCa-2 0.238×, NCI-H23 0.237×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RKO 0.163×, MIA PaCa-2 0.199×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.336×; ⚠ cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.356×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.643×** | -6.5 | 5e-08 | 28/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.724× | -3.3 | 0.17 | 20/48 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.702× | -3.3 | 0.17 | 17/48 (HOP62, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.556× | -3.2 | 0.17 | 22/47 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.728× | -3.2 | 0.17 | 22/47 (AN3 CA, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.803× | -3.1 | 0.17 | 23/48 (HOP62, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.34× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -13.0) |
| [[HT-29 (line)]] | alt | 47.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.7) |
| [[KATO III (line)]] | alt | 46.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.41× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 28.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.7) |
| [[RKO (line)]] | wt | 31.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.0) |
| [[LoVo (line)]] | wt | 32.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.4) |
| [[LS 180 (line)]] | wt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[PANC-1 (line)]] | alt | 36.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW1417 (line)]] | alt | 35.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.9) |
| [[SW480 (line)]] | alt | 47.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.5) |
| [[A-427 (line)]] | wt | 29.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.356× (z -9.7) |
| [[A498 (line)]] | wt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.58× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.109× (z -8.8) |
| [[HS-578T (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[J82 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.57 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.3) |
| [[A-172 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSCC1]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PRIM1]] | +0.69 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[POLA1]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MSH2]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[HAUS1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CDCA7L]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[RFC4]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[NPM3]] | +0.66 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[L2HGDH]] | +0.65 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PPAT]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FANCB]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.64 | +0.59 / +0.49 | both halves | 1e-05 | pathway: Biological oxidations |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | -0.67 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[C11orf71]] | -0.64 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZBED5]] | -0.64 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[LRRC37A3]] | -0.63 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[ZNF764]] | -0.63 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[BOLA1]] | -0.63 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CCDC17]] | -0.63 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ATE1OSP]] | -0.63 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[HHLA3]] | -0.62 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[FAM200A]] | -0.62 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[WBP4]] | -0.62 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[LINC02951]] | -0.62 | -0.45 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises GGCT's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without PODXL2 | 0.001 | ⚠ within organs, on part of the lines |
| [[CDCA7L]] | B | CDCA7L activity raises GGCT's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without CDCA7L | 0.045 | ⚠ within organs, on part of the lines |
| [[CDCA7]] | B | CDCA7 activity raises GGCT's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without CDCA7 | 0.069 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises GGCT's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without DSCC1 | 0.098 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.1, -44.5); signed map (-35.6, -41.3). **Vector** length 86.9, 23.6% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Leading Strand Synthesis* (reactome, mean cos +0.51 to 12); *Polymerase switching* (reactome, mean cos +0.51 to 12); *Polymerase switching on the C-strand of the telomere* (reactome, mean cos +0.51 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.0 | +8.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.3 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.9 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.3 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.4 | +1.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.4 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | gamma-glutamylcyclotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:30,496,621-30,504,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3077, CRF21, Ggc; previously C7orf24, GCTG |
| Gene groups (HGNC) | Carbon-nitrogen lyases |
| Reactome | 4 pathways, smallest: Glutathione synthesis and recycling; Glutathione conjugation; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [O75223](https://www.uniprot.org/uniprotkb/O75223) (Gamma-glutamylcyclotransferase):

> Catalyzes the formation of 5-oxoproline from gamma-glutamyl dipeptides and may play a significant role in glutathione homeostasis. Induces release of cytochrome c from mitochondria with resultant induction of apoptosis.

**Summary**, from NCBI Gene [79017](https://www.ncbi.nlm.nih.gov/gene/79017):

> The protein encoded by this gene catalyzes the formation of 5-oxoproline from gamma-glutamyl dipeptides, the penultimate step in glutathione catabolism, and may play a critical role in glutathione homeostasis. The encoded protein may also play a role in cell proliferation, and the expression of this gene is a potential marker for cancer. Pseudogenes of this gene are located on the long arm of chromosome 5 and the short arm of chromosomes 2 and 20. Alternatively spliced transcript variants …

**Accessions** — [HGNC:21705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21705) · Entrez [79017](https://www.ncbi.nlm.nih.gov/gene/79017) · UniProt [O75223](https://www.uniprot.org/uniprotkb/O75223) · Ensembl [ENSG00000006625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006625)

## Data

Gene col 120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 120); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 120]; `tensor/DDL_lfc|DDL_z.npy` [120]; `embed/gene_vectors.npy` [120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 120 or target_col == 120). Every well: [[GGCT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGCT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
