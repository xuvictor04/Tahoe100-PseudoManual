---
symbol: "COMMD7"
type: "gene"
col: 7397
ensembl_id: "ENSG00000149600"
name: "COMM domain containing 7"
location: "20q11.21"
module: 17
arm: "+"
pooled_cpm: 20.37
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# COMMD7

*COMM domain containing 7* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.29× (z +4.3, q 0.006, up in 19 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.25× (z +3.9, q 0.020, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.473× (z -13.1, q 2e-36, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.592× (z -13.0, q 3e-36, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CGRRF1]] (+0.61, fdr 3e-05), [[SUCLG1]] (+0.60, fdr 1e-05), [[MAP4K5]] (+0.59, fdr 1e-05); moves opposite to [[TMBIM6]] (-0.52, fdr 4e-05), [[M6PR]] (-0.51, fdr 5e-05), [[CFL1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.3 | 0.006 | 19/31 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.3 | 0.006 | 19/39 (A-427, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.020 | 17/48 (SNU-1, BT-474, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.021 | 12/45 (NCI-H1573, HOP62, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.024 | 14/48 (SNU-1, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +3.7 | 0.024 | 12/36 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[vincristine (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.032 | 2/41 (NCI-H1573, RPMI-7951) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.11 | 11/46 (A-427, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.11 | 8/48 (NCI-H1792, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.473×** | -13.1 | 2e-36 | 39/48 (SNU-423, HS-578T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -13.0 | 3e-36 | 37/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.478×** | -12.9 | 6e-36 | 39/48 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.511×** | -11.8 | 9e-30 | 36/47 (SNU-1, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.513×** | -11.7 | 1e-29 | 39/48 (RKO, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -11.3 | 1e-27 | 33/47 (SNU-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.553×** | -10.4 | 2e-23 | 36/47 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.572×** | -9.8 | 8e-21 | 35/47 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -9.8 | 1e-20 | 36/47 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -9.7 | 2e-20 | 35/46 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.738×** | -7.5 | 3e-12 | 29/48 (SW1417, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.712×** | -6.0 | 1e-07 | 23/48 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.718×** | -5.6 | 1e-06 | 21/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.740×** | -5.3 | 5e-06 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -4.7 | 1e-04 | 21/48 (SNU-423, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.725×** | -2.9 | 0.086 | 7/48 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.728×** | -2.9 | 0.092 | 10/45 (NCI-H2347, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 59.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.4) |
| [[SW480 (line)]] | alt | 15.8 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -13.8) |
| [[J82 (line)]] | alt | 39.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -16.6) |
| [[SW1417 (line)]] | alt | 40.6 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.371× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.496× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 33.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -12.4) |
| [[RKO (line)]] | wt | 29.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.5) |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.369× (z -12.4) |
| [[C32 (line)]] | wt | 17.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.249× (z -8.5) |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.5) |
| [[HS-578T (line)]] | alt | 30.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -10.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.3) |
| [[A-172 (line)]] | wt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.1) |
| [[A498 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -8.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 23.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.449× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 37.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.1) |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -9.9) |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.185× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0686× (z -10.6) |
| [[KATO III (line)]] | alt | 17.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.237× (z -9.0) |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.323× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.334× (z -8.9) |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGRRF1]] | +0.61 | +0.75 / +0.43 | both halves | 3e-05 |  |
| [[SUCLG1]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MAP4K5]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[BBS5]] | +0.57 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[RP9]] | +0.57 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[QDPR]] | +0.56 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[MRPL21]] | +0.56 | +0.59 / +0.38 | both halves | 7e-05 |  |
| [[COMMD2]] | +0.56 | +0.60 / +0.55 | both halves | 1e-05 | same gene group; pathway: Neddylation; STRING 967 |
| [[NEK3]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ANXA7]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RWDD1]] | +0.54 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[REPS1]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMBIM6]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[M6PR]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[CFL1]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SNRPB]] | -0.47 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[HCFC1]] | -0.47 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[DPH1-AS1]] | -0.46 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[EIF4EBP2]] | -0.46 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[MZF1]] | -0.46 | -0.43 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises COMMD7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.6, -2.9); signed map (-23.8, -13.2). **Vector** length 81.2, 16.5% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.8 | -12.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.6 | -9.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -7.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,702,699-32,743,467 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1085F17.3; previously C20orf92 |
| Gene groups (HGNC) | COMM domain containing; CCC complex |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VX2](https://www.uniprot.org/uniprotkb/Q86VX2) (COMM domain-containing protein 7):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. Associates with the NF-kappa-B complex and suppresses its transcriptional activity.

**Summary**, from NCBI Gene [149951](https://www.ncbi.nlm.nih.gov/gene/149951):

> Enables NF-kappaB binding activity. Involved in negative regulation of DNA-templated transcription and tumor necrosis factor-mediated signaling pathway. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16223) · Entrez [149951](https://www.ncbi.nlm.nih.gov/gene/149951) · UniProt [Q86VX2](https://www.uniprot.org/uniprotkb/Q86VX2) · Ensembl [ENSG00000149600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149600)

## Data

Gene col 7397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7397); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7397]; `tensor/DDL_lfc|DDL_z.npy` [7397]; `embed/gene_vectors.npy` [7397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7397 or target_col == 7397). Every well: [[COMMD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
