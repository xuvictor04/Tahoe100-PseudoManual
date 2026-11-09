---
symbol: "TRIM41"
type: "gene"
col: 7057
ensembl_id: "ENSG00000146063"
name: "tripartite motif containing 41"
location: "5q35.3"
module: 138
arm: "+"
pooled_cpm: 22.48
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# TRIM41

*tripartite motif containing 41* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.31× (z +3.8, q 0.078, up in 16 of 44 measured lines) ⚠ transcription drop.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.754× (z -4.0, q 0.034, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.167×, AsPC-1 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.176×); [[Flutamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0780×); [[Ataluren (drug)]] 0.5 µM in 1 line (SW48 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF558]] (+0.63, fdr 1e-05), [[CACTIN]] (+0.59, fdr 1e-05), [[ZNF865]] (+0.59, fdr 1e-05); moves opposite to [[MAP4K5]] (-0.47, fdr 9e-05), [[KIF13A]] (-0.47, fdr 1e-04), [[PTPN13]] (-0.43, fdr 5e-05).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.8 | 0.078 | 16/44 (A498, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.4 | 0.17 | 1/48 (COLO 205) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.167×, AsPC-1 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.176×); [[Flutamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0780×); [[Ataluren (drug)]] 0.5 µM in 1 line (SW48 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.754×** | -4.0 | 0.034 | 16/48 (A-427, RKO, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -3.7 | 0.055 | 19/47 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.789× | -3.2 | 0.20 | 17/47 (A-427, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 0.793× | -3.2 | 0.20 | 16/45 (LOX-IMVI, NCI-H1573, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.803× | -3.1 | 0.20 | 11/48 (HepG2/C3A, AN3 CA, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.806× | -3.1 | 0.20 | 9/47 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 44.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0780× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.139× (z -8.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 17.3 | 0 | 1 | — | [[Ataluren (drug)]] 0.5 µM 0.130× (z -9.3) |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF558]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[CACTIN]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF865]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CDK11A]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ARHGEF1]] | +0.57 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SLC25A44]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[KHNYN]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PNKP]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MBD1]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[UVSSA]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.53 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[ZNF384]] | +0.52 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP4K5]] | -0.47 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[KIF13A]] | -0.47 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PTPN13]] | -0.43 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.475). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.2, -26.5); signed map (0.8, 8.3). **Vector** length 81.9, 15.7% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.1 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Oxaliplatin (drug)]] 0.05 µM |  | +1.7 | +1.5 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.7 | +1.5 |
| fall | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.2 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.1 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.5 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | -2.5 | -3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:181,222,499-181,235,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC1127, RINCK |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV44](https://www.uniprot.org/uniprotkb/Q8WV44) (E3 ubiquitin-protein ligase TRIM41):

> E3 ligase that plays essential roles in innate antiviral response. Directly binds to influenza A virus or vesicular stomatitis virus nucleoproteins and targets them for ubiquitination and proteasomal degradation, thereby limiting viral infections. Activates the innate antiviral response by catalyzing monoubiquitination of CGAS, thereby activating CGAS. Also involved in innate antiviral response by mediating 'Lys-63'-linked polyubiquitylation of BCL10 which in turn hubs NEMO for activation of …

**Summary**, from NCBI Gene [90933](https://www.ncbi.nlm.nih.gov/gene/90933):

> This gene encodes a member of the tripartite motif (TRIM) family. The TRIM family is characterized by a signature motif composed of a RING finger, one or more B-box domains, and a coiled-coil region. This encoded protein may play a role in protein kinase C signaling. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:19013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19013) · Entrez [90933](https://www.ncbi.nlm.nih.gov/gene/90933) · UniProt [Q8WV44](https://www.uniprot.org/uniprotkb/Q8WV44) · Ensembl [ENSG00000146063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146063)

## Data

Gene col 7057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7057); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7057]; `tensor/DDL_lfc|DDL_z.npy` [7057]; `embed/gene_vectors.npy` [7057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7057 or target_col == 7057). Every well: [[TRIM41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
