---
symbol: "GBP2"
type: "gene"
col: 8554
ensembl_id: "ENSG00000162645"
name: "guanylate binding protein 2"
location: "1p22.2"
module: 70
arm: "+"
pooled_cpm: 45.05
n_lines_expressing: 37
n_dd_up: 51
n_dd_down: 62
n_dd_up_clean: 48
n_dd_down_clean: 48
in_vector_space: true
direction_upstream: 59
direction_downstream: 67
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# GBP2

*guanylate binding protein 2* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 3.02× (z +16.0, q 0e+00, up in 33 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 62 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.538× (z -13.1, q 2e-36, down in 29 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFB]] (+0.81, fdr 7e-06), [[GBP4]] (+0.74, fdr 7e-06, ⚠ same locus), [[GBP1]] (+0.72, fdr 7e-06, ⚠ same locus), [[TNFSF10]] (+0.72, fdr 7e-06), [[BDKRB2]] (+0.70, fdr 7e-06); moves opposite to [[HMGA2]] (-0.61, fdr 7e-06), [[SPRY4-AS1]] (-0.61, fdr 7e-06), [[DPY19L3]] (-0.57, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 59 arrows point to it, the strongest [[MAF]] → it (grade B ⚠); 67 go from it, the strongest it → [[SLC25A15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 3 with an alert ⚠; shown: the 15 strongest. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **3.02×** | +16.0 | 0e+00 | 33/34 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **2.88×** | +15.1 | 0e+00 | 34/36 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.76×** | +14.7 | 0e+00 | 33/35 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **2.37×** | +14.1 | 9e-43 | 33/35 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **2.45×** | +12.9 | 6e-36 | 34/36 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +12.4 | 2e-33 | 24/35 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **2.23×** | +12.1 | 1e-31 | 31/36 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **2.02×** | +11.9 | 7e-31 | 31/35 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.78×** | +11.2 | 3e-27 | 30/35 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.99×** | +10.3 | 3e-23 | 27/34 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.61×** | +8.8 | 1e-16 | 29/36 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +8.6 | 4e-16 | 26/35 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.84×** | +8.5 | 9e-16 | 28/35 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.99×** | +7.5 | 3e-12 | 25/35 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +6.5 | 2e-09 | 21/35 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 65 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 62 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -13.1 | 2e-36 | 29/36 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.441×** | -12.2 | 6e-32 | 25/35 (Panc 03.27, A498, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.436×** | -11.5 | 3e-28 | 21/32 (Hs 766T, BT-474, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.477×** | -11.1 | 2e-26 | 27/35 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.491×** | -10.6 | 2e-24 | 26/35 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.516×** | -9.9 | 4e-21 | 26/35 (C32, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.521×** | -9.4 | 5e-19 | 23/34 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.524×** | -9.3 | 1e-18 | 26/34 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.540×** | -9.2 | 2e-18 | 22/36 (CHP-212, COLO 205, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.531×** | -9.1 | 5e-18 | 27/35 (SNU-423, C32, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.673×** | -8.3 | 4e-15 | 27/36 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.681×** | -8.1 | 3e-14 | 22/35 (A549, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.681×** | -8.1 | 3e-14 | 26/36 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.593×** | -7.8 | 3e-13 | 25/36 (HS-578T, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.500×** | -7.5 | 3e-12 | 26/35 (COLO 205, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.612×** | -7.3 | 8e-12 | 25/36 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.651×** | -6.4 | 5e-09 | 21/35 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.656×** | -6.3 | 9e-09 | 22/35 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.688×** | -5.6 | 7e-07 | 19/35 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.690×** | -5.5 | 8e-07 | 17/35 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -5.3 | 3e-06 | 18/35 (Hs 766T, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 293 | 7 | 8 (5 ⚠) | [[Binimetinib (drug)]] 0.5 µM 2.78× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -14.7) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.350× (z -9.7) |
| [[COLO 205 (line)]] | alt | 165 | 1 | 12 (7 ⚠) | [[Peretinoin (drug)]] 5 µM 3.05× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -26.6) |
| [[A498 (line)]] | wt | 89.1 | 0 | 11 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.239× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 151 | 0 | 10 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -16.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.321× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 69.7 | 6 | 3 | [[Trametinib (drug)]] 0.5 µM 4.48× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.192× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 11.9 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +21.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 7 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 2.91× (z +18.2) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 5.49× (z +9.4) | [[Tofacitinib (drug)]] 5 µM 0.297× (z -8.7) |
| [[SNU-423 (line)]] | alt | 106 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +15.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -10.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.294× (z -10.0) |
| [[HS-578T (line)]] | alt | 61.9 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +11.5) | [[Tofacitinib (drug)]] 5 µM 0.369× (z -8.5) |
| [[BT-474 (line)]] | alt | 77.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +18.4) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 25.8 | 5 | 0 | [[Trametinib (drug)]] 5 µM 6.15× (z +10.4) | — |
| [[C32 (line)]] | wt | 97.3 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.148× (z -11.7) |
| [[HOP62 (line)]] | alt | 12.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +18.0) | — |
| [[HT-29 (line)]] | alt | 71.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0281× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -8.6) |
| [[A-172 (line)]] | wt | 38.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 25.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.197× (z -11.7) |
| [[CHP-212 (line)]] | wt | 92.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0509× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 29.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +23.1) | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0831× (z -11.6) ⚠ toxic · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.153× (z -8.7) |
| [[Hs 766T (line)]] | wt | 101 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.133× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +20.3) | — |
| [[Panc 03.27 (line)]] | alt | 88.7 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.147× (z -13.7) |
| [[J82 (line)]] | alt | 24.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 37.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.209× (z -10.4) |
| [[KATO III (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +17.5) | — |
| [[RPMI-7951 (line)]] | alt | 57.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -10.3) |
| [[SW 900 (line)]] | alt | 64.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.6) |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.120× (z -9.2) |
| [[A-427 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.87 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.73 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFB]] | +0.81 | +0.77 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GBP4]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 853; ⚠ same locus (30.7 kb, same strand: neighbours can correlate without regulation) |
| [[GBP1]] | +0.72 | +0.70 / +0.75 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 967; ⚠ same locus (40.8 kb, same strand: neighbours can correlate without regulation) |
| [[TNFSF10]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 | STRING 474 |
| [[BDKRB2]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[B2M]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 487 |
| [[MVP-DT]] | +0.68 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[TMEM140]] | +0.68 | +0.64 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[EFNA1]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[CFH]] | +0.67 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 419 |
| [[TRANK1]] | +0.67 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[BMF]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGA2]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[DPY19L3]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CAPRIN2]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[NBPF15]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 40, C 19. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAF]] | B | MAF activity raises GBP2's level | lines that do not express MAF (27) vs lines expressing it (23) | 3.65× lower at baseline in the lines without MAF | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[TNFSF10]] | B | TNFSF10 activity raises GBP2's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 3.06× lower at baseline in the lines without TNFSF10 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[FYB1]] | B | FYB1 activity raises GBP2's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 3.68× lower at baseline in the lines without FYB1 | 0.004 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[SPINK1]] | B | SPINK1 activity raises GBP2's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 2.95× lower at baseline in the lines without SPINK1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[MMP13]] | B | MMP13 activity raises GBP2's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without MMP13 | 0.005 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[IFI16]] | B | IFI16 activity raises GBP2's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 3.69× lower at baseline in the lines without IFI16 | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[NLRC5]] | B | NLRC5 activity raises GBP2's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 5.17× lower at baseline in the lines without NLRC5 | 0.006 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[TNFAIP6]] | B | TNFAIP6 activity raises GBP2's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 3.12× lower at baseline in the lines without TNFAIP6 | 0.009 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[GATA6]] | B | GATA6 activity raises GBP2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 3.01× lower at baseline in the lines without GATA6 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[APOL3]] | B | APOL3 activity raises GBP2's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 4.29× lower at baseline in the lines without APOL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[CASP10]] | B | CASP10 activity raises GBP2's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without CASP10 | 0.011 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[SAMD9L]] | B | SAMD9L activity raises GBP2's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.57× lower at baseline in the lines without SAMD9L | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |

### Downstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 52, C 15. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A15]] | B | GBP2 activity lowers SLC25A15's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.78× higher at baseline in the lines without GBP2 | 0.002 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[MVP]] | B | GBP2 activity raises MVP's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without GBP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[TNFSF10]] | B | GBP2 activity raises TNFSF10's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 4.34× lower at baseline in the lines without GBP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[NEURL3]] | B | GBP2 activity raises NEURL3's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[ATP1B1]] | B | GBP2 activity raises ATP1B1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.85× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[NLRC5]] | B | GBP2 activity raises NLRC5's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[CTNND1]] | B | GBP2 activity raises CTNND1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[CASP10]] | B | GBP2 activity raises CASP10's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.83× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[ELF3]] | B | GBP2 activity raises ELF3's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.85× lower at baseline in the lines without GBP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[B2M]] | B | GBP2 activity raises B2M's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without GBP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[BCL3]] | B | GBP2 activity raises BCL3's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without GBP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[ALPK1]] | B | GBP2 activity raises ALPK1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without GBP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.4, 49.9); signed map (60.6, 28.1). **Vector** length 157, 54.7% of its response variance represented; |z| ≥ 3 in 1,674 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.55 to 25); *Antigen processing-Cross presentation* (reactome, mean cos +0.53 to 14); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +10.3 | +16.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +10.0 | +14.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +8.9 | +14.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +8.8 | +12.9 |
|  | [[Trametinib (drug)]] 5 µM |  | +8.6 | +15.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +8.0 | +12.1 |
| fall | [[Budesonide (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.2 | -5.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.1 | -8.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.6 | -5.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.6 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | guanylate binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:89,106,132-89,150,456 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Guanylate binding proteins |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, ALLOGRAFT_REJECTION |
| Reactome | 12 pathways, smallest: CASP4 inflammasome assembly; Enterobacterial factors antagonize host defense; GBP-mediated host defense |
| Matched by | ensembl_id |

**Function**, from UniProt [P32456](https://www.uniprot.org/uniprotkb/P32456) (Guanylate-binding protein 2):

> Interferon (IFN)-inducible GTPase that plays important roles in innate immunity against a diverse range of bacterial, viral and protozoan pathogens. Hydrolyzes GTP to GMP in 2 consecutive cleavage reactions, but the major reaction product is GDP. Following infection, recruited to the pathogen-containing vacuoles or vacuole-escaped bacteria and acts as a positive regulator of inflammasome assembly by promoting the release of inflammasome ligands from bacteria (By similarity). Acts by promoting …

**Summary**, from NCBI Gene [2634](https://www.ncbi.nlm.nih.gov/gene/2634):

> This gene belongs to the guanine-binding protein (GBP) family, which includes interferon-induced proteins that can bind to guanine nucleotides (GMP, GDP and GTP). The encoded protein is a GTPase which hydrolyzes GTP, predominantly to GDP. The protein may play a role as a marker of squamous cell carcinomas. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:4183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4183) · Entrez [2634](https://www.ncbi.nlm.nih.gov/gene/2634) · UniProt [P32456](https://www.uniprot.org/uniprotkb/P32456) · Ensembl [ENSG00000162645](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162645)

## Data

Gene col 8554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8554); `tables/drug_effects.parquet` (119 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8554]; `tensor/DDL_lfc|DDL_z.npy` [8554]; `embed/gene_vectors.npy` [8554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8554 or target_col == 8554). Every well: [[GBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
