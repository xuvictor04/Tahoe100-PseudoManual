---
symbol: "RNF34"
type: "gene"
col: 9989
ensembl_id: "ENSG00000170633"
name: "ring finger protein 34"
location: "12q24.31"
module: 129
arm: "+"
pooled_cpm: 41.01
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# RNF34

*ring finger protein 34* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.54× (z +8.4, q 3e-14, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.628× (z -9.1, q 6e-17, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N4BP1]] (+0.60, fdr 1e-05), [[FAM118B]] (+0.56, fdr 1e-05), [[RMND5B]] (+0.53, fdr 1e-05); moves opposite to [[CMBL]] (-0.51, fdr 2e-05), [[BCO2]] (-0.51, fdr 2e-04), [[SYT9-AS1]] (-0.49, fdr 1e-04).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +8.4 | 3e-14 | 34/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.0 | 2e-13 | 31/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +7.8 | 1e-12 | 30/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +7.6 | 4e-12 | 31/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.36×** | +5.8 | 6e-07 | 27/47 (HT-29, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.8 | 8e-07 | 25/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +5.1 | 3e-05 | 23/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.0 | 4e-05 | 22/47 (PANC-1, CFPAC-1, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.28×** | +4.7 | 1e-04 | 21/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.002 | 21/47 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.046 | 7/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.067 | 16/47 (C32, HOP62, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.092 | 9/47 (HEC-1-A, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Ivermectin (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.092 | 9/47 (NCI-H2030, SW1417, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.0 | 0.099 | 13/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -9.1 | 6e-17 | 39/48 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -9.0 | 9e-17 | 32/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.678×** | -7.6 | 6e-12 | 33/47 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -7.3 | 5e-11 | 32/47 (A-427, COLO 205, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.743×** | -5.8 | 8e-07 | 27/47 (SK-MEL-2, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.753×** | -5.3 | 1e-05 | 21/39 (A-427, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.607×** | -5.1 | 3e-05 | 17/35 (HT-29, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.608×** | -5.1 | 3e-05 | 25/49 (NCI-H2347, AN3 CA, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.787×** | -4.3 | 9e-04 | 19/42 (A498, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.661×** | -4.2 | 0.001 | 22/42 (Hs 766T, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.816×** | -4.0 | 0.004 | 19/48 (SW480, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.6 | 0.014 | 15/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.832×** | -3.6 | 0.015 | 14/48 (SW 1088, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.827×** | -3.5 | 0.019 | 17/48 (SK-MEL-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.722×** | -3.3 | 0.034 | 13/47 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.732×** | -3.2 | 0.052 | 13/48 (NCI-H2347, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.806×** | -3.0 | 0.090 | 8/48 (Hs 766T, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 51.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -14.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 51.3 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.397× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.443× (z -9.7) |
| [[A498 (line)]] | wt | 25.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -11.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 40.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -11.8) |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 2 | — | [[Trametinib (drug)]] 0.5 µM 0.159× (z -9.0) |
| [[COLO 205 (line)]] | alt | 57.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -9.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 43.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -10.3) |
| [[HT-29 (line)]] | alt | 34.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Lonafarnib (drug)]] 5 µM 0.150× (z -9.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 35.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.301× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 53.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.321× (z -9.5) |
| [[SW1417 (line)]] | alt | 53.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -10.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -11.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -8.5) |
| [[Hs 766T (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0823× (z -9.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.131× (z -8.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 61.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.448× (z -9.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 59.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.187× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.458× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 40.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP1]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FAM118B]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[RMND5B]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TECPR2]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[MTMR9]] | +0.52 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[ZNF7]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[UBE2D2]] | +0.52 | +0.37 / +0.55 | both halves | 9e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[BTBD10]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[DHRS7B]] | +0.51 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[KLHL22]] | +0.50 | +0.43 / +0.57 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ZNF200]] | +0.50 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TLNRD1]] | +0.50 | +0.42 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMBL]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[BCO2]] | -0.51 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[SYT9-AS1]] | -0.49 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[GSTM2]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[ARHGEF26-AS1]] | -0.48 | -0.19 / -0.38 | ⚠ not reproduced | 8e-04 |  |
| [[APP]] | -0.48 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CNOT2]] | -0.47 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[FXR1]] | -0.47 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[COPS8-DT]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CREG1]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[RAPGEF4]] | -0.46 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[CPVL]] | -0.45 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[PAPOLA]] | -0.45 | -0.29 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RNF34's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.208). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.1, 2.8); signed map (-11.9, -22.2). **Vector** length 98.6, 23.2% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +4.7 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.0 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.6 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.4 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,400,083-121,430,623 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIFF, FLJ21786, RIF |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 7 pathways, smallest: Regulation of TP53 Degradation; Regulation of TP53 Expression and Degradation; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969K3](https://www.uniprot.org/uniprotkb/Q969K3) (E3 ubiquitin-protein ligase RNF34):

> E3 ubiquitin-protein ligase that regulates several biological processes through the ubiquitin-mediated proteasomal degradation of various target proteins. Ubiquitinates the caspases CASP8 and CASP10, promoting their proteasomal degradation, to negatively regulate cell death downstream of death domain receptors in the extrinsic pathway of apoptosis. May mediate 'Lys-48'-linked polyubiquitination of RIPK1 and its subsequent proteasomal degradation thereby indirectly regulating the tumor necrosis …

**Summary**, from NCBI Gene [80196](https://www.ncbi.nlm.nih.gov/gene/80196):

> The protein encoded by this gene contains a RINF finger, a motif known to be involved in protein-protein and protein-DNA interactions. This protein interacts with DNAJA3/hTid-1, which is a DnaJ protein reported to function as a modulator of apoptosis. Overexpression of this gene in Hela cells was shown to confer the resistance to TNF-alpha induced apoptosis, suggesting an anti-apoptotic function of this protein. This protein can be cleaved by caspase-3 during the induction of apoptosis. This …

**Accessions** — [HGNC:17297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17297) · Entrez [80196](https://www.ncbi.nlm.nih.gov/gene/80196) · UniProt [Q969K3](https://www.uniprot.org/uniprotkb/Q969K3) · Ensembl [ENSG00000170633](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170633)

## Data

Gene col 9989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9989); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9989]; `tensor/DDL_lfc|DDL_z.npy` [9989]; `embed/gene_vectors.npy` [9989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9989 or target_col == 9989). Every well: [[RNF34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
