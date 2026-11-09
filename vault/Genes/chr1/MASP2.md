---
symbol: "MASP2"
type: "gene"
col: 190
ensembl_id: "ENSG00000009724"
name: "MBL associated serine protease 2"
location: "1p36.22"
module: 53
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# MASP2

*MBL associated serine protease 2* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.45× (z +11.5, q 6e-28, up in 31 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Talc (drug)]] 0.5 µM in 1 line (HOP62 0.0528×); [[Penfluridol (drug)]] 5 µM in 1 line (A498 0.0779×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOMM20L-DT]] (+0.79, fdr 7e-06), [[IL12RB2]] (+0.78, fdr 7e-06), [[ELAVL3]] (+0.77, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +11.5 | 6e-28 | 31/34 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.55×** | +11.5 | 6e-28 | 9/14 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +10.5 | 1e-23 | 2/3 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +7.9 | 3e-13 | 5/5 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +6.8 | 1e-09 | 5/13 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +5.3 | 1e-05 | 7/36 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.2 | 2e-05 | 13/36 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +5.1 | 3e-05 | 14/41 (HOP62, SW48, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.65×** | +4.6 | 3e-04 | 11/30 (SW1417, NCI-H460, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.002 | 4/35 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.53×** | +3.8 | 0.007 | 9/45 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.8 | 0.008 | 7/31 (A549, KATO III, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.076 | 5/44 (RPMI-7951, PANC-1, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | 1.89× | +3.0 | 0.10 | 2/28 (HEC-1-A, SW480) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 190.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Talc (drug)]] 0.5 µM in 1 line (HOP62 0.0528×); [[Penfluridol (drug)]] 5 µM in 1 line (A498 0.0779×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -3.3 | 0.52 | 15/47 (MIA PaCa-2, AN3 CA, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.791× | -3.0 | 0.60 | 1/45 (HepG2/C3A) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.15 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0779× (z -8.7) |
| [[A549 (line)]] | wt | 2.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.57× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 2.50 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0528× (z -9.0) |
| [[A-172 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM20L-DT]] | +0.79 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.78 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.77 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.76 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[DNAJC9-AS1-1]] | +0.74 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.74 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[MYH3]] | +0.73 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[F2]] | +0.72 | +0.60 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_COAGULATION; STRING 688 |
| [[MYO15A]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.72 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[ARL9]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.71 | +0.60 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2]] | B | F2 activity raises MASP2's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.17× lower at baseline in the lines without F2 | 0.062 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises MASP2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.19× lower at baseline in the lines without ASGR1 | 0.083 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.0, -16.9); signed map (20.0, 12.7). **Vector** length 38.5, 3.59% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MBL associated serine protease 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,022,009-11,047,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Map19, sMAP, MAP-2; previously MASP1P1 |
| Gene groups (HGNC) | Serine proteases; Sushi domain containing; Complement system activation components |
| Hallmark sets | COAGULATION |
| Reactome | 10 pathways, smallest: Lectin pathway of complement activation; Creation of C4 and C2 activators; Initial triggering of complement |
| Matched by | ensembl_id |

**Function**, from UniProt [O00187](https://www.uniprot.org/uniprotkb/O00187) (Mannan-binding lectin serine protease 2):

> Precursor of a serum protease that activates the lectin pathway of the complement system, a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system. The lectin complement system is activated following association of lectins, such as MBL2, FCN1, FCN2 or FCN3, to carbohydrates on the pathogen surface. MASP2 is cleaved and activated by MASP1 in response to lectin-binding to pathogen carbohydrates. Can activate prothrombin …

**Summary**, from NCBI Gene [10747](https://www.ncbi.nlm.nih.gov/gene/10747):

> This gene encodes a member of the peptidase S1 family of serine proteases. The encoded preproprotein is proteolytically processed to generate A and B chains that heterodimerize to form the mature protease. This protease cleaves complement components C2 and C4 in order to generate C3 convertase in the lectin pathway of the complement system. The encoded protease also plays a role in the coagulation cascade through cleavage of prothrombin to form thrombin. Myocardial infarction and acute stroke …

**Accessions** — [HGNC:6902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6902) · Entrez [10747](https://www.ncbi.nlm.nih.gov/gene/10747) · UniProt [O00187](https://www.uniprot.org/uniprotkb/O00187) · Ensembl [ENSG00000009724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009724)

## Data

Gene col 190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 190); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 190]; `tensor/DDL_lfc|DDL_z.npy` [190]; `embed/gene_vectors.npy` [190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 190 or target_col == 190). Every well: [[MASP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MASP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
