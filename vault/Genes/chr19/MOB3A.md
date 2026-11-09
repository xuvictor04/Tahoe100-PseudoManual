---
symbol: "MOB3A"
type: "gene"
col: 10209
ensembl_id: "ENSG00000172081"
name: "MOB kinase activator 3A"
location: "19p13.3"
module: 218
arm: "+"
pooled_cpm: 32.23
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# MOB3A

*MOB kinase activator 3A* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.25× (z +4.2, q 0.018, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.428× (z -15.1, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OGG1]] (+0.61, fdr 2e-05), [[BTBD2]] (+0.60, fdr 3e-05, ⚠ same locus), [[MARCHF2]] (+0.59, fdr 5e-05), [[TNNT1]] (+0.56, fdr 3e-05); moves opposite to [[NCOA2]] (-0.53, fdr 2e-04), [[ADI1]] (-0.52, fdr 3e-04), [[NNT]] (-0.51, fdr 2e-04).
> It is in [[Module 218]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.018 | 18/48 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +3.9 | 0.023 | 18/47 (A-427, hTERT-HPNE, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.028 | 12/47 (A-172, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.052 | 9/47 (HOP62, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.052 | 7/48 (RKO, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.13 | 7/48 (LoVo, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.428×** | -15.1 | 0e+00 | 38/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.473×** | -13.3 | 7e-38 | 35/47 (A-172, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.516×** | -12.2 | 4e-32 | 39/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -11.3 | 2e-27 | 33/47 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.531×** | -11.3 | 2e-27 | 34/48 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -11.2 | 4e-27 | 36/48 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.576×** | -9.8 | 7e-21 | 31/48 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.606×** | -9.3 | 2e-18 | 32/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -8.6 | 5e-16 | 29/47 (SHP-77, J82, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -6.4 | 8e-09 | 29/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -6.3 | 2e-08 | 23/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -6.2 | 4e-08 | 25/48 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.718×** | -6.1 | 4e-08 | 27/48 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -5.6 | 1e-06 | 26/45 (SHP-77, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.754×** | -5.2 | 7e-06 | 22/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -5.0 | 2e-05 | 24/48 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -4.2 | 7e-04 | 20/48 (A-172, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.849× | -3.0 | 0.056 | 15/48 (SW 1088, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 48.6 | 0 | 10 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -12.6) |
| [[HOP62 (line)]] | alt | 67.7 | 0 | 8 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.245× (z -14.2) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -10.4) |
| [[A-172 (line)]] | wt | 63.7 | 0 | 7 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -19.6) |
| [[NCI-H1573 (line)]] | alt | 49.9 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -17.3) |
| [[H4 (line)]] | wt | 47.2 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.155× (z -11.4) |
| [[SHP-77 (line)]] | alt | 72.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -17.0) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -10.9) |
| [[SW 900 (line)]] | alt | 46.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -17.3) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 45.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -11.4) |
| [[SW480 (line)]] | alt | 21.7 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -11.9) |
| [[LoVo (line)]] | wt | 22.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.344× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 26.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.88× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.7) |
| [[A-427 (line)]] | wt | 33.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.240× (z -10.8) |
| [[A549 (line)]] | wt | 29.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.0) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.304× (z -8.9) |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -9.1) |
| [[C-33 A (line)]] | alt | 30.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -9.6) |
| [[COLO 205 (line)]] | alt | 31.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -13.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -13.6) |
| [[HS-578T (line)]] | alt | 36.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -13.5) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -10.2) |
| [[J82 (line)]] | alt | 29.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H23 (line)]] | alt | 34.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 21.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.355× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 36.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.0) |
| [[SNU-423 (line)]] | alt | 39.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -11.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -8.5) |
| [[A498 (line)]] | wt | 35.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.5 µM 0.0674× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 54.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -14.6) |
| [[HCT15 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -14.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -12.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.266× (z -10.4) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.430× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 13.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -11.1) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OGG1]] | +0.61 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[BTBD2]] | +0.60 | +0.58 / +0.44 | both halves | 3e-05 | ⚠ same locus (36.2 kb, same strand: neighbours can correlate without regulation) |
| [[MARCHF2]] | +0.59 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[TNNT1]] | +0.56 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ASL]] | +0.55 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[NIBAN2]] | +0.54 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[MAPK8IP3]] | +0.54 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[TMEM44]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D25]] | +0.53 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[ZKSCAN5]] | +0.53 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ARID3B]] | +0.53 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[ANGPTL4]] | +0.53 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[GNAI2]] | +0.53 | +0.47 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA2]] | -0.53 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[ADI1]] | -0.52 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[NNT]] | -0.51 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[HNF4G]] | -0.49 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[CASD1]] | -0.49 | -0.40 / -0.26 | both halves | 3e-04 |  |
| [[BTN3A3]] | -0.49 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[PHACTR2]] | -0.49 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[HFE]] | -0.48 | -0.41 / -0.22 | both halves | 6e-04 |  |
| [[DECR1]] | -0.48 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[PTPRK]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[FUCA2]] | -0.48 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[ARID1B]] | -0.48 | -0.43 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.3, 2.3); signed map (-27.7, 16.5). **Vector** length 99.4, 24.0% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.7 | -13.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -11.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -9.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MOB kinase activator 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,071,036-2,096,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOB1C, MOB-LAK, moblak; previously MOBKL2A |
| Gene groups (HGNC) | MOB kinase activators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BX8](https://www.uniprot.org/uniprotkb/Q96BX8) (MOB kinase activator 3A):

> May regulate the activity of kinases.

**Summary**, from NCBI Gene [126308](https://www.ncbi.nlm.nih.gov/gene/126308):

> Predicted to enable protein kinase activator activity. Predicted to be involved in signal transduction. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29802) · Entrez [126308](https://www.ncbi.nlm.nih.gov/gene/126308) · UniProt [Q96BX8](https://www.uniprot.org/uniprotkb/Q96BX8) · Ensembl [ENSG00000172081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172081)

## Data

Gene col 10209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10209); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10209]; `tensor/DDL_lfc|DDL_z.npy` [10209]; `embed/gene_vectors.npy` [10209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10209 or target_col == 10209). Every well: [[MOB3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOB3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
