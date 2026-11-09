---
symbol: "ARL6IP1"
type: "gene"
col: 9971
ensembl_id: "ENSG00000170540"
name: "ARL6 interacting reticulophagy regulator 1"
location: "16p12.3"
module: 22
arm: "+"
pooled_cpm: 290.6
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ARL6IP1

*ARL6 interacting reticulophagy regulator 1* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +15.5, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Cytarabine (drug)]] 5 µM: 0.709× (z -3.5, q 0.098, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.710× (z -3.5, q 0.098, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.388×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTTG1]] (+0.77, fdr 7e-06), [[PIF1]] (+0.74, fdr 7e-06), [[PRR11]] (+0.72, fdr 7e-06); moves opposite to [[MAK16]] (-0.56, fdr 3e-05), [[MRPL20]] (-0.55, fdr 3e-05), [[DNAJA3]] (-0.55, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +15.5 | 0e+00 | 49/49 (KATO III, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.92×** | +11.4 | 1e-27 | 47/48 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.24×** | +10.9 | 2e-25 | 48/49 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.76×** | +10.8 | 7e-25 | 47/48 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.76×** | +10.3 | 5e-23 | 43/44 (A549, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.79×** | +8.7 | 4e-16 | 32/48 (NCI-H1792, C32, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.21×** | +8.4 | 4e-15 | 46/48 (KATO III, NCI-H23, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.19×** | +8.3 | 6e-15 | 47/48 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +7.2 | 5e-11 | 42/50 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.06×** | +7.1 | 9e-11 | 42/45 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.93×** | +7.0 | 2e-10 | 44/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +6.8 | 4e-10 | 26/50 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **3.13×** | +6.3 | 1e-08 | 44/47 (C32, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.1 | 4e-08 | 42/47 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.0 | 9e-08 | 39/48 (MIA PaCa-2, BT-474, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.008 | 28/48 (BT-474, HOP62, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.026 | 33/48 (COLO 205, KATO III, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.057 | 26/48 (NCI-H23, LoVo, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.068 | 28/48 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9971.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.388×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.709×** | -3.5 | 0.098 | 36/48 (SHP-77, A-427, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.710×** | -3.5 | 0.098 | 33/49 (HepG2/C3A, AN3 CA, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.692×** | -3.5 | 0.098 | 34/48 (A549, C32, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -3.4 | 0.098 | 30/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.562× | -3.2 | 0.14 | 30/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.82 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 239 | 8 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 327 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +13.2) | — |
| [[KATO III (line)]] | alt | 498 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +18.8) | — |
| [[NCI-H460 (line)]] | wt | 173 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 390 | 7 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +14.2) | — |
| [[SW1417 (line)]] | alt | 396 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +14.6) | — |
| [[A-172 (line)]] | wt | 300 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.2) | — |
| [[A549 (line)]] | wt | 301 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 285 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 245 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.7) | — |
| [[J82 (line)]] | alt | 338 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 276 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 138 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +12.9) | — |
| [[SW480 (line)]] | alt | 264 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +13.4) | — |
| [[CFPAC-1 (line)]] | alt | 354 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 255 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 188 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 228 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +13.1) | — |
| [[RKO (line)]] | wt | 228 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +13.9) | — |
| [[A498 (line)]] | wt | 442 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.89× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 303 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +15.3) | — |
| [[HepG2_C3A (line)]] | wt | 241 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +18.0) | — |
| [[Hs 766T (line)]] | wt | 422 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 180 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 191 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.29× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SHP-77 (line)]] | alt | 232 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 455 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +16.7) | — |
| [[C-33 A (line)]] | alt | 273 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 189 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 320 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.41× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 198 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 203 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 227 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 304 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.92× (z +9.1) | — |
| [[A-427 (line)]] | wt | 249 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 319 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 495 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 296 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 269 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +11.2) | — |
| [[SW48 (line)]] | wt | 348 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 374 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 239 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 449 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 235 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 318 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTTG1]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[PIF1]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[PRR11]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[NUSAP1]] | +0.71 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[CDCA2]] | +0.71 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[NEK2]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[KIF18A]] | +0.70 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[TOP2A]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[KIF20A]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[DLGAP5]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[FAM72D]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAK16]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[MRPL20]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 | STRING 826 |
| [[DNAJA3]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RAD51D]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[DDX31]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[BYSL]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 | STRING 772 |
| [[REXO4]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[NDUFAF4]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[RRS1]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[MRPS23]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[EIF6]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARL6IP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.3, -57.8); signed map (-51.7, -41.6). **Vector** length 126, 60.7% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.50 to 60); *DREAM G2/M down* (control, mean cos +0.60 to 28); *mitotic spindle* (hallmark, mean cos +0.52 to 38).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +6.3 | +7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +5.3 | +5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.2 | +6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | +5.0 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.2 | +4.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.2 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.6 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.5 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ARL6 interacting reticulophagy regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:18,791,669-18,801,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AIP1, ARMER, KIAA0069, SPG61; previously ARL6IP |
| Hallmark sets | DNA_REPAIR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15041](https://www.uniprot.org/uniprotkb/Q15041) (ADP-ribosylation factor-like protein 6-interacting protein 1):

> Positively regulates SLC1A1/EAAC1-mediated glutamate transport by increasing its affinity for glutamate in a PKC activity-dependent manner. Promotes the catalytic efficiency of SLC1A1/EAAC1 probably by reducing its interaction with ARL6IP5, a negative regulator of SLC1A1/EAAC1-mediated glutamate transport (By similarity). Plays a role in the formation and stabilization of endoplasmic reticulum tubules. Negatively regulates apoptosis, possibly by modulating the activity of caspase-9 (CASP9). …

**Summary**, from NCBI Gene [23204](https://www.ncbi.nlm.nih.gov/gene/23204):

> This gene belongs to the ARL6ip family and encodes a transmembrane protein that is predominantly localized to intracytoplasmic membranes. It is highly expressed in early myeloid progenitor cells and thought to be involved in protein transport, membrane trafficking, or cell signaling during hematopoietic maturation. Mutations in this gene are associated with spastic paraplegia 61 (SPG61). Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:697) · Entrez [23204](https://www.ncbi.nlm.nih.gov/gene/23204) · UniProt [Q15041](https://www.uniprot.org/uniprotkb/Q15041) · Ensembl [ENSG00000170540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170540)

## Data

Gene col 9971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9971); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9971]; `tensor/DDL_lfc|DDL_z.npy` [9971]; `embed/gene_vectors.npy` [9971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9971 or target_col == 9971). Every well: [[ARL6IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL6IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
