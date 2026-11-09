---
symbol: "PIN4"
type: "gene"
col: 2236
ensembl_id: "ENSG00000102309"
name: "peptidylprolyl cis/trans isomerase, NIMA-interacting 4"
location: "Xq13.1"
module: 118
arm: "+"
pooled_cpm: 41.55
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# PIN4

*peptidylprolyl cis/trans isomerase, NIMA-interacting 4* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +9.3, q 6e-18, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.509× (z -10.2, q 2e-21, down in 42 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.526× (z -9.6, q 2e-19, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOXRED1]] (+0.68, fdr 9e-06), [[ANKRD49]] (+0.68, fdr 7e-06), [[ING4]] (+0.67, fdr 1e-05); moves opposite to [[CDCA7]] (-0.64, fdr 7e-06), [[PPAT]] (-0.63, fdr 1e-05), [[ICMT]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +9.3 | 6e-18 | 39/48 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.9 | 6e-13 | 33/45 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.3 | 6e-11 | 39/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +7.2 | 1e-10 | 34/48 (NCI-H1573, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.2 | 5e-08 | 27/39 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 5e-08 | 32/48 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.6 | 3e-04 | 21/48 (A-172, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +4.5 | 4e-04 | 24/42 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.002 | 23/48 (LoVo, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.002 | 24/48 (Panc 03.27, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.011 | 19/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.014 | 21/48 (SNU-423, LS 180, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +3.6 | 0.017 | 17/46 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.027 | 15/48 (CFPAC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.027 | 20/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.045 | 15/48 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.049 | 18/47 (SW480, SW48, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -10.2 | 2e-21 | 42/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.526×** | -9.6 | 2e-19 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -8.8 | 3e-16 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -5.6 | 4e-06 | 31/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.736×** | -4.4 | 0.001 | 25/47 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.773×** | -3.9 | 0.009 | 25/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.773×** | -3.9 | 0.009 | 21/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.654×** | -3.3 | 0.062 | 17/48 (AN3 CA, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.811×** | -3.1 | 0.097 | 17/47 (NCI-H661, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.811×** | -3.1 | 0.097 | 18/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.3 | 1 | 6 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.203× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.331× (z -13.1) |
| [[SW480 (line)]] | alt | 69.7 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -16.6) |
| [[PANC-1 (line)]] | alt | 40.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.271× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -12.1) |
| [[A-172 (line)]] | wt | 42.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 31.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.264× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 57.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A498 (line)]] | wt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +11.0) | — |
| [[A549 (line)]] | wt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 69.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.311× (z -9.0) ⚠ toxic |
| [[J82 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -12.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.375× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 51.6 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.93× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 50.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOXRED1]] | +0.68 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[ANKRD49]] | +0.68 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[ING4]] | +0.67 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ATP6V1E1]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.65 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[ZSWIM3]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[KDM5A]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SEM1]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[TBCA]] | +0.62 | +0.67 / +0.66 | both halves | 7e-06 | STRING 497 |
| [[SYF2]] | +0.61 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[BRAP]] | +0.61 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.61 | +0.67 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA7]] | -0.64 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[PPAT]] | -0.63 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ICMT]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[THEM6]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DDX12P]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[PARP1]] | -0.58 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SIGMAR1]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[DDX11]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SSX2IP]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[DSCC1]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[POLD2]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIN4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.9, 3.2); signed map (-2.5, -4.6). **Vector** length 77.2, 17.2% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +1.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +0.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl cis/trans isomerase, NIMA-interacting 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:72,181,353-72,302,926 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAR14, PAR17, EPVH |
| Gene groups (HGNC) | Parvulins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y237](https://www.uniprot.org/uniprotkb/Q9Y237) (Peptidyl-prolyl cis-trans isomerase NIMA-interacting 4):

> Isoform 1 is involved as a ribosomal RNA processing factor in ribosome biogenesis. Binds to tightly bent AT-rich stretches of double-stranded DNA.; Isoform 2 binds to double-stranded DNA.

**Summary**, from NCBI Gene [5303](https://www.ncbi.nlm.nih.gov/gene/5303):

> This gene encodes a member of the parvulin subfamily of the peptidyl-prolyl cis/trans isomerase protein family. The encoded protein catalyzes the isomerization of peptidylprolyl bonds, and may play a role in the cell cycle, chromatin remodeling, and/or ribosome biogenesis. The encoded protein may play an additional role in the mitochondria. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:8992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8992) · Entrez [5303](https://www.ncbi.nlm.nih.gov/gene/5303) · UniProt [Q9Y237](https://www.uniprot.org/uniprotkb/Q9Y237) · Ensembl [ENSG00000102309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102309)

## Data

Gene col 2236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2236); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2236]; `tensor/DDL_lfc|DDL_z.npy` [2236]; `embed/gene_vectors.npy` [2236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2236 or target_col == 2236). Every well: [[PIN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
