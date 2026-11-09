---
symbol: "GET4"
type: "gene"
col: 14214
ensembl_id: "ENSG00000239857"
name: "guided entry of tail-anchored proteins factor 4"
location: "7p22.3"
module: 157
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# GET4

*guided entry of tail-anchored proteins factor 4* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +9.0, q 9e-17, up in 24 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.816× (z -6.0, q 1e-06, down in 23 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (HT-29 0.0761×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMRP]] (+0.66, fdr 7e-06), [[AKT2]] (+0.65, fdr 3e-05), [[CRTC2]] (+0.62, fdr 1e-05); moves opposite to [[DNM1L]] (-0.46, fdr 4e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +9.0 | 9e-17 | 24/33 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +7.1 | 2e-10 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +5.6 | 4e-06 | 16/32 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +5.5 | 4e-06 | 12/28 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +5.5 | 5e-06 | 18/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +5.4 | 8e-06 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +5.0 | 5e-05 | 13/42 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.6 | 3e-04 | 5/18 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +4.4 | 6e-04 | 8/45 (PANC-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~19% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.2 | 0.002 | 4/15 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.018 | 3/47 (SHP-77, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.051 | 2/26 (NCI-H1792, LS 180) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.051 | 11/42 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.44×** | +3.1 | 0.083 | 3/43 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14214.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (HT-29 0.0761×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.816×** | -6.0 | 1e-06 | 23/48 (Hs 766T, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.90 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 4.31 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0761× (z -9.1) |
| [[A-172 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMRP]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[AKT2]] | +0.65 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[CRTC2]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LENG8]] | +0.61 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[RHOT2]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[AGRN]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[WDR6]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[EDC4]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CDK5RAP3]] | +0.58 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[MIB2]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TEPSIN]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CFAP410]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNM1L]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.8, -24.2); signed map (0.3, 4.8). **Vector** length 40.7, 4.15% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.4 | +3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +0.7 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | guided entry of tail-anchored proteins factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:876,554-896,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-20, H_NH1244M04.5, CEE, TRC35; previously C7orf20 |
| Gene groups (HGNC) | BAG6 complex; GET4-GET5 transmembrane domain recognition complex subunits |
| Reactome | 2 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5D6](https://www.uniprot.org/uniprotkb/Q7L5D6) (Golgi to ER traffic protein 4 homolog):

> As part of a cytosolic protein quality control complex, the BAG6/BAT3 complex, maintains misfolded and hydrophobic patches-containing proteins in a soluble state and participates in their proper delivery to the endoplasmic reticulum or alternatively can promote their sorting to the proteasome where they undergo degradation. The BAG6/BAT3 complex is involved in the post-translational delivery of tail-anchored/type II transmembrane proteins to the endoplasmic reticulum membrane. Recruited to …

**Summary**, from NCBI Gene [51608](https://www.ncbi.nlm.nih.gov/gene/51608):

> Enables protein carrier activity and protein-folding chaperone binding activity. Involved in several processes, including post-translational protein targeting to endoplasmic reticulum membrane; protein catabolic process; and tail-anchored membrane protein insertion into ER membrane. Located in cytosol. Part of BAT3 complex. Implicated in congenital disorder of glycosylation type IIy. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21690) · Entrez [51608](https://www.ncbi.nlm.nih.gov/gene/51608) · UniProt [Q7L5D6](https://www.uniprot.org/uniprotkb/Q7L5D6) · Ensembl [ENSG00000239857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239857)

## Data

Gene col 14214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14214); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14214]; `tensor/DDL_lfc|DDL_z.npy` [14214]; `embed/gene_vectors.npy` [14214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14214 or target_col == 14214). Every well: [[GET4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GET4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
