---
symbol: "COLGALT1"
type: "gene"
col: 5049
ensembl_id: "ENSG00000130309"
name: "collagen beta(1-O)galactosyltransferase 1"
location: "19p13.11"
module: 50
arm: "+"
pooled_cpm: 37.81
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# COLGALT1

*collagen beta(1-O)galactosyltransferase 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +15.2, q 0e+00, up in 34 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A498 2.74×, PANC-1 2.92×, HS-578T 2.74×, RPMI-7951 3.44×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (Panc 03.27 4.02×, A498 2.42×, SW480 3.25×, LoVo 3.60×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.322× (z -32.1, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A39]] (+0.74, fdr 7e-06), [[ADAM15]] (+0.72, fdr 7e-06), [[TMEM109]] (+0.72, fdr 7e-06); moves opposite to [[TRIP11]] (-0.70, fdr 7e-06), [[NSRP1]] (-0.70, fdr 7e-06), [[SEC62]] (-0.69, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5049.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A498 2.74×, PANC-1 2.92×, HS-578T 2.74×, RPMI-7951 3.44×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (Panc 03.27 4.02×, A498 2.42×, SW480 3.25×, LoVo 3.60×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +15.2 | 0e+00 | 34/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +14.7 | 0e+00 | 34/39 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +9.6 | 2e-19 | 28/41 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +6.8 | 2e-09 | 25/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.23×** | +4.2 | 0.003 | 19/46 (C32, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dexamethasone (drug)]] 5 µM |  | 1.18× | +3.3 | 0.088 | 12/47 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.35× | +3.1 | 0.14 | 9/32 (HEC-1-A, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.322×** | -32.1 | 0e+00 | 44/46 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.376×** | -19.6 | 0e+00 | 42/46 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.380×** | -18.6 | 0e+00 | 43/47 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.650×** | -8.6 | 9e-16 | 36/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.655×** | -8.1 | 4e-14 | 31/47 (H4, A498, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.680×** | -6.8 | 1e-09 | 30/47 (A498, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -6.6 | 4e-09 | 29/47 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.661×** | -4.3 | 0.001 | 18/42 (A-427, J82, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.808×** | -3.9 | 0.005 | 16/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.821×** | -3.9 | 0.005 | 16/47 (SW48, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.878× | -3.7 | 0.012 | 15/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.879× | -3.7 | 0.012 | 9/47 (A549, J82, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.835× | -3.6 | 0.013 | 16/47 (LS 180, A498, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.5 | 0.020 | 14/47 (SW 1088, CFPAC-1, …) | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.852× | -3.2 | 0.050 | 7/47 (KATO III, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.805×** | -3.1 | 0.063 | 7/47 (A-172, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.863× | -3.0 | 0.089 | 15/47 (SW 1088, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 87.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -19.2) |
| [[SNU-423 (line)]] | alt | 48.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.9) |
| [[A-427 (line)]] | wt | 43.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0988× (z -22.3) |
| [[A498 (line)]] | wt | 88.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -21.9) |
| [[HOP62 (line)]] | alt | 35.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -20.3) |
| [[HS-578T (line)]] | alt | 104 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -12.8) |
| [[J82 (line)]] | alt | 70.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -26.3) |
| [[NCI-H460 (line)]] | wt | 24.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 50.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.2) |
| [[PANC-1 (line)]] | alt | 26.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0984× (z -23.7) |
| [[SW480 (line)]] | alt | 20.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.4) |
| [[C32 (line)]] | wt | 41.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -9.5) |
| [[H4 (line)]] | wt | 59.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0805× (z -18.2) |
| [[KATO III (line)]] | alt | 17.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 43.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 66.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -32.1) |
| [[RPMI-7951 (line)]] | alt | 54.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -21.2) |
| [[SK-MEL-2 (line)]] | alt | 47.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -17.4) |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -11.0) |
| [[A549 (line)]] | wt | 25.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 31.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.7) |
| [[C-33 A (line)]] | alt | 46.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.238× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 40.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 37.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.5) |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 35.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 46.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -25.4) |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.2) |
| [[RKO (line)]] | wt | 35.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.6) |
| [[SW48 (line)]] | wt | 54.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.1) |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -11.4) |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 0.05 µM 0.0703× (z -8.9) |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0881× (z -11.1) |
| [[HCT15 (line)]] | alt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.8) |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.5) |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -10.8) |
| [[LoVo (line)]] | wt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -16.5) |
| [[SNU-1 (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 51.0 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0699× (z -9.1) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -11.1) |
| [[AN3 CA (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A39]] | +0.74 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[TMEM109]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[APMAP]] | +0.69 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[NUTF2]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[NAGA]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[AKT1]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[TATDN2]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[CS]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[INTS11]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP11]] | -0.70 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.70 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[SEC62]] | -0.69 | -0.64 / -0.75 | both halves | 7e-06 |  |
| [[UPF3B]] | -0.68 | -0.73 / -0.64 | both halves | 7e-06 |  |
| [[TOPORS]] | -0.68 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.68 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[DCTN6]] | -0.68 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.67 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[MRPS18C]] | -0.67 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[PPIG]] | -0.66 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[RSF1]] | -0.66 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[SNRNP27]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises COLGALT1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without KATNAL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[MXRA7]] | B | MXRA7 activity raises COLGALT1's level | lines that do not express MXRA7 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without MXRA7 | 0.060 | ⚠ within organs, on part of the lines; also absent: FKBP7, KIF3C, SNTA1; its own permutation p |
| [[CERCAM]] | B | CERCAM activity raises COLGALT1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without CERCAM | 0.075 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[FHL1]] | B | FHL1 activity raises COLGALT1's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without FHL1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[LGALS3BP]] | B | LGALS3BP activity lowers COLGALT1's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.37× higher at baseline in the lines without LGALS3BP | 0.090 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[NSRP1]] | C | NSRP1's natural level strengthens COLGALT1's drug response | NSRP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.32; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[P3H1]] | C | P3H1 activity raises COLGALT1's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without P3H1 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.1, -25.6); signed map (-27.1, -41.7). **Vector** length 108, 27.2% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.4 | -18.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -19.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -32.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -8.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | collagen beta(1-O)galactosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,555,649-17,583,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22329; previously GLT25D1 |
| Gene groups (HGNC) | Collagen beta(1-O)galactosyltransferases |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Collagen biosynthesis and modifying enzymes; Collagen formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBJ5](https://www.uniprot.org/uniprotkb/Q8NBJ5) (Procollagen galactosyltransferase 1):

> Beta-galactosyltransferase that transfers beta-galactose to hydroxylysine residues of type I collagen. By acting on collagen glycosylation, facilitates the formation of collagen triple helix. Also involved in the biosynthesis of collagen type IV.

**Summary**, from NCBI Gene [79709](https://www.ncbi.nlm.nih.gov/gene/79709):

> The protein encoded by this gene is one of two enzymes that transfers galactose moieties to hydroxylysine residues of collagen and mannose binding lectin. This gene is constitutively expressed and encodes a soluble protein that localizes to the endoplasmic reticulum. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:26182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26182) · Entrez [79709](https://www.ncbi.nlm.nih.gov/gene/79709) · UniProt [Q8NBJ5](https://www.uniprot.org/uniprotkb/Q8NBJ5) · Ensembl [ENSG00000130309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130309)

## Data

Gene col 5049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5049); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5049]; `tensor/DDL_lfc|DDL_z.npy` [5049]; `embed/gene_vectors.npy` [5049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5049 or target_col == 5049). Every well: [[COLGALT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COLGALT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
