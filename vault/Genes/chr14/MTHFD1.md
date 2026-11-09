---
symbol: "MTHFD1"
type: "gene"
col: 2013
ensembl_id: "ENSG00000100714"
name: "methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1"
location: "14q23.3"
module: 6
arm: "+"
pooled_cpm: 34.38
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MTHFD1

*methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.48× (z +20.4, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.54× (z +5.8, q 5e-07, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.808× (z -4.2, q 0.014, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.239×, MIA PaCa-2 0.407×, NCI-H23 0.454×, SW480 0.460×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H23 0.419×, RKO 0.355×, MIA PaCa-2 0.387×, KATO III 0.375×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 2 lines (SW48 0.183×, LOX-IMVI 0.263×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKDC]] (+0.86, fdr 7e-06), [[TFDP1]] (+0.80, fdr 7e-06), [[MCM3]] (+0.79, fdr 7e-06); moves opposite to [[TERF2IP]] (-0.73, fdr 7e-06), [[GABARAPL2]] (-0.69, fdr 7e-06), [[SELENOK]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDCA7L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.48×** | +20.4 | 0e+00 | 44/45 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.13×** | +18.6 | 0e+00 | 38/40 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.91×** | +13.4 | 6e-39 | 40/43 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.83×** | +7.9 | 4e-13 | 41/47 (C32, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +7.6 | 3e-12 | 40/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.8 | 5e-07 | 29/48 (NCI-H1792, A549, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.6 | 1e-06 | 3/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +5.5 | 2e-06 | 28/48 (NCI-H1792, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +5.0 | 4e-05 | 27/48 (NCI-H1792, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +4.3 | 9e-04 | 22/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +4.2 | 0.001 | 23/48 (NCI-H1792, A549, …) | two highest doses | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **1.75×** | +3.9 | 0.004 | 20/46 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.016 | 15/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.021 | 15/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 1.19× | +3.3 | 0.032 | 16/48 (NCI-H460, A-427, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.60×** | +3.3 | 0.032 | 12/48 (Hs 766T, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.076 | 14/47 (NCI-H23, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2013.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.239×, MIA PaCa-2 0.407×, NCI-H23 0.454×, SW480 0.460×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H23 0.419×, RKO 0.355×, MIA PaCa-2 0.387×, KATO III 0.375×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 2 lines (SW48 0.183×, LOX-IMVI 0.263×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.808×** | -4.2 | 0.014 | 25/48 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -4.0 | 0.017 | 24/47 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.797× | -3.2 | 0.29 | 19/46 (CHP-212, SW 900, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.856× | -3.1 | 0.30 | 16/48 (KATO III, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 51.2 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.9) |
| [[KATO III (line)]] | alt | 37.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.41× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.5) |
| [[LoVo (line)]] | wt | 25.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.41× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 83.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.3) |
| [[A549 (line)]] | wt | 29.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.41× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 18.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 18.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.73× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HS-578T (line)]] | alt | 17.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.263× (z -8.8) |
| [[PANC-1 (line)]] | alt | 33.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 50.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.4) |
| [[A-427 (line)]] | wt | 50.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.7) |
| [[A498 (line)]] | wt | 35.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HCT15 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.36× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 29.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 14.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.86× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 44.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 34.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 63.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 32.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SHP-77 (line)]] | alt | 53.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-423 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.74× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 16.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.29× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 78.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.183× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.26× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.51× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.07× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 41.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.8) | — |
| [[RKO (line)]] | wt | 54.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.80 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[MCM3]] | +0.79 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.78 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[RANBP1]] | +0.76 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[IPO5]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[ATIC]] | +0.75 | +0.70 / +0.80 | both halves | 7e-06 | STRING 998 |
| [[NUP155]] | +0.75 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[PRPS1]] | +0.75 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[POLA1]] | +0.74 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[ICMT]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.73 | -0.68 / -0.72 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.69 | -0.65 / -0.80 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.69 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.68 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.67 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.67 | -0.57 / -0.76 | both halves | 1e-05 |  |
| [[NOSIP]] | -0.67 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[ADPRM]] | -0.67 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[NKAP]] | -0.67 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[LINC00685]] | -0.66 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.66 | -0.62 / -0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | -0.66 | -0.67 / -0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SYF2]] | -0.65 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[BSDC1]] | -0.65 | -0.52 / -0.71 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7L]] | B | CDCA7L activity raises MTHFD1's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.30× lower at baseline in the lines without CDCA7L | 0.050 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-29.8, -33.0); signed map (-19.9, -44.7). **Vector** length 127, 38.1% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.51 to 65); *DNA strand elongation* (reactome, mean cos +0.53 to 28); *E2F G1/S* (control, mean cos +0.53 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +6.2 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.7 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.7 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.6 | +13.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +5.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.6 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.7 | -2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.1 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,388,031-64,463,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MTHFC, MTHFD |
| Gene groups (HGNC) | Minor histocompatibility antigens; MTHFD family; Methylenetetrahydrofolate dehydrogenases; Formyltetrahydrofolate synthetases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P11586](https://www.uniprot.org/uniprotkb/P11586) (C-1-tetrahydrofolate synthase, cytoplasmic):

> Trifunctional enzyme that catalyzes the interconversion of three forms of one-carbon-substituted tetrahydrofolate: (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate, 5,10-methenyltetrahydrofolate and (6S)-10-formyltetrahydrofolate. These derivatives of tetrahydrofolate are differentially required in nucleotide and amino acid biosynthesis, (6S)-10-formyltetrahydrofolate being required for purine biosynthesis while (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate is used for serine and methionine …

**Summary**, from NCBI Gene [4522](https://www.ncbi.nlm.nih.gov/gene/4522):

> This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, and de novo purine syntheses. The trifunctional enzymatic activities are conferred by two major …

**Accessions** — [HGNC:7432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7432) · Entrez [4522](https://www.ncbi.nlm.nih.gov/gene/4522) · UniProt [P11586](https://www.uniprot.org/uniprotkb/P11586) · Ensembl [ENSG00000100714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100714)

## Data

Gene col 2013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2013); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2013]; `tensor/DDL_lfc|DDL_z.npy` [2013]; `embed/gene_vectors.npy` [2013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2013 or target_col == 2013). Every well: [[MTHFD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTHFD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
