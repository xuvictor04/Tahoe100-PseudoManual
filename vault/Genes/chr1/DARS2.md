---
symbol: "DARS2"
type: "gene"
col: 3927
ensembl_id: "ENSG00000117593"
name: "aspartyl-tRNA synthetase 2, mitochondrial"
location: "1q25.1"
module: 24
arm: "-"
pooled_cpm: 16.02
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DARS2

*aspartyl-tRNA synthetase 2, mitochondrial* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.86× (z +20.7, q 0e+00, up in 37 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +7.2, q 1e-10, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.597× (z -7.9, q 2e-12, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSME3]] (+0.72, fdr 7e-06), [[NUP155]] (+0.71, fdr 7e-06), [[WDR77]] (+0.71, fdr 1e-05); moves opposite to [[SIRT2]] (-0.76, fdr 7e-06), [[LAMTOR5]] (-0.73, fdr 7e-06), [[COMMD6]] (-0.73, fdr 7e-06).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SIGIRR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.86×** | +20.7 | 0e+00 | 37/38 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +19.7 | 0e+00 | 25/25 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +14.9 | 0e+00 | 31/33 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +7.2 | 1e-10 | 23/48 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.5 | 8e-09 | 25/48 (A-172, SNU-423, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.9 | 9e-05 | 16/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +4.6 | 4e-04 | 15/46 (SNU-423, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +3.5 | 0.027 | 15/46 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.027 | 10/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Delamanid (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.028 | 7/47 (BT-474, SNU-423, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.4 | 0.028 | 13/47 (PANC-1, BT-474, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.028 | 11/47 (SNU-423, LoVo, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.038 | 9/48 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.24×** | +3.2 | 0.064 | 14/42 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.087 | 8/46 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.095 | 11/47 (HEC-1-A, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.597×** | -7.9 | 2e-12 | 27/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -6.7 | 4e-09 | 23/46 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.672×** | -6.1 | 2e-07 | 23/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.675×** | -6.0 | 3e-07 | 23/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.696×** | -5.6 | 3e-06 | 20/47 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.701×** | -5.4 | 5e-06 | 16/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -5.3 | 1e-05 | 23/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.792×** | -5.0 | 3e-05 | 19/48 (LS 180, KATO III, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.754×** | -4.1 | 0.002 | 15/46 (PANC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.775×** | -3.9 | 0.006 | 17/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.021 | 13/47 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.809×** | -3.2 | 0.058 | 9/47 (A498, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.6 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.312× (z -11.8) |
| [[A-427 (line)]] | wt | 39.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.1) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.266× (z -12.3) |
| [[SW480 (line)]] | alt | 18.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +11.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.335× (z -9.3) |
| [[A498 (line)]] | wt | 13.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.63× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 23.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.23× (z +10.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.217× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.56× (z +8.7) ⚠ toxic; transcription drop | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.153× (z -11.3) ⚠ toxic |
| [[A549 (line)]] | wt | 16.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.07× (z +12.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 9.84 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +9.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.61× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 9.27 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.64× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 12.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.88× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.0929× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 9.04 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.83× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -14.9) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.330× (z -8.7) |
| [[BT-474 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -13.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.25 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0988× (z -10.1) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +10.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0737× (z -9.6) |
| [[J82 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 25.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[SHP-77 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[NUP155]] | +0.71 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[WDR77]] | +0.71 | +0.57 / +0.79 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ADAT1]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[IPO5]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[CCT7]] | +0.71 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.70 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[NUP205]] | +0.70 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[CEP41]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[BTBD1]] | +0.69 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.76 | -0.60 / -0.72 | both halves | 7e-06 |  |
| [[LAMTOR5]] | -0.73 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.73 | -0.67 / -0.67 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | -0.72 | -0.58 / -0.69 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[GABARAPL2]] | -0.71 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.71 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[RNF114]] | -0.71 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[LIN7B]] | -0.70 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[RPL18]] ⚠ | -0.70 | -0.47 / -0.71 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | -0.69 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | -0.69 | -0.61 / -0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.69 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[SAT2]] | -0.69 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[TOMM7]] | -0.69 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[ATP5MJ]] | -0.68 | -0.59 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIGIRR]] | B | SIGIRR activity lowers DARS2's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.24× higher at baseline in the lines without SIGIRR | 0.044 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[HDAC6]] | B | HDAC6 activity raises DARS2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.4, -32.2); signed map (-13.3, -43.3). **Vector** length 89.9, 18.7% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.8 | +19.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +20.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +14.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -0.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +3.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -5.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.5 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -7.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | aspartyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:173,824,653-173,858,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10514, mtAspRS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PI48](https://www.uniprot.org/uniprotkb/Q6PI48) (Aspartate--tRNA ligase, mitochondrial):

> Catalyzes the attachment of aspartate to tRNA(Asp) in a two-step reaction: aspartate is first activated by ATP to form Asp-AMP and then transferred to the acceptor end of tRNA(Asp).

**Summary**, from NCBI Gene [55157](https://www.ncbi.nlm.nih.gov/gene/55157):

> The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:25538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25538) · Entrez [55157](https://www.ncbi.nlm.nih.gov/gene/55157) · UniProt [Q6PI48](https://www.uniprot.org/uniprotkb/Q6PI48) · Ensembl [ENSG00000117593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117593)

## Data

Gene col 3927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3927); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3927]; `tensor/DDL_lfc|DDL_z.npy` [3927]; `embed/gene_vectors.npy` [3927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3927 or target_col == 3927). Every well: [[DARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
