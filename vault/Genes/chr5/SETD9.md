---
symbol: "SETD9"
type: "gene"
col: 7902
ensembl_id: "ENSG00000155542"
name: "SET domain containing 9"
location: "5q11.2"
module: 35
arm: "+"
pooled_cpm: 5.13
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# SETD9

*SET domain containing 9* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +12.9, q 3e-35, up in 33 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.0741×; ⚠ toxic); [[RMC-6236 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0742×); [[Penfluridol (drug)]] 0.5 µM in 1 line (SNU-423 0.0741×); [[Pimozide (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0802×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC2HC1C]] (+0.65, fdr 6e-05), [[KLRK1-AS1]] (+0.63, fdr 1e-04), [[SFRP4]] (+0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HSPA2-AS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +12.9 | 3e-35 | 33/40 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +11.7 | 3e-29 | 20/24 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +10.1 | 1e-21 | 11/14 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.5 | 3e-15 | 6/9 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +7.9 | 3e-13 | 18/27 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.53×** | +7.8 | 7e-13 | 18/41 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +7.0 | 2e-10 | 17/45 (A498, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +6.1 | 8e-08 | 13/27 (SW1417, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +6.0 | 1e-07 | 13/42 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.4 | 5e-06 | 14/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.2 | 0.001 | 6/20 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.1 | 0.002 | 8/32 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.003 | 11/40 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +3.5 | 0.019 | 9/39 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.034 | 7/45 (KATO III, PANC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.058 | 1/41 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7902.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.0741×; ⚠ toxic); [[RMC-6236 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0742×); [[Penfluridol (drug)]] 0.5 µM in 1 line (SNU-423 0.0741×); [[Pimozide (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0802×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fusidic acid (drug)]] 5 µM |  | 0.841× | -3.1 | 0.99 | 6/47 (PANC-1, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.04 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.116× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 6.21 | 0 | 1 | — | [[RMC-6236 (drug)]] 0.05 µM 0.0742× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 5.36 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0802× (z -9.0) |
| [[SNU-423 (line)]] | alt | 4.98 | 0 | 1 | — | [[Penfluridol (drug)]] 0.5 µM 0.0741× (z -10.3) |
| [[SW1417 (line)]] | alt | 6.34 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0741× (z -11.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 13 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC2HC1C]] | +0.65 | +0.68 / +0.39 | both halves | 6e-05 |  |
| [[KLRK1-AS1]] | +0.63 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[SFRP4]] | +0.62 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[NUTM2E]] | +0.62 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[SPEN-AS1]] | +0.61 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[OOEP]] | +0.61 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[C2CD5-AS1]] | +0.61 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PPP1R9A-AS1]] | +0.61 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[CHMP3-AS1]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[RBMS3-AS3]] | +0.60 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[MED28-DT]] | +0.60 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PIGP]] | +0.60 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSPA2-AS1]] | C | HSPA2-AS1's natural level weakens SETD9's drug response | HSPA2-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.23; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.6, 23.1); signed map (31.1, -2.5). **Vector** length 41.2, 4.26% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | +0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:56,909,260-56,925,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33648; previously C5orf35 |
| Gene groups (HGNC) | SET domain containing; Putative lysine methyltransferases |
| Reactome | 3 pathways, smallest: Regulation of TP53 Activity through Methylation; Regulation of TP53 Activity; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

UniProt [Q8NE22](https://www.uniprot.org/uniprotkb/Q8NE22) carries no function annotation.

**Summary**, from NCBI Gene [133383](https://www.ncbi.nlm.nih.gov/gene/133383):

> Predicted to enable lysine N-methyltransferase activity. Predicted to be involved in regulation of signal transduction by p53 class mediator. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28508) · Entrez [133383](https://www.ncbi.nlm.nih.gov/gene/133383) · UniProt [Q8NE22](https://www.uniprot.org/uniprotkb/Q8NE22) · Ensembl [ENSG00000155542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155542)

## Data

Gene col 7902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7902); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7902]; `tensor/DDL_lfc|DDL_z.npy` [7902]; `embed/gene_vectors.npy` [7902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7902 or target_col == 7902). Every well: [[SETD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
