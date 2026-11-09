---
symbol: "SYNC"
type: "gene"
col: 8527
ensembl_id: "ENSG00000162520"
name: "syncoilin, intermediate filament protein"
location: "1p35.1"
module: 21
arm: "+"
pooled_cpm: 7.67
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SYNC

*syncoilin, intermediate filament protein* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.89× (z +11.2, q 2e-26, up in 29 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.50× (z +4.3, q 0.002, up in 19 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.0942×, MIA PaCa-2 0.130×); [[Docetaxel (drug)]] 0.05 µM in 1 line (HOP62 0.124×; ⚠ transcription drop); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0897×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (AsPC-1 0.0892×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF451-AS1]] (+0.68, fdr 7e-06), [[HSPA2-AS1]] (+0.67, fdr 1e-05), [[ENO4]] (+0.66, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LIMS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +11.2 | 2e-26 | 29/32 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +9.2 | 7e-18 | 8/13 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +6.5 | 2e-08 | 19/22 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.7 | 4e-04 | 17/34 (CFPAC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.3 | 0.002 | 19/47 (SW480, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.002 | 15/43 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.5 | 0.036 | 10/37 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.041 | 13/43 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.057 | 9/46 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.35× | +3.1 | 0.12 | 9/37 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.0942×, MIA PaCa-2 0.130×); [[Docetaxel (drug)]] 0.05 µM in 1 line (HOP62 0.124×; ⚠ transcription drop); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0897×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (AsPC-1 0.0892×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 6.28 | 0 | 2 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0897× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 5.20 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0892× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 5.33 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0942× (z -9.6) |
| [[HOP62 (line)]] | alt | 8.19 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -10.8) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 7.43 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.130× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 5.03 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0848× (z -8.7) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF451-AS1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[ENO4]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.66 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[CNGB3]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZNF846]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ZNF236-DT]] | +0.63 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[CHMP3-AS1]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TTC36-AS1]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIMS2]] | B | LIMS2 activity raises SYNC's level | lines that do not express LIMS2 (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without LIMS2 | 0.047 | ⚠ within organs, on part of the lines; also absent: PALM, FHL1, ZNF469 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, 26.4); signed map (32.5, 4.2). **Vector** length 53.3, 7.09% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | +1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -0.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | syncoilin, intermediate filament protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,679,906-32,703,596 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SYNCOILIN; previously SYNC1 |
| Gene groups (HGNC) | Intermediate filaments Type III |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7C4](https://www.uniprot.org/uniprotkb/Q9H7C4) (Syncoilin):

> Atypical type III intermediate filament (IF) protein that may play a supportive role in the efficient coupling of mechanical stress between the myofibril and fiber exterior. May facilitate lateral force transmission during skeletal muscle contraction. Does not form homofilaments nor heterofilaments with other IF proteins.

**Summary**, from NCBI Gene [81493](https://www.ncbi.nlm.nih.gov/gene/81493):

> This gene encodes a member of the intermediate filament family which contains an N-terminal head domain, followed by a central coiled-coil region and a short C-terminal tail. The protein is highly expressed in skeletal and cardiac muscle. The protein links the dystrophin associated protein complex (DAPC) to desmin filaments in muscle and may have a structural role in striated muscle. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun …

**Accessions** — [HGNC:28897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28897) · Entrez [81493](https://www.ncbi.nlm.nih.gov/gene/81493) · UniProt [Q9H7C4](https://www.uniprot.org/uniprotkb/Q9H7C4) · Ensembl [ENSG00000162520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162520)

## Data

Gene col 8527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8527); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8527]; `tensor/DDL_lfc|DDL_z.npy` [8527]; `embed/gene_vectors.npy` [8527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8527 or target_col == 8527). Every well: [[SYNC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
