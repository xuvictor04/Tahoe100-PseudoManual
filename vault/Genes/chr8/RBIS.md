---
symbol: "RBIS"
type: "gene"
col: 10747
ensembl_id: "ENSG00000176731"
name: "ribosomal biogenesis factor"
location: "8q21.2"
module: 43
arm: "+"
pooled_cpm: 38.78
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RBIS

*ribosomal biogenesis factor* — 8q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.84× (z +5.9, q 3e-06, up in 36 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.42× (z +3.4, q 0.068, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.617× (z -6.0, q 1e-06, down in 39 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.244×, RKO 0.342×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.216×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.261×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MJ]] (+0.87, fdr 7e-06), [[TOMM7]] (+0.82, fdr 7e-06), [[COMMD6]] (+0.80, fdr 7e-06); moves opposite to [[FGD5-AS1]] (-0.75, fdr 7e-06), [[EIF4G2]] (-0.73, fdr 1e-05), [[SEPTIN11]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.84×** | +5.9 | 3e-06 | 36/44 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.60×** | +4.6 | 0.001 | 37/46 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.56×** | +4.1 | 0.007 | 23/39 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.0 | 0.007 | 33/47 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.068 | 25/48 (COLO 205, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +3.4 | 0.068 | 31/48 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.77×** | +3.3 | 0.077 | 28/48 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.77×** | +3.3 | 0.077 | 34/48 (KATO III, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10747.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.244×, RKO 0.342×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.216×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.261×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -6.0 | 1e-06 | 39/47 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.015 | 25/48 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 35.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.3) |
| [[RKO (line)]] | wt | 94.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.4) |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MJ]] | +0.87 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.82 | +0.67 / +0.82 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.80 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.79 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[RPL31]] | +0.78 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[RPS14]] | +0.78 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | +0.77 | +0.63 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS26]] | +0.77 | +0.46 / +0.77 | both halves | 2e-05 |  |
| [[POLR2I]] | +0.77 | +0.45 / +0.80 | both halves | 3e-05 |  |
| [[RPL17]] | +0.77 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[RPL36]] | +0.77 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.76 | +0.59 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD5-AS1]] | -0.75 | -0.60 / -0.74 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.73 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[SEPTIN11]] | -0.69 | -0.53 / -0.72 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.66 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[PTBP1]] | -0.64 | -0.67 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RBIS's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.9, -24.4); signed map (-34.7, 6.5). **Vector** length 75.9, 22.7% of its response variance represented; |z| ≥ 3 in 384 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.60 to 55); *Peptide chain elongation* (reactome, mean cos +0.61 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.61 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.2 | +3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.6 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -3.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -3.1 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.2 — chr8:85,214,048-85,220,421 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C8orf59 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0T1](https://www.uniprot.org/uniprotkb/Q8N0T1) (Ribosomal biogenesis factor):

> Trans-acting factor in ribosome biogenesis required for efficient 40S and 60S subunit production.

**Summary**, from NCBI Gene [401466](https://www.ncbi.nlm.nih.gov/gene/401466):

> Involved in ribosome biogenesis. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32235) · Entrez [401466](https://www.ncbi.nlm.nih.gov/gene/401466) · UniProt [Q8N0T1](https://www.uniprot.org/uniprotkb/Q8N0T1) · Ensembl [ENSG00000176731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176731)

## Data

Gene col 10747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10747); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10747]; `tensor/DDL_lfc|DDL_z.npy` [10747]; `embed/gene_vectors.npy` [10747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10747 or target_col == 10747). Every well: [[RBIS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBIS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
