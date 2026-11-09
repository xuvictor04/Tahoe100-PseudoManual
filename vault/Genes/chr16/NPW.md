---
symbol: "NPW"
type: "gene"
col: 11477
ensembl_id: "ENSG00000183971"
name: "neuropeptide W"
location: "16p13.3"
module: 21
arm: "+"
pooled_cpm: 2.91
n_lines_expressing: 45
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# NPW

*neuropeptide W* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.39× (z +14.7, q 0e+00, up in 22 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pemigatinib (drug)]] 0.05 µM in 1 line (A498 0.0594×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETFBKMT]] (+0.63, fdr 1e-05), [[C1orf56]] (+0.58, fdr 4e-05), [[WASL-DT]] (+0.58, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +14.7 | 0e+00 | 22/26 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +10.0 | 4e-21 | 10/10 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.94×** | +8.5 | 3e-15 | 6/6 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +8.2 | 5e-14 | 3/4 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +7.1 | 1e-10 | 7/12 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.4 | 5e-06 | 10/27 (NCI-H23, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.002 | 6/38 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 1/40 (A498) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.004 | 8/39 (A498, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.56×** | +3.8 | 0.008 | 7/22 (SW480, SHP-77, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.016 | 6/35 (A-427, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11477.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pemigatinib (drug)]] 0.05 µM in 1 line (A498 0.0594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.675× | -3.4 | 0.42 | 8/38 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.681× | -3.1 | 0.53 | 10/31 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.42 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0594× (z -9.1) |
| [[A-172 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.922 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.950 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFBKMT]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[C1orf56]] | +0.58 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[WASL-DT]] | +0.58 | +0.40 / +0.63 | both halves | 4e-05 |  |
| [[SPATA1]] | +0.58 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[HRG-AS1]] | +0.58 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[C12orf40]] | +0.57 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[SLC27A6]] | +0.57 | +0.23 / +0.61 | both halves | 5e-04 |  |
| [[USH2A]] | +0.57 | +0.30 / +0.65 | both halves | 2e-04 |  |
| [[CHMP3-AS1]] | +0.56 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[A2ML1-AS1]] | +0.56 | +0.29 / +0.62 | both halves | 2e-04 |  |
| [[SPATA21]] | +0.56 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[SORCS3]] | +0.56 | +0.30 / +0.60 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 26.2); signed map (37.1, 3.5). **Vector** length 34.3, 3.54% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +3.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.4 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.0 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | neuropeptide W |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,009,926-2,020,755 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PPL8 |
| Gene groups (HGNC) | Neuropeptides |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N729](https://www.uniprot.org/uniprotkb/Q8N729) (Neuropeptide W):

> Plays a regulatory role in the organization of neuroendocrine signals accessing the anterior pituitary gland. Stimulates water drinking and food intake. May play a role in the hypothalamic response to stress (By similarity). NPW23 activates GPR7 and GPR8 more efficiently than NPW30.

**Summary**, from NCBI Gene [283869](https://www.ncbi.nlm.nih.gov/gene/283869):

> The product of this gene is processed into 23- and 30-amino acid neuropeptides that bind and activate two G-protein coupled receptors in the central nervous system. The neuropeptides have been shown to enhance cortisol secretion from adrenal cells through the adenylate cyclase/protein kinase A signaling cascade. The preproprotein is translated using a non-AUG initiation codon that is inferred from analyses of the mouse ortholog. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30509) · Entrez [283869](https://www.ncbi.nlm.nih.gov/gene/283869) · UniProt [Q8N729](https://www.uniprot.org/uniprotkb/Q8N729) · Ensembl [ENSG00000183971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183971)

## Data

Gene col 11477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11477); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11477]; `tensor/DDL_lfc|DDL_z.npy` [11477]; `embed/gene_vectors.npy` [11477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11477 or target_col == 11477). Every well: [[NPW — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPW.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
