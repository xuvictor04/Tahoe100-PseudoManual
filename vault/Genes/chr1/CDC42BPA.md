---
symbol: "CDC42BPA"
type: "gene"
col: 6802
ensembl_id: "ENSG00000143776"
name: "CDC42 binding protein kinase alpha"
location: "1q42.13"
module: 5
arm: "+"
pooled_cpm: 333.42
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CDC42BPA

*CDC42 binding protein kinase alpha* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.24× (z +4.1, q 0.019, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Bortezomib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.15×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (C32 2.60×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 1.58×; ⚠ cell-cycle shift, explains ~31% of this change); [[Peretinoin (drug)]] 5 µM in 1 line (NCI-H1573 2.25×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.371× (z -18.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUTM2B-AS1]] (+0.63, fdr 1e-05), [[GCLM]] (+0.62, fdr 1e-05), [[EIF4G3]] (+0.61, fdr 1e-05); moves opposite to [[SRP54-AS1]] (-0.59, fdr 1e-05), [[ANKRD37]] (-0.58, fdr 1e-05), [[TBC1D22A-DT]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6802.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Bortezomib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.15×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (C32 2.60×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 1.58×; ⚠ cell-cycle shift, explains ~31% of this change); [[Peretinoin (drug)]] 5 µM in 1 line (NCI-H1573 2.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.24×** | +4.1 | 0.019 | 29/48 (C-33 A, BT-474, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.20 | 11/48 (C-33 A, RKO, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.3 | 0.20 | 20/48 (C-33 A, CFPAC-1, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.20 | 21/48 (C-33 A, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.371×** | -18.9 | 0e+00 | 47/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.373×** | -18.8 | 0e+00 | 48/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.439×** | -15.7 | 0e+00 | 48/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -14.2 | 2e-43 | 49/49 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.631×** | -12.4 | 3e-33 | 36/48 (LoVo, NCI-H1792, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -8.4 | 4e-15 | 41/47 (SW 900, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.680×** | -7.1 | 1e-10 | 37/50 (SW48, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.708×** | -6.6 | 3e-09 | 43/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.700×** | -6.5 | 4e-09 | 37/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.719×** | -6.3 | 2e-08 | 42/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.772×** | -4.9 | 4e-05 | 27/48 (PANC-1, SW48, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.785×** | -4.6 | 2e-04 | 28/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.793×** | -4.1 | 0.002 | 27/45 (A-427, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.683×** | -3.8 | 0.006 | 23/38 (Panc 03.27, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.782×** | -3.8 | 0.006 | 29/48 (SW480, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.834× | -3.2 | 0.040 | 21/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.793×** | -3.1 | 0.045 | 25/48 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.891× | -3.1 | 0.050 | 1/49 (NCI-H661) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.734×** | -3.1 | 0.051 | 22/48 (HCT15, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.846× | -2.9 | 0.073 | 20/47 (RKO, CHP-212, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.749×** | -2.9 | 0.086 | 21/48 (MIA PaCa-2, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 521 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -13.7) |
| [[KATO III (line)]] | alt | 382 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -27.1) |
| [[PANC-1 (line)]] | alt | 288 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -15.9) |
| [[LoVo (line)]] | wt | 592 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -24.0) |
| [[SNU-1 (line)]] | wt | 432 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.365× (z -13.8) |
| [[SW48 (line)]] | wt | 387 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -17.5) |
| [[HT-29 (line)]] | alt | 338 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -26.2) |
| [[LS 180 (line)]] | wt | 555 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -27.6) |
| [[NCI-H1573 (line)]] | alt | 259 | 1 | 6 (5 ⚠) | [[Peretinoin (drug)]] 5 µM 2.25× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -20.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.8) |
| [[A-172 (line)]] | wt | 466 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -18.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -16.7) |
| [[HEC-1-A (line)]] | alt | 352 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -20.9) |
| [[HOP62 (line)]] | alt | 285 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -19.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.338× (z -14.6) |
| [[J82 (line)]] | alt | 293 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 353 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 299 | 1 (1 ⚠) | 5 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.15× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.335× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 241 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -21.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.282× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 265 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 277 | 0 | 6 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0594× (z -19.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.249× (z -18.5) |
| [[SW 900 (line)]] | alt | 359 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -14.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.377× (z -13.7) |
| [[A-427 (line)]] | wt | 303 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -15.3) |
| [[BT-474 (line)]] | alt | 295 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -16.2) |
| [[COLO 205 (line)]] | alt | 451 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -16.2) |
| [[HCT15 (line)]] | alt | 455 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 291 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -11.5) |
| [[SNU-423 (line)]] | alt | 198 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.403× (z -12.1) |
| [[A549 (line)]] | wt | 279 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 292 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -16.2) |
| [[Hs 766T (line)]] | wt | 350 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -16.2) |
| [[RKO (line)]] | wt | 390 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -17.4) |
| [[RPMI-7951 (line)]] | alt | 260 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.434× (z -10.3) |
| [[SW1417 (line)]] | alt | 558 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -18.4) |
| [[SW480 (line)]] | alt | 360 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -27.3) |
| [[A498 (line)]] | wt | 254 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.393× (z -10.2) |
| [[C32 (line)]] | wt | 195 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.60× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 201 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -12.0) |
| [[HS-578T (line)]] | alt | 185 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 262 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 244 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -13.2) |
| [[SHP-77 (line)]] | alt | 276 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 302 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.531× (z -10.0) |
| [[C-33 A (line)]] | alt | 322 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.511× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -15.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 356 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -9.5) |
| [[NCI-H661 (line)]] | alt | 312 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -8.6) |
| [[AN3 CA (line)]] | alt | 261 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 260 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 217 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTM2B-AS1]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GCLM]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[EIF4G3]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SLC35F6]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[IDE]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[WWC3]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ROCK2]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ME1]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ATE1]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PTPN11]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[SLC7A11]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[HLCS]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.59 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TBC1D22A-DT]] | -0.57 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TYK2]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ESCO1]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[APAF1]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[RAB3A]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CRLS1]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[AFMID]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NARF]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MED26]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[KLHL28]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.359). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (5.2, -21.8); signed map (5.7, -49.9). **Vector** length 116, 43.6% of its response variance represented; |z| ≥ 3 in 1,299 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.4 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.4 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.0 | -0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +6.5 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.0 | +3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +1.7 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.5 | -8.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 binding protein kinase alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:226,989,865-227,318,492 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRCKA, PK428, FLJ23347, KIAA0451, MRCKalpha |
| Gene groups (HGNC) | CDC42 binding protein kinase family |
| Hallmark sets | UV_RESPONSE_DN, MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: RHOJ GTPase cycle; RHOQ GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VT25](https://www.uniprot.org/uniprotkb/Q5VT25) (Serine/threonine-protein kinase MRCK alpha):

> Serine/threonine-protein kinase which is an important downstream effector of CDC42 and plays a role in the regulation of cytoskeleton reorganization and cell migration. Regulates actin cytoskeletal reorganization via phosphorylation of PPP1R12C and MYL9/MLC2. In concert with MYO18A and LURAP1, is involved in modulating lamellar actomyosin retrograde flow that is crucial to cell protrusion and migration. Phosphorylates: PPP1R12A, LIMK1 and LIMK2. May play a role in TFRC-mediated iron uptake. In …

**Summary**, from NCBI Gene [8476](https://www.ncbi.nlm.nih.gov/gene/8476):

> The protein encoded by this gene is a member of the serine/threonine protein kinase family. This kinase contains multiple functional domains. Its kinase domain is highly similar to that of the myotonic dystrophy protein kinase (DMPK). This kinase also contains a Rac interactive binding (CRIB) domain, and has been shown to bind CDC42. It may function as a CDC42 downstream effector mediating CDC42 induced peripheral actin formation, and promoting cytoskeletal reorganization. Multiple …

**Accessions** — [HGNC:1737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1737) · Entrez [8476](https://www.ncbi.nlm.nih.gov/gene/8476) · UniProt [Q5VT25](https://www.uniprot.org/uniprotkb/Q5VT25) · Ensembl [ENSG00000143776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143776)

## Data

Gene col 6802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6802); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6802]; `tensor/DDL_lfc|DDL_z.npy` [6802]; `embed/gene_vectors.npy` [6802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6802 or target_col == 6802). Every well: [[CDC42BPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42BPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
