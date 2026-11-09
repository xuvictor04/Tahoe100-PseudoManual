---
symbol: "SPATA21"
type: "gene"
col: 11893
ensembl_id: "ENSG00000187144"
name: "spermatogenesis associated 21"
location: "1p36.13"
module: 21
arm: "+"
pooled_cpm: 3.58
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SPATA21

*spermatogenesis associated 21* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.52× (z +14.2, q 5e-43, up in 20 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.32× (z +13.4, q 2e-38, up in 32 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.05 µM in 1 line (A498 0.0879×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP3-AS1]] (+0.89, fdr 7e-06), [[PKD2L2]] (+0.85, fdr 7e-06), [[CNTNAP5]] (+0.84, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02384]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC51A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.52×** | +14.2 | 5e-43 | 20/23 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +13.4 | 2e-38 | 32/38 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +12.1 | 2e-31 | 7/7 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +11.0 | 8e-26 | 24/36 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +8.9 | 7e-17 | 5/9 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.5 | 6e-09 | 15/36 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.8 | 1e-04 | 6/22 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +3.8 | 0.011 | 1/40 (SW480) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.39×** | +3.7 | 0.011 | 8/25 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.6 | 0.019 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.36×** | +3.5 | 0.027 | 9/46 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.028 | 6/35 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.028 | 5/45 (PANC-1, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.029 | 3/44 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +3.4 | 0.030 | 7/44 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.050 | 9/44 (SW48, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.050 | 6/33 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.077 | 9/44 (SW480, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11893.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.05 µM in 1 line (A498 0.0879×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -4.6 | 0.002 | 17/48 (LS 180, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.86 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0879× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +8.9) | — |
| [[LoVo (line)]] | wt | 3.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +9.6) | — |
| [[SW480 (line)]] | alt | 3.54 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP3-AS1]] | +0.89 | +0.73 / +0.84 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.85 | +0.72 / +0.82 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.84 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[C2CD5-AS1]] | +0.84 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[USH2A]] | +0.82 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.82 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.82 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.81 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.81 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.81 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.81 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[ABHD15-AS1]] | +0.81 | +0.69 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02384]] | B | LINC02384 activity raises SPATA21's level | lines that do not express LINC02384 (26) vs lines expressing it (24) | 1.02× lower at baseline in the lines without LINC02384 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, ENSG00000277693, FAM230C; maybe low, not absent |
| [[MAP1LC3A]] | C | MAP1LC3A activity lowers SPATA21's level | lines that do not express MAP1LC3A (4) vs lines expressing it (46) | 1.06× higher at baseline in the lines without MAP1LC3A | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285155; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC51A]] | C | SPATA21's natural level weakens SLC51A's drug response | SPATA21's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.74, reverse +0.04; direction clear | 0.013 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.885). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, 27.1); signed map (32.9, 5.4). **Vector** length 38.0, 3.59% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -4.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,387,117-16,437,424 (-) |
| Ensembl biotype | protein_coding |
| Also known as | spergen-2, spergen2 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z572](https://www.uniprot.org/uniprotkb/Q7Z572) (Spermatogenesis-associated protein 21):

> Involved in the differentiation of haploid spermatids.

**Summary**, from NCBI Gene [374955](https://www.ncbi.nlm.nih.gov/gene/374955):

> Predicted to enable calcium ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28026) · Entrez [374955](https://www.ncbi.nlm.nih.gov/gene/374955) · UniProt [Q7Z572](https://www.uniprot.org/uniprotkb/Q7Z572) · Ensembl [ENSG00000187144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187144)

## Data

Gene col 11893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11893); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11893]; `tensor/DDL_lfc|DDL_z.npy` [11893]; `embed/gene_vectors.npy` [11893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11893 or target_col == 11893). Every well: [[SPATA21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
