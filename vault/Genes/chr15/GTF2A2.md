---
symbol: "GTF2A2"
type: "gene"
col: 6388
ensembl_id: "ENSG00000140307"
name: "general transcription factor IIA subunit 2"
location: "15q22.2"
module: 48
arm: "+"
pooled_cpm: 60.68
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# GTF2A2

*general transcription factor IIA subunit 2* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +9.8, q 9e-20, up in 43 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.67× (z +5.5, q 4e-06, up in 36 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.528×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.493×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX17]] (+0.60, fdr 2e-05), [[ROMO1]] (+0.59, fdr 2e-05), [[MRPS18C]] (+0.59, fdr 1e-05); moves opposite to [[FANCG]] (-0.51, fdr 3e-05), [[AZIN1]] (-0.49, fdr 5e-05), [[BACE1-AS]] (-0.48, fdr 4e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.49×** | +9.8 | 9e-20 | 43/49 (HT-29, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.05×** | +7.7 | 3e-12 | 42/47 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.11×** | +7.7 | 3e-12 | 35/42 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.2 | 7e-08 | 45/47 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.5 | 4e-06 | 36/48 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.4 | 6e-06 | 38/49 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.62×** | +5.2 | 2e-05 | 39/48 (KATO III, SW480, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.58×** | +4.9 | 6e-05 | 36/48 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.57×** | +4.8 | 9e-05 | 44/48 (HT-29, COLO 205, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.51×** | +4.4 | 5e-04 | 35/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.52×** | +4.3 | 7e-04 | 34/48 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +4.3 | 9e-04 | 30/48 (C32, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.46×** | +4.0 | 0.002 | 32/48 (HT-29, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +3.9 | 0.004 | 26/48 (MIA PaCa-2, COLO 205, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.45×** | +3.7 | 0.008 | 25/45 (HT-29, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.017 | 30/48 (HOP62, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.041 | 25/48 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.062 | 19/48 (J82, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6388.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.528×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.493×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.751× | -3.0 | 0.79 | 21/48 (A-172, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 64.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[LoVo (line)]] | wt | 177 | 1 (1 ⚠) | 1 | [[Belinostat (drug)]] 0.5 µM 2.43× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.2) |
| [[PANC-1 (line)]] | alt | 61.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SW480 (line)]] | alt | 50.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A498 (line)]] | wt | 65.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[COLO 205 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HOP62 (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HT-29 (line)]] | alt | 66.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[KATO III (line)]] | alt | 72.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[LS 180 (line)]] | wt | 169 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.82× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H23 (line)]] | alt | 55.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H460 (line)]] | wt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A-172 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 22 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX17]] | +0.60 | +0.48 / +0.66 | both halves | 2e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[ROMO1]] | +0.59 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[MRPS18C]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[POLR2K]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR; STRING 968 |
| [[COX7A2]] ⚠ | +0.58 | +0.39 / +0.65 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA13]] ⚠ | +0.58 | +0.52 / +0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.55 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[MRPS36]] ⚠ | +0.54 | +0.39 / +0.59 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL51]] ⚠ | +0.54 | +0.41 / +0.57 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFC2]] | +0.53 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ATP5PD]] | +0.53 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[R3HCC1L]] | +0.53 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[SLIRP]] | +0.52 | +0.38 / +0.65 | both halves | 7e-05 |  |
| [[MRPL33]] | +0.51 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[NDUFA1]] | +0.51 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[COX6B1]] | +0.51 | +0.37 / +0.58 | both halves | 7e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCG]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[AZIN1]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[BACE1-AS]] | -0.48 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[ILF3]] | -0.46 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[SMG1P3]] | -0.46 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[PSMG1]] | -0.45 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[ATXN2L]] | -0.44 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[MTHFD1]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[CS]] | -0.44 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[IPO5]] | -0.43 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[LINC01237]] | -0.43 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ELOVL5]] | -0.42 | -0.44 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GTF2A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-48.0, -21.9); signed map (-36.5, 9.8). **Vector** length 55.8, 13.7% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.50 to 7); *Cristae formation* (reactome, mean cos +0.50 to 7); *Mitochondrial biogenesis* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +2.4 | +7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.4 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~76% of this change | -3.8 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | -1.8 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | +1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | +2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIA subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:59,638,062-59,657,541 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIA, HsT18745 |
| Gene groups (HGNC) | General transcription factor IIA complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 16 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [P52657](https://www.uniprot.org/uniprotkb/P52657) (Transcription initiation factor IIA subunit 2):

> TFIIA is a component of the transcription machinery of RNA polymerase II and plays an important role in transcriptional activation. TFIIA in a complex with TBP mediates transcriptional activity.

**Summary**, from NCBI Gene [2958](https://www.ncbi.nlm.nih.gov/gene/2958):

> Accurate transcription initiation on TATA-containing class II genes involves the ordered assembly of RNA polymerase II (POLR2A; MIM 180660) and the general initiation factors TFIIA, TFIIB (MIM 189963), TFIID (MIM 313650), TFIIE (MIM 189962), TFIIF (MIM 189968), TFIIG/TFIIJ, and TFIIH (MIM 189972). The first step involves recognition of the TATA element by the TATA-binding subunit (TBP; MIM 600075) and may be regulated by TFIIA, a factor that interacts with both TBP and a TBP-associated factor …

**Accessions** — [HGNC:4647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4647) · Entrez [2958](https://www.ncbi.nlm.nih.gov/gene/2958) · UniProt [P52657](https://www.uniprot.org/uniprotkb/P52657) · Ensembl [ENSG00000140307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140307)

## Data

Gene col 6388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6388); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6388]; `tensor/DDL_lfc|DDL_z.npy` [6388]; `embed/gene_vectors.npy` [6388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6388 or target_col == 6388). Every well: [[GTF2A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
