---
symbol: "VPS9D1"
type: "gene"
col: 1116
ensembl_id: "ENSG00000075399"
name: "VPS9 domain containing 1"
location: "16q24.3"
module: 36
arm: "+"
pooled_cpm: 14.12
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# VPS9D1

*VPS9 domain containing 1* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +8.9, q 5e-16, up in 28 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 3.08×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (19 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.403× (z -12.4, q 2e-32, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.757× (z -5.3, q 8e-06, down in 18 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL16]] (+0.59, fdr 1e-05), [[MEF2B]] (+0.59, fdr 3e-05), [[MIR22HG]] (+0.58, fdr 1e-05); moves opposite to [[PPP1CC]] (-0.53, fdr 4e-05), [[CDCA7L]] (-0.50, fdr 3e-05), [[NT5DC1]] (-0.49, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1116.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 3.08×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.9 | 5e-16 | 28/44 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.31× | +3.5 | 0.11 | 12/45 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.28 | 5/48 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Rimonabant (drug)]] 5 µM |  | 1.17× | +3.0 | 0.28 | 3/48 (HOP62, A498, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.28 | 7/41 (COLO 205, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.403×** | -12.4 | 2e-32 | 40/48 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.424×** | -11.7 | 4e-29 | 33/45 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.647×** | -8.4 | 1e-14 | 26/45 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.543×** | -8.3 | 1e-14 | 33/47 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.535×** | -8.2 | 3e-14 | 31/42 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.578×** | -7.5 | 8e-12 | 30/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.572×** | -7.3 | 2e-11 | 26/47 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.757×** | -5.3 | 8e-06 | 18/47 (SW 900, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.683×** | -5.2 | 1e-05 | 24/46 (A-172, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.684×** | -5.2 | 1e-05 | 21/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.689×** | -5.1 | 2e-05 | 26/48 (COLO 205, A-172, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.699×** | -4.8 | 6e-05 | 22/46 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.692×** | -4.8 | 7e-05 | 18/27 (A498, HEC-1-A, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.703×** | -4.8 | 7e-05 | 20/43 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.704×** | -4.8 | 7e-05 | 19/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.711×** | -4.6 | 1e-04 | 19/46 (A-172, LOX-IMVI, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -3.9 | 0.003 | 17/48 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.590×** | -3.7 | 0.005 | 19/42 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.644×** | -3.1 | 0.044 | 10/46 (NCI-H460, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.047 | 5/48 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.796×** | -3.0 | 0.068 | 10/48 (CFPAC-1, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.0) ⚠ cell-cycle shift, explains ~69% of this change |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0694× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 14.9 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0576× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 36.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.8) ⚠ cell-cycle shift, explains ~69% of this change |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -13.4) ⚠ cell-cycle shift, explains ~69% of this change |
| [[NCI-H460 (line)]] | wt | 14.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +11.2) | [[Digitoxin (drug)]] 0.05 µM 0.204× (z -11.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -20.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0811× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -18.3) ⚠ cell-cycle shift, explains ~69% of this change |
| [[J82 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -8.8) ⚠ cell-cycle shift, explains ~69% of this change |
| [[LOX-IMVI (line)]] | wt | 9.15 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0885× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 7.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0800× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.148× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 7.34 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0950× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 9.53 | 0 | 1 | — | [[Altretamine (drug)]] 5 µM 0.0704× (z -8.5) |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL16]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MEF2B]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[MIR22HG]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[RAB43]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ARPC5L]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TRIM39]] | +0.53 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[RAB35]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZNF276]] | +0.52 | +0.45 / +0.58 | both halves | 3e-05 | STRING 694; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RAB11B-AS1]] | +0.52 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[FBXL18]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[LENG8-AS1]] | +0.51 | +0.40 / +0.59 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1CC]] | -0.53 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[CDCA7L]] | -0.50 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[NT5DC1]] | -0.49 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[VPS41]] | -0.49 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[MANEA]] | -0.49 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TMEM64]] | -0.48 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CREG1]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PEG10]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ENPP4]] | -0.47 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[CHIC1]] | -0.47 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[SLC25A30]] | -0.46 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[VPS8]] | -0.46 | -0.39 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.248). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-15.0, -1.6); signed map (-20.1, 0.2). **Vector** length 76.8, 14.5% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.4 | -12.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.8 | -3.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.8 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | VPS9 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,707,134-89,720,898 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATP-BL; previously C16orf7 |
| Gene groups (HGNC) | VPS9 domain containing |
| Matched by | ensembl_id |

UniProt [Q9Y2B5](https://www.uniprot.org/uniprotkb/Q9Y2B5) carries no function annotation.

**Summary**, from NCBI Gene [9605](https://www.ncbi.nlm.nih.gov/gene/9605):

> Predicted to enable guanyl-nucleotide exchange factor activity and small GTPase binding activity. Predicted to be involved in proton motive force-driven ATP synthesis. Predicted to be active in cytosol and endocytic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13526) · Entrez [9605](https://www.ncbi.nlm.nih.gov/gene/9605) · UniProt [Q9Y2B5](https://www.uniprot.org/uniprotkb/Q9Y2B5) · Ensembl [ENSG00000075399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075399)

## Data

Gene col 1116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1116); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1116]; `tensor/DDL_lfc|DDL_z.npy` [1116]; `embed/gene_vectors.npy` [1116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1116 or target_col == 1116). Every well: [[VPS9D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS9D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
