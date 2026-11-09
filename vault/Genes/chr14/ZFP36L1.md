---
symbol: "ZFP36L1"
type: "gene"
col: 11709
ensembl_id: "ENSG00000185650"
name: "ZFP36 like 1 zinc finger CCCH-type"
location: "14q24.1"
module: 113
arm: "+"
pooled_cpm: 267.54
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ZFP36L1

*ZFP36 like 1 zinc finger CCCH-type* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.77× (z +6.5, q 6e-08, up in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.44× (z +4.3, q 0.003, up in 27 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 4.40×, HS-578T 2.71×, CFPAC-1 2.37×; ⚠ cell-cycle shift, would explain all of this change); [[Betamethasone dipropionate (drug)]] 0.5 µM in 2 lines (NCI-H1573 5.73×, Hs 766T 4.03×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 6.32×); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H1573 5.88×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.314× (z -13.6, q 3e-39, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP1]] (+0.73, fdr 7e-06), [[IRX3]] (+0.69, fdr 7e-06), [[CEBPB]] (+0.68, fdr 7e-06); moves opposite to [[NOMO2]] (-0.56, fdr 5e-05), [[AGO1]] (-0.50, fdr 3e-05), [[COPS7B]] (-0.50, fdr 3e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SAA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 4.40×, HS-578T 2.71×, CFPAC-1 2.37×; ⚠ cell-cycle shift, would explain all of this change); [[Betamethasone dipropionate (drug)]] 0.5 µM in 2 lines (NCI-H1573 5.73×, Hs 766T 4.03×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 6.32×); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H1573 5.88×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.77×** | +6.5 | 6e-08 | 33/46 (A549, CFPAC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +4.5 | 0.002 | 26/46 (C32, HS-578T, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.44×** | +4.3 | 0.003 | 25/46 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.003 | 27/46 (MIA PaCa-2, SW1417, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.2 | 0.003 | 28/45 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +3.5 | 0.046 | 28/46 (A549, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11709.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.314×** | -13.6 | 3e-39 | 44/46 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.338×** | -12.7 | 1e-34 | 42/46 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.487×** | -8.4 | 7e-15 | 37/46 (A549, C-33 A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.611×** | -5.6 | 4e-06 | 31/46 (A498, C-33 A, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.682×** | -4.5 | 8e-04 | 40/46 (AsPC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.514×** | -4.1 | 0.004 | 33/47 (A549, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.712×** | -4.0 | 0.006 | 25/46 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.704×** | -3.9 | 0.006 | 27/48 (A498, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.735×** | -3.6 | 0.020 | 29/46 (SW 900, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.827× | -3.1 | 0.10 | 22/46 (C-33 A, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 102 | 21 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 6.32× (z +15.1) | — |
| [[Hs 766T (line)]] | wt | 215 | 17 (2 ⚠) | 3 | [[Betamethasone dipropionate (drug)]] 0.5 µM 4.03× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.208× (z -13.7) |
| [[HOP62 (line)]] | alt | 101 | 13 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +11.7) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 5 µM 4.37× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 498 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -18.7) |
| [[COLO 205 (line)]] | alt | 313 | 1 (1 ⚠) | 8 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 4.03× (z +11.2) ⚠ cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.184× (z -14.3) |
| [[A498 (line)]] | wt | 667 | 1 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.53× (z +9.0) ⚠ cell-cycle shift, explains ~22% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -17.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.201× (z -15.8) |
| [[CFPAC-1 (line)]] | alt | 514 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.391× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 519 | 4 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.68× (z +10.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.54× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.2) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H460 (line)]] | wt | 71.1 | 6 (1 ⚠) | 0 | [[Betamethasone dipropionate (drug)]] 5 µM 3.76× (z +10.5) | — |
| [[A549 (line)]] | wt | 339 | 2 (2 ⚠) | 3 | [[Harringtonine (drug)]] 0.5 µM 4.35× (z +14.2) ⚠ cell-cycle shift, explains ~22% of this change | [[Panobinostat (drug)]] 5 µM 0.119× (z -20.5) |
| [[H4 (line)]] | wt | 122 | 5 | 0 | [[Betamethasone dipropionate (drug)]] 5 µM 3.98× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 434 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -15.8) |
| [[HS-578T (line)]] | alt | 197 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 2.64× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.218× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 313 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +9.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.90× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.314× (z -10.6) |
| [[SNU-423 (line)]] | alt | 438 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -12.6) |
| [[SW 900 (line)]] | alt | 339 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -13.8) |
| [[SW1417 (line)]] | alt | 168 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.72× (z +9.8) | — |
| [[A-172 (line)]] | wt | 403 | 1 | 2 | [[Homoharringtonine (drug)]] 0.05 µM 3.83× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -11.7) |
| [[AN3 CA (line)]] | alt | 419 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 416 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -12.1) |
| [[C32 (line)]] | wt | 75.8 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +14.2) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.279× (z -8.5) |
| [[CHP-212 (line)]] | wt | 252 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 285 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -14.3) |
| [[J82 (line)]] | alt | 369 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -15.0) |
| [[KATO III (line)]] | alt | 127 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.2) ⚠ cell-cycle shift, explains ~75% of this change | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -9.6) |
| [[LS 180 (line)]] | wt | 202 | 1 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 2.69× (z +9.1) ⚠ cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.211× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 165 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -9.7) |
| [[PANC-1 (line)]] | alt | 81.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -14.6) |
| [[SW480 (line)]] | alt | 273 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.29× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.23× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 244 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -10.7) |
| [[HT-29 (line)]] | alt | 133 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 252 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 323 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 632 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 337 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 351 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -9.5) |
| [[SNU-1 (line)]] | wt | 191 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 2.96× (z +8.6) ⚠ cell-cycle shift, explains ~22% of this change | [[Panobinostat (drug)]] 5 µM 0.316× (z -9.1) |
| [[A-427 (line)]] | wt | 81.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -10.8) |
| [[BT-474 (line)]] | alt | 313 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.8) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[NCI-H661 (line)]] | alt | 186 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -10.6) |
| [[SW48 (line)]] | wt | 543 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP1]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[IRX3]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[CEBPB]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[CEBPD]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PNRC1]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ZFHX3]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[MT1E]] | +0.63 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[KLF9]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[KLF6]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ZFP36L2]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 | same gene group; STRING 917 |
| [[BCL6]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MAFB]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO2]] | -0.56 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[AGO1]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[COPS7B]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SNRNP40]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[EEF1AKMT2]] | -0.48 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[RPN1]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[CHID1]] | -0.48 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[FAM20B]] | -0.48 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[FKBP9]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[BPNT2]] | -0.47 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[NSD2]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PABIR2]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAA1]] | B | SAA1 activity raises ZFP36L1's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without SAA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[TBX3]] | B | TBX3 activity lowers ZFP36L1's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 2.19× higher at baseline in the lines without TBX3 | 0.092 | ⚠ within organs, on part of the lines |
| [[HDAC6]] | B | HDAC6 activity raises ZFP36L1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.1, 13.5); signed map (15.0, 27.6). **Vector** length 125, 39.9% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.51 to 5); *metallothionein* (control, mean cos +0.51 to 5); *Response to metal ions* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.0 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +7.2 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.7 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.3 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.8 | +3.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.6 | +2.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.4 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +4.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.4 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.4 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.9 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | -2.2 | -2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ZFP36 like 1 zinc finger CCCH-type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:68,787,660-68,796,253 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Berg36, ERF1, TIS11B, cMG1; previously BRF1 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Hallmark sets | P53_PATHWAY |
| Reactome | 3 pathways, smallest: Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; Regulation of mRNA stability by proteins that bind AU-rich elements; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07352](https://www.uniprot.org/uniprotkb/Q07352) (mRNA decay activator protein ZFP36L1):

> Zinc-finger RNA-binding protein that destabilizes several cytoplasmic AU-rich element (ARE)-containing mRNA transcripts by promoting their poly(A) tail removal or deadenylation, and hence provide a mechanism for attenuating protein synthesis. Acts as a 3'-untranslated region (UTR) ARE mRNA-binding adapter protein to communicate signaling events to the mRNA decay machinery. Functions by recruiting the CCR4-NOT deadenylase complex and components of the cytoplasmic RNA decay machinery to the bound …

**Summary**, from NCBI Gene [677](https://www.ncbi.nlm.nih.gov/gene/677):

> This gene is a member of the TIS11 family of early response genes, which are induced by various agonists such as the phorbol ester TPA and the polypeptide mitogen EGF. This gene is well conserved across species and has a promoter that contains motifs seen in other early-response genes. The encoded protein contains a distinguishing putative zinc finger domain with a repeating cys-his motif. This putative nuclear transcription factor most likely functions in regulating the response to growth …

**Accessions** — [HGNC:1107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1107) · Entrez [677](https://www.ncbi.nlm.nih.gov/gene/677) · UniProt [Q07352](https://www.uniprot.org/uniprotkb/Q07352) · Ensembl [ENSG00000185650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185650)

## Data

Gene col 11709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11709); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11709]; `tensor/DDL_lfc|DDL_z.npy` [11709]; `embed/gene_vectors.npy` [11709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11709 or target_col == 11709). Every well: [[ZFP36L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP36L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
