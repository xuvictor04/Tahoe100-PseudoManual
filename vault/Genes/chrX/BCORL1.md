---
symbol: "BCORL1"
type: "gene"
col: 1417
ensembl_id: "ENSG00000085185"
name: "BCL6 corepressor like 1"
location: "Xq26.1"
module: 162
arm: "+"
pooled_cpm: 38.51
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# BCORL1

*BCL6 corepressor like 1* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +13.0, q 1e-35, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.392× (z -18.3, q 0e+00, down in 37 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.726× (z -6.3, q 4e-08, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR47]] (+0.65, fdr 7e-06), [[CNNM4]] (+0.65, fdr 1e-05), [[PLEKHO2]] (+0.64, fdr 7e-06); moves opposite to [[CRPPA]] (-0.54, fdr 7e-05), [[DECR1]] (-0.53, fdr 8e-05), [[SRFBP1]] (-0.53, fdr 2e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +13.0 | 1e-35 | 33/48 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +11.6 | 1e-28 | 42/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +11.4 | 5e-28 | 43/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +10.2 | 3e-22 | 40/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +9.0 | 3e-17 | 40/48 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +8.5 | 2e-15 | 32/48 (SW1417, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +8.1 | 6e-14 | 38/48 (A-427, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +7.5 | 6e-12 | 32/48 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.3 | 0.001 | 17/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +4.2 | 0.002 | 22/48 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.005 | 11/47 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.14× | +3.7 | 0.009 | 16/48 (PANC-1, SW480, …) | all doses, flat | low cells (technical?) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.058 | 6/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.392×** | -18.3 | 0e+00 | 37/45 (C32, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.424×** | -15.6 | 0e+00 | 38/42 (SNU-423, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.468×** | -14.3 | 3e-44 | 32/38 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.529×** | -6.5 | 1e-08 | 17/33 (A-172, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.726×** | -6.3 | 4e-08 | 24/48 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.740×** | -5.7 | 1e-06 | 26/48 (SNU-423, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.754×** | -5.5 | 3e-06 | 25/47 (HCT15, NCI-H1573, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -5.4 | 5e-06 | 23/48 (CHP-212, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.783×** | -4.8 | 1e-04 | 22/48 (A-172, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.788×** | -4.7 | 2e-04 | 23/47 (PANC-1, SW 1271, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.799×** | -4.4 | 5e-04 | 20/48 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.652×** | -4.4 | 6e-04 | 20/48 (A-172, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.805×** | -4.2 | 1e-03 | 20/48 (NCI-H2030, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.807×** | -4.2 | 0.001 | 15/48 (PANC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.813×** | -3.9 | 0.004 | 22/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.832×** | -3.6 | 0.009 | 12/48 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.011 | 14/47 (SW 1271, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.838× | -3.5 | 0.014 | 13/48 (AN3 CA, BT-474, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | 0.839× | -3.3 | 0.025 | 15/47 (A-172, HOP62, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.840× | -3.3 | 0.026 | 14/48 (A549, NCI-H2030, …) | top dose only | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.041 | 14/45 (SW 900, C32, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.041 | 17/48 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.041 | 9/47 (PANC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 0.05 µM |  | 0.866× | -2.8 | 0.092 | 5/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.9 | 0 | 6 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0736× (z -11.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 25.9 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +8.6) | [[Simotinib (drug)]] 5 µM 0.289× (z -9.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 60.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.47× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 1.92× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 61.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -25.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 27.5 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 25.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +18.2) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 35.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 90.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -13.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 57.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0727× (z -21.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 46.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0736× (z -17.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 44.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.5) |
| [[HOP62 (line)]] | alt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 55.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -13.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 48.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -15.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 38.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -15.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 26.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.4) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 37.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0700× (z -26.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 62.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -12.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.0) | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 1 | — | [[Tolcapone (drug)]] 0.5 µM 0.0612× (z -9.5) |
| [[COLO 205 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +10.4) | — |
| [[KATO III (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -17.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -12.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.126× (z -9.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -11.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR47]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CNNM4]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[PLEKHO2]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[AHDC1]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[BIK]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[EPHB3]] | +0.62 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ASMTL]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MAST1]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[DOCK6]] | +0.61 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RBM38]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[HCN2]] | +0.60 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[NCKAP5L]] | +0.60 | +0.62 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRPPA]] | -0.54 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[DECR1]] | -0.53 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[SRFBP1]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[QRSL1]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZRANB2-DT]] | -0.52 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[ITFG1]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | -0.51 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[EIF3F]] | -0.51 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[GAS2]] | -0.51 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[SUCLG2]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.51 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[AHI1-DT]] | -0.50 | -0.33 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises BCORL1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without SEMA6B | 0.041 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[PDZD4]] | B | PDZD4 activity raises BCORL1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.30× lower at baseline in the lines without PDZD4 | 0.057 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[CACNG7]] | B | CACNG7 activity raises BCORL1's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without CACNG7 | 0.062 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[KIF26A]] | B | KIF26A activity raises BCORL1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.22× lower at baseline in the lines without KIF26A | 0.084 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers BCORL1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers BCORL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PNMA2]] | B | PNMA2 activity raises BCORL1's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 1.30× lower at baseline in the lines without PNMA2 | 0.087 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |
| [[MEX3B]] | C | MEX3B activity raises BCORL1's level | lines that do not express MEX3B (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without MEX3B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIF17, DPF1, CNTNAP1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, -6.2); signed map (-2.1, 25.8). **Vector** length 106, 27.3% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +8.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.4 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +11.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.2 | +3.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.9 | -15.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -18.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.0 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | BCL6 corepressor like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:129,981,107-130,058,071 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11362, BCoR-L1; previously CXorf10 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5H9F3](https://www.uniprot.org/uniprotkb/Q5H9F3) (BCL-6 corepressor-like protein 1):

> Transcriptional corepressor. May specifically inhibit gene expression when recruited to promoter regions by sequence-specific DNA-binding proteins such as BCL6. This repression may be mediated at least in part by histone deacetylase activities which can associate with this corepressor.

**Summary**, from NCBI Gene [63035](https://www.ncbi.nlm.nih.gov/gene/63035):

> The protein encoded by this gene is a transcriptional corepressor that is found tethered to promoter regions by DNA-binding proteins. The encoded protein can interact with several different class II histone deacetylases to repress transcription. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:25657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25657) · Entrez [63035](https://www.ncbi.nlm.nih.gov/gene/63035) · UniProt [Q5H9F3](https://www.uniprot.org/uniprotkb/Q5H9F3) · Ensembl [ENSG00000085185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085185)

## Data

Gene col 1417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1417); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1417]; `tensor/DDL_lfc|DDL_z.npy` [1417]; `embed/gene_vectors.npy` [1417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1417 or target_col == 1417). Every well: [[BCORL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCORL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
