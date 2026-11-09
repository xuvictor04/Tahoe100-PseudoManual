---
symbol: "ATP5MJ"
type: "gene"
col: 7977
ensembl_id: "ENSG00000156411"
name: "ATP synthase membrane subunit j"
location: "14q32.33"
module: 48
arm: "+"
pooled_cpm: 45.34
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ATP5MJ

*ATP synthase membrane subunit j* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +6.1, q 8e-07, up in 43 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.626× (z -4.2, q 0.015, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMTOR5]] (+0.89, fdr 7e-06), [[COMMD6]] (+0.89, fdr 7e-06), [[ATP5MK]] (+0.88, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.79, fdr 7e-06), [[HNRNPK]] (-0.75, fdr 7e-06), [[TUG1]] (-0.75, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.69×** | +6.1 | 8e-07 | 43/46 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.18×** | +5.0 | 2e-04 | 46/48 (BT-474, SW480, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **2.05×** | +4.4 | 0.002 | 31/40 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.90×** | +4.1 | 0.006 | 42/48 (HOP62, SW480, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.0 | 0.006 | 45/47 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.84×** | +3.9 | 0.009 | 34/46 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.74×** | +3.6 | 0.031 | 39/48 (SW480, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.73×** | +3.2 | 0.085 | 30/45 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.64×** | +3.2 | 0.099 | 33/47 (COLO 205, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7977.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.626×** | -4.2 | 0.015 | 39/48 (C-33 A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5]] | +0.89 | +0.80 / +0.91 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.89 | +0.78 / +0.89 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.88 | +0.80 / +0.88 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[RBIS]] | +0.87 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.87 | +0.80 / +0.88 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.86 | +0.78 / +0.83 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 413 |
| [[RPS14]] | +0.85 | +0.77 / +0.85 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | +0.85 | +0.73 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | +0.85 | +0.78 / +0.86 | both halves | 7e-06 |  |
| [[ATP5ME]] | +0.84 | +0.70 / +0.87 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 997 |
| [[RPL35A]] | +0.84 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | +0.84 | +0.73 / +0.89 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6B1]] | +0.84 | +0.77 / +0.89 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 412 |
| [[ELOB]] | +0.84 | +0.72 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.79 | -0.66 / -0.72 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.75 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[TUG1]] | -0.75 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | -0.72 | -0.64 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ATP5MJ's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.861). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-44.9, -22.5); signed map (-34.0, 8.2). **Vector** length 75.2, 30.9% of its response variance represented; |z| ≥ 3 in 441 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.65 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.69 to 24); *Complex IV assembly* (reactome, mean cos +0.69 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.4 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.3 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.1 | +4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -6.5 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -6.4 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -5.9 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase membrane subunit j |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,912,288-103,928,269 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MP68, MLQ, 6.8PL; previously C14orf2, ATP5MPL |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P56378](https://www.uniprot.org/uniprotkb/P56378) (ATP synthase F(0) complex subunit j, mitochondrial):

> Subunit j, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a stationary …

**Summary**, from NCBI Gene [9556](https://www.ncbi.nlm.nih.gov/gene/9556):

> Predicted to be involved in proton motive force-driven ATP synthesis. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1188) · Entrez [9556](https://www.ncbi.nlm.nih.gov/gene/9556) · UniProt [P56378](https://www.uniprot.org/uniprotkb/P56378) · Ensembl [ENSG00000156411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156411)

## Data

Gene col 7977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7977); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7977]; `tensor/DDL_lfc|DDL_z.npy` [7977]; `embed/gene_vectors.npy` [7977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7977 or target_col == 7977). Every well: [[ATP5MJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5MJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
