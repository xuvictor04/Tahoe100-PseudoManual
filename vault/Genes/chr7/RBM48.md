---
symbol: "RBM48"
type: "gene"
col: 4854
ensembl_id: "ENSG00000127993"
name: "RNA binding motif protein 48"
location: "7q21.2"
module: 23
arm: "+"
pooled_cpm: 21.45
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 17
n_dd_up_clean: 25
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RBM48

*RNA binding motif protein 48* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +17.6, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.551× (z -11.9, q 9e-30, down in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.727× (z -9.0, q 5e-17, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUPT7L]] (+0.75, fdr 7e-06), [[C3orf38]] (+0.73, fdr 1e-05), [[PNISR-AS1]] (+0.71, fdr 3e-05); moves opposite to [[TRABD]] (-0.61, fdr 1e-04), [[GMDS]] (-0.61, fdr 3e-05), [[ARHGAP8]] (-0.61, fdr 8e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +17.6 | 0e+00 | 42/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +17.2 | 0e+00 | 42/47 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.82×** | +16.4 | 0e+00 | 45/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.41×** | +15.5 | 0e+00 | 40/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +15.4 | 0e+00 | 43/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +13.4 | 4e-39 | 38/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +10.7 | 1e-24 | 36/45 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +10.7 | 1e-24 | 37/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +10.1 | 2e-22 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +9.8 | 5e-21 | 33/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +9.2 | 2e-18 | 33/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +8.9 | 2e-17 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +8.3 | 5e-15 | 34/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.0 | 5e-14 | 29/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.9 | 1e-13 | 31/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +7.4 | 5e-12 | 30/48 (HT-29, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 2e-10 | 27/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.551×** | -11.9 | 9e-30 | 45/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -9.2 | 1e-17 | 20/34 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.727×** | -9.0 | 5e-17 | 37/48 (SW480, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -8.0 | 2e-13 | 31/48 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.692×** | -7.3 | 3e-11 | 23/41 (HCT15, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.572×** | -5.8 | 5e-07 | 27/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.581×** | -5.7 | 1e-06 | 23/48 (A498, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.756×** | -5.6 | 2e-06 | 22/48 (CHP-212, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.599×** | -5.3 | 6e-06 | 19/47 (BT-474, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.649×** | -4.5 | 4e-04 | 17/45 (Hs 766T, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.651×** | -4.5 | 4e-04 | 17/46 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.746×** | -4.2 | 0.001 | 15/48 (A498, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.813×** | -4.1 | 0.002 | 14/48 (PANC-1, SHP-77, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.816×** | -4.0 | 0.002 | 18/48 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.7 | 0.009 | 3/48 (SW 1088, SW48, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.709×** | -3.6 | 0.011 | 10/48 (A-427, HCT15, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.784×** | -3.5 | 0.017 | 9/48 (NCI-H1792, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.026 | 8/48 (A498, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 0.852× | -3.2 | 0.041 | 5/47 (J82, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.863× | -2.9 | 0.094 | 5/48 (COLO 205, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.9 | 6 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +10.7) | — |
| [[SW480 (line)]] | alt | 27.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 24.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 25.8 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -16.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 20.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.8) | — |
| [[KATO III (line)]] | alt | 26.2 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.09× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 18.7 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 19.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 20.2 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.43× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -11.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.8) | — |
| [[LoVo (line)]] | wt | 16.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.7× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 22.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 34.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.0) | — |
| [[A498 (line)]] | wt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +8.8) | — |
| [[A549 (line)]] | wt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0851× (z -10.2) |
| [[H4 (line)]] | wt | 23.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.130× (z -9.9) |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -10.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.112× (z -9.5) |
| [[HOP62 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 25.8 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0842× (z -8.8) |
| [[J82 (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.31× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPT7L]] | +0.75 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[C3orf38]] | +0.73 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PNISR-AS1]] | +0.71 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[MFF-DT]] | +0.69 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[AHI1-DT]] | +0.68 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[GABPA]] | +0.68 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ERCC6L2-AS1]] | +0.66 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[ZNF189]] | +0.65 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[METTL6]] | +0.65 | +0.63 / +0.30 | both halves | 2e-04 |  |
| [[EFCAB6]] | +0.65 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | +0.64 | +0.55 / +0.26 | both halves | 4e-04 |  |
| [[SLU7]] | +0.64 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRABD]] | -0.61 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[GMDS]] | -0.61 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ARHGAP8]] | -0.61 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[TCF3]] | -0.61 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[LPCAT1]] | -0.61 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[NAA10]] ⚠ | -0.60 | -0.37 / -0.36 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[DNMT3B]] | -0.60 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[FCHO1]] | -0.60 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[C20orf27]] | -0.59 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[GNA12]] | -0.59 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[ST6GALNAC4]] | -0.59 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[GNB1L]] | -0.59 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[PPM1G]] | -0.58 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RBM48's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (1.0, 17.1); signed map (24.1, -12.7). **Vector** length 92.4, 21.6% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +17.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.9 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +8.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +16.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +6.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.1 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.8 | -11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.3 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.3 | -8.0 |
|  | [[EX229 (drug)]] 5 µM |  | -5.0 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.0 | -5.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.4 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 48 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:92,528,773-92,540,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564O0523, HSPC304; previously C7orf64 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5RL73](https://www.uniprot.org/uniprotkb/Q5RL73) (RNA-binding protein 48):

> As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs.

**Summary**, from NCBI Gene [84060](https://www.ncbi.nlm.nih.gov/gene/84060):

> Predicted to enable RNA binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21785) · Entrez [84060](https://www.ncbi.nlm.nih.gov/gene/84060) · UniProt [Q5RL73](https://www.uniprot.org/uniprotkb/Q5RL73) · Ensembl [ENSG00000127993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127993)

## Data

Gene col 4854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4854); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4854]; `tensor/DDL_lfc|DDL_z.npy` [4854]; `embed/gene_vectors.npy` [4854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4854 or target_col == 4854). Every well: [[RBM48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
