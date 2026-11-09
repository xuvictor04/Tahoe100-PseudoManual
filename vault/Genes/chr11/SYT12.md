---
symbol: "SYT12"
type: "gene"
col: 10359
ensembl_id: "ENSG00000173227"
name: "synaptotagmin 12"
location: "11q13.2"
module: 61
arm: "+"
pooled_cpm: 2.78
n_lines_expressing: 41
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SYT12

*synaptotagmin 12* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.07× (z +12.4, q 3e-32, up in 5 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +9.7, q 8e-20, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.663× (z -3.6, q 0.084, down in 5 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A549 0.0279×; ⚠ cell-cycle shift, explains ~0% of this change); [[Talc (drug)]] 0.05 µM in 1 line (BT-474 0.0664×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0686×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA1E]] (+0.62, fdr 8e-06), [[S100A3]] (+0.61, fdr 1e-05), [[EBI3]] (+0.58, fdr 1e-05); moves opposite to [[VTI1B]] (-0.47, fdr 9e-05), [[HSDL1]] (-0.47, fdr 4e-05), [[ZNF449]] (-0.45, fdr 4e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[ABCC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.07×** | +12.4 | 3e-32 | 5/12 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +10.0 | 4e-21 | 3/4 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +9.7 | 8e-20 | 20/29 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +9.4 | 5e-19 | 19/26 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +8.5 | 2e-15 | 1/7 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +7.8 | 7e-13 | 15/26 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +7.1 | 8e-11 | 18/35 (SW480, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +6.2 | 5e-08 | 7/30 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 9/34 (NCI-H2347, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +5.5 | 2e-06 | 17/32 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.87×** | +5.5 | 2e-06 | 14/36 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +5.1 | 1e-05 | 11/30 (SHP-77, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.4 | 6e-04 | 2/13 (BT-474, HOP62) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.70×** | +4.2 | 9e-04 | 4/24 (SNU-1, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.58×** | +4.0 | 0.002 | 9/35 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.015 | 1/17 (SW480) | inconsistent across doses | low cells (technical?) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +3.0 | 0.074 | 3/32 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.39×** | +2.9 | 0.091 | 3/31 (NCI-H2347, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10359.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A549 0.0279×; ⚠ cell-cycle shift, explains ~0% of this change); [[Talc (drug)]] 0.05 µM in 1 line (BT-474 0.0664×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0686×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.663×** | -3.6 | 0.084 | 5/28 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.665×** | -3.6 | 0.084 | 8/37 (C-33 A, Hs 766T, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.684× | -3.4 | 0.14 | 9/36 (NCI-H460, HT-29, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.520× | -3.0 | 0.35 | 3/29 (BT-474, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.89 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0279× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 7.74 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0664× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 2.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 3.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +9.5) | — |
| [[J82 (line)]] | alt | 1.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 4.57 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0686× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 6.15 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.50× (z +8.7) | — |
| [[A-172 (line)]] | wt | 0.774 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.721 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.951 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.964 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.707 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.883 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.731 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.863 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA1E]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 | pathway: Neuronal System |
| [[S100A3]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[EBI3]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MMD]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ADGRE2]] | +0.55 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[ABCA6]] | +0.55 | +0.63 / +0.40 | both halves | 4e-05 | same gene group |
| [[HS3ST3B1]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[GASAL1]] | +0.53 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[AQP3]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[CTNNA3]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 | same gene group |
| [[RASGRF1]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 | pathway: Neuronal System |
| [[SKIL]] | +0.51 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VTI1B]] | -0.47 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[HSDL1]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZNF449]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC3]] | B | SYT12 activity raises ABCC3's level | lines that do not express SYT12 (9) vs lines expressing it (41) | 3.25× lower at baseline in the lines without SYT12 | 0.013 | ⚠ within organs, on part of the lines; also absent: EMSLR; maybe low, not absent |
| [[AQP3]] | B | SYT12 activity raises AQP3's level | lines that do not express SYT12 (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without SYT12 | 0.044 | ⚠ within organs, on part of the lines; also absent: EMSLR; maybe low, not absent |
| [[TMEFF2]] | B | SYT12 activity lowers TMEFF2's level | lines that do not express SYT12 (9) vs lines expressing it (41) | 1.34× higher at baseline in the lines without SYT12 | 0.050 | ⚠ within organs, on part of the lines; also absent: EMSLR; maybe low, not absent |
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | B | SYT12 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SYT12 (9) vs lines expressing it (39) | the lines without SYT12: 0.89× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: EMSLR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, 8.5); signed map (12.6, 27.7). **Vector** length 48.9, 7.25% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +6.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.9 | +2.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,006,778-67,050,863 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRG1 |
| Gene groups (HGNC) | Synaptotagmins; MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV01](https://www.uniprot.org/uniprotkb/Q8IV01) (Synaptotagmin-12):

> Synaptic vesicle phosphoprotein that enhances spontaneous neurotransmitter release but does not effect induced neurotransmitter release (By similarity). Unlike other synaptotagmins, it does not bind Ca(2+) or phospholipids (By similarity). Essential for mossy-fiber long-term potentiation in the hippocampus (By similarity).

**Summary**, from NCBI Gene [91683](https://www.ncbi.nlm.nih.gov/gene/91683):

> This gene is a member of the synaptotagmin gene family and encodes a protein similar to other family members that mediate calcium-dependent regulation of membrane trafficking in synaptic transmission. Studies of the orthologous gene in rat have shown that the encoded protein selectively modulates spontaneous synaptic-vesicle exocytosis and may also be involved in regulating calcium independent secretion in nonneuronal cells. Alternative splicing results in multiple transcript variants. The gene …

**Accessions** — [HGNC:18381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18381) · Entrez [91683](https://www.ncbi.nlm.nih.gov/gene/91683) · UniProt [Q8IV01](https://www.uniprot.org/uniprotkb/Q8IV01) · Ensembl [ENSG00000173227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173227)

## Data

Gene col 10359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10359); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10359]; `tensor/DDL_lfc|DDL_z.npy` [10359]; `embed/gene_vectors.npy` [10359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10359 or target_col == 10359). Every well: [[SYT12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
