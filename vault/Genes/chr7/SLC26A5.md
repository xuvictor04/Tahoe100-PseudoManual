---
symbol: "SLC26A5"
type: "gene"
col: 9982
ensembl_id: "ENSG00000170615"
name: "solute carrier family 26 member 5"
location: "7q22.1"
module: 21
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SLC26A5

*solute carrier family 26 member 5* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +12.2, q 2e-31, up in 28 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (J82 0.0757×); [[Canagliflozin (drug)]] 0.5 µM in 1 line (BT-474 0.0550×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM217A]] (+0.78, fdr 7e-06), [[PWRN1]] (+0.75, fdr 2e-05), [[RN7SL1]] (+0.75, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ENTREP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +12.2 | 2e-31 | 28/34 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +11.7 | 2e-29 | 3/5 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +11.0 | 8e-26 | 15/18 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +9.8 | 1e-20 | 27/44 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +8.8 | 2e-16 | 3/7 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.86×** | +6.0 | 2e-07 | 16/44 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.21×** | +5.9 | 3e-07 | 17/38 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.4 | 4e-06 | 17/42 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.64×** | +4.8 | 9e-05 | 14/46 (PANC-1, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +4.8 | 9e-05 | 3/16 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.8 | 9e-05 | 3/19 (Hs 766T, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.8 | 9e-05 | 9/35 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +4.4 | 5e-04 | 10/41 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.4 | 5e-04 | 9/32 (LS 180, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 5e-04 | 15/43 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +4.2 | 8e-04 | 6/32 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.006 | 8/35 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.020 | 8/32 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.024 | 3/38 (PANC-1, Hs 766T, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.058 | 10/43 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9982.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (J82 0.0757×); [[Canagliflozin (drug)]] 0.5 µM in 1 line (BT-474 0.0550×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.840× | -6.0 | 1e-06 | 26/48 (SHP-77, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 4.39 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.5 µM 0.0550× (z -8.5) |
| [[J82 (line)]] | alt | 2.53 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0757× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.67× (z +8.9) | — |
| [[SW480 (line)]] | alt | 5.11 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.71× (z +9.2) | — |
| [[A-172 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM217A]] | +0.78 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[PWRN1]] | +0.75 | +0.47 / +0.83 | both halves | 2e-05 |  |
| [[RN7SL1]] | +0.75 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.75 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.74 | +0.48 / +0.83 | both halves | 2e-05 |  |
| [[UBOX5-AS1]] | +0.73 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SFRP4]] | +0.73 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.72 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.72 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.72 | +0.65 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTREP1]] | B | ENTREP1 activity raises SLC26A5's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without ENTREP1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[HES2]] | B | HES2 activity raises SLC26A5's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.15× lower at baseline in the lines without HES2 | 0.061 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[REEP1]] | B | REEP1 activity raises SLC26A5's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.18× lower at baseline in the lines without REEP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, 30.3); signed map (34.9, 7.1). **Vector** length 47.0, 5.73% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +3.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 26 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:103,352,730-103,446,207 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DFNB61, PRESTIN; previously PRES |
| Gene groups (HGNC) | Solute carrier family 26 |
| Reactome | 3 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [P58743](https://www.uniprot.org/uniprotkb/P58743) (Prestin):

> Voltage-sensitive motor protein that drives outer hair cell (OHC) electromotility (eM) and participates in sound amplification in the hearing organ (By similarity). Converts changes in the transmembrane electric potential into mechanical displacements resulting in the coupling of its expansion to movement of a charged voltage sensor across the lipid membrane (By similarity). The nature of the voltage sensor is not completely clear, and two models compete. In the first model, acts as an …

**Summary**, from NCBI Gene [375611](https://www.ncbi.nlm.nih.gov/gene/375611):

> This gene encodes a member of the SLC26A/SulP transporter family. The protein functions as a molecular motor in motile outer hair cells (OHCs) of the cochlea, inducing changes in cell length that act to amplify sound levels. The transmembrane protein is an incomplete anion transporter, and does not allow anions to cross the cell membrane but instead undergoes a conformational change in response to changes in intracellular Cl- levels that results in a change in cell length. The protein functions …

**Accessions** — [HGNC:9359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9359) · Entrez [375611](https://www.ncbi.nlm.nih.gov/gene/375611) · UniProt [P58743](https://www.uniprot.org/uniprotkb/P58743) · Ensembl [ENSG00000170615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170615)

## Data

Gene col 9982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9982); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9982]; `tensor/DDL_lfc|DDL_z.npy` [9982]; `embed/gene_vectors.npy` [9982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9982 or target_col == 9982). Every well: [[SLC26A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC26A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
