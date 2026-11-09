---
symbol: "CASP10"
type: "gene"
col: 33
ensembl_id: "ENSG00000003400"
name: "caspase 10"
location: "2q33.1"
module: 70
arm: "+"
pooled_cpm: 21.62
n_lines_expressing: 31
n_dd_up: 27
n_dd_down: 26
n_dd_up_clean: 21
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 53
direction_downstream: 72
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# CASP10

*caspase 10* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +7.6, q 2e-11, up in 17 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.436× (z -9.9, q 3e-20, down in 23 of 26 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.545× (z -7.2, q 6e-11, down in 21 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFB]] (+0.75, fdr 7e-06), [[TNFSF10]] (+0.73, fdr 7e-06), [[TLR3]] (+0.72, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[OASL]] → it (grade B ⚠); 72 go from it, the strongest it → [[GBP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 33.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.6 | 2e-11 | 17/29 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.1 | 3e-07 | 15/29 (J82, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +5.6 | 4e-06 | 21/28 (AsPC-1, LoVo, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +5.4 | 7e-06 | 19/29 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +5.2 | 2e-05 | 15/29 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.2 | 2e-05 | 17/28 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.37×** | +5.1 | 2e-05 | 18/28 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 3e-05 | 20/28 (LoVo, AsPC-1, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.48×** | +5.0 | 3e-05 | 18/29 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 4e-05 | 15/28 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +5.0 | 4e-05 | 17/29 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 1e-04 | 16/29 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.6 | 2e-04 | 15/28 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.44×** | +4.3 | 6e-04 | 14/28 (SW1417, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +4.2 | 9e-04 | 14/28 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.001 | 15/28 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 13/29 (A498, SW1417, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 33.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.436×** | -9.9 | 3e-20 | 23/26 (SW 900, CFPAC-1, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.441×** | -9.8 | 5e-20 | 22/28 (SW1417, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.490×** | -8.2 | 6e-14 | 22/24 (NCI-H1792, SW 900, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.486×** | -8.0 | 3e-13 | 19/24 (A498, SW 900, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.545×** | -7.2 | 6e-11 | 21/28 (HCT15, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.606×** | -6.0 | 2e-07 | 19/28 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.608×** | -5.9 | 2e-07 | 20/28 (SNU-423, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.612×** | -5.9 | 3e-07 | 17/28 (SW1417, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.657×** | -4.8 | 9e-05 | 17/29 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.763×** | -4.6 | 3e-04 | 18/29 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.673×** | -4.6 | 3e-04 | 15/27 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.768×** | -4.5 | 3e-04 | 16/28 (LoVo, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.688×** | -4.5 | 3e-04 | 17/28 (BT-474, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.689×** | -4.4 | 4e-04 | 17/28 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.006 | 15/28 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.733×** | -3.7 | 0.007 | 12/28 (LoVo, KATO III, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.579×** | -3.4 | 0.020 | 9/28 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.760×** | -3.3 | 0.028 | 12/28 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.660×** | -3.2 | 0.032 | 12/28 (MIA PaCa-2, SW 900, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.035 | 13/28 (LoVo, COLO 205, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.784×** | -2.9 | 0.077 | 11/28 (LoVo, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 33. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 60.1 | 1 (1 ⚠) | 8 (4 ⚠) | [[Trametinib (drug)]] 5 µM 3.03× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.202× (z -12.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.333× (z -12.0) |
| [[SW 900 (line)]] | alt | 47.7 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0667× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.181× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 49.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.277× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 57.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0479× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 54.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.191× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 67.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 13.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +11.3) | — |
| [[A498 (line)]] | wt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 24.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 51.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 32.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[BT-474 (line)]] | alt | 9.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0907× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.153× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 5.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 33), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFB]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[TNFSF10]] | +0.73 | +0.68 / +0.76 | both halves | 7e-06 | pathway: Death Receptor Signaling; STRING 917 |
| [[TLR3]] | +0.72 | +0.63 / +0.69 | both halves | 7e-06 | STRING 402 |
| [[TRIM38]] | +0.71 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[APOL1]] | +0.70 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[PDZK1IP1]] | +0.69 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[DUOX2]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SLC34A2]] | +0.68 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TMEM140]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[RBM47]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 36, C 17. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | B | OASL activity raises CASP10's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.38× lower at baseline in the lines without OASL | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises CASP10's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without GBP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IFI27]] | B | IFI27 activity raises CASP10's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.81× lower at baseline in the lines without IFI27 | 0.004 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[FRK]] | B | FRK activity raises CASP10's level | lines that do not express FRK (22) vs lines expressing it (28) | 3.32× lower at baseline in the lines without FRK | 0.004 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[TOP2A]] | B | TOP2A activity lowers CASP10's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises CASP10's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.32× lower at baseline in the lines without ELF3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[IFIT3]] | B | IFIT3 activity raises CASP10's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.70× lower at baseline in the lines without IFIT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[GBP2]] | B | GBP2 activity raises CASP10's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.83× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[DUOX2]] | B | DUOX2 activity raises CASP10's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without DUOX2 | 0.011 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[TRANK1]] | B | TRANK1 activity raises CASP10's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 3.92× lower at baseline in the lines without TRANK1 | 0.012 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises CASP10's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.43× lower at baseline in the lines without CTSS | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[IFIT2]] | B | IFIT2 activity raises CASP10's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.89× lower at baseline in the lines without IFIT2 | 0.018 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |

### Downstream of this gene

*72 arrows, 72 of them with an alert ⚠; grade A 0, B 56, C 16. Shown: the 12 strongest; 60 more arrows (60 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP1]] | B | CASP10 activity raises GBP1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 3.24× lower at baseline in the lines without CASP10 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IFI44]] | B | CASP10 activity raises IFI44's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without CASP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[GBP3]] | B | CASP10 activity raises GBP3's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 3.12× lower at baseline in the lines without CASP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[APOL6]] | B | CASP10 activity raises APOL6's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without CASP10 | 0.004 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IFIT3]] | B | CASP10 activity raises IFIT3's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.50× lower at baseline in the lines without CASP10 | 0.005 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[B2M]] | B | CASP10 activity raises B2M's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without CASP10 | 0.005 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[OASL]] | B | CASP10 activity raises OASL's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.45× lower at baseline in the lines without CASP10 | 0.008 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[TRANK1]] | B | CASP10 activity raises TRANK1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without CASP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IFIT2]] | B | CASP10 activity raises IFIT2's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without CASP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[SAMD9L]] | B | CASP10 activity raises SAMD9L's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without CASP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[CTSS]] | B | CASP10 activity raises CTSS's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.59× lower at baseline in the lines without CASP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[PSMB10]] | B | CASP10 activity raises PSMB10's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.54× lower at baseline in the lines without CASP10 | 0.010 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.5, 50.4); signed map (61.3, 28.9). **Vector** length 97.3, 30.3% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.51 to 25); *Antigen processing-Cross presentation* (reactome, mean cos +0.54 to 14); *Interferon gamma signaling* (reactome, mean cos +0.53 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +4.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.2 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.9 | -3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.2 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.2 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | caspase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,182,872-201,229,428 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCH4, FLICE-2 |
| Gene groups (HGNC) | Caspases; Death effector domain containing; Death inducing signaling complex |
| Hallmark sets | COMPLEMENT |
| Reactome | 9 pathways, smallest: FasL/ CD95L signaling; TRAIL  signaling; TP53 Regulates Transcription of Caspase Activators and Caspases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92851](https://www.uniprot.org/uniprotkb/Q92851) (Caspase-10):

> Involved in the activation cascade of caspases responsible for apoptosis execution. Recruited to both Fas- and TNFR-1 receptors in a FADD dependent manner. May participate in the granzyme B apoptotic pathways. Cleaves and activates effector caspases CASP3, CASP4, CASP6, CASP7, CASP8 and CASP9. Hydrolyzes the small- molecule substrates, Tyr-Val-Ala-Asp-|-AMC and Asp-Glu-Val-Asp-|-AMC.; Isoform 7 can enhance NF-kappaB activity but promotes only slight apoptosis.; Isoform C is proteolytically …

**Summary**, from NCBI Gene [843](https://www.ncbi.nlm.nih.gov/gene/843):

> This gene encodes a protein which is a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes which undergo proteolytic processing at conserved aspartic residues to produce two subunits, large and small, that dimerize to form the active enzyme. This protein cleaves and activates caspases 3 and 7, and the protein itself is processed by caspase 8. …

**Accessions** — [HGNC:1500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1500) · Entrez [843](https://www.ncbi.nlm.nih.gov/gene/843) · UniProt [Q92851](https://www.uniprot.org/uniprotkb/Q92851) · Ensembl [ENSG00000003400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003400)

## Data

Gene col 33: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 33); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 33, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 33]; `tensor/DDL_lfc|DDL_z.npy` [33]; `embed/gene_vectors.npy` [33]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 33 or target_col == 33). Every well: [[CASP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
