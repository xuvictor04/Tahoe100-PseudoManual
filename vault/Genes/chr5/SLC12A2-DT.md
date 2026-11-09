---
symbol: "SLC12A2-DT"
type: "gene"
col: 14450
ensembl_id: "ENSG00000245937"
name: "SLC12A2 divergent transcript"
location: "5q23.3"
module: 1
arm: "+"
pooled_cpm: 51.2
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 25
n_dd_up_clean: 11
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SLC12A2-DT

*SLC12A2 divergent transcript* — 5q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +10.5, q 3e-23, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.342× (z -14.2, q 9e-43, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABPB1-AS1]] (+0.66, fdr 5e-05), [[ADGRA3]] (+0.65, fdr 1e-05), [[FBXL17]] (+0.63, fdr 3e-05); moves opposite to [[VRK3]] (-0.64, fdr 1e-05), [[GNAI2]] (-0.63, fdr 2e-05), [[GIPR]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF385A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +10.5 | 3e-23 | 40/47 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +7.2 | 2e-10 | 39/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 1e-04 | 29/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +4.5 | 8e-04 | 27/48 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.003 | 24/48 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.0 | 0.005 | 24/48 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.005 | 24/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.013 | 23/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.7 | 0.013 | 20/42 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.33×** | +3.6 | 0.018 | 22/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.054 | 18/48 (A-172, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.069 | 20/47 (LS 180, SW48, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +3.1 | 0.069 | 23/44 (SK-MEL-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.069 | 18/48 (HOP62, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.074 | 15/48 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.085 | 13/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.342×** | -14.2 | 9e-43 | 43/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.349×** | -13.9 | 2e-41 | 38/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.436×** | -11.0 | 9e-26 | 42/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.465×** | -10.1 | 6e-22 | 43/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.487×** | -9.5 | 2e-19 | 40/48 (HT-29, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -9.2 | 2e-18 | 36/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.266×** | -9.1 | 5e-18 | 44/49 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.516×** | -8.8 | 1e-16 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.301×** | -8.3 | 8e-15 | 36/48 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.533×** | -7.9 | 2e-13 | 39/48 (SW48, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.684×** | -7.1 | 5e-11 | 33/48 (A498, PANC-1, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.603×** | -6.4 | 6e-09 | 30/47 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.469×** | -5.2 | 7e-06 | 27/43 (SW48, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.761×** | -5.1 | 1e-05 | 31/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.487×** | -5.0 | 3e-05 | 31/48 (COLO 205, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.643×** | -4.7 | 1e-04 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.743×** | -3.9 | 0.003 | 27/48 (BT-474, LoVo, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.012 | 16/48 (SW 1088, PANC-1, …) | top dose only | plate-row cell shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.766×** | -3.4 | 0.018 | 19/48 (LS 180, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 108 | 0 | 13 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.165× (z -17.5) |
| [[PANC-1 (line)]] | alt | 76.5 | 1 | 12 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 55.9 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.4) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -10.5) |
| [[SW480 (line)]] | alt | 47.8 | 0 | 8 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -15.3) |
| [[A-427 (line)]] | wt | 109 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.294× (z -13.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -12.5) |
| [[LoVo (line)]] | wt | 64.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -15.7) |
| [[LS 180 (line)]] | wt | 72.3 | 0 | 6 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.254× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 62.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -10.6) |
| [[SW1417 (line)]] | alt | 44.6 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -12.6) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -11.5) |
| [[COLO 205 (line)]] | alt | 70.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.1) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.246× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 64.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -9.2) |
| [[SW48 (line)]] | wt | 87.7 | 0 | 5 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.112× (z -12.9) |
| [[C-33 A (line)]] | alt | 72.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -9.1) |
| [[J82 (line)]] | alt | 25.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 66.0 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.59× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -12.7) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.122× (z -9.7) |
| [[A498 (line)]] | wt | 52.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -16.7) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.309× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 59.0 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -10.9) |
| [[RKO (line)]] | wt | 47.0 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 72.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.134× (z -9.2) |
| [[SNU-1 (line)]] | wt | 57.3 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0695× (z -16.0) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.0662× (z -8.8) |
| [[C32 (line)]] | wt | 40.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.2) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.248× (z -8.8) |
| [[KATO III (line)]] | alt | 39.8 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.332× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 45.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -11.3) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.351× (z -8.5) |
| [[A549 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -9.9) ⚠ cell-cycle shift, explains ~79% of this change |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 100 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.435× (z -9.5) |
| [[Hs 766T (line)]] | wt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.4) ⚠ cell-cycle shift, explains ~79% of this change |
| [[RPMI-7951 (line)]] | alt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 24.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.7) | — |
| [[A-172 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1-AS1]] | +0.66 | +0.75 / +0.40 | both halves | 5e-05 |  |
| [[ADGRA3]] | +0.65 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[FBXL17]] | +0.63 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[GCFC2]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[RNASEH2B]] | +0.62 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[POGLUT1]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PARD3B]] | +0.61 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[RXYLT1]] | +0.61 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[CYP4V2]] | +0.61 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[MBNL3]] | +0.61 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[SRFBP1]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SLC35F2]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK3]] | -0.64 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[GNAI2]] | -0.63 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[GIPR]] | -0.62 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[MKNK1]] | -0.62 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ATOSB]] | -0.59 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[NOSIP]] | -0.58 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PLCD1]] | -0.58 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[HSPB11]] | -0.58 | -0.66 / -0.32 | both halves | 2e-04 |  |
| [[SLC8B1]] | -0.58 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[GYS1]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[MACO1]] | -0.57 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[MYO9B]] | -0.57 | -0.61 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF385A]] | B | ZNF385A activity lowers SLC12A2-DT's level | lines that do not express ZNF385A (7) vs lines expressing it (43) | 1.21× higher at baseline in the lines without ZNF385A | 0.068 | ⚠ within organs, on part of the lines; also absent: PDP1, AGBL2; maybe low, not absent |
| [[PDE3B]] | B | PDE3B activity strengthens SLC12A2-DT's drug response | lines that do not express PDE3B (20) vs lines expressing it (29) | the lines without PDE3B respond 0.72× as strongly (z diff +1.69); strongest at Digitoxin 5 µM: 0.55x vs 0.33x (z diff +3.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4; target measured in part of the lines; artifact flags |
| [[PDE3B]] | B | PDE3B activity raises SLC12A2-DT's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without PDE3B | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[TDRD3]] | C | TDRD3's natural level strengthens SLC12A2-DT's drug response | TDRD3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.01; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.3, 7.2); signed map (24.4, -33.1). **Vector** length 88.0, 26.9% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -10.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SLC12A2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q23.3 — chr5:127,939,152-128,083,172 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ33630; previously LINC01184 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49565) · Entrez [644873](https://www.ncbi.nlm.nih.gov/gene/644873) · Ensembl [ENSG00000245937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245937)

## Data

Gene col 14450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14450); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14450]; `tensor/DDL_lfc|DDL_z.npy` [14450]; `embed/gene_vectors.npy` [14450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14450 or target_col == 14450). Every well: [[SLC12A2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC12A2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
