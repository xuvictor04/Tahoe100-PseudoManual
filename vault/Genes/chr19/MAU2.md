---
symbol: "MAU2"
type: "gene"
col: 5008
ensembl_id: "ENSG00000129933"
name: "MAU2 sister chromatid cohesion factor"
location: "19p13.11"
module: 149
arm: "+"
pooled_cpm: 34.28
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# MAU2

*MAU2 sister chromatid cohesion factor* — 19p13.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.386× (z -15.9, q 0e+00, down in 31 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.601× (z -12.8, q 4e-35, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3HC1]] (+0.77, fdr 7e-06), [[ALKBH1]] (+0.73, fdr 7e-06), [[ZNF721]] (+0.71, fdr 7e-06); moves opposite to [[TFRC]] (-0.66, fdr 1e-05), [[COLGALT1]] (-0.61, fdr 3e-05), [[NPTN]] (-0.61, fdr 3e-05).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.24× | +3.7 | 0.11 | 17/48 (C32, CFPAC-1, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.21× | +3.3 | 0.21 | 6/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.3 | 0.21 | 7/48 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.20× | +3.1 | 0.29 | 9/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.29 | 9/48 (NCI-H1792, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.386×** | -15.9 | 0e+00 | 31/38 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.435×** | -14.7 | 0e+00 | 40/47 (A-427, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.433×** | -13.7 | 2e-40 | 33/43 (HCT15, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -12.8 | 4e-35 | 42/48 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.483×** | -12.7 | 4e-35 | 45/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.502×** | -12.2 | 3e-32 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.517×** | -11.7 | 1e-29 | 48/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.508×** | -11.3 | 7e-28 | 40/47 (COLO 205, A-172, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.646×** | -7.7 | 7e-13 | 37/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.666×** | -7.2 | 3e-11 | 34/48 (NCI-H1792, A-427, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -7.2 | 4e-11 | 38/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.670×** | -7.1 | 6e-11 | 31/47 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.724×** | -5.6 | 7e-07 | 26/48 (LoVo, SHP-77, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.748×** | -4.8 | 5e-05 | 22/48 (A-427, RKO, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.618×** | -4.2 | 8e-04 | 20/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.786×** | -4.2 | 8e-04 | 20/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.794×** | -4.1 | 0.002 | 23/48 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.657×** | -3.7 | 0.006 | 17/47 (A549, A-427, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.670×** | -3.5 | 0.011 | 14/48 (A549, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.011 | 14/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.674×** | -3.5 | 0.012 | 13/48 (NCI-H460, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.018 | 14/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.705×** | -3.1 | 0.041 | 8/48 (SW 1271, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.844× | -3.0 | 0.054 | 10/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.059 | 12/48 (LS 180, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.4 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.9) |
| [[SW480 (line)]] | alt | 42.9 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.333× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.492× (z -8.5) |
| [[A-172 (line)]] | wt | 47.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 42.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 65.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.8) |
| [[HS-578T (line)]] | alt | 39.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0929× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 32.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -8.5) |
| [[A-427 (line)]] | wt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 34.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.4) |
| [[HCT15 (line)]] | alt | 51.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0777× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 24.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -8.6) |
| [[LoVo (line)]] | wt | 31.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0739× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[PANC-1 (line)]] | alt | 30.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 54.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.4) |
| [[SW1417 (line)]] | alt | 32.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[COLO 205 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -14.1) ⚠ toxic |
| [[H4 (line)]] | wt | 51.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0993× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0787× (z -9.0) |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[LS 180 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -10.3) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A498 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3HC1]] | +0.77 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.73 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[N4BP2L2]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[GPATCH8]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | STRING 402 |
| [[SETDB1]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | STRING 489 |
| [[ABRAXAS2]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[IP6K1]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[RPAP1]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFRC]] | -0.66 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.61 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[NPTN]] | -0.61 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[STT3B]] | -0.60 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[C12orf75]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[DPY19L1]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.2, 5.6); signed map (-3.9, -14.9). **Vector** length 90.7, 22.3% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | -0.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.9 | -13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -4.0 | -14.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | MAU2 sister chromatid cohesion factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,320,829-19,358,754 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC75361, mau-2, MAU2L, SCC4; previously KIAA0892 |
| Reactome | 5 pathways, smallest: Cohesin Loading onto Chromatin; Mitotic Telophase/Cytokinesis; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6X3](https://www.uniprot.org/uniprotkb/Q9Y6X3) (MAU2 chromatid cohesion factor homolog):

> Plays an important role in the loading of the cohesin complex on to DNA. Forms a heterodimeric complex (also known as cohesin loading complex) with NIPBL/SCC2 which mediates the loading of the cohesin complex onto chromatin. Plays a role in sister chromatid cohesion and normal progression through prometaphase.

**Summary**, from NCBI Gene [23383](https://www.ncbi.nlm.nih.gov/gene/23383):

> Enables cohesin loader activity. Involved in maintenance of mitotic sister chromatid cohesion. Located in chromatin and nuclear body. Part of Scc2-Scc4 cohesin loading complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29140) · Entrez [23383](https://www.ncbi.nlm.nih.gov/gene/23383) · UniProt [Q9Y6X3](https://www.uniprot.org/uniprotkb/Q9Y6X3) · Ensembl [ENSG00000129933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129933)

## Data

Gene col 5008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5008); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5008]; `tensor/DDL_lfc|DDL_z.npy` [5008]; `embed/gene_vectors.npy` [5008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5008 or target_col == 5008). Every well: [[MAU2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAU2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
