---
symbol: "POLD2"
type: "gene"
col: 2787
ensembl_id: "ENSG00000106628"
name: "DNA polymerase delta 2, accessory subunit"
location: "7p13"
module: 6
arm: "+"
pooled_cpm: 27.19
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# POLD2

*DNA polymerase delta 2, accessory subunit* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.31× (z +15.1, q 0e+00, up in 40 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.62× (z +3.1, q 0.073, up in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HEC-1-A 3.74×, A498 3.66×, SW480 3.66×, KATO III 5.66×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 4.01×, PANC-1 3.11×, A498 3.40×, NCI-H1792 6.55×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.726× (z -5.7, q 7e-06, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.272×, MIA PaCa-2 0.429×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.320×, SNU-1 0.251×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.317×, SK-MEL-2 0.393×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLB1L2]] (+0.72, fdr 7e-06), [[CDCA7]] (+0.69, fdr 7e-06), [[SIGMAR1]] (+0.68, fdr 7e-06); moves opposite to [[LINC02951]] (-0.63, fdr 3e-05), [[N4BP2L1]] (-0.63, fdr 6e-05), [[EIF3J-DT]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 14 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HEC-1-A 3.74×, A498 3.66×, SW480 3.66×, KATO III 5.66×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 4.01×, PANC-1 3.11×, A498 3.40×, NCI-H1792 6.55×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.31×** | +15.1 | 0e+00 | 40/44 (HEC-1-A, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.81×** | +12.5 | 1e-33 | 35/38 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.30×** | +8.7 | 7e-16 | 34/41 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +7.3 | 5e-11 | 34/44 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.76×** | +7.1 | 1e-10 | 41/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.67×** | +6.4 | 1e-08 | 38/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.64×** | +6.2 | 4e-08 | 33/48 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.61×** | +6.0 | 1e-07 | 32/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.58×** | +5.8 | 4e-07 | 28/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.41×** | +4.3 | 0.001 | 26/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **1.37×** | +4.0 | 0.003 | 24/46 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~87% of this change | **1.34×** | +3.6 | 0.017 | 19/47 (NCI-H1573, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.31×** | +3.4 | 0.033 | 21/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | 1.19× | +3.1 | 0.073 | 17/48 (HT-29, Hs 766T, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.62×** | +3.1 | 0.073 | 15/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.272×, MIA PaCa-2 0.429×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.320×, SNU-1 0.251×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.317×, SK-MEL-2 0.393×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.726×** | -5.7 | 7e-06 | 30/48 (LoVo, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.805×** | -3.9 | 0.031 | 25/48 (A-427, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.589× | -3.4 | 0.11 | 20/47 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[KATO III (line)]] | alt | 31.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 18.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 42.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 16.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.55× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SNU-423 (line)]] | alt | 21.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW480 (line)]] | alt | 35.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A-172 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-427 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.320× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HS-578T (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HT-29 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LS 180 (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[PANC-1 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[RKO (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.1) |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.251× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1L2]] | +0.72 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.68 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[TTLL12]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[QSOX2]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MSH5]] | +0.66 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RPE]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.66 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TBCD]] | +0.65 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LSM4]] | +0.64 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[XPO5]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02951]] | -0.63 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[N4BP2L1]] | -0.63 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[EIF3J-DT]] | -0.63 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.63 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[LRRC39]] | -0.62 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ATE1OSP]] | -0.62 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CCDC59]] | -0.61 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[PPP1R12A-AS2]] | -0.61 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.61 | -0.69 / -0.36 | both halves | 1e-04 |  |
| [[SLC6A13]] | -0.61 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CFAP53]] | -0.61 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ZNF425]] | -0.60 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises POLD2's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without PODXL2 | 0.001 | ⚠ within organs, on part of the lines |
| [[CDCA7]] | B | CDCA7 activity raises POLD2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without CDCA7 | 0.078 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.589). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-29.0, -33.9); signed map (-29.0, -43.9). **Vector** length 76.4, 18.0% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +4.2 | +7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.1 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +3.3 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.1 | +15.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.6 | +0.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +0.3 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.3 | -0.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase delta 2, accessory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,114,631-44,124,358 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 47 pathways, smallest: Leading Strand Synthesis; Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha) |
| Matched by | ensembl_id |

**Function**, from UniProt [P49005](https://www.uniprot.org/uniprotkb/P49005) (DNA polymerase delta subunit 2):

> Accessory component of both the DNA polymerase delta complex and the DNA polymerase zeta complex. As a component of the trimeric and tetrameric DNA polymerase delta complexes (Pol-delta3 and Pol-delta4, respectively), plays a role in high fidelity genome replication, including in lagging strand synthesis, and repair. Pol-delta3 and Pol-delta4 are characterized by the absence or the presence of POLD4. They exhibit differences in catalytic activity. Most notably, Pol-delta3 shows higher …

**Summary**, from NCBI Gene [5425](https://www.ncbi.nlm.nih.gov/gene/5425):

> This gene encodes the 50-kDa catalytic subunit of DNA polymerase delta. DNA polymerase delta possesses both polymerase and 3' to 5' exonuclease activity and plays a critical role in DNA replication and repair. The encoded protein is required for the stimulation of DNA polymerase delta activity by the processivity cofactor proliferating cell nuclear antigen (PCNA). Expression of this gene may be a marker for ovarian carcinomas. Alternatively spliced transcript variants encoding multiple isoforms …

**Accessions** — [HGNC:9176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9176) · Entrez [5425](https://www.ncbi.nlm.nih.gov/gene/5425) · UniProt [P49005](https://www.uniprot.org/uniprotkb/P49005) · Ensembl [ENSG00000106628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106628)

## Data

Gene col 2787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2787); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2787]; `tensor/DDL_lfc|DDL_z.npy` [2787]; `embed/gene_vectors.npy` [2787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2787 or target_col == 2787). Every well: [[POLD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
