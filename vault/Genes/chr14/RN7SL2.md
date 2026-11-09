---
symbol: "RN7SL2"
type: "gene"
col: 15805
ensembl_id: "ENSG00000274012"
name: "RNA component of signal recognition particle 7SL2"
location: "14q21.3"
module: 21
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# RN7SL2

*RNA component of signal recognition particle 7SL2* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.38× (z +11.2, q 3e-26, up in 10 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +3.4, q 0.051, up in 10 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 11.5×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RN7SL1]] (+0.91, fdr 7e-06), [[CTBP1-AS]] (+0.88, fdr 7e-06, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[ZRANB2-AS1]] (+0.87, fdr 7e-06), [[FAM217A]] (+0.85, fdr 7e-06); moves opposite to [[PRKDC]] (-0.65, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCDC144NL-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15805.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 11.5×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.38×** | +11.2 | 3e-26 | 10/10 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.46×** | +10.4 | 4e-23 | 5/5 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.63×** | +9.8 | 2e-20 | 1/1 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +5.6 | 2e-06 | 12/24 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.17×** | +5.1 | 3e-05 | 3/9 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +4.3 | 0.001 | 5/12 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.19×** | +4.0 | 0.006 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.44×** | +3.4 | 0.042 | 8/34 (A498, NCI-H1573, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.051 | 10/33 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.39× | +3.1 | 0.11 | 9/32 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.62× | +3.1 | 0.11 | 0/18 | inconsistent across doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.89× | +3.0 | 0.12 | 1/29 (HS-578T) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.860× | -3.6 | 0.17 | 22/47 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.593× | -3.3 | 0.29 | 13/41 (A498, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.35 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.5× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RN7SL1]] | +0.91 | +0.85 / +0.89 | both halves | 7e-06 | same gene group |
| [[CTBP1-AS]] ⚠ | +0.88 | +0.75 / +0.87 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZRANB2-AS1]] | +0.87 | +0.82 / +0.88 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.85 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | +0.84 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[KIZ-AS1]] ⚠ | +0.82 | +0.68 / +0.82 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[VPS39-DT]] | +0.81 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.81 | +0.69 / +0.84 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.80 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[RHOQ-AS1]] | +0.79 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.79 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.78 | +0.73 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144NL-1]] | B | CCDC144NL-1 activity raises RN7SL2's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 1.19× lower at baseline in the lines without CCDC144NL-1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[KIAA2012]] | C | KIAA2012 activity raises RN7SL2's level | lines that do not express KIAA2012 (3) vs lines expressing it (47) | 1.18× lower at baseline in the lines without KIAA2012 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OPN3, SMAD7, TESK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, 29.0); signed map (34.5, 6.1). **Vector** length 33.9, 3.03% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +9.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA component of signal recognition particle 7SL2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q21.3 — chr14:49,862,550-49,862,849 (-) |
| Ensembl biotype | misc_RNA |
| Also known as | 7SL1c, 7L30.1, RNSRP2 |
| Gene groups (HGNC) | Signal recognition particle; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [378706](https://www.ncbi.nlm.nih.gov/gene/378706):

> The signal recognition particle (SRP) is a cytoplasmic ribonucleoprotein complex that mediates cotranslational insertion of secretory proteins into the lumen of the endoplasmic reticulum. The SRP consists of 6 polypeptides (e.g., SRP19; MIM 182175) and a 7SL RNA molecule, such as RN7SL2, that is partially homologous to Alu DNA (Ullu and Weiner, 1984 [PubMed 6084597]).[supplied by OMIM, Jul 2008]

**Accessions** — [HGNC:23134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23134) · Entrez [378706](https://www.ncbi.nlm.nih.gov/gene/378706) · Ensembl [ENSG00000274012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274012)

## Data

Gene col 15805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15805); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15805]; `tensor/DDL_lfc|DDL_z.npy` [15805]; `embed/gene_vectors.npy` [15805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15805 or target_col == 15805). Every well: [[RN7SL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RN7SL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
