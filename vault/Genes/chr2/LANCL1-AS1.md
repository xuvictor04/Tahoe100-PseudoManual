---
symbol: "LANCL1-AS1"
type: "gene"
col: 13948
ensembl_id: "ENSG00000234281"
name: "LANCL1 antisense RNA 1"
location: "2q34"
module: 21
arm: "+"
pooled_cpm: 3.02
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# LANCL1-AS1

*LANCL1 antisense RNA 1* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.58× (z +18.8, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Malotilate (drug)]] 0.5 µM: 0.670× (z -4.2, q 0.017, down in 9 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HRG-AS1]] (+0.85, fdr 7e-06), [[CHMP3-AS1]] (+0.83, fdr 7e-06), [[SPATA1]] (+0.82, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.58×** | +18.8 | 0e+00 | 36/36 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.04×** | +11.6 | 1e-28 | 30/43 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +11.0 | 8e-26 | 13/18 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +8.4 | 5e-15 | 5/6 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +7.9 | 4e-13 | 17/35 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +6.9 | 4e-10 | 15/31 (NCI-H2030, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +6.6 | 4e-09 | 2/7 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +6.4 | 1e-08 | 10/17 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +5.9 | 3e-07 | 12/35 (SW48, COLO 205, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.8 | 7e-05 | 9/31 (NCI-H1792, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.008 | 7/43 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.011 | 10/46 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.097 | 6/32 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.50× | +3.0 | 0.10 | 0/39 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Malotilate (drug)]] 0.5 µM |  | **0.670×** | -4.2 | 0.017 | 9/42 (Panc 03.27, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.98 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.65× (z +10.2) | — |
| [[A498 (line)]] | wt | 2.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.80× (z +9.8) | — |
| [[C32 (line)]] | wt | 3.47 | 1 | 0 | [[Auranofin (drug)]] 5 µM 21.0× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 3.14 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.2× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +12.4) | — |
| [[A-427 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HRG-AS1]] | +0.85 | +0.69 / +0.82 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.83 | +0.68 / +0.81 | both halves | 7e-06 | same gene group |
| [[SPATA1]] | +0.82 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.82 | +0.81 / +0.73 | both halves | 7e-06 | same gene group |
| [[DENND6A-AS1]] | +0.80 | +0.70 / +0.76 | both halves | 7e-06 | same gene group |
| [[PAXBP1-AS1]] | +0.80 | +0.76 / +0.69 | both halves | 7e-06 | same gene group |
| [[SYNM-AS1]] | +0.80 | +0.69 / +0.76 | both halves | 7e-06 | same gene group |
| [[PSMD14-DT]] | +0.79 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[HPSE2]] | +0.79 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.79 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.78 | +0.60 / +0.76 | both halves | 7e-06 | same gene group |
| [[CCNO-DT]] | +0.77 | +0.55 / +0.78 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LANCL1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HAND2-AS1]] | B | HAND2-AS1 activity raises LANCL1-AS1's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.18× lower at baseline in the lines without HAND2-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.842). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, 25.4); signed map (32.5, 3.1). **Vector** length 44.1, 4.71% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +18.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | LANCL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q34 — chr2:210,324,759-210,469,246 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LANCLOT |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50727) · Entrez [102724820](https://www.ncbi.nlm.nih.gov/gene/102724820) · Ensembl [ENSG00000234281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234281)

## Data

Gene col 13948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13948); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13948]; `tensor/DDL_lfc|DDL_z.npy` [13948]; `embed/gene_vectors.npy` [13948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13948 or target_col == 13948). Every well: [[LANCL1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LANCL1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
