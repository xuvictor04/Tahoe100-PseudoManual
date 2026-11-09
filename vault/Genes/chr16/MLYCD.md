---
symbol: "MLYCD"
type: "gene"
col: 2325
ensembl_id: "ENSG00000103150"
name: "malonyl-CoA decarboxylase"
location: "16q23.3"
module: 15
arm: "+"
pooled_cpm: 11.44
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MLYCD

*malonyl-CoA decarboxylase* — 16q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.67× (z +14.9, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.311× (z -12.4, q 9e-33, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.660× (z -4.4, q 6e-04, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABL2A]] (+0.62, fdr 2e-05), [[CDNF]] (+0.60, fdr 1e-05), [[STARD7-AS1]] (+0.60, fdr 1e-05); moves opposite to [[MAPRE2]] (-0.59, fdr 1e-04), [[RADX]] (-0.55, fdr 4e-05), [[TMEM14A]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +14.9 | 0e+00 | 42/43 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +8.4 | 1e-14 | 33/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +6.7 | 3e-09 | 32/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +5.1 | 5e-05 | 21/45 (LoVo, SW480, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 9e-05 | 24/47 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.4 | 1e-03 | 22/47 (SW480, KATO III, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.003 | 18/47 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.004 | 15/45 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.004 | 19/48 (A-427, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.015 | 10/47 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.018 | 15/46 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.070 | 9/48 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.34× | +3.0 | 0.12 | 7/48 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.311×** | -12.4 | 9e-33 | 42/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.375×** | -10.4 | 4e-23 | 38/44 (KATO III, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.465×** | -8.1 | 8e-14 | 37/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.473×** | -7.3 | 3e-11 | 31/45 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.489×** | -7.0 | 3e-10 | 28/39 (SHP-77, COLO 205, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.597×** | -5.5 | 4e-06 | 26/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.635×** | -4.8 | 1e-04 | 22/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.644×** | -4.7 | 2e-04 | 17/34 (SHP-77, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.653×** | -4.5 | 4e-04 | 22/46 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -4.4 | 6e-04 | 24/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -4.2 | 0.002 | 21/48 (LoVo, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.492×** | -3.9 | 0.004 | 20/46 (NCI-H1573, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -3.8 | 0.007 | 20/47 (PANC-1, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -3.7 | 0.008 | 18/47 (RKO, A498, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.525×** | -3.6 | 0.013 | 13/42 (SW 900, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.00 | 1 | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.235× (z -9.2) |
| [[LoVo (line)]] | wt | 13.6 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 24.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.0568× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 11.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.130× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 19.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0673× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 7.99 | 0 | 2 | — | [[Oxaprozin (drug)]] 5 µM 0.0641× (z -9.5) |
| [[HT-29 (line)]] | alt | 8.82 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0952× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0420× (z -16.8) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 7.25 | 0 | 2 | — | [[Neratinib (drug)]] 0.05 µM 0.0752× (z -10.2) |
| [[A-172 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.113× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0463× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.161× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0639× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 8.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0879× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABL2A]] | +0.62 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CDNF]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PDCD6P1]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[GTPBP10]] | +0.59 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PGS1]] | +0.58 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[RABL2B]] | +0.58 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[UBAP1L]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[WASH2P-1]] | +0.56 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ABHD15]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[DNAJC30]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[MRM1]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE2]] | -0.59 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[RADX]] | -0.55 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[TMEM14A]] | -0.54 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CCDC88A]] | -0.51 | -0.16 / -0.50 | ⚠ one half (not replicated) | 0.001 |  |
| [[SPTLC3]] | -0.50 | -0.20 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[CXADR]] | -0.50 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[HPSE]] | -0.49 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[PLS1]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PAFAH1B3]] | -0.49 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[HMGN3]] | -0.49 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[GDF11]] | -0.49 | -0.09 / -0.43 | ⚠ not reproduced | 0.003 |  |
| [[RGS9]] | -0.49 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[ULBP3]] | -0.49 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[MIR181A1HG]] | -0.48 | -0.25 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MLYCD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C8orf88]] | B | C8orf88 activity lowers MLYCD's level | lines that do not express C8orf88 (12) vs lines expressing it (38) | 1.37× higher at baseline in the lines without C8orf88 | 0.020 | ⚠ within organs, on part of the lines; also absent: TUSC3, MAP9, BVES-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.9, 19.5); signed map (29.4, -20.3). **Vector** length 64.2, 11.3% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +14.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.7 | -7.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | malonyl-CoA decarboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.3 — chr16:83,899,115-83,951,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCD, hMCD |
| Gene groups (HGNC) | Decarboxylases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 6 pathways, smallest: Beta-oxidation of very long chain fatty acids; Peroxisomal lipid metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O95822](https://www.uniprot.org/uniprotkb/O95822) (Malonyl-CoA decarboxylase, mitochondrial):

> Catalyzes the conversion of malonyl-CoA to acetyl-CoA. In the fatty acid biosynthesis MCD selectively removes malonyl-CoA and thus assures that methyl-malonyl-CoA is the only chain elongating substrate for fatty acid synthase and that fatty acids with multiple methyl side chains are produced. In peroxisomes it may be involved in degrading intraperoxisomal malonyl-CoA, which is generated by the peroxisomal beta-oxidation of odd chain-length dicarboxylic fatty acids. Plays a role in the metabolic …

**Summary**, from NCBI Gene [23417](https://www.ncbi.nlm.nih.gov/gene/23417):

> The product of this gene catalyzes the breakdown of malonyl-CoA to acetyl-CoA and carbon dioxide. Malonyl-CoA is an intermediate in fatty acid biosynthesis, and also inhibits the transport of fatty acyl CoAs into mitochondria. Consequently, the encoded protein acts to increase the rate of fatty acid oxidation. It is found in mitochondria, peroxisomes, and the cytoplasm. Mutations in this gene result in malonyl-CoA decarboyxlase deficiency. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7150) · Entrez [23417](https://www.ncbi.nlm.nih.gov/gene/23417) · UniProt [O95822](https://www.uniprot.org/uniprotkb/O95822) · Ensembl [ENSG00000103150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103150)

## Data

Gene col 2325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2325); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2325]; `tensor/DDL_lfc|DDL_z.npy` [2325]; `embed/gene_vectors.npy` [2325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2325 or target_col == 2325). Every well: [[MLYCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLYCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
