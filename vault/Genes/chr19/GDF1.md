---
symbol: "GDF1"
type: "gene"
col: 5043
ensembl_id: "ENSG00000130283"
name: "growth differentiation factor 1"
location: "19p13.11"
module: 53
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# GDF1

*growth differentiation factor 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +11.5, q 9e-28, up in 22 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.610× (z -5.0, q 3e-04, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRX]] (+0.68, fdr 7e-06), [[CPT1C]] (+0.65, fdr 7e-06), [[TINCR]] (+0.65, fdr 9e-06); moves opposite to [[ARHGAP17]] (-0.49, fdr 2e-05), [[LANCL1]] (-0.48, fdr 1e-05), [[CD99L2]] (-0.48, fdr 1e-04).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GBX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +11.5 | 9e-28 | 22/37 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.01×** | +11.2 | 8e-27 | 30/41 (SW480, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +7.0 | 4e-10 | 22/46 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.5 | 9e-09 | 5/18 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.4 | 2e-08 | 13/33 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +5.8 | 5e-07 | 19/43 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.5 | 4e-06 | 3/7 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +4.7 | 2e-04 | 2/8 (HEC-1-A, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 0.001 | 7/37 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 12/43 (HCT15, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[EX229 (drug)]] 5 µM |  | **1.93×** | +3.5 | 0.025 | 3/29 (HOP62, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.033 | 5/31 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.81×** | +3.2 | 0.066 | 2/21 (PANC-1, HOP62) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.78×** | +3.1 | 0.080 | 3/30 (NCI-H2347, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.080 | 1/39 (NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.610×** | -5.0 | 3e-04 | 23/45 (PANC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.638×** | -4.4 | 0.003 | 17/41 (C-33 A, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -4.1 | 0.009 | 18/42 (SNU-423, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.708×** | -3.5 | 0.061 | 9/44 (SNU-423, SW 900, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.726× | -3.3 | 0.12 | 7/45 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | 0.807× | -3.1 | 0.18 | 6/45 (SK-MEL-2, AN3 CA, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 0.810× | -3.1 | 0.18 | 6/43 (HepG2/C3A, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0683× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.197× (z -10.0) |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.158× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 8.28 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.89 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.107× (z -8.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[NCI-H460 (line)]] | wt | 3.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 3.72 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0494× (z -9.1) |
| [[A-172 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRX]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[TINCR]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[LRRC23]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CSPG5]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[DOK3]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[KIF17]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DHDH]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP17]] | -0.49 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[LANCL1]] | -0.48 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[CD99L2]] | -0.48 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[IFNGR1]] | -0.47 | -0.54 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBX1]] | B | GBX1 activity raises GDF1's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.94× lower at baseline in the lines without GBX1 | 0.010 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[ISM2]] | B | ISM2 activity raises GDF1's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without ISM2 | 0.055 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[KCNQ2]] | B | KCNQ2 activity raises GDF1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without KCNQ2 | 0.079 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.3, -17.0); signed map (16.2, 13.9). **Vector** length 69.0, 10.7% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | growth differentiation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,868,545-18,896,158 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Transforming growth factor beta superfamily |
| Reactome | 1 pathways, smallest: Signaling by NODAL |
| Matched by | ensembl_id |

**Function**, from UniProt [P27539](https://www.uniprot.org/uniprotkb/P27539) (Embryonic growth/differentiation factor 1):

> May mediate cell differentiation events during embryonic development.

**Summary**, from NCBI Gene [2657](https://www.ncbi.nlm.nih.gov/gene/2657):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. Studies in rodents suggest that this protein is involved in the establishment of left-right asymmetry in early …

**Accessions** — [HGNC:4214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4214) · Entrez [2657](https://www.ncbi.nlm.nih.gov/gene/2657) · UniProt [P27539](https://www.uniprot.org/uniprotkb/P27539) · Ensembl [ENSG00000130283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130283)

## Data

Gene col 5043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5043); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5043]; `tensor/DDL_lfc|DDL_z.npy` [5043]; `embed/gene_vectors.npy` [5043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5043 or target_col == 5043). Every well: [[GDF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
