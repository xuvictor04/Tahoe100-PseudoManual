---
symbol: "TXNRD1"
type: "gene"
col: 12590
ensembl_id: "ENSG00000198431"
name: "thioredoxin reductase 1"
location: "12q23.3"
module: 117
arm: "+"
pooled_cpm: 579.36
n_lines_expressing: 49
n_dd_up: 43
n_dd_down: 8
n_dd_up_clean: 32
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# TXNRD1

*thioredoxin reductase 1* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.07× (z +18.1, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.648× (z -10.0, q 1e-20, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EID3]] (+0.89, fdr 7e-06, ⚠ read-through risk), [[GCLM]] (+0.80, fdr 7e-06), [[SLC7A11]] (+0.69, fdr 7e-06), [[AKR1C1]] (+0.64, fdr 7e-06); moves opposite to [[TYK2]] (-0.55, fdr 1e-05), [[PEX11B]] (-0.54, fdr 1e-05), [[LRRC40]] (-0.53, fdr 4e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.07×** | +18.1 | 0e+00 | 44/47 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.63×** | +15.6 | 0e+00 | 43/47 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.70×** | +15.1 | 0e+00 | 44/47 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.54×** | +14.5 | 1e-45 | 43/46 (HOP62, HCT15, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.45×** | +14.2 | 2e-43 | 44/47 (LS 180, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.28×** | +10.1 | 8e-22 | 38/44 (LS 180, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +8.4 | 2e-15 | 33/47 (NCI-H1792, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +8.1 | 3e-14 | 36/47 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +7.7 | 1e-12 | 37/47 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +7.3 | 1e-11 | 32/47 (COLO 205, SW 900, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.59×** | +7.3 | 1e-11 | 37/47 (BT-474, C-33 A, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.57×** | +7.3 | 1e-11 | 36/47 (Panc 03.27, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.76×** | +6.5 | 3e-09 | 33/48 (LS 180, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.52×** | +6.5 | 4e-09 | 37/46 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +6.1 | 3e-08 | 30/47 (A-172, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +5.7 | 3e-07 | 31/48 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +5.4 | 2e-06 | 37/47 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.648×** | -10.0 | 1e-20 | 32/47 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -9.2 | 1e-17 | 29/48 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.627×** | -7.6 | 7e-12 | 39/47 (RKO, LoVo, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.629×** | -7.2 | 6e-11 | 30/46 (HT-29, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.773×** | -5.9 | 4e-07 | 29/47 (RKO, LoVo, …) | two highest doses | low cells (technical?) |
| [[APTO-253 (drug)]] 5 µM |  | **0.584×** | -4.6 | 5e-04 | 33/47 (NCI-H2347, J82, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.015 | 25/47 (LoVo, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.804×** | -3.4 | 0.045 | 23/47 (NCI-H23, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.822× | -3.1 | 0.13 | 22/47 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 280 | 17 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.6× (z +21.0) | — |
| [[RKO (line)]] | wt | 550 | 3 (1 ⚠) | 12 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.99× (z +11.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 0.5 µM 2.54× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -19.6) |
| [[HT-29 (line)]] | alt | 1,007 | 5 | 9 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.25× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.207× (z -15.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.435× (z -12.2) |
| [[COLO 205 (line)]] | alt | 346 | 13 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.06× (z +17.1) | — |
| [[CFPAC-1 (line)]] | alt | 290 | 10 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.05× (z +16.0) | — |
| [[LoVo (line)]] | wt | 527 | 7 (1 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.15× (z +19.4) | [[Selinexor (drug)]] 5 µM 0.501× (z -11.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Selinexor (drug)]] 0.5 µM 0.421× (z -10.3) |
| [[SNU-423 (line)]] | alt | 314 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.97× (z +18.1) | — |
| [[A-172 (line)]] | wt | 182 | 9 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.30× (z +18.7) | — |
| [[LS 180 (line)]] | wt | 279 | 9 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.79× (z +21.8) | — |
| [[NCI-H2347 (line)]] | alt | 509 | 7 (2 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +15.2) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.486× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.608× (z -9.2) |
| [[A-427 (line)]] | wt | 770 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.09× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.447× (z -10.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.598× (z -10.1) |
| [[HCT15 (line)]] | alt | 696 | 5 (1 ⚠) | 3 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.91× (z +14.2) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.55× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 2,150 | 1 | 7 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.52× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -26.8) |
| [[Panc 03.27 (line)]] | alt | 266 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.45× (z +13.8) | — |
| [[SW480 (line)]] | alt | 193 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.22× (z +21.8) | — |
| [[A549 (line)]] | wt | 541 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.88× (z +15.2) | — |
| [[HepG2_C3A (line)]] | wt | 437 | 6 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.11× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.391× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HOP62 (line)]] | alt | 227 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.86× (z +15.7) | — |
| [[J82 (line)]] | alt | 819 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 1,062 | 3 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.73× (z +11.1) | [[Adagrasib (drug)]] 0.05 µM 0.585× (z -15.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 1,273 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -18.7) |
| [[NCI-H460 (line)]] | wt | 856 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.05 µM 4.51× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -10.2) |
| [[SW1417 (line)]] | alt | 352 | 5 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.62× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.4) |
| [[C-33 A (line)]] | alt | 274 | 5 | 1 | [[Auranofin (drug)]] 5 µM 5.07× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 593 | 2 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 167 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.36× (z +10.2) | — |
| [[KATO III (line)]] | alt | 526 | 4 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.97× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 441 | 5 (1 ⚠) | 1 | [[TAK-901 (drug)]] 0.05 µM 3.27× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.4) |
| [[SNU-1 (line)]] | wt | 682 | 2 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.45× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -17.6) |
| [[HS-578T (line)]] | alt | 183 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.72× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 227 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.76× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 475 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.62× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.7) |
| [[SW48 (line)]] | wt | 502 | 1 | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.63× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 1,191 | 2 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 4.88× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.5) |
| [[PANC-1 (line)]] | alt | 555 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.64× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.9) |
| [[SW 900 (line)]] | alt | 455 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +12.3) | — |
| [[AN3 CA (line)]] | alt | 315 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.45× (z +17.0) | — |
| [[Hs 766T (line)]] | wt | 282 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.27× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 1,368 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -13.4) |
| [[BT-474 (line)]] | alt | 266 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.21× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 436 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -19.0) |
| [[A498 (line)]] | wt | 801 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -8.6) |
| [[CHP-212 (line)]] | wt | 206 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.79× (z +10.5) | — |
| [[H4 (line)]] | wt | 405 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.48× (z +8.8) ⚠ toxic | — |
| [[C32 (line)]] | wt | 107 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 799 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 511 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 515 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID3]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | STRING 689; ⚠ **readthrough risk**: EID3 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[GCLM]] | +0.80 | +0.79 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 795 |
| [[SLC7A11]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 664 |
| [[AKR1C1]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 | STRING 581 |
| [[CYP4F11]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NMRAL2P]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NMRAL2P-1]] | +0.60 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[EIF4G3]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TXN]] | +0.59 | +0.62 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 999 |
| [[PIR]] | +0.58 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PRDX1]] | +0.58 | +0.65 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 795 |
| [[SEL1L3]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PTGR1]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 | STRING 412 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYK2]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[PEX11B]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[LRRC40]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[INTS6L]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ARHGAP1]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ZNF451]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CRLS1]] | -0.48 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[TGDS]] | -0.47 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ICAM3]] | -0.47 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[LINC00674]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SPATA7]] | -0.46 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[HADHB]] | -0.46 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1B]] | B | MAP1B activity lowers TXNRD1's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 1.51× higher at baseline in the lines without MAP1B | 0.055 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[SLC7A11]] | B | SLC7A11 activity raises TXNRD1's level | lines that do not express SLC7A11 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without SLC7A11 | 0.064 | ⚠ within organs, on part of the lines; also absent: CD68; maybe low, not absent |
| [[GYPC]] | B | GYPC activity lowers TXNRD1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.69× higher at baseline in the lines without GYPC | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[COBL]] | B | COBL activity raises TXNRD1's level | lines that do not express COBL (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without COBL | 0.096 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[TXN]] | C | TXN's natural level weakens TXNRD1's drug response | TXN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.12; direction not clear | 0.041 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NUTM2A-AS1]] | C | NUTM2A-AS1 activity raises TXNRD1's level | lines that do not express NUTM2A-AS1 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without NUTM2A-AS1 | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ISG15, ENSG00000285257, BIRC3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.9, 48.1); signed map (51.6, -10.5). **Vector** length 160, 57.9% of its response variance represented; |z| ≥ 3 in 2,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.4 | +14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.6 | +18.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.1 | +15.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.4 | +15.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.6 | +14.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.2 | +7.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.0 | +6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.4 | +5.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.2 | -10.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.8 | -5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.4 | -7.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.5 | -7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -9.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | -1.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -3.1 | -2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:104,215,779-104,350,307 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TXNR, GRIM-12, Trxr1, TXNR1 |
| Gene groups (HGNC) | Selenoproteins; Glutaredoxin domain containing; Flavoproteins; Thioredoxin reductase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, MTORC1_SIGNALING |
| Reactome | 20 pathways, smallest: Metabolism of ingested H2SeO4 and H2SeO3 into H2Se; Uptake and function of diphtheria toxin; NFE2L2 regulating anti-oxidant/detoxification enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16881](https://www.uniprot.org/uniprotkb/Q16881) (Thioredoxin reductase 1, cytoplasmic):

> Reduces disulfide protein thioredoxin (Trx) to its dithiol-containing form. Homodimeric flavoprotein involved in the regulation of cellular redox reactions, growth and differentiation. A selenocysteine residue at the C-terminal active site is essential for catalysis (Probable). Also has reductase activity on hydrogen peroxide (H2O2).; [Isoform 1]: Induces actin and tubulin polymerization, leading to formation of cell membrane protrusions.; [Isoform 4]: Enhances the transcriptional activity of …

**Summary**, from NCBI Gene [7296](https://www.ncbi.nlm.nih.gov/gene/7296):

> The protein encoded by this gene belongs to the pyridine nucleotide-disulfide oxidoreductase family, and is a member of the thioredoxin (Trx) system. Three thioredoxin reductase (TrxR) isozymes are found in mammals. TrxRs are selenocysteine-containing flavoenzymes, which reduce thioredoxins, as well as other substrates, and play a key role in redox homoeostasis. This gene encodes an ubiquitously expressed, cytosolic form of TrxR, which functions as a homodimer containing FAD, and selenocysteine …

**Accessions** — [HGNC:12437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12437) · Entrez [7296](https://www.ncbi.nlm.nih.gov/gene/7296) · UniProt [Q16881](https://www.uniprot.org/uniprotkb/Q16881) · Ensembl [ENSG00000198431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198431)

## Data

Gene col 12590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12590); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12590]; `tensor/DDL_lfc|DDL_z.npy` [12590]; `embed/gene_vectors.npy` [12590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12590 or target_col == 12590). Every well: [[TXNRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
