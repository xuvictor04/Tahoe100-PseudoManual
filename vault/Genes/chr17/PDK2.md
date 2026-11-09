---
symbol: "PDK2"
type: "gene"
col: 90
ensembl_id: "ENSG00000005882"
name: "pyruvate dehydrogenase kinase 2"
location: "17q21.33"
module: 127
arm: "+"
pooled_cpm: 4.95
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# PDK2

*pyruvate dehydrogenase kinase 2* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.56× (z +8.8, q 6e-16, up in 8 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.76× (z +5.5, q 4e-06, up in 20 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.415× (z -8.6, q 4e-15, down in 29 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.433× (z -8.2, q 7e-14, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MADD]] (+0.53, fdr 4e-05), [[BCAM]] (+0.52, fdr 3e-05), [[ZDHHC11B]] (+0.51, fdr 5e-05); moves opposite to [[ZBTB8OS]] (-0.50, fdr 5e-05), [[CCZ1P1]] (-0.46, fdr 8e-05), [[C9orf85]] (-0.45, fdr 2e-04).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARHGDIB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 90.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +8.8 | 6e-16 | 8/12 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +7.1 | 3e-10 | 15/46 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.6 | 6e-09 | 11/20 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +6.6 | 6e-09 | 7/14 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +5.5 | 4e-06 | 20/42 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.63×** | +4.7 | 2e-04 | 14/46 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.002 | 16/45 (RKO, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.006 | 12/44 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.011 | 8/44 (KATO III, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.6 | 0.021 | 8/26 (SW1417, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.036 | 10/44 (CFPAC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.092 | 8/44 (SW480, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 90.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.415×** | -8.6 | 4e-15 | 29/44 (A-427, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.433×** | -8.2 | 7e-14 | 24/44 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.495×** | -6.9 | 1e-09 | 24/43 (A498, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.516×** | -6.5 | 1e-08 | 20/44 (hTERT-HPNE, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -5.8 | 6e-07 | 23/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.571×** | -5.5 | 4e-06 | 18/45 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -5.5 | 4e-06 | 22/36 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -5.1 | 3e-05 | 17/42 (LS 180, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.467×** | -3.9 | 0.006 | 11/25 (LS 180, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.477×** | -3.8 | 0.008 | 11/34 (SW1417, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.767×** | -3.7 | 0.012 | 9/44 (H4, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.772×** | -3.5 | 0.019 | 7/46 (A-427, SW48, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.605×** | -3.5 | 0.019 | 10/46 (A-427, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.701×** | -3.5 | 0.019 | 11/43 (NCI-H23, COLO 205, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -3.5 | 0.019 | 10/43 (NCI-H1792, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.523×** | -3.3 | 0.030 | 11/39 (HS-578T, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.622×** | -3.3 | 0.030 | 10/43 (SNU-1, KATO III, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.718×** | -3.3 | 0.035 | 16/41 (NCI-H1573, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 90. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 8.66 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 5.63 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0700× (z -8.5) |
| [[J82 (line)]] | alt | 7.96 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 7.36 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0890× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 90), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MADD]] | +0.53 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[BCAM]] | +0.52 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[ZDHHC11B]] | +0.51 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[BAG6]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[BAIAP2-DT]] | +0.50 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[SLC9A3R1]] | +0.50 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[BACE1-AS]] | +0.50 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[PRR36]] | +0.48 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[LRCH4]] | +0.48 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[C1QTNF3]] | +0.48 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[ARHGDIB]] | +0.47 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[SSH3]] | +0.47 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB8OS]] | -0.50 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[CCZ1P1]] | -0.46 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[C9orf85]] | -0.45 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[TMEM267]] | -0.45 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[DHX32]] | -0.45 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ZNF431]] | -0.45 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[TM2D1]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[PGLS-DT]] | -0.43 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[PCOLCE2]] | -0.43 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[NDUFA6]] | -0.42 | -0.27 / -0.30 | both halves | 3e-04 | pathway: Aerobic respiration and respiratory electron transport |
| [[PAAF1]] | -0.42 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[MTG2]] | -0.42 | -0.21 / -0.35 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGDIB]] | B | ARHGDIB activity raises PDK2's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without ARHGDIB | 0.004 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[CDC42BPG]] | B | CDC42BPG activity raises PDK2's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.43× lower at baseline in the lines without CDC42BPG | 0.040 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[LINC02813]] | B | LINC02813 activity raises PDK2's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.22× lower at baseline in the lines without LINC02813 | 0.043 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.445). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, -6.9); signed map (-6.7, 21.4). **Vector** length 54.7, 7.50% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +6.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.2 | +0.7 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +1.0 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -8.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,094,737-50,112,152 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDHK2 |
| Gene groups (HGNC) | Pyruvate dehydrogenase kinase family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 6 pathways, smallest: Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism; Signaling by Retinoic Acid |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15119](https://www.uniprot.org/uniprotkb/Q15119) ([Pyruvate dehydrogenase (acetyl-transferring)] kinase isozyme 2, mitochondrial):

> Kinase that plays a key role in the regulation of glucose and fatty acid metabolism and homeostasis via phosphorylation of the pyruvate dehydrogenase subunits PDHA1 and PDHA2. This inhibits pyruvate dehydrogenase activity, and thereby regulates metabolite flux through the tricarboxylic acid cycle, down-regulates aerobic respiration and inhibits the formation of acetyl-coenzyme A from pyruvate. Inhibition of pyruvate dehydrogenase decreases glucose utilization and increases fat metabolism. …

**Summary**, from NCBI Gene [5164](https://www.ncbi.nlm.nih.gov/gene/5164):

> This gene encodes a member of the pyruvate dehydrogenase kinase family. The encoded protein phosphorylates pyruvate dehydrogenase, down-regulating the activity of the mitochondrial pyruvate dehydrogenase complex. Overexpression of this gene may play a role in both cancer and diabetes. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:8810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8810) · Entrez [5164](https://www.ncbi.nlm.nih.gov/gene/5164) · UniProt [Q15119](https://www.uniprot.org/uniprotkb/Q15119) · Ensembl [ENSG00000005882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005882)

## Data

Gene col 90: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 90); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 90, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 90]; `tensor/DDL_lfc|DDL_z.npy` [90]; `embed/gene_vectors.npy` [90]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 90 or target_col == 90). Every well: [[PDK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
