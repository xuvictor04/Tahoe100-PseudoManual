---
symbol: "OMG"
type: "gene"
col: 4774
ensembl_id: "ENSG00000126861"
name: "oligodendrocyte myelin glycoprotein"
location: "17q11.2"
module: 21
arm: "+"
pooled_cpm: 4.32
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# OMG

*oligodendrocyte myelin glycoprotein* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.24× (z +9.5, q 1e-18, up in 18 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +5.0, q 5e-05, up in 13 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.798× (z -9.2, q 3e-17, down in 33 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.658× (z -4.9, q 3e-04, down in 13 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIRC6-AS2-1]] (+0.83, fdr 7e-06), [[EHBP1-AS1]] (+0.81, fdr 7e-06), [[CTDSPL2-DT]] (+0.80, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +9.5 | 1e-18 | 18/23 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +9.2 | 2e-17 | 5/8 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +6.9 | 1e-09 | 12/27 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +6.4 | 3e-08 | 8/14 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.1 | 4e-05 | 14/36 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.0 | 5e-05 | 13/38 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.010 | 5/47 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.012 | 2/45 (NCI-H23, NCI-H2030) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.047 | 8/45 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.3 | 0.047 | 1/19 (NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.798×** | -9.2 | 3e-17 | 33/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.658×** | -4.9 | 3e-04 | 13/47 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.040 | 15/46 (CFPAC-1, A-427, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.734×** | -3.6 | 0.040 | 10/46 (AN3 CA, J82, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.93 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0928× (z -8.5) |
| [[HT-29 (line)]] | alt | 5.62 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0808× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 4.38 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0799× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 3.87 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0654× (z -10.8) |
| [[A-172 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC6-AS2-1]] | +0.83 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[EHBP1-AS1]] | +0.81 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CTDSPL2-DT]] | +0.80 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[ZBTB20-AS5]] | +0.79 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.78 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.78 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.78 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.78 | +0.60 / +0.78 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.78 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.78 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.77 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[RN7SL1]] | +0.77 | +0.62 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises OMG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers OMG's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.835). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 27.9); signed map (33.5, 5.8). **Vector** length 33.6, 2.81% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -3.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.8 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -0.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | oligodendrocyte myelin glycoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:31,272,013-31,297,539 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OMGP |
| Reactome | 4 pathways, smallest: Axonal growth inhibition (RHOA activation); p75NTR regulates axonogenesis; p75 NTR receptor-mediated signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P23515](https://www.uniprot.org/uniprotkb/P23515) (Oligodendrocyte-myelin glycoprotein):

> Cell adhesion molecule contributing to the interactive process required for myelination in the central nervous system.

**Summary**, from NCBI Gene [4974](https://www.ncbi.nlm.nih.gov/gene/4974):

> Predicted to enable identical protein binding activity. Predicted to be involved in neuron projection regeneration. Predicted to act upstream of or within regulation of collateral sprouting of intact axon in response to injury. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8135) · Entrez [4974](https://www.ncbi.nlm.nih.gov/gene/4974) · UniProt [P23515](https://www.uniprot.org/uniprotkb/P23515) · Ensembl [ENSG00000126861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126861)

## Data

Gene col 4774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4774); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4774]; `tensor/DDL_lfc|DDL_z.npy` [4774]; `embed/gene_vectors.npy` [4774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4774 or target_col == 4774). Every well: [[OMG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OMG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
