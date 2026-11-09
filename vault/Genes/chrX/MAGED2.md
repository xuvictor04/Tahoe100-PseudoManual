---
symbol: "MAGED2"
type: "gene"
col: 2238
ensembl_id: "ENSG00000102316"
name: "MAGE family member D2"
location: "Xp11.21"
module: 41
arm: "+"
pooled_cpm: 32.81
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MAGED2

*MAGE family member D2* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +10.6, q 2e-23, up in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.68× (z +10.2, q 5e-22, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.326× (z -15.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YME1L1]] (+0.58, fdr 1e-05), [[COPB2]] (+0.58, fdr 1e-05), [[RNF167]] (+0.58, fdr 1e-05); moves opposite to [[ZNF544]] (-0.63, fdr 1e-05), [[PUS7]] (-0.61, fdr 8e-06), [[DTNB]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +10.6 | 2e-23 | 36/43 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +10.2 | 5e-22 | 40/48 (SW480, SHP-77, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +10.1 | 1e-21 | 25/35 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.57×** | +6.3 | 5e-08 | 34/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.7 | 2e-06 | 21/38 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.46×** | +5.3 | 1e-05 | 31/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.004 | 20/48 (CFPAC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.054 | 22/48 (SW480, SHP-77, …) | top dose only | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.054 | 20/48 (A-172, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.3 | 0.064 | 2/48 (HOP62, MIA PaCa-2) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.100 | 15/48 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | 1.51× | +3.0 | 0.12 | 17/46 (HOP62, KATO III, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.326×** | -15.6 | 0e+00 | 47/48 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.353×** | -14.5 | 3e-45 | 46/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.485×** | -14.2 | 1e-43 | 36/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.365×** | -14.0 | 2e-42 | 43/47 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.375×** | -13.7 | 2e-40 | 43/48 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.380×** | -13.5 | 2e-39 | 46/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.429×** | -11.8 | 4e-30 | 44/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.453×** | -11.0 | 2e-26 | 39/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.517×** | -9.2 | 2e-18 | 33/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.577×** | -7.6 | 1e-12 | 37/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -6.7 | 1e-09 | 34/48 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.623×** | -6.6 | 2e-09 | 35/48 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.628×** | -6.1 | 4e-08 | 33/48 (H4, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.442×** | -5.9 | 1e-07 | 29/48 (HOP62, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.662×** | -5.5 | 1e-06 | 25/44 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.681×** | -5.3 | 3e-06 | 27/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -5.0 | 2e-05 | 25/47 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 73.6 | 0 | 14 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.139× (z -14.3) |
| [[HOP62 (line)]] | alt | 67.5 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -18.2) |
| [[KATO III (line)]] | alt | 21.4 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 55.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -13.9) |
| [[SW480 (line)]] | alt | 39.1 | 2 | 7 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.68× (z +14.1) | [[Belinostat (drug)]] 5 µM 0.274× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 48.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 37.6 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.218× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 27.5 | 1 | 6 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.35× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.2) |
| [[A-172 (line)]] | wt | 44.7 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.256× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.258× (z -12.0) |
| [[HS-578T (line)]] | alt | 43.4 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -12.9) |
| [[SNU-423 (line)]] | alt | 69.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -10.6) |
| [[A498 (line)]] | wt | 36.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.4) |
| [[Hs 766T (line)]] | wt | 54.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -15.2) |
| [[HT-29 (line)]] | alt | 22.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 53.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -11.8) |
| [[BT-474 (line)]] | alt | 50.7 | 1 | 3 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.42× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -11.8) |
| [[COLO 205 (line)]] | alt | 28.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.4) |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.157× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 79.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -14.3) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.1) |
| [[SW 1088 (line)]] | alt | 80.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0341× (z -11.9) |
| [[SW 900 (line)]] | alt | 36.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -11.8) |
| [[SW1417 (line)]] | alt | 39.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 18.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -10.3) |
| [[LS 180 (line)]] | wt | 10.6 | 1 | 1 | [[Selinexor (drug)]] 5 µM 3.86× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.169× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -11.1) |
| [[PANC-1 (line)]] | alt | 21.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.0) |
| [[SHP-77 (line)]] | alt | 64.8 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.51× (z +11.9) | — |
| [[A549 (line)]] | wt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.104× (z -8.9) |
| [[J82 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.146× (z -9.4) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YME1L1]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[COPB2]] | +0.58 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[RNF167]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[MTFR1L]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PRCP]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[BPNT1]] | +0.56 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[FBXO8]] | +0.56 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[COPG1]] | +0.55 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[AMZ2]] | +0.55 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[FAM8A1]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[OAT]] | +0.54 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[BROX]] | +0.54 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF544]] | -0.63 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[PUS7]] | -0.61 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[DTNB]] | -0.55 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[SCLY]] | -0.53 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TANGO6]] | -0.53 | -0.71 / -0.39 | both halves | 6e-05 |  |
| [[ANKS6]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[LDLRAD3]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[METTL2B]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[NRF1]] | -0.51 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[NUP50-DT]] | -0.50 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[DAP3]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[MTHFD1L]] | -0.50 | -0.57 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.403). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-4.7, -31.9); signed map (-16.8, -30.1). **Vector** length 92.1, 25.3% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +13.0 | +10.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.1 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.3 | +5.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.1 | +2.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.1 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.7 | -11.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -11.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -14.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.7 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -7.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MAGE family member D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:54,807,599-54,816,015 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JCL-1, BCG1, 11B6, MAGE-D2, HCA10, MAGED, MGC8386 |
| Gene groups (HGNC) | MAGE family; Small nucleolar RNA protein coding host genes |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNF1](https://www.uniprot.org/uniprotkb/Q9UNF1) (Melanoma-associated antigen D2):

> Regulates the expression, localization to the plasma membrane and function of the sodium chloride cotransporters SLC12A1 and SLC12A3, two key components of salt reabsorption in the distal renal tubule.

**Summary**, from NCBI Gene [10916](https://www.ncbi.nlm.nih.gov/gene/10916):

> This gene is a member of the MAGED gene family. The MAGED genes are clustered on chromosome Xp11. This gene is located in Xp11.2, a hot spot for X-linked intellectual disability (XLID). Mutations in this gene cause a form of transient antenatal Bartter's syndrome. This gene may also be involved in several types of cancer, including breast cancer and melanoma. The protein encoded by this gene is progressively recruited from the cytoplasm to the nucleoplasm during the interphase and after …

**Accessions** — [HGNC:16353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16353) · Entrez [10916](https://www.ncbi.nlm.nih.gov/gene/10916) · UniProt [Q9UNF1](https://www.uniprot.org/uniprotkb/Q9UNF1) · Ensembl [ENSG00000102316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102316)

## Data

Gene col 2238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2238); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2238]; `tensor/DDL_lfc|DDL_z.npy` [2238]; `embed/gene_vectors.npy` [2238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2238 or target_col == 2238). Every well: [[MAGED2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGED2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
