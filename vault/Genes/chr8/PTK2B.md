---
symbol: "PTK2B"
type: "gene"
col: 4234
ensembl_id: "ENSG00000120899"
name: "protein tyrosine kinase 2 beta"
location: "8p21.2"
module: 31
arm: "+"
pooled_cpm: 42.54
n_lines_expressing: 40
n_dd_up: 8
n_dd_down: 31
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 45
direction_downstream: 30
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PTK2B

*protein tyrosine kinase 2 beta* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.54× (z +8.0, q 7e-13, up in 20 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.437× (z -15.2, q 0e+00, down in 25 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYBG2]] (+0.64, fdr 1e-05), [[GJB3]] (+0.61, fdr 1e-05), [[AKAP13]] (+0.60, fdr 2e-05); moves opposite to [[LAMTOR5-AS1]] (-0.45, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); 30 go from it, the strongest it → [[CCDC120]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +8.0 | 7e-13 | 20/38 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +7.9 | 7e-13 | 19/38 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.7 | 5e-09 | 21/38 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +6.3 | 5e-08 | 19/37 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 4e-06 | 13/37 (A-172, HS-578T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.002 | 11/38 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.013 | 18/38 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.014 | 11/38 (SK-MEL-2, SNU-1, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.047 | 11/37 (A-172, HS-578T, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.20× | +3.2 | 0.080 | 8/38 (A-427, SW48, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.26× | +3.1 | 0.11 | 6/38 (KATO III, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -15.2 | 0e+00 | 25/38 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.596×** | -9.5 | 6e-19 | 28/37 (A498, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -9.1 | 1e-17 | 24/37 (AN3 CA, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.705×** | -9.1 | 2e-17 | 23/37 (NCI-H460, A498, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -8.9 | 7e-17 | 26/39 (KATO III, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -8.8 | 2e-16 | 18/28 (KATO III, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.627×** | -8.6 | 8e-16 | 23/37 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.617×** | -8.5 | 9e-16 | 22/34 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.625×** | -8.0 | 9e-14 | 19/28 (KATO III, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -7.4 | 8e-12 | 24/38 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.636×** | -7.1 | 6e-11 | 21/34 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.684×** | -7.0 | 2e-10 | 21/38 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.705×** | -6.4 | 6e-09 | 22/37 (KATO III, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.706×** | -6.4 | 7e-09 | 23/37 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.706×** | -6.2 | 3e-08 | 18/37 (NCI-H460, KATO III, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.709×** | -6.0 | 8e-08 | 17/37 (NCI-H2347, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.583×** | -5.2 | 7e-06 | 16/36 (NCI-H2347, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.605×** | -4.8 | 4e-05 | 16/36 (CFPAC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.606×** | -4.8 | 4e-05 | 15/36 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.613×** | -4.7 | 6e-05 | 19/37 (A498, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.613×** | -4.7 | 6e-05 | 17/36 (A498, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.627×** | -4.5 | 2e-04 | 15/36 (A498, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.791×** | -4.3 | 4e-04 | 13/36 (SK-MEL-2, Hs 766T, …) | two highest doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.875× | -3.4 | 0.011 | 7/39 (NCI-H2347, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 55.0 | 2 | 7 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.64× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -17.4) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.392× (z -10.4) |
| [[KATO III (line)]] | alt | 71.7 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.147× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 40.0 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -26.9) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -12.7) |
| [[SW480 (line)]] | alt | 35.4 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.412× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.414× (z -9.9) |
| [[A-427 (line)]] | wt | 23.3 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.5) ⚠ cell-cycle shift, explains ~82% of this change | [[Digitoxin (drug)]] 5 µM 0.128× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -12.2) |
| [[A498 (line)]] | wt | 56.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.7) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.348× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 149 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 206 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 146 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 73.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -10.7) |
| [[A-172 (line)]] | wt | 26.1 | 3 | 0 | [[Clobetasol propionate (drug)]] 5 µM 3.49× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 49.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -13.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.7) ⚠ cell-cycle shift, explains ~82% of this change |
| [[HS-578T (line)]] | alt | 12.0 | 1 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 7.39× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 41.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -12.5) ⚠ cell-cycle shift, explains ~82% of this change |
| [[Panc 03.27 (line)]] | alt | 94.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.170× (z -8.6) |
| [[SW 900 (line)]] | alt | 27.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SW1417 (line)]] | alt | 89.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -17.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0989× (z -11.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[COLO 205 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -9.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0909× (z -14.9) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.102× (z -10.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.96 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.69 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYBG2]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GJB3]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[AKAP13]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 | same gene group |
| [[TLDC2]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[SDR16C5]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[HS3ST1]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PTPN12]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 | STRING 884 |
| [[SH2D3A]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PLEK2]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 | STRING 474 |
| [[TMC6]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CEACAM1]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5-AS1]] | -0.45 | -0.42 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 45, C 0. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity raises PTK2B's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 3.96× lower at baseline in the lines without IRF6 | 6e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[INAVA]] | B | INAVA activity raises PTK2B's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.41× lower at baseline in the lines without INAVA | 6e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises PTK2B's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.98× lower at baseline in the lines without TMPRSS4 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CDH1]] | B | CDH1 activity raises PTK2B's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without CDH1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[P2RY2]] | B | P2RY2 activity raises PTK2B's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.32× lower at baseline in the lines without P2RY2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[SH2D3A]] | B | SH2D3A activity raises PTK2B's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.32× lower at baseline in the lines without SH2D3A | 5e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[FA2H]] | B | FA2H activity raises PTK2B's level | lines that do not express FA2H (27) vs lines expressing it (23) | 3.52× lower at baseline in the lines without FA2H | 5e-04 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[B3GNT3]] | B | B3GNT3 activity raises PTK2B's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without B3GNT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[PRSS8]] | B | PRSS8 activity raises PTK2B's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.51× lower at baseline in the lines without PRSS8 | 0.001 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[ATP2C2]] | B | ATP2C2 activity raises PTK2B's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.24× lower at baseline in the lines without ATP2C2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[FAM83B]] | B | FAM83B activity raises PTK2B's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.15× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[TINAGL1]] | B | TINAGL1 activity raises PTK2B's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.56× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 30, C 0. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | PTK2B activity raises CCDC120's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.26× lower at baseline in the lines without PTK2B | 0.012 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KIF13B]] | B | PTK2B activity raises KIF13B's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without PTK2B | 0.018 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TINAGL1]] | B | PTK2B activity raises TINAGL1's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 4.36× lower at baseline in the lines without PTK2B | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TGFA]] | B | PTK2B activity raises TGFA's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.65× lower at baseline in the lines without PTK2B | 0.020 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ITGB4]] | B | PTK2B activity raises ITGB4's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.52× lower at baseline in the lines without PTK2B | 0.024 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CORO2A]] | B | PTK2B activity raises CORO2A's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without PTK2B | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PROSER2]] | B | PTK2B activity raises PROSER2's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.18× lower at baseline in the lines without PTK2B | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[JUP]] | B | PTK2B activity raises JUP's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.71× lower at baseline in the lines without PTK2B | 0.035 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PTK6]] | B | PTK2B activity raises PTK6's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.39× lower at baseline in the lines without PTK2B | 0.035 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEMA3B]] | B | PTK2B activity raises SEMA3B's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without PTK2B | 0.038 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANO1]] | B | PTK2B activity raises ANO1's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.16× lower at baseline in the lines without PTK2B | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GJB3]] | B | PTK2B activity raises GJB3's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.90× lower at baseline in the lines without PTK2B | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.9, 53.1); signed map (1.9, 37.9). **Vector** length 102, 25.2% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +8.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +5.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -4.1 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | +1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine kinase 2 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:27,311,482-27,459,391 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAKB, PYK2, RAFTK, PTK, CADTK; previously FAK2 |
| Gene groups (HGNC) | Minor histocompatibility antigens; FERM domain containing; PTK2 family tyrosine kinases; MicroRNA protein coding host genes |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 13 pathways, smallest: Interleukin-2 signaling; Signal regulatory protein family interactions; Interleukin-2 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14289](https://www.uniprot.org/uniprotkb/Q14289) (Protein-tyrosine kinase 2-beta):

> Non-receptor protein-tyrosine kinase that regulates reorganization of the actin cytoskeleton, cell polarization, cell migration, adhesion, spreading and bone remodeling. Plays a role in the regulation of the humoral immune response, and is required for normal levels of marginal B-cells in the spleen and normal migration of splenic B-cells. Required for normal macrophage polarization and migration towards sites of inflammation. Regulates cytoskeleton rearrangement and cell spreading in T-cells, …

**Summary**, from NCBI Gene [2185](https://www.ncbi.nlm.nih.gov/gene/2185):

> This gene encodes a cytoplasmic protein tyrosine kinase which is involved in calcium-induced regulation of ion channels and activation of the map kinase signaling pathway. The encoded protein may represent an important signaling intermediate between neuropeptide-activated receptors or neurotransmitters that increase calcium flux and the downstream signals that regulate neuronal activity. The encoded protein undergoes rapid tyrosine phosphorylation and activation in response to increases in the …

**Accessions** — [HGNC:9612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9612) · Entrez [2185](https://www.ncbi.nlm.nih.gov/gene/2185) · UniProt [Q14289](https://www.uniprot.org/uniprotkb/Q14289) · Ensembl [ENSG00000120899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120899)

## Data

Gene col 4234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4234); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4234]; `tensor/DDL_lfc|DDL_z.npy` [4234]; `embed/gene_vectors.npy` [4234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4234 or target_col == 4234). Every well: [[PTK2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTK2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
