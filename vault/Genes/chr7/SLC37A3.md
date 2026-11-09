---
symbol: "SLC37A3"
type: "gene"
col: 8102
ensembl_id: "ENSG00000157800"
name: "solute carrier family 37 member 3"
location: "7q34"
module: 40
arm: "+"
pooled_cpm: 69.42
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SLC37A3

*solute carrier family 37 member 3* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 5 µM: 1.62× (z +5.3, q 7e-05, up in 28 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.19× (z +5.1, q 1e-04, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 2.19×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.15×); [[Auranofin (drug)]] 5 µM in 1 line (A-427 2.31×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.411× (z -17.9, q 0e+00, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.639× (z -11.7, q 2e-29, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA5]] (+0.75, fdr 7e-06), [[EEF1AKMT4]] (+0.75, fdr 7e-06), [[ZCCHC7]] (+0.74, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.69, fdr 1e-05), [[CSTF2T]] (-0.68, fdr 7e-06), [[ZNF776]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8102.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 2.19×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.15×); [[Auranofin (drug)]] 5 µM in 1 line (A-427 2.31×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.3 | 7e-05 | 28/45 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.1 | 1e-04 | 22/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.20×** | +5.0 | 1e-04 | 22/49 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +4.9 | 1e-04 | 27/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.9 | 1e-04 | 19/49 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +4.7 | 2e-04 | 29/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.6 | 3e-04 | 23/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 0.001 | 27/48 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.002 | 22/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.013 | 18/48 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.16× | +3.2 | 0.072 | 20/48 (CFPAC-1, BT-474, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.073 | 20/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.0 | 0.10 | 16/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.16× | +3.0 | 0.10 | 18/48 (CFPAC-1, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.411×** | -17.9 | 0e+00 | 34/44 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.520×** | -13.7 | 2e-40 | 47/49 (HCT15, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.508×** | -13.1 | 3e-37 | 39/45 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -11.7 | 2e-29 | 39/48 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.619×** | -10.1 | 7e-22 | 36/48 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.673×** | -8.0 | 1e-13 | 35/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -7.4 | 1e-11 | 31/48 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -6.5 | 6e-09 | 32/48 (H4, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.772×** | -5.0 | 3e-05 | 26/47 (C32, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.786×** | -4.9 | 7e-05 | 28/48 (hTERT-HPNE, SNU-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.810×** | -4.4 | 5e-04 | 25/48 (A498, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.829×** | -3.9 | 0.004 | 19/48 (COLO 205, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.4 | 0.033 | 16/48 (HS-578T, RKO, …) | top dose only | low cells (technical?) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.859× | -3.2 | 0.058 | 11/47 (SW 1271, HOP62, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.861× | -3.1 | 0.061 | 14/48 (COLO 205, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.862× | -3.1 | 0.061 | 10/48 (C32, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 123 | 0 | 7 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0502× (z -18.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -17.5) |
| [[hTERT-HPNE (line)]] | wt | 62.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.266× (z -10.6) |
| [[H4 (line)]] | wt | 94.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.280× (z -10.0) |
| [[SW 900 (line)]] | alt | 93.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.1) |
| [[A498 (line)]] | wt | 133 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.350× (z -11.7) |
| [[HS-578T (line)]] | alt | 83.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.5) |
| [[PANC-1 (line)]] | alt | 69.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.19× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -11.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 63.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.1) |
| [[HCT15 (line)]] | alt | 82.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -15.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 92.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -19.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 68.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.8) |
| [[Hs 766T (line)]] | wt | 68.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -11.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 99.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.572× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 91.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 76.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 79.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -9.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 83.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.0) |
| [[SW480 (line)]] | alt | 63.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -14.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 54.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +9.5) | — |
| [[A549 (line)]] | wt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -9.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0864× (z -15.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -11.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 58.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -19.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 58.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.1) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[NCI-H661 (line)]] | alt | 65.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0863× (z -10.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 110 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA5]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.75 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ZCCHC7]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[COG5]] | +0.73 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ELP2]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[BET1L]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MPG]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[RABAC1]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SDF2L1]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.69 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[CSTF2T]] | -0.68 | -0.73 / -0.60 | both halves | 7e-06 |  |
| [[ZNF776]] | -0.67 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[VEZF1]] | -0.67 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[YWHAE]] | -0.66 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[ZNF772]] | -0.66 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.66 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[DDX6]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.64 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.64 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | -0.64 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[TIA1]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers SLC37A3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (3.8, -20.7); signed map (-45.9, 8.3). **Vector** length 127, 36.9% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +5.6 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.6 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +1.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.6 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.5 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 37 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:140,293,693-140,404,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761N0624, SPX3 |
| Gene groups (HGNC) | Solute carrier family 37 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCC5](https://www.uniprot.org/uniprotkb/Q8NCC5) (Sugar phosphate exchanger 3):

> Unlike the other SLC37 members, lacks glucose-6-phosphate antiporter activity. In osteoclasts, forms a transporter complex with ATRAID for nitrogen-containing-bisphosphonates (N-BPs) required for releasing N-BP molecules that have trafficked to lysosomes through fluid-phase endocytosis into the cytosol.

**Summary**, from NCBI Gene [84255](https://www.ncbi.nlm.nih.gov/gene/84255):

> Enables xenobiotic transmembrane transporter activity. Involved in xenobiotic transmembrane transport. Located in endoplasmic reticulum membrane and lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20651) · Entrez [84255](https://www.ncbi.nlm.nih.gov/gene/84255) · UniProt [Q8NCC5](https://www.uniprot.org/uniprotkb/Q8NCC5) · Ensembl [ENSG00000157800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157800)

## Data

Gene col 8102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8102); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8102]; `tensor/DDL_lfc|DDL_z.npy` [8102]; `embed/gene_vectors.npy` [8102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8102 or target_col == 8102). Every well: [[SLC37A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC37A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
