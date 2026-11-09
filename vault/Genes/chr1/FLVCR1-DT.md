---
symbol: "FLVCR1-DT"
type: "gene"
col: 12598
ensembl_id: "ENSG00000198468"
name: "FLVCR1 divergent transcript"
location: "1q32.3"
module: 24
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# FLVCR1-DT

*FLVCR1 divergent transcript* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.85× (z +10.1, q 3e-21, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 3.49× (z +8.3, q 2e-14, up in 35 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.374× (z -6.6, q 3e-08, down in 21 of 36 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAT14]] (+0.67, fdr 1e-05), [[PITPNA-AS1]] (+0.65, fdr 1e-05), [[AKAP1-DT]] (+0.65, fdr 7e-06); moves opposite to [[RBM19]] (-0.56, fdr 3e-05), [[CERS2]] (-0.55, fdr 4e-05), [[PRMT3]] (-0.53, fdr 9e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.85×** | +10.1 | 3e-21 | 2/2 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.62×** | +8.6 | 3e-15 | 12/13 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.49×** | +8.3 | 2e-14 | 35/39 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.33×** | +8.0 | 2e-13 | 36/42 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +7.1 | 1e-10 | 13/25 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.61×** | +6.4 | 2e-08 | 30/41 (A498, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.63×** | +5.9 | 2e-07 | 2/2 (NCI-H2347, PANC-1) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +5.4 | 5e-06 | 9/42 (SW480, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.17×** | +5.2 | 2e-05 | 23/44 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.4 | 5e-04 | 6/16 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +4.4 | 7e-04 | 3/9 (NCI-H2030, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +3.7 | 0.011 | 8/21 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.012 | 8/42 (C32, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.5 | 0.020 | 3/8 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.44×** | +3.4 | 0.024 | 4/30 (HOP62, LS 180, …) | top dose only | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.374×** | -6.6 | 3e-08 | 21/36 (PANC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.448×** | -5.3 | 3e-05 | 20/45 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.739 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.680 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.762 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.658 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 20 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAT14]] | +0.67 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PITPNA-AS1]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[AKAP1-DT]] | +0.65 | +0.60 / +0.72 | both halves | 7e-06 | same gene group |
| [[FAM104B]] | +0.63 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[ZNF232-AS1]] | +0.61 | +0.39 / +0.76 | both halves | 5e-05 |  |
| [[FAM229B]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[CLN8-AS1]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[HPF1]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[KMT2E]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 | same gene group |
| [[HINT2]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[NUDT8]] | +0.59 | +0.40 / +0.59 | both halves | 5e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM19]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[CERS2]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[PRMT3]] | -0.53 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[MCM3AP]] | -0.53 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[MTA1]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ELK4]] | -0.52 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[PSME3]] | -0.52 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[TMEM43]] | -0.49 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[HCFC1]] | -0.49 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[REXO1]] | -0.49 | -0.27 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises FLVCR1-DT's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without HES6 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NME3]] | B | NME3 activity lowers FLVCR1-DT's level | lines that do not express NME3 (5) vs lines expressing it (45) | 1.14× higher at baseline in the lines without NME3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TACC2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.5, -17.4); signed map (-22.0, -3.6). **Vector** length 37.8, 4.49% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +2.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +2.2 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +5.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | FLVCR1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.3 — chr1:212,852,105-212,858,139 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LQK1; previously NCRNA00292, FLVCR1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

UniProt [Q8TAF5](https://www.uniprot.org/uniprotkb/Q8TAF5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39077) · Entrez [642946](https://www.ncbi.nlm.nih.gov/gene/642946) · UniProt [Q8TAF5](https://www.uniprot.org/uniprotkb/Q8TAF5) · Ensembl [ENSG00000198468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198468)

## Data

Gene col 12598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12598); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12598]; `tensor/DDL_lfc|DDL_z.npy` [12598]; `embed/gene_vectors.npy` [12598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12598 or target_col == 12598). Every well: [[FLVCR1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLVCR1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
