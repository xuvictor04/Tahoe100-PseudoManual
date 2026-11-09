---
symbol: "FBXO9"
type: "gene"
col: 3326
ensembl_id: "ENSG00000112146"
name: "F-box protein 9"
location: "6p12.1"
module: 198
arm: "+"
pooled_cpm: 47.45
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# FBXO9

*F-box protein 9* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.49× (z +6.9, q 3e-09, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.775× (z -6.3, q 2e-07, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCOR3]] (+0.68, fdr 7e-06), [[CLPX]] (+0.67, fdr 8e-06), [[ANKRD13C]] (+0.65, fdr 7e-06); moves opposite to [[RELT]] (-0.62, fdr 7e-06), [[MIR222HG]] (-0.58, fdr 1e-05), [[ERCC1]] (-0.58, fdr 1e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +6.9 | 3e-09 | 35/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.3 | 8e-08 | 28/48 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 5e-05 | 36/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.7 | 0.030 | 19/47 (A-427, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.25×** | +3.5 | 0.051 | 16/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.084 | 16/48 (BT-474, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.3 | 0.084 | 18/47 (A-172, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.084 | 9/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.089 | 16/47 (HCT15, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.13 | 19/42 (NCI-H23, SHP-77, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.775×** | -6.3 | 2e-07 | 23/48 (COLO 205, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.578×** | -5.0 | 2e-04 | 29/48 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.768×** | -4.6 | 8e-04 | 25/48 (SNU-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.824× | -3.4 | 0.11 | 19/48 (SW480, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 51.4 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.198× (z -14.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.189× (z -10.6) |
| [[COLO 205 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -20.1) |
| [[AN3 CA (line)]] | alt | 70.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -13.9) |
| [[HS-578T (line)]] | alt | 46.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -8.5) |
| [[J82 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 45.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 76.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -14.8) |
| [[SW 900 (line)]] | alt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.6) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CLPX]] | +0.67 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[ANKRD13C]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PAIP1]] | +0.65 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[XPA]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[KCTD3]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZNF224]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[RCHY1]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TNRC6A]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RNPC3]] | +0.59 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[SPATA5L1]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELT]] | -0.62 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[MIR222HG]] | -0.58 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ERCC1]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[CDC37]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[EGR3]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SPTBN5]] | -0.57 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[EHD4]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[PLEKHO2]] | -0.56 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ACTN1]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[C13orf46]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[FOSL1]] | -0.54 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[EGR1]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.5, 0.0); signed map (-23.2, -8.4). **Vector** length 96.3, 22.0% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.8 | +6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.3 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +2.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.8 | -3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:53,051,991-53,100,873 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX9, NY-REN-57 |
| Gene groups (HGNC) | F-boxes other |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK97](https://www.uniprot.org/uniprotkb/Q9UK97) (F-box only protein 9):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins and plays a role in several biological processes such as cell cycle, cell proliferation, or maintenance of chromosome stability. Ubiquitinates mTORC1-bound TTI1 and TELO2 when they are phosphorylated by CK2 following growth factor deprivation, leading to their degradation. In contrast, does not mediate …

**Summary**, from NCBI Gene [26268](https://www.ncbi.nlm.nih.gov/gene/26268):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13588) · Entrez [26268](https://www.ncbi.nlm.nih.gov/gene/26268) · UniProt [Q9UK97](https://www.uniprot.org/uniprotkb/Q9UK97) · Ensembl [ENSG00000112146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112146)

## Data

Gene col 3326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3326); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3326]; `tensor/DDL_lfc|DDL_z.npy` [3326]; `embed/gene_vectors.npy` [3326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3326 or target_col == 3326). Every well: [[FBXO9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
