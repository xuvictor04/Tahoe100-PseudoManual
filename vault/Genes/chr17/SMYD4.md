---
symbol: "SMYD4"
type: "gene"
col: 11828
ensembl_id: "ENSG00000186532"
name: "SET and MYND domain containing 4"
location: "17p13.3"
module: 3
arm: "+"
pooled_cpm: 26.56
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SMYD4

*SET and MYND domain containing 4* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.10× (z +14.1, q 2e-42, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.519× (z -17.6, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LCMT1]] (+0.72, fdr 7e-06), [[SDHAP2]] (+0.72, fdr 7e-06), [[NUP85]] (+0.71, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.66, fdr 1e-05), [[RIPK2-DT]] (-0.64, fdr 1e-05), [[TAF9B]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +14.1 | 2e-42 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +11.8 | 2e-29 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +11.6 | 1e-28 | 42/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.011 | 9/45 (hTERT-HPNE, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.23×** | +3.8 | 0.015 | 16/44 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.21×** | +3.6 | 0.025 | 13/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.033 | 8/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.046 | 6/48 (C32, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.051 | 13/48 (SNU-423, NCI-H460, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11828.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.519×** | -17.6 | 0e+00 | 41/47 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.516×** | -11.6 | 9e-29 | 29/39 (HEC-1-A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.547×** | -11.5 | 3e-28 | 36/48 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.553×** | -10.8 | 4e-25 | 37/47 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.596×** | -9.9 | 8e-21 | 36/47 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -8.7 | 3e-16 | 31/47 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.634×** | -8.7 | 4e-16 | 26/42 (HCT15, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -7.4 | 1e-11 | 33/47 (H4, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.684×** | -7.2 | 3e-11 | 30/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -5.3 | 6e-06 | 23/48 (A-172, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -5.2 | 1e-05 | 20/48 (A498, Panc 03.27, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -5.2 | 1e-05 | 23/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -4.8 | 6e-05 | 20/35 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.622×** | -4.7 | 9e-05 | 18/47 (RPMI-7951, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.784×** | -4.6 | 1e-04 | 21/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.778×** | -4.6 | 1e-04 | 18/47 (hTERT-HPNE, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -4.5 | 2e-04 | 22/48 (COLO 205, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.667×** | -4.0 | 0.002 | 17/48 (SNU-1, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.812×** | -4.0 | 0.002 | 18/48 (CFPAC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.831×** | -3.3 | 0.023 | 18/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.5 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.416× (z -10.1) |
| [[A-172 (line)]] | wt | 39.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 43.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 21.9 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.64× (z +8.8) | [[Digitoxin (drug)]] 0.5 µM 0.321× (z -10.2) |
| [[A498 (line)]] | wt | 42.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 40.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0513× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.0) |
| [[SW 900 (line)]] | alt | 29.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.1) |
| [[HOP62 (line)]] | alt | 24.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -14.5) |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.159× (z -10.3) |
| [[C32 (line)]] | wt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -11.0) |
| [[COLO 205 (line)]] | alt | 27.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -8.6) |
| [[H4 (line)]] | wt | 29.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.1) |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.1) |
| [[J82 (line)]] | alt | 42.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.534× (z -9.6) |
| [[KATO III (line)]] | alt | 31.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -8.5) |
| [[SNU-423 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.6) |
| [[A-427 (line)]] | wt | 22.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -9.9) |
| [[A549 (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.7) |
| [[C-33 A (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -11.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.1) |
| [[HCT15 (line)]] | alt | 63.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -11.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -10.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 20.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 42.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -12.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -10.3) |
| [[SNU-1 (line)]] | wt | 23.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0662× (z -13.3) |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | +0.72 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.72 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NUP85]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SDHAF1]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.69 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[DSN1]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[SIVA1]] | +0.68 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PPIH]] | +0.67 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TRAIP]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[L2HGDH]] | +0.66 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[DEPDC5]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[NUP160]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.66 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.64 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[TAF9B]] | -0.64 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[RAP2C-AS1]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.63 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.63 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[TUG1]] | -0.62 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | -0.60 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[DDX3X]] | -0.60 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[LEKR1]] | -0.60 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[COL12A1]] | -0.59 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[ZNF655]] | -0.59 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SMYD4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ITPR2]] | B | ITPR2 activity raises SMYD4's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without ITPR2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |
| [[DHRS7B]] | C | DHRS7B's natural level strengthens SMYD4's drug response | DHRS7B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.38; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises SMYD4's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without ITPR2-AS1 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.8, -38.3); signed map (-38.0, 1.7). **Vector** length 100, 24.4% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.8 | +11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +14.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.0 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | +2.9 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | -0.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.0 | -11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -17.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.9 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | SET and MYND domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,779,485-1,830,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1936, ZMYND21 |
| Gene groups (HGNC) | Zinc fingers MYND-type; SET domain containing; Non-histone lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYR2](https://www.uniprot.org/uniprotkb/Q8IYR2) (Protein-lysine N-methyltransferase SMYD4):

> Protein-lysine N-methyltransferase. Monomethylates PRMT5, modulating its transcriptional activity. May also act as a histone methyltransferase (By similarity). Plays a critical role in cardiac development. Acts as a key epigenetic regulator of gene expression during cardiac development via its dual activities as a methyltransferase and negative regulator of HDAC1 (By similarity).

**Summary**, from NCBI Gene [114826](https://www.ncbi.nlm.nih.gov/gene/114826):

> Enables protein-lysine N-methyltransferase activity. Involved in heart development. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21067) · Entrez [114826](https://www.ncbi.nlm.nih.gov/gene/114826) · UniProt [Q8IYR2](https://www.uniprot.org/uniprotkb/Q8IYR2) · Ensembl [ENSG00000186532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186532)

## Data

Gene col 11828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11828); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11828]; `tensor/DDL_lfc|DDL_z.npy` [11828]; `embed/gene_vectors.npy` [11828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11828 or target_col == 11828). Every well: [[SMYD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMYD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
