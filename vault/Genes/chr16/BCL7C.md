---
symbol: "BCL7C"
type: "gene"
col: 1802
ensembl_id: "ENSG00000099385"
name: "BAF chromatin remodeling complex subunit BCL7C"
location: "16p11.2"
module: 2
arm: "+"
pooled_cpm: 30.13
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# BCL7C

*BAF chromatin remodeling complex subunit BCL7C* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.44× (z +7.0, q 1e-09, up in 27 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 3.41×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1573 3.09×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.292× (z -33.6, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIP2A]] (+0.63, fdr 7e-06), [[OGG1]] (+0.62, fdr 1e-05), [[DCAKD]] (+0.61, fdr 1e-05); moves opposite to [[ASF1A]] (-0.63, fdr 1e-05), [[FOXA1]] (-0.55, fdr 6e-05), [[TRIM69]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1802.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 3.41×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1573 3.09×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.0 | 1e-09 | 27/45 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.5 | 1e-05 | 20/36 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.3 | 3e-05 | 20/45 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +4.6 | 6e-04 | 19/43 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.20×** | +3.6 | 0.037 | 15/47 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.17 | 16/48 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.17 | 12/48 (LOX-IMVI, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.292×** | -33.6 | 0e+00 | 45/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.363×** | -18.8 | 0e+00 | 47/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.399×** | -17.7 | 0e+00 | 38/47 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.301×** | -12.1 | 1e-31 | 43/48 (A-427, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -9.5 | 4e-19 | 34/48 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.622×** | -9.1 | 7e-18 | 33/48 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -8.8 | 1e-16 | 31/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -8.3 | 1e-14 | 38/48 (NCI-H460, HEC-1-A, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.641×** | -8.2 | 1e-14 | 32/47 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -7.7 | 1e-12 | 35/48 (CFPAC-1, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.683×** | -6.9 | 2e-10 | 35/48 (A-172, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.754×** | -5.4 | 3e-06 | 21/46 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -5.4 | 4e-06 | 23/48 (A-172, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.783×** | -4.7 | 1e-04 | 19/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.6 | 2e-04 | 23/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -4.5 | 2e-04 | 18/48 (hTERT-HPNE, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -4.4 | 4e-04 | 14/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -4.4 | 4e-04 | 19/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.800×** | -4.3 | 5e-04 | 18/48 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.036 | 14/47 (SW1417, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.2 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -22.3) |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -22.2) |
| [[SNU-1 (line)]] | wt | 41.8 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0832× (z -14.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.5) |
| [[A-172 (line)]] | wt | 55.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -25.8) |
| [[MIA PaCa-2 (line)]] | alt | 69.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0720× (z -38.7) |
| [[A-427 (line)]] | wt | 47.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -28.9) |
| [[HEC-1-A (line)]] | alt | 41.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -22.7) |
| [[SW480 (line)]] | alt | 23.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.6) |
| [[A549 (line)]] | wt | 30.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -22.4) |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 23.0 | 2 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 3.41× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 36.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.7) |
| [[A498 (line)]] | wt | 30.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.2) |
| [[AN3 CA (line)]] | alt | 36.8 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0759× (z -10.3) |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -17.8) |
| [[C32 (line)]] | wt | 29.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.9) |
| [[H4 (line)]] | wt | 29.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.0) |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -10.4) |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.211× (z -12.5) |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 43.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -23.3) |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0627× (z -9.8) ⚠ cell-cycle shift, explains ~12% of this change |
| [[Panc 03.27 (line)]] | alt | 17.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -13.2) |
| [[SHP-77 (line)]] | alt | 40.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.231× (z -11.5) ⚠ toxic |
| [[SW48 (line)]] | wt | 25.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.7) |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.3) |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -10.0) |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.8) |
| [[Hs 766T (line)]] | wt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.2) |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.8) |
| [[J82 (line)]] | alt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.6) |
| [[KATO III (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.5) |
| [[PANC-1 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -15.5) |
| [[RKO (line)]] | wt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.145× (z -11.1) |
| [[SNU-423 (line)]] | alt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -21.7) |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[OGG1]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[DCAKD]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SPATA33]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[EEF1AKMT2]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[CROCCP3]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[TCF3]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[CERS5]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CROCCP2]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PACS2]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CTNNBIP1]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HMCES]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASF1A]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[FOXA1]] | -0.55 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[TRIM69]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[AKR1B1]] | -0.52 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[METTL18]] | -0.52 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[MSRB2]] | -0.52 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[DZIP3]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CAMK2D]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[CAPS2]] | -0.51 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[TIGD2]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[NCOA7]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[DNAJB4]] | -0.51 | -0.56 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP2]] | B | BMP2 activity lowers BCL7C's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.31× higher at baseline in the lines without BMP2 | 0.006 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[FRMD4B]] | B | FRMD4B activity lowers BCL7C's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.43× higher at baseline in the lines without FRMD4B | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[GATA6]] | B | GATA6 activity lowers BCL7C's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.38× higher at baseline in the lines without GATA6 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[CCSER1]] | B | CCSER1 activity lowers BCL7C's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 1.28× higher at baseline in the lines without CCSER1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.1, -0.8); signed map (-44.6, -2.8). **Vector** length 86.8, 19.3% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +5.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +3.5 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.2 | -4.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.8 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -33.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -17.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -18.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -8.3 |

## What is on record

|  |  |
|---|---|
| Name | BAF chromatin remodeling complex subunit BCL7C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,833,626-30,894,302 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMARCJ3 |
| Gene groups (HGNC) | BAF complex subunits; MicroRNA protein coding host genes |
| Reactome | 18 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUZ0](https://www.uniprot.org/uniprotkb/Q8WUZ0) (B-cell CLL/lymphoma 7 protein family member C):

> May play an anti-apoptotic role.

**Summary**, from NCBI Gene [9274](https://www.ncbi.nlm.nih.gov/gene/9274):

> This gene is identified by the similarity of its product to the N-terminal region of BCL7A protein. The BCL7A protein is encoded by the gene known to be directly involved in a three-way gene translocation in a Burkitt lymphoma cell line. The function of this gene has not yet been determined. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:1006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1006) · Entrez [9274](https://www.ncbi.nlm.nih.gov/gene/9274) · UniProt [Q8WUZ0](https://www.uniprot.org/uniprotkb/Q8WUZ0) · Ensembl [ENSG00000099385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099385)

## Data

Gene col 1802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1802); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1802]; `tensor/DDL_lfc|DDL_z.npy` [1802]; `embed/gene_vectors.npy` [1802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1802 or target_col == 1802). Every well: [[BCL7C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL7C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
