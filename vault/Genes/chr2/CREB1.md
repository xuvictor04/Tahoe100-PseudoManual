---
symbol: "CREB1"
type: "gene"
col: 3976
ensembl_id: "ENSG00000118260"
name: "cAMP responsive element binding protein 1"
location: "2q33.3"
module: 88
arm: "+"
pooled_cpm: 114.24
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# CREB1

*cAMP responsive element binding protein 1* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +11.7, q 7e-29, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.611× (z -9.8, q 7e-20, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.646× (z -8.7, q 6e-16, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APLF]] (+0.60, fdr 1e-05), [[LRCH3]] (+0.59, fdr 1e-05), [[SLC9A8]] (+0.58, fdr 1e-05); moves opposite to [[SHQ1]] (-0.61, fdr 1e-05), [[FTO]] (-0.58, fdr 1e-05), [[SKP2]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 088]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +11.7 | 7e-29 | 33/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-04 | 25/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.007 | 25/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.016 | 23/48 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.096 | 18/47 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.2 | 0.096 | 14/48 (A-172, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.096 | 19/49 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.17× | +3.1 | 0.12 | 17/49 (NCI-H460, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.611×** | -9.8 | 7e-20 | 43/48 (SW480, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.618×** | -9.6 | 3e-19 | 39/49 (RKO, LS 180, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.646×** | -8.7 | 6e-16 | 37/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.653×** | -8.1 | 6e-14 | 35/44 (NCI-H1573, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.594×** | -8.1 | 7e-14 | 41/48 (RKO, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.684×** | -7.6 | 4e-12 | 39/48 (RKO, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.769×** | -7.4 | 1e-11 | 34/49 (NCI-H1792, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.672×** | -7.3 | 2e-11 | 35/45 (SK-MEL-2, SW480, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -5.5 | 3e-06 | 32/48 (NCI-H23, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.776×** | -4.8 | 7e-05 | 31/47 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.790×** | -4.7 | 1e-04 | 25/48 (SW48, SW480, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.649×** | -4.5 | 3e-04 | 27/47 (NCI-H23, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -4.3 | 7e-04 | 20/48 (RKO, CHP-212, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.798×** | -4.2 | 9e-04 | 22/48 (PANC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.821×** | -3.9 | 0.003 | 24/48 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.841× | -3.3 | 0.031 | 18/49 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.734×** | -3.2 | 0.036 | 21/48 (C32, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.797×** | -3.2 | 0.036 | 18/49 (PANC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 187 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.399× (z -10.0) |
| [[PANC-1 (line)]] | alt | 82.4 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +16.2) | [[Ixazomib citrate (drug)]] 5 µM 0.375× (z -12.7) |
| [[SW480 (line)]] | alt | 103 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A-172 (line)]] | wt | 116 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 93.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.0) | — |
| [[LoVo (line)]] | wt | 102 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[LS 180 (line)]] | wt | 126 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[MIA PaCa-2 (line)]] | alt | 82.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 96.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 73.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -11.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[AsPC-1 (line)]] | alt | 172 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.367× (z -10.9) |
| [[C32 (line)]] | wt | 94.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HEC-1-A (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.0) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HOP62 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.473× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[Hs 766T (line)]] | wt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 102 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H1573 (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.477× (z -9.4) |
| [[SW1417 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW48 (line)]] | wt | 95.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.240× (z -12.0) |
| [[AN3 CA (line)]] | alt | 96.5 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.241× (z -8.6) |
| [[BT-474 (line)]] | alt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 93.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 98.6 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.351× (z -10.5) |
| [[HT-29 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[KATO III (line)]] | alt | 90.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -14.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H460 (line)]] | wt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.477× (z -8.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 87.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SNU-1 (line)]] | wt | 82.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -8.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW 900 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[C-33 A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLF]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LRCH3]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SLC9A8]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ZBED5]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ST7L]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[HIVEP1]] | +0.57 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[FNTA]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SOCS2]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ERCC6L2]] | +0.56 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[XIAP]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[SERPINB7]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHQ1]] | -0.61 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[FTO]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 | STRING 481 |
| [[SKP2]] | -0.57 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[ARHGEF7]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 | pathway: Activation of NMDA receptors and postsynaptic events |
| [[DFFB]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[KATNB1]] | -0.57 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CTNNBL1]] | -0.56 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[PHKA2]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[KANTR]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PACSIN2]] | -0.54 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SMG1P2]] | -0.54 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[NTAN1]] | -0.54 | -0.53 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.6, 7.2); signed map (18.1, -23.9). **Vector** length 119, 35.3% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.1 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.8 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | -0.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.5 | -9.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.4 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -3.9 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -5.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.0 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -3.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cAMP responsive element binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:207,529,737-207,605,988 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CREB1 transcription factor family |
| Reactome | 94 pathways, smallest: MECP2 regulates transcription factors; MECP2 regulates transcription of neuronal ligands; CREB phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P16220](https://www.uniprot.org/uniprotkb/P16220) (Cyclic AMP-responsive element-binding protein 1):

> Phosphorylation-dependent transcription factor that stimulates transcription upon binding to the DNA cAMP response element (CRE), a sequence present in many viral and cellular promoters (By similarity). Transcription activation is enhanced by the TORC coactivators which act independently of Ser-119 phosphorylation. Involved in different cellular processes including the synchronization of circadian rhythmicity and the differentiation of adipose cells (By similarity). Regulates the expression of …

**Summary**, from NCBI Gene [1385](https://www.ncbi.nlm.nih.gov/gene/1385):

> This gene encodes a transcription factor that is a member of the leucine zipper family of DNA binding proteins. This protein binds as a homodimer to the cAMP-responsive element, an octameric palindrome. The protein is phosphorylated by several protein kinases, and induces transcription of genes in response to hormonal stimulation of the cAMP pathway. Alternate splicing of this gene results in several transcript variants encoding different isoforms. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:2345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2345) · Entrez [1385](https://www.ncbi.nlm.nih.gov/gene/1385) · UniProt [P16220](https://www.uniprot.org/uniprotkb/P16220) · Ensembl [ENSG00000118260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118260)

## Data

Gene col 3976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3976); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3976]; `tensor/DDL_lfc|DDL_z.npy` [3976]; `embed/gene_vectors.npy` [3976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3976 or target_col == 3976). Every well: [[CREB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
