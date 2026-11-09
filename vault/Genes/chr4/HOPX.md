---
symbol: "HOPX"
type: "gene"
col: 10118
ensembl_id: "ENSG00000171476"
name: "HOP homeobox"
location: "4q12"
module: 106
arm: "+"
pooled_cpm: 3.71
n_lines_expressing: 8
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# HOPX

*HOP homeobox* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.43× (z +10.6, q 2e-23, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.69× (z +6.6, q 7e-09, up in 0 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GALT1]] (+0.57, fdr 1e-05), [[DNAH5]] (+0.56, fdr 3e-05), [[SLC16A7]] (+0.55, fdr 2e-05); moves opposite to [[WNT7B]] (-0.50, fdr 4e-05), [[HBEGF]] (-0.50, fdr 3e-05), [[TM4SF19]] (-0.50, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NFIB]] → it (grade B ⚠); 3 go from it, the strongest it → [[TSC22D3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.43×** | +10.6 | 2e-23 | 4/4 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.68×** | +9.6 | 4e-19 | 2/2 (NCI-H2347, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.97×** | +7.8 | 1e-12 | 2/2 (NCI-H460, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +6.6 | 7e-09 | 0/4 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.15×** | +5.1 | 4e-05 | 2/5 (SNU-423, CFPAC-1) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +4.1 | 0.004 | 1/4 (SNU-423) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.37×** | +4.0 | 0.004 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +3.8 | 0.010 | 1/2 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.07×** | +3.8 | 0.010 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.8 | 0.010 | 1/3 (NCI-H2347) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.17×** | +3.6 | 0.015 | 0/4 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +3.4 | 0.028 | 0/3 | top dose only | cell-cycle shift (explains ~23% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.72×** | +3.4 | 0.034 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.10×** | +3.3 | 0.040 | 3/4 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.09×** | +3.3 | 0.040 | 3/4 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.58×** | +3.2 | 0.049 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.95×** | +3.1 | 0.056 | 3/4 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +2.9 | 0.095 | 2/5 (BT-474, CFPAC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.474× | -3.3 | 0.56 | 0/5 | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.639× | -3.0 | 0.68 | 0/5 | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.293 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT1]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[DNAH5]] | +0.56 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[SLC16A7]] | +0.55 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[AKR1C2]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[MAOA]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ADGRG2]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FGA]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SLC7A2]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[TGFB2]] | +0.54 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PDK4]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[NNMT]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[TBXT]] ⚠ | +0.51 | +0.42 / +0.49 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MAP2]] | +0.51 | +0.56 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT7B]] | -0.50 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[HBEGF]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TM4SF19]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CDCP1]] | -0.49 | -0.40 / -0.54 | both halves | 5e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[TMEM158]] | -0.49 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[CELSR1]] | -0.48 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[UPP1]] | -0.48 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TNFRSF11A]] | -0.48 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CALB2]] | -0.47 | -0.59 / -0.39 | both halves | 6e-05 | STRING 480 |
| [[ATP6V0D2]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[OTUB2]] | -0.47 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[KHDRBS3]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIB]] | B | NFIB activity lowers HOPX's level | lines that do not express NFIB (7) vs lines expressing it (43) | 1.55× higher at baseline in the lines without NFIB | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSC22D3]] | B | HOPX activity raises TSC22D3's level | lines that do not express HOPX (42) vs lines expressing it (8) | 2.50× lower at baseline in the lines without HOPX | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TBXT, GSG1L2 |
| [[TBXT]] | C | HOPX activity raises TBXT's level | lines that do not express HOPX (42) vs lines expressing it (8) | 3.22× lower at baseline in the lines without HOPX | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TBXT, GSG1L2; co-absent with the target |
| [[GSG1L2]] | C | HOPX activity raises GSG1L2's level | lines that do not express HOPX (42) vs lines expressing it (8) | 2.06× lower at baseline in the lines without HOPX | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TBXT, GSG1L2; co-absent with the target |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.8, 18.9); signed map (49.5, 26.7). **Vector** length 16.5, 5.77% of its response variance represented; |z| ≥ 3 in 124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +0.9 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +1.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.6 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.6 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.6 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.5 | -0.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.4 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.4 | -1.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | HOP homeobox |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,647,989-56,681,877 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAGY, HOP, OB1, NECC1, SMAP31 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPY8](https://www.uniprot.org/uniprotkb/Q9BPY8) (Homeodomain-only protein):

> Atypical homeodomain protein which does not bind DNA and is required to modulate cardiac growth and development. Acts via its interaction with SRF, thereby modulating the expression of SRF-dependent cardiac-specific genes and cardiac development. Prevents SRF-dependent transcription either by inhibiting SRF binding to DNA or by recruiting histone deacetylase (HDAC) proteins that prevent transcription by SRF. Overexpression causes cardiac hypertrophy (By similarity). May act as a tumor …

**Summary**, from NCBI Gene [84525](https://www.ncbi.nlm.nih.gov/gene/84525):

> The protein encoded by this gene is a homeodomain protein that lacks certain conserved residues required for DNA binding. It was reported that choriocarcinoma cell lines and tissues failed to express this gene, which suggested the possible involvement of this gene in malignant conversion of placental trophoblasts. Studies in mice suggest that this protein may interact with serum response factor (SRF) and modulate SRF-dependent cardiac-specific gene expression and cardiac development. Multiple …

**Accessions** — [HGNC:24961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24961) · Entrez [84525](https://www.ncbi.nlm.nih.gov/gene/84525) · UniProt [Q9BPY8](https://www.uniprot.org/uniprotkb/Q9BPY8) · Ensembl [ENSG00000171476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171476)

## Data

Gene col 10118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10118); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10118]; `tensor/DDL_lfc|DDL_z.npy` [10118]; `embed/gene_vectors.npy` [10118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10118 or target_col == 10118). Every well: [[HOPX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOPX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
