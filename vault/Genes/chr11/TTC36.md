---
symbol: "TTC36"
type: "gene"
col: 10253
ensembl_id: "ENSG00000172425"
name: "tetratricopeptide repeat domain 36"
location: "11q23.3"
module: 47
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# TTC36

*tetratricopeptide repeat domain 36* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +9.4, q 3e-18, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.365× (z -8.2, q 2e-13, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM25]] (+0.91, fdr 7e-06, ⚠ same locus), [[MYOCOS]] (+0.83, fdr 7e-06), [[EPHX3]] (+0.80, fdr 7e-06), [[RFPL3S]] (+0.79, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00334]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HCLS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +9.4 | 3e-18 | 17/31 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.4 | 2e-05 | 10/28 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.72×** | +4.4 | 0.002 | 6/21 (KATO III, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.1 | 0.005 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.006 | 3/45 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.52× | +3.1 | 0.17 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.365×** | -8.2 | 2e-13 | 25/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -5.0 | 2e-04 | 19/41 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.553×** | -4.8 | 3e-04 | 22/40 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.569×** | -4.4 | 0.001 | 14/34 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.606×** | -4.1 | 0.005 | 10/16 (LOX-IMVI, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.639×** | -3.6 | 0.026 | 11/36 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **0.663×** | -3.3 | 0.067 | 10/43 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | 0.681× | -3.1 | 0.12 | 9/43 (HepG2/C3A, RPMI-7951, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.673× | -3.1 | 0.12 | 4/38 (A-172, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.691× | -3.0 | 0.15 | 8/41 (H4, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 6.16 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0428× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~82% of this change |
| [[A498 (line)]] | wt | 2.11 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0531× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 3.66 | 0 | 1 | — | [[APTO-253 (drug)]] 0.05 µM 0.0419× (z -9.6) |
| [[PANC-1 (line)]] | alt | 1.77 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0448× (z -9.3) |
| [[A-172 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM25]] | +0.91 | +0.86 / +0.88 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MYOCOS]] | +0.83 | +0.84 / +0.78 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.80 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[RFPL3S]] | +0.79 | +0.79 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.79 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[OIT3]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[HCLS1]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.77 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[PILRA]] | +0.77 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[IMPG2]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.76 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[USP50]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00334]] | B | LINC00334 activity raises TTC36's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.30× lower at baseline in the lines without LINC00334 | 0.042 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[PRKCG]] | B | PRKCG activity raises TTC36's level | lines that do not express PRKCG (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without PRKCG | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC36A4, DBN1, CEP41; maybe low, not absent |
| [[LINC02133]] | C | LINC02133 activity raises TTC36's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 1.35× lower at baseline in the lines without LINC02133 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HCLS1]] | C | TTC36's natural level strengthens HCLS1's drug response | TTC36's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.20; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, -14.8); signed map (17.3, 10.6). **Vector** length 56.2, 7.82% of its response variance represented; |z| ≥ 3 in 1,212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +4.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -2.8 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -8.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,527,472-118,531,197 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HBP21 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [A6NLP5](https://www.uniprot.org/uniprotkb/A6NLP5) carries no function annotation.

**Summary**, from NCBI Gene [143941](https://www.ncbi.nlm.nih.gov/gene/143941):

> The protein encoded by this gene has three tetratricopeptide repeats and is a chaperone for heat shock protein 70. The encoded protein may function as a tumor suppressor in hepatocellular carcinoma (HCC) since it promotes apoptosis but is downregulated in HCC. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:33708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33708) · Entrez [143941](https://www.ncbi.nlm.nih.gov/gene/143941) · UniProt [A6NLP5](https://www.uniprot.org/uniprotkb/A6NLP5) · Ensembl [ENSG00000172425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172425)

## Data

Gene col 10253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10253); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10253]; `tensor/DDL_lfc|DDL_z.npy` [10253]; `embed/gene_vectors.npy` [10253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10253 or target_col == 10253). Every well: [[TTC36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
