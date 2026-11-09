---
symbol: "CSE1L"
type: "gene"
col: 4498
ensembl_id: "ENSG00000124207"
name: "chromosome segregation 1 like"
location: "20q13.13"
module: 6
arm: "+"
pooled_cpm: 127.48
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CSE1L

*chromosome segregation 1 like* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (15 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.65× (z +8.4, q 4e-14, up in 42 of 47 measured lines) ⚠ toxic; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.04× (z +6.5, q 8e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.835× (z -4.5, q 0.003, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~83% of this change. The strongest without an alert is [[ULK-101 (drug)]] 0.05 µM: 0.812× (z -3.5, q 0.099, down in 20 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HEC-1-A 0.499×, C-33 A 0.532×, J82 0.637×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.548×, H4 0.395×; ⚠ cell-cycle shift, explains ~83% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.567×, SNU-1 0.511×; ⚠ cell-cycle shift, explains ~0% of this change); [[Osimertinib (mesylate) (drug)]] 5 µM in 1 line (SW 1088 0.0815×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMELESS]] (+0.82, fdr 7e-06), [[RANBP1]] (+0.80, fdr 7e-06), [[MMS22L]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PKD1L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 18 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.65×** | +8.4 | 4e-14 | 42/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.54×** | +7.6 | 1e-11 | 37/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **1.56×** | +7.5 | 2e-11 | 28/44 (SNU-423, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.50×** | +7.1 | 2e-10 | 32/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +6.5 | 8e-09 | 38/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +6.2 | 5e-08 | 36/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +5.8 | 6e-07 | 33/48 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.36×** | +5.3 | 7e-06 | 28/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +5.3 | 9e-06 | 26/49 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.35×** | +5.2 | 1e-05 | 29/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.7 | 1e-04 | 24/38 (NCI-H1573, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 2e-04 | 29/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.31×** | +4.5 | 2e-04 | 25/48 (NCI-H1792, LoVo, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.62×** | +4.4 | 4e-04 | 28/49 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.28×** | +4.2 | 0.001 | 27/47 (COLO 205, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4498.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HEC-1-A 0.499×, C-33 A 0.532×, J82 0.637×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.548×, H4 0.395×; ⚠ cell-cycle shift, explains ~83% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.567×, SNU-1 0.511×; ⚠ cell-cycle shift, explains ~0% of this change); [[Osimertinib (mesylate) (drug)]] 5 µM in 1 line (SW 1088 0.0815×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.835× | -4.5 | 0.003 | 24/48 (A-427, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.812×** | -3.5 | 0.099 | 20/49 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.822×** | -3.5 | 0.099 | 18/48 (A-172, SW1417, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.826× | -3.4 | 0.10 | 22/48 (J82, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.832× | -3.3 | 0.11 | 18/49 (KATO III, RPMI-7951, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.833× | -3.2 | 0.11 | 17/49 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.836× | -3.2 | 0.12 | 20/48 (A-172, NCI-H460, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.838× | -3.1 | 0.12 | 17/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.840× | -3.1 | 0.12 | 21/48 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | 0.721× | -3.0 | 0.15 | 16/48 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 118 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +14.2) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[A-427 (line)]] | wt | 198 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 69.3 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.4) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H1792 (line)]] | alt | 75.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 106 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.01× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | — |
| [[J82 (line)]] | alt | 347 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 136 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.55× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[SNU-423 (line)]] | alt | 91.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | — |
| [[SW 1088 (line)]] | alt | 85.1 | 0 | 2 (1 ⚠) | — | [[Nimesulide (drug)]] 0.05 µM 0.0734× (z -9.4) ⚠ unreliable plate only · without an alert: [[Osimertinib (mesylate) (drug)]] 5 µM 0.0815× (z -9.0) |
| [[A549 (line)]] | wt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 214 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 67.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.395× (z -9.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[Hs 766T (line)]] | wt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 97.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.58× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 46.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +8.6) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H596 (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.163× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 94.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 181 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 175 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMELESS]] | +0.82 | +0.82 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RANBP1]] | +0.80 | +0.80 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 786 |
| [[MMS22L]] | +0.80 | +0.82 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[TYMS]] | +0.79 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[NUP205]] | +0.78 | +0.79 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 661 |
| [[CEP78]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[TUBGCP3]] | +0.77 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[VRK1]] | +0.77 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.76 | +0.78 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[GMPS]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 | STRING 454 |
| [[MCM3]] | +0.76 | +0.73 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[GINS1]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKD1L2]] | B | PKD1L2 activity raises CSE1L's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without PKD1L2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises CSE1L's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without CDCA7 | 0.088 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CSE1L's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without PBK | 0.047 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises CSE1L's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.782). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.4, -42.5); signed map (-34.0, -43.6). **Vector** length 138, 50.0% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.61 to 28); *DNA Replication* (reactome, mean cos +0.58 to 40); *E2F G1/S* (control, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | +4.9 | +7.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | +4.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | +5.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.5 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.1 | +2.8 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -1.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | -3.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.8 | -3.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.2 | -3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.9 | -2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | chromosome segregation 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,046,246-49,096,960 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAS, XPO2, CSE1 |
| Gene groups (HGNC) | Exportins |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [P55060](https://www.uniprot.org/uniprotkb/P55060) (Exportin-2):

> Export receptor for importin-alpha. Mediates importin-alpha re-export from the nucleus to the cytoplasm after import substrates (cargos) have been released into the nucleoplasm. In the nucleus binds cooperatively to importin-alpha and to the GTPase Ran in its active GTP-bound form. Docking of this trimeric complex to the nuclear pore complex (NPC) is mediated through binding to nucleoporins. Upon transit of a nuclear export complex into the cytoplasm, disassembling of the complex and hydrolysis …

**Summary**, from NCBI Gene [1434](https://www.ncbi.nlm.nih.gov/gene/1434):

> Proteins that carry a nuclear localization signal (NLS) are transported into the nucleus by the importin-alpha/beta heterodimer. Importin-alpha binds the NLS, while importin-beta mediates translocation through the nuclear pore complex. After translocation, RanGTP binds importin-beta and displaces importin-alpha. Importin-alpha must then be returned to the cytoplasm, leaving the NLS protein behind. The protein encoded by this gene binds strongly to NLS-free importin-alpha, and this binding is …

**Accessions** — [HGNC:2431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2431) · Entrez [1434](https://www.ncbi.nlm.nih.gov/gene/1434) · UniProt [P55060](https://www.uniprot.org/uniprotkb/P55060) · Ensembl [ENSG00000124207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124207)

## Data

Gene col 4498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4498); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4498]; `tensor/DDL_lfc|DDL_z.npy` [4498]; `embed/gene_vectors.npy` [4498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4498 or target_col == 4498). Every well: [[CSE1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSE1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
