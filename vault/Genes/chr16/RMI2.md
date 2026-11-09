---
symbol: "RMI2"
type: "gene"
col: 10635
ensembl_id: "ENSG00000175643"
name: "RecQ mediated genome instability 2"
location: "16p13.13"
module: 71
arm: "+"
pooled_cpm: 10.45
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# RMI2

*RecQ mediated genome instability 2* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.48× (z +23.2, q 0e+00, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.484× (z -9.7, q 2e-19, down in 32 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.540× (z -7.8, q 2e-12, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF367]] (+0.78, fdr 7e-06), [[MASTL]] (+0.75, fdr 7e-06), [[GPR19]] (+0.74, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.48×** | +23.2 | 0e+00 | 43/44 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +11.5 | 3e-28 | 31/43 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.38×** | +11.1 | 3e-26 | 35/42 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.54×** | +5.3 | 2e-05 | 10/25 (SHP-77, NCI-H2347, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.43×** | +4.8 | 2e-04 | 16/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.44×** | +4.6 | 3e-04 | 13/37 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.2 | 0.002 | 11/37 (SW1417, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 14/43 (RPMI-7951, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.008 | 13/48 (J82, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +3.6 | 0.017 | 13/47 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.26× | +3.1 | 0.10 | 14/33 (SW1417, LoVo, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.26× | +3.1 | 0.10 | 5/47 (J82, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.484×** | -9.7 | 2e-19 | 32/47 (SW480, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.540×** | -7.8 | 2e-12 | 26/44 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -6.6 | 1e-08 | 26/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.660×** | -5.5 | 4e-06 | 22/46 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -5.5 | 4e-06 | 18/45 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -4.8 | 2e-04 | 20/42 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.700×** | -4.8 | 2e-04 | 18/43 (A498, KATO III, …) | two highest doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.509×** | -4.7 | 2e-04 | 12/43 (A498, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.635×** | -4.3 | 9e-04 | 11/48 (A498, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -4.1 | 0.002 | 16/46 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.570×** | -3.9 | 0.004 | 10/41 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.753×** | -3.6 | 0.016 | 14/46 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.768×** | -3.4 | 0.027 | 14/38 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.833× | -3.4 | 0.027 | 15/47 (A498, H4, …) | two highest doses | low cells (technical?); position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.709×** | -3.3 | 0.038 | 8/46 (Hs 766T, SNU-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.635×** | -3.2 | 0.053 | 10/43 (SW480, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pentagastrin (drug)]] 0.05 µM |  | **0.790×** | -3.2 | 0.053 | 7/44 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.644×** | -3.1 | 0.066 | 6/37 (A-427, A498, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.799×** | -3.0 | 0.080 | 12/46 (C-33 A, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 29.2 | 0 | 8 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -16.2) |
| [[PANC-1 (line)]] | alt | 9.92 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +14.0) | [[Bortezomib (drug)]] 0.05 µM 0.202× (z -10.3) |
| [[SW480 (line)]] | alt | 13.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.309× (z -8.9) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 22.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.0) |
| [[A-172 (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.3) |
| [[A-427 (line)]] | wt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.7) |
| [[A549 (line)]] | wt | 9.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 5.10 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0706× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.139× (z -8.8) |
| [[C32 (line)]] | wt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.50× (z +9.5) | — |
| [[H4 (line)]] | wt | 9.99 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0779× (z -8.7) |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0933× (z -9.4) |
| [[HOP62 (line)]] | alt | 8.25 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HT-29 (line)]] | alt | 5.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +9.6) | — |
| [[J82 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +14.0) | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0454× (z -8.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 5.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.132× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 8.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +11.0) | — |
| [[RKO (line)]] | wt | 4.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.20× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SW1417 (line)]] | alt | 8.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF367]] | +0.78 | +0.69 / +0.82 | both halves | 7e-06 |  |
| [[MASTL]] | +0.75 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GPR19]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ASF1B]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 856 |
| [[RAD51AP1]] | +0.73 | +0.66 / +0.73 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 754 |
| [[RMI1]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 999 |
| [[ESCO2]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[C21orf58]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[DYRK4]] | +0.68 | +0.57 / +0.68 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RMI2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GOLGA2P5-1]] | B | GOLGA2P5-1 activity raises RMI2's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without GOLGA2P5-1 | 0.050 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.8, -47.0); signed map (-41.7, -47.4). **Vector** length 90.5, 18.9% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +23.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.2 | +11.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.8 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.1 | -7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -9.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.6 | -3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.5 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RecQ mediated genome instability 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:11,249,619-11,381,662 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC24665, BLAP18; previously C16orf75 |
| Reactome | 28 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E14](https://www.uniprot.org/uniprotkb/Q96E14) (RecQ-mediated genome instability protein 2):

> Essential component of the RMI complex, a complex that plays an important role in the processing of homologous recombination intermediates. It is required to regulate sister chromatid segregation and to limit DNA crossover. Essential for the stability, localization, and function of BLM, TOP3A, and complexes containing BLM. In the RMI complex, it is required to target BLM to chromatin and stress-induced nuclear foci and mitotic phosphorylation of BLM.

**Summary**, from NCBI Gene [116028](https://www.ncbi.nlm.nih.gov/gene/116028):

> RMI2 is a component of the BLM (RECQL3; MIM 604610) complex, which plays a role in homologous recombination-dependent DNA repair and is essential for genome stability (Xu et al., 2008 [PubMed 18923082]).[supplied by OMIM, Nov 2008]

**Accessions** — [HGNC:28349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28349) · Entrez [116028](https://www.ncbi.nlm.nih.gov/gene/116028) · UniProt [Q96E14](https://www.uniprot.org/uniprotkb/Q96E14) · Ensembl [ENSG00000175643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175643)

## Data

Gene col 10635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10635); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10635]; `tensor/DDL_lfc|DDL_z.npy` [10635]; `embed/gene_vectors.npy` [10635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10635 or target_col == 10635). Every well: [[RMI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
