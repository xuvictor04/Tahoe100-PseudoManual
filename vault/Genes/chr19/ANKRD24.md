---
symbol: "ANKRD24"
type: "gene"
col: 1602
ensembl_id: "ENSG00000089847"
name: "ankyrin repeat domain 24"
location: "19p13.3"
module: 17
arm: "+"
pooled_cpm: 7.85
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 25
n_dd_up_clean: 23
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ANKRD24

*ankyrin repeat domain 24* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.85× (z +17.3, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.197× (z -14.6, q 1e-45, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPHP1]] (+0.59, fdr 4e-05), [[MTRES1]] (+0.57, fdr 3e-05), [[NECAP1]] (+0.57, fdr 8e-05); moves opposite to [[METTL4]] (-0.63, fdr 1e-05), [[PRDM10]] (-0.57, fdr 4e-05), [[SUMO3]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRKN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.85×** | +17.3 | 0e+00 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.04×** | +16.2 | 0e+00 | 44/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.18×** | +14.8 | 0e+00 | 44/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.48×** | +11.2 | 6e-27 | 44/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.59×** | +8.6 | 1e-15 | 33/39 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +7.6 | 2e-12 | 24/43 (HCT15, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +6.7 | 1e-09 | 32/48 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **3.56×** | +6.0 | 2e-07 | 30/46 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.80×** | +5.3 | 9e-06 | 20/46 (NCI-H460, A-172, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.7 | 2e-04 | 7/15 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 4e-04 | 16/42 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.64×** | +4.4 | 4e-04 | 21/47 (KATO III, COLO 205, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.59×** | +4.2 | 0.001 | 18/45 (SW480, SNU-423, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 13/48 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.002 | 20/45 (NCI-H460, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.002 | 13/48 (LS 180, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.197×** | -14.6 | 1e-45 | 41/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.243×** | -12.7 | 2e-34 | 39/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.281×** | -11.4 | 8e-28 | 33/40 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.324×** | -10.1 | 7e-22 | 34/46 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.375×** | -8.8 | 1e-16 | 34/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.403×** | -8.2 | 3e-14 | 35/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.438×** | -7.4 | 1e-11 | 29/46 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.444×** | -7.3 | 2e-11 | 28/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.520×** | -5.9 | 3e-07 | 26/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.523×** | -5.5 | 2e-06 | 28/44 (C32, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.576×** | -4.7 | 1e-04 | 21/35 (PANC-1, A549, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.597×** | -4.6 | 2e-04 | 20/46 (NCI-H460, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.388×** | -4.4 | 4e-04 | 18/44 (A549, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.396×** | -4.4 | 5e-04 | 18/39 (NCI-H1792, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.632×** | -4.1 | 0.001 | 19/47 (NCI-H460, A549, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.725×** | -4.1 | 0.002 | 19/47 (PANC-1, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.628×** | -4.0 | 0.002 | 17/46 (LoVo, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.004 | 21/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -3.8 | 0.004 | 20/45 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.458×** | -3.7 | 0.007 | 14/40 (A549, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.08 | 4 | 9 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.51× (z +11.9) | [[Digitoxin (drug)]] 0.5 µM 0.0774× (z -15.1) |
| [[A549 (line)]] | wt | 20.9 | 0 | 8 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0685× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 7.22 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.53× (z +10.9) | [[Digitoxin (drug)]] 0.05 µM 0.134× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 9.83 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0736× (z -11.0) |
| [[SW480 (line)]] | alt | 9.70 | 1 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.39× (z +8.9) | [[Digitoxin (drug)]] 0.05 µM 0.0966× (z -12.3) |
| [[HCT15 (line)]] | alt | 22.6 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +12.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0706× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 12.1 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.75× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.144× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -8.6) |
| [[A-172 (line)]] | wt | 11.2 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 7.43× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.107× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 12.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.15× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.217× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.14 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +9.2) | [[Digitoxin (drug)]] 0.5 µM 0.0200× (z -18.2) |
| [[NCI-H1792 (line)]] | alt | 9.79 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0363× (z -13.2) |
| [[C-33 A (line)]] | alt | 12.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.108× (z -8.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 5.58 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0413× (z -11.7) |
| [[KATO III (line)]] | alt | 8.00 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0981× (z -9.5) |
| [[A-427 (line)]] | wt | 9.11 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.57× (z +8.6) | — |
| [[A498 (line)]] | wt | 16.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.79× (z +10.0) | — |
| [[C32 (line)]] | wt | 6.02 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0440× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 4.65 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0434× (z -10.0) |
| [[LS 180 (line)]] | wt | 4.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.82× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 5.72 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.8× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 5.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0573× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 8.14 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0948× (z -8.6) |
| [[SW1417 (line)]] | alt | 8.43 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -8.9) |
| [[AN3 CA (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP1]] | +0.59 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[MTRES1]] | +0.57 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[NECAP1]] | +0.57 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[ODAD4]] | +0.57 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[RING1]] | +0.55 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[CUTALP]] | +0.55 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[POTEF]] | +0.55 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[C11orf65]] | +0.55 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[HNRNPDL]] | +0.53 | +0.29 / +0.45 | both halves | 2e-04 |  |
| [[IFTAP]] | +0.52 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[BTBD2]] | +0.50 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[USP4]] | +0.50 | +0.32 / +0.39 | both halves | 2e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL4]] | -0.63 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.57 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[SUMO3]] | -0.57 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ZNF124]] | -0.55 | -0.05 / -0.37 | ⚠ not reproduced | 0.005 |  |
| [[FKBP4]] | -0.54 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZNF718]] | -0.54 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[PGRMC1]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[C1orf216]] | -0.51 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[HCFC1]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[FUCA2]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CIAO2A]] | -0.50 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[MCM9]] | -0.49 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[CDK2AP1]] | -0.49 | -0.35 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKN]] | B | PRKN activity raises ANKRD24's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.06× lower at baseline in the lines without PRKN | 0.020 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.404). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.3, 27.7); signed map (-6.8, -2.1). **Vector** length 76.2, 16.7% of its response variance represented; |z| ≥ 3 in 1,395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +7.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.2 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +4.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.2 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.1 | +11.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +4.4 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.4 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.8 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,182,689-4,224,814 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1981 |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF21](https://www.uniprot.org/uniprotkb/Q8TF21) (Ankyrin repeat domain-containing protein 24):

> Component of the stereocilia rootlet in hair cells of inner ear. Bridges the apical plasma membrane with the lower rootlet and maintains normal distribution of TRIOBP, thereby reinforcing stereocilia insertion points and organizing rootlets for hearing with long-term resilience.

**Summary**, from NCBI Gene [170961](https://www.ncbi.nlm.nih.gov/gene/170961):

> Predicted to enable actin binding activity. Predicted to be involved in auditory receptor cell stereocilium organization and sensory perception of sound. Predicted to be located in plasma membrane. Predicted to be part of stereocilium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29424) · Entrez [170961](https://www.ncbi.nlm.nih.gov/gene/170961) · UniProt [Q8TF21](https://www.uniprot.org/uniprotkb/Q8TF21) · Ensembl [ENSG00000089847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089847)

## Data

Gene col 1602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1602); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1602]; `tensor/DDL_lfc|DDL_z.npy` [1602]; `embed/gene_vectors.npy` [1602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1602 or target_col == 1602). Every well: [[ANKRD24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
