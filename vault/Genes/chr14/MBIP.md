---
symbol: "MBIP"
type: "gene"
col: 7508
ensembl_id: "ENSG00000151332"
name: "MAP3K12 binding inhibitory protein 1"
location: "14q13.3"
module: 45
arm: "+"
pooled_cpm: 37.99
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# MBIP

*MAP3K12 binding inhibitory protein 1* — 14q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.60× (z +14.1, q 3e-42, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.458× (z -11.5, q 9e-28, down in 36 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.766× (z -3.9, q 0.017, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCOR3]] (+0.69, fdr 7e-06), [[RCHY1]] (+0.68, fdr 7e-06), [[COPS4]] (+0.68, fdr 7e-06); moves opposite to [[GATAD2A]] (-0.68, fdr 7e-06), [[KPNA4]] (-0.64, fdr 1e-05), [[DDX21]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FRG1DP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.60×** | +14.1 | 3e-42 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +13.0 | 3e-36 | 43/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.66×** | +10.3 | 8e-23 | 37/48 (LoVo, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +8.0 | 2e-13 | 32/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +6.5 | 1e-08 | 30/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.2 | 5e-08 | 28/47 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +6.0 | 2e-07 | 30/48 (LoVo, SW480, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +5.3 | 8e-06 | 31/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 25/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.4 | 7e-04 | 29/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 26/48 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 20/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +4.2 | 0.001 | 20/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.1 | 0.002 | 14/34 (NCI-H1573, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +4.0 | 0.002 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.17× | +3.2 | 0.049 | 13/48 (Panc 03.27, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7508.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.458×** | -11.5 | 9e-28 | 36/46 (HCT15, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -7.7 | 4e-12 | 28/39 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.766×** | -3.9 | 0.017 | 18/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.777×** | -3.7 | 0.030 | 21/48 (RPMI-7951, KATO III, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.791×** | -3.4 | 0.056 | 15/48 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -3.4 | 0.056 | 17/48 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.796×** | -3.4 | 0.063 | 17/48 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.3 | 0.078 | 5/49 (CHP-212, Hs 766T, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.809× | -3.1 | 0.10 | 12/48 (C32, LoVo, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.810× | -3.1 | 0.10 | 11/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -3.1 | 0.10 | 20/48 (HEC-1-A, SW 1271, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.812× | -3.1 | 0.10 | 17/48 (H4, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.814× | -3.0 | 0.11 | 13/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 38.8 | 7 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.34× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 65.7 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.60× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 36.8 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +15.0) | — |
| [[BT-474 (line)]] | alt | 111 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.37× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -12.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 24.4 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.09× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.24× (z +13.1) | — |
| [[SW48 (line)]] | wt | 37.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.56× (z +10.4) | — |
| [[A549 (line)]] | wt | 32.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +15.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.94× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -13.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 52.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.37× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 19.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 40.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 31.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.89× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 14.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.89× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 93.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.21× (z +9.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -14.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -13.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 32.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -10.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -14.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -10.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 30.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.274× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -10.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 20.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 94.5 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.87× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~17% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -13.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -15.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[RCHY1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[COPS4]] | +0.68 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[KBTBD3]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[USP33]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SNX2]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[KCTD3]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ACOT8]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[RHOXF1]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[FBXO7]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MRPL22]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.68 | -0.61 / -0.67 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[KPNA4]] | -0.64 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[DDX21]] | -0.63 | -0.53 / -0.64 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[ACTN1]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[BLZF2P]] | -0.59 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[EIF4G3]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[NABP1]] | -0.58 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[NOP2]] | -0.58 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[AATF]] | -0.57 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[WDR4]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PUS1]] | -0.57 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[ETF1]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1DP]] | B | FRG1DP activity lowers MBIP's level | lines that do not express FRG1DP (17) vs lines expressing it (33) | 1.21× higher at baseline in the lines without FRG1DP | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000237596, C9, GLIPR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.7, -24.2); signed map (-24.1, -8.4). **Vector** length 84.8, 20.3% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +1.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MAP3K12 binding inhibitory protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.3 — chr14:36,298,564-36,320,637 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ATAC complex |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS73](https://www.uniprot.org/uniprotkb/Q9NS73) (MAP3K12-binding inhibitory protein 1):

> Functions as part of the ATAC complex, a complex with histone acetyltransferase activity on histones H3 and H4. Inhibits the MAP3K12 activity to induce the activation of the JNK/SAPK pathway. Together with MOCS2B, inhibits the activity of stress kinase EIF2AK2/PKR; this may lead to effects such as suppression of JNK activation and subsequent stress-responsive transcription, or suppression of eIF2a phosphorylation to favor translation.

**Summary**, from NCBI Gene [51562](https://www.ncbi.nlm.nih.gov/gene/51562):

> Enables identical protein binding activity and protein kinase inhibitor activity. Involved in several processes, including positive regulation of JNK cascade; regulation of gene expression; and regulation of tubulin deacetylation. Located in cytosol; nucleolus; and nucleoplasm. Part of ATAC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20427) · Entrez [51562](https://www.ncbi.nlm.nih.gov/gene/51562) · UniProt [Q9NS73](https://www.uniprot.org/uniprotkb/Q9NS73) · Ensembl [ENSG00000151332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151332)

## Data

Gene col 7508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7508); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7508]; `tensor/DDL_lfc|DDL_z.npy` [7508]; `embed/gene_vectors.npy` [7508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7508 or target_col == 7508). Every well: [[MBIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
