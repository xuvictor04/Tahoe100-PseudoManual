---
symbol: "RFC2"
type: "gene"
col: 552
ensembl_id: "ENSG00000049541"
name: "replication factor C subunit 2"
location: "7q11.23"
module: 6
arm: "+"
pooled_cpm: 31.81
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RFC2

*replication factor C subunit 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.35× (z +12.8, q 5e-35, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 1.51× (z +3.2, q 0.043, up in 12 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A549 4.13×, J82 2.66×, A-172 2.37×, A498 1.86×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H460 3.41×, SW480 2.61×, LoVo 3.99×; ⚠ cell-cycle shift, explains ~57% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 2.96×, NCI-H1573 3.77×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 0.833× (z -3.9, q 0.032, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.314×, C32 0.415×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.254×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.226×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM10]] (+0.81, fdr 7e-06), [[GINS2]] (+0.81, fdr 7e-06), [[WDHD1]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 18 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A549 4.13×, J82 2.66×, A-172 2.37×, A498 1.86×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H460 3.41×, SW480 2.61×, LoVo 3.99×; ⚠ cell-cycle shift, explains ~57% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 2.96×, NCI-H1573 3.77×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.35×** | +12.8 | 5e-35 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.10×** | +11.2 | 1e-26 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.97×** | +10.2 | 4e-22 | 42/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.74×** | +8.0 | 1e-13 | 24/37 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.69×** | +7.6 | 5e-12 | 30/48 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.72×** | +6.8 | 1e-09 | 30/43 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.33×** | +6.1 | 8e-08 | 24/47 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.48×** | +5.5 | 3e-06 | 23/41 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.42×** | +5.3 | 8e-06 | 27/46 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +3.9 | 0.006 | 20/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.8 | 0.008 | 24/48 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~91% of this change | **1.29×** | +3.7 | 0.009 | 18/43 (SW480, PANC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.29×** | +3.7 | 0.010 | 15/48 (A-427, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.27×** | +3.6 | 0.011 | 20/48 (LoVo, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.31×** | +3.4 | 0.027 | 16/48 (PANC-1, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.043 | 12/47 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.314×, C32 0.415×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.254×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.226×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.833×** | -3.9 | 0.032 | 18/48 (HCT15, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.9 | 0.032 | 3/48 (HT-29, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.795×** | -3.5 | 0.079 | 19/48 (Hs 766T, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -3.4 | 0.079 | 19/48 (NCI-H1792, C32, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.717×** | -3.4 | 0.079 | 17/48 (KATO III, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.801×** | -3.3 | 0.079 | 19/48 (LS 180, A-427, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.783× | -3.2 | 0.10 | 17/48 (A-427, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.11 | 13/48 (SHP-77, HCT15, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.788× | -3.1 | 0.11 | 15/48 (KATO III, A-172, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | 0.676× | -3.1 | 0.12 | 9/47 (A498, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.83 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.9 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.96× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 18.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +9.2) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H460 (line)]] | wt | 20.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.41× (z +9.4) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SW480 (line)]] | alt | 35.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +10.1) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[A-427 (line)]] | wt | 42.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 41.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.77× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.3) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[A-172 (line)]] | wt | 44.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 66.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 20.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 57.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.415× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.3) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM10]] | +0.81 | +0.77 / +0.82 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 588 |
| [[GINS2]] | +0.81 | +0.73 / +0.79 | both halves | 7e-06 | pathway: DNA Replication; STRING 621 |
| [[WDHD1]] | +0.81 | +0.73 / +0.84 | both halves | 7e-06 | STRING 662 |
| [[EXO1]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 893 |
| [[DTL]] | +0.80 | +0.72 / +0.85 | both halves | 7e-06 | pathway: DNA Damage Bypass; STRING 677 |
| [[CDC45]] | +0.80 | +0.76 / +0.80 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 809 |
| [[E2F1]] | +0.80 | +0.75 / +0.82 | both halves | 7e-06 | pathway: S Phase |
| [[BLM]] | +0.79 | +0.73 / +0.77 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 833 |
| [[CENPM]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CHAF1A]] | +0.77 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[RBL1]] | +0.77 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.77 | +0.71 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises RFC2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.53× lower at baseline in the lines without E2F2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.7, -45.5); signed map (-38.7, -44.6). **Vector** length 101, 27.0% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.64 to 23); *Activation of the pre-replicative complex* (reactome, mean cos +0.67 to 22); *Mitotic G1 phase and G1/S transition* (reactome, mean cos +0.66 to 34).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.6 | +11.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.5 | +12.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.4 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.5 | +7.6 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +3.0 | +3.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +1.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Methotrexate (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.9 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.5 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.7 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | replication factor C subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,231,499-74,254,458 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A1, RFC40 |
| Gene groups (HGNC) | AAA ATPases; Replication factor C |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 59 pathways, smallest: Leading Strand Synthesis; Polymerase switching; Translesion synthesis by REV1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P35250](https://www.uniprot.org/uniprotkb/P35250) (Replication factor C subunit 2):

> Subunit of the replication factor C (RFC) complex which acts during elongation of primed DNA templates by DNA polymerases delta and epsilon, and is necessary for ATP-dependent loading of proliferating cell nuclear antigen (PCNA) onto primed DNA. This subunit binds ATP (By similarity).

**Summary**, from NCBI Gene [5982](https://www.ncbi.nlm.nih.gov/gene/5982):

> This gene encodes a member of the activator 1 small subunits family. The elongation of primed DNA templates by DNA polymerase delta and epsilon requires the action of the accessory proteins, proliferating cell nuclear antigen (PCNA) and replication factor C (RFC). Replication factor C, also called activator 1, is a protein complex consisting of five distinct subunits. This gene encodes the 40 kD subunit, which has been shown to be responsible for binding ATP and may help promote cell survival. …

**Accessions** — [HGNC:9970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9970) · Entrez [5982](https://www.ncbi.nlm.nih.gov/gene/5982) · UniProt [P35250](https://www.uniprot.org/uniprotkb/P35250) · Ensembl [ENSG00000049541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049541)

## Data

Gene col 552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 552); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 552]; `tensor/DDL_lfc|DDL_z.npy` [552]; `embed/gene_vectors.npy` [552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 552 or target_col == 552). Every well: [[RFC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
