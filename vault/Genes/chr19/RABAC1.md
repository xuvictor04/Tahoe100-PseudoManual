---
symbol: "RABAC1"
type: "gene"
col: 2599
ensembl_id: "ENSG00000105404"
name: "Rab acceptor 1"
location: "19q13.2"
module: 48
arm: "+"
pooled_cpm: 16.33
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# RABAC1

*Rab acceptor 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +4.7, q 0.002, up in 28 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +3.9, q 0.013, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.382× (z -8.5, q 1e-14, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OST4]] (+0.81, fdr 7e-06), [[SSR4]] (+0.81, fdr 7e-06), [[ALKBH7]] (+0.80, fdr 7e-06); moves opposite to [[ATIC]] (-0.70, fdr 7e-06), [[SFPQ]] (-0.69, fdr 1e-05), [[GUF1]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EGFL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +4.7 | 0.002 | 28/34 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.88×** | +4.0 | 0.013 | 30/44 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +3.9 | 0.013 | 15/29 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.013 | 27/46 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | 1.69× | +3.3 | 0.10 | 29/47 (HT-29, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2599.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.382×** | -8.5 | 1e-14 | 40/46 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.409×** | -5.6 | 7e-06 | 42/45 (RPMI-7951, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -3.7 | 0.041 | 27/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.571× | -3.3 | 0.10 | 24/47 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.591× | -3.3 | 0.10 | 23/48 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | 0.594× | -3.2 | 0.10 | 26/48 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.372× | -3.2 | 0.10 | 26/44 (LOX-IMVI, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -10.9) |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.4) |
| [[A549 (line)]] | wt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -9.7) |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -8.7) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -8.5) |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.8) |
| [[KATO III (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.6) |
| [[A-172 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OST4]] | +0.81 | +0.64 / +0.87 | both halves | 7e-06 |  |
| [[SSR4]] | +0.81 | +0.67 / +0.85 | both halves | 7e-06 | STRING 424 |
| [[ALKBH7]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[C1orf122]] | +0.79 | +0.56 / +0.82 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.78 | +0.43 / +0.81 | both halves | 3e-05 |  |
| [[ATP5MK]] | +0.76 | +0.58 / +0.79 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.75 | +0.56 / +0.81 | both halves | 1e-05 |  |
| [[UBL5]] | +0.74 | +0.57 / +0.81 | both halves | 1e-05 |  |
| [[PCSK1N]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ZNHIT1]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.73 | +0.58 / +0.80 | both halves | 7e-06 |  |
| [[APOC1]] | +0.73 | +0.51 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | -0.70 | -0.68 / -0.70 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.69 | -0.50 / -0.73 | both halves | 1e-05 |  |
| [[GUF1]] | -0.66 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[GTF2H3]] | -0.66 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[SRSF1]] | -0.65 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[SRSF10]] | -0.64 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.64 | -0.41 / -0.72 | both halves | 4e-05 |  |
| [[RUVBL1]] | -0.64 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[FARSB]] | -0.64 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[SF3B3]] | -0.63 | -0.65 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGFL7]] | B | EGFL7 activity lowers RABAC1's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without EGFL7 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCTD15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.811). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.0, -21.4); signed map (-33.4, 10.5). **Vector** length 73.1, 21.1% of its response variance represented; |z| ≥ 3 in 529 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.59 to 31); *Respiratory electron transport* (reactome, mean cos +0.58 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.59 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | Rab acceptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,956,681-41,959,321 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRA1, PRAF1, YIP3 |
| Gene groups (HGNC) | YIP superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI14](https://www.uniprot.org/uniprotkb/Q9UI14) (Prenylated Rab acceptor protein 1):

> General Rab protein regulator required for vesicle formation from the Golgi complex. May control vesicle docking and fusion by mediating the action of Rab GTPases to the SNARE complexes. In addition it inhibits the removal of Rab GTPases from the membrane by GDI.

**Summary**, from NCBI Gene [10567](https://www.ncbi.nlm.nih.gov/gene/10567):

> Enables identical protein binding activity. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9794) · Entrez [10567](https://www.ncbi.nlm.nih.gov/gene/10567) · UniProt [Q9UI14](https://www.uniprot.org/uniprotkb/Q9UI14) · Ensembl [ENSG00000105404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105404)

## Data

Gene col 2599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2599); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2599]; `tensor/DDL_lfc|DDL_z.npy` [2599]; `embed/gene_vectors.npy` [2599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2599 or target_col == 2599). Every well: [[RABAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
