---
symbol: "MICAL3"
type: "gene"
col: 14344
ensembl_id: "ENSG00000243156"
name: "microtubule associated monooxygenase, calponin and LIM domain containing 3"
location: "22q11.21"
module: 195
arm: "+"
pooled_cpm: 149.6
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# MICAL3

*microtubule associated monooxygenase, calponin and LIM domain containing 3* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.91× (z +12.2, q 2e-31, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.487× (z -13.5, q 7e-39, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.767× (z -5.0, q 9e-05, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A498 0.231×, HEC-1-A 0.220×, NCI-H2347 0.218×, SW48 0.194×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.0450×, A-427 0.0883×, SNU-1 0.0842×, Panc 03.27 0.175×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.212×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.511×); [[Auranofin (drug)]] 5 µM in 1 line (RKO 0.403×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.483×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTCL1]] (+0.61, fdr 7e-06), [[IFFO2]] (+0.59, fdr 2e-05), [[DNMT3B]] (+0.55, fdr 3e-05); moves opposite to [[ADAM20P1]] (-0.54, fdr 1e-05), [[ANKRA2]] (-0.53, fdr 3e-05), [[RBM48]] (-0.51, fdr 4e-05).
> It is in [[Module 195]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +12.2 | 2e-31 | 43/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +10.2 | 8e-22 | 40/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +8.6 | 1e-15 | 31/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +8.1 | 6e-14 | 34/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +6.8 | 1e-09 | 39/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.5 | 3e-06 | 30/48 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +5.4 | 5e-06 | 35/49 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.3 | 8e-06 | 25/48 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 4e-04 | 27/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.005 | 24/48 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +3.9 | 0.005 | 20/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.015 | 22/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.025 | 24/48 (COLO 205, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14344.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A498 0.231×, HEC-1-A 0.220×, NCI-H2347 0.218×, SW48 0.194×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.0450×, A-427 0.0883×, SNU-1 0.0842×, Panc 03.27 0.175×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.212×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.511×); [[Auranofin (drug)]] 5 µM in 1 line (RKO 0.403×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.483×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.487×** | -13.5 | 7e-39 | 45/49 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.504×** | -12.3 | 1e-32 | 39/44 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -8.6 | 2e-15 | 34/45 (SW48, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.767×** | -5.0 | 9e-05 | 26/48 (RKO, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.7 | 3e-04 | 22/48 (NCI-H2347, C32, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | **0.809×** | -4.0 | 0.007 | 24/47 (J82, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.832×** | -3.5 | 0.044 | 20/48 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.840× | -3.2 | 0.11 | 21/47 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.846× | -3.1 | 0.11 | 17/48 (HOP62, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 108 | 8 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.512× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 431 | 0 | 9 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -23.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 264 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -20.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 45.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.2) | — |
| [[LoVo (line)]] | wt | 118 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -13.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 176 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 332 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.511× (z -11.1) |
| [[HOP62 (line)]] | alt | 78.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.479× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 149 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -12.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 128 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 211 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -15.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 321 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -19.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 87.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 55.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.57× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 117 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 219 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -15.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 212 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -14.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 108 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 203 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -16.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 76.0 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 81.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 187 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -10.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 85.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 90.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.07× (z +9.2) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.369× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.483× (z -9.4) |
| [[PANC-1 (line)]] | alt | 96.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -10.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 161 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -10.4) |
| [[SW48 (line)]] | wt | 194 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -15.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 85.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 78.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 87.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0622× (z -15.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 178 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0842× (z -24.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 157 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.413× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 255 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Eplerenone (drug)]] 0.05 µM 0.158× (z -8.6) |
| [[A-427 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0883× (z -28.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -13.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0450× (z -30.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTCL1]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[IFFO2]] | +0.59 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[DNMT3B]] | +0.55 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[CCDC85C]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[MAST2]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[GNAZ]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[EML1]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[GLI2]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[ABCC1]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[VAV2]] | +0.50 | +0.52 / +0.37 | both halves | 9e-05 |  |
| [[KIAA0930]] | +0.50 | +0.48 / +0.42 | both halves | 4e-05 | same gene group |
| [[FAM78B]] | +0.49 | +0.45 / +0.41 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM20P1]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ANKRA2]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RBM48]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CDKL3]] | -0.51 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TBC1D15]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ING4]] | -0.50 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ZNF490]] | -0.50 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[N4BP2L2]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ADAM20]] | -0.49 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[KLRD1]] | -0.49 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[MAIP1]] | -0.48 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[N4BP2L1]] | -0.48 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.9, 32.6); signed map (-5.1, 27.6). **Vector** length 115, 36.0% of its response variance represented; |z| ≥ 3 in 1,200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.1 | +6.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.7 | +3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +12.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -8.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.5 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -12.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | +0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated monooxygenase, calponin and LIM domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:17,787,649-18,024,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0819 |
| Gene groups (HGNC) | LIM domain containing; MicroRNA protein coding host genes; Bivalent Mical/EHBP Rab binding domain containing; Flavoproteins; MICAL oxygenase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7RTP6](https://www.uniprot.org/uniprotkb/Q7RTP6) ([F-actin]-monooxygenase MICAL3):

> Monooxygenase that promotes depolymerization of F-actin by mediating oxidation of specific methionine residues on actin to form methionine-sulfoxide, resulting in actin filament disassembly and preventing repolymerization. In the absence of actin, it also functions as a NADPH oxidase producing H(2)O(2). Seems to act as Rab effector protein and plays a role in vesicle trafficking. Involved in exocytic vesicles tethering and fusion: the monooxygenase activity is required for this process and …

**Summary**, from NCBI Gene [57553](https://www.ncbi.nlm.nih.gov/gene/57553):

> Enables actin binding activity and molecular adaptor activity. Involved in actin filament depolymerization. Located in Flemming body; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24694) · Entrez [57553](https://www.ncbi.nlm.nih.gov/gene/57553) · UniProt [Q7RTP6](https://www.uniprot.org/uniprotkb/Q7RTP6) · Ensembl [ENSG00000243156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243156)

## Data

Gene col 14344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14344); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14344]; `tensor/DDL_lfc|DDL_z.npy` [14344]; `embed/gene_vectors.npy` [14344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14344 or target_col == 14344). Every well: [[MICAL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICAL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
