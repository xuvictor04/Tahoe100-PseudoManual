---
symbol: "PPFIBP1"
type: "gene"
col: 3168
ensembl_id: "ENSG00000110841"
name: "PPFIB scaffold protein 1"
location: "12p11.23-p11.22"
module: 84
arm: "+"
pooled_cpm: 395.2
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 20
direction_downstream: 1
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# PPFIBP1

*PPFIB scaffold protein 1* — 12p11.23-p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.19× (z +5.7, q 7e-06, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 2.23×, SNU-1 2.28×, LS 180 1.84×); [[Tucidinostat (drug)]] 5 µM in 3 lines (SW1417 1.73×, KATO III 1.65×, MIA PaCa-2 1.56×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.61×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.473× (z -23.9, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO10]] (+0.65, fdr 7e-06), [[NMNAT2]] (+0.65, fdr 1e-05), [[WWTR1]] (+0.64, fdr 1e-05); moves opposite to [[KEAP1]] (-0.55, fdr 2e-05), [[AKAP8]] (-0.52, fdr 1e-04), [[CDH26]] (-0.51, fdr 3e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[COL15A1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[REP15]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3168.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 2.23×, SNU-1 2.28×, LS 180 1.84×); [[Tucidinostat (drug)]] 5 µM in 3 lines (SW1417 1.73×, KATO III 1.65×, MIA PaCa-2 1.56×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.61×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.7 | 7e-06 | 24/48 (SW1417, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +4.4 | 0.003 | 26/49 (SW1417, KATO III, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.29× | +3.1 | 0.43 | 20/48 (HOP62, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.473×** | -23.9 | 0e+00 | 44/49 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.563×** | -12.9 | 8e-36 | 42/48 (LoVo, SW48, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -12.2 | 4e-32 | 41/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.747×** | -9.3 | 3e-18 | 27/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.707×** | -7.5 | 7e-12 | 30/44 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.724×** | -7.3 | 4e-11 | 27/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.745×** | -6.4 | 1e-08 | 30/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.738×** | -6.3 | 2e-08 | 28/45 (SW48, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.758×** | -6.2 | 3e-08 | 31/48 (C32, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -6.1 | 5e-08 | 28/48 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.767×** | -6.0 | 1e-07 | 31/48 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.774×** | -5.7 | 4e-07 | 27/49 (SW48, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **0.794×** | -5.2 | 1e-05 | 29/48 (SW480, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.784×** | -5.1 | 1e-05 | 28/48 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.678×** | -4.6 | 2e-04 | 29/49 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.823×** | -4.4 | 4e-04 | 23/49 (A-172, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.823×** | -4.4 | 4e-04 | 25/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.827×** | -4.3 | 6e-04 | 23/49 (H4, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.833×** | -4.1 | 0.001 | 24/48 (A-172, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.841× | -3.9 | 0.002 | 21/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.838× | -3.8 | 0.003 | 23/48 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.877× | -3.6 | 0.005 | 18/48 (A-172, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.852× | -3.6 | 0.007 | 18/48 (A-172, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 577 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -22.6) |
| [[A-172 (line)]] | wt | 479 | 0 | 17 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -21.4) |
| [[C32 (line)]] | wt | 774 | 0 | 15 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -20.6) |
| [[H4 (line)]] | wt | 428 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 496 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -24.4) |
| [[SW480 (line)]] | alt | 912 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -31.6) |
| [[J82 (line)]] | alt | 259 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -19.1) |
| [[NCI-H1573 (line)]] | alt | 261 | 7 (6 ⚠) | 2 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 2.25× (z +10.2) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 2.01× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.9) |
| [[SW48 (line)]] | wt | 986 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -23.3) |
| [[Hs 766T (line)]] | wt | 382 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 541 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -17.1) |
| [[HOP62 (line)]] | alt | 751 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.9) |
| [[SNU-423 (line)]] | alt | 451 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -20.1) |
| [[LoVo (line)]] | wt | 687 | 0 | 5 | — | [[Auranofin (drug)]] 5 µM 0.258× (z -19.4) |
| [[RPMI-7951 (line)]] | alt | 392 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -18.5) |
| [[A-427 (line)]] | wt | 162 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.0) | — |
| [[AsPC-1 (line)]] | alt | 407 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -18.3) |
| [[HS-578T (line)]] | alt | 464 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -18.6) |
| [[hTERT-HPNE (line)]] | wt | 575 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 572 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -19.0) |
| [[SW1417 (line)]] | alt | 312 | 2 (1 ⚠) | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.73× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -17.2) |
| [[HCT15 (line)]] | alt | 296 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 316 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -22.0) |
| [[LS 180 (line)]] | wt | 241 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.454× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 313 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -17.7) |
| [[SW 900 (line)]] | alt | 487 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -12.6) |
| [[A549 (line)]] | wt | 346 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -17.0) |
| [[HT-29 (line)]] | alt | 223 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.393× (z -13.6) |
| [[KATO III (line)]] | alt | 143 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.65× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.629× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 153 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.56× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.521× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 348 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 337 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -10.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.645× (z -9.8) |
| [[RKO (line)]] | wt | 353 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -21.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.575× (z -8.5) |
| [[SW 1088 (line)]] | alt | 524 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.4) |
| [[SW 1271 (line)]] | alt | 460 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -10.0) |
| [[A498 (line)]] | wt | 299 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 163 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -13.0) |
| [[CHP-212 (line)]] | wt | 496 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -17.4) |
| [[COLO 205 (line)]] | alt | 211 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 173 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 216 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -12.1) |
| [[SHP-77 (line)]] | alt | 170 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -10.7) |
| [[SNU-1 (line)]] | wt | 159 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 258 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 135 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 203 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 452 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 246 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO10]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NMNAT2]] | +0.65 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[WWTR1]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ADAM19]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[COL13A1]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[RAC2]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[DNMBP]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CALM1]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 | pathway: Neuronal System |
| [[AMOTL1]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PDLIM7]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[LRRC8C]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[DYNLT3]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KEAP1]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AKAP8]] | -0.52 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[CDH26]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ACTR3C]] | -0.50 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[CPSF7]] | -0.50 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[RPRD2]] | -0.49 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[NCOA6]] | -0.49 | -0.30 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 16, C 4. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL15A1]] | B | COL15A1 activity raises PPFIBP1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 1.71× lower at baseline in the lines without COL15A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[SPOCK1]] | B | SPOCK1 activity raises PPFIBP1's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 1.50× lower at baseline in the lines without SPOCK1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[INSYN2B]] | B | INSYN2B activity raises PPFIBP1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 1.68× lower at baseline in the lines without INSYN2B | 0.015 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[CD59]] | B | CD59 activity raises PPFIBP1's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without CD59 | 0.021 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[MMP1]] | B | MMP1 activity raises PPFIBP1's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.39× lower at baseline in the lines without MMP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[HTR7]] | B | HTR7 activity raises PPFIBP1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.37× lower at baseline in the lines without HTR7 | 0.043 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[PLAT]] | B | PLAT activity raises PPFIBP1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.55× lower at baseline in the lines without PLAT | 0.046 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[SLC46A3]] | B | SLC46A3 activity raises PPFIBP1's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without SLC46A3 | 0.049 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| [[ITGB3]] | B | ITGB3 activity raises PPFIBP1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without ITGB3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[LINC02454]] | B | LINC02454 activity raises PPFIBP1's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 1.82× lower at baseline in the lines without LINC02454 | 0.053 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[MIR100HG]] | B | MIR100HG activity raises PPFIBP1's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without MIR100HG | 0.057 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[F2R]] | B | F2R activity raises PPFIBP1's level | lines that do not express F2R (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without F2R | 0.060 | ⚠ within organs, on part of the lines; also absent: FGF2, LHFPL6, LGALS1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REP15]] | C | PPFIBP1's natural level strengthens REP15's drug response | PPFIBP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.65; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.3, 6.2); signed map (5.4, 49.4). **Vector** length 121, 40.6% of its response variance represented; |z| ≥ 3 in 1,880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.4 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +8.8 | +4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.3 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +5.6 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.1 | -7.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +2.0 |
|  | [[Flutamide (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.2 | -12.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.7 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.5 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.1 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | PPFIB scaffold protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23-p11.22 — chr12:27,523,431-27,695,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L2, hSGT2, hSgt2p, SGT2, liprin-beta1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; PPFI scaffold protein family |
| Reactome | 6 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses; Signaling by ALK fusions and activated point mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86W92](https://www.uniprot.org/uniprotkb/Q86W92) (Liprin-beta-1):

> May regulate the disassembly of focal adhesions. Did not bind receptor-like tyrosine phosphatases type 2A.

**Summary**, from NCBI Gene [8496](https://www.ncbi.nlm.nih.gov/gene/8496):

> The protein encoded by this gene is a member of the LAR protein-tyrosine phosphatase-interacting protein (liprin) family. Liprins interact with members of LAR family of transmembrane protein tyrosine phosphatases, which are known to be important for axon guidance and mammary gland development. It has been proposed that liprins are multivalent proteins that form complex structures and act as scaffolds for the recruitment and anchoring of LAR family of tyrosine phosphatases. This protein was …

**Accessions** — [HGNC:9249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9249) · Entrez [8496](https://www.ncbi.nlm.nih.gov/gene/8496) · UniProt [Q86W92](https://www.uniprot.org/uniprotkb/Q86W92) · Ensembl [ENSG00000110841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110841)

## Data

Gene col 3168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3168); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3168]; `tensor/DDL_lfc|DDL_z.npy` [3168]; `embed/gene_vectors.npy` [3168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3168 or target_col == 3168). Every well: [[PPFIBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPFIBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
