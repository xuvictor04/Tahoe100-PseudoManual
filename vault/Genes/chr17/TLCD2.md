---
symbol: "TLCD2"
type: "gene"
col: 11696
ensembl_id: "ENSG00000185561"
name: "TLC domain containing 2"
location: "17p13.3"
module: 133
arm: "+"
pooled_cpm: 18.8
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 22
n_dd_up_clean: 20
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# TLCD2

*TLC domain containing 2* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.19× (z +9.7, q 1e-19, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.445× (z -10.1, q 4e-21, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR22HG]] (+0.60, fdr 1e-05, ⚠ same locus), [[MVP-DT]] (+0.58, fdr 2e-05), [[CELF6]] (+0.57, fdr 1e-05), [[MAPK6]] (+0.56, fdr 2e-05); moves opposite to [[XPO7]] (-0.48, fdr 3e-05), [[RTTN]] (-0.47, fdr 6e-05), [[NCAPD3]] (-0.47, fdr 6e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SYT5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +9.7 | 1e-19 | 35/47 (C32, NCI-H23, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.6 | 8e-12 | 24/39 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.0 | 7e-10 | 12/25 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.8 | 2e-09 | 28/46 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.2 | 2e-05 | 15/32 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 3e-05 | 21/48 (A-427, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.33×** | +4.9 | 6e-05 | 25/48 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 3e-04 | 19/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.44×** | +4.5 | 4e-04 | 16/48 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +4.5 | 4e-04 | 20/48 (PANC-1, KATO III, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +4.5 | 4e-04 | 23/46 (A-427, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +4.3 | 1e-03 | 21/46 (AsPC-1, KATO III, …) | rises with dose | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 15/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.002 | 17/47 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.002 | 17/47 (NCI-H2030, PANC-1, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 20/46 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.013 | 9/47 (A-427, C-33 A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.013 | 13/48 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.018 | 12/47 (C-33 A, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.021 | 13/47 (KATO III, SW480, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.445×** | -10.1 | 4e-21 | 34/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.481×** | -9.1 | 2e-17 | 33/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.512×** | -8.3 | 2e-14 | 29/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.545×** | -7.6 | 5e-12 | 29/46 (HT-29, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.606×** | -6.0 | 2e-07 | 23/46 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.410×** | -5.8 | 6e-07 | 24/45 (COLO 205, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.648×** | -5.4 | 5e-06 | 21/46 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -5.1 | 3e-05 | 22/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.674×** | -4.9 | 6e-05 | 22/45 (PANC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.676×** | -4.9 | 6e-05 | 21/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.696×** | -4.5 | 3e-04 | 21/48 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.508×** | -4.4 | 5e-04 | 17/46 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.693×** | -4.4 | 5e-04 | 17/43 (J82, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.517×** | -4.3 | 7e-04 | 21/46 (HS-578T, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.696×** | -4.2 | 0.001 | 15/45 (SW1417, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Folic acid (drug)]] 5 µM |  | **0.821×** | -3.5 | 0.016 | 11/48 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.035 | 11/46 (LS 180, NCI-H460, …) | two highest doses | position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **0.777×** | -3.1 | 0.049 | 8/46 (HCT15, AN3 CA, …) | inconsistent across doses |  |
| [[Salicylic acid (drug)]] 5 µM |  | 0.845× | -3.0 | 0.074 | 8/48 (A498, HEC-1-A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -3.0 | 0.077 | 12/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.849× | -2.9 | 0.088 | 6/48 (MIA PaCa-2, A498, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.2 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -14.5) |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 21.9 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.131× (z -10.6) |
| [[COLO 205 (line)]] | alt | 71.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.7) |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 9.55 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 9.92× (z +9.0) | — |
| [[LoVo (line)]] | wt | 25.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -8.9) |
| [[A498 (line)]] | wt | 17.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 26.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.14× (z +8.7) | — |
| [[KATO III (line)]] | alt | 37.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 16.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +20.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.87× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 7.83 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +10.0) | [[Silodosin (drug)]] 5 µM 0.0873× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[LOX-IMVI (line)]] | wt | 21.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR22HG]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 | ⚠ same locus (1.1 kb, same strand: neighbours can correlate without regulation) |
| [[MVP-DT]] | +0.58 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[CELF6]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[MAPK6]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SGK2]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DMGDH]] | +0.54 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[C5AR1]] | +0.54 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ALOX12-AS1]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SLC23A3]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ASS1]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP30]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ADM2]] | +0.53 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ZCWPW2]] | +0.53 | +0.56 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPO7]] | -0.48 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RTTN]] | -0.47 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[NCAPD3]] | -0.47 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[RBL1]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[DENND6A]] | -0.47 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[GINS1]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ORC5]] | -0.46 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[TFB1M]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[COA1]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CASP2]] | -0.46 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[UBE2T]] | -0.46 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[MCM6]] | -0.45 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT5]] | B | SYT5 activity raises TLCD2's level | lines that do not express SYT5 (10) vs lines expressing it (40) | 1.46× lower at baseline in the lines without SYT5 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ACVR2A; also absent: B4GALNT1, LARP6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.8, 18.0); signed map (21.1, -1.5). **Vector** length 102, 24.9% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +4.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -10.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -2.3 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.3 | -6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | +3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | TLC domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,702,816-1,710,377 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TLC domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NGC4](https://www.uniprot.org/uniprotkb/A6NGC4) (TLC domain-containing protein 2):

> Regulates the composition and fluidity of the plasma membrane. Inhibits the incorporation of membrane-fluidizing phospholipids containing omega-3 long-chain polyunsaturated fatty acids (LCPUFA) and thereby promotes membrane rigidity. Does not appear to have any effect on LCPUFA synthesis.

**Summary**, from NCBI Gene [727910](https://www.ncbi.nlm.nih.gov/gene/727910):

> Involved in several processes, including membrane assembly; phospholipid homeostasis; and regulation of membrane lipid distribution. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33522) · Entrez [727910](https://www.ncbi.nlm.nih.gov/gene/727910) · UniProt [A6NGC4](https://www.uniprot.org/uniprotkb/A6NGC4) · Ensembl [ENSG00000185561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185561)

## Data

Gene col 11696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11696); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11696]; `tensor/DDL_lfc|DDL_z.npy` [11696]; `embed/gene_vectors.npy` [11696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11696 or target_col == 11696). Every well: [[TLCD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLCD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
