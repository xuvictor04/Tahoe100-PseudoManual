---
symbol: "PKD2L2"
type: "gene"
col: 1232
ensembl_id: "ENSG00000078795"
name: "polycystin 2 like 2, transient receptor potential cation channel"
location: "5q31.2"
module: 21
arm: "+"
pooled_cpm: 3.49
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PKD2L2

*polycystin 2 like 2, transient receptor potential cation channel* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +10.5, q 7e-23, up in 21 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +9.3, q 3e-18, up in 27 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Erlotinib (drug)]] 5 µM in 1 line (NCI-H2347 0.0416×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H460 0.109×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0822×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA21]] (+0.85, fdr 7e-06), [[TOMM20L-DT]] (+0.84, fdr 7e-06), [[CTDSPL2-DT]] (+0.83, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FLJ46284]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +10.5 | 7e-23 | 21/22 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +9.3 | 3e-18 | 27/37 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +9.1 | 2e-17 | 4/5 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +6.8 | 1e-09 | 3/9 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +5.5 | 4e-06 | 18/37 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.48×** | +4.1 | 0.004 | 7/41 (NCI-H1573, J82, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +4.0 | 0.005 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +4.0 | 0.005 | 7/22 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.8 | 0.010 | 3/23 (KATO III, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.6 | 0.018 | 9/35 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Erlotinib (drug)]] 5 µM in 1 line (NCI-H2347 0.0416×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H460 0.109×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0822×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.34 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0822× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 2.93 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0416× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 3.76 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.109× (z -11.0) |
| [[A-172 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA21]] | +0.85 | +0.72 / +0.82 | both halves | 7e-06 |  |
| [[TOMM20L-DT]] | +0.84 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.83 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.83 | +0.65 / +0.84 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.82 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.82 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[ASB14]] | +0.81 | +0.75 / +0.86 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.81 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.81 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.81 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[ZNF451-AS1]] | +0.81 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[EAF1-AS1]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLJ46284]] | C | FLJ46284 activity lowers PKD2L2's level | lines that do not express FLJ46284 (4) vs lines expressing it (46) | 1.04× higher at baseline in the lines without FLJ46284 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP126 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.0, 26.8); signed map (32.5, 5.4). **Vector** length 37.8, 3.29% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | polycystin 2 like 2, transient receptor potential cation channel |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:137,887,968-137,942,747 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRPP5 |
| Gene groups (HGNC) | Polycystin 2, transient receptor potential cation channel family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZM6](https://www.uniprot.org/uniprotkb/Q9NZM6) (Polycystin-2-like protein 2):

> Exhibits a lower single conductance but no spontaneous channel activity. May function as a regulator of calcium channels or a channel component involving Ca2(+) homeostasis (By similarity).

**Summary**, from NCBI Gene [27039](https://www.ncbi.nlm.nih.gov/gene/27039):

> Predicted to enable calcium channel activity. Predicted to be involved in detection of mechanical stimulus. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9012) · Entrez [27039](https://www.ncbi.nlm.nih.gov/gene/27039) · UniProt [Q9NZM6](https://www.uniprot.org/uniprotkb/Q9NZM6) · Ensembl [ENSG00000078795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078795)

## Data

Gene col 1232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1232); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1232]; `tensor/DDL_lfc|DDL_z.npy` [1232]; `embed/gene_vectors.npy` [1232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1232 or target_col == 1232). Every well: [[PKD2L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKD2L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
