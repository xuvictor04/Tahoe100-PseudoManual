---
symbol: "TMPRSS9"
type: "gene"
col: 10915
ensembl_id: "ENSG00000178297"
name: "transmembrane serine protease 9"
location: "19p13.3"
module: 53
arm: "+"
pooled_cpm: 4.08
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# TMPRSS9

*transmembrane serine protease 9* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 18.4× (z +24.9, q 0e+00, up in 42 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELAVL3]] (+0.79, fdr 7e-06), [[SEC1P]] (+0.76, fdr 7e-06), [[CPNE9]] (+0.76, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **18.4×** | +24.9 | 0e+00 | 42/44 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **7.27×** | +23.9 | 0e+00 | 33/36 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **10.3×** | +19.8 | 0e+00 | 45/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.45×** | +18.0 | 0e+00 | 34/35 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.59×** | +17.3 | 0e+00 | 43/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.34×** | +14.3 | 3e-44 | 43/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.70×** | +14.3 | 3e-44 | 5/5 (HepG2/C3A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.25×** | +12.3 | 4e-33 | 21/22 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.87×** | +11.5 | 5e-29 | 29/37 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.88×** | +10.7 | 7e-25 | 9/9 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +7.1 | 5e-11 | 28/44 (SW480, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.24×** | +6.6 | 2e-09 | 25/43 (C32, A498, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +6.3 | 2e-08 | 25/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.9 | 4e-05 | 20/45 (A-172, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.76×** | +4.6 | 1e-04 | 16/37 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.2 | 8e-04 | 14/42 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.018 | 8/38 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Pyridoxine (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.032 | 5/43 (RPMI-7951, Panc 03.27, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +3.2 | 0.032 | 5/41 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.06 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 160× (z +22.4) | — |
| [[HEC-1-A (line)]] | alt | 5.51 | 6 | 0 | [[Auranofin (drug)]] 5 µM 31.5× (z +13.9) | — |
| [[A498 (line)]] | wt | 3.64 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +17.7) | — |
| [[KATO III (line)]] | alt | 5.72 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 52.5× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.85 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 2.89 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.96× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 2.51 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 2.94 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 85.0× (z +17.2) | — |
| [[NCI-H23 (line)]] | alt | 6.09 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +15.3) | — |
| [[NCI-H460 (line)]] | wt | 2.25 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +14.7) | — |
| [[A549 (line)]] | wt | 2.38 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 65.2× (z +10.5) | — |
| [[C32 (line)]] | wt | 3.98 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 80.6× (z +15.9) | — |
| [[A-172 (line)]] | wt | 6.56 | 2 | 0 | [[Auranofin (drug)]] 5 µM 40.8× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 2.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 2.07 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 44.5× (z +9.2) | — |
| [[LoVo (line)]] | wt | 4.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +14.1) | — |
| [[A-427 (line)]] | wt | 4.58 | 1 | 0 | [[Auranofin (drug)]] 5 µM 22.9× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 8.52 | 1 | 0 | [[Auranofin (drug)]] 5 µM 22.0× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 2.71 | 1 | 0 | [[Auranofin (drug)]] 5 µM 33.5× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 3.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.6× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.17 | 1 | 0 | [[Auranofin (drug)]] 5 µM 23.2× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 2.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 5.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 5.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 2.73 | 1 | 0 | [[Auranofin (drug)]] 5 µM 73.5× (z +10.6) | — |
| [[SW48 (line)]] | wt | 4.07 | 1 | 0 | [[Auranofin (drug)]] 5 µM 86.9× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAVL3]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.76 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.76 | +0.84 / +0.67 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.75 | +0.79 / +0.82 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.74 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[RYR1]] | +0.74 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[PRRT3]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[SLC8A2]] | +0.72 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[CELF5]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.70 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.70 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[IRAG1-AS1]] | +0.70 | +0.77 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMPRSS9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.838). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, -14.9); signed map (21.5, 12.6). **Vector** length 65.7, 11.0% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +24.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +23.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +7.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane serine protease 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,360,238-2,426,261 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Type II transmembrane serine proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z410](https://www.uniprot.org/uniprotkb/Q7Z410) (Transmembrane protease serine 9):

> Serase-1 and serase-2 are serine proteases that hydrolyze the peptides N-t-Boc-Gln-Ala-Arg-AMC and N-t-Boc-Gln-Gly-Arg-AMC. In contrast, N-t-Boc-Ala-Phe-Lys-AMC and N-t-Boc-Ala-Pro-Ala-AMC are not significantly hydrolyzed.

**Summary**, from NCBI Gene [360200](https://www.ncbi.nlm.nih.gov/gene/360200):

> The protein encoded by this gene is a membrane-bound type II serine polyprotease that is cleaved to release three different proteases. Two of the proteases are active and can be inhibited by serine protease inhibitors, and one is thought to be catalytically inactive. This gene enhances the invasive capability of pancreatic cancer cells and may be involved in cancer progression. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:30079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30079) · Entrez [360200](https://www.ncbi.nlm.nih.gov/gene/360200) · UniProt [Q7Z410](https://www.uniprot.org/uniprotkb/Q7Z410) · Ensembl [ENSG00000178297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178297)

## Data

Gene col 10915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10915); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10915]; `tensor/DDL_lfc|DDL_z.npy` [10915]; `embed/gene_vectors.npy` [10915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10915 or target_col == 10915). Every well: [[TMPRSS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMPRSS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
