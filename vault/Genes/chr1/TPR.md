---
symbol: "TPR"
type: "gene"
col: 515
ensembl_id: "ENSG00000047410"
name: "translocated promoter region, nuclear basket protein"
location: "1q31.1"
module: 17
arm: "+"
pooled_cpm: 365.7
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TPR

*translocated promoter region, nuclear basket protein* — 1q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +11.7, q 1e-28, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~65% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (NCI-H1573 2.32×, HEC-1-A 1.93×, RKO 2.23×, PANC-1 1.76×, …; ⚠ cell-cycle shift, explains ~65% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 2.06×, NCI-H1573 1.96×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HEC-1-A 1.89×, NCI-H1573 2.07×; ⚠ cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.674× (z -9.8, q 5e-20, down in 42 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.776× (z -8.0, q 5e-13, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (SW 900 0.490×, A549 0.554×, CHP-212 0.475×, AsPC-1 0.650×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.338×, C32 0.446×, SW 900 0.431×, CHP-212 0.316×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 5 lines (KATO III 0.430×, SW480 0.475×, SW 900 0.422×, HT-29 0.491×, …; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (SW 900 0.449×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMC3]] (+0.71, fdr 7e-06), [[TCAF1]] (+0.66, fdr 1e-05), [[CDC5L]] (+0.65, fdr 7e-06); moves opposite to [[CTTN]] (-0.55, fdr 3e-05), [[CERS2]] (-0.55, fdr 4e-05), [[PRDM15]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RNF5]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 515.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (NCI-H1573 2.32×, HEC-1-A 1.93×, RKO 2.23×, PANC-1 1.76×, …; ⚠ cell-cycle shift, explains ~65% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 2.06×, NCI-H1573 1.96×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HEC-1-A 1.89×, NCI-H1573 2.07×; ⚠ cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.46×** | +11.7 | 1e-28 | 42/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.32×** | +7.3 | 1e-10 | 31/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.32×** | +6.9 | 1e-09 | 38/48 (NCI-H460, HEC-1-A, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.31×** | +6.7 | 4e-09 | 32/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.48×** | +5.3 | 1e-05 | 38/47 (LoVo, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.22×** | +5.2 | 2e-05 | 25/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.4 | 0.050 | 19/48 (LS 180, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.25× | +3.0 | 0.16 | 24/49 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 515.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (SW 900 0.490×, A549 0.554×, CHP-212 0.475×, AsPC-1 0.650×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.338×, C32 0.446×, SW 900 0.431×, CHP-212 0.316×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 5 lines (KATO III 0.430×, SW480 0.475×, SW 900 0.422×, HT-29 0.491×, …; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (SW 900 0.449×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -9.8 | 5e-20 | 42/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -8.0 | 5e-13 | 33/49 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.857× | -3.8 | 0.024 | 18/44 (NCI-H1573, C32, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 0.873× | -3.3 | 0.11 | 11/48 (SW 900, HS-578T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.880× | -3.3 | 0.11 | 21/48 (SW 900, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.883× | -3.2 | 0.13 | 12/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -3.1 | 0.13 | 16/48 (HS-578T, SW 900, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -3.1 | 0.13 | 0/50 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 405 | 7 (7 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.9) ⚠ cell-cycle shift, explains ~65% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -10.5) |
| [[SW 900 (line)]] | alt | 786 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -14.6) |
| [[C32 (line)]] | wt | 837 | 3 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.0) ⚠ cell-cycle shift, explains ~65% of this change | [[Dinaciclib (drug)]] 5 µM 0.446× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 373 | 4 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +16.5) ⚠ cell-cycle shift, explains ~65% of this change | [[Dinaciclib (drug)]] 5 µM 0.522× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 263 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.4) ⚠ cell-cycle shift, explains ~65% of this change | [[Dinaciclib (drug)]] 5 µM 0.338× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 311 | 1 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.56× (z +8.7) ⚠ cell-cycle shift, explains ~73% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -10.6) |
| [[LoVo (line)]] | wt | 311 | 4 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.84× (z +11.1) ⚠ toxic; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 348 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.9) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[RKO (line)]] | wt | 363 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.1) ⚠ cell-cycle shift, explains ~65% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -8.5) |
| [[HS-578T (line)]] | alt | 298 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 289 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.8) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[A549 (line)]] | wt | 409 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.0) ⚠ cell-cycle shift, explains ~65% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -12.9) |
| [[CHP-212 (line)]] | wt | 577 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.2) |
| [[HCT15 (line)]] | alt | 423 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.519× (z -10.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -8.9) |
| [[KATO III (line)]] | alt | 245 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.2) ⚠ cell-cycle shift, explains ~65% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -15.1) ⚠ toxic |
| [[LS 180 (line)]] | wt | 326 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 360 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.1) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[SHP-77 (line)]] | alt | 388 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -10.3) |
| [[SW1417 (line)]] | alt | 264 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.7) ⚠ cell-cycle shift, explains ~65% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.643× (z -8.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 415 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.615× (z -10.1) ⚠ toxic |
| [[A498 (line)]] | wt | 394 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.3) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[BT-474 (line)]] | alt | 249 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.6) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[HT-29 (line)]] | alt | 321 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.491× (z -12.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 455 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.9) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H1792 (line)]] | alt | 355 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.5) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H2347 (line)]] | alt | 447 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +12.6) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[Panc 03.27 (line)]] | alt | 344 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.587× (z -9.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 340 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 321 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.568× (z -9.6) ⚠ toxic |
| [[SW48 (line)]] | wt | 407 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.554× (z -9.0) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 328 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.475× (z -14.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 473 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 407 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 436 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 292 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 239 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 349 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 307 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 372 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 612 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 319 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC3]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[TCAF1]] | +0.66 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CDC5L]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 573 |
| [[GPATCH11]] | +0.63 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CETN3]] | +0.62 | +0.56 / +0.69 | both halves | 1e-05 | STRING 945 |
| [[IK]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[HPF1]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SNAPIN]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[RFC1]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ROCK1]] | +0.59 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[PHF3]] | +0.59 | +0.62 / +0.61 | both halves | 7e-06 | STRING 495 |
| [[AKAP9]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTTN]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CERS2]] | -0.55 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PRDM15]] | -0.55 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SENP3]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 | STRING 439 |
| [[KCTD15]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[LY6G5B]] | -0.52 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[TMEM11-DT]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CAPN15]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[SAP30L-AS1]] | -0.51 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[CTC-338M12.4]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[POU6F1]] | -0.50 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[TRNT1]] | -0.50 | -0.38 / -0.39 | both halves | 6e-05 | pathway: tRNA processing |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF5]] | C | RNF5's natural level weakens TPR's drug response | RNF5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.32; direction not clear | 0.023 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.1, 1.7); signed map (-19.0, -10.5). **Vector** length 137, 44.8% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +7.5 | +11.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +5.5 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.1 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.9 | +7.3 |
|  | [[AZD-7648 (drug)]] 0.5 µM |  | +3.3 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Saquinavir (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.9 |
|  | [[Thymol (drug)]] 5 µM |  | +2.9 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.8 | -9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.4 | -2.6 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -3.3 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -2.7 | -1.7 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | translocated promoter region, nuclear basket protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.1 — chr1:186,311,652-186,375,693 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 72 pathways, smallest: IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus; IPs transport between nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P12270](https://www.uniprot.org/uniprotkb/P12270) (Nucleoprotein TPR):

> Component of the nuclear pore complex (NPC), a complex required for the trafficking across the nuclear envelope. Functions as a scaffolding element in the nuclear phase of the NPC essential for normal nucleocytoplasmic transport of proteins and mRNAs, plays a role in the establishment of nuclear-peripheral chromatin compartmentalization in interphase, and in the mitotic spindle checkpoint signaling during mitosis. Involved in the quality control and retention of unspliced mRNAs in the nucleus; …

**Summary**, from NCBI Gene [7175](https://www.ncbi.nlm.nih.gov/gene/7175):

> This gene encodes a large coiled-coil protein that forms intranuclear filaments attached to the inner surface of nuclear pore complexes (NPCs). The protein directly interacts with several components of the NPC. It is required for the nuclear export of mRNAs and some proteins. Oncogenic fusions of the 5' end of this gene with several different kinase genes occur in some neoplasias. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12017) · Entrez [7175](https://www.ncbi.nlm.nih.gov/gene/7175) · UniProt [P12270](https://www.uniprot.org/uniprotkb/P12270) · Ensembl [ENSG00000047410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047410)

## Data

Gene col 515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 515); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 515]; `tensor/DDL_lfc|DDL_z.npy` [515]; `embed/gene_vectors.npy` [515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 515 or target_col == 515). Every well: [[TPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
