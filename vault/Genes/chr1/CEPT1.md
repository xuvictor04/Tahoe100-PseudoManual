---
symbol: "CEPT1"
type: "gene"
col: 5531
ensembl_id: "ENSG00000134255"
name: "choline/ethanolamine phosphotransferase 1"
location: "1p13.3"
module: 17
arm: "+"
pooled_cpm: 53.12
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CEPT1

*choline/ethanolamine phosphotransferase 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.21× (z +4.9, q 6e-04, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 2.12×, PANC-1 1.64×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.62×; ⚠ position not correctable); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.99×); [[Binimetinib (drug)]] 5 µM in 1 line (MIA PaCa-2 2.44×); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.09×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.597× (z -13.2, q 3e-37, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.133×, SW48 0.169×, SW1417 0.317×, HCT15 0.249×, …; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 3 lines (SNU-1 0.187×, NCI-H460 0.433×, SW480 0.501×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.336×, SW480 0.495×, SNU-423 0.411×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS31]] (+0.71, fdr 7e-06), [[PHC3]] (+0.70, fdr 7e-06), [[SUCLG1]] (+0.69, fdr 7e-06); moves opposite to [[GATAD2A]] (-0.60, fdr 1e-05), [[PIP5KL1]] (-0.55, fdr 1e-05), [[VMP1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5531.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 2.12×, PANC-1 1.64×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.62×; ⚠ position not correctable); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.99×); [[Binimetinib (drug)]] 5 µM in 1 line (MIA PaCa-2 2.44×); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.09×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 6e-04 | 21/48 (A-427, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.13× | +4.3 | 0.004 | 5/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.005 | 18/47 (HT-29, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.010 | 19/48 (PANC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.9 | 0.010 | 11/48 (HOP62, LoVo, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.9 | 0.010 | 14/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.15× | +3.8 | 0.012 | 14/49 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.017 | 15/48 (HS-578T, A-172, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.5 | 0.028 | 5/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.4 | 0.041 | 3/48 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.2 | 0.060 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.13× | +3.2 | 0.060 | 7/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.09× | +3.2 | 0.060 | 10/48 (RKO, A549, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.2 | 0.065 | 1/48 (BT-474) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.1 | 0.086 | 13/48 (BT-474, PANC-1, …) | two highest doses | composition shift |
| [[Capivasertib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.086 | 1/48 (Panc 03.27) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.13× | +3.0 | 0.094 | 7/48 (NCI-H23, C-33 A, …) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5531.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.133×, SW48 0.169×, SW1417 0.317×, HCT15 0.249×, …; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 3 lines (SNU-1 0.187×, NCI-H460 0.433×, SW480 0.501×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.336×, SW480 0.495×, SNU-423 0.411×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -13.2 | 3e-37 | 41/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -12.6 | 1e-33 | 36/43 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.657×** | -10.8 | 1e-24 | 33/48 (AN3 CA, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -10.3 | 8e-23 | 29/42 (SK-MEL-2, SW48, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -8.6 | 7e-16 | 29/48 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -7.7 | 1e-12 | 33/47 (hTERT-HPNE, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.815×** | -5.2 | 1e-05 | 24/48 (NCI-H460, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.823×** | -5.0 | 4e-05 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.824×** | -5.0 | 4e-05 | 23/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.828×** | -4.9 | 7e-05 | 24/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.725×** | -4.3 | 9e-04 | 17/44 (SW 900, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.866× | -3.7 | 0.010 | 14/48 (SW480, Hs 766T, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.904× | -3.6 | 0.012 | 8/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.887× | -3.1 | 0.082 | 15/48 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.889× | -3.0 | 0.097 | 17/48 (A498, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.8 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -15.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 80.1 | 7 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +17.1) ⚠ position not correctable · without an alert: [[Elimusertib hydrochloride (drug)]] 0.05 µM 2.99× (z +10.8) | — |
| [[SW480 (line)]] | alt | 62.0 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.495× (z -11.2) |
| [[SW48 (line)]] | wt | 47.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -13.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 56.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0861× (z -12.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 80.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.336× (z -12.0) |
| [[SNU-1 (line)]] | wt | 95.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -13.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 44.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -12.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 74.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -11.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.271× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.150× (z -10.2) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -10.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -16.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 95.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 51.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.411× (z -9.4) |
| [[A-172 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[PHC3]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[SUCLG1]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.68 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[SUPT20H]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MRPL39]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.65 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[UBA3]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RAD52]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[MTX2]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[COQ9]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.60 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[PIP5KL1]] | -0.55 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[VMP1]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[NPC1]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[FBRSL1]] | -0.54 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | -0.54 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[LHX4]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FARP2]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CEPT1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.545). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.9, 4.2); signed map (-18.4, -11.1). **Vector** length 99.2, 22.7% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -12.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.6 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -10.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | choline/ethanolamine phosphotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:111,139,479-111,185,104 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 5 pathways, smallest: Synthesis of PE; Synthesis of PC; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6K0](https://www.uniprot.org/uniprotkb/Q9Y6K0) (Choline/ethanolaminephosphotransferase 1):

> Catalyzes both phosphatidylcholine and phosphatidylethanolamine biosynthesis from CDP-choline and CDP-ethanolamine, respectively. Involved in protein-dependent process of phospholipid transport to distribute phosphatidyl choline to the lumenal surface. Has a higher cholinephosphotransferase activity than ethanolaminephosphotransferase activity.

**Summary**, from NCBI Gene [10390](https://www.ncbi.nlm.nih.gov/gene/10390):

> This gene codes for a choline/ethanolaminephosphotransferase, which functions in the synthesis of choline- or ethanolamine- containing phospholipids. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:24289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24289) · Entrez [10390](https://www.ncbi.nlm.nih.gov/gene/10390) · UniProt [Q9Y6K0](https://www.uniprot.org/uniprotkb/Q9Y6K0) · Ensembl [ENSG00000134255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134255)

## Data

Gene col 5531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5531); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5531]; `tensor/DDL_lfc|DDL_z.npy` [5531]; `embed/gene_vectors.npy` [5531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5531 or target_col == 5531). Every well: [[CEPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
