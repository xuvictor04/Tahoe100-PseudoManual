---
symbol: "PRSS48"
type: "gene"
col: 12090
ensembl_id: "ENSG00000189099"
name: "serine protease 48"
location: "4q31.3"
module: 21
arm: "+"
pooled_cpm: 2.0
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PRSS48

*serine protease 48* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.96× (z +9.8, q 4e-20, up in 6 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +8.6, q 3e-15, up in 13 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW480 0.114×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TACR3-AS1]] (+0.72, fdr 7e-06), [[DNAJC9-AS1-1]] (+0.69, fdr 7e-06), [[PPP1R9A-AS1]] (+0.67, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01956]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +9.8 | 4e-20 | 6/10 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.6 | 3e-15 | 13/29 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +8.5 | 3e-15 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +5.6 | 4e-06 | 11/31 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +5.5 | 5e-06 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +4.7 | 3e-04 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.6 | 3e-04 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +4.6 | 3e-04 | 11/36 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.2 | 0.001 | 2/19 (MIA PaCa-2, Hs 766T) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.003 | 4/19 (KATO III, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +4.0 | 0.003 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.019 | 3/40 (HCT15, RKO, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.1 | 0.083 | 2/17 (NCI-H1573, HOP62) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.093 | 1/30 (J82) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12090.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW480 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.838× | -5.9 | 2e-06 | 25/45 (SW480, LS 180, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.689× | -3.2 | 0.31 | 4/43 (SW 900, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Pimozide (drug)]] 5 µM |  | 0.707× | -3.2 | 0.31 | 13/43 (KATO III, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.64 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.114× (z -8.9) |
| [[A-172 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TACR3-AS1]] | +0.72 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[DNAJC9-AS1-1]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.67 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[NEMP2-DT]] | +0.66 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LINC01811]] | +0.64 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[G2E3-AS1]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R42]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.64 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[CTDSPL2-DT]] | +0.64 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[CHMP3-AS1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PROSER2-AS1]] | +0.63 | +0.46 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01956]] | B | LINC01956 activity raises PRSS48's level | lines that do not express LINC01956 (38) vs lines expressing it (12) | 1.09× lower at baseline in the lines without LINC01956 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01440, SYT4, LINC03000 |
| [[PCDH11X]] | B | PCDH11X activity raises PRSS48's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 1.13× lower at baseline in the lines without PCDH11X | 0.098 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.3, 25.5); signed map (31.0, 5.2). **Vector** length 34.7, 3.07% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.9 | +1.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -5.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 48 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:151,277,161-151,291,862 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ESSPL |
| Gene groups (HGNC) | Serine proteases |
| Matched by | ensembl_id |

UniProt [Q7RTY5](https://www.uniprot.org/uniprotkb/Q7RTY5) carries no function annotation.

**Summary**, from NCBI Gene [345062](https://www.ncbi.nlm.nih.gov/gene/345062):

> Predicted to enable serine-type endopeptidase activity. Predicted to be involved in proteolysis. Predicted to be located in extracellular region. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24635) · Entrez [345062](https://www.ncbi.nlm.nih.gov/gene/345062) · UniProt [Q7RTY5](https://www.uniprot.org/uniprotkb/Q7RTY5) · Ensembl [ENSG00000189099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189099)

## Data

Gene col 12090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12090); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12090]; `tensor/DDL_lfc|DDL_z.npy` [12090]; `embed/gene_vectors.npy` [12090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12090 or target_col == 12090). Every well: [[PRSS48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
