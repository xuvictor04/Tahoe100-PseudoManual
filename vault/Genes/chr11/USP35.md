---
symbol: "USP35"
type: "gene"
col: 3984
ensembl_id: "ENSG00000118369"
name: "ubiquitin specific peptidase 35"
location: "11q14.1"
module: 30
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# USP35

*ubiquitin specific peptidase 35* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.29× (z +9.7, q 2e-19, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.478× (z -12.2, q 1e-31, down in 34 of 40 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.413× (z -9.6, q 2e-19, down in 25 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHSD1]] (+0.78, fdr 7e-06), [[LRFN3]] (+0.73, fdr 7e-06), [[RNF216P1]] (+0.73, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.72, fdr 7e-06), [[WARS2-AS1]] (-0.68, fdr 3e-05), [[SMIM19]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +9.7 | 2e-19 | 33/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +9.5 | 1e-18 | 31/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +7.4 | 2e-11 | 19/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +7.1 | 2e-10 | 17/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +5.8 | 7e-07 | 13/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.68×** | +5.7 | 1e-06 | 14/43 (LS 180, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +5.6 | 2e-06 | 20/40 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.6 | 3e-04 | 10/46 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +4.2 | 0.002 | 4/45 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.003 | 7/45 (BT-474, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.79×** | +3.5 | 0.021 | 1/15 (PANC-1) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.039 | 2/44 (LS 180, SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Lumateperone (tosylate) (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.079 | 2/46 (NCI-H460, MIA PaCa-2) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.079 | 6/44 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.478×** | -12.2 | 1e-31 | 34/40 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.413×** | -9.6 | 2e-19 | 25/39 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.481×** | -8.2 | 3e-14 | 24/44 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.544×** | -7.1 | 1e-10 | 26/47 (NCI-H460, SNU-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.558×** | -6.8 | 9e-10 | 20/37 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -6.3 | 4e-08 | 23/46 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.615×** | -5.7 | 1e-06 | 22/45 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -5.0 | 3e-05 | 14/38 (HS-578T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.677×** | -4.4 | 7e-04 | 14/31 (A549, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.004 | 17/39 (NCI-H2347, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.720×** | -3.9 | 0.006 | 15/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -3.6 | 0.013 | 9/44 (SW48, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.065 | 11/33 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Thymol (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.083 | 10/46 (CHP-212, NCI-H1573, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.03 | 0 | 3 | — | [[Erythromycin (drug)]] 0.5 µM 0.0727× (z -9.1) |
| [[HOP62 (line)]] | alt | 3.57 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Bestatin (drug)]] 0.05 µM 0.0719× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 5.20 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -12.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 9.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 5.14 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.103× (z -9.9) |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0615× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 4.35 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.112× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 5.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0854× (z -8.6) |
| [[PANC-1 (line)]] | alt | 3.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 3.12 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0786× (z -10.1) |
| [[A-427 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD1]] | +0.78 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[LRFN3]] | +0.73 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[RNF216P1]] | +0.73 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[KCTD21]] | +0.71 | +0.68 / +0.58 | both halves | 7e-06 | STRING 516; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[RIMS3]] | +0.71 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[OSBPL7]] | +0.70 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SNTA1]] | +0.69 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[PLD2]] | +0.69 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.68 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[PEDS1]] | +0.68 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.68 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[NTAN1]] | +0.67 | +0.67 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.72 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | -0.68 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[SMIM19]] | -0.67 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[R3HDM2]] | -0.66 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[ZNF337-AS1]] | -0.65 | -0.68 / -0.36 | both halves | 1e-04 |  |
| [[INO80D]] | -0.65 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[HELQ]] | -0.64 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[CCDC125]] | -0.63 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[KDSR]] | -0.63 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[ZNF518A]] | -0.63 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[UNK]] | -0.63 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[BAZ2B]] | -0.63 | -0.55 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises USP35's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.0, -1.0); signed map (-38.9, -6.7). **Vector** length 65.5, 9.48% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.6 | +5.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.3 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.8 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -3.6 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:78,188,812-78,215,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1372 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2H5](https://www.uniprot.org/uniprotkb/Q9P2H5) (Ubiquitin carboxyl-terminal hydrolase 35):

> Deubiquitinase that plays a role in different processes including cell cycle regulation, mitophagy or endoplasmic reticulum stress. Inhibits TNFalpha-induced NF-kappa-B activation through stabilizing TNIP2 protein via deubiquitination. Plays an essential role during mitosis by deubiquitinating and thereby regulating the levels of Aurora B/AURKB protein. In addition, regulates the protein levels of other key component of the chromosomal passenger complex (CPC) such as survivin/BIRC5 or …

**Summary**, from NCBI Gene [57558](https://www.ncbi.nlm.nih.gov/gene/57558):

> This gene encodes a member of the peptidase C19 family of ubiquitin-specific proteases. These deubiquitinating enzymes (DUBs) catalyze the removal of ubiquitin proteins from other proteins. The encoded protein associates with polarized mitochondria and has been shown to inhibit NF-kappa B activation and delay PARK2-mediated degradation of mitochondria. Expression of this gene is upregulated by the let-7a microRNA and reduced expression has been observed in human tumor tissues. [provided by …

**Accessions** — [HGNC:20061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20061) · Entrez [57558](https://www.ncbi.nlm.nih.gov/gene/57558) · UniProt [Q9P2H5](https://www.uniprot.org/uniprotkb/Q9P2H5) · Ensembl [ENSG00000118369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118369)

## Data

Gene col 3984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3984); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3984]; `tensor/DDL_lfc|DDL_z.npy` [3984]; `embed/gene_vectors.npy` [3984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3984 or target_col == 3984). Every well: [[USP35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
