---
symbol: "TAF1D"
type: "gene"
col: 9224
ensembl_id: "ENSG00000166012"
name: "TATA-box binding protein associated factor, RNA polymerase I subunit D"
location: "11q21"
module: 20
arm: "-"
pooled_cpm: 310.82
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TAF1D

*TATA-box binding protein associated factor, RNA polymerase I subunit D* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.25× (z +15.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Busulfan (drug)]] 0.05 µM: 0.759× (z -3.6, q 0.064, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4A-AS1]] (+0.79, fdr 7e-06), [[SNHG7]] (+0.77, fdr 7e-06), [[SNHG32]] (+0.75, fdr 7e-06); moves opposite to [[GPAA1]] (-0.62, fdr 1e-05), [[TGOLN2]] (-0.61, fdr 1e-05), [[EIF4EBP2]] (-0.61, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +15.0 | 0e+00 | 46/48 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +11.1 | 3e-26 | 44/48 (CFPAC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +9.8 | 1e-20 | 47/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +9.1 | 2e-17 | 48/48 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +7.9 | 5e-13 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.7 | 2e-12 | 45/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.72×** | +6.9 | 5e-10 | 40/48 (A-427, LoVo, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +6.3 | 2e-08 | 45/48 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 4e-08 | 43/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +5.9 | 2e-07 | 44/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +5.4 | 4e-06 | 44/49 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +4.8 | 7e-05 | 38/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 7e-05 | 37/48 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.8 | 8e-05 | 44/45 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 37/49 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.63×** | +4.6 | 2e-04 | 43/49 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.91×** | +4.4 | 3e-04 | 43/48 (CFPAC-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.81×** | +4.1 | 0.001 | 42/48 (CFPAC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.76×** | +3.9 | 0.003 | 36/48 (CFPAC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.005 | 42/48 (CFPAC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Busulfan (drug)]] 0.05 µM |  | **0.759×** | -3.6 | 0.064 | 34/49 (NCI-H2347, SW 900, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -3.6 | 0.064 | 28/44 (AsPC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -3.6 | 0.064 | 30/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.788× | -3.1 | 0.24 | 32/48 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -3.0 | 0.30 | 1/50 (SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 231 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +16.7) | — |
| [[LoVo (line)]] | wt | 494 | 6 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.33× (z +14.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.2) | — |
| [[SW480 (line)]] | alt | 396 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.94× (z +14.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +10.8) | — |
| [[A-427 (line)]] | wt | 290 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 310 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 182 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 363 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 332 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 329 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.54× (z +10.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 408 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.7) | — |
| [[RKO (line)]] | wt | 412 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +19.4) | — |
| [[SK-MEL-2 (line)]] | alt | 175 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.4) | — |
| [[HT-29 (line)]] | alt | 361 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.8) | — |
| [[KATO III (line)]] | alt | 324 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 398 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 212 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.8) | — |
| [[Panc 03.27 (line)]] | alt | 401 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 285 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +10.8) | — |
| [[A-172 (line)]] | wt | 133 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.2) | — |
| [[A549 (line)]] | wt | 282 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 358 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.8) | — |
| [[H4 (line)]] | wt | 299 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.85× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 214 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 163 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 273 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.9) | — |
| [[J82 (line)]] | alt | 276 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 254 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 242 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 251 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.8) | — |
| [[A498 (line)]] | wt | 228 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 430 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.6) | — |
| [[C32 (line)]] | wt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.0) | — |
| [[HCT15 (line)]] | alt | 285 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.90× (z +10.3) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 262 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 285 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 338 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 379 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 278 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.42× (z +9.4) ⚠ toxic | — |
| [[SNU-1 (line)]] | wt | 447 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.89× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 763 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 273 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 463 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 330 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 400 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 401 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 506 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | +0.79 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SNHG8]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[SNHG12]] | +0.75 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[ZFAS1]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SNHG6]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[GAS5]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NACA]] ⚠ | +0.68 | +0.60 / +0.67 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | +0.67 | +0.56 / +0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZC3H15]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[EIF3E]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ATP5MC2]] | +0.62 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[ADPRM]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPAA1]] | -0.62 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[TGOLN2]] | -0.61 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[EIF4EBP2]] | -0.61 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[PPP1CA]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ARPC4]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[VMA21]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.58 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CDK2]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[SRP9]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[AP1B1]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 | same gene group |
| [[DBNL]] | -0.57 | -0.36 / -0.63 | both halves | 1e-04 |  |
| [[FKBP1A]] | -0.56 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.0, -28.7); signed map (-15.2, -2.3). **Vector** length 110, 48.1% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.1 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | -0.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.3 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.8 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.4 | +7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.1 | +4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor, RNA polymerase I subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:93,729,948-93,784,391 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5306, TAF(I)41; previously JOSD3 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Reactome | 10 pathways, smallest: SIRT1 negatively regulates rRNA expression; RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5J8](https://www.uniprot.org/uniprotkb/Q9H5J8) (TATA box-binding protein-associated factor RNA polymerase I subunit D):

> Component of the transcription factor SL1/TIF-IB complex, which is involved in the assembly of the PIC (pre-initiation complex) during RNA polymerase I-dependent transcription. The rate of PIC formation probably is primarily dependent on the rate of association of SL1/TIF-IB with the rDNA promoter. SL1/TIF-IB is involved in stabilization of nucleolar transcription factor 1/UBTF on rDNA. Formation of SL1/TIF-IB excludes the association of TBP with TFIID subunits.

**Summary**, from NCBI Gene [79101](https://www.ncbi.nlm.nih.gov/gene/79101):

> TAF1D is a member of the SL1 complex, which includes TBP (MIM 600075) and TAF1A (MIM 604903), TAF1B (MIM 604904), and TAF1C (MIM 604905), and plays a role in RNA polymerase I transcription (Wang et al., 2004 [PubMed 15520167]; Gorski et al., 2007 [PubMed 17318177]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:28759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28759) · Entrez [79101](https://www.ncbi.nlm.nih.gov/gene/79101) · UniProt [Q9H5J8](https://www.uniprot.org/uniprotkb/Q9H5J8) · Ensembl [ENSG00000166012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166012)

## Data

Gene col 9224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9224); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9224]; `tensor/DDL_lfc|DDL_z.npy` [9224]; `embed/gene_vectors.npy` [9224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9224 or target_col == 9224). Every well: [[TAF1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
