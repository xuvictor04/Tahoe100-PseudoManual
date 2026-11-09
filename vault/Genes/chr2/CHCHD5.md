---
symbol: "CHCHD5"
type: "gene"
col: 4631
ensembl_id: "ENSG00000125611"
name: "coiled-coil-helix-coiled-coil-helix domain containing 5"
location: "2q14.1"
module: 24
arm: "+"
pooled_cpm: 8.4
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# CHCHD5

*coiled-coil-helix-coiled-coil-helix domain containing 5* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.24× (z +5.6, q 1e-05, up in 24 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bendamustine (drug)]] 5 µM: 1.67× (z +3.4, q 0.070, up in 22 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.593× (z -5.1, q 2e-04, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.81, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[IFI27L2]] (+0.79, fdr 1e-05), [[POLR2I]] (+0.75, fdr 7e-06), [[RPP21]] (+0.73, fdr 7e-06); moves opposite to [[MOB1A]] (-0.67, fdr 7e-06), [[CBX5]] (-0.62, fdr 3e-05), [[LIN7C]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4631.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +5.6 | 1e-05 | 24/32 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.79×** | +4.0 | 0.011 | 22/37 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +4.0 | 0.011 | 11/15 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +3.9 | 0.014 | 14/23 (A549, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Bendamustine (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.070 | 22/43 (A-172, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.593×** | -5.1 | 2e-04 | 29/44 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.502×** | -4.7 | 6e-04 | 30/46 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.514×** | -4.6 | 9e-04 | 28/46 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.593×** | -3.6 | 0.040 | 23/46 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -3.6 | 0.040 | 25/46 (BT-474, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -3.5 | 0.040 | 22/42 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.610× | -3.1 | 0.14 | 17/46 (A-427, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 9.04 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.05 µM 0.0464× (z -10.6) |
| [[J82 (line)]] | alt | 6.89 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0665× (z -10.9) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 17 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.81 | +0.56 / +0.84 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.79 | +0.50 / +0.82 | both halves | 1e-05 |  |
| [[POLR2I]] | +0.75 | +0.60 / +0.82 | both halves | 7e-06 |  |
| [[RPP21]] | +0.73 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[WDR83OS]] ⚠ | +0.72 | +0.55 / +0.74 | both halves | 1e-05 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB4]] | +0.71 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[COX6B1]] | +0.71 | +0.40 / +0.75 | both halves | 5e-05 |  |
| [[MRPL32]] | +0.71 | +0.35 / +0.79 | both halves | 1e-04 |  |
| [[ZFAND2A-DT]] | +0.70 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[LAMTOR5]] | +0.70 | +0.44 / +0.79 | both halves | 3e-05 |  |
| [[TRIM52-AS1]] | +0.70 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[JOSD2]] | +0.70 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[ATP5MC2]] | +0.70 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[CHCHD1]] | +0.70 | +0.34 / +0.75 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.67 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[CBX5]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.62 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[TARDBP]] | -0.61 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[IPO5]] | -0.61 | -0.32 / -0.67 | both halves | 2e-04 |  |
| [[FLNA]] | -0.60 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[MMGT1]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 | pathway: Protein localization |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CHCHD5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM174C]] | C | FAM174C's natural level strengthens CHCHD5's drug response | FAM174C's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.25; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.829). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.9, -16.0); signed map (-14.2, -3.8). **Vector** length 49.7, 8.86% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.56 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +0.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.2 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.9 | +5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil-helix-coiled-coil-helix domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,584,240-112,589,275 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11104, MIC14, MIX14; previously C2orf9 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

UniProt [Q9BSY4](https://www.uniprot.org/uniprotkb/Q9BSY4) carries no function annotation.

**Summary**, from NCBI Gene [84269](https://www.ncbi.nlm.nih.gov/gene/84269):

> Predicted to be involved in cellular respiration. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17840) · Entrez [84269](https://www.ncbi.nlm.nih.gov/gene/84269) · UniProt [Q9BSY4](https://www.uniprot.org/uniprotkb/Q9BSY4) · Ensembl [ENSG00000125611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125611)

## Data

Gene col 4631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4631); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4631]; `tensor/DDL_lfc|DDL_z.npy` [4631]; `embed/gene_vectors.npy` [4631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4631 or target_col == 4631). Every well: [[CHCHD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHCHD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
