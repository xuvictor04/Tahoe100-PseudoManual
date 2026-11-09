---
symbol: "PIGZ"
type: "gene"
col: 4045
ensembl_id: "ENSG00000119227"
name: "phosphatidylinositol glycan anchor biosynthesis class Z (Gwada blood group)"
location: "3q29"
module: 15
arm: "+"
pooled_cpm: 9.86
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PIGZ

*phosphatidylinositol glycan anchor biosynthesis class Z (Gwada blood group)* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +9.8, q 5e-20, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.260× (z -15.4, q 0e+00, down in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.493× (z -8.1, q 5e-14, down in 24 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STARD7-AS1]] (+0.59, fdr 2e-05), [[PPP1CB-DT]] (+0.58, fdr 3e-05), [[ZNF236-DT]] (+0.58, fdr 3e-05); moves opposite to [[EID1]] (-0.49, fdr 1e-04), [[PCNX2]] (-0.46, fdr 6e-04), [[NEK1]] (-0.45, fdr 7e-04, ⚠ one half only (not replicated)), [[GALNT2]] (-0.45, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITGA9-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.8 | 5e-20 | 32/43 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.006 | 16/45 (LS 180, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.22× | +3.2 | 0.18 | 10/46 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 1.32× | +3.2 | 0.18 | 3/44 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.22× | +3.1 | 0.18 | 10/45 (COLO 205, MIA PaCa-2, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.21× | +3.1 | 0.18 | 7/46 (PANC-1, Panc 03.27, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.19 | 8/47 (SW1417, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4045.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.260×** | -15.4 | 0e+00 | 41/46 (HT-29, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.302×** | -13.2 | 4e-37 | 37/44 (COLO 205, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.480×** | -11.6 | 5e-29 | 28/42 (HT-29, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.378×** | -11.1 | 1e-26 | 35/41 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.422×** | -9.9 | 7e-21 | 29/46 (COLO 205, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.437×** | -9.5 | 3e-19 | 29/46 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.493×** | -8.1 | 5e-14 | 24/40 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.275×** | -7.7 | 8e-13 | 27/43 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.509×** | -7.7 | 8e-13 | 23/45 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.413×** | -7.6 | 2e-12 | 29/44 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.510×** | -7.4 | 7e-12 | 27/36 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.441×** | -7.0 | 1e-10 | 29/45 (SW480, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.552×** | -6.8 | 5e-10 | 24/47 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.570×** | -6.4 | 6e-09 | 25/45 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.576×** | -6.3 | 1e-08 | 23/46 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.517×** | -5.7 | 5e-07 | 24/44 (HT-29, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.593×** | -5.6 | 6e-07 | 19/42 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -5.6 | 6e-07 | 22/44 (HT-29, COLO 205, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.456×** | -4.7 | 8e-05 | 17/39 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.2 | 8e-04 | 21/46 (COLO 205, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.578×** | -3.3 | 0.025 | 12/42 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.706×** | -2.8 | 0.099 | 3/44 (SW 1271, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 41.1 | 0 | 19 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0561× (z -25.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0623× (z -16.7) |
| [[COLO 205 (line)]] | alt | 51.9 | 0 | 11 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0239× (z -20.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0932× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -16.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -16.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -11.1) |
| [[SW480 (line)]] | alt | 9.57 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -13.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -12.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -10.9) |
| [[SNU-1 (line)]] | wt | 26.5 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0550× (z -13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -10.6) |
| [[A-172 (line)]] | wt | 15.6 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.185× (z -9.4) |
| [[HOP62 (line)]] | alt | 9.43 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0550× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 4.71 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0299× (z -15.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 6.78 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0427× (z -19.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -15.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0827× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0734× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[BT-474 (line)]] | alt | 6.44 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -10.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 6.37 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 8.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 6.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0450× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 8.73 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0723× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD7-AS1]] | +0.59 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PPP1CB-DT]] | +0.58 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZNF236-DT]] | +0.58 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[SLC12A9]] | +0.57 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[SIAH1]] | +0.57 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[H3-3A-DT]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[MLYCD]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[PPP1R26-AS1]] | +0.54 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[ZNF816-ZNF321P]] | +0.52 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[DENND10]] | +0.52 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[SEC24B-AS1]] | +0.52 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[SPESP1]] | +0.52 | +0.38 / +0.46 | both halves | 7e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID1]] | -0.49 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PCNX2]] | -0.46 | -0.22 / -0.51 | both halves | 6e-04 |  |
| [[NEK1]] | -0.45 | -0.20 / -0.53 | ⚠ one half (not replicated) | 7e-04 |  |
| [[GALNT2]] | -0.45 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[PLTP]] | -0.44 | -0.46 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA9-AS1]] | B | ITGA9-AS1 activity raises PIGZ's level | lines that do not express ITGA9-AS1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without ITGA9-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CTDSPL, SLC43A2; maybe low, not absent |
| [[IL17RE]] | B | IL17RE activity raises PIGZ's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without IL17RE | 0.089 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.7, 22.6); signed map (33.4, -7.5). **Vector** length 69.9, 12.9% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | -0.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.7 | -11.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.4 | +2.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.9 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -7.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.4 | +0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class Z (Gwada blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,946,356-196,969,060 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12768, MGC52163, SMP3, hSMP3, PIG-Z, GPI-MT-IV |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases; Blood group antigens; Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VD9](https://www.uniprot.org/uniprotkb/Q86VD9) (GPI alpha-1,2-mannosyltransferase 4):

> Alpha-1,2-mannosyltransferase that catalyzes the transfer of the fourth mannose, via an alpha-1,2 bond, from a dolichol-phosphate-mannose (Dol-P-Man) to a 2-acyl-6-[alpha-D-mannosyl-(1->2)-alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H6) intermediate to generate a …

**Summary**, from NCBI Gene [80235](https://www.ncbi.nlm.nih.gov/gene/80235):

> The glycosylphosphatidylinositol (GPI) anchor is a glycolipid found on many blood cells that serves to anchor proteins to the cell surface. This gene encodes a protein that is localized to the endoplasmic reticulum, and is involved in GPI anchor biosynthesis. As shown for the yeast homolog, which is a member of a family of dolichol-phosphate-mannose (Dol-P-Man)-dependent mannosyltransferases, this protein can also add a side-branching fourth mannose to GPI precursors during the assembly of GPI …

**Accessions** — [HGNC:30596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30596) · Entrez [80235](https://www.ncbi.nlm.nih.gov/gene/80235) · UniProt [Q86VD9](https://www.uniprot.org/uniprotkb/Q86VD9) · Ensembl [ENSG00000119227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119227)

## Data

Gene col 4045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4045); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4045]; `tensor/DDL_lfc|DDL_z.npy` [4045]; `embed/gene_vectors.npy` [4045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4045 or target_col == 4045). Every well: [[PIGZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
