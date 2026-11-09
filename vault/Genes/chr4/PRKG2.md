---
symbol: "PRKG2"
type: "gene"
col: 6209
ensembl_id: "ENSG00000138669"
name: "protein kinase cGMP-dependent 2"
location: "4q21.21"
module: 158
arm: "+"
pooled_cpm: 5.69
n_lines_expressing: 33
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# PRKG2

*protein kinase cGMP-dependent 2* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +7.0, q 1e-09, up in 18 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.470× (z -8.4, q 2e-14, down in 20 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKG2-AS1]] (+0.56, fdr 1e-05, ⚠ same locus), [[C6orf141]] (+0.56, fdr 3e-05), [[ARHGAP25]] (+0.53, fdr 2e-05), [[C5orf63]] (+0.51, fdr 3e-05); moves opposite to [[EFCAB11]] (-0.48, fdr 3e-05), [[GUCD1]] (-0.45, fdr 1e-04), [[TSEN34]] (-0.44, fdr 6e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PPP1R1C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +7.0 | 1e-09 | 18/30 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.84×** | +6.8 | 4e-09 | 19/30 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.0 | 5e-07 | 2/8 (HOP62, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +5.2 | 3e-05 | 8/30 (A-427, HOP62, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 4e-04 | 10/29 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.5 | 0.047 | 5/20 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.071 | 10/30 (SW48, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.092 | 3/30 (A498, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.32× | +3.1 | 0.12 | 6/30 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.470×** | -8.4 | 2e-14 | 20/30 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.524×** | -7.2 | 2e-10 | 22/27 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.590×** | -5.9 | 8e-07 | 16/30 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.606×** | -5.6 | 3e-06 | 17/30 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -5.3 | 1e-05 | 15/23 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.661×** | -4.6 | 4e-04 | 10/30 (CHP-212, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -3.6 | 0.029 | 10/29 (SW480, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.9 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.155× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 8.95 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.05 µM 0.0707× (z -10.3) |
| [[A549 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0682× (z -11.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0726× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[NCI-H460 (line)]] | wt | 5.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0534× (z -18.7) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 4.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Artesunate (drug)]] 5 µM 0.257× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKG2-AS1]] | +0.56 | +0.52 / +0.65 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[C6orf141]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ARHGAP25]] | +0.53 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[C5orf63]] | +0.51 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PRKAA2]] | +0.51 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[ANKRD20A5P]] | +0.50 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[SLC6A17]] | +0.49 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[VSIG1]] | +0.49 | +0.38 / +0.39 | both halves | 6e-05 |  |
| [[LINC02223]] | +0.49 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[BCAN-AS2]] | +0.49 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LINC00460]] | +0.49 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[LINC02842]] | +0.47 | +0.51 / +0.27 | both halves | 3e-04 |  |
| [[YWHAEP7-1]] | +0.47 | +0.39 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB11]] | -0.48 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[GUCD1]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[TSEN34]] | -0.44 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[SLC25A1]] | -0.44 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[NPHP4]] | -0.43 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PPP1R16A]] | -0.43 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[PMS2P4-1]] | -0.42 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[RABL6]] | -0.42 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[KMT5C]] | -0.42 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[DNM2]] | -0.41 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[SIN3A]] | -0.41 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ALDH6A1]] | -0.41 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R1C]] | B | PPP1R1C activity raises PRKG2's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without PPP1R1C | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[KLRC3]] | B | KLRC3 activity raises PRKG2's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without KLRC3 | 0.042 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[BCAN-AS2]] | B | BCAN-AS2 activity raises PRKG2's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without BCAN-AS2 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.7, 38.6); signed map (6.6, 41.4). **Vector** length 53.5, 9.79% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +0.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -8.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.1 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.5 | -4.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | +0.7 |
|  | [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[Malotilate (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cGMP-dependent 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:81,087,370-81,215,222 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cGKII, PRKGR2, PKG2 |
| Gene groups (HGNC) | Protein kinase G family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 18 pathways, smallest: Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation; cGMP effects; Nitric oxide stimulates guanylate cyclase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13237](https://www.uniprot.org/uniprotkb/Q13237) (cGMP-dependent protein kinase 2):

> Crucial regulator of intestinal secretion and bone growth. Phosphorylates and activates CFTR on the plasma membrane. Plays a key role in intestinal secretion by regulating cGMP-dependent translocation of CFTR in jejunum. Acts downstream of NMDAR to activate the plasma membrane accumulation of GRIA1/GLUR1 in synapse and increase synaptic plasticity. Phosphorylates GRIA1/GLUR1 at Ser-863 (By similarity). Acts as a regulator of gene expression and activator of the extracellular signal-regulated …

**Summary**, from NCBI Gene [5593](https://www.ncbi.nlm.nih.gov/gene/5593):

> This gene encodes a protein that belongs to the serine/threonine protein kinase family of proteins. The encoded protein binds to and inhibits the activation of several receptor tyrosine kinases. The membrane-bound protein is a regulator of intestinal secretion, bone growth and renin secretion. Alternate splicing results in multiple transcript variants encoding distinct isoforms whose regulatory N-termini differ in length but whose C-terminal catalytic domains are identical. [provided by RefSeq, …

**Accessions** — [HGNC:9416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9416) · Entrez [5593](https://www.ncbi.nlm.nih.gov/gene/5593) · UniProt [Q13237](https://www.uniprot.org/uniprotkb/Q13237) · Ensembl [ENSG00000138669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138669)

## Data

Gene col 6209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6209); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6209]; `tensor/DDL_lfc|DDL_z.npy` [6209]; `embed/gene_vectors.npy` [6209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6209 or target_col == 6209). Every well: [[PRKG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
