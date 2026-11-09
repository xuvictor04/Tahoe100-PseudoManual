---
symbol: "WARS2"
type: "gene"
col: 3851
ensembl_id: "ENSG00000116874"
name: "tryptophanyl tRNA synthetase 2, mitochondrial"
location: "1p12"
module: 51
arm: "+"
pooled_cpm: 37.71
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# WARS2

*tryptophanyl tRNA synthetase 2, mitochondrial* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +16.3, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.512× (z -15.1, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INO80]] (+0.82, fdr 7e-06), [[EPC2]] (+0.78, fdr 7e-06), [[LANCL2]] (+0.78, fdr 7e-06); moves opposite to [[GMCL1]] (-0.61, fdr 2e-05), [[OSTF1]] (-0.60, fdr 3e-05), [[MXRA7]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +16.3 | 0e+00 | 39/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +11.0 | 8e-26 | 37/47 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +10.9 | 2e-25 | 37/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +9.8 | 1e-20 | 36/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +8.5 | 3e-15 | 31/48 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +8.3 | 7e-15 | 31/48 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.7 | 2e-09 | 25/47 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +6.5 | 6e-09 | 29/48 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +6.0 | 2e-07 | 25/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.37×** | +5.9 | 3e-07 | 27/47 (SW48, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +5.5 | 3e-06 | 23/48 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.3 | 5e-06 | 18/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.2 | 8e-06 | 21/48 (AsPC-1, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +5.0 | 3e-05 | 21/46 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.4 | 4e-04 | 12/48 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 6e-04 | 17/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.001 | 15/48 (A498, SNU-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.008 | 12/48 (RPMI-7951, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.512×** | -15.1 | 0e+00 | 44/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.530×** | -14.3 | 1e-43 | 42/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.545×** | -13.6 | 4e-40 | 40/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.573×** | -12.5 | 9e-34 | 42/48 (BT-474, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -12.0 | 4e-31 | 44/48 (SW1417, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -11.2 | 5e-27 | 28/41 (HCT15, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -10.9 | 1e-25 | 39/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.649×** | -9.7 | 2e-20 | 27/47 (SHP-77, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.472×** | -8.8 | 8e-17 | 37/48 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -7.5 | 4e-12 | 29/48 (MIA PaCa-2, CHP-212, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -7.4 | 5e-12 | 29/48 (NCI-H23, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.734×** | -6.7 | 1e-09 | 25/47 (PANC-1, SNU-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.747×** | -6.6 | 2e-09 | 32/48 (CHP-212, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -6.0 | 6e-08 | 24/47 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.768×** | -5.9 | 1e-07 | 24/46 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.823×** | -4.4 | 4e-04 | 17/48 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.859× | -3.3 | 0.032 | 15/48 (C-33 A, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.873× | -3.0 | 0.063 | 6/48 (A498, SW1417, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 116 | 0 | 8 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -15.7) |
| [[SW1417 (line)]] | alt | 47.0 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.389× (z -10.4) |
| [[A498 (line)]] | wt | 25.0 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -9.2) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.371× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.264× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 21.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 32.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -10.7) |
| [[PANC-1 (line)]] | alt | 31.5 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.356× (z -11.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -10.3) |
| [[SNU-1 (line)]] | wt | 61.5 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.51× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -14.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 43.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.342× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 42.0 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.285× (z -10.7) |
| [[SHP-77 (line)]] | alt | 69.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0436× (z -29.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 57.3 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.292× (z -9.9) |
| [[C32 (line)]] | wt | 33.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 37.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 32.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[LOX-IMVI (line)]] | wt | 35.5 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +8.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -8.7) |
| [[LS 180 (line)]] | wt | 47.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.6) | [[Auranofin (drug)]] 5 µM 0.450× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 61.7 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 29.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 33.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.3) | — |
| [[RKO (line)]] | wt | 53.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.318× (z -9.9) |
| [[A549 (line)]] | wt | 30.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.247× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 44.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0581× (z -12.5) |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.345× (z -8.8) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 38.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.395× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.164× (z -9.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 34.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.337× (z -9.8) |
| [[SW48 (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 54.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.432× (z -10.5) |
| [[A-427 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80]] | +0.82 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[EPC2]] | +0.78 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.78 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[YJU2]] | +0.74 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[NFYC]] | +0.74 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TTC27]] | +0.73 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[EPC1]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[THADA]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[FASTKD2]] | +0.71 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ZNF644]] | +0.71 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SENP6]] | +0.69 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SCAF8]] | +0.69 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.61 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[OSTF1]] | -0.60 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[MXRA7]] | -0.60 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[PLCB3]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[HDAC3]] | -0.57 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[C12orf75]] | -0.57 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[DPYSL2]] | -0.57 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.56 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[UBTD1]] | -0.56 | -0.64 / -0.40 | both halves | 4e-05 |  |
| [[HSPB11]] | -0.56 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PJA2]] | -0.56 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[EHBP1L1]] | -0.56 | -0.48 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.1, 12.0); signed map (11.9, -31.2). **Vector** length 110, 29.1% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +16.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.5 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +5.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +5.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.1 | -12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -10.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.4 | -12.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.4 | -15.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.8 | -8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | tryptophanyl tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:119,031,216-119,140,654 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mtTrpRS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGM6](https://www.uniprot.org/uniprotkb/Q9UGM6) (Tryptophan--tRNA ligase, mitochondrial):

> Catalyzes the attachment of tryptophan to tRNA(Trp) in a two-step reaction: tryptophan is first activated by ATP to form Trp-AMP and then transferred to the acceptor end of tRNA(Trp).

**Summary**, from NCBI Gene [10352](https://www.ncbi.nlm.nih.gov/gene/10352):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of tryptophanyl-tRNA synthetase exist, a cytoplasmic form, named WARS, and a mitochondrial form, named WARS2. This gene encodes the mitochondrial tryptophanyl-tRNA synthetase. Two alternative …

**Accessions** — [HGNC:12730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12730) · Entrez [10352](https://www.ncbi.nlm.nih.gov/gene/10352) · UniProt [Q9UGM6](https://www.uniprot.org/uniprotkb/Q9UGM6) · Ensembl [ENSG00000116874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116874)

## Data

Gene col 3851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3851); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3851]; `tensor/DDL_lfc|DDL_z.npy` [3851]; `embed/gene_vectors.npy` [3851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3851 or target_col == 3851). Every well: [[WARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
