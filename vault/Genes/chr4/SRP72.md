---
symbol: "SRP72"
type: "gene"
col: 10525
ensembl_id: "ENSG00000174780"
name: "signal recognition particle 72"
location: "4q12"
module: 42
arm: "+"
pooled_cpm: 148.51
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SRP72

*signal recognition particle 72* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.05× (z +13.1, q 1e-36, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.71× (z +5.1, q 3e-05, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.773× (z -6.7, q 1e-08, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USO1]] (+0.76, fdr 7e-06), [[DDX1]] (+0.67, fdr 7e-06), [[EIF2A]] (+0.65, fdr 7e-06); moves opposite to [[SMURF1]] (-0.54, fdr 3e-05), [[TMEM50A]] (-0.53, fdr 3e-05), [[PMEL]] (-0.51, fdr 5e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +13.1 | 1e-36 | 47/49 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +12.8 | 5e-35 | 42/44 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +8.4 | 9e-15 | 37/45 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.71×** | +5.1 | 3e-05 | 40/48 (SW480, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.32×** | +5.1 | 3e-05 | 36/48 (NCI-H1573, COLO 205, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.4 | 0.001 | 31/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.26×** | +4.0 | 0.005 | 25/47 (NCI-H1792, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.007 | 28/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.47×** | +3.7 | 0.012 | 29/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.012 | 28/45 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.23×** | +3.7 | 0.012 | 24/48 (NCI-H1792, COLO 205, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **1.22×** | +3.6 | 0.014 | 26/48 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.22×** | +3.6 | 0.014 | 21/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.015 | 29/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.020 | 25/48 (C32, Panc 03.27, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.021 | 24/48 (AsPC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.024 | 30/48 (RKO, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.039 | 23/48 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.046 | 15/49 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.073 | 22/48 (SW1417, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -6.7 | 1e-08 | 32/49 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.749×** | -5.3 | 3e-05 | 34/48 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.761×** | -5.0 | 9e-05 | 34/48 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.779×** | -4.6 | 5e-04 | 30/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -4.6 | 5e-04 | 22/48 (SW1417, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.795×** | -4.1 | 0.005 | 28/48 (A498, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.009 | 29/47 (AsPC-1, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.825×** | -3.5 | 0.028 | 26/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.828×** | -3.5 | 0.032 | 22/47 (C32, H4, …) | rises with dose |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | 0.836× | -3.3 | 0.053 | 21/47 (BT-474, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.869× | -3.2 | 0.063 | 14/48 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.842× | -3.2 | 0.072 | 15/48 (NCI-H2347, RKO, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.840× | -3.1 | 0.084 | 20/47 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 237 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.39× (z +13.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 134 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +17.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 162 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +11.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -11.5) |
| [[A549 (line)]] | wt | 115 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +12.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 112 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +13.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +12.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 126 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +11.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 147 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 175 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +19.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 133 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +13.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 123 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +15.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 182 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.0) |
| [[HOP62 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +12.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 133 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 311 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 183 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +8.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +9.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HCT15 (line)]] | alt | 244 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 119 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +8.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 144 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -8.8) |
| [[LS 180 (line)]] | wt | 154 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -10.9) |
| [[RKO (line)]] | wt | 180 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -13.2) |
| [[SHP-77 (line)]] | alt | 230 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM 0.185× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 110 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.510× (z -8.5) |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 95.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 146 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USO1]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[DDX1]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[EIF2A]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[EPRS1]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 | STRING 556 |
| [[LARS1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MTDH]] | +0.63 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[RUSF1]] | +0.60 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[UBE2J1]] | +0.59 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[GNL2]] | +0.59 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[RSL24D1]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A46]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HSPA9]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Protein localization |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMURF1]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TMEM50A]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PMEL]] | -0.51 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[LUZP1]] | -0.51 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[GATAD2B]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[COPS9]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[NDUFB1]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[ST3GAL2]] | -0.49 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[CYBA]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[BLOC1S1]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[DCAF15]] | -0.48 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[HMGB1P5]] ⚠ | -0.48 | -0.46 / -0.37 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SRP72's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.388). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.3, -19.3); signed map (-58.9, 11.2). **Vector** length 101, 33.9% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.3 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +13.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.8 | +2.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -4.0 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -1.7 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | signal recognition particle 72 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,467,617-56,503,681 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Signal recognition particle |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O76094](https://www.uniprot.org/uniprotkb/O76094) (Signal recognition particle subunit SRP72):

> Component of the signal recognition particle (SRP) complex, a ribonucleoprotein complex that mediates the cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER). The SRP complex interacts with the signal sequence in nascent secretory and membrane proteins and directs them to the membrane of the ER. The SRP complex targets the ribosome-nascent chain complex to the SRP receptor (SR), which is anchored in the ER, where SR compaction and GTPase rearrangement …

**Summary**, from NCBI Gene [6731](https://www.ncbi.nlm.nih.gov/gene/6731):

> This gene encodes the 72 kDa subunit of the signal recognition particle (SRP), a ribonucleoprotein complex that mediates the targeting of secretory proteins to the endoplasmic reticulum (ER). The SRP complex consists of a 7S RNA and 6 protein subunits: SRP9, SRP14, SRP19, SRP54, SRP68, and SRP72, that are bound to the 7S RNA as monomers or heterodimers. SRP has at least 3 distinct functions that can be associated with the protein subunits: signal recognition, translational arrest, and ER …

**Accessions** — [HGNC:11303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11303) · Entrez [6731](https://www.ncbi.nlm.nih.gov/gene/6731) · UniProt [O76094](https://www.uniprot.org/uniprotkb/O76094) · Ensembl [ENSG00000174780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174780)

## Data

Gene col 10525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10525); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10525]; `tensor/DDL_lfc|DDL_z.npy` [10525]; `embed/gene_vectors.npy` [10525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10525 or target_col == 10525). Every well: [[SRP72 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRP72.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
