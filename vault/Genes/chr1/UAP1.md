---
symbol: "UAP1"
type: "gene"
col: 3878
ensembl_id: "ENSG00000117143"
name: "UDP-N-acetylglucosamine pyrophosphorylase 1"
location: "1q23.3"
module: 52
arm: "+"
pooled_cpm: 163.98
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# UAP1

*UDP-N-acetylglucosamine pyrophosphorylase 1* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.41× (z +6.2, q 4e-07, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.510× (z -8.2, q 2e-13, down in 33 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.735× (z -5.5, q 6e-06, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL2]] (+0.59, fdr 3e-05), [[TAF13]] (+0.57, fdr 2e-05), [[POLG]] (+0.54, fdr 3e-05); moves opposite to [[SPPL3]] (-0.49, fdr 1e-04), [[SUMO2]] (-0.48, fdr 5e-05), [[CDKN2A]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +6.2 | 4e-07 | 35/49 (NCI-H1573, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.50×** | +5.2 | 7e-05 | 33/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.9 | 1e-04 | 32/48 (C32, HEC-1-A, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.44×** | +4.7 | 4e-04 | 32/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +4.5 | 7e-04 | 31/49 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.41×** | +4.3 | 0.001 | 28/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 28/48 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.004 | 28/47 (NCI-H1573, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +3.6 | 0.022 | 25/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.022 | 22/49 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.13 | 22/47 (A-427, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3878.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.510×** | -8.2 | 2e-13 | 33/44 (J82, NCI-H23, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -7.2 | 2e-10 | 34/45 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.634×** | -5.8 | 2e-06 | 32/48 (RKO, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.735×** | -5.5 | 6e-06 | 35/48 (A-172, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.669×** | -5.1 | 5e-05 | 32/48 (RKO, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -4.8 | 1e-04 | 30/47 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.705×** | -4.4 | 8e-04 | 31/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -4.3 | 0.001 | 28/48 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.712×** | -4.3 | 0.001 | 30/49 (RKO, AsPC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.704×** | -4.3 | 0.001 | 27/48 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.718×** | -4.0 | 0.003 | 31/48 (RKO, SW 1088, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.724×** | -3.9 | 0.004 | 30/50 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.739×** | -3.7 | 0.011 | 26/48 (J82, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.755×** | -3.5 | 0.016 | 29/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.757×** | -3.5 | 0.017 | 28/48 (J82, A-172, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.782×** | -3.1 | 0.066 | 24/48 (SW1417, A498, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.787×** | -3.0 | 0.076 | 25/49 (SW 1088, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 641 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -19.8) |
| [[A-172 (line)]] | wt | 454 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 190 | 2 (1 ⚠) | 5 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.13× (z +8.7) | [[Adagrasib (drug)]] 0.05 µM 0.538× (z -17.7) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 0.288× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 493 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +10.0) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.3× (z +9.3) | [[Adagrasib (drug)]] 0.05 µM 0.618× (z -12.1) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 74.4 | 6 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.26× (z +14.9) | — |
| [[C32 (line)]] | wt | 217 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 457 | 3 (2 ⚠) | 1 | [[Peretinoin (drug)]] 5 µM 3.62× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.9) |
| [[J82 (line)]] | alt | 272 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[HEC-1-A (line)]] | alt | 55.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 176 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 18.8× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 134 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 274 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.33× (z +9.4) | [[Ponatinib (drug)]] 5 µM 0.374× (z -8.9) |
| [[SW 1088 (line)]] | alt | 158 | 0 | 2 (1 ⚠) | — | [[Vilanterol (drug)]] 0.05 µM 0.0530× (z -11.5) |
| [[A498 (line)]] | wt | 169 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.559× (z -8.5) |
| [[C-33 A (line)]] | alt | 77.9 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.99× (z +8.8) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[CFPAC-1 (line)]] | alt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 137 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 289 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H2030 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -9.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 92.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 98.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.7) | — |
| [[SHP-77 (line)]] | alt | 58.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.86× (z +10.2) ⚠ toxic; cell-cycle shift, explains ~81% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 85.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 99.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.340× (z -9.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 50.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +14.1) | — |
| [[A549 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 115 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 98.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL2]] | +0.59 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[TAF13]] | +0.57 | +0.61 / +0.49 | both halves | 2e-05 |  |
| [[POLG]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[SLC16A1]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PMM2]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[SLC1A5]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[NANS]] | +0.53 | +0.61 / +0.38 | both halves | 6e-05 | pathway: Asparagine N-linked glycosylation; STRING 573 |
| [[NDEL1]] | +0.52 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[ZNF275]] | +0.52 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[GOLGA3]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ATG101]] | +0.51 | +0.65 / +0.36 | both halves | 1e-04 |  |
| [[ARF4]] | +0.51 | +0.60 / +0.37 | both halves | 7e-05 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPPL3]] | -0.49 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[SUMO2]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[CDKN2A]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RCOR3]] | -0.46 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[INTU]] | -0.46 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[RABGAP1]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ABHD16A]] | -0.46 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ABCB7]] | -0.45 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[KAT6A]] | -0.45 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[ARID2]] | -0.45 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[UVRAG]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[NDUFAF8]] | -0.43 | -0.40 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (12.7, -27.8); signed map (-50.6, 5.7). **Vector** length 130, 44.8% of its response variance represented; |z| ≥ 3 in 1,428 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.7 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.7 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +6.6 | +5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.5 | +4.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.1 | +3.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -7.7 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.2 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.0 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | UDP-N-acetylglucosamine pyrophosphorylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:162,561,722-162,601,240 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AGX1, AgX; previously SPAG2 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 4 pathways, smallest: Synthesis of UDP-N-acetyl-glucosamine; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16222](https://www.uniprot.org/uniprotkb/Q16222) (UDP-N-acetylhexosamine pyrophosphorylase):

> Catalyzes the last step in biosynthesis of uridine diphosphate-N-acetylglucosamine (UDP-GlcNAc) by converting UTP and glucosamine 1-phosphate (GlcNAc-1-P) to the sugar nucleotide. Also converts UTP and galactosamine 1-phosphate (GalNAc-1-P) into uridine diphosphate-N-acetylgalactosamine (UDP-GalNAc). In addition to its role in metabolism, acts as a regulator of innate immunity in response to virus infection by mediating pyrophosphorylation of IRF3: catalyzes pyrophosphorylation of IRF3 …

**Summary**, from NCBI Gene [6675](https://www.ncbi.nlm.nih.gov/gene/6675):

> Enables identical protein binding activity and protein serine pyrophosphorylase activity. Involved in antiviral innate immune response and positive regulation of type I interferon production. Is active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12457) · Entrez [6675](https://www.ncbi.nlm.nih.gov/gene/6675) · UniProt [Q16222](https://www.uniprot.org/uniprotkb/Q16222) · Ensembl [ENSG00000117143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117143)

## Data

Gene col 3878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3878); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3878]; `tensor/DDL_lfc|DDL_z.npy` [3878]; `embed/gene_vectors.npy` [3878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3878 or target_col == 3878). Every well: [[UAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
