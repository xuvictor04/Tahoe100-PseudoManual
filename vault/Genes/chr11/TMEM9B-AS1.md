---
symbol: "TMEM9B-AS1"
type: "gene"
col: 14898
ensembl_id: "ENSG00000254860"
name: "TMEM9B antisense RNA 1"
location: "11p15.4"
module: 10
arm: "+"
pooled_cpm: 14.69
n_lines_expressing: 45
n_dd_up: 29
n_dd_down: 18
n_dd_up_clean: 24
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TMEM9B-AS1

*TMEM9B antisense RNA 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +8.9, q 5e-16, up in 30 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.407× (z -9.7, q 1e-19, down in 35 of 42 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.411× (z -9.6, q 2e-19, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BDNF-AS]] (+0.76, fdr 2e-05), [[RXYLT1]] (+0.75, fdr 1e-05), [[OXA1L-DT]] (+0.75, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MIR1915HG]] → it (grade B ⚠); 11 go from it, the strongest it → [[BDNF-AS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.9 | 5e-16 | 30/42 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.0 | 5e-07 | 22/39 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +5.7 | 2e-06 | 24/41 (A-172, C-33 A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.63×** | +5.3 | 1e-05 | 25/42 (A498, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.3 | 1e-05 | 6/16 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.40×** | +5.2 | 1e-05 | 13/42 (C32, RKO, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +5.1 | 3e-05 | 16/41 (A-427, LS 180, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +4.3 | 1e-03 | 15/40 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 0.001 | 17/40 (NCI-H1573, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.002 | 15/40 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.008 | 14/40 (SW480, Hs 766T, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.011 | 12/43 (LoVo, J82, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.013 | 12/42 (SW480, LoVo, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.013 | 10/42 (HOP62, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.013 | 13/43 (SW480, A498, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.38×** | +3.6 | 0.013 | 10/42 (SW 1271, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.028 | 9/43 (MIA PaCa-2, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.407×** | -9.7 | 1e-19 | 35/42 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.411×** | -9.6 | 2e-19 | 32/42 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.424×** | -9.3 | 2e-18 | 29/38 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.434×** | -9.1 | 2e-17 | 31/42 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.473×** | -8.1 | 6e-14 | 29/42 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.248×** | -7.9 | 3e-13 | 30/38 (A-427, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -7.2 | 4e-11 | 28/40 (PANC-1, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.543×** | -6.6 | 3e-09 | 28/41 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.572×** | -6.0 | 9e-08 | 20/42 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.597×** | -5.6 | 1e-06 | 23/43 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.646×** | -4.5 | 4e-04 | 24/40 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.652×** | -4.4 | 4e-04 | 22/37 (A-427, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.530×** | -3.6 | 0.014 | 15/29 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.737×** | -3.3 | 0.040 | 16/41 (A-427, LS 180, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.740×** | -3.2 | 0.043 | 13/42 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.585×** | -3.0 | 0.076 | 14/37 (HS-578T, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.5 | 0 | 10 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.153× (z -17.1) |
| [[SW480 (line)]] | alt | 13.6 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -11.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -9.1) |
| [[A549 (line)]] | wt | 30.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.2) |
| [[LoVo (line)]] | wt | 21.3 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0636× (z -18.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 23.8 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.104× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 21.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0770× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~50% of this change · without an alert: [[Raltitrexed (drug)]] 0.5 µM 0.214× (z -9.0) |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -11.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 15.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.140× (z -11.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.211× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.161× (z -9.1) |
| [[C-33 A (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 8.92 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0578× (z -10.8) |
| [[COLO 205 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0499× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +8.9) | — |
| [[RKO (line)]] | wt | 7.99 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0785× (z -10.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 4.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0499× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDNF-AS]] | +0.76 | +0.80 / +0.47 | both halves | 2e-05 | same gene group |
| [[RXYLT1]] | +0.75 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.75 | +0.79 / +0.45 | both halves | 3e-05 |  |
| [[SEPTIN7-DT]] | +0.75 | +0.78 / +0.43 | both halves | 3e-05 |  |
| [[NSMCE1-DT]] | +0.74 | +0.84 / +0.40 | both halves | 5e-05 |  |
| [[FAM227B]] | +0.73 | +0.77 / +0.46 | both halves | 3e-05 |  |
| [[EPM2A-DT]] | +0.73 | +0.80 / +0.36 | both halves | 9e-05 |  |
| [[F8]] | +0.73 | +0.80 / +0.36 | both halves | 1e-04 |  |
| [[BCDIN3D]] | +0.72 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[DPH6-DT]] | +0.72 | +0.76 / +0.44 | both halves | 3e-05 |  |
| [[UGDH-AS1]] | +0.72 | +0.78 / +0.48 | both halves | 2e-05 | same gene group |
| [[PDCL3P4]] | +0.72 | +0.76 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | B | MIR1915HG activity raises TMEM9B-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without MIR1915HG | 0.005 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises TMEM9B-AS1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.81× lower at baseline in the lines without ANKRD20A21P | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity strengthens TMEM9B-AS1's drug response | lines that do not express ANKRD20A21P (27) vs lines expressing it (16) | the lines without ANKRD20A21P respond 0.67× as strongly (z diff +1.73); strongest at Digitoxin 5 µM: 0.45x vs 0.30x (z diff +3.2) | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P; target measured in part of the lines; artifact flags |
| [[FTCDNL1]] | B | FTCDNL1 activity raises TMEM9B-AS1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 2.17× lower at baseline in the lines without FTCDNL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BDNF-AS]] | B | TMEM9B-AS1 activity raises BDNF-AS's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.71× lower at baseline in the lines without TMEM9B-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[SPTY2D1OS]] | B | TMEM9B-AS1 activity raises SPTY2D1OS's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.54× lower at baseline in the lines without TMEM9B-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[RXYLT1]] | B | TMEM9B-AS1 activity raises RXYLT1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without TMEM9B-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[SLC16A1-AS1]] | B | TMEM9B-AS1 activity raises SLC16A1-AS1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without TMEM9B-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[TRIM66]] | B | TMEM9B-AS1 activity raises TRIM66's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 2.18× lower at baseline in the lines without TMEM9B-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[ENTPD3-AS1]] | B | TMEM9B-AS1 activity raises ENTPD3-AS1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without TMEM9B-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[DHRS12]] | B | TMEM9B-AS1 activity raises DHRS12's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without TMEM9B-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[WASHC3]] | B | TMEM9B-AS1 activity raises WASHC3's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without TMEM9B-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[ZCWPW1]] | B | TMEM9B-AS1 activity raises ZCWPW1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.55× lower at baseline in the lines without TMEM9B-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[IDNK]] | B | TMEM9B-AS1 activity raises IDNK's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without TMEM9B-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[KLHDC1]] | B | TMEM9B-AS1 activity raises KLHDC1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without TMEM9B-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.797). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.8, 18.0); signed map (31.1, -10.6). **Vector** length 79.0, 16.4% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.9 | -9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -7.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | TMEM9B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.4 — chr11:8,964,502-8,977,527 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C11orf18 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:19230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19230) · Entrez [493900](https://www.ncbi.nlm.nih.gov/gene/493900) · Ensembl [ENSG00000254860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254860)

## Data

Gene col 14898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14898); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14898]; `tensor/DDL_lfc|DDL_z.npy` [14898]; `embed/gene_vectors.npy` [14898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14898 or target_col == 14898). Every well: [[TMEM9B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM9B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
