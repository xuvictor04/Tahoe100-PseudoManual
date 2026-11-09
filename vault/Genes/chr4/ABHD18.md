---
symbol: "ABHD18"
type: "gene"
col: 8856
ensembl_id: "ENSG00000164074"
name: "abhydrolase domain containing 18"
location: "4q28.2"
module: 131
arm: "+"
pooled_cpm: 68.89
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# ABHD18

*abhydrolase domain containing 18* — 4q28.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +5.2, q 1e-04, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 2.38×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 2.92×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.296× (z -12.4, q 1e-32, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETFDH]] (+0.71, fdr 7e-06), [[TULP3]] (+0.71, fdr 7e-06), [[SEC22A]] (+0.70, fdr 7e-06); moves opposite to [[PUF60]] (-0.64, fdr 7e-06), [[KRT8P12]] (-0.63, fdr 7e-06), [[PURB]] (-0.62, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8856.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 2.38×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 2.92×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.2 | 1e-04 | 29/48 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.093 | 18/49 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.10 | 23/50 (LS 180, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.18× | +3.3 | 0.10 | 15/50 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 1.38× | +3.3 | 0.10 | 14/48 (PANC-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.12 | 17/47 (A549, A498, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.13 | 7/49 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.0 | 0.18 | 15/48 (A498, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.296×** | -12.4 | 1e-32 | 47/49 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.522×** | -11.7 | 3e-29 | 35/45 (KATO III, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.660×** | -11.5 | 4e-28 | 34/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -11.3 | 1e-27 | 39/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.562×** | -11.2 | 3e-27 | 39/49 (HCT15, SW480, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.370×** | -10.1 | 4e-22 | 43/48 (Panc 03.27, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.596×** | -9.7 | 3e-20 | 36/48 (A498, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -9.4 | 3e-19 | 38/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.619×** | -9.4 | 5e-19 | 40/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.649×** | -8.4 | 2e-15 | 31/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.677×** | -7.6 | 1e-12 | 40/48 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.672×** | -7.4 | 5e-12 | 30/42 (H4, A-427, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -7.3 | 1e-11 | 36/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.555×** | -6.0 | 8e-08 | 26/37 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.558×** | -6.0 | 1e-07 | 30/45 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.768×** | -5.2 | 8e-06 | 27/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.808×** | -3.9 | 0.002 | 21/48 (A498, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.845× | -3.1 | 0.041 | 19/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.845× | -3.0 | 0.057 | 20/47 (HS-578T, CHP-212, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.861× | -2.9 | 0.079 | 13/47 (CFPAC-1, SNU-423, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 86.3 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.150× (z -10.4) |
| [[PANC-1 (line)]] | alt | 71.1 | 0 | 7 (6 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.210× (z -11.4) |
| [[A498 (line)]] | wt | 70.3 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -17.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.263× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 63.6 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.353× (z -13.7) |
| [[A549 (line)]] | wt | 59.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -15.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.377× (z -9.9) |
| [[HOP62 (line)]] | alt | 66.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.9) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -8.9) |
| [[HS-578T (line)]] | alt | 48.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 55.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -18.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.182× (z -10.6) |
| [[A-427 (line)]] | wt | 62.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.390× (z -10.4) |
| [[HCT15 (line)]] | alt | 139 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0349× (z -33.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 74.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 53.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.9) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -9.8) |
| [[SW480 (line)]] | alt | 59.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -10.9) |
| [[A-172 (line)]] | wt | 57.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -20.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -10.5) |
| [[C32 (line)]] | wt | 48.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.332× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 83.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.385× (z -11.1) |
| [[H4 (line)]] | wt | 85.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 37.4 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -9.9) |
| [[SNU-423 (line)]] | alt | 52.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -15.4) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.503× (z -9.3) |
| [[Hs 766T (line)]] | wt | 67.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[KATO III (line)]] | alt | 88.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -17.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 83.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 57.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -9.0) |
| [[SW 1088 (line)]] | alt | 88.4 | 0 | 2 | — | [[Meloxicam (drug)]] 0.5 µM 0.0607× (z -10.9) |
| [[AN3 CA (line)]] | alt | 53.6 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.172× (z -9.7) |
| [[C-33 A (line)]] | alt | 94.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 63.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[J82 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -12.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 92.1 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 71.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.144× (z -10.5) |
| [[SW 900 (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -9.7) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SW1417 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -8.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[AsPC-1 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 68.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFDH]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[TULP3]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SEC22A]] | +0.70 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[SNHG25]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[DDT]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[PRKRA]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[FAU]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[DPM3]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TRPC4AP]] | +0.66 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[APTR]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[LUC7L]] | +0.64 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUF60]] | -0.64 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[KRT8P12]] | -0.63 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[PURB]] | -0.62 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.62 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.61 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.61 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ZFP41]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[CEP41]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[FAT1]] | -0.60 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.60 | -0.52 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.8, -31.5); signed map (-40.7, 10.3). **Vector** length 98.7, 28.1% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.55 to 20); *Peptide chain elongation* (reactome, mean cos +0.55 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.55 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.0 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.9 | -8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +0.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.3 | -11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -8.0 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -7.3 | -11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -9.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -12.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -10.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.2 — chr4:127,965,315-128,039,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21106; previously C4orf29 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0P651](https://www.uniprot.org/uniprotkb/Q0P651) (Cardiolipin-specific deacylase, mitochondrial):

> Catalyzes the hydrolysis of an acyl chain from the tetra-acylated cardiolipin (CL) and produces the tri-acylated monolysocardiolipin (MLCL). Prefers CL with shorter and saturated fatty acyl chains as substrates. Together with Tafazzin (TAZ), it participates in the mechanism of CL remodeling, a process consisting of repetitive cycles of hydrolysis and reacylation of the fatty acids that make up CL, where the nascent acyl chains are replaced with longer, unsaturated chains.

**Summary**, from NCBI Gene [80167](https://www.ncbi.nlm.nih.gov/gene/80167):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26111) · Entrez [80167](https://www.ncbi.nlm.nih.gov/gene/80167) · UniProt [Q0P651](https://www.uniprot.org/uniprotkb/Q0P651) · Ensembl [ENSG00000164074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164074)

## Data

Gene col 8856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8856); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8856]; `tensor/DDL_lfc|DDL_z.npy` [8856]; `embed/gene_vectors.npy` [8856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8856 or target_col == 8856). Every well: [[ABHD18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
