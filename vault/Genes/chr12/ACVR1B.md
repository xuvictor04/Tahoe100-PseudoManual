---
symbol: "ACVR1B"
type: "gene"
col: 5716
ensembl_id: "ENSG00000135503"
name: "activin A receptor type 1B"
location: "12q13.13"
module: 146
arm: "+"
pooled_cpm: 28.82
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# ACVR1B

*activin A receptor type 1B* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.95× (z +5.9, q 2e-06, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.359× (z -17.2, q 0e+00, down in 41 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.701× (z -8.5, q 5e-15, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A-427 0.103×, A-172 0.0651×, C32 0.0592×, J82 0.127×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.138×, A-427 0.196×, LOX-IMVI 0.169×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.0917×, SW480 0.201×, A-427 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.243×, NCI-H2347 0.391×, LOX-IMVI 0.435×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.324×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB13]] (+0.65, fdr 7e-06), [[CHPT1]] (+0.65, fdr 1e-05), [[NISCH]] (+0.60, fdr 8e-06); moves opposite to [[LINC00310]] (-0.54, fdr 1e-05), [[MPP4]] (-0.54, fdr 3e-05), [[OGDH]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +5.9 | 2e-06 | 27/46 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +5.5 | 1e-05 | 24/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +4.7 | 6e-04 | 25/48 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 9e-04 | 19/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 1e-03 | 19/47 (KATO III, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +4.3 | 0.002 | 22/48 (SHP-77, RPMI-7951, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.9 | 0.007 | 21/46 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.26×** | +3.9 | 0.007 | 20/48 (CHP-212, SNU-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.031 | 16/47 (A498, A549, …) | two highest doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.092 | 13/47 (SHP-77, HepG2/C3A, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.14× | +3.1 | 0.11 | 5/48 (J82, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5716.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A-427 0.103×, A-172 0.0651×, C32 0.0592×, J82 0.127×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.138×, A-427 0.196×, LOX-IMVI 0.169×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.0917×, SW480 0.201×, A-427 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.243×, NCI-H2347 0.391×, LOX-IMVI 0.435×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.324×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.359×** | -17.2 | 0e+00 | 41/45 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -17.1 | 0e+00 | 32/37 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -8.5 | 5e-15 | 31/48 (A-427, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.654×** | -6.6 | 6e-09 | 29/42 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.722×** | -5.3 | 2e-05 | 26/46 (LOX-IMVI, H4, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.732×** | -5.0 | 4e-05 | 24/48 (NCI-H2347, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.878× | -3.1 | 0.16 | 21/47 (LOX-IMVI, C32, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.835× | -3.0 | 0.17 | 13/48 (COLO 205, SW1417, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.17 | 10/47 (LOX-IMVI, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 32.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.3) |
| [[A-427 (line)]] | wt | 43.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -13.7) |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 25.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0592× (z -17.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 36.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 33.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0917× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 31.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 30.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -14.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -12.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 25.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -20.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0651× (z -18.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -11.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -11.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -15.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -12.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -8.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB13]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CHPT1]] | +0.65 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[NISCH]] | +0.60 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[FAM222B]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ZNF592]] | +0.57 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MTFMT]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[GATA4]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[NELFA]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CDAN1]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CHST10]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TTLL4]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00310]] | -0.54 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[MPP4]] | -0.54 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[OGDH]] | -0.54 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[ADCY10P1]] | -0.54 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.53 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[NEK10]] | -0.53 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[LINC02798]] | -0.53 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[PHEX]] | -0.53 | -0.68 / -0.39 | both halves | 6e-05 |  |
| [[ERI2]] | -0.53 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[MYH15]] | -0.53 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ASPH]] | -0.52 | -0.31 / -0.63 | both halves | 2e-04 |  |
| [[FER]] | -0.52 | -0.60 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ACVR1B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.6, 14.7); signed map (-28.4, -18.1). **Vector** length 96.7, 22.1% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.1 | -1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.6 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.2 | +3.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.1 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.2 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[9-ING-41 (drug)]] 0.05 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | activin A receptor type 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:51,951,699-51,997,078 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALK4, SKR2, ActRIB; previously ACVRLK4 |
| Gene groups (HGNC) | Type 1 receptor serine/threonine kinases |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INFLAMMATORY_RESPONSE, P53_PATHWAY |
| Reactome | 4 pathways, smallest: Regulation of signaling by NODAL; Signaling by NODAL; Signaling by Activin |
| Matched by | ensembl_id |

**Function**, from UniProt [P36896](https://www.uniprot.org/uniprotkb/P36896) (Activin receptor type-1B):

> Transmembrane serine/threonine kinase activin type-1 receptor forming an activin receptor complex with activin receptor type-2 (ACVR2A or ACVR2B). Transduces the activin signal from the cell surface to the cytoplasm and is thus regulating a many physiological and pathological processes including neuronal differentiation and neuronal survival, hair follicle development and cycling, FSH production by the pituitary gland, wound healing, extracellular matrix production, immunosuppression and …

**Summary**, from NCBI Gene [91](https://www.ncbi.nlm.nih.gov/gene/91):

> This gene encodes an activin A type IB receptor. Activins are dimeric growth and differentiation factors which belong to the transforming growth factor-beta (TGF-beta) superfamily of structurally related signaling proteins. Activins signal through a heteromeric complex of receptor serine kinases which include at least two type I and two type II receptors. This protein is a type I receptor which is essential for signaling. Mutations in this gene are associated with pituitary tumors. Alternate …

**Accessions** — [HGNC:172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:172) · Entrez [91](https://www.ncbi.nlm.nih.gov/gene/91) · UniProt [P36896](https://www.uniprot.org/uniprotkb/P36896) · Ensembl [ENSG00000135503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135503)

## Data

Gene col 5716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5716); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5716]; `tensor/DDL_lfc|DDL_z.npy` [5716]; `embed/gene_vectors.npy` [5716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5716 or target_col == 5716). Every well: [[ACVR1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACVR1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
