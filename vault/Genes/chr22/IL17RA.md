---
symbol: "IL17RA"
type: "gene"
col: 10846
ensembl_id: "ENSG00000177663"
name: "interleukin 17 receptor A"
location: "22q11.1"
module: 3
arm: "+"
pooled_cpm: 30.23
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# IL17RA

*interleukin 17 receptor A* — 22q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.19× (z +5.2, q 1e-04, up in 21 of 47 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.34× (z +4.5, q 0.002, up in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 2.47×, PANC-1 1.72×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.535× (z -18.4, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAHD1]] (+0.76, fdr 7e-06), [[ZNF500]] (+0.67, fdr 7e-06), [[NUDT22]] (+0.67, fdr 3e-05); moves opposite to [[CBX5]] (-0.64, fdr 1e-05), [[FAT1]] (-0.64, fdr 7e-06), [[TPM1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYOF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10846.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 2.47×, PANC-1 1.72×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.2 | 1e-04 | 21/47 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 0.002 | 15/47 (SW480, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.11 | 17/47 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.19 | 5/48 (HS-578T, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.24 | 18/48 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.535×** | -18.4 | 0e+00 | 39/47 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.564×** | -11.9 | 3e-30 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -11.2 | 9e-27 | 42/49 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.585×** | -10.7 | 1e-24 | 39/48 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.608×** | -10.3 | 5e-23 | 30/45 (C-33 A, H4, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -10.0 | 2e-21 | 32/47 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -9.4 | 6e-19 | 40/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -8.9 | 6e-17 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -8.5 | 9e-16 | 27/39 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.677×** | -7.8 | 4e-13 | 24/37 (HT-29, Hs 766T, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.727×** | -6.3 | 1e-08 | 30/46 (BT-474, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.739×** | -6.2 | 2e-08 | 25/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.575×** | -6.0 | 8e-08 | 22/47 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.796×** | -4.7 | 1e-04 | 14/48 (SNU-423, AsPC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.4 | 5e-04 | 0/48 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.6 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.286× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 33.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.7) |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.6) |
| [[PANC-1 (line)]] | alt | 23.0 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 38.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.9) |
| [[HCT15 (line)]] | alt | 40.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.6) |
| [[SW480 (line)]] | alt | 27.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.436× (z -9.0) |
| [[A-172 (line)]] | wt | 22.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.4) |
| [[AN3 CA (line)]] | alt | 42.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.114× (z -10.0) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Bicalutamide (drug)]] 0.5 µM 0.143× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 26.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -12.8) |
| [[C-33 A (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 32.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.9) |
| [[H4 (line)]] | wt | 29.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 29.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.7) |
| [[J82 (line)]] | alt | 20.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.9) |
| [[LoVo (line)]] | wt | 33.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 30.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.257× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 26.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 50.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -15.6) |
| [[A-427 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -8.5) |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[C32 (line)]] | wt | 52.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.340× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.341× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 32.2 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.205× (z -8.5) |
| [[SW1417 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAHD1]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[ZNF500]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[NUDT22]] | +0.67 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[ARL8A]] | +0.65 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[GTF3C5]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SCNM1]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[ITPKA]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[RAB11FIP3]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[C8orf76]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[MTF1]] | +0.62 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[GPR89A]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MED10]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX5]] | -0.64 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[FAT1]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[TPM1]] | -0.64 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.63 | -0.49 / -0.66 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[ABLIM1]] | -0.62 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[CDK6]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PLCB4]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CDH2]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 | same gene group |
| [[SRP9]] | -0.60 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[SFPQ]] | -0.60 | -0.31 / -0.69 | both halves | 2e-04 |  |
| [[SEMA3C]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.59 | -0.46 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOF]] | B | MYOF activity strengthens IL17RA's drug response | lines that do not express MYOF (6) vs lines expressing it (43) | the lines without MYOF respond 0.41× as strongly (z diff +2.02); strongest at Dinaciclib 5 µM: 1.16x vs 0.57x (z diff +4.6) | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2; target measured in part of the lines; artifact flags |
| [[EID1]] | C | EID1 activity raises IL17RA's level | lines that do not express EID1 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without EID1 | 0.081 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-13.1, -4.2); signed map (-25.8, 7.0). **Vector** length 89.2, 18.9% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +4.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -5.9 | -10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -5.2 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | -3.7 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.8 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 17 receptor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.1 — chr22:17,084,954-17,115,693 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hIL-17R, IL-17RA, CDw217, CD217; previously IL17R |
| Gene groups (HGNC) | CD molecules; Interleukin receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 8 pathways, smallest: Interleukin-17 signaling; SARS-CoV-2 activates/modulates innate and adaptive immune responses; SARS-CoV-2-host interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F46](https://www.uniprot.org/uniprotkb/Q96F46) (Interleukin-17 receptor A):

> Receptor for IL17A and IL17F, major effector cytokines of innate and adaptive immune system involved in antimicrobial host defense and maintenance of tissue integrity. Receptor for IL17A. Receptor for IL17F. Binds to IL17A with higher affinity than to IL17F. Binds IL17A and IL17F homodimers as part of a heterodimeric complex with IL17RC. Also binds heterodimers formed by IL17A and IL17F as part of a heterodimeric complex with IL17RC. Cytokine binding triggers homotypic interaction of IL17RA and …

**Summary**, from NCBI Gene [23765](https://www.ncbi.nlm.nih.gov/gene/23765):

> Interleukin 17A (IL17A) is a proinflammatory cytokine secreted by activated T-lymphocytes. It is a potent inducer of the maturation of CD34-positive hematopoietic precursors into neutrophils. The transmembrane protein encoded by this gene (interleukin 17A receptor; IL17RA) is a ubiquitous type I membrane glycoprotein that binds with low affinity to interleukin 17A. Interleukin 17A and its receptor play a pathogenic role in many inflammatory and autoimmune diseases such as rheumatoid arthritis. …

**Accessions** — [HGNC:5985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5985) · Entrez [23765](https://www.ncbi.nlm.nih.gov/gene/23765) · UniProt [Q96F46](https://www.uniprot.org/uniprotkb/Q96F46) · Ensembl [ENSG00000177663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177663)

## Data

Gene col 10846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10846); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10846]; `tensor/DDL_lfc|DDL_z.npy` [10846]; `embed/gene_vectors.npy` [10846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10846 or target_col == 10846). Every well: [[IL17RA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL17RA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
