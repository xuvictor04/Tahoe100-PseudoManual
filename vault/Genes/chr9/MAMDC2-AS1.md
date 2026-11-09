---
symbol: "MAMDC2-AS1"
type: "gene"
col: 12915
ensembl_id: "ENSG00000204706"
name: "MAMDC2 antisense RNA 1"
location: "9q21.12"
module: 26
arm: "+"
pooled_cpm: 3.7
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MAMDC2-AS1

*MAMDC2 antisense RNA 1* — 9q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.85× (z +10.6, q 1e-23, up in 29 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.224× (z -10.7, q 5e-24, down in 35 of 42 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Niclosamide (olamine) (drug)]] 0.5 µM: 0.592× (z -3.7, q 0.011, down in 13 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLK4]] (+0.77, fdr 7e-06), [[LIX1-AS1]] (+0.76, fdr 7e-06), [[ALG1L9P]] (+0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZRANB2-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +10.6 | 1e-23 | 29/33 (SHP-77, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +8.9 | 1e-16 | 20/30 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +7.7 | 2e-12 | 1/6 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +6.3 | 5e-08 | 19/34 (Panc 03.27, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +5.5 | 5e-06 | 23/38 (C32, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.52×** | +4.3 | 0.002 | 9/43 (KATO III, A498, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.79×** | +4.2 | 0.002 | 16/42 (C-33 A, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +4.2 | 0.002 | 3/15 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.012 | 8/42 (J82, H4, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.65×** | +3.6 | 0.018 | 13/39 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.019 | 4/43 (Panc 03.27, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +3.5 | 0.020 | 13/37 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +3.4 | 0.025 | 2/9 (NCI-H2347, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.65×** | +3.3 | 0.034 | 8/42 (SW480, A-172, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.034 | 10/42 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.043 | 2/45 (A498, HOP62) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.043 | 10/39 (NCI-H23, A498, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.054 | 11/42 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.56×** | +3.0 | 0.069 | 6/38 (SW480, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12915.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.224×** | -10.7 | 5e-24 | 35/42 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.338×** | -7.8 | 2e-12 | 29/39 (SHP-77, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.391×** | -6.7 | 3e-09 | 21/27 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.427×** | -6.1 | 2e-07 | 24/39 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.472×** | -5.2 | 3e-05 | 21/39 (Panc 03.27, CFPAC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.504×** | -4.6 | 5e-04 | 14/43 (C-33 A, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.575×** | -4.0 | 0.006 | 13/33 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.576×** | -3.9 | 0.006 | 16/44 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.592×** | -3.7 | 0.011 | 13/43 (A498, SW1417, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.610×** | -3.5 | 0.023 | 16/39 (LoVo, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.708×** | -3.5 | 0.025 | 17/36 (A498, COLO 205, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.618×** | -3.4 | 0.028 | 12/42 (A-427, HT-29, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.641×** | -3.2 | 0.065 | 7/39 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.648×** | -3.1 | 0.074 | 17/41 (COLO 205, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.648×** | -3.1 | 0.074 | 14/41 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0491× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 7.59 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0699× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0752× (z -9.6) |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0629× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 5.35 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0617× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 7.53 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 7.22 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0398× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 4.19 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0612× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 7.46 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0581× (z -10.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SHP-77 (line)]] | alt | 5.71 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0373× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.971 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK4]] | +0.77 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LIX1-AS1]] | +0.76 | +0.68 / +0.65 | both halves | 7e-06 | same gene group |
| [[ALG1L9P]] | +0.75 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.74 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.74 | +0.68 / +0.50 | both halves | 1e-05 | same gene group |
| [[STPG2]] | +0.73 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[CCDC30]] | +0.73 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[ZRANB2-DT]] | +0.73 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.73 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[NEK11]] | +0.71 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SAXO1]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SIAH2-AS1]] | +0.71 | +0.62 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAMDC2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers MAMDC2-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[LINC01917]] | B | LINC01917 activity raises MAMDC2-AS1's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without LINC01917 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[SMC5-DT]] | C | SMC5-DT's natural level strengthens MAMDC2-AS1's drug response | SMC5-DT's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.14; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZRANB2-DT]] | C | MAMDC2-AS1 activity raises ZRANB2-DT's level | lines that do not express MAMDC2-AS1 (3) vs lines expressing it (47) | 2.31× lower at baseline in the lines without MAMDC2-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LCA5, TEX9, TMEM178A; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.6, 17.3); signed map (24.9, -3.0). **Vector** length 67.0, 11.4% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +0.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -3.3 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.9 | -3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MAMDC2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q21.12 — chr9:70,033,921-70,175,888 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SMC5-DT |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48719) · Entrez [100507244](https://www.ncbi.nlm.nih.gov/gene/100507244) · Ensembl [ENSG00000204706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204706)

## Data

Gene col 12915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12915); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12915]; `tensor/DDL_lfc|DDL_z.npy` [12915]; `embed/gene_vectors.npy` [12915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12915 or target_col == 12915). Every well: [[MAMDC2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAMDC2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
