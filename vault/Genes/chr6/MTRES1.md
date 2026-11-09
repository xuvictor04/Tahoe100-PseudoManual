---
symbol: "MTRES1"
type: "gene"
col: 5058
ensembl_id: "ENSG00000130349"
name: "mitochondrial transcription rescue factor 1"
location: "6q21"
module: 12
arm: "+"
pooled_cpm: 11.58
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MTRES1

*mitochondrial transcription rescue factor 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.63× (z +12.1, q 1e-30, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.315× (z -14.4, q 5e-44, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARS2]] (+0.72, fdr 7e-06), [[KRI1]] (+0.71, fdr 1e-05), [[GTF2H5]] (+0.71, fdr 7e-06); moves opposite to [[PGRMC1]] (-0.70, fdr 1e-05), [[CMPK1]] (-0.64, fdr 7e-06), [[SUMO3]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RAPGEF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +12.1 | 1e-30 | 44/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +10.8 | 1e-24 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +7.6 | 5e-12 | 35/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +6.3 | 5e-08 | 23/41 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.9 | 9e-05 | 20/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.002 | 18/47 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 10/46 (SW480, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.008 | 14/45 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.039 | 8/46 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.048 | 8/47 (SW 1088, SW1417, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.094 | 10/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.40× | +3.0 | 0.11 | 5/44 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5058.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.315×** | -14.4 | 5e-44 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.424×** | -10.0 | 7e-21 | 35/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -9.5 | 5e-19 | 34/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.527×** | -8.0 | 2e-13 | 33/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.532×** | -7.3 | 3e-11 | 31/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -6.7 | 1e-09 | 26/40 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -6.3 | 3e-08 | 29/46 (PANC-1, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.600×** | -6.0 | 1e-07 | 28/46 (PANC-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -5.4 | 3e-06 | 23/46 (C32, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -4.9 | 6e-05 | 23/47 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.483×** | -4.7 | 1e-04 | 19/43 (RPMI-7951, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.688×** | -4.6 | 2e-04 | 19/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.587×** | -3.5 | 0.022 | 10/21 (SW480, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.587×** | -3.5 | 0.022 | 17/35 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -3.2 | 0.048 | 12/46 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.049 | 9/47 (BT-474, SW 1088, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.778×** | -3.1 | 0.065 | 9/47 (COLO 205, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0913× (z -19.9) |
| [[SW480 (line)]] | alt | 14.4 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.52× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -15.2) |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -13.0) |
| [[C32 (line)]] | wt | 9.52 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0906× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 10.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0700× (z -13.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 9.74 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.145× (z -11.4) |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0985× (z -8.9) ⚠ toxic |
| [[J82 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0997× (z -12.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0953× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -8.7) |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0997× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARS2]] | +0.72 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[KRI1]] | +0.71 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[GTF2H5]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.68 | +0.73 / +0.68 | both halves | 7e-06 | pathway: Mitochondrial ribosome-associated quality control |
| [[BRIX1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SURF6]] | +0.67 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[GMEB1]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[USP4]] | +0.66 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MRPL57]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 | pathway: Mitochondrial ribosome-associated quality control; STRING 868 |
| [[FRA10AC1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RPP14]] | +0.65 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGRMC1]] | -0.70 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[CMPK1]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[SUMO3]] | -0.63 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.62 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.62 | -0.39 / -0.66 | both halves | 6e-05 |  |
| [[GHITM]] | -0.61 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[EDEM1]] | -0.60 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[PAPOLA]] | -0.60 | -0.29 / -0.67 | both halves | 3e-04 |  |
| [[STT3B]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[CYBRD1]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[BCL2L2]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF4]] | B | RAPGEF4 activity raises MTRES1's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without RAPGEF4 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-41.2, -1.0); signed map (-15.6, -10.8). **Vector** length 67.8, 12.1% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +10.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.2 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.8 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial transcription rescue factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:107,028,199-107,051,586 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC230, PRED31; previously C6orf203 |
| Reactome | 3 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0P8](https://www.uniprot.org/uniprotkb/Q9P0P8) (Mitochondrial transcription rescue factor 1):

> Mitochondrial RNA-binding protein involved in mitochondrial transcription regulation. Functions as a protective factor to maintain proper mitochondrial RNA level during stress. Acts at the transcription level and its protective function depends on its RNA binding ability. Part of a mitoribosome-associated quality control pathway that prevents aberrant translation by responding to interruptions during elongation. As heterodimer with MTRF, ejects the unfinished nascent chain and peptidyl transfer …

**Summary**, from NCBI Gene [51250](https://www.ncbi.nlm.nih.gov/gene/51250):

> Enables ribosomal large subunit binding activity and tRNA binding activity. Involved in regulation of mitochondrial transcription and rescue of stalled mitochondrial ribosome. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17971) · Entrez [51250](https://www.ncbi.nlm.nih.gov/gene/51250) · UniProt [Q9P0P8](https://www.uniprot.org/uniprotkb/Q9P0P8) · Ensembl [ENSG00000130349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130349)

## Data

Gene col 5058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5058); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5058]; `tensor/DDL_lfc|DDL_z.npy` [5058]; `embed/gene_vectors.npy` [5058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5058 or target_col == 5058). Every well: [[MTRES1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTRES1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
