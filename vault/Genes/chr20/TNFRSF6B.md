---
symbol: "TNFRSF6B"
type: "gene"
col: 14363
ensembl_id: "ENSG00000243509"
name: "TNF receptor superfamily member 6b"
location: "20q13.33"
module: 34
arm: "+"
pooled_cpm: 17.92
n_lines_expressing: 17
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 27
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TNFRSF6B

*TNF receptor superfamily member 6b* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.58× (z +9.0, q 9e-17, up in 3 of 12 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.432× (z -5.5, q 2e-05, down in 12 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRE2]] (+0.72, fdr 1e-05), [[LINC02725]] (+0.68, fdr 1e-05), [[HPCAL1]] (+0.64, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TGM2]] → it (grade B ⚠); 27 go from it, the strongest it → [[RAPGEF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +9.0 | 9e-17 | 3/12 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +8.6 | 2e-15 | 5/12 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +5.9 | 6e-07 | 1/12 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **2.11×** | +5.3 | 2e-05 | 4/14 (KATO III, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.09× | +3.0 | 0.26 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.432×** | -5.5 | 2e-05 | 12/15 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.487×** | -4.6 | 1e-03 | 14/15 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.627×** | -4.6 | 1e-03 | 13/15 (MIA PaCa-2, Panc 03.27, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.538×** | -4.2 | 0.004 | 11/14 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.539×** | -4.1 | 0.004 | 12/15 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.620×** | -3.8 | 0.014 | 11/15 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.588×** | -3.7 | 0.014 | 10/15 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.605×** | -3.6 | 0.027 | 15/15 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.602×** | -3.5 | 0.035 | 13/14 (MIA PaCa-2, SW 900, …) | all doses, flat | position effect removed |
| [[crizotinib (drug)]] 5 µM |  | **0.614×** | -3.3 | 0.052 | 12/15 (SW 900, AsPC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.635×** | -3.2 | 0.069 | 12/15 (KATO III, SW 900, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.629×** | -3.1 | 0.093 | 6/15 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.648×** | -3.1 | 0.093 | 12/15 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 216 | 0 | 21 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.353× (z -19.8) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0617× (z -14.5) |
| [[KATO III (line)]] | alt | 56.6 | 0 | 20 (7 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0570× (z -20.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0605× (z -14.0) |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0970× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 44.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.163× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0825× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -12.0) |
| [[HT-29 (line)]] | alt | 5.93 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0878× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0623× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.128× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0856× (z -10.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 4.54 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0671× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.516× (z -9.3) ⚠ position not correctable |
| [[SW480 (line)]] | alt | 6.56 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRE2]] | +0.72 | +0.57 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[LINC02725]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[HPCAL1]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LINC02320]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MYEOV]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[STMN3]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 | ⚠ same locus (39.0 kb: neighbours can correlate without regulation) |
| [[LAMA3]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ADAM8]] | +0.60 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[VSIG1]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PLK3]] | +0.59 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[LINC00659]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TGFA]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGM2]] | B | TGM2 activity raises TNFRSF6B's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without TGM2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[MAP2K1]] | B | MAP2K1 activity raises TNFRSF6B's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[ITGA3]] | B | ITGA3 activity raises TNFRSF6B's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.65× lower at baseline in the lines without ITGA3 | 0.070 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[ADAM8]] | C | ADAM8 activity raises TNFRSF6B's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without ADAM8 | 0.044 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 16, C 11. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF3]] | B | TNFRSF6B activity raises RAPGEF3's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.80× lower at baseline in the lines without TNFRSF6B | 0.017 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[TCF7L2]] | B | TNFRSF6B activity raises TCF7L2's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.69× lower at baseline in the lines without TNFRSF6B | 0.026 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[PDE2A]] | B | TNFRSF6B activity raises PDE2A's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.63× lower at baseline in the lines without TNFRSF6B | 0.035 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[MAP3K5]] | B | TNFRSF6B activity raises MAP3K5's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without TNFRSF6B | 0.044 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[ITGA6]] | B | TNFRSF6B activity strengthens ITGA6's drug response | lines that do not express TNFRSF6B (26) vs lines expressing it (15) | the lines without TNFRSF6B respond 0.90× as strongly (z diff +0.75); strongest at Trametinib 0.5 µM: 0.69x vs 0.52x (z diff +2.3) | 0.046 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19; target measured in part of the lines; artifact flags |
| [[GDPGP1]] | B | TNFRSF6B activity raises GDPGP1's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.81× lower at baseline in the lines without TNFRSF6B | 0.050 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[TCF7L2]] | B | TNFRSF6B activity weakens TCF7L2's drug response | lines that do not express TNFRSF6B (31) vs lines expressing it (16) | the lines without TNFRSF6B respond 1.11× as strongly (z diff -0.81); strongest at Homoharringtonine 5 µM: 1.47x vs 0.88x (z diff -8.1) | 0.054 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19; target measured in part of the lines; both ways; artifact flags |
| [[PTK6]] | B | TNFRSF6B activity raises PTK6's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without TNFRSF6B | 0.055 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[PLEK2]] | B | TNFRSF6B activity raises PLEK2's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 4.02× lower at baseline in the lines without TNFRSF6B | 0.057 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[SCAT1]] | B | TNFRSF6B activity raises SCAT1's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 2.11× lower at baseline in the lines without TNFRSF6B | 0.058 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[PKP2]] | B | TNFRSF6B activity raises PKP2's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 2.17× lower at baseline in the lines without TNFRSF6B | 0.062 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[RAPGEF3]] | B | TNFRSF6B activity strengthens RAPGEF3's drug response | lines that do not express TNFRSF6B (27) vs lines expressing it (13) | the lines without TNFRSF6B respond 0.59× as strongly (z diff +1.11); strongest at Panobinostat 5 µM: 0.64x vs 0.40x (z diff +2.0) | 0.063 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.7, 3.8); signed map (3.8, 40.8). **Vector** length 62.6, 18.2% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | -0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.0 | +2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +0.9 | +1.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.7 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 6b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,696,652-63,698,684 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DcR3, DCR3, TR6, M68 |
| Gene groups (HGNC) | Tumor necrosis factor receptor superfamily |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [O95407](https://www.uniprot.org/uniprotkb/O95407) (Tumor necrosis factor receptor superfamily member 6B):

> Soluble decoy receptor that binds and neutralizes the TNF-family ligands TNFSF14/LIGHT, TNFSF15, and FASLG, preventing them from interacting with their cognate receptors and thereby blocking apoptosis and other immune-signaling pathway.

**Summary**, from NCBI Gene [8771](https://www.ncbi.nlm.nih.gov/gene/8771):

> This gene belongs to the tumor necrosis factor receptor superfamily. The encoded protein is postulated to play a regulatory role in suppressing FasL- and LIGHT-mediated cell death. It acts as a decoy receptor that competes with death receptors for ligand binding. Over-expression of this gene has been noted in gastrointestinal tract tumors. Read-through transcription into this gene from the neighboring upstream gene, which encodes regulator of telomere elongation helicase 1 (RTEL1), generates a …

**Accessions** — [HGNC:11921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11921) · Entrez [8771](https://www.ncbi.nlm.nih.gov/gene/8771) · UniProt [O95407](https://www.uniprot.org/uniprotkb/O95407) · Ensembl [ENSG00000243509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243509)

## Data

Gene col 14363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14363); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14363]; `tensor/DDL_lfc|DDL_z.npy` [14363]; `embed/gene_vectors.npy` [14363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14363 or target_col == 14363). Every well: [[TNFRSF6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
