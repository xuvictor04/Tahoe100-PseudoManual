---
symbol: "MRPL22"
type: "gene"
col: 1351
ensembl_id: "ENSG00000082515"
name: "mitochondrial ribosomal protein L22"
location: "5q33.2"
module: 220
arm: "+"
pooled_cpm: 34.79
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# MRPL22

*mitochondrial ribosomal protein L22* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.41× (z +9.0, q 1e-16, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.807× (z -4.1, q 0.022, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (AN3 CA 0.113×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Resveratrol (drug)]] 0.05 µM in 1 line (H4 0.170×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFS4]] (+0.80, fdr 7e-06), [[CWC15]] (+0.71, fdr 7e-06), [[METTL14]] (+0.71, fdr 7e-06); moves opposite to [[GATAD2A]] (-0.59, fdr 1e-05), [[KPNA4]] (-0.58, fdr 6e-05), [[NPIPB5]] (-0.57, fdr 1e-05).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF224]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.41×** | +9.0 | 1e-16 | 44/48 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.64×** | +6.7 | 6e-09 | 33/47 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.57×** | +6.1 | 1e-07 | 33/48 (LoVo, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +6.1 | 1e-07 | 39/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +5.4 | 9e-06 | 31/48 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.9 | 7e-05 | 28/48 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 7e-05 | 28/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.40×** | +4.4 | 9e-04 | 25/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +4.3 | 1e-03 | 24/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.35×** | +4.1 | 0.003 | 26/47 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.82×** | +3.6 | 0.015 | 17/47 (HCT15, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.20×** | +3.5 | 0.020 | 23/48 (A549, SW48, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.026 | 21/48 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.094 | 11/47 (HCT15, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.0 | 0.094 | 17/47 (A498, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1351.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (AN3 CA 0.113×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Resveratrol (drug)]] 0.05 µM in 1 line (H4 0.170×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -4.1 | 0.022 | 24/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.841× | -3.3 | 0.23 | 14/48 (SW1417, NCI-H460, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 65.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 38.5 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +11.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[H4 (line)]] | wt | 28.7 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.170× (z -9.3) |
| [[SW480 (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +8.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFS4]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | STRING 450 |
| [[CWC15]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[METTL14]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[METTL17]] | +0.70 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[CDC40]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TNRC6A]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[MRPL21]] | +0.66 | +0.57 / +0.63 | both halves | 8e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 999 |
| [[UBA3]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RCHY1]] | +0.66 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[NDUFB4]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[NECAP1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[COPS5]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.59 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.58 | -0.38 / -0.66 | both halves | 6e-05 |  |
| [[NPIPB5]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SECISBP2]] | -0.55 | -0.42 / -0.62 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF224]] | C | ZNF224's natural level weakens MRPL22's drug response | ZNF224's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.10; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.871). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-23.1, -4.0); signed map (-22.6, -10.5). **Vector** length 82.2, 20.5% of its response variance represented; |z| ≥ 3 in 595 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.58 to 4); *Complex I biogenesis* (reactome, mean cos +0.62 to 3); *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.7 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +1.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.1 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +9.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | +0.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:154,941,073-154,969,411 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-L25, RPML25, HSPC158, uL22m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9NWU5](https://www.uniprot.org/uniprotkb/Q9NWU5) carries no function annotation.

**Summary**, from NCBI Gene [29093](https://www.ncbi.nlm.nih.gov/gene/29093):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14480) · Entrez [29093](https://www.ncbi.nlm.nih.gov/gene/29093) · UniProt [Q9NWU5](https://www.uniprot.org/uniprotkb/Q9NWU5) · Ensembl [ENSG00000082515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082515)

## Data

Gene col 1351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1351); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1351]; `tensor/DDL_lfc|DDL_z.npy` [1351]; `embed/gene_vectors.npy` [1351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1351 or target_col == 1351). Every well: [[MRPL22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
