---
symbol: "ZDHHC17"
type: "gene"
col: 11869
ensembl_id: "ENSG00000186908"
name: "zDHHC palmitoyltransferase 17"
location: "12q21.2"
module: 17
arm: "+"
pooled_cpm: 93.19
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZDHHC17

*zDHHC palmitoyltransferase 17* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.19× (z +4.2, q 0.016, up in 19 of 48 measured lines) ⚠ cell-cycle shift, explains ~67% of this change.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.543× (z -10.5, q 7e-23, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.604× (z -8.6, q 7e-16, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (CHP-212 0.0863×, CFPAC-1 0.268×, KATO III 0.250×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-423 0.406×, A549 0.463×, LOX-IMVI 0.445×; ⚠ cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 0.319×, NCI-H23 0.319×, NCI-H1573 0.286×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (SNU-423 0.367×, MIA PaCa-2 0.317×, A-172 0.456×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA5]] (+0.72, fdr 7e-06), [[ZNF428]] (+0.69, fdr 1e-05), [[NDUFA5]] (+0.69, fdr 7e-06); moves opposite to [[SNTB2]] (-0.60, fdr 1e-05), [[FBXW7]] (-0.58, fdr 1e-05), [[PLEKHA6]] (-0.56, fdr 7e-06).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NDUFS4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.19× | +4.2 | 0.016 | 19/48 (LoVo, KATO III, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.24×** | +3.7 | 0.054 | 28/48 (KATO III, LoVo, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.45× | +3.0 | 0.38 | 20/49 (NCI-H460, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 15 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11869.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (CHP-212 0.0863×, CFPAC-1 0.268×, KATO III 0.250×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-423 0.406×, A549 0.463×, LOX-IMVI 0.445×; ⚠ cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 0.319×, NCI-H23 0.319×, NCI-H1573 0.286×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (SNU-423 0.367×, MIA PaCa-2 0.317×, A-172 0.456×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.543×** | -10.5 | 7e-23 | 46/48 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.571×** | -9.6 | 2e-19 | 45/48 (A549, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.673×** | -9.6 | 2e-19 | 43/49 (SNU-423, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.558×** | -9.2 | 4e-18 | 41/45 (CHP-212, CFPAC-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.604×** | -8.6 | 7e-16 | 42/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.609×** | -8.2 | 3e-14 | 31/44 (A549, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.624×** | -8.1 | 6e-14 | 42/49 (NCI-H23, NCI-H1792, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.646×** | -7.5 | 5e-12 | 36/48 (A549, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.669×** | -6.6 | 2e-09 | 34/47 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.678×** | -6.4 | 9e-09 | 40/50 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.692×** | -6.1 | 7e-08 | 33/47 (NCI-H460, HCT15, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.697×** | -5.9 | 1e-07 | 35/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.811×** | -5.1 | 2e-05 | 35/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.748×** | -5.0 | 3e-05 | 34/48 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.767×** | -4.5 | 2e-04 | 31/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 118 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[CFPAC-1 (line)]] | alt | 97.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 144 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[HOP62 (line)]] | alt | 101 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -10.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H1792 (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[CHP-212 (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0863× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 67.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.317× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.450× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 88.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.456× (z -8.8) |
| [[A-427 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.429× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 98.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -11.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[RKO (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 86.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW 1271 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0957× (z -11.8) ⚠ transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SW 900 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 129 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 90.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 83.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA5]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ZNF428]] | +0.69 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PMPCB]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[COPS5]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[FAM204A]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[IFT46]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[POLK]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ESD]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[IFT74]] | +0.62 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CCDC25]] | +0.62 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTB2]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[FBXW7]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PLEKHA6]] | -0.56 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[NPIPB11]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.53 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[ARPC5L]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | -0.52 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[PITPNA]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZDHHC17's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFS4]] | C | ZDHHC17's natural level strengthens NDUFS4's drug response | ZDHHC17's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.10; direction clear | 0.037 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-22.8, 3.0); signed map (8.6, -25.5). **Vector** length 80.1, 21.8% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +7.4 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +4.6 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.7 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.5 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -8.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | -3.1 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.9 | -9.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:76,764,103-76,853,696 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HIP14, HYPH, KIAA0946 |
| Gene groups (HGNC) | Zinc fingers DHHC-type; Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUH5](https://www.uniprot.org/uniprotkb/Q8IUH5) (Palmitoyltransferase ZDHHC17):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates and is involved in a variety of cellular processes. Has no stringent fatty acid selectivity and in addition to palmitate can also transfer onto target proteins myristate from tetradecanoyl-CoA and stearate from octadecanoyl-CoA (By similarity). Palmitoyltransferase specific for a subset of neuronal proteins, including SNAP25, DLG4/PSD95, GAD2, SYT1 and HTT. Also palmitoylates neuronal protein GPM6A as …

**Summary**, from NCBI Gene [23390](https://www.ncbi.nlm.nih.gov/gene/23390):

> Enables identical protein binding activity and protein-cysteine S-palmitoyltransferase activity. Involved in lipoprotein transport; protein palmitoylation; and regulation of programmed cell death. Located in Golgi membrane and Golgi-associated vesicle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18412) · Entrez [23390](https://www.ncbi.nlm.nih.gov/gene/23390) · UniProt [Q8IUH5](https://www.uniprot.org/uniprotkb/Q8IUH5) · Ensembl [ENSG00000186908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186908)

## Data

Gene col 11869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11869); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11869]; `tensor/DDL_lfc|DDL_z.npy` [11869]; `embed/gene_vectors.npy` [11869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11869 or target_col == 11869). Every well: [[ZDHHC17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
