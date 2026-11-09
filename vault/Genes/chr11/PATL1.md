---
symbol: "PATL1"
type: "gene"
col: 9380
ensembl_id: "ENSG00000166889"
name: "PAT1 homolog 1, processing body mRNA decay factor"
location: "11q12.1"
module: 14
arm: "+"
pooled_cpm: 103.29
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PATL1

*PAT1 homolog 1, processing body mRNA decay factor* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +16.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.641× (z -10.0, q 6e-21, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCA]] (+0.64, fdr 2e-05), [[FMR1]] (+0.61, fdr 1e-05), [[YY1AP1]] (+0.61, fdr 9e-06); moves opposite to [[PRDX1]] (-0.60, fdr 1e-05), [[LRRC8A]] (-0.54, fdr 9e-05), [[ST3GAL1]] (-0.54, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[JAK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +16.3 | 0e+00 | 44/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.40×** | +13.9 | 9e-42 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.30×** | +13.9 | 1e-41 | 48/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +10.6 | 7e-24 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +10.1 | 5e-22 | 45/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +8.9 | 4e-17 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +8.2 | 2e-14 | 44/48 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +8.2 | 3e-14 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +6.9 | 3e-10 | 39/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +6.5 | 4e-09 | 38/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 6e-06 | 31/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.39×** | +4.4 | 5e-04 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.5 | 0.019 | 23/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.028 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.052 | 21/48 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -10.0 | 6e-21 | 42/49 (CHP-212, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.589×** | -8.4 | 8e-15 | 42/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.627×** | -7.4 | 2e-11 | 43/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.762×** | -6.1 | 1e-07 | 30/48 (HOP62, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.685×** | -6.0 | 2e-07 | 40/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -5.1 | 3e-05 | 32/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.803×** | -5.0 | 6e-05 | 27/48 (A498, J82, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.741×** | -4.8 | 1e-04 | 34/49 (NCI-H2347, A549, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -4.4 | 6e-04 | 30/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -4.3 | 8e-04 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.762×** | -4.2 | 0.002 | 31/47 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **0.769×** | -4.0 | 0.003 | 28/43 (AsPC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.720×** | -3.7 | 0.008 | 30/48 (RPMI-7951, AN3 CA, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.040 | 25/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.815×** | -3.3 | 0.041 | 23/49 (NCI-H2347, SNU-1, …) | rises with dose | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | 0.869× | -3.2 | 0.055 | 19/49 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.822×** | -3.1 | 0.057 | 20/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.0 | 0.078 | 17/48 (HEC-1-A, HT-29, …) | rises with dose | position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | 0.869× | -3.0 | 0.078 | 7/49 (LOX-IMVI, C32, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.7 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +17.4) | — |
| [[HOP62 (line)]] | alt | 88.0 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +20.0) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.554× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 66.4 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[PANC-1 (line)]] | alt | 92.0 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.28× (z +19.9) | — |
| [[A-172 (line)]] | wt | 121 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +21.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 134 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -13.1) |
| [[J82 (line)]] | alt | 127 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +23.6) | — |
| [[A498 (line)]] | wt | 80.9 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 94.7 | 3 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.90× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -13.9) |
| [[SW480 (line)]] | alt | 103 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +15.3) | — |
| [[A549 (line)]] | wt | 133 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.3) |
| [[BT-474 (line)]] | alt | 136 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 104 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -10.7) |
| [[Hs 766T (line)]] | wt | 125 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +16.2) | — |
| [[HT-29 (line)]] | alt | 107 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +11.9) | — |
| [[KATO III (line)]] | alt | 101 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +13.3) | — |
| [[NCI-H23 (line)]] | alt | 74.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.8) | — |
| [[A-427 (line)]] | wt | 118 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.5) | — |
| [[C32 (line)]] | wt | 74.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.3) | — |
| [[COLO 205 (line)]] | alt | 86.7 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.87× (z +16.0) | — |
| [[H4 (line)]] | wt | 79.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 117 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 112 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 167 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 14.1× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.1) |
| [[SNU-423 (line)]] | alt | 160 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 127 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 79.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +12.0) | — |
| [[LoVo (line)]] | wt | 75.9 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.42× (z +11.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 147 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 81.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.03× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 142 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 124 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[RKO (line)]] | wt | 127 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.12× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -10.4) |
| [[SW1417 (line)]] | alt | 136 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 80.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -15.6) |
| [[HCT15 (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 84.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.4) | — |
| [[SW48 (line)]] | wt | 88.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCA]] | +0.64 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[FMR1]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[YY1AP1]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[TIFA]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MIER1]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ATG3]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[FAM111A-DT]] | +0.59 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[NFKBIA]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[BCL3]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SETDB2]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ADAR]] | +0.56 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[PSMB8]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[LRRC8A]] | -0.54 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[ST3GAL1]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[BIN3]] | -0.52 | -0.43 / -0.55 | both halves | 4e-05 |  |
| [[PDCD6]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DAP3]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CAP1]] | -0.51 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[EVI5]] | -0.51 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[POMP]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[S100A16]] | -0.49 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[RABGEF1]] | -0.49 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[DOCK5]] | -0.49 | -0.46 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAK2]] | B | JAK2 activity raises PATL1's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, -8.7); signed map (31.2, -27.1). **Vector** length 92.7, 31.8% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +16.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | +4.5 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.1 | +10.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +0.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.0 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | +1.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | PAT1 homolog 1, processing body mRNA decay factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:59,636,716-59,669,037 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36874, Pat1b |
| Reactome | 3 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TB9](https://www.uniprot.org/uniprotkb/Q86TB9) (Protein PAT1 homolog 1):

> RNA-binding protein involved in deadenylation-dependent decapping of mRNAs, leading to the degradation of mRNAs. Acts as a scaffold protein that connects deadenylation and decapping machinery. Required for cytoplasmic mRNA processing body (P-body) assembly.; (Microbial infection) In case of infection, required for translation and replication of hepatitis C virus (HCV).

**Summary**, from NCBI Gene [219988](https://www.ncbi.nlm.nih.gov/gene/219988):

> Enables poly(G) binding activity and poly(U) RNA binding activity. Involved in P-body assembly and deadenylation-dependent decapping of nuclear-transcribed mRNA. Located in CCR4-NOT complex and P-body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26721) · Entrez [219988](https://www.ncbi.nlm.nih.gov/gene/219988) · UniProt [Q86TB9](https://www.uniprot.org/uniprotkb/Q86TB9) · Ensembl [ENSG00000166889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166889)

## Data

Gene col 9380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9380); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9380]; `tensor/DDL_lfc|DDL_z.npy` [9380]; `embed/gene_vectors.npy` [9380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9380 or target_col == 9380). Every well: [[PATL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PATL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
