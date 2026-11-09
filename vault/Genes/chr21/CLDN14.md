---
symbol: "CLDN14"
type: "gene"
col: 8239
ensembl_id: "ENSG00000159261"
name: "claudin 14"
location: "21q22.13"
module: 75
arm: "+"
pooled_cpm: 4.49
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# CLDN14

*claudin 14* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.35× (z +11.2, q 3e-26, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +7.3, q 4e-11, up in 18 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0981×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.0749×; ⚠ toxic); [[ULK-101 (drug)]] 0.05 µM in 1 line (HS-578T 0.0526×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESR1]] (+0.73, fdr 7e-06), [[SLC9C1]] (+0.71, fdr 1e-05), [[SLC13A4]] (+0.70, fdr 1e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[OR9Q1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +11.2 | 3e-26 | 3/6 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.21×** | +10.4 | 1e-22 | 4/10 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +10.1 | 1e-21 | 8/17 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.3 | 4e-11 | 18/36 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +4.6 | 4e-04 | 8/33 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.4 | 8e-04 | 13/39 (A-172, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.2 | 0.002 | 3/19 (NCI-H1573, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +3.8 | 0.010 | 7/18 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.010 | 9/43 (Hs 766T, LOX-IMVI, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.055 | 4/29 (NCI-H1792, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.39×** | +3.2 | 0.072 | 5/35 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.2 | 0.072 | 8/26 (Hs 766T, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.072 | 3/25 (KATO III, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0981×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.0749×; ⚠ toxic); [[ULK-101 (drug)]] 0.05 µM in 1 line (HS-578T 0.0526×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.850× | -5.5 | 3e-05 | 24/47 (RKO, LS 180, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.722× | -3.1 | 0.50 | 12/43 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.66 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 4.55 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.93× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 3.50 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0526× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 5.66 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0749× (z -9.9) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0981× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESR1]] | +0.73 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.71 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SLC13A4]] | +0.70 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[OBI1-AS1]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SORCS1]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CHMP1B-AS1]] | +0.67 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LINC00504]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.66 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[MIR4300HG]] | +0.65 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[GALNTL6]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[SFRP4]] | +0.65 | +0.46 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OR9Q1]] | B | OR9Q1 activity raises CLDN14's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.10× lower at baseline in the lines without OR9Q1 | 0.019 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises CLDN14's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without CLDN14-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[LINC01828]] | B | LINC01828 activity raises CLDN14's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 1.81× lower at baseline in the lines without LINC01828 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.1, 24.3); signed map (33.9, 9.9). **Vector** length 46.7, 5.47% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +3.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +0.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | claudin 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.13 — chr21:36,460,621-36,576,569 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNB29 |
| Gene groups (HGNC) | Claudins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O95500](https://www.uniprot.org/uniprotkb/O95500) (Claudin-14):

> Plays a major role in tight junction-specific obliteration of the intercellular space, through calcium-independent cell-adhesion activity.

**Summary**, from NCBI Gene [23562](https://www.ncbi.nlm.nih.gov/gene/23562):

> Tight junctions represent one mode of cell-to-cell adhesion in epithelial or endothelial cell sheets, forming continuous seals around cells and serving as a physical barrier to prevent solutes and water from passing freely through the paracellular space. These junctions are comprised of sets of continuous networking strands in the outwardly facing cytoplasmic leaflet, with complementary grooves in the inwardly facing extracytoplasmic leaflet. The protein encoded by this gene, a member of the …

**Accessions** — [HGNC:2035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2035) · Entrez [23562](https://www.ncbi.nlm.nih.gov/gene/23562) · UniProt [O95500](https://www.uniprot.org/uniprotkb/O95500) · Ensembl [ENSG00000159261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159261)

## Data

Gene col 8239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8239); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8239]; `tensor/DDL_lfc|DDL_z.npy` [8239]; `embed/gene_vectors.npy` [8239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8239 or target_col == 8239). Every well: [[CLDN14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
