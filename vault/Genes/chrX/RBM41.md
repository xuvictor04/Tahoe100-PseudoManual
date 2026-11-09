---
symbol: "RBM41"
type: "gene"
col: 1593
ensembl_id: "ENSG00000089682"
name: "RNA binding motif protein 41"
location: "Xq22.3"
module: 64
arm: "+"
pooled_cpm: 71.94
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# RBM41

*RNA binding motif protein 41* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.41× (z +8.9, q 3e-16, up in 29 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.29× (z +6.9, q 1e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.654× (z -16.2, q 0e+00, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.684× (z -14.5, q 3e-45, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGGT1B]] (+0.66, fdr 1e-05), [[TMLHE]] (+0.65, fdr 1e-05), [[FAM204A]] (+0.65, fdr 1e-05); moves opposite to [[RELL1]] (-0.59, fdr 2e-05), [[TMEM104]] (-0.53, fdr 3e-05), [[ING1]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SRC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +8.9 | 3e-16 | 29/43 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +8.8 | 3e-16 | 32/48 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.23×** | +8.1 | 1e-13 | 27/48 (AsPC-1, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +6.9 | 1e-09 | 33/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +5.8 | 7e-07 | 25/48 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.15× | +3.8 | 0.015 | 13/48 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.7 | 0.015 | 15/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.042 | 9/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.086 | 11/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.654×** | -16.2 | 0e+00 | 38/48 (NCI-H460, SNU-423, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -14.5 | 3e-45 | 33/49 (Panc 03.27, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -14.3 | 2e-44 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.616×** | -13.1 | 4e-37 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -11.1 | 1e-26 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.701×** | -9.2 | 3e-18 | 30/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.738×** | -8.2 | 2e-14 | 32/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.748×** | -7.8 | 3e-13 | 28/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.756×** | -7.5 | 3e-12 | 28/48 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.771×** | -7.0 | 1e-10 | 29/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.816×** | -5.3 | 7e-06 | 23/48 (NCI-H460, NCI-H1573, …) | top dose only | composition shift; position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.772×** | -3.7 | 0.011 | 11/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.873× | -3.7 | 0.011 | 12/48 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.882× | -3.4 | 0.032 | 14/48 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.918× | -3.2 | 0.046 | 8/49 (CFPAC-1, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 96.2 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -26.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.385× (z -16.1) |
| [[PANC-1 (line)]] | alt | 57.0 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -19.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -18.5) |
| [[SNU-423 (line)]] | alt | 105 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -22.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.487× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 62.0 | 1 (1 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.42× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -18.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.399× (z -10.9) |
| [[C32 (line)]] | wt | 46.7 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -11.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.3) |
| [[Hs 766T (line)]] | wt | 67.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -14.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -12.9) |
| [[HT-29 (line)]] | alt | 111 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.97× (z +9.8) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.490× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.525× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 56.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -17.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 57.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.454× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 87.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +13.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 101 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.503× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 84.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -14.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.388× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.504× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 99.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.232× (z -10.7) |
| [[A-427 (line)]] | wt | 55.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +10.6) ⚠ cell-cycle shift, explains ~53% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.427× (z -9.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -18.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.2) |
| [[LS 180 (line)]] | wt | 79.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.471× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 45.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 56.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 131 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.568× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.626× (z -8.9) |
| [[A498 (line)]] | wt | 62.2 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[AN3 CA (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 74.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.278× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~88% of this change |
| [[HOP62 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -14.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.454× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -10.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -12.2) |
| [[RKO (line)]] | wt | 51.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 38.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.3) |
| [[SW1417 (line)]] | alt | 79.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.01× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGGT1B]] | +0.66 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[TMLHE]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[FAM204A]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CUL5]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[EFCAB7]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CWC27]] | +0.64 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[IRAK1BP1]] | +0.63 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZFR]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[LINC01278]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[NUDT9]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ZNF383]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[MRPS9]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL1]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[TMEM104]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ING1]] | -0.52 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[POLG]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[BCL2L12]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[LINC01128]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[PRADC1]] | -0.51 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[CFL1]] | -0.51 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[CCNYL1]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TOR1B]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[TRIOBP]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRC]] | B | SRC activity lowers RBM41's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-23.3, 0.3); signed map (-20.0, -21.2). **Vector** length 82.5, 17.8% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.5 | +8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +6.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +4.6 | +3.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.9 | -3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.1 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.1 | -16.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.0 | -7.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.5 | -7.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[vincristine (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:107,052,095-107,118,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11016 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IZ5](https://www.uniprot.org/uniprotkb/Q96IZ5) (RNA-binding protein 41):

> May bind RNA.

**Summary**, from NCBI Gene [55285](https://www.ncbi.nlm.nih.gov/gene/55285):

> Predicted to enable U12 snRNA binding activity and pre-mRNA intronic binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Predicted to be part of U12-type spliceosomal complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25617) · Entrez [55285](https://www.ncbi.nlm.nih.gov/gene/55285) · UniProt [Q96IZ5](https://www.uniprot.org/uniprotkb/Q96IZ5) · Ensembl [ENSG00000089682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089682)

## Data

Gene col 1593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1593); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1593]; `tensor/DDL_lfc|DDL_z.npy` [1593]; `embed/gene_vectors.npy` [1593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1593 or target_col == 1593). Every well: [[RBM41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
