---
symbol: "SOCS7"
type: "gene"
col: 15811
ensembl_id: "ENSG00000274211"
name: "suppressor of cytokine signaling 7"
location: "17q12"
module: 40
arm: "+"
pooled_cpm: 57.37
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SOCS7

*suppressor of cytokine signaling 7* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.65× (z +14.6, q 3e-45, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.515× (z -18.7, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAT1]] (+0.70, fdr 7e-06), [[PDIA5]] (+0.70, fdr 7e-06), [[ANKS3]] (+0.70, fdr 7e-06); moves opposite to [[RIPK2-DT]] (-0.63, fdr 1e-05), [[PATL2]] (-0.62, fdr 2e-05), [[CASC9]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +14.6 | 3e-45 | 39/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +14.1 | 2e-42 | 32/48 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +11.5 | 4e-28 | 35/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +10.3 | 7e-23 | 33/48 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +6.2 | 5e-08 | 23/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +5.9 | 5e-07 | 20/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +5.1 | 3e-05 | 14/48 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.5 | 5e-04 | 17/48 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.028 | 7/48 (BT-474, CHP-212, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 1.23× | +3.1 | 0.11 | 4/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.12 | 8/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -18.7 | 0e+00 | 44/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -17.2 | 0e+00 | 34/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.663×** | -11.2 | 1e-26 | 28/44 (H4, J82, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -10.6 | 5e-24 | 31/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.723×** | -9.5 | 2e-19 | 30/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.735×** | -9.0 | 2e-17 | 27/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -8.7 | 3e-16 | 32/48 (HT-29, KATO III, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.747×** | -8.6 | 9e-16 | 33/48 (NCI-H460, KATO III, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.783×** | -7.2 | 4e-11 | 27/48 (BT-474, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.799×** | -6.6 | 3e-09 | 22/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -6.4 | 6e-09 | 23/48 (A-427, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.827×** | -5.6 | 1e-06 | 22/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | 0.840× | -5.1 | 1e-05 | 22/49 (HT-29, C-33 A, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -5.1 | 1e-05 | 15/48 (A-427, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.724×** | -5.0 | 3e-05 | 15/49 (J82, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.884× | -3.5 | 0.015 | 16/47 (NCI-H2030, C-33 A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.900× | -3.1 | 0.048 | 6/48 (LoVo, KATO III, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.924× | -3.0 | 0.081 | 7/48 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.928× | -2.9 | 0.083 | 3/48 (Panc 03.27, RPMI-7951, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.927× | -2.9 | 0.083 | 3/48 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.9 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.410× (z -13.1) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.479× (z -10.4) |
| [[A-172 (line)]] | wt | 49.2 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -22.7) |
| [[A-427 (line)]] | wt | 99.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 59.0 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.8) | [[Harringtonine (drug)]] 5 µM 0.430× (z -11.4) |
| [[HOP62 (line)]] | alt | 54.3 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.275× (z -16.1) |
| [[J82 (line)]] | alt | 37.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -17.6) |
| [[A498 (line)]] | wt | 77.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.441× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 49.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 45.8 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.110× (z -11.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.334× (z -10.1) |
| [[HT-29 (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[KATO III (line)]] | alt | 78.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 50.4 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.550× (z -8.6) |
| [[C32 (line)]] | wt | 37.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 45.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.364× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.415× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 72.8 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.49× (z +10.6) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Harringtonine (drug)]] 5 µM 0.433× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 49.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.3) |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.1) |
| [[SW1417 (line)]] | alt | 49.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.393× (z -10.4) |
| [[BT-474 (line)]] | alt | 221 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -8.6) |
| [[C-33 A (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[CHP-212 (line)]] | wt | 89.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -10.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 52.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -8.9) |
| [[H4 (line)]] | wt | 47.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 54.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.408× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 52.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 46.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -12.2) |
| [[RKO (line)]] | wt | 43.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.159× (z -15.2) ⚠ toxic; cell-cycle shift, explains ~76% of this change |
| [[RPMI-7951 (line)]] | alt | 27.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.248× (z -8.9) |
| [[SW 1271 (line)]] | alt | 59.2 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0744× (z -10.5) |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.331× (z -8.6) |
| [[A549 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT1]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ANKS3]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[BET1L]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[RNF41]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[DEXI]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[NCK1]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 | same gene group; STRING 874 |
| [[SSR2]] | +0.65 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[COG5]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK2-DT]] | -0.63 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PATL2]] | -0.62 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[CASC9]] | -0.60 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[TIA1]] | -0.60 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.59 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[GDAP1]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ZNF462]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[GNGT1]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PNRC2]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[LGALS8]] | -0.58 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[SUCLG2-DT]] | -0.58 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CLIC2]] | -0.58 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SOCS7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (3.8, -20.6); signed map (-45.8, 8.2). **Vector** length 107, 26.2% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +14.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +10.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.0 | -18.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -17.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -8.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | suppressor of cytokine signaling 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,351,844-38,405,593 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAP4, NCKAP4 |
| Gene groups (HGNC) | SH2 domain containing; Suppressors of cytokine signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14512](https://www.uniprot.org/uniprotkb/O14512) (Suppressor of cytokine signaling 7):

> Substrate-recognition component of a cullin-5-RING E3 ubiquitin-protein ligase complex (ECS complex, also named CRL5 complex), which mediates the ubiquitination and subsequent proteasomal degradation of target proteins, such as DAB1 and IRS1. Specifically recognizes and binds phosphorylated proteins via its SH2 domain, promoting their ubiquitination (By similarity). The ECS(SOCS7) complex acts as a key regulator of reelin signaling by mediating ubiquitination and degradation of phosphorylated …

**Summary**, from NCBI Gene [30837](https://www.ncbi.nlm.nih.gov/gene/30837):

> Predicted to enable phosphorylation-dependent protein binding activity; signaling adaptor activity; and ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in insulin receptor signaling pathway; proteasome-mediated ubiquitin-dependent protein catabolic process; and regulation of neuron migration. Predicted to act upstream of or within brain development; fat cell differentiation; and protein ubiquitination. Is active in cytoplasm. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:29846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29846) · Entrez [30837](https://www.ncbi.nlm.nih.gov/gene/30837) · UniProt [O14512](https://www.uniprot.org/uniprotkb/O14512) · Ensembl [ENSG00000274211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274211)

## Data

Gene col 15811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15811); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15811]; `tensor/DDL_lfc|DDL_z.npy` [15811]; `embed/gene_vectors.npy` [15811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15811 or target_col == 15811). Every well: [[SOCS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOCS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
