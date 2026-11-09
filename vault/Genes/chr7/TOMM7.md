---
symbol: "TOMM7"
type: "gene"
col: 12264
ensembl_id: "ENSG00000196683"
name: "translocase of outer mitochondrial membrane 7"
location: "7p15.3"
module: 43
arm: "+"
pooled_cpm: 75.37
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# TOMM7

*translocase of outer mitochondrial membrane 7* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.10× (z +6.1, q 6e-07, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.605× (z -4.7, q 0.002, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.316×, NCI-H23 0.318×); [[Drospirenone (drug)]] 0.5 µM in 1 line (NCI-H661 0.0502×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL36]] (+0.90, fdr 7e-06), [[ATP5MC2]] (+0.89, fdr 7e-06), [[UQCRB]] (+0.89, fdr 7e-06, ⚠ UQCRB in the vector space only through flagged drug-doses), [[RPL35A]] (+0.88, fdr 7e-06); moves opposite to [[PSME3]] (-0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RPS28]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.10×** | +6.1 | 6e-07 | 45/49 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +5.6 | 6e-06 | 40/43 (NCI-H460, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.04×** | +4.7 | 4e-04 | 43/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.6 | 0.032 | 38/47 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.72×** | +3.6 | 0.032 | 39/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 1.66× | +3.1 | 0.18 | 31/45 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12264.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.316×, NCI-H23 0.318×); [[Drospirenone (drug)]] 0.5 µM in 1 line (NCI-H661 0.0502×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.605×** | -4.7 | 0.002 | 41/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 79.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 74.3 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0502× (z -10.6) |
| [[A-172 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 93.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 80.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 26 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL36]] | +0.90 | +0.84 / +0.90 | both halves | 7e-06 | pathway: Protein localization |
| [[ATP5MC2]] | +0.89 | +0.82 / +0.91 | both halves | 7e-06 |  |
| [[UQCRB]] ⚠ | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | STRING 481; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.88 | +0.83 / +0.88 | both halves | 7e-06 | pathway: Protein localization; STRING 513 |
| [[RPS27A]] ⚠ | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | pathway: Autophagy; STRING 558; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.88 | +0.81 / +0.88 | both halves | 7e-06 | pathway: Protein localization; STRING 729 |
| [[RPL18]] ⚠ | +0.87 | +0.80 / +0.87 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5ME]] | +0.87 | +0.70 / +0.88 | both halves | 7e-06 | STRING 706 |
| [[ATP5MJ]] | +0.87 | +0.80 / +0.88 | both halves | 7e-06 |  |
| [[RPS27]] | +0.86 | +0.80 / +0.88 | both halves | 7e-06 | pathway: Protein localization; STRING 488 |
| [[RPL34]] | +0.86 | +0.81 / +0.86 | both halves | 7e-06 | pathway: Protein localization; STRING 461 |
| [[RPS14]] | +0.86 | +0.77 / +0.87 | both halves | 7e-06 | pathway: Protein localization; STRING 453 |
| [[RPL23]] | +0.86 | +0.76 / +0.88 | both halves | 7e-06 | pathway: Protein localization; STRING 520 |
| [[COMMD6]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | STRING 418 |
| [[RPS29]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | pathway: Protein localization; STRING 694 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.74 | -0.62 / -0.77 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS28]] | B | RPS28 activity raises TOMM7's level | lines that do not express RPS28 (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without RPS28 | 0.011 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | TOMM7's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | TOMM7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.474 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.837). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.7, -24.4); signed map (-34.7, 7.9). **Vector** length 77.4, 37.6% of its response variance represented; |z| ≥ 3 in 371 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.70 to 55); *Peptide chain elongation* (reactome, mean cos +0.71 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.71 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +2.4 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | -0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.1 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.6 | -0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +0.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.2 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | +0.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | translocase of outer mitochondrial membrane 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:22,812,628-22,822,849 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tom7 |
| Gene groups (HGNC) | Translocase of outer mitochondrial membrane complex |
| Reactome | 7 pathways, smallest: PINK1-PRKN Mediated Mitophagy; Mitophagy; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0U1](https://www.uniprot.org/uniprotkb/Q9P0U1) (Mitochondrial import receptor subunit TOM7 homolog):

> Component of the translocase of the outer membrane of mitochondria (TOM) complex essential for the recognition and translocation of cytosolically synthesized mitochondrial preproteins. The TOM complex associates with the ion channel VDAC2 and PINK1 kinase at depolarized mitochondria, this interaction stabilizes PINK1 at the outer mitochondrial membrane and triggers downstream mitophagy by the recruitment of the E3 ubiquitin ligase PRKN.

**Summary**, from NCBI Gene [54543](https://www.ncbi.nlm.nih.gov/gene/54543):

> This gene encodes a subunit of the translocase of the outer mitochondrial membrane. The encoded protein regulates the assembly and stability of the translocase complex. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:21648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21648) · Entrez [54543](https://www.ncbi.nlm.nih.gov/gene/54543) · UniProt [Q9P0U1](https://www.uniprot.org/uniprotkb/Q9P0U1) · Ensembl [ENSG00000196683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196683)

## Data

Gene col 12264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12264); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12264]; `tensor/DDL_lfc|DDL_z.npy` [12264]; `embed/gene_vectors.npy` [12264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12264 or target_col == 12264). Every well: [[TOMM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
