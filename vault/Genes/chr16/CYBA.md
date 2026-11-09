---
symbol: "CYBA"
type: "gene"
col: 579
ensembl_id: "ENSG00000051523"
name: "cytochrome b-245 alpha chain"
location: "16q24.2"
module: 58
arm: "+"
pooled_cpm: 43.04
n_lines_expressing: 32
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CYBA

*cytochrome b-245 alpha chain* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.96× (z +8.2, q 1e-13, up in 26 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 5.43×, NCI-H460 4.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.399× (z -9.8, q 6e-20, down in 29 of 30 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC39A4]] (+0.74, fdr 7e-06), [[TSTD1]] (+0.65, fdr 1e-05), [[GCHFR]] (+0.63, fdr 2e-05); moves opposite to [[IDE]] (-0.58, fdr 1e-05), [[RNF6]] (-0.57, fdr 1e-04), [[SETD7]] (-0.55, fdr 4e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AQP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 579.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 5.43×, NCI-H460 4.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.96×** | +8.2 | 1e-13 | 26/27 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.17×** | +5.4 | 1e-05 | 23/26 (LoVo, HT-29, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.09×** | +5.4 | 1e-05 | 24/25 (LS 180, KATO III, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.62×** | +3.7 | 0.037 | 22/29 (NCI-H460, LS 180, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.58×** | +3.5 | 0.060 | 19/29 (J82, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.52× | +3.1 | 0.21 | 15/29 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.399×** | -9.8 | 6e-20 | 29/30 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.536×** | -4.7 | 7e-04 | 23/30 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.547×** | -4.6 | 0.001 | 25/30 (SW 900, HCT15, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.556×** | -3.8 | 0.023 | 23/30 (SW 900, COLO 205, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.403×** | -3.5 | 0.055 | 27/30 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -3.4 | 0.055 | 21/30 (A549, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.417×** | -3.4 | 0.064 | 17/29 (Hs 766T, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.669× | -3.0 | 0.16 | 20/30 (HT-29, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 69.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -16.5) |
| [[HCT15 (line)]] | alt | 78.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.5) |
| [[LoVo (line)]] | wt | 34.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -8.5) |
| [[SW480 (line)]] | alt | 33.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.2) |
| [[A498 (line)]] | wt | 136 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.9) |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.4) |
| [[KATO III (line)]] | alt | 81.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.2) |
| [[LS 180 (line)]] | wt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 42.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -8.8) |
| [[SW 900 (line)]] | alt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.2) |
| [[A-172 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.96 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 89.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 8 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A4]] | +0.74 | +0.73 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TSTD1]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GCHFR]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SLC35B2]] | +0.59 | +0.58 / +0.36 | both halves | 9e-05 |  |
| [[APRT]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 | STRING 532 |
| [[IGFBP2]] | +0.56 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[TNNI3]] | +0.55 | +0.48 / +0.36 | both halves | 9e-05 |  |
| [[C19orf33]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[UQCR11]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[FAAP20]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CST3]] | +0.55 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ENTPD2]] | +0.55 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDE]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[RNF6]] | -0.57 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[SETD7]] | -0.55 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[PSMD11]] | -0.51 | -0.52 / -0.37 | both halves | 9e-05 | pathway: Antigen processing-Cross presentation |
| [[MRPL9]] | -0.51 | -0.61 / -0.23 | both halves | 5e-04 |  |
| [[FECH]] | -0.51 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[CCT7]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[ZXDA]] | -0.50 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[PSME3IP1]] | -0.50 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[NADK2]] | -0.49 | -0.59 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[MTHFSD]] | -0.49 | -0.47 / -0.21 | both halves | 7e-04 |  |
| [[UBQLN1]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[FZD6]] | -0.49 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[SRP72]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | AQP3 activity raises CYBA's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 3.11× lower at baseline in the lines without AQP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises CYBA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.6, -17.3); signed map (-31.9, 6.4). **Vector** length 60.0, 20.8% of its response variance represented; |z| ≥ 3 in 386 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +4.3 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.0 | +1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.3 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b-245 alpha chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:88,643,275-88,651,083 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p22-PHOX, p22phox |
| Reactome | 26 pathways, smallest: Cross-presentation of particulate exogenous antigens (phagosomes); Killing mechanisms; WNT5:FZD7-mediated leishmania damping |
| Matched by | ensembl_id |

**Function**, from UniProt [P13498](https://www.uniprot.org/uniprotkb/P13498) (Cytochrome b-245 light chain):

> Subunit of NADPH oxidase complexes that is required for the NADPH oxidase activity that generates, in various cell types, superoxide from molecular oxygen utilizing NADPH as an electron donor. Subunit of the phagocyte NADPH oxidase complex that mediates the transfer of electrons from cytosolic NADPH to O2 to produce the superoxide anion (O2(-)). In the activated complex, electrons are first transferred from NADPH to flavin adenine dinucleotide (FAD) and subsequently transferred via two heme …

**Summary**, from NCBI Gene [1535](https://www.ncbi.nlm.nih.gov/gene/1535):

> Cytochrome b is comprised of a light chain (alpha) and a heavy chain (beta). This gene encodes the light, alpha subunit which has been proposed as a primary component of the microbicidal oxidase system of phagocytes. Mutations in this gene are associated with autosomal recessive chronic granulomatous disease (CGD), that is characterized by the failure of activated phagocytes to generate superoxide, which is important for the microbicidal activity of these cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2577) · Entrez [1535](https://www.ncbi.nlm.nih.gov/gene/1535) · UniProt [P13498](https://www.uniprot.org/uniprotkb/P13498) · Ensembl [ENSG00000051523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051523)

## Data

Gene col 579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 579); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 579]; `tensor/DDL_lfc|DDL_z.npy` [579]; `embed/gene_vectors.npy` [579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 579 or target_col == 579). Every well: [[CYBA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYBA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
