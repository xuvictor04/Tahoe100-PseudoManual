---
symbol: "MCM5"
type: "gene"
col: 1917
ensembl_id: "ENSG00000100297"
name: "minichromosome maintenance complex component 5"
location: "22q12.3"
module: 6
arm: "+"
pooled_cpm: 13.46
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCM5

*minichromosome maintenance complex component 5* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +11.4, q 3e-27, up in 33 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.86× (z +7.9, q 2e-13, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.615× (z -8.8, q 8e-16, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC45]] (+0.89, fdr 7e-06), [[MCM3]] (+0.87, fdr 7e-06), [[MCM2]] (+0.87, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.43×** | +11.4 | 3e-27 | 33/39 (A498, LOX-IMVI, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.21×** | +10.1 | 1e-21 | 32/45 (PANC-1, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.08×** | +8.7 | 8e-16 | 18/28 (LOX-IMVI, A549, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.95×** | +8.5 | 2e-15 | 29/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.96×** | +8.3 | 2e-14 | 12/18 (A498, HS-578T, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.90×** | +8.2 | 2e-14 | 33/46 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +7.9 | 2e-13 | 24/46 (A-172, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.82×** | +7.7 | 1e-12 | 29/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.59×** | +5.7 | 8e-07 | 19/40 (HCT15, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.49×** | +4.9 | 6e-05 | 15/46 (SHP-77, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +4.5 | 3e-04 | 19/46 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +4.4 | 4e-04 | 19/47 (C32, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.26×** | +4.1 | 0.002 | 8/48 (LoVo, LS 180, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.0 | 0.002 | 9/21 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.24×** | +3.9 | 0.004 | 12/48 (LS 180, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.008 | 17/48 (Hs 766T, NCI-H1573, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.015 | 13/47 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.074 | 10/48 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.54×** | +2.9 | 0.086 | 5/40 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.615×** | -8.8 | 8e-16 | 36/48 (KATO III, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.680×** | -7.0 | 8e-10 | 27/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.599×** | -6.6 | 1e-08 | 26/45 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.689×** | -4.8 | 3e-04 | 17/45 (A-427, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.696×** | -4.6 | 4e-04 | 19/45 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -4.2 | 0.002 | 6/48 (MIA PaCa-2, SHP-77, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.714×** | -4.1 | 0.003 | 16/45 (HEC-1-A, A-427, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.814×** | -3.7 | 0.013 | 13/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.023 | 10/48 (RKO, LS 180, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.028 | 15/47 (NCI-H23, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.764×** | -3.4 | 0.029 | 13/47 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.760×** | -3.4 | 0.036 | 18/48 (A-427, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.083 | 11/46 (Panc 03.27, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.631×** | -3.1 | 0.083 | 11/47 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.633×** | -3.1 | 0.083 | 11/44 (Hs 766T, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.86 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 30.6 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.208× (z -14.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -13.6) |
| [[A498 (line)]] | wt | 19.9 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.134× (z -19.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 18.7 | 4 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.18× (z +9.8) ⚠ cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 17.8 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.55× (z +10.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 29.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 37.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +8.9) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0897× (z -9.4) |
| [[KATO III (line)]] | alt | 17.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.285× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 7.89 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 15.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0742× (z -11.4) |
| [[SW48 (line)]] | wt | 15.4 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.153× (z -10.2) |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC45]] | +0.89 | +0.92 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[MCM3]] | +0.87 | +0.90 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[MCM2]] | +0.87 | +0.83 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[WDR76]] | +0.86 | +0.89 / +0.84 | both halves | 7e-06 | STRING 534 |
| [[MCM4]] | +0.86 | +0.83 / +0.83 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[TONSL]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | STRING 655 |
| [[POLE]] | +0.86 | +0.84 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 997 |
| [[CDC25A]] | +0.85 | +0.85 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 556 |
| [[E2F1]] | +0.84 | +0.86 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 728 |
| [[XRCC2]] | +0.84 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.83 | +0.85 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 579 |
| [[CHAF1A]] | +0.83 | +0.87 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 894 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises MCM5's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without CDC25A | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises MCM5's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without E2F2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises MCM5's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without DSCC1 | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.866). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.7, -43.5); signed map (-36.9, -46.4). **Vector** length 109, 27.1% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Homology Directed Repair* (reactome, mean cos +0.68 to 32); *Chromosome Maintenance* (reactome, mean cos +0.67 to 29); *HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA)* (reactome, mean cos +0.69 to 29).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +4.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +4.2 | +8.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.8 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +3.7 | +11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.7 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.6 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -3.8 | -4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.5 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance complex component 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:35,400,134-35,425,431 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CDC46 |
| Gene groups (HGNC) | MCM family; minichromosome maintenance 2-7 complex |
| Hallmark sets | MYC_TARGETS_V2, G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 20 pathways, smallest: Regulation of MITF-M-dependent genes involved in DNA replication, damage repair and senescence; Unwinding of DNA; Activation of the pre-replicative complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P33992](https://www.uniprot.org/uniprotkb/P33992) (DNA replication licensing factor MCM5):

> Acts as a component of the MCM2-7 complex (MCM complex) which is the replicative helicase essential for 'once per cell cycle' DNA replication initiation and elongation in eukaryotic cells. Core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built. The active ATPase sites in the MCM2-7 ring are formed through the interaction surfaces of two neighboring subunits such that a critical structure of a …

**Summary**, from NCBI Gene [4174](https://www.ncbi.nlm.nih.gov/gene/4174):

> The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycle and may actively participate in cell cycle regulation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6948) · Entrez [4174](https://www.ncbi.nlm.nih.gov/gene/4174) · UniProt [P33992](https://www.uniprot.org/uniprotkb/P33992) · Ensembl [ENSG00000100297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100297)

## Data

Gene col 1917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1917); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1917]; `tensor/DDL_lfc|DDL_z.npy` [1917]; `embed/gene_vectors.npy` [1917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1917 or target_col == 1917). Every well: [[MCM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
