---
symbol: "C2CD5"
type: "gene"
col: 3274
ensembl_id: "ENSG00000111731"
name: "C2 calcium dependent domain containing 5"
location: "12p12.1"
module: 28
arm: "+"
pooled_cpm: 60.73
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 37
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# C2CD5

*C2 calcium dependent domain containing 5* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 1.29× (z +3.7, q 0.059, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.349× (z -15.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBN]] (+0.72, fdr 7e-06), [[HNRNPD]] (+0.68, fdr 7e-06), [[NELFCD]] (+0.66, fdr 1e-05); moves opposite to [[RABGEF1]] (-0.64, fdr 1e-05), [[TPTEP2-CSNK1E]] (-0.63, fdr 7e-06), [[TMED7-TICAM2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FOXRED2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.059 | 24/48 (SW 900, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.059 | 24/48 (SW 900, A498, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.059 | 24/48 (KATO III, SW 900, …) | rises with dose |  |
| [[Rifaximin (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.059 | 23/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.059 | 19/48 (MIA PaCa-2, LS 180, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.078 | 19/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.081 | 17/48 (CFPAC-1, A549, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.085 | 16/48 (KATO III, SNU-423, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.25× | +3.2 | 0.10 | 17/47 (LoVo, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.12 | 21/48 (NCI-H1792, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.349×** | -15.2 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.360×** | -14.7 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.361×** | -14.7 | 0e+00 | 46/48 (SW480, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.410×** | -12.9 | 1e-35 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.433×** | -12.1 | 2e-31 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -11.8 | 4e-30 | 45/48 (A549, A498, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.615×** | -7.0 | 2e-10 | 40/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.613×** | -6.6 | 2e-09 | 35/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.633×** | -6.6 | 3e-09 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -6.2 | 4e-08 | 36/48 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -5.1 | 1e-05 | 30/48 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.694×** | -5.0 | 2e-05 | 28/47 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -4.6 | 2e-04 | 26/50 (Panc 03.27, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -4.4 | 5e-04 | 26/47 (CHP-212, RKO, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -4.3 | 5e-04 | 25/49 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.742×** | -4.3 | 6e-04 | 29/48 (AN3 CA, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.820×** | -4.0 | 0.002 | 29/49 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.763×** | -3.8 | 0.003 | 26/47 (SNU-423, MIA PaCa-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 142 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -16.1) |
| [[PANC-1 (line)]] | alt | 62.8 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -18.5) |
| [[A549 (line)]] | wt | 80.4 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -17.2) |
| [[HOP62 (line)]] | alt | 44.8 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.212× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 32.8 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.248× (z -11.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -11.3) |
| [[SW480 (line)]] | alt | 196 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -22.3) |
| [[A-172 (line)]] | wt | 41.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -10.1) |
| [[A-427 (line)]] | wt | 95.5 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.437× (z -9.5) |
| [[LoVo (line)]] | wt | 56.0 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.292× (z -11.8) |
| [[SNU-423 (line)]] | alt | 38.4 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.237× (z -12.3) |
| [[SW 900 (line)]] | alt | 79.7 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -12.7) |
| [[HT-29 (line)]] | alt | 44.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -10.6) |
| [[LS 180 (line)]] | wt | 53.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 50.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 77.8 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.260× (z -12.1) |
| [[RKO (line)]] | wt | 57.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.248× (z -10.1) |
| [[A498 (line)]] | wt | 40.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -14.4) |
| [[C32 (line)]] | wt | 42.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.2) |
| [[COLO 205 (line)]] | alt | 59.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -12.0) |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 69.6 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.188× (z -12.4) |
| [[SNU-1 (line)]] | wt | 59.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.254× (z -9.4) |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -11.3) |
| [[AN3 CA (line)]] | alt | 75.6 | 0 | 2 | — | [[Decitabine (drug)]] 0.5 µM 0.215× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0722× (z -14.5) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 88.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 51.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.378× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.395× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 54.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.368× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 43.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.170× (z -11.7) |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Vilanterol (drug)]] 0.5 µM 0.203× (z -11.9) |
| [[SW48 (line)]] | wt | 65.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -11.4) |
| [[C-33 A (line)]] | alt | 78.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.351× (z -8.6) |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -9.2) ⚠ toxic |
| [[H4 (line)]] | wt | 39.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.166× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 58.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.417× (z -9.3) |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -8.7) |
| [[J82 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.370× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 54.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.312× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 52.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.248× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 78.9 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.160× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 34.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.290× (z -9.1) |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0527× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBN]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[HNRNPD]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[NELFCD]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[DHX9]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SLX4IP]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PTBP2]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[FAM98B]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[MDM1]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[HNRNPR]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[DCLRE1A]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TUBGCP3]] | +0.61 | +0.43 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | -0.64 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.63 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[TMED7-TICAM2]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[CDC20-DT]] | -0.60 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[MROH1]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PHKG1]] | -0.60 | -0.40 / -0.64 | both halves | 4e-05 |  |
| [[ZNF778]] | -0.59 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[C9orf153]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TPT1-AS1]] | -0.58 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[TICAM2]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[SWT1]] | -0.58 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TMEM165]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXRED2]] | C | FOXRED2 activity strengthens C2CD5's drug response | lines that do not express FOXRED2 (3) vs lines expressing it (45) | the lines without FOXRED2 respond 0.63× as strongly (z diff +2.32); strongest at Digitoxin 5 µM: 0.56x vs 0.33x (z diff +3.7) | 0.021 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.8, 1.4); signed map (6.8, -38.1). **Vector** length 84.8, 23.6% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.3 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.1 | -3.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.1 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.9 | -14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -11.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | -12.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | C2 calcium dependent domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:22,448,583-22,544,546 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDP138; previously KIAA0528 |
| Gene groups (HGNC) | C2 domain containing |
| Reactome | 3 pathways, smallest: Translocation of SLC2A4 (GLUT4) to the plasma membrane; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YS7](https://www.uniprot.org/uniprotkb/Q86YS7) (C2 domain-containing protein 5):

> Required for insulin-stimulated glucose transport and glucose transporter SLC2A4/GLUT4 translocation from intracellular glucose storage vesicle (GSV) to the plasma membrane (PM) in adipocytes. Binds phospholipid membranes in a calcium-dependent manner and is necessary for the optimal membrane fusion between SLC2A4/GLUT4 GSV and the PM.

**Summary**, from NCBI Gene [9847](https://www.ncbi.nlm.nih.gov/gene/9847):

> Enables calcium ion binding activity and calcium-dependent phospholipid binding activity. Involved in several processes, including insulin receptor signaling pathway; positive regulation of protein targeting to membrane; and positive regulation of vesicle fusion. Located in several cellular components, including cell cortex; cytoplasmic vesicle membrane; and ruffle membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29062) · Entrez [9847](https://www.ncbi.nlm.nih.gov/gene/9847) · UniProt [Q86YS7](https://www.uniprot.org/uniprotkb/Q86YS7) · Ensembl [ENSG00000111731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111731)

## Data

Gene col 3274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3274); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3274]; `tensor/DDL_lfc|DDL_z.npy` [3274]; `embed/gene_vectors.npy` [3274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3274 or target_col == 3274). Every well: [[C2CD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2CD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
