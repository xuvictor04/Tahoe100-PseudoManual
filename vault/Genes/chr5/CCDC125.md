---
symbol: "CCDC125"
type: "gene"
col: 11393
ensembl_id: "ENSG00000183323"
name: "coiled-coil domain containing 125"
location: "5q13.2"
module: 95
arm: "+"
pooled_cpm: 31.8
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# CCDC125

*coiled-coil domain containing 125* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +15.9, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.640× (z -8.2, q 1e-13, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EP300]] (+0.61, fdr 4e-04), [[ASH1L]] (+0.61, fdr 5e-05), [[ZNF638]] (+0.60, fdr 1e-05); moves opposite to [[USP35]] (-0.63, fdr 3e-05), [[HERC2P3]] (-0.58, fdr 3e-05), [[RNF216P1]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +15.9 | 0e+00 | 42/47 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +11.6 | 2e-28 | 33/46 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.8 | 2e-16 | 32/47 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +8.8 | 3e-16 | 33/47 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +8.0 | 2e-13 | 25/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +7.8 | 6e-13 | 24/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +7.2 | 4e-11 | 28/46 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.45×** | +6.9 | 5e-10 | 28/47 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +5.5 | 2e-06 | 23/46 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +5.3 | 7e-06 | 20/46 (A549, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +5.2 | 1e-05 | 23/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.1 | 1e-05 | 20/47 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.1 | 1e-05 | 21/47 (A498, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 1e-04 | 17/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +4.3 | 6e-04 | 20/47 (A-172, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +4.3 | 6e-04 | 19/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 19/46 (AsPC-1, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.003 | 15/47 (SW480, NCI-H1792, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11393.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.640×** | -8.2 | 1e-13 | 30/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -6.5 | 2e-08 | 25/46 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.718×** | -6.0 | 4e-07 | 29/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.744×** | -5.1 | 4e-05 | 24/47 (BT-474, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.763×** | -5.0 | 7e-05 | 19/46 (SNU-423, MIA PaCa-2, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.787×** | -4.4 | 1e-03 | 20/47 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.799×** | -4.1 | 0.003 | 17/47 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.872× | -3.6 | 0.026 | 18/47 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.830×** | -3.4 | 0.037 | 16/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.703×** | -3.4 | 0.040 | 11/47 (H4, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.3 | 0.045 | 18/46 (SW480, SNU-423, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.836× | -3.3 | 0.046 | 13/47 (NCI-H2030, AN3 CA, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.725×** | -3.1 | 0.087 | 10/45 (Panc 03.27, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | 0.849× | -3.0 | 0.11 | 12/46 (C-33 A, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.1 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +23.5) | — |
| [[A498 (line)]] | wt | 24.9 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +18.6) | — |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.271× (z -9.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.280× (z -9.6) |
| [[PANC-1 (line)]] | alt | 46.6 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +24.2) | [[Ixazomib citrate (drug)]] 0.5 µM 0.477× (z -8.7) |
| [[A549 (line)]] | wt | 27.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +14.6) | — |
| [[C32 (line)]] | wt | 13.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 10.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 39.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 41.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +21.8) | — |
| [[HEC-1-A (line)]] | alt | 37.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.0) | — |
| [[HS-578T (line)]] | alt | 15.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +10.5) | — |
| [[LoVo (line)]] | wt | 35.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +15.3) | — |
| [[NCI-H1573 (line)]] | alt | 36.5 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.32× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 29.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 27.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.8) | — |
| [[A-172 (line)]] | wt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +11.9) | — |
| [[A-427 (line)]] | wt | 67.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[AsPC-1 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +16.8) | — |
| [[C-33 A (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 41.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.5) | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -9.7) |
| [[J82 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -11.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.65× (z +10.5) | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.143× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 33.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.8) | — |
| [[RKO (line)]] | wt | 34.0 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 50.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 33.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EP300]] | +0.61 | +0.48 / +0.24 | both halves | 4e-04 |  |
| [[ASH1L]] | +0.61 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[ZNF638]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[UNK]] | +0.58 | +0.64 / +0.29 | both halves | 2e-04 |  |
| [[BAZ2B]] | +0.58 | +0.64 / +0.30 | both halves | 2e-04 |  |
| [[TGIF2]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ZC3H6]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[NFYC]] | +0.58 | +0.62 / +0.29 | both halves | 3e-04 |  |
| [[DNAI4]] | +0.57 | +0.69 / +0.23 | both halves | 6e-04 |  |
| [[RSF1]] | +0.56 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[RBM5]] | +0.56 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[TAPBPL]] | +0.56 | +0.65 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP35]] | -0.63 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[HERC2P3]] | -0.58 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[RNF216P1]] | -0.56 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[MSTO2P]] | -0.55 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[NAPG]] | -0.55 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[FAR1]] | -0.55 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[CTNNBL1]] | -0.54 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[OTULIN]] | -0.53 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[FBXW2]] | -0.53 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[NCK2]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[NSDHL]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TCP1]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC125's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (2.7, 9.4); signed map (21.2, -16.6). **Vector** length 87.4, 19.0% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of HOX genes during differentiation* (reactome, mean cos +0.51 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.8 | +4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +11.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.2 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.1 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.5 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.4 | +6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -5.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 125 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,280,175-69,332,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KENAE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Z20](https://www.uniprot.org/uniprotkb/Q86Z20) (Coiled-coil domain-containing protein 125):

> May be involved in the regulation of cell migration.

**Summary**, from NCBI Gene [202243](https://www.ncbi.nlm.nih.gov/gene/202243):

> Enables identical protein binding activity. Involved in activation of GTPase activity; negative regulation of Rho protein signal transduction; and negative regulation of cell motility. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28924) · Entrez [202243](https://www.ncbi.nlm.nih.gov/gene/202243) · UniProt [Q86Z20](https://www.uniprot.org/uniprotkb/Q86Z20) · Ensembl [ENSG00000183323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183323)

## Data

Gene col 11393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11393); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11393]; `tensor/DDL_lfc|DDL_z.npy` [11393]; `embed/gene_vectors.npy` [11393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11393 or target_col == 11393). Every well: [[CCDC125 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC125.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
