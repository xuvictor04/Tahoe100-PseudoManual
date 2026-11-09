---
symbol: "DNAH3"
type: "gene"
col: 8168
ensembl_id: "ENSG00000158486"
name: "dynein axonemal heavy chain 3"
location: "16p12.3"
module: 191
arm: "+"
pooled_cpm: 2.19
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# DNAH3

*dynein axonemal heavy chain 3* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.05× (z +29.4, q 0e+00, up in 31 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL26A1]] (+0.81, fdr 7e-06), [[HULC]] (+0.81, fdr 7e-06), [[KCNAB1]] (+0.80, fdr 7e-06).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.05×** | +29.4 | 0e+00 | 31/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.07×** | +18.7 | 0e+00 | 27/31 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.76×** | +18.6 | 0e+00 | 1/1 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.78×** | +18.0 | 0e+00 | 10/11 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.20×** | +15.5 | 0e+00 | 27/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.73×** | +14.6 | 0e+00 | 25/36 (LoVo, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.26×** | +14.5 | 1e-45 | 2/2 (SW1417, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.73×** | +14.1 | 4e-43 | 32/39 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.09×** | +13.3 | 2e-38 | 28/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.88×** | +10.0 | 1e-21 | 28/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.52×** | +8.7 | 2e-16 | 22/40 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +7.9 | 1e-13 | 24/42 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.14×** | +7.2 | 4e-11 | 20/40 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +6.7 | 1e-09 | 18/43 (A549, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +6.3 | 1e-08 | 12/36 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +6.0 | 8e-08 | 15/42 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.6 | 7e-07 | 6/43 (A549, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +5.0 | 2e-05 | 5/24 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.45 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 45.0× (z +16.2) | — |
| [[A549 (line)]] | wt | 2.16 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.6× (z +12.6) | — |
| [[A498 (line)]] | wt | 1.45 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +10.5) | — |
| [[LoVo (line)]] | wt | 1.71 | 2 | 0 | [[Auranofin (drug)]] 5 µM 32.2× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +14.0) | — |
| [[A-172 (line)]] | wt | 1.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +9.4) | — |
| [[C32 (line)]] | wt | 1.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 70.2× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 2.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.0× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 1.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +10.5) | — |
| [[KATO III (line)]] | alt | 2.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 1.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 75.9× (z +13.7) | — |
| [[SK-MEL-2 (line)]] | alt | 2.83 | 1 | 0 | [[Auranofin (drug)]] 5 µM 55.7× (z +8.6) | — |
| [[SW480 (line)]] | alt | 4.04 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.06× (z +9.7) | — |
| [[A-427 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL26A1]] | +0.81 | +0.88 / +0.81 | both halves | 7e-06 |  |
| [[HULC]] | +0.81 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.80 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[XKR4]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[DPP6]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[LINC01933]] | +0.75 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MAP3K20-AS1]] | +0.73 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[COL28A1]] | +0.72 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.72 | +0.78 / +0.71 | both halves | 7e-06 | same gene group; STRING 701 |
| [[MYO16]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNAH3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00243]] | B | LINC00243 activity raises DNAH3's level | lines that do not express LINC00243 (5) vs lines expressing it (45) | 1.41× lower at baseline in the lines without LINC00243 | 0.099 | ⚠ within organs, on part of the lines; also absent: DDR1, LAMA2, ATP9A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, 27.0); signed map (30.3, 13.9). **Vector** length 53.0, 7.26% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +29.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +18.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +14.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:20,933,111-21,159,441 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Dnahc3b, DLP3, Hsadhc3, DKFZp434N074 |
| Gene groups (HGNC) | Dyneins, axonemal inner arm I1/f complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD57](https://www.uniprot.org/uniprotkb/Q8TD57) (Dynein axonemal heavy chain 3):

> Force generating protein of respiratory cilia. Produces force towards the minus ends of microtubules. Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP. Involved in sperm motility; implicated in sperm flagellar assembly (By similarity). Essential for the assembly and structural organization of the sperm flagellum's axoneme, including its inner dynein arms and accessory components, which are critical for maintaining flagellar integrity and …

**Summary**, from NCBI Gene [55567](https://www.ncbi.nlm.nih.gov/gene/55567):

> This gene belongs to the dynein family, whose members encode large proteins that are constituents of the microtubule-associated motor protein complex. This complex is composed of dynein heavy, intermediate and light chains, which can be axonemal or cytoplasmic. This protein is an axonemal dynein heavy chain. It is involved in producing force for ciliary beating by using energy from ATP hydrolysis. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided …

**Accessions** — [HGNC:2949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2949) · Entrez [55567](https://www.ncbi.nlm.nih.gov/gene/55567) · UniProt [Q8TD57](https://www.uniprot.org/uniprotkb/Q8TD57) · Ensembl [ENSG00000158486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158486)

## Data

Gene col 8168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8168); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8168]; `tensor/DDL_lfc|DDL_z.npy` [8168]; `embed/gene_vectors.npy` [8168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8168 or target_col == 8168). Every well: [[DNAH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
