---
symbol: "LGALS1"
type: "gene"
col: 1864
ensembl_id: "ENSG00000100097"
name: "galectin 1"
location: "22q13.1"
module: 192
arm: "+"
pooled_cpm: 133.44
n_lines_expressing: 38
n_dd_up: 1
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# LGALS1

*galectin 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +4.7, q 0.001, up in 34 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.521× (z -4.1, q 0.017, down in 32 of 36 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.634× (z -4.0, q 0.017, down in 25 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.262×, MIA PaCa-2 0.302×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.104×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VIM]] (+0.72, fdr 7e-06), [[CDKN2D]] (+0.71, fdr 7e-06), [[CDK2AP2]] (+0.66, fdr 1e-05); moves opposite to [[SPTBN2]] (-0.64, fdr 1e-05), [[FUBP1]] (-0.62, fdr 2e-05), [[ZNF300]] (-0.62, fdr 4e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC03047]] → it (grade B ⚠); 10 go from it, the strongest it → [[PLIN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.57×** | +4.7 | 0.001 | 34/37 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | 1.80× | +3.5 | 0.11 | 26/32 (A-427, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~87% of this change | 1.63× | +3.1 | 0.42 | 28/36 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1864.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.262×, MIA PaCa-2 0.302×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.104×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.521×** | -4.1 | 0.017 | 32/36 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -4.0 | 0.017 | 25/36 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.553×** | -3.7 | 0.043 | 23/36 (AN3 CA, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.573× | -3.3 | 0.15 | 23/36 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.702× | -3.1 | 0.19 | 21/36 (HOP62, SW 1271, …) | top dose only | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | 0.609× | -3.1 | 0.19 | 31/36 (NCI-H460, J82, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.396× | -3.0 | 0.20 | 32/37 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.99 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 73.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 263 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.6) |
| [[A-172 (line)]] | wt | 264 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.73 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 231 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 183 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 507 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 393 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 141 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 503 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIM]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 879 |
| [[CDKN2D]] | +0.71 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CDK2AP2]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ARL3]] | +0.65 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.64 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[RRAS]] | +0.64 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[A1BG]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MINDY2]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN2]] | -0.64 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[FUBP1]] | -0.62 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[ZNF300]] | -0.62 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ABCF2]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.60 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MTA1]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[PRRC2B]] | -0.59 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[DUS3L]] | -0.59 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[MRM1]] | -0.59 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[GNL3L]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.58 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[NADK]] | -0.58 | -0.48 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03047]] | B | LINC03047 activity raises LGALS1's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 3.13× lower at baseline in the lines without LINC03047 | 0.079 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |
| [[IFI27L2]] | B | IFI27L2 activity raises LGALS1's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 4.17× lower at baseline in the lines without IFI27L2 | 0.087 | ⚠ within organs, on part of the lines |
| [[VIM]] | C | VIM activity raises LGALS1's level | lines that do not express VIM (18) vs lines expressing it (32) | 5.81× lower at baseline in the lines without VIM | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LOXL2, ADAMTS18, MAP1B; co-absent with the target |
| [[MYADM]] | C | MYADM activity raises LGALS1's level | lines that do not express MYADM (3) vs lines expressing it (47) | 7.02× lower at baseline in the lines without MYADM | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN3]] | B | LGALS1 activity raises PLIN3's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 2.12× lower at baseline in the lines without LGALS1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[FSCN1]] | B | LGALS1 activity raises FSCN1's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 3.78× lower at baseline in the lines without LGALS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[IKBIP]] | B | LGALS1 activity raises IKBIP's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 2.69× lower at baseline in the lines without LGALS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[TUBA1A]] | B | LGALS1 activity raises TUBA1A's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 3.58× lower at baseline in the lines without LGALS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[MYADM]] | B | LGALS1 activity raises MYADM's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 2.42× lower at baseline in the lines without LGALS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[ILK]] | B | LGALS1 activity raises ILK's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 1.25× lower at baseline in the lines without LGALS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[FBXO33]] | B | LGALS1 activity lowers FBXO33's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 1.26× higher at baseline in the lines without LGALS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[GSKIP]] | B | LGALS1 activity lowers GSKIP's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 1.54× higher at baseline in the lines without LGALS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[VKORC1]] | B | LGALS1 activity raises VKORC1's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without LGALS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[VIM]] | C | LGALS1 activity raises VIM's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 12.49× lower at baseline in the lines without LGALS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM; co-absent with the target |

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.6, -29.3); signed map (-28.4, 15.7). **Vector** length 79.7, 34.2% of its response variance represented; |z| ≥ 3 in 418 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +0.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.5 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.1 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | galectin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,675,636-37,679,802 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GBP |
| Gene groups (HGNC) | Receptor ligands; Galectins |
| Hallmark sets | FATTY_ACID_METABOLISM, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P09382](https://www.uniprot.org/uniprotkb/P09382) (Galectin-1):

> Lectin that binds beta-galactoside and a wide array of complex carbohydrates. Plays a role in regulating apoptosis, cell proliferation and cell differentiation. Inhibits CD45 protein phosphatase activity and therefore the dephosphorylation of Lyn kinase. Strong inducer of T-cell apoptosis. Plays a negative role in Th17 cell differentiation via activation of the receptor CD69.

**Summary**, from NCBI Gene [3956](https://www.ncbi.nlm.nih.gov/gene/3956):

> The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. This gene product may act as an autocrine negative growth factor that regulates cell proliferation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6561) · Entrez [3956](https://www.ncbi.nlm.nih.gov/gene/3956) · UniProt [P09382](https://www.uniprot.org/uniprotkb/P09382) · Ensembl [ENSG00000100097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100097)

## Data

Gene col 1864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1864); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1864]; `tensor/DDL_lfc|DDL_z.npy` [1864]; `embed/gene_vectors.npy` [1864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1864 or target_col == 1864). Every well: [[LGALS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGALS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
