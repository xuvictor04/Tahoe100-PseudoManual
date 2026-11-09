---
symbol: "SUCLG1"
type: "gene"
col: 8715
ensembl_id: "ENSG00000163541"
name: "succinate-CoA ligase GDP/ADP-forming subunit alpha"
location: "2p11.2"
module: 12
arm: "+"
pooled_cpm: 55.25
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SUCLG1

*succinate-CoA ligase GDP/ADP-forming subunit alpha* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +9.0, q 1e-16, up in 42 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.66× (z +5.5, q 2e-06, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.709× (z -3.8, q 0.084, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RP9]] (+0.70, fdr 1e-05), [[SUPT20H]] (+0.69, fdr 1e-05), [[CEPT1]] (+0.69, fdr 7e-06); moves opposite to [[HCFC1]] (-0.60, fdr 1e-05), [[MAT2A]] (-0.57, fdr 1e-05), [[TARDBP]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.27×** | +9.0 | 1e-16 | 42/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.08×** | +7.7 | 3e-12 | 35/41 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.92×** | +7.2 | 1e-10 | 44/48 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.97×** | +7.2 | 1e-10 | 46/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.56×** | +6.6 | 6e-09 | 38/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.81×** | +6.5 | 6e-09 | 41/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.73×** | +6.0 | 1e-07 | 40/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.5 | 2e-06 | 37/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 2e-05 | 40/48 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +5.1 | 2e-05 | 34/48 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +4.9 | 6e-05 | 39/48 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.61×** | +4.8 | 6e-05 | 31/45 (MIA PaCa-2, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.2 | 0.001 | 36/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.06×** | +4.2 | 0.001 | 33/49 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.43×** | +3.9 | 0.004 | 31/48 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.047 | 26/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.081 | 26/48 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -3.8 | 0.084 | 30/48 (HT-29, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.751× | -3.2 | 0.32 | 26/48 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.580× | -3.1 | 0.32 | 24/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[A549 (line)]] | wt | 65.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.3) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[LoVo (line)]] | wt | 51.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 42.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[PANC-1 (line)]] | alt | 54.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.7) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[A-427 (line)]] | wt | 83.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[AsPC-1 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +8.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[LOX-IMVI (line)]] | wt | 66.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[LS 180 (line)]] | wt | 67.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H1792 (line)]] | alt | 73.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[SNU-423 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[A-172 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 61.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP9]] | +0.70 | +0.83 / +0.53 | both halves | 1e-05 |  |
| [[SUPT20H]] | +0.69 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ASB8]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.64 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.64 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[GEMIN2]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[MRPS31]] | +0.63 | +0.73 / +0.57 | both halves | 1e-05 | STRING 417 |
| [[FRA10AC1]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[POLK]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[RWDD1]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.60 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.57 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.54 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[MZF1]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SLC25A53]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.51 | -0.61 / -0.55 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SUCLG1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ASB8]] | C | ASB8's natural level weakens SUCLG1's drug response | ASB8's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.13; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.5, 3.4); signed map (-18.0, -10.6). **Vector** length 76.9, 22.9% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.7 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +2.6 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.6 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.8 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.4 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.6 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | succinate-CoA ligase GDP/ADP-forming subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:84,423,528-84,460,045 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Succinate-CoA ligase subunits |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P53597](https://www.uniprot.org/uniprotkb/P53597) (Succinate--CoA ligase):

> Succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of either ATP or GTP and thus represents the only step of substrate-level phosphorylation in the TCA. The alpha subunit of the enzyme binds the substrates coenzyme A and phosphate, while succinate binding and specificity for either ATP or GTP is provided by different beta subunits (By similarity). Also able to act as an itaconyl- and malyl-CoA synthetase.

**Summary**, from NCBI Gene [8802](https://www.ncbi.nlm.nih.gov/gene/8802):

> This gene encodes the alpha subunit of the heterodimeric enzyme succinate coenzyme A ligase. This enzyme is targeted to the mitochondria and catalyzes the conversion of succinyl CoA and ADP or GDP to succinate and ATP or GTP. Mutations in this gene are the cause of the metabolic disorder fatal infantile lactic acidosis and mitochondrial DNA depletion. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:11449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11449) · Entrez [8802](https://www.ncbi.nlm.nih.gov/gene/8802) · UniProt [P53597](https://www.uniprot.org/uniprotkb/P53597) · Ensembl [ENSG00000163541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163541)

## Data

Gene col 8715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8715); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8715]; `tensor/DDL_lfc|DDL_z.npy` [8715]; `embed/gene_vectors.npy` [8715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8715 or target_col == 8715). Every well: [[SUCLG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUCLG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
