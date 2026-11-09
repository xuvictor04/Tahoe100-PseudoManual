---
symbol: "ANAPC1"
type: "gene"
col: 7690
ensembl_id: "ENSG00000153107"
name: "anaphase promoting complex subunit 1"
location: "2q13"
module: 18
arm: "+"
pooled_cpm: 50.35
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ANAPC1

*anaphase promoting complex subunit 1* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.71× (z +8.6, q 4e-15, up in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.28× (z +3.9, q 0.009, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 2.54×, COLO 205 2.96×, CFPAC-1 2.01×; ⚠ cell-cycle shift, explains ~38% of this change); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 2.14×; ⚠ cell-cycle shift, explains ~58% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.699× (z -5.3, q 6e-05, down in 25 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.751× (z -4.6, q 8e-04, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.294×, PANC-1 0.374×, HEC-1-A 0.388×, SK-MEL-2 0.300×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.335×, MIA PaCa-2 0.366×, SK-MEL-2 0.330×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.245×, SW1417 0.357×, NCI-H2030 0.363×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS25]] (+0.76, fdr 7e-06), [[LARS2]] (+0.72, fdr 7e-06), [[MDN1]] (+0.71, fdr 7e-06); moves opposite to [[HDAC5]] (-0.62, fdr 1e-05), [[CHP1]] (-0.57, fdr 2e-05), [[UBE2B]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CYP46A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 2.54×, COLO 205 2.96×, CFPAC-1 2.01×; ⚠ cell-cycle shift, explains ~38% of this change); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 2.14×; ⚠ cell-cycle shift, explains ~58% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +8.6 | 4e-15 | 45/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.28×** | +5.5 | 9e-06 | 32/48 (NCI-H2347, A549, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +4.9 | 2e-04 | 30/47 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.23×** | +4.7 | 4e-04 | 25/48 (HT-29, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.29×** | +4.1 | 0.006 | 21/48 (NCI-H1573, AsPC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.009 | 21/48 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.027 | 22/48 (Panc 03.27, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.069 | 15/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.10 | 16/47 (NCI-H23, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.21× | +3.1 | 0.10 | 18/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.22× | +3.1 | 0.10 | 19/48 (SW 900, HT-29, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.21× | +3.0 | 0.13 | 15/48 (A498, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.294×, PANC-1 0.374×, HEC-1-A 0.388×, SK-MEL-2 0.300×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.335×, MIA PaCa-2 0.366×, SK-MEL-2 0.330×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.245×, SW1417 0.357×, NCI-H2030 0.363×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.699×** | -5.3 | 6e-05 | 25/45 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -5.2 | 6e-05 | 31/48 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.751×** | -4.6 | 8e-04 | 25/48 (RKO, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **0.801×** | -3.6 | 0.049 | 21/47 (HCT15, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.796×** | -3.5 | 0.049 | 22/42 (SK-MEL-2, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **0.809×** | -3.4 | 0.062 | 21/48 (SW1417, HCT15, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.807×** | -3.3 | 0.073 | 22/48 (PANC-1, SNU-423, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 94.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -11.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HCT15 (line)]] | alt | 79.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 25.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LOX-IMVI (line)]] | wt | 54.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0831× (z -11.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 90.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.14× (z +9.0) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[PANC-1 (line)]] | alt | 65.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 76.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS25]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[LARS2]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[MDN1]] | +0.71 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[METTL3]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[COX10]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TSR1]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[ATR]] | +0.68 | +0.72 / +0.59 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[NAF1]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[PUS7]] | +0.67 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[ALG8]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SNX5]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC5]] | -0.62 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[CHP1]] | -0.57 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[UBE2B]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TMCC2]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TUFT1]] | -0.55 | -0.53 / -0.41 | both halves | 4e-05 | same gene group |
| [[DBP]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[KLF2]] | -0.55 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[POLD4]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 | pathway: DNA Replication |
| [[DLGAP4]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MEF2D]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[DDAH2]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RING1]] | -0.55 | -0.46 / -0.47 | both halves | 3e-05 | pathway: Cellular Senescence; STRING 901 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP46A1]] | B | CYP46A1 activity raises ANAPC1's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.44× lower at baseline in the lines without CYP46A1 | 0.086 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |
| [[TMCC2]] | B | TMCC2 activity raises ANAPC1's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.61× lower at baseline in the lines without TMCC2 | 0.090 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.0, -32.8); signed map (-0.6, -50.5). **Vector** length 105, 27.4% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.1 | +8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.8 | +5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.2 | +4.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +4.0 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.7 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:111,611,639-111,884,690 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCPR, TSG24, APC1 |
| Gene groups (HGNC) | Anaphase promoting complex; MicroRNA protein coding host genes |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1A4](https://www.uniprot.org/uniprotkb/Q9H1A4) (Anaphase-promoting complex subunit 1):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [64682](https://www.ncbi.nlm.nih.gov/gene/64682):

> This gene encodes a subunit of the anaphase-promoting complex. This complex is an E3 ubiquitin ligase that regulates progression through the metaphase to anaphase portion of the cell cycle by ubiquitinating proteins which targets them for degradation. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:19988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19988) · Entrez [64682](https://www.ncbi.nlm.nih.gov/gene/64682) · UniProt [Q9H1A4](https://www.uniprot.org/uniprotkb/Q9H1A4) · Ensembl [ENSG00000153107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153107)

## Data

Gene col 7690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7690); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7690]; `tensor/DDL_lfc|DDL_z.npy` [7690]; `embed/gene_vectors.npy` [7690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7690 or target_col == 7690). Every well: [[ANAPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
