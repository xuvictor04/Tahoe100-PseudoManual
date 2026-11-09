---
symbol: "RPS6KA1"
type: "gene"
col: 3940
ensembl_id: "ENSG00000117676"
name: "ribosomal protein S6 kinase A1"
location: "1p36.11"
module: 100
arm: "+"
pooled_cpm: 17.37
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# RPS6KA1

*ribosomal protein S6 kinase A1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.30× (z +14.3, q 1e-43, up in 42 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.169×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.339×; ⚠ cell-cycle shift, explains ~24% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (A549 0.107×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHDC1]] (+0.69, fdr 7e-06), [[ADGRB2]] (+0.66, fdr 1e-05), [[FOXO6]] (+0.61, fdr 3e-05); moves opposite to [[PLAC8L1]] (-0.57, fdr 5e-05), [[DPY19L1P2]] (-0.57, fdr 1e-05), [[DPH5-DT]] (-0.54, fdr 4e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[KIAA1522]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +14.3 | 1e-43 | 42/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.09×** | +12.6 | 4e-34 | 41/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +11.6 | 1e-28 | 39/45 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +9.0 | 3e-17 | 25/44 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +8.8 | 2e-16 | 33/44 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +8.6 | 6e-16 | 35/45 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +8.5 | 1e-15 | 29/46 (LS 180, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +7.0 | 1e-10 | 22/45 (A549, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +6.4 | 1e-08 | 24/44 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.3 | 2e-08 | 20/44 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +5.0 | 2e-05 | 19/46 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.9 | 6e-05 | 19/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 2e-04 | 17/44 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.2 | 0.001 | 18/40 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.003 | 14/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.012 | 14/44 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.089 | 8/42 (RKO, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3940.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.169×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.339×; ⚠ cell-cycle shift, explains ~24% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (A549 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.821× | -3.4 | 0.39 | 16/43 (A-427, BT-474, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.877× | -3.2 | 0.39 | 13/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 9.95 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +8.5) | [[XRK3F2 (drug)]] 0.5 µM 0.107× (z -8.6) |
| [[A-427 (line)]] | wt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -11.6) |
| [[A498 (line)]] | wt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[C32 (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +11.5) | — |
| [[A-172 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHDC1]] | +0.69 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ADGRB2]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 | same gene group |
| [[FOXO6]] | +0.61 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[MAST3]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SEMA6B]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SLC26A6]] | +0.59 | +0.52 / +0.51 | both halves | 1e-05 | same gene group |
| [[F11R]] | +0.59 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PEDS1]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MINK1]] | +0.57 | +0.49 / +0.43 | both halves | 3e-05 | pathway: Cellular Senescence |
| [[TCIRG1]] | +0.56 | +0.47 / +0.43 | both halves | 3e-05 | same gene group |
| [[TTYH3]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TSPAN33]] | +0.55 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAC8L1]] | -0.57 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[DPY19L1P2]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.54 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[MCPH1]] | -0.54 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HCG18]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[HCG17]] | -0.52 | -0.48 / -0.26 | both halves | 3e-04 |  |
| [[THADA]] | -0.52 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[VPS13B]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ENOX2]] | -0.51 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ALG8]] | -0.51 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[LANCL2]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[CKMT2-AS1]] | -0.51 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1522]] | B | KIAA1522 activity raises RPS6KA1's level | lines that do not express KIAA1522 (5) vs lines expressing it (45) | 2.56× lower at baseline in the lines without KIAA1522 | 0.003 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4 |
| [[CCDC120]] | B | CCDC120 activity raises RPS6KA1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without CCDC120 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[F11R]] | B | F11R activity raises RPS6KA1's level | lines that do not express F11R (10) vs lines expressing it (40) | 1.65× lower at baseline in the lines without F11R | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[LLGL2]] | B | LLGL2 activity raises RPS6KA1's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without LLGL2 | 0.025 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[MAP3K9]] | B | MAP3K9 activity raises RPS6KA1's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without MAP3K9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[CDC42BPG]] | B | CDC42BPG activity raises RPS6KA1's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without CDC42BPG | 0.063 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[KIAA1671]] | C | KIAA1671 activity raises RPS6KA1's level | lines that do not express KIAA1671 (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without KIAA1671 | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: SOX13, FZD5, PDCD6P1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.1, -4.2); signed map (-26.2, 20.9). **Vector** length 73.4, 13.0% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +6.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +8.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.6 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,529,761-26,575,030 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RSK1, HU-1, p90Rsk, MAPKAPK1 |
| Gene groups (HGNC) | MAPK activated protein kinases; MicroRNA protein coding host genes; Ribosomal protein S6 kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 49 pathways, smallest: CREB phosphorylation; RSK activation; Gastrin-CREB signalling pathway via PKC and MAPK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15418](https://www.uniprot.org/uniprotkb/Q15418) (Ribosomal protein S6 kinase alpha-1):

> Serine/threonine-protein kinase that acts downstream of ERK (MAPK1/ERK2 and MAPK3/ERK1) signaling and mediates mitogenic and stress-induced activation of the transcription factors CREB1, ETV1/ER81 and NR4A1/NUR77, regulates translation through RPS6 and EIF4B phosphorylation, and mediates cellular proliferation, survival, and differentiation by modulating mTOR signaling and repressing pro-apoptotic function of BAD and DAPK1. In fibroblast, is required for EGF-stimulated phosphorylation of CREB1, …

**Summary**, from NCBI Gene [6195](https://www.ncbi.nlm.nih.gov/gene/6195):

> This gene encodes a member of the RSK (ribosomal S6 kinase) family of serine/threonine kinases. This kinase contains 2 nonidentical kinase catalytic domains and phosphorylates various substrates, including members of the mitogen-activated kinase (MAPK) signalling pathway. The activity of this protein has been implicated in controlling cell growth and differentiation. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10430) · Entrez [6195](https://www.ncbi.nlm.nih.gov/gene/6195) · UniProt [Q15418](https://www.uniprot.org/uniprotkb/Q15418) · Ensembl [ENSG00000117676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117676)

## Data

Gene col 3940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3940); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3940]; `tensor/DDL_lfc|DDL_z.npy` [3940]; `embed/gene_vectors.npy` [3940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3940 or target_col == 3940). Every well: [[RPS6KA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
