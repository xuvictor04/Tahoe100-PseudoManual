---
symbol: "SIPA1L1"
type: "gene"
col: 12414
ensembl_id: "ENSG00000197555"
name: "signal induced proliferation associated 1 like 1"
location: "14q24.2"
module: 5
arm: "+"
pooled_cpm: 287.47
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SIPA1L1

*signal induced proliferation associated 1 like 1* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.40× (z +6.0, q 1e-06, up in 35 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 1.33× (z +4.4, q 0.004, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.424× (z -15.1, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRG]] (+0.69, fdr 7e-06), [[NHSL1]] (+0.63, fdr 1e-05), [[TPK1]] (+0.61, fdr 1e-05); moves opposite to [[MAPK3]] (-0.61, fdr 1e-05), [[USP30]] (-0.57, fdr 1e-05), [[DBP]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AKAP12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +6.0 | 1e-06 | 35/46 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.33×** | +4.4 | 0.004 | 36/45 (C32, A-172, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.006 | 26/46 (SW480, CFPAC-1, …) | top dose only |  |
| [[Dabrafenib (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.037 | 29/47 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.037 | 24/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.037 | 26/46 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.092 | 22/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.424×** | -15.1 | 0e+00 | 44/46 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.416×** | -14.8 | 0e+00 | 37/42 (LS 180, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.445×** | -14.2 | 1e-43 | 45/46 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.423×** | -12.7 | 1e-34 | 42/47 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.503×** | -12.1 | 2e-31 | 41/46 (HT-29, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.495×** | -11.4 | 4e-28 | 35/43 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -8.2 | 2e-14 | 33/46 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.643×** | -7.8 | 6e-13 | 39/46 (SW480, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -7.7 | 1e-12 | 33/45 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.539×** | -5.7 | 8e-07 | 37/45 (H4, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.836× | -4.4 | 5e-04 | 22/46 (RKO, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.817×** | -3.5 | 0.019 | 24/46 (RKO, LOX-IMVI, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.682×** | -3.5 | 0.019 | 25/47 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.818×** | -3.5 | 0.019 | 22/46 (J82, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.830×** | -3.1 | 0.066 | 21/45 (RKO, NCI-H1792, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.832×** | -3.1 | 0.066 | 19/47 (HS-578T, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 447 | 11 | 7 (4 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.51× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.368× (z -11.1) |
| [[Hs 766T (line)]] | wt | 111 | 14 | 0 | [[Budesonide (drug)]] 5 µM 4.58× (z +13.4) | — |
| [[RKO (line)]] | wt | 507 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -18.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.293× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 478 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 789 | 0 | 11 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.170× (z -17.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.295× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 537 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.235× (z -15.8) |
| [[HOP62 (line)]] | alt | 605 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -16.5) |
| [[C32 (line)]] | wt | 440 | 1 | 8 (4 ⚠) | [[Ponatinib (drug)]] 5 µM 2.18× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.547× (z -10.4) |
| [[LoVo (line)]] | wt | 301 | 5 (5 ⚠) | 4 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.28× (z +11.2) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.275× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.483× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 1,109 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.168× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 116 | 2 (2 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.7) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.416× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SNU-423 (line)]] | alt | 399 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -15.0) |
| [[HS-578T (line)]] | alt | 179 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 440 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.226× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.386× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 299 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.300× (z -14.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -14.1) |
| [[SW480 (line)]] | alt | 201 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.401× (z -15.5) |
| [[C-33 A (line)]] | alt | 357 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.366× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 298 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -19.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.319× (z -12.5) |
| [[HT-29 (line)]] | alt | 209 | 1 (1 ⚠) | 5 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.97× (z +8.8) ⚠ unreliable plate only | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -17.5) |
| [[hTERT-HPNE (line)]] | wt | 408 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.307× (z -10.9) |
| [[SW1417 (line)]] | alt | 193 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -14.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -12.1) |
| [[A-427 (line)]] | wt | 316 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -12.4) |
| [[LS 180 (line)]] | wt | 312 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.400× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 409 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -13.0) |
| [[PANC-1 (line)]] | alt | 172 | 2 (2 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.44× (z +12.8) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.395× (z -12.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 472 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.291× (z -12.9) |
| [[A-172 (line)]] | wt | 139 | 3 (3 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.20× (z +9.4) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.407× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 170 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -12.7) |
| [[A549 (line)]] | wt | 147 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 176 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +19.3) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -9.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 294 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.396× (z -9.5) |
| [[COLO 205 (line)]] | alt | 280 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -11.1) |
| [[H4 (line)]] | wt | 367 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -8.7) |
| [[J82 (line)]] | alt | 179 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[RPMI-7951 (line)]] | alt | 202 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.354× (z -8.9) |
| [[SHP-77 (line)]] | alt | 132 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.501× (z -8.6) |
| [[AN3 CA (line)]] | alt | 224 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.234× (z -11.3) |
| [[BT-474 (line)]] | alt | 190 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 267 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0483× (z -12.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 54.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 69.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRG]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NHSL1]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TPK1]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.59 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[TRMT6]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SLC26A2]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[HMGA2]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PRKCE]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[ENOX2]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[STXBP5]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[MAP4K4]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MOSMO]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK3]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 | pathway: Neuronal System |
| [[USP30]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[DBP]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[GPRC5B]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[IFT172]] | -0.53 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[OGA]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GDPD3]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[FRG1DP]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[TP53BP1]] | -0.48 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[IFT52]] | -0.48 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[C12orf76]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[GALM]] | -0.48 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKAP12]] | B | AKAP12 activity raises SIPA1L1's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 1.72× lower at baseline in the lines without AKAP12 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[DIAPH2]] | B | DIAPH2 activity raises SIPA1L1's level | lines that do not express DIAPH2 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without DIAPH2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000271204 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (21.7, -8.1); signed map (13.2, 21.8). **Vector** length 127, 44.0% of its response variance represented; |z| ≥ 3 in 1,634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +0.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.3 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.9 | +4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +0.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.7 | -5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.2 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -15.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -1.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.7 | -2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | signal induced proliferation associated 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:71,320,449-71,741,229 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0440, E6TP1, SPAR1 |
| Gene groups (HGNC) | PDZ domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O43166](https://www.uniprot.org/uniprotkb/O43166) (Signal-induced proliferation-associated 1-like protein 1):

> Stimulates the GTPase activity of RAP2A. Promotes reorganization of the actin cytoskeleton and recruits DLG4 to F-actin. Contributes to the regulation of dendritic spine morphogenesis (By similarity).

**Summary**, from NCBI Gene [26037](https://www.ncbi.nlm.nih.gov/gene/26037):

> Predicted to enable GTPase activator activity; actin filament binding activity; and protein kinase binding activity. Predicted to be involved in several processes, including activation of GTPase activity; postsynaptic actin cytoskeleton organization; and regulation of postsynapse organization. Located in actin cytoskeleton and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20284) · Entrez [26037](https://www.ncbi.nlm.nih.gov/gene/26037) · UniProt [O43166](https://www.uniprot.org/uniprotkb/O43166) · Ensembl [ENSG00000197555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197555)

## Data

Gene col 12414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12414); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12414]; `tensor/DDL_lfc|DDL_z.npy` [12414]; `embed/gene_vectors.npy` [12414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12414 or target_col == 12414). Every well: [[SIPA1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIPA1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
