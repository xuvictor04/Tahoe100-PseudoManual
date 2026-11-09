---
symbol: "SMN1"
type: "gene"
col: 10207
ensembl_id: "ENSG00000172062"
name: "survival of motor neuron 1, telomeric"
location: "5q13.2"
module: 49
arm: "+"
pooled_cpm: 4.48
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SMN1

*survival of motor neuron 1, telomeric* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +9.5, q 1e-18, up in 23 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0701×; ⚠ cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (A-172 0.0617×); [[Berberine (chloride hydrate) (drug)]] 0.05 µM in 1 line (C32 0.0622×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMN2]] (+0.84, fdr 7e-06), [[PRPF3]] (+0.65, fdr 1e-05), [[TVP23B]] (+0.62, fdr 1e-05); moves opposite to [[DDX5]] (-0.55, fdr 2e-05), [[NECTIN3]] (-0.47, fdr 1e-04), [[KLF12]] (-0.46, fdr 1e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +9.5 | 1e-18 | 23/39 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.58×** | +8.9 | 2e-16 | 35/42 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.64×** | +7.6 | 8e-12 | 24/38 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.2 | 3e-05 | 13/38 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +5.0 | 8e-05 | 16/47 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +4.4 | 9e-04 | 16/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.003 | 10/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +4.1 | 0.003 | 10/43 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.7 | 0.014 | 4/12 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.2 | 0.088 | 5/46 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.46× | +3.0 | 0.12 | 3/45 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10207.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0701×; ⚠ cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (A-172 0.0617×); [[Berberine (chloride hydrate) (drug)]] 0.05 µM in 1 line (C32 0.0622×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -4.3 | 0.008 | 19/48 (C-33 A, LoVo, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.680× | -3.1 | 0.37 | 10/43 (RKO, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.760× | -3.0 | 0.37 | 6/47 (NCI-H2030, SW 1271, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.825× | -3.0 | 0.37 | 5/47 (SW48, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.34 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0617× (z -9.3) |
| [[C32 (line)]] | wt | 3.91 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.05 µM 0.0622× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 4.74 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0701× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMN2]] | +0.84 | +0.79 / +0.79 | both halves | 7e-06 | same gene group; STRING 980 |
| [[PRPF3]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TVP23B]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[AARSD1]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PARL]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[RAD17]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PMS2CL]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[DRG1]] | +0.59 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[CLASRP]] | +0.57 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ZNF565]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[NPRL3]] | +0.56 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[TAMM41]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection; STRING 478 |
| [[NECTIN3]] | -0.47 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[KLF12]] | -0.46 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.459). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.5, -8.0); signed map (-34.7, -24.1). **Vector** length 36.3, 3.15% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +2.1 | +8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.2 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.2 | +2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +0.5 |
|  | [[Elimusertib hydrochloride (drug)]] 0.5 µM |  | +0.7 | +1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +0.7 | +2.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.6 | +1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | survival of motor neuron 1, telomeric |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:70,925,030-70,953,942 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCD541, SMNT, SMA1, SMA2, SMA3, GEMIN1, TDRD16A; previously SMA@, SMA |
| Gene groups (HGNC) | Tudor domain containing; SMN complex; Proteins encoded by multiple genes |
| Reactome | 8 pathways, smallest: SARS-CoV-2 modulates host translation machinery; Metabolism of non-coding RNA; snRNP Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16637](https://www.uniprot.org/uniprotkb/Q16637) (Survival motor neuron protein):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [6606](https://www.ncbi.nlm.nih.gov/gene/6606):

> This gene is part of a 500 kb inverted duplication on chromosome 5q13. This duplicated region contains at least four genes and repetitive elements which make it prone to rearrangements and deletions. The repetitiveness and complexity of the sequence have also caused difficulty in determining the organization of this genomic region. The telomeric and centromeric copies of this gene are nearly identical and encode the same protein. However, mutations in this gene, the telomeric copy, are …

**Accessions** — [HGNC:11117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11117) · Entrez [6606](https://www.ncbi.nlm.nih.gov/gene/6606) · UniProt [Q16637](https://www.uniprot.org/uniprotkb/Q16637) · Ensembl [ENSG00000172062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172062)

## Data

Gene col 10207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10207); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10207]; `tensor/DDL_lfc|DDL_z.npy` [10207]; `embed/gene_vectors.npy` [10207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10207 or target_col == 10207). Every well: [[SMN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
