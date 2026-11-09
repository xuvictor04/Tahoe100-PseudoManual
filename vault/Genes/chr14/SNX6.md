---
symbol: "SNX6"
type: "gene"
col: 4982
ensembl_id: "ENSG00000129515"
name: "sorting nexin 6"
location: "14q13.1"
module: 167
arm: "+"
pooled_cpm: 159.05
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# SNX6

*sorting nexin 6* — 14q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.63× (z +9.5, q 1e-18, up in 40 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (A549 2.56×, SW480 2.26×, A498 2.21×, MIA PaCa-2 2.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 2.38×, SW480 1.92×, SW 900 2.33×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 1.82×; ⚠ cell-cycle shift, explains ~52% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.699× (z -10.9, q 1e-24, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAFAH1B1]] (+0.61, fdr 1e-05), [[TAOK3]] (+0.57, fdr 3e-05), [[C1R]] (+0.57, fdr 1e-05); moves opposite to [[IVNS1ABP]] (-0.55, fdr 2e-05), [[SAMD10]] (-0.53, fdr 6e-05), [[BEND3]] (-0.52, fdr 4e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4982.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (A549 2.56×, SW480 2.26×, A498 2.21×, MIA PaCa-2 2.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 2.38×, SW480 1.92×, SW 900 2.33×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 1.82×; ⚠ cell-cycle shift, explains ~52% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +9.5 | 1e-18 | 40/49 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.7 | 4e-06 | 28/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +4.6 | 8e-04 | 26/45 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4982.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -10.9 | 1e-24 | 41/49 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.765×** | -8.1 | 1e-13 | 29/48 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.746×** | -6.3 | 6e-08 | 36/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.767×** | -5.7 | 2e-06 | 33/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.792×** | -5.0 | 7e-05 | 30/48 (SNU-423, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -4.9 | 8e-05 | 29/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.796×** | -4.9 | 8e-05 | 31/48 (CFPAC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.805×** | -4.6 | 2e-04 | 27/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.868× | -4.3 | 0.001 | 19/48 (CFPAC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Folic acid (drug)]] 5 µM |  | 0.883× | -3.8 | 0.010 | 5/48 (SW 900, KATO III, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.841× | -3.7 | 0.010 | 19/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.761× | -3.1 | 0.11 | 24/49 (CFPAC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 140 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 306 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -14.2) |
| [[J82 (line)]] | alt | 177 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 268 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -13.5) |
| [[A498 (line)]] | wt | 153 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +10.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -9.8) |
| [[HOP62 (line)]] | alt | 161 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.647× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 208 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.526× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 130 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +13.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -10.9) |
| [[A549 (line)]] | wt | 207 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +12.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -16.4) |
| [[AsPC-1 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.543× (z -8.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[BT-474 (line)]] | alt | 211 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 187 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 228 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 181 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.517× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 277 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -12.3) |
| [[PANC-1 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.4) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[RKO (line)]] | wt | 131 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.6) |
| [[SNU-423 (line)]] | alt | 183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -15.5) |
| [[SW480 (line)]] | alt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.631× (z -8.9) |
| [[HS-578T (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.6) |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.122× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -12.9) |
| [[SNU-1 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 140 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0972× (z -10.0) |
| [[SW 900 (line)]] | alt | 89.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 155 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 102 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 126 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 190 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 625 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 211 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B1]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TAOK3]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[C1R]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[OPTN]] | +0.55 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[XRN1]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[NUB1]] | +0.53 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[ROCK1]] | +0.51 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TYMP]] | +0.51 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[SP100]] | +0.51 | +0.30 / +0.62 | both halves | 2e-04 |  |
| [[MAP4K3]] | +0.51 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[ZYG11B]] | +0.50 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[CHMP5]] | +0.49 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IVNS1ABP]] | -0.55 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[SAMD10]] | -0.53 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[BEND3]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ETV4]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[PIGW]] | -0.49 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[BCL2]] | -0.48 | -0.56 / -0.43 | both halves | 4e-05 |  |
| [[DPY19L3-DT]] | -0.48 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ASB1]] | -0.48 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[CYP27B1]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[TBRG4]] | -0.47 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[SHC3]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LRP5]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SNX6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.373). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.8, -56.7); signed map (36.5, -35.0). **Vector** length 105, 30.4% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +9.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +1.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -10.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.4 | -4.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.2 | -2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.1 — chr14:34,561,093-34,630,160 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNH7](https://www.uniprot.org/uniprotkb/Q9UNH7) (Sorting nexin-6):

> Involved in several stages of intracellular trafficking. Interacts with membranes phosphatidylinositol 3,4-bisphosphate and/or phosphatidylinositol 4,5-bisphosphate (Probable). Acts in part as component of the retromer membrane-deforming SNX-BAR subcomplex. The SNX-BAR retromer mediates retrograde transport of cargo proteins from endosomes to the trans-Golgi network (TGN) and is involved in endosome-to-plasma membrane transport for cargo protein recycling. The SNX-BAR subcomplex functions to …

**Summary**, from NCBI Gene [58533](https://www.ncbi.nlm.nih.gov/gene/58533):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein associates with the long isoform of the leptin receptor, the transforming growth factor-beta family of receptor serine-threonine kinases, and with receptor tyrosine kinases for platelet-derived growth factor, insulin, and epidermal growth factor. This protein may form oligomeric …

**Accessions** — [HGNC:14970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14970) · Entrez [58533](https://www.ncbi.nlm.nih.gov/gene/58533) · UniProt [Q9UNH7](https://www.uniprot.org/uniprotkb/Q9UNH7) · Ensembl [ENSG00000129515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129515)

## Data

Gene col 4982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4982); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4982]; `tensor/DDL_lfc|DDL_z.npy` [4982]; `embed/gene_vectors.npy` [4982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4982 or target_col == 4982). Every well: [[SNX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
