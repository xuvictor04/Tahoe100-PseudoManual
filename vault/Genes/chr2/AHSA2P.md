---
symbol: "AHSA2P"
type: "gene"
col: 10353
ensembl_id: "ENSG00000173209"
name: "activator of HSP90 ATPase homolog 2, pseudogene"
location: "2p15"
module: 157
arm: "+"
pooled_cpm: 34.54
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# AHSA2P

*activator of HSP90 ATPase homolog 2, pseudogene* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.47× (z +7.5, q 4e-11, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.56× (z +6.2, q 1e-07, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.392× (z -13.0, q 5e-36, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCED1A]] (+0.71, fdr 1e-05), [[ALKBH6]] (+0.70, fdr 7e-06), [[DNAJA4]] (+0.68, fdr 1e-05); moves opposite to [[CDKN2D]] (-0.58, fdr 3e-05), [[TXNDC17]] (-0.56, fdr 5e-05), [[ANAPC11]] (-0.56, fdr 1e-04).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.47×** | +7.5 | 4e-11 | 37/48 (A498, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.65×** | +6.5 | 2e-08 | 36/48 (RKO, LS 180, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +6.2 | 1e-07 | 34/48 (KATO III, A498, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.48×** | +5.4 | 1e-05 | 30/48 (A-172, HT-29, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.0 | 6e-05 | 25/48 (RKO, C32, …) | top dose only | position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **1.66×** | +3.7 | 0.022 | 19/47 (LOX-IMVI, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | 1.52× | +3.0 | 0.19 | 17/42 (RKO, LS 180, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.392×** | -13.0 | 5e-36 | 47/48 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.417×** | -12.2 | 1e-31 | 44/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.424×** | -11.9 | 2e-30 | 44/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.582×** | -7.5 | 7e-12 | 39/48 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.619×** | -6.7 | 3e-09 | 35/47 (SW 1271, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.654×** | -5.9 | 3e-07 | 30/47 (LS 180, BT-474, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.741×** | -5.9 | 3e-07 | 28/47 (MIA PaCa-2, RKO, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -5.7 | 1e-06 | 34/48 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.642×** | -5.4 | 4e-06 | 29/47 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.709×** | -4.8 | 9e-05 | 26/47 (RKO, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.547×** | -4.4 | 6e-04 | 27/47 (SNU-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.589×** | -3.9 | 0.006 | 23/48 (LoVo, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.769×** | -3.7 | 0.011 | 19/48 (A-172, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.775×** | -3.6 | 0.015 | 23/48 (LS 180, HS-578T, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.776×** | -3.5 | 0.016 | 17/48 (HEC-1-A, NCI-H1792, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 69.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 49.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 33.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.280× (z -11.3) |
| [[A549 (line)]] | wt | 51.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.304× (z -9.5) |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.313× (z -9.5) |
| [[LoVo (line)]] | wt | 27.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.305× (z -9.8) |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.272× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -9.8) |
| [[SW480 (line)]] | alt | 48.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.394× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 34.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -8.9) |
| [[HCT15 (line)]] | alt | 42.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.389× (z -8.6) |
| [[HS-578T (line)]] | alt | 19.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -9.5) |
| [[LS 180 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.359× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 39.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.246× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 31.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -9.0) |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -8.8) |
| [[SW 1271 (line)]] | alt | 59.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0768× (z -9.4) |
| [[A-172 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCED1A]] | +0.71 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ALKBH6]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[DNAJA4]] | +0.68 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SRSF5]] | +0.65 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[UBXN8]] | +0.63 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[BMS1P23]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MTX1]] | +0.62 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[AP1G2-AS1]] | +0.61 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[DHX38]] | +0.61 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[RCC1L]] | +0.61 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[ZFHX2-AS1]] | +0.59 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[TYW3]] | +0.59 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | -0.58 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.56 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ANAPC11]] | -0.56 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[LAGE3]] | -0.54 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[LGALS1]] | -0.54 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[DOP1A]] | -0.54 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[INIP]] | -0.54 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[KRTCAP2]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ATP5F1D]] ⚠ | -0.53 | -0.24 / -0.45 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ANTKMT]] | -0.53 | -0.16 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[MRPL41]] ⚠ | -0.52 | -0.29 / -0.40 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ARL3]] | -0.52 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[PAFAH1B3]] | -0.51 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[PIBF1]] | -0.51 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[PUSL1]] | -0.51 | -0.25 / -0.32 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers AHSA2P's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.3, 10.1); signed map (-24.1, -29.0). **Vector** length 103, 25.5% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.7 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +8.1 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.7 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.2 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.2 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.0 | -13.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -11.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | activator of HSP90 ATPase homolog 2, pseudogene |
| Locus type | pseudogene |
| Location | 2p15 — chr2:61,177,539-61,186,786 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | DKFZp564C236, Hch1, AHA1; previously AHSA2 |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q719I0](https://www.uniprot.org/uniprotkb/Q719I0) (Putative activator of 90 kDa heat shock protein ATPase homolog 2):

> Co-chaperone that stimulates HSP90 ATPase activity.

**Summary**, from NCBI Gene [130872](https://www.ncbi.nlm.nih.gov/gene/130872):

> Predicted to enable ATPase activator activity. Predicted to be involved in protein folding. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20437) · Entrez [130872](https://www.ncbi.nlm.nih.gov/gene/130872) · UniProt [Q719I0](https://www.uniprot.org/uniprotkb/Q719I0) · Ensembl [ENSG00000173209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173209)

## Data

Gene col 10353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10353); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10353]; `tensor/DDL_lfc|DDL_z.npy` [10353]; `embed/gene_vectors.npy` [10353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10353 or target_col == 10353). Every well: [[AHSA2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHSA2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
