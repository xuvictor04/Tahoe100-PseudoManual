---
symbol: "LMO3"
type: "gene"
col: 536
ensembl_id: "ENSG00000048540"
name: "LIM domain only 3"
location: "12p12.3"
module: 162
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 14
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# LMO3

*LIM domain only 3* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.55× (z +10.8, q 1e-24, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.18× (z +9.1, q 1e-17, up in 1 of 3 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.413× (z -4.1, q 0.021, down in 0 of 9 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOPX]] (+0.47, fdr 3e-05), [[PGR]] (+0.47, fdr 4e-04), [[INHBB]] (+0.45, fdr 2e-04); moves opposite to [[PLEKHO2]] (-0.51, fdr 4e-05), [[CCNYL1]] (-0.50, fdr 4e-05), [[TRIOBP]] (-0.49, fdr 1e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[EPHB3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.55×** | +10.8 | 1e-24 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.80×** | +9.8 | 2e-20 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.18×** | +9.1 | 1e-17 | 1/3 (LS 180) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.10×** | +7.5 | 7e-12 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +4.7 | 3e-04 | 1/5 (BT-474) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.24×** | +4.5 | 7e-04 | 0/6 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +4.2 | 0.002 | 2/2 (SHP-77, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.89×** | +4.2 | 0.002 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.1 | 0.003 | 1/1 (NCI-H2347) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.06×** | +4.0 | 0.003 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.74×** | +3.9 | 0.006 | 1/1 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.95×** | +3.7 | 0.009 | 0/2 | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.4 | 0.026 | 0/2 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.32×** | +3.3 | 0.034 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +3.3 | 0.038 | 0/1 | top dose only | cell-cycle shift (explains ~11% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.77×** | +3.2 | 0.051 | 0/2 | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +3.2 | 0.051 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.051 | 1/2 (NCI-H2347) | inconsistent across doses | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.92×** | +3.0 | 0.078 | 0/2 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 536.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.413×** | -4.1 | 0.021 | 0/9 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.852 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.590 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.582 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.692 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.523 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.522 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.403 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOPX]] | +0.47 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PGR]] | +0.47 | +0.59 / +0.24 | both halves | 4e-04 |  |
| [[INHBB]] | +0.45 | +0.30 / +0.38 | both halves | 2e-04 |  |
| [[ADI1]] | +0.45 | +0.37 / +0.39 | both halves | 8e-05 |  |
| [[CTPS2]] | +0.45 | +0.32 / +0.31 | both halves | 2e-04 |  |
| [[SORBS2]] | +0.43 | +0.43 / +0.29 | both halves | 3e-04 |  |
| [[PRLR]] | +0.43 | +0.55 / +0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[PBX1]] | +0.42 | +0.33 / +0.34 | both halves | 1e-04 |  |
| [[MTUS1]] | +0.42 | +0.31 / +0.37 | both halves | 2e-04 |  |
| [[HAVCR1]] | +0.41 | +0.33 / +0.39 | both halves | 1e-04 |  |
| [[ARFGEF2]] | +0.41 | +0.26 / +0.45 | both halves | 4e-04 |  |
| [[PUM2]] | +0.41 | +0.31 / +0.36 | both halves | 2e-04 |  |
| [[FGL1]] | +0.40 | +0.28 / +0.39 | both halves | 3e-04 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHO2]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[CCNYL1]] | -0.50 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[TRIOBP]] | -0.49 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[LONRF3]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[TUBA1C]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SNAI1]] | -0.48 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[LUCAT1]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[PTAFR]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ZNF470]] | -0.47 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[HAP1]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[GOLT1A]] | -0.46 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[SPTSSB]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB3]] | B | LMO3 activity raises EPHB3's level | lines that do not express LMO3 (36) vs lines expressing it (14) | 1.87× lower at baseline in the lines without LMO3 | 0.027 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent |
| [[MTUS1]] | B | LMO3 activity raises MTUS1's level | lines that do not express LMO3 (36) vs lines expressing it (14) | 2.07× lower at baseline in the lines without LMO3 | 0.058 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent |
| [[PDGFA]] | B | LMO3 activity lowers PDGFA's level | lines that do not express LMO3 (36) vs lines expressing it (14) | 1.43× higher at baseline in the lines without LMO3 | 0.085 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent |
| cells under [[Furosemide (drug)]] 0.5 µM | B | LMO3 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express LMO3 (36) vs lines expressing it (12) | the lines without LMO3: 0.91× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent |
| [[S100A14]] | C | LMO3 activity raises S100A14's level | lines that do not express LMO3 (36) vs lines expressing it (14) | 2.38× lower at baseline in the lines without LMO3 | 0.050 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent; co-absent with the target |
| [[CD24]] | C | LMO3 activity raises CD24's level | lines that do not express LMO3 (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without LMO3 | 0.089 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction -0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, -5.5); signed map (51.9, 17.2). **Vector** length 11.3, 2.41% of its response variance represented; |z| ≥ 3 in 140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.0 | +9.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.9 | +10.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.5 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.4 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.4 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.4 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.4 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.3 | +0.6 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.4 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | +2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.3 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.3 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.3 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.2 | -0.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain only 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:16,548,372-16,610,594 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Rhom-3, DAT1; previously RBTNL2 |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

UniProt [Q8TAP4](https://www.uniprot.org/uniprotkb/Q8TAP4) carries no function annotation.

**Summary**, from NCBI Gene [55885](https://www.ncbi.nlm.nih.gov/gene/55885):

> The protein encoded by this gene belongs to the rhombotin family of cysteine-rich LIM domain oncogenes. This gene is predominantly expressed in the brain. Related family members, LMO1 and LMO2 on chromosome 11, have been reported to be involved in chromosomal translocations in T-cell leukemia. Many alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:6643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6643) · Entrez [55885](https://www.ncbi.nlm.nih.gov/gene/55885) · UniProt [Q8TAP4](https://www.uniprot.org/uniprotkb/Q8TAP4) · Ensembl [ENSG00000048540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048540)

## Data

Gene col 536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 536); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 536]; `tensor/DDL_lfc|DDL_z.npy` [536]; `embed/gene_vectors.npy` [536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 536 or target_col == 536). Every well: [[LMO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
