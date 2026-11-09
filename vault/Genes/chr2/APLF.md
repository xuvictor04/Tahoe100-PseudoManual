---
symbol: "APLF"
type: "gene"
col: 9828
ensembl_id: "ENSG00000169621"
name: "aprataxin and PNKP like factor"
location: "2p13.3"
module: 68
arm: "+"
pooled_cpm: 28.84
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 20
n_dd_up_clean: 23
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# APLF

*aprataxin and PNKP like factor* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.34× (z +21.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.388× (z -11.6, q 2e-28, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRCC1]] (+0.75, fdr 7e-06), [[ZC3H6]] (+0.73, fdr 7e-06), [[PPP1R12A-AS2]] (+0.73, fdr 2e-05); moves opposite to [[PHKA2]] (-0.69, fdr 1e-05), [[SHQ1]] (-0.67, fdr 3e-05), [[GRB2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SOCS2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.34×** | +21.0 | 0e+00 | 46/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.02×** | +13.1 | 2e-36 | 46/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +12.4 | 4e-33 | 39/47 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +9.9 | 6e-21 | 40/46 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.6 | 3e-12 | 31/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +6.3 | 3e-08 | 32/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +6.1 | 1e-07 | 28/47 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +4.6 | 3e-04 | 25/47 (A498, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.005 | 24/47 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.82×** | +3.8 | 0.007 | 22/47 (A-427, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.007 | 18/47 (SW480, NCI-H2030, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.007 | 20/46 (NCI-H23, hTERT-HPNE, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.007 | 23/47 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.007 | 25/47 (NCI-H23, SW48, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.011 | 19/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9828.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.388×** | -11.6 | 2e-28 | 41/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.479×** | -9.0 | 5e-17 | 39/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -7.9 | 4e-13 | 36/47 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.567×** | -7.0 | 5e-10 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.571×** | -6.9 | 7e-10 | 31/46 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.554×** | -6.8 | 8e-10 | 36/47 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.354×** | -6.7 | 2e-09 | 33/47 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.365×** | -6.5 | 7e-09 | 32/47 (SNU-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.602×** | -6.2 | 3e-08 | 31/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.383×** | -6.2 | 4e-08 | 28/40 (PANC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -5.8 | 3e-07 | 29/46 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -5.6 | 1e-06 | 30/47 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.473×** | -4.8 | 7e-05 | 26/47 (SNU-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.676×** | -4.8 | 7e-05 | 29/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.698×** | -4.4 | 4e-04 | 26/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.618×** | -4.2 | 9e-04 | 22/47 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.632×** | -4.0 | 0.002 | 22/47 (PANC-1, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.580×** | -3.5 | 0.015 | 17/46 (SW48, C32, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.754×** | -3.3 | 0.027 | 14/47 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.775×** | -3.1 | 0.050 | 20/47 (NCI-H2030, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.0 | 3 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +23.5) | [[Digitoxin (drug)]] 0.5 µM 0.157× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 53.1 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.387× (z -8.5) |
| [[SW480 (line)]] | alt | 33.4 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.5) | [[Digitoxin (drug)]] 0.5 µM 0.196× (z -15.0) |
| [[A-172 (line)]] | wt | 52.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 49.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.179× (z -9.8) |
| [[LoVo (line)]] | wt | 16.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.94× (z +19.4) | — |
| [[LOX-IMVI (line)]] | wt | 40.5 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.294× (z -9.0) |
| [[SNU-1 (line)]] | wt | 90.0 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0544× (z -17.0) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.0388× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 32.0 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.0) | [[Ixazomib citrate (drug)]] 5 µM 0.323× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 58.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 15.2 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 58.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 79.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.3) | [[Ixazomib citrate (drug)]] 5 µM 0.388× (z -9.2) |
| [[A498 (line)]] | wt | 23.7 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.96× (z +11.9) | — |
| [[A549 (line)]] | wt | 39.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -9.3) |
| [[AN3 CA (line)]] | alt | 45.6 | 0 | 2 (1 ⚠) | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0737× (z -11.1) |
| [[BT-474 (line)]] | alt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +15.6) | — |
| [[CHP-212 (line)]] | wt | 31.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +9.0) | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0654× (z -9.9) |
| [[HOP62 (line)]] | alt | 35.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +19.0) | — |
| [[Hs 766T (line)]] | wt | 39.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +14.5) | [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -9.0) |
| [[LS 180 (line)]] | wt | 18.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.205× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 32.7 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.12× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.235× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 8.35 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +15.0) | — |
| [[RKO (line)]] | wt | 18.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 28.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 26.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +13.8) | — |
| [[SW48 (line)]] | wt | 29.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +14.6) | — |
| [[AsPC-1 (line)]] | alt | 9.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +10.7) | — |
| [[C32 (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +8.9) | — |
| [[J82 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 33.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRCC1]] | +0.75 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[ZC3H6]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.73 | +0.83 / +0.48 | both halves | 2e-05 |  |
| [[RFX3-DT]] | +0.73 | +0.84 / +0.38 | both halves | 6e-05 |  |
| [[CGGBP1]] | +0.72 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[HHLA3]] | +0.71 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.71 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SEPTIN7-DT]] | +0.71 | +0.80 / +0.43 | both halves | 3e-05 |  |
| [[DNAI4]] | +0.71 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[AK9]] | +0.71 | +0.80 / +0.44 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | +0.69 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | +0.69 | +0.79 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKA2]] | -0.69 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.67 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[GRB2]] | -0.66 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.66 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.65 | -0.75 / -0.33 | both halves | 1e-04 |  |
| [[GTF2E2]] | -0.63 | -0.69 / -0.39 | both halves | 6e-05 |  |
| [[STRAP]] | -0.63 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[AP1S1]] | -0.62 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[YIPF1]] | -0.62 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[L2HGDH]] | -0.62 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[TAF5L]] | -0.62 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[USP35]] | -0.61 | -0.65 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises APLF's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without SOCS2-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[SOCS2]] | B | SOCS2 activity raises APLF's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without SOCS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[DRAM1]] | B | DRAM1 activity raises APLF's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without DRAM1 | 0.028 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[EMP3]] | B | EMP3 activity raises APLF's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without EMP3 | 0.067 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[ZMAT1]] | B | ZMAT1 activity raises APLF's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.46× lower at baseline in the lines without ZMAT1 | 0.097 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B |
| [[RFX3-DT]] | C | RFX3-DT activity raises APLF's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without RFX3-DT | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.797). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.2, 12.1); signed map (21.4, -14.0). **Vector** length 116, 35.4% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +12.4 | +21.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.9 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.7 | +9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.0 | -11.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.7 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | +1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.7 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.3 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -6.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | aprataxin and PNKP like factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:68,467,572-68,655,862 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC47799, Xip1, ZCCHH1; previously C2orf13 |
| Gene groups (HGNC) | Zinc fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IW19](https://www.uniprot.org/uniprotkb/Q8IW19) (Aprataxin and PNK-like factor):

> Histone chaperone involved in single-strand and double-strand DNA break repair. Recruited to sites of DNA damage through interaction with branched poly-ADP-ribose chains, a polymeric post-translational modification synthesized transiently at sites of chromosomal damage to accelerate DNA strand break repair reactions. Following recruitment to DNA damage sites, acts as a histone chaperone that mediates histone eviction during DNA repair and promotes recruitment of histone variant MACROH2A1. Also …

**Summary**, from NCBI Gene [200558](https://www.ncbi.nlm.nih.gov/gene/200558):

> Enables several functions, including nuclease activity; poly-ADP-D-ribose binding activity; and protein folding chaperone. Involved in DNA repair; DNA repair-dependent chromatin remodeling; and protein localization to chromatin. Located in nucleoplasm. Is active in site of double-strand break. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28724) · Entrez [200558](https://www.ncbi.nlm.nih.gov/gene/200558) · UniProt [Q8IW19](https://www.uniprot.org/uniprotkb/Q8IW19) · Ensembl [ENSG00000169621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169621)

## Data

Gene col 9828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9828); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9828]; `tensor/DDL_lfc|DDL_z.npy` [9828]; `embed/gene_vectors.npy` [9828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9828 or target_col == 9828). Every well: [[APLF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APLF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
