---
symbol: "SMN2"
type: "gene"
col: 12991
ensembl_id: "ENSG00000205571"
name: "survival of motor neuron 2, centromeric"
location: "5q13.2"
module: 89
arm: "+"
pooled_cpm: 3.47
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# SMN2

*survival of motor neuron 2, centromeric* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +7.0, q 1e-09, up in 15 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.822× (z -8.4, q 2e-14, down in 28 of 42 measured lines) ⚠ position not correctable. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 0.641× (z -3.8, q 0.023, down in 7 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMN1]] (+0.84, fdr 7e-06), [[AARSD1]] (+0.62, fdr 1e-05), [[PARL]] (+0.60, fdr 1e-05); moves opposite to [[MICALL2]] (-0.47, fdr 1e-04), [[DIAPH1]] (-0.46, fdr 1e-04), [[ZMIZ1]] (-0.46, fdr 4e-04).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ZNF461]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +7.0 | 1e-09 | 15/30 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +6.5 | 3e-08 | 19/32 (PANC-1, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.56×** | +6.0 | 5e-07 | 7/28 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.36×** | +5.4 | 8e-06 | 2/6 (NCI-H460, A498) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +4.3 | 0.002 | 3/41 (A498, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.4 | 0.055 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 1.21× | +3.2 | 0.11 | 4/37 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Vandetanib (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.13 | 3/37 (SW48, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.28× | +3.0 | 0.16 | 3/40 (NCI-H2347, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.822×** | -8.4 | 2e-14 | 28/42 (RKO, SW480, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.641×** | -3.8 | 0.023 | 7/30 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.793×** | -3.8 | 0.023 | 14/40 (SK-MEL-2, J82, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.744×** | -3.6 | 0.050 | 10/32 (SK-MEL-2, PANC-1, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 0.767× | -3.2 | 0.15 | 3/40 (A549, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 0.773× | -3.1 | 0.17 | 10/36 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.762× | -3.0 | 0.19 | 7/24 (SW480, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 6.26 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0603× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 6.04 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.147× (z -9.2) |
| [[SW1417 (line)]] | alt | 3.93 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0771× (z -8.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMN1]] | +0.84 | +0.79 / +0.79 | both halves | 7e-06 | same gene group; STRING 980 |
| [[AARSD1]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PARL]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[METTL16]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TDG]] | +0.59 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PSMD5]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZNF573]] | +0.57 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ZNF133]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[DRG1]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[TVP23B]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PRPF3]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.55 | +0.56 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICALL2]] | -0.47 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[DIAPH1]] | -0.46 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ZMIZ1]] | -0.46 | -0.24 / -0.54 | both halves | 4e-04 |  |
| [[PKM]] | -0.45 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[GPR137C]] | -0.44 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[RAPGEF2]] | -0.44 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF461]] | B | SMN2 activity raises ZNF461's level | lines that do not express SMN2 (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without SMN2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ZFP30, ENSG00000289728; maybe low, not absent |

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.527). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.9, -7.4); signed map (-13.5, -13.3). **Vector** length 29.1, 2.34% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +1.6 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +6.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +0.9 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +0.9 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | +0.7 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +2.2 |
|  | [[Elimusertib hydrochloride (drug)]] 0.5 µM |  | +0.6 | +1.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +0.5 | +2.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.0 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -0.9 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | survival of motor neuron 2, centromeric |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:70,049,638-70,078,522 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCD541, SMNC, GEMIN1, TDRD16B |
| Gene groups (HGNC) | Tudor domain containing; SMN complex; Proteins encoded by multiple genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16637](https://www.uniprot.org/uniprotkb/Q16637) (Survival motor neuron protein):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [6607](https://www.ncbi.nlm.nih.gov/gene/6607):

> This gene is part of a 500 kb inverted duplication on chromosome 5q13. This duplicated region contains at least four genes and repetitive elements which make it prone to rearrangements and deletions. The repetitiveness and complexity of the sequence have also caused difficulty in determining the organization of this genomic region. The telomeric and centromeric copies of this gene are nearly identical and encode the same protein. While mutations in the telomeric copy are associated with spinal …

**Accessions** — [HGNC:11118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11118) · Entrez [6607](https://www.ncbi.nlm.nih.gov/gene/6607) · UniProt [Q16637](https://www.uniprot.org/uniprotkb/Q16637) · Ensembl [ENSG00000205571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205571)

## Data

Gene col 12991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12991); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12991]; `tensor/DDL_lfc|DDL_z.npy` [12991]; `embed/gene_vectors.npy` [12991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12991 or target_col == 12991). Every well: [[SMN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
