---
symbol: "H2AZ2"
type: "gene"
col: 2694
ensembl_id: "ENSG00000105968"
name: "H2A.Z variant histone 2"
location: "7p13"
module: 22
arm: "+"
pooled_cpm: 103.31
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# H2AZ2

*H2A.Z variant histone 2* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.91× (z +20.5, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +4.4, q 3e-04, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.712× (z -5.1, q 2e-04, down in 37 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.649× (z -3.4, q 0.089, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.531×, A-427 0.517×, A-172 0.496×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0982×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H23 0.409×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOP2A]] (+0.78, fdr 7e-06), [[NCAPD2]] (+0.78, fdr 7e-06), [[STMN1]] (+0.77, fdr 7e-06); moves opposite to [[ZNF581]] (-0.60, fdr 1e-05), [[DNAJC2]] (-0.60, fdr 2e-05), [[NOXRED1]] (-0.59, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.91×** | +20.5 | 0e+00 | 48/49 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.72×** | +19.0 | 0e+00 | 43/44 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.45×** | +13.4 | 8e-39 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.36×** | +12.9 | 1e-35 | 47/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.68×** | +12.7 | 1e-34 | 43/45 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.79×** | +8.7 | 3e-16 | 43/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +8.7 | 3e-16 | 30/48 (SNU-423, A549, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.75×** | +8.4 | 4e-15 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.67×** | +7.4 | 8e-12 | 44/47 (C32, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.60×** | +7.0 | 1e-10 | 38/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.54×** | +6.4 | 6e-09 | 39/48 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.48×** | +5.9 | 2e-07 | 38/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~95% of this change | **1.46×** | +5.7 | 5e-07 | 38/48 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +5.2 | 7e-06 | 31/48 (A549, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.36×** | +4.6 | 2e-04 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.4 | 3e-04 | 26/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +4.2 | 7e-04 | 31/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.011 | 20/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.025 | 18/48 (A-427, HS-578T, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.058 | 19/49 (C32, BT-474, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.085 | 20/48 (HT-29, H4, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +2.8 | 0.098 | 14/48 (A549, A-172, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2694.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.531×, A-427 0.517×, A-172 0.496×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0982×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H23 0.409×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.712×** | -5.1 | 2e-04 | 37/48 (H4, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.668×** | -5.0 | 2e-04 | 33/48 (A498, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -4.8 | 4e-04 | 30/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.802×** | -4.7 | 4e-04 | 27/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.649×** | -3.4 | 0.089 | 24/48 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 0.808× | -3.2 | 0.11 | 28/49 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.861× | -3.2 | 0.11 | 19/48 (HCT15, SW48, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.814× | -3.1 | 0.14 | 24/48 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.0 | 0.16 | 18/49 (H4, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.2 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 146 | 7 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +14.5) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[PANC-1 (line)]] | alt | 136 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SNU-423 (line)]] | alt | 74.0 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW480 (line)]] | alt | 139 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 109 | 5 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Selinexor (drug)]] 5 µM 0.496× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 111 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 97.1 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.35× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 71.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.92× (z +18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AsPC-1 (line)]] | alt | 103 | 4 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.2) ⚠ cell-cycle shift, explains ~51% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.413× (z -9.1) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 166 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Selinexor (drug)]] 0.5 µM 0.306× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 95.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LS 180 (line)]] | wt | 93.3 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +12.3) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H1792 (line)]] | alt | 47.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 134 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.31× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Selinexor (drug)]] 5 µM 0.531× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 63.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CFPAC-1 (line)]] | alt | 52.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 81.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 88.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.24× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW 900 (line)]] | alt | 88.0 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +10.2) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SW1417 (line)]] | alt | 159 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 108 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HEC-1-A (line)]] | alt | 138 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 99.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 56.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LOX-IMVI (line)]] | wt | 71.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 117 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 76.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RPMI-7951 (line)]] | alt | 116 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 119 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Selinexor (drug)]] 5 µM 0.517× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Hs 766T (line)]] | wt | 78.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 81.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 83.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[BT-474 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[CHP-212 (line)]] | wt | 61.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0982× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HCT15 (line)]] | alt | 90.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2030 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SNU-1 (line)]] | wt | 84.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP2A]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[NCAPD2]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[STMN1]] | +0.77 | +0.79 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[ANLN]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[SKA2]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[NCAPH]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[KIF23]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[BIRC5]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KNL1]] | +0.73 | +0.76 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[ECT2]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[NCAPG]] | +0.72 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[RACGAP1]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF581]] | -0.60 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[DNAJC2]] | -0.60 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[NOXRED1]] | -0.59 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[ZNF343]] | -0.59 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises H2AZ2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without NEURL1B | 0.088 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PBK]] | C | PBK activity raises H2AZ2's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without PBK | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.7, -53.9); signed map (-48.0, -44.6). **Vector** length 122, 48.5% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.62 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.56 to 48); *E2F targets* (hallmark, mean cos +0.58 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +6.6 | +12.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +6.2 | +13.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +6.2 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.2 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.8 | +4.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | -9.8 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.6 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -8.2 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.1 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.0 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -5.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | H2A.Z variant histone 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,826,791-44,848,087 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10170, MGC10831, MGC1947; previously H2AV, H2AFV |
| Gene groups (HGNC) | H2A histones |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 108 pathways, smallest: ChAHP complex assembly; DNA methylation; RNA Polymerase I Promoter Opening |
| Matched by | ensembl_id |

**Function**, from UniProt [Q71UI9](https://www.uniprot.org/uniprotkb/Q71UI9) (Histone H2A.V):

> Variant histone H2A which replaces conventional H2A in a subset of nucleosomes. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling. May be …

**Summary**, from NCBI Gene [94239](https://www.ncbi.nlm.nih.gov/gene/94239):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Nucleosomes consist of approximately 146 bp of DNA wrapped around a histone octamer composed of pairs of each of the four core histones (H2A, H2B, H3, and H4). The chromatin fiber is further compacted through the interaction of a linker histone, H1, with the DNA between the nucleosomes to form higher order chromatin structures. This gene encodes a replication-independent …

**Accessions** — [HGNC:20664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20664) · Entrez [94239](https://www.ncbi.nlm.nih.gov/gene/94239) · UniProt [Q71UI9](https://www.uniprot.org/uniprotkb/Q71UI9) · Ensembl [ENSG00000105968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105968)

## Data

Gene col 2694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2694); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2694]; `tensor/DDL_lfc|DDL_z.npy` [2694]; `embed/gene_vectors.npy` [2694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2694 or target_col == 2694). Every well: [[H2AZ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2AZ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
