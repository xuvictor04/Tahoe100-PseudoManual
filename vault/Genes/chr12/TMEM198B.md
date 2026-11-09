---
symbol: "TMEM198B"
type: "gene"
col: 11327
ensembl_id: "ENSG00000182796"
name: "transmembrane protein 198B (pseudogene)"
location: "12q13.2"
module: 157
arm: "+"
pooled_cpm: 4.94
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# TMEM198B

*transmembrane protein 198B (pseudogene)* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.62× (z +11.2, q 2e-26, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.344× (z -8.9, q 4e-16, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMNTD2]] (+0.65, fdr 1e-05), [[EME2]] (+0.61, fdr 2e-05), [[NEIL1]] (+0.59, fdr 3e-05); moves opposite to [[PSMA7]] (-0.48, fdr 3e-04), [[METTL2A]] (-0.47, fdr 5e-04), [[ZMYM1]] (-0.46, fdr 2e-04).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ID2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +11.2 | 2e-26 | 36/38 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +7.0 | 7e-10 | 15/26 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +6.6 | 7e-09 | 24/35 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +6.4 | 3e-08 | 2/5 (PANC-1, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +5.3 | 1e-05 | 4/10 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +4.9 | 9e-05 | 15/48 (Panc 03.27, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +4.6 | 4e-04 | 18/47 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.5 | 6e-04 | 13/47 (A-172, LoVo, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.3 | 9e-04 | 16/45 (A498, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.45×** | +4.3 | 0.001 | 16/46 (LoVo, RKO, …) | top dose only | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.1 | 0.002 | 9/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.025 | 8/43 (KATO III, PANC-1, …) | two highest doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.51×** | +3.4 | 0.035 | 11/43 (A549, hTERT-HPNE, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.049 | 10/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.056 | 16/47 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.056 | 10/47 (Hs 766T, AsPC-1, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.069 | 3/43 (SW480, C-33 A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11327.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.344×** | -8.9 | 4e-16 | 32/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.386×** | -7.9 | 6e-13 | 29/43 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.420×** | -7.2 | 9e-11 | 28/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.422×** | -7.2 | 9e-11 | 28/43 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.500×** | -5.8 | 8e-07 | 23/37 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.517×** | -5.5 | 3e-06 | 21/37 (NCI-H23, COLO 205, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.533×** | -5.3 | 1e-05 | 23/47 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.557×** | -4.7 | 2e-04 | 22/43 (RPMI-7951, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.598×** | -4.3 | 0.001 | 19/46 (A549, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -4.2 | 0.002 | 19/43 (SW48, HOP62, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.617×** | -3.9 | 0.005 | 14/45 (C-33 A, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.656×** | -3.5 | 0.019 | 9/47 (A-427, NCI-H661, …) | two highest doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.655×** | -3.4 | 0.028 | 12/44 (BT-474, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.770×** | -3.1 | 0.073 | 17/37 (RPMI-7951, AsPC-1, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.09 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0597× (z -8.9) |
| [[SW480 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0890× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -9.3) |
| [[A-427 (line)]] | wt | 7.60 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0603× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 4.29 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0712× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 4.77 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0938× (z -9.0) |
| [[LoVo (line)]] | wt | 8.28 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0889× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0556× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 6.91 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0388× (z -12.0) |
| [[PANC-1 (line)]] | alt | 3.43 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0722× (z -10.2) |
| [[A-172 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMNTD2]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[EME2]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NEIL1]] | +0.59 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[INPPL1]] | +0.59 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[AKT2]] | +0.58 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[AP1G2-AS1]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CDNF]] | +0.56 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[DPY19L3-DT]] | +0.56 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[PCED1A]] | +0.55 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[HFM1]] | +0.55 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[LENG8]] | +0.55 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[ZNF514]] | +0.55 | +0.47 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA7]] | -0.48 | -0.26 / -0.40 | both halves | 3e-04 |  |
| [[METTL2A]] | -0.47 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[ZMYM1]] | -0.46 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[METTL2B]] | -0.46 | -0.26 / -0.43 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | B | ID2-AS1 activity raises TMEM198B's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without ID2-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[TOP2A]] | B | TOP2A activity lowers TMEM198B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.9, 29.3); signed map (31.8, -20.6). **Vector** length 55.0, 7.63% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +4.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -1.8 | -4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 198B (pseudogene) |
| Locus type | pseudogene |
| Location | 12q13.2 — chr12:55,832,159-55,834,988 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43629) · Entrez [440104](https://www.ncbi.nlm.nih.gov/gene/440104) · Ensembl [ENSG00000182796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182796)

## Data

Gene col 11327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11327); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11327]; `tensor/DDL_lfc|DDL_z.npy` [11327]; `embed/gene_vectors.npy` [11327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11327 or target_col == 11327). Every well: [[TMEM198B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM198B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
