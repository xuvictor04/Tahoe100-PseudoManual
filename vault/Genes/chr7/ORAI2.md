---
symbol: "ORAI2"
type: "gene"
col: 8404
ensembl_id: "ENSG00000160991"
name: "ORAI calcium release-activated calcium modulator 2"
location: "7q22.1"
module: 38
arm: "+"
pooled_cpm: 27.06
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ORAI2

*ORAI calcium release-activated calcium modulator 2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +8.8, q 7e-16, up in 35 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 3.47×, A549 3.56×, CFPAC-1 3.06×, MIA PaCa-2 2.83×, …); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 3.57×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.624× (z -4.9, q 6e-04, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PILRA]] (+0.79, fdr 7e-06), [[TINCR]] (+0.76, fdr 7e-06), [[CCNP]] (+0.74, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8404.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 3.47×, A549 3.56×, CFPAC-1 3.06×, MIA PaCa-2 2.83×, …); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 3.57×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.8 | 7e-16 | 35/46 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +8.6 | 2e-15 | 39/47 (LoVo, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.4 | 1e-05 | 26/43 (A-427, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~12% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.624×** | -4.9 | 6e-04 | 25/47 (SK-MEL-2, H4, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -4.4 | 0.003 | 24/47 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -3.9 | 0.019 | 23/47 (SW480, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -3.8 | 0.020 | 24/47 (KATO III, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -3.7 | 0.020 | 26/47 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -3.5 | 0.044 | 23/47 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.701×** | -3.5 | 0.044 | 21/46 (MIA PaCa-2, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -3.4 | 0.049 | 23/46 (H4, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.745× | -3.0 | 0.16 | 17/46 (A-172, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +8.8) | — |
| [[H4 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -9.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 42.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 16.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0303× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 16.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +11.8) | — |
| [[RKO (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.233× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~2% of this change |
| [[A-427 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRA]] | +0.79 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[TINCR]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[CCNP]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[LINC02798]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[ASGR1]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.73 | +0.72 / +0.66 | both halves | 7e-06 | pathway: Muscle contraction |
| [[CPNE9]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[VWCE]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.72 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[AVIL]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.72 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[POU2F2]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises ORAI2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without ASGR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises ORAI2's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without LINC00334 | 0.035 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.7, -19.0); signed map (12.1, 12.4). **Vector** length 107, 28.0% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +2.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +1.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.7 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -2.8 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ORAI calcium release-activated calcium modulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,433,106-102,456,825 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CBCIP2, FLJ12474, FLJ14733, H_NH0514P08.8; previously C7orf19, TMEM142B |
| Gene groups (HGNC) | ORAI calcium release-activated calcium modulators |
| Reactome | 10 pathways, smallest: Elevation of cytosolic Ca2+ levels; Platelet calcium homeostasis; Antigen activates B Cell Receptor (BCR) leading to generation of second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SN7](https://www.uniprot.org/uniprotkb/Q96SN7) (Protein orai-2):

> Pore-forming subunit of inward rectifying Ca(2+) release-activated Ca(2+) (CRAC) channels. Assembles with ORAI1 and ORAI3 to form hexameric CRAC channels that mediate Ca(2+) influx upon depletion of endoplasmic reticulum Ca(2+) store and channel activation by Ca(2+) sensor STIM1, a process known as store-operated Ca(2+) entry (SOCE). Various pore subunit combinations may account for distinct CRAC channel spatiotemporal and cell-type specific dynamics. ORAI1 mainly contributes to the generation …

**Summary**, from NCBI Gene [80228](https://www.ncbi.nlm.nih.gov/gene/80228):

> Enables store-operated calcium channel activity. Involved in store-operated calcium entry. Located in several cellular components, including cytosol; mitochondrion; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21667) · Entrez [80228](https://www.ncbi.nlm.nih.gov/gene/80228) · UniProt [Q96SN7](https://www.uniprot.org/uniprotkb/Q96SN7) · Ensembl [ENSG00000160991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160991)

## Data

Gene col 8404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8404); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8404]; `tensor/DDL_lfc|DDL_z.npy` [8404]; `embed/gene_vectors.npy` [8404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8404 or target_col == 8404). Every well: [[ORAI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORAI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
