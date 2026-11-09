---
symbol: "ASTN2"
type: "gene"
col: 7253
ensembl_id: "ENSG00000148219"
name: "astrotactin 2"
location: "9q33.1"
module: 131
arm: "+"
pooled_cpm: 146.02
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# ASTN2

*astrotactin 2* — 9q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.53× (z +7.4, q 1e-10, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 4.53×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 4.37×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.493× (z -8.0, q 1e-12, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (SNU-1 0.190×, H4 0.266×, LOX-IMVI 0.303×, SW480 0.350×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS23]] (+0.81, fdr 7e-06), [[RPS11]] (+0.80, fdr 7e-06), [[RPS15]] (+0.79, fdr 7e-06, ⚠ RPS15 in the vector space only through flagged drug-doses), [[RPL15]] (+0.79, fdr 7e-06); moves opposite to [[NUP188]] (-0.58, fdr 1e-05), [[EIF4G1]] (-0.57, fdr 1e-05), [[NCBP1]] (-0.56, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7253.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 4.53×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 4.37×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +7.4 | 1e-10 | 47/49 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +4.1 | 0.011 | 36/44 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +4.0 | 0.011 | 37/45 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +4.0 | 0.011 | 38/48 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7253.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (SNU-1 0.190×, H4 0.266×, LOX-IMVI 0.303×, SW480 0.350×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.493×** | -8.0 | 1e-12 | 43/48 (SNU-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.671× | -3.2 | 0.43 | 37/48 (C-33 A, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 144 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +9.4) | — |
| [[A549 (line)]] | wt | 212 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.2) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -8.8) |
| [[CHP-212 (line)]] | wt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.3) |
| [[COLO 205 (line)]] | alt | 72.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +8.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 185 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.9) |
| [[HCT15 (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.8) |
| [[J82 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 200 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -12.4) |
| [[LS 180 (line)]] | wt | 178 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 193 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 205 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.0) |
| [[SNU-1 (line)]] | wt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.8) |
| [[SW480 (line)]] | alt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.4) |
| [[A-172 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 150 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 165 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 196 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS23]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[RPS11]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 | same gene group |
| [[RPS15]] ⚠ | +0.79 | +0.76 / +0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL15]] | +0.79 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[RPS13]] ⚠ | +0.78 | +0.73 / +0.79 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[RPL32]] | +0.76 | +0.74 / +0.78 | both halves | 7e-06 | same gene group |
| [[RPL36A]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[RPL28]] | +0.75 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[RPL8]] ⚠ | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[FAU]] | +0.75 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[RPS29]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[RPL7A]] | +0.73 | +0.71 / +0.76 | both halves | 7e-06 | same gene group |
| [[RPS10]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[RPL38]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[RPS21]] | +0.73 | +0.70 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.58 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 | same gene group |
| [[NCBP1]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[LMNB2]] | -0.55 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[DCLRE1A]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.6, -27.2); signed map (-62.3, -3.1). **Vector** length 92.5, 41.3% of its response variance represented; |z| ≥ 3 in 403 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.74 to 20); *Peptide chain elongation* (reactome, mean cos +0.75 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.75 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | -1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.5 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | astrotactin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.1 — chr9:116,423,112-117,415,070 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0634 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75129](https://www.uniprot.org/uniprotkb/O75129) (Astrotactin-2):

> Mediates recycling of the neuronal cell adhesion molecule ASTN1 to the anterior pole of the cell membrane in migrating neurons. Promotes ASTN1 internalization and intracellular transport of endocytosed ASTN1 (By similarity). Selectively binds inositol-4,5-bisphosphate, inositol-3,4,5-trisphosphate and inositol-1,3,4,5-tetrakisphosphate, suggesting it is recruited to membranes that contain lipids with a phosphoinositide headgroup.

**Summary**, from NCBI Gene [23245](https://www.ncbi.nlm.nih.gov/gene/23245):

> This gene encodes a protein that is expressed in the brain and may function in neuronal migration, based on functional studies of the related astrotactin 1 gene in human and mouse. A deletion at this locus has been associated with schizophrenia. Multiple transcript variants encoding different proteins have been found for this locus. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:17021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17021) · Entrez [23245](https://www.ncbi.nlm.nih.gov/gene/23245) · UniProt [O75129](https://www.uniprot.org/uniprotkb/O75129) · Ensembl [ENSG00000148219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148219)

## Data

Gene col 7253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7253); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7253]; `tensor/DDL_lfc|DDL_z.npy` [7253]; `embed/gene_vectors.npy` [7253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7253 or target_col == 7253). Every well: [[ASTN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASTN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
