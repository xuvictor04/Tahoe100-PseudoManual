---
symbol: "TNKS2"
type: "gene"
col: 2888
ensembl_id: "ENSG00000107854"
name: "tankyrase 2"
location: "10q23.32"
module: 69
arm: "+"
pooled_cpm: 138.75
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# TNKS2

*tankyrase 2* — 10q23.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +13.1, q 1e-36, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.623× (z -9.1, q 7e-17, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.275×, SW48 0.191×, NCI-H23 0.322×, SK-MEL-2 0.330×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.325×, HT-29 0.376×, NCI-H2347 0.478×, CFPAC-1 0.424×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (CFPAC-1 0.371×, SHP-77 0.275×, SW48 0.271×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAB3]] (+0.58, fdr 2e-05), [[KLHDC2]] (+0.58, fdr 2e-05), [[ATOSA]] (+0.58, fdr 1e-05); moves opposite to [[RRP7BP-1]] (-0.55, fdr 1e-05), [[ZNF787]] (-0.54, fdr 3e-05), [[CLPB]] (-0.52, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +13.1 | 1e-36 | 41/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +11.0 | 7e-26 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +7.6 | 4e-12 | 38/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.5 | 1e-08 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.9 | 4e-07 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 4e-07 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +5.7 | 1e-06 | 32/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.6 | 2e-06 | 32/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +4.7 | 2e-04 | 34/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.014 | 29/48 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.20× | +3.4 | 0.028 | 24/48 (NCI-H2030, HT-29, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.028 | 21/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.062 | 22/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.069 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.094 | 11/48 (SNU-423, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2888.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.275×, SW48 0.191×, NCI-H23 0.322×, SK-MEL-2 0.330×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.325×, HT-29 0.376×, NCI-H2347 0.478×, CFPAC-1 0.424×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (CFPAC-1 0.371×, SHP-77 0.275×, SW48 0.271×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -9.1 | 7e-17 | 42/49 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -8.1 | 1e-13 | 35/44 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -7.0 | 6e-10 | 34/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.682×** | -6.8 | 2e-09 | 33/45 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -4.8 | 2e-04 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.774×** | -4.7 | 2e-04 | 29/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.884× | -3.3 | 0.072 | 9/48 (CHP-212, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.854× | -3.0 | 0.18 | 16/48 (LoVo, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 128 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +16.7) | — |
| [[SW480 (line)]] | alt | 145 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.545× (z -8.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 148 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 150 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 158 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 168 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -11.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 170 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +17.9) | — |
| [[A-427 (line)]] | wt | 119 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -9.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 134 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 154 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -11.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 120 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 199 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 155 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +13.9) | — |
| [[SW48 (line)]] | wt | 123 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 170 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 156 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.445× (z -8.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 146 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.3) | — |
| [[KATO III (line)]] | alt | 122 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 115 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -12.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 162 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.5) | — |
| [[C32 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -11.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.495× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 177 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 147 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 92.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.123× (z -9.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SHP-77 (line)]] | alt | 69.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -11.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 95.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.448× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 270 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 138 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 114 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAB3]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[KLHDC2]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ATOSA]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.56 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[FBXO8]] | +0.55 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[LNX2]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[MAT2B]] | +0.55 | +0.28 / +0.65 | both halves | 3e-04 | pathway: Deubiquitination |
| [[CERT1]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TRAPPC6B]] | +0.54 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[UBXN7]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[PIK3CA]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[OGA]] | +0.53 | +0.37 / +0.61 | both halves | 8e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP-1]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ZNF787]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[CLPB]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 | same gene group |
| [[RRP7BP]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[TMEM201]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NOL10]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NAA15]] | -0.50 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[LETM1]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[NOP2]] | -0.49 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CHCHD6]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MINDY4]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[C1orf159]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.5, -46.8); signed map (-13.6, 8.0). **Vector** length 77.7, 21.6% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.5 | +3.4 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -7.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | +0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tankyrase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.32 — chr10:91,798,426-91,865,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TNKL, TANK2, PARP-5b, PARP-5c, PARP5B, PARP5C, pART6, ARTD6 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Poly(ADP-ribose) polymerases; Sterile alpha motif domain containing |
| Reactome | 11 pathways, smallest: Signaling by WNT in cancer; Degradation of AXIN; Regulation of PTEN stability and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2K2](https://www.uniprot.org/uniprotkb/Q9H2K2) (Poly):

> Poly-ADP-ribosyltransferase involved in various processes such as Wnt signaling pathway, telomere length and vesicle trafficking. Acts as an activator of the Wnt signaling pathway by mediating poly-ADP-ribosylation of AXIN1 and AXIN2, 2 key components of the beta-catenin destruction complex: poly-ADP-ribosylated target proteins are recognized by RNF146, which mediates their ubiquitination and subsequent degradation. Also mediates poly-ADP-ribosylation of BABAM1/MERIT40, BCR, BLZF1, CASC3, …

**Summary**, from NCBI Gene [80351](https://www.ncbi.nlm.nih.gov/gene/80351):

> Enables NAD+ poly-ADP-ribosyltransferase activity; NAD+-protein mono-ADP-ribosyltransferase activity; and enzyme binding activity. Involved in several processes, including positive regulation of canonical Wnt signaling pathway; post-translational protein modification; and regulation of telomere maintenance. Located in nuclear envelope; pericentriolar material; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15677) · Entrez [80351](https://www.ncbi.nlm.nih.gov/gene/80351) · UniProt [Q9H2K2](https://www.uniprot.org/uniprotkb/Q9H2K2) · Ensembl [ENSG00000107854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107854)

## Data

Gene col 2888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2888); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2888]; `tensor/DDL_lfc|DDL_z.npy` [2888]; `embed/gene_vectors.npy` [2888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2888 or target_col == 2888). Every well: [[TNKS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNKS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
