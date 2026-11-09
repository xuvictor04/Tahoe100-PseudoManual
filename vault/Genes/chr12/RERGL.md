---
symbol: "RERGL"
type: "gene"
col: 3230
ensembl_id: "ENSG00000111404"
name: "RERG like"
location: "12p12.3"
module: 165
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 41
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# RERGL

*RERG like* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.36× (z +21.5, q 0e+00, up in 13 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Triamcinolone (drug)]] 0.05 µM: 0.631× (z -3.8, q 0.083, down in 12 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC8A1-AS1]] (+0.68, fdr 7e-06), [[LINC02511]] (+0.67, fdr 1e-05), [[PLXNA4]] (+0.66, fdr 1e-05).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[SORCS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.36×** | +21.5 | 0e+00 | 13/18 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.17×** | +13.4 | 2e-38 | 14/23 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **4.21×** | +11.8 | 6e-30 | 20/27 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.08×** | +11.1 | 2e-26 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +9.9 | 4e-21 | 17/31 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +9.2 | 4e-18 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +7.3 | 2e-11 | 7/18 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +6.8 | 6e-10 | 8/21 (A-172, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +6.6 | 3e-09 | 1/6 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.22×** | +6.6 | 3e-09 | 12/20 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +6.5 | 3e-09 | 6/20 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.5 | 3e-09 | 6/31 (A498, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +6.4 | 9e-09 | 6/15 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +4.7 | 9e-05 | 11/29 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.75×** | +4.3 | 5e-04 | 3/6 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.65×** | +4.1 | 0.002 | 1/10 (A-172) | inconsistent across doses | low cells (technical?) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.010 | 0/16 | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.022 | 2/11 (NCI-H23, HOP62) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.025 | 0/13 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.631×** | -3.8 | 0.083 | 12/28 (HS-578T, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 1.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +9.2) | — |
| [[A-172 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.836 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.976 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.661 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.659 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.597 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.683 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.645 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.665 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.761 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.603 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.663 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.830 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.820 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.793 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.730 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.600 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.651 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.531 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC8A1-AS1]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.67 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[PLXNA4]] | +0.66 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[ADAMTSL1]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DYNLRB2-AS1]] | +0.63 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[LUZP2]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LRRC4C]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[LINC01483]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[KCNIP1]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[FAT3]] | +0.61 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[RELN]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RERGL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORCS1]] | B | RERGL activity raises SORCS1's level | lines that do not express RERGL (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without RERGL | 0.041 | ⚠ within organs, on part of the lines; also absent: DPYS, TUSC3; maybe low, not absent |
| [[LINC01500]] | B | RERGL activity raises LINC01500's level | lines that do not express RERGL (9) vs lines expressing it (41) | 1.60× lower at baseline in the lines without RERGL | 0.072 | ⚠ within organs, on part of the lines; also absent: DPYS, TUSC3; maybe low, not absent |
| [[LINC02511]] | B | RERGL activity raises LINC02511's level | lines that do not express RERGL (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without RERGL | 0.079 | ⚠ within organs, on part of the lines; also absent: DPYS, TUSC3; maybe low, not absent |
| [[LINC01117]] | B | RERGL activity raises LINC01117's level | lines that do not express RERGL (9) vs lines expressing it (41) | 2.44× lower at baseline in the lines without RERGL | 0.095 | ⚠ within organs, on part of the lines; also absent: DPYS, TUSC3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, 30.8); signed map (32.2, 17.3). **Vector** length 44.1, 7.23% of its response variance represented; |z| ≥ 3 in 774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +21.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +3.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | RERG like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:18,080,869-18,320,107 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22655 |
| Gene groups (HGNC) | RAS type GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H628](https://www.uniprot.org/uniprotkb/Q9H628) (Ras-related and estrogen-regulated growth inhibitor-like protein):

> Binds GDP/GTP and may possess intrinsic GTPase activity.

**Summary**, from NCBI Gene [79785](https://www.ncbi.nlm.nih.gov/gene/79785):

> Predicted to enable G protein activity and GTP binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26213) · Entrez [79785](https://www.ncbi.nlm.nih.gov/gene/79785) · UniProt [Q9H628](https://www.uniprot.org/uniprotkb/Q9H628) · Ensembl [ENSG00000111404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111404)

## Data

Gene col 3230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3230); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3230]; `tensor/DDL_lfc|DDL_z.npy` [3230]; `embed/gene_vectors.npy` [3230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3230 or target_col == 3230). Every well: [[RERGL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RERGL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
