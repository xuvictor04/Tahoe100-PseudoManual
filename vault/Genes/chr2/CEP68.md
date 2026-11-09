---
symbol: "CEP68"
type: "gene"
col: 246
ensembl_id: "ENSG00000011523"
name: "centrosomal protein 68"
location: "2p14"
module: 187
arm: "+"
pooled_cpm: 19.42
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 16
n_dd_up_clean: 19
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# CEP68

*centrosomal protein 68* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +17.6, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.671× (z -7.8, q 3e-12, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN3]] (+0.63, fdr 2e-04), [[EZH1]] (+0.58, fdr 4e-05), [[YPEL1]] (+0.57, fdr 1e-05); moves opposite to [[LRRC59]] (-0.50, fdr 4e-05), [[EP400P1]] (-0.46, fdr 9e-05), [[CLTC]] (-0.46, fdr 1e-04).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +17.6 | 0e+00 | 42/47 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +10.8 | 7e-25 | 36/47 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +9.6 | 2e-19 | 36/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +9.0 | 2e-17 | 31/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +7.3 | 4e-11 | 30/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.8 | 5e-07 | 18/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.8 | 7e-07 | 21/48 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.6 | 2e-06 | 21/46 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.5 | 3e-06 | 20/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 1e-05 | 18/47 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.9 | 6e-05 | 16/48 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 7e-04 | 16/48 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Alpelisib (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.004 | 8/46 (NCI-H23, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.005 | 6/47 (KATO III, NCI-H2030, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.019 | 6/47 (RKO, SW1417, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.020 | 5/48 (KATO III, SW1417, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.037 | 8/48 (PANC-1, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.671×** | -7.8 | 3e-12 | 30/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.683×** | -7.5 | 2e-11 | 27/47 (SNU-1, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.755×** | -5.5 | 4e-06 | 18/47 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.755×** | -5.5 | 4e-06 | 24/46 (SW 900, A549, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -5.5 | 4e-06 | 23/44 (MIA PaCa-2, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.759×** | -5.2 | 2e-05 | 23/47 (SNU-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.788×** | -4.7 | 2e-04 | 13/47 (SW480, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -4.5 | 4e-04 | 17/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.797×** | -4.5 | 5e-04 | 18/42 (SK-MEL-2, SNU-423, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.811×** | -4.1 | 0.002 | 17/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.680×** | -4.0 | 0.004 | 14/45 (KATO III, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.825×** | -3.8 | 0.006 | 17/47 (A-427, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.812×** | -3.8 | 0.006 | 16/36 (BT-474, Panc 03.27, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.782×** | -3.5 | 0.023 | 6/48 (MIA PaCa-2, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.734×** | -3.2 | 0.055 | 13/46 (SNU-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.828×** | -3.2 | 0.057 | 3/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +15.6) | — |
| [[A-172 (line)]] | wt | 24.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.5) | [[Lonafarnib (drug)]] 5 µM 0.101× (z -9.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 29.8 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.217× (z -9.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0773× (z -13.0) |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -9.7) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.168× (z -8.7) |
| [[A549 (line)]] | wt | 27.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[C32 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.112× (z -10.0) |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 1 | — | [[Tomivosertib (drug)]] 5 µM 0.0670× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN3]] | +0.63 | +0.32 / +0.65 | both halves | 2e-04 |  |
| [[EZH1]] | +0.58 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[YPEL1]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MORC3]] | +0.50 | +0.17 / +0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[PAPOLG]] | +0.49 | +0.27 / +0.55 | both halves | 3e-04 |  |
| [[EAPP]] | +0.49 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[ZSCAN2]] | +0.49 | +0.29 / +0.60 | both halves | 3e-04 |  |
| [[HERPUD2]] | +0.49 | +0.26 / +0.51 | both halves | 4e-04 |  |
| [[ZC2HC1A]] | +0.48 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[COQ8A]] | +0.48 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[CCDC115]] | +0.48 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[PIK3CA]] | +0.48 | +0.29 / +0.43 | both halves | 3e-04 |  |
| [[DSTYK]] | +0.47 | +0.34 / +0.58 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC59]] | -0.50 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[EP400P1]] | -0.46 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[CLTC]] | -0.46 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[SRPRA]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SPCS3]] | -0.46 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[MINAR1]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[DNAJB11]] | -0.44 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PDHA1]] | -0.44 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[PSMD1]] | -0.44 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[AIFM1]] | -0.44 | -0.14 / -0.43 | ⚠ not reproduced | 0.002 |  |
| [[NRDC]] | -0.44 | -0.21 / -0.49 | both halves | 7e-04 |  |
| [[FAM98A]] | -0.43 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[UGGT1]] | -0.43 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CEP68's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIK3CA]] | B | PIK3CA activity lowers CEP68's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.5, -50.5); signed map (-15.4, 7.1). **Vector** length 64.3, 10.0% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +17.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +1.5 | +3.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +1.3 | +3.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.2 | -4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.1 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | -3.3 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 68 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:65,056,354-65,087,004 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0582 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76N32](https://www.uniprot.org/uniprotkb/Q76N32) (Centrosomal protein of 68 kDa):

> Involved in maintenance of centrosome cohesion, probably as part of a linker structure which prevents centrosome splitting. Required for localization of CDK5RAP2 to the centrosome during interphase. Contributes to CROCC/rootletin filament formation.

**Summary**, from NCBI Gene [23177](https://www.ncbi.nlm.nih.gov/gene/23177):

> Enables protein domain specific binding activity and protein kinase binding activity. Involved in centriole-centriole cohesion. Located in centriolar satellite. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29076) · Entrez [23177](https://www.ncbi.nlm.nih.gov/gene/23177) · UniProt [Q76N32](https://www.uniprot.org/uniprotkb/Q76N32) · Ensembl [ENSG00000011523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011523)

## Data

Gene col 246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 246); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 246]; `tensor/DDL_lfc|DDL_z.npy` [246]; `embed/gene_vectors.npy` [246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 246 or target_col == 246). Every well: [[CEP68 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP68.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
