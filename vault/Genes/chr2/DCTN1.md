---
symbol: "DCTN1"
type: "gene"
col: 12925
ensembl_id: "ENSG00000204843"
name: "dynactin subunit 1"
location: "2p13.1"
module: 25
arm: "+"
pooled_cpm: 48.01
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DCTN1

*dynactin subunit 1* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.93× (z +14.8, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.39× (z +4.6, q 5e-04, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (PANC-1 4.49×, A498 4.03×, A549 4.08×, LS 180 4.93×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 4.07×, A498 3.84×, NCI-H460 4.03×, LoVo 3.94×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 3.55×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.631× (z -9.3, q 6e-18, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.681× (z -5.5, q 7e-06, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4H]] (+0.79, fdr 7e-06), [[NONO]] (+0.72, fdr 7e-06), [[TAF6]] (+0.72, fdr 7e-06); moves opposite to [[ERVK3-1]] (-0.65, fdr 1e-05), [[SNHG9]] (-0.63, fdr 1e-05), [[RBX1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DSG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12925.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (PANC-1 4.49×, A498 4.03×, A549 4.08×, LS 180 4.93×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 4.07×, A498 3.84×, NCI-H460 4.03×, LoVo 3.94×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 3.55×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +14.8 | 0e+00 | 42/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +14.3 | 7e-44 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +9.8 | 3e-20 | 40/44 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.29×** | +5.2 | 4e-05 | 29/48 (SK-MEL-2, KATO III, …) | rises with dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.6 | 5e-04 | 26/48 (PANC-1, A498, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.25× | +3.3 | 0.10 | 18/47 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.14 | 17/48 (A-172, SW1417, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.631×** | -9.3 | 6e-18 | 39/48 (LOX-IMVI, H4, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -8.2 | 1e-13 | 42/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -5.5 | 7e-06 | 37/48 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.698×** | -5.0 | 8e-05 | 38/48 (SW 1088, HepG2/C3A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.712×** | -4.9 | 1e-04 | 30/48 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.728×** | -4.5 | 5e-04 | 29/48 (RKO, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.747×** | -4.1 | 0.004 | 29/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.767×** | -3.6 | 0.019 | 22/48 (AN3 CA, HEC-1-A, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.801×** | -3.2 | 0.086 | 24/48 (HT-29, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.802×** | -3.2 | 0.086 | 19/47 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.803×** | -3.1 | 0.086 | 19/48 (SW 1088, A498, …) | rises with dose | position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | 0.810× | -3.0 | 0.12 | 18/48 (SW 1271, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 79.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 58.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +14.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.89× (z +10.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 34.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -8.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 31.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +12.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.389× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 34.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.93× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 51.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 57.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +16.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 52.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 41.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 54.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 69.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 59.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +13.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 46.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.4) |
| [[HOP62 (line)]] | alt | 41.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 69.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.85× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 54.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 37.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +13.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 38.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.158× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 35.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.198× (z -9.9) |
| [[C32 (line)]] | wt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +8.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 43.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.17× (z +10.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +10.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 65.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4H]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[NONO]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TAF6]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins |
| [[DHFR]] | +0.72 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[PRPF8]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.71 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[EIF3C]] | +0.70 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.69 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[RPSA]] | +0.69 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[EEF1A1]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 | STRING 635 |
| [[EMC1]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.68 | +0.48 / +0.77 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK3-1]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[SNHG9]] | -0.63 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[RBX1]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 | pathway: G2/M Transition |
| [[RPL36AL]] ⚠ | -0.62 | -0.44 / -0.67 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM258]] | -0.62 | -0.42 / -0.67 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation |
| [[MRPL36]] | -0.61 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.61 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | -0.60 | -0.37 / -0.65 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZBTB7A]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[MRPL23]] | -0.59 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[KRT10]] ⚠ | -0.58 | -0.50 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SPATC1]] | -0.58 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSG2]] | B | DSG2 activity lowers DCTN1's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 1.35× higher at baseline in the lines without DSG2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[MYO5A]] | B | MYO5A activity raises DCTN1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without MYO5A | 0.060 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[IL27RA]] | C | IL27RA activity raises DCTN1's level | lines that do not express IL27RA (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without IL27RA | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ITGA2B, TMEM132A, CLEC2D; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.3, -23.3); signed map (-20.6, -36.4). **Vector** length 125, 35.3% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +9.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.9 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.8 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.1 | -9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -8.2 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -4.2 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -5.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[Decitabine (drug)]] 0.5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | dynactin subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,361,154-74,392,087 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Dynactin subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 40 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; XBP1(S) activates chaperone genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14203](https://www.uniprot.org/uniprotkb/Q14203) (Dynactin subunit 1):

> Part of the dynactin complex that activates the molecular motor dynein for ultra-processive transport along microtubules (By similarity). Plays a key role in dynein-mediated retrograde transport of vesicles and organelles along microtubules by recruiting and tethering dynein to microtubules. Binds to both dynein and microtubules providing a link between specific cargos, microtubules and dynein. Essential for targeting dynein to microtubule plus ends, recruiting dynein to membranous cargos and …

**Summary**, from NCBI Gene [1639](https://www.ncbi.nlm.nih.gov/gene/1639):

> This gene encodes the largest subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. Dynactin is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positioning, and axonogenesis. This subunit interacts with dynein intermediate chain by its domains …

**Accessions** — [HGNC:2711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2711) · Entrez [1639](https://www.ncbi.nlm.nih.gov/gene/1639) · UniProt [Q14203](https://www.uniprot.org/uniprotkb/Q14203) · Ensembl [ENSG00000204843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204843)

## Data

Gene col 12925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12925); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12925]; `tensor/DDL_lfc|DDL_z.npy` [12925]; `embed/gene_vectors.npy` [12925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12925 or target_col == 12925). Every well: [[DCTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
