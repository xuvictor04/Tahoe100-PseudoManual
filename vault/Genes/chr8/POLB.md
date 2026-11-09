---
symbol: "POLB"
type: "gene"
col: 954
ensembl_id: "ENSG00000070501"
name: "DNA polymerase beta"
location: "8p11.21"
module: 3
arm: "+"
pooled_cpm: 35.57
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# POLB

*DNA polymerase beta* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.78× (z +21.5, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.161×, LOX-IMVI 0.340×, AsPC-1 0.323×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.252×, Panc 03.27 0.344×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.168×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN2D]] (+0.64, fdr 4e-05), [[MRPL41]] (+0.62, fdr 4e-04, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[MIEN1]] (+0.61, fdr 5e-05), [[ETHE1]] (+0.61, fdr 3e-05); moves opposite to [[TUG1]] (-0.60, fdr 3e-04), [[SMCR8]] (-0.59, fdr 5e-05), [[RCN1]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SIGIRR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.78×** | +21.5 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +18.8 | 0e+00 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +18.6 | 0e+00 | 47/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +11.7 | 2e-29 | 34/48 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.54×** | +9.0 | 2e-17 | 34/46 (LoVo, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +6.6 | 4e-09 | 29/48 (HEC-1-A, LoVo, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.4 | 1e-08 | 30/47 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 1e-06 | 23/48 (SW480, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +5.7 | 1e-06 | 25/47 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +5.6 | 1e-06 | 24/48 (Hs 766T, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +5.4 | 3e-06 | 24/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.29×** | +5.1 | 1e-05 | 24/46 (NCI-H2030, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 2e-05 | 23/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.26×** | +4.7 | 1e-04 | 21/46 (LoVo, LS 180, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.6 | 2e-04 | 20/48 (NCI-H23, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.009 | 8/48 (AsPC-1, J82, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.024 | 4/49 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.045 | 7/47 (A-172, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.047 | 9/48 (Hs 766T, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 954.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.161×, LOX-IMVI 0.340×, AsPC-1 0.323×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.252×, Panc 03.27 0.344×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.168×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | 0.842× | -3.6 | 0.16 | 10/48 (A-427, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 52.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 47.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 35.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.59× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 33.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.41× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 41.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 84.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +9.5) | — |
| [[J82 (line)]] | alt | 42.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.8) | — |
| [[LoVo (line)]] | wt | 38.1 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.77× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.29× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 43.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 36.8 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.09× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +11.4) | — |
| [[SW1417 (line)]] | alt | 50.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +11.1) | — |
| [[SW480 (line)]] | alt | 35.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +16.6) | — |
| [[HEC-1-A (line)]] | alt | 42.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 36.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.7) | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.168× (z -10.0) |
| [[PANC-1 (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.8) | — |
| [[A498 (line)]] | wt | 32.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +8.7) | — |
| [[A549 (line)]] | wt | 30.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +8.6) | — |
| [[H4 (line)]] | wt | 32.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.7) | — |
| [[KATO III (line)]] | alt | 34.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 29.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.20× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 15.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +8.5) | — |
| [[SW48 (line)]] | wt | 50.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.8) | — |
| [[A-427 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 15 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | +0.64 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[MRPL41]] ⚠ | +0.62 | +0.26 / +0.58 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MIEN1]] | +0.61 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[ETHE1]] | +0.61 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[RNF114]] | +0.61 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[ELOB]] | +0.61 | +0.24 / +0.58 | both halves | 4e-04 |  |
| [[TMEM191A-1]] | +0.60 | +0.37 / +0.43 | both halves | 9e-05 |  |
| [[POLR2I]] | +0.59 | +0.18 / +0.50 | ⚠ not reproduced | 9e-04 | pathway: HALLMARK_DNA_REPAIR |
| [[C4orf48]] | +0.59 | +0.29 / +0.52 | both halves | 3e-04 |  |
| [[TMEM160]] | +0.59 | +0.23 / +0.51 | both halves | 5e-04 |  |
| [[NDUFA3]] | +0.58 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[PIGH]] | +0.57 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[RPP21]] | +0.57 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[ATP5MJ]] | +0.56 | +0.24 / +0.48 | both halves | 4e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | -0.60 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[SMCR8]] | -0.59 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[RCN1]] | -0.57 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[HNRNPL]] | -0.57 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[UBAP2L]] | -0.57 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.57 | -0.23 / -0.49 | both halves | 5e-04 |  |
| [[U2AF2]] | -0.56 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[ZNF460]] | -0.56 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[SMU1]] | -0.54 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[CFAP418-AS1]] | -0.53 | -0.22 / -0.32 | both halves | 6e-04 |  |
| [[SETD7]] | -0.53 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[DNAJB12]] | -0.53 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIGIRR]] | B | SIGIRR activity lowers POLB's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without SIGIRR | 0.025 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-45.7, -18.4); signed map (-31.2, 8.6). **Vector** length 73.0, 13.9% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.9 | +18.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +21.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +18.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | +1.9 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.2 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,338,454-42,371,808 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DNA polymerases; DNA-(apurinic or apyrimidinic site) lyases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 10 pathways, smallest: Resolution of AP sites via the single-nucleotide replacement pathway; APEX1-Independent Resolution of AP Sites via the Single Nucleotide Replacement Pathway; POLB-Dependent Long Patch Base Excision Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [P06746](https://www.uniprot.org/uniprotkb/P06746) (DNA polymerase beta):

> Repair polymerase that plays a key role in base-excision repair. During this process, the damaged base is excised by specific DNA glycosylases, the DNA backbone is nicked at the abasic site by an apurinic/apyrimidic (AP) endonuclease, and POLB removes 5'-deoxyribose-phosphate from the preincised AP site acting as a 5'-deoxyribose-phosphate lyase (5'-dRP lyase); through its DNA polymerase activity, it adds one nucleotide to the 3' end of the arising single-nucleotide gap. Conducts 'gap-filling' …

**Summary**, from NCBI Gene [5423](https://www.ncbi.nlm.nih.gov/gene/5423):

> The protein encoded by this gene is a DNA polymerase involved in base excision and repair, also called gap-filling DNA synthesis. The encoded protein, acting as a monomer, is normally found in the cytoplasm, but it translocates to the nucleus upon DNA damage. Several transcript variants of this gene exist, but the full-length nature of only one has been described to date. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:9174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9174) · Entrez [5423](https://www.ncbi.nlm.nih.gov/gene/5423) · UniProt [P06746](https://www.uniprot.org/uniprotkb/P06746) · Ensembl [ENSG00000070501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070501)

## Data

Gene col 954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 954); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 954]; `tensor/DDL_lfc|DDL_z.npy` [954]; `embed/gene_vectors.npy` [954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 954 or target_col == 954). Every well: [[POLB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
