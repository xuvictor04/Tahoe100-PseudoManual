---
symbol: "NACA4P"
type: "gene"
col: 13630
ensembl_id: "ENSG00000228224"
name: "NACA family member 4, pseudogene"
location: "8q22.3"
module: 43
arm: "+"
pooled_cpm: 22.44
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# NACA4P

*NACA family member 4, pseudogene* — 8q22.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.80× (z +6.5, q 5e-08, up in 40 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL18]] (+0.90, fdr 7e-06, ⚠ RPL18 in the vector space only through flagged drug-doses), [[SNHG6]] (+0.87, fdr 7e-06), [[RPL35A]] (+0.86, fdr 7e-06), [[RPS27]] (+0.85, fdr 7e-06); moves opposite to [[SF3B4]] (-0.70, fdr 3e-05), [[PSME3]] (-0.69, fdr 2e-05), [[POGLUT3]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +6.5 | 5e-08 | 40/41 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +5.5 | 1e-05 | 26/34 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.92×** | +4.2 | 0.004 | 36/46 (SW1417, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.393× | -3.2 | 0.66 | 24/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 26 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL18]] ⚠ | +0.90 | +0.84 / +0.92 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | +0.87 | +0.84 / +0.85 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.86 | +0.73 / +0.90 | both halves | 7e-06 |  |
| [[RPS13]] ⚠ | +0.86 | +0.78 / +0.88 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS27]] | +0.85 | +0.72 / +0.88 | both halves | 7e-06 |  |
| [[ATP5MC2]] | +0.85 | +0.76 / +0.86 | both halves | 7e-06 |  |
| [[RPS3]] ⚠ | +0.85 | +0.75 / +0.87 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | +0.84 | +0.72 / +0.87 | both halves | 7e-06 |  |
| [[RPL31]] | +0.84 | +0.69 / +0.89 | both halves | 7e-06 |  |
| [[RPL23]] | +0.84 | +0.72 / +0.87 | both halves | 7e-06 |  |
| [[RPL9]] ⚠ | +0.84 | +0.75 / +0.87 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | +0.84 | +0.74 / +0.85 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.83 | +0.68 / +0.88 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.83 | +0.68 / +0.85 | both halves | 7e-06 |  |
| [[RPS8]] | +0.83 | +0.70 / +0.86 | both halves | 7e-06 |  |
| [[EPB41L4A-AS1]] | +0.83 | +0.71 / +0.86 | both halves | 7e-06 |  |
| [[ADGRL3-AS1]] | +0.82 | +0.61 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B4]] | -0.70 | -0.45 / -0.76 | both halves | 3e-05 |  |
| [[PSME3]] | -0.69 | -0.48 / -0.74 | both halves | 2e-05 |  |
| [[POGLUT3]] | -0.69 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[EMC1]] | -0.68 | -0.54 / -0.71 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.823). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-43.7, -26.8); signed map (-58.8, -3.2). **Vector** length 60.2, 17.4% of its response variance represented; |z| ≥ 3 in 377 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.68 to 55); *Peptide chain elongation* (reactome, mean cos +0.69 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.68 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.0 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | NACA family member 4, pseudogene |
| Locus type | pseudogene |
| Location | 8q22.3 — chr8:101,368,910-101,369,550 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | FKSG17; previously NACAP1 |
| Matched by | ensembl_id |

UniProt [Q9BZK3](https://www.uniprot.org/uniprotkb/Q9BZK3) carries no function annotation.

**Summary**, from NCBI Gene [83955](https://www.ncbi.nlm.nih.gov/gene/83955):

> Predicted to enable unfolded protein binding activity. Predicted to be involved in protein targeting to membrane. Predicted to be part of nascent polypeptide-associated complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24688) · Entrez [83955](https://www.ncbi.nlm.nih.gov/gene/83955) · UniProt [Q9BZK3](https://www.uniprot.org/uniprotkb/Q9BZK3) · Ensembl [ENSG00000228224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228224)

## Data

Gene col 13630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13630); `tables/drug_effects.parquet` (4 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13630]; `tensor/DDL_lfc|DDL_z.npy` [13630]; `embed/gene_vectors.npy` [13630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13630 or target_col == 13630). Every well: [[NACA4P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NACA4P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
