---
symbol: "GGA3"
type: "gene"
col: 4614
ensembl_id: "ENSG00000125447"
name: "golgi associated, gamma adaptin ear containing, ARF binding protein 3"
location: "17q25.1"
module: 114
arm: "+"
pooled_cpm: 35.99
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# GGA3

*golgi associated, gamma adaptin ear containing, ARF binding protein 3* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +17.8, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.475× (z -14.9, q 0e+00, down in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.709× (z -6.9, q 1e-09, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A549 0.0608×, A-427 0.0972×, SW480 0.192×, NCI-H1792 0.138×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.108×, LoVo 0.123×, HEC-1-A 0.205×, A549 0.211×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A549 0.107×, NCI-H23 0.129×, LS 180 0.179×, HOP62 0.197×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMEB2]] (+0.69, fdr 1e-05), [[KMT2B]] (+0.69, fdr 7e-06), [[UNK]] (+0.67, fdr 7e-06); moves opposite to [[PAPSS1]] (-0.60, fdr 1e-05), [[PLEKHB2]] (-0.58, fdr 1e-05), [[AZIN1]] (-0.57, fdr 2e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZDHHC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +17.8 | 0e+00 | 41/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +11.8 | 2e-29 | 37/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +9.9 | 1e-20 | 41/47 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +9.1 | 1e-17 | 35/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +7.8 | 8e-13 | 33/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.0 | 3e-10 | 31/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.6 | 4e-09 | 28/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 5e-04 | 20/48 (HEC-1-A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.004 | 17/47 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.009 | 15/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.19× | +3.6 | 0.019 | 16/48 (SHP-77, HEC-1-A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.066 | 14/48 (A549, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.070 | 16/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.075 | 9/48 (Hs 766T, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4614.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A549 0.0608×, A-427 0.0972×, SW480 0.192×, NCI-H1792 0.138×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.108×, LoVo 0.123×, HEC-1-A 0.205×, A549 0.211×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A549 0.107×, NCI-H23 0.129×, LS 180 0.179×, HOP62 0.197×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.475×** | -14.9 | 0e+00 | 40/45 (A549, A-427, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.470×** | -14.0 | 5e-42 | 35/42 (A549, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -12.9 | 7e-36 | 31/40 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.709×** | -6.9 | 1e-09 | 35/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.757×** | -5.3 | 1e-05 | 29/48 (AN3 CA, KATO III, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -5.1 | 3e-05 | 23/47 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.817×** | -3.9 | 0.009 | 19/48 (A-427, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 45.8 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0608× (z -28.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 47.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 31.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -19.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 50.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +21.6) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -13.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 47.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -20.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 37.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -16.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 42.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -17.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 42.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -17.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 35.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 34.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 36.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +14.4) | — |
| [[A-427 (line)]] | wt | 42.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -21.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 33.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -12.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -14.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 27.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -18.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 35.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 48.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -11.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -11.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 31.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +15.1) | — |
| [[RKO (line)]] | wt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -13.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -11.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMEB2]] | +0.69 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[KMT2B]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[UNK]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RBX1]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZC3HC1]] | +0.64 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[LSM6]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TJAP1]] | +0.62 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[NDUFA13]] ⚠ | +0.61 | +0.64 / +0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZCCHC3]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ZCCHC10]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[UBE2J2]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MTG2]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPSS1]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[PLEKHB2]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[AZIN1]] | -0.57 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[OAT]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[HLTF]] | -0.52 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[TMED7]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[TCP1]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[DPYSL2]] | -0.51 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[YWHAQ]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[EIF2S3]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[PRKAR2B]] | -0.50 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[CNIH1]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDHHC1]] | C | ZDHHC1 activity raises GGA3's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without ZDHHC1 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.9, 6.9); signed map (0.8, -9.2). **Vector** length 88.8, 19.0% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.7 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +17.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.6 | +11.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.0 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.4 | -14.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.6 | -14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | golgi associated, gamma adaptin ear containing, ARF binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,236,599-75,262,363 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0154 |
| Gene groups (HGNC) | Golgi associated, gamma adaptin ear containing, ARF binding proteins |
| Reactome | 8 pathways, smallest: MET receptor recycling; TBC/RABGAPs; Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ52](https://www.uniprot.org/uniprotkb/Q9NZ52) (ADP-ribosylation factor-binding protein GGA3):

> Plays a role in protein sorting and trafficking between the trans-Golgi network (TGN) and endosomes. Mediates the ARF-dependent recruitment of clathrin to the TGN and binds ubiquitinated proteins and membrane cargo molecules with a cytosolic acidic cluster-dileucine (DXXLL) motif. Mediates export of the GPCR receptor ADRA2B to the cell surface. nvolved in BACE1 transport and sorting as well as regulation of BACE1 protein levels. Regulates retrograde transport of BACE1 from endosomes to the …

**Summary**, from NCBI Gene [23163](https://www.ncbi.nlm.nih.gov/gene/23163):

> This gene encodes a member of the Golgi-localized, gamma adaptin ear-containing, ARF-binding (GGA) family. This family includes ubiquitous coat proteins that regulate the trafficking of proteins between the trans-Golgi network and the lysosome. These proteins share an amino-terminal VHS domain which mediates sorting of the mannose 6-phosphate receptors at the trans-Golgi network. They also contain a carboxy-terminal region with homology to the ear domain of gamma-adaptins. Multiple …

**Accessions** — [HGNC:17079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17079) · Entrez [23163](https://www.ncbi.nlm.nih.gov/gene/23163) · UniProt [Q9NZ52](https://www.uniprot.org/uniprotkb/Q9NZ52) · Ensembl [ENSG00000125447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125447)

## Data

Gene col 4614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4614); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4614]; `tensor/DDL_lfc|DDL_z.npy` [4614]; `embed/gene_vectors.npy` [4614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4614 or target_col == 4614). Every well: [[GGA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
