---
symbol: "LTV1"
type: "gene"
col: 5718
ensembl_id: "ENSG00000135521"
name: "LTV1 ribosome biogenesis factor"
location: "6q24.2"
module: 1
arm: "+"
pooled_cpm: 31.65
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# LTV1

*LTV1 ribosome biogenesis factor* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.43× (z +15.3, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.812× (z -3.6, q 0.084, down in 9 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.170×, A-427 0.179×, C-33 A 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.284×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BYSL]] (+0.86, fdr 7e-06), [[RRS1]] (+0.81, fdr 7e-06), [[MAK16]] (+0.80, fdr 7e-06); moves opposite to [[MXD1]] (-0.71, fdr 7e-06), [[AAMDC]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC8D]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +15.3 | 0e+00 | 40/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +14.2 | 1e-43 | 43/48 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.11×** | +12.9 | 8e-36 | 47/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.66×** | +12.4 | 4e-33 | 38/48 (LS 180, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +11.4 | 4e-28 | 42/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +11.2 | 3e-27 | 43/46 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.33×** | +10.9 | 1e-25 | 44/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +10.1 | 3e-22 | 43/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.90×** | +9.6 | 5e-20 | 35/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.72×** | +9.3 | 6e-19 | 36/47 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.70×** | +9.1 | 3e-18 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.69×** | +9.0 | 1e-17 | 33/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.72×** | +9.0 | 1e-17 | 39/47 (LoVo, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.68×** | +8.9 | 1e-17 | 32/47 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.73×** | +8.8 | 7e-17 | 30/45 (Panc 03.27, SW480, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +7.3 | 1e-11 | 36/47 (LoVo, NCI-H1573, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.22×** | +7.2 | 2e-11 | 40/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.17×** | +7.0 | 9e-11 | 35/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +7.0 | 9e-11 | 35/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.04×** | +6.5 | 3e-09 | 35/47 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +6.3 | 8e-09 | 28/48 (MIA PaCa-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +6.1 | 2e-08 | 29/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.76×** | +5.1 | 8e-06 | 26/48 (NCI-H1573, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.74×** | +5.0 | 1e-05 | 18/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5718.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.170×, A-427 0.179×, C-33 A 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.284×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.084 | 9/48 (SW 1088, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.813×** | -3.6 | 0.084 | 23/47 (SW48, CHP-212, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.818×** | -3.5 | 0.084 | 14/47 (NCI-H1573, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.814×** | -3.4 | 0.084 | 14/47 (A498, COLO 205, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 5 µM |  | 0.832× | -3.2 | 0.16 | 8/48 (HOP62, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.826× | -3.1 | 0.16 | 10/48 (J82, SW48, …) | inconsistent across doses | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.832× | -3.1 | 0.18 | 8/47 (A-172, HS-578T, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 32.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.02× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.24× (z +9.2) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[CFPAC-1 (line)]] | alt | 8.78 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.24× (z +8.9) | — |
| [[LoVo (line)]] | wt | 35.2 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.47× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +9.4) | — |
| [[A-172 (line)]] | wt | 18.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 56.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 25.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.2) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A549 (line)]] | wt | 23.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[C-33 A (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.45× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +8.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.36× (z +9.0) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.68× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.63× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.51× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.19× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SHP-77 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 67.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.85× (z +9.1) | — |
| [[SW480 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.45× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BYSL]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[RRS1]] | +0.81 | +0.81 / +0.77 | both halves | 7e-06 | STRING 797 |
| [[MAK16]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | STRING 949 |
| [[TCERG1]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[ZNF202]] | +0.78 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[UTP15]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 712 |
| [[GPATCH4]] | +0.78 | +0.75 / +0.77 | both halves | 7e-06 | STRING 530 |
| [[UTP14A]] | +0.77 | +0.77 / +0.78 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 827 |
| [[DDX31]] | +0.76 | +0.73 / +0.78 | both halves | 7e-06 | STRING 473 |
| [[POLR1A]] | +0.76 | +0.76 / +0.79 | both halves | 7e-06 | STRING 415 |
| [[DDX10]] | +0.76 | +0.76 / +0.81 | both halves | 7e-06 | same gene group; STRING 861 |
| [[PNO1]] | +0.76 | +0.75 / +0.77 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD1]] | -0.71 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.67 | -0.57 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8D]] | C | LRRC8D activity raises LTV1's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.864). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.6, -36.6); signed map (-0.6, -44.1). **Vector** length 99.4, 27.9% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.59 to 15); *MYC targets v2* (hallmark, mean cos +0.58 to 10); *Mitochondrial mRNA modification* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +12.9 |
|  | [[EX229 (drug)]] 5 µM |  | +5.4 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.8 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.7 | +7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.7 | +6.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.2 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | LTV1 ribosome biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:143,843,338-143,863,812 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14909, dJ468K18.4; previously C6orf93 |
| Gene groups (HGNC) | SSU processome |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GA3](https://www.uniprot.org/uniprotkb/Q96GA3) (Protein LTV1 homolog):

> Essential for ribosome biogenesis.

**Summary**, from NCBI Gene [84946](https://www.ncbi.nlm.nih.gov/gene/84946):

> Predicted to be involved in ribosomal small subunit biogenesis and ribosomal small subunit export from nucleus. Located in cytosol and nucleoplasm. Implicated in inflammatory poikiloderma with hair abnormalities and acral keratoses. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21173) · Entrez [84946](https://www.ncbi.nlm.nih.gov/gene/84946) · UniProt [Q96GA3](https://www.uniprot.org/uniprotkb/Q96GA3) · Ensembl [ENSG00000135521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135521)

## Data

Gene col 5718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5718); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5718]; `tensor/DDL_lfc|DDL_z.npy` [5718]; `embed/gene_vectors.npy` [5718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5718 or target_col == 5718). Every well: [[LTV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
