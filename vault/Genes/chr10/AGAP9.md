---
symbol: "AGAP9"
type: "gene"
col: 12823
ensembl_id: "ENSG00000204172"
name: "ArfGAP with GTPase domain, ankyrin repeat and PH domain 9"
location: "10q11.22"
module: 28
arm: "+"
pooled_cpm: 7.42
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AGAP9

*ArfGAP with GTPase domain, ankyrin repeat and PH domain 9* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.32× (z +4.4, q 0.006, up in 9 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.865× (z -8.1, q 3e-13, down in 12 of 45 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.712× (z -5.4, q 1e-05, down in 13 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGAP13P]] (+0.70, fdr 7e-06), [[BMS1P1-1]] (+0.60, fdr 1e-05), [[BMS1P4-1]] (+0.57, fdr 2e-05); moves opposite to [[ITGA7]] (-0.49, fdr 1e-04), [[DVL2]] (-0.47, fdr 8e-05), [[TGFB1]] (-0.46, fdr 5e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TGFB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 0.006 | 9/44 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.1 | 0.010 | 7/36 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.22× | +3.1 | 0.27 | 3/44 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.27 | 3/44 (COLO 205, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.865× | -8.1 | 3e-13 | 12/45 (SNU-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.681×** | -6.1 | 2e-07 | 19/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.712×** | -5.4 | 1e-05 | 13/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.1 | 5e-05 | 17/40 (SK-MEL-2, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.3 | 0.002 | 10/44 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.782×** | -3.8 | 0.014 | 9/33 (SK-MEL-2, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Allantoin (drug)]] 0.5 µM |  | **0.779×** | -3.6 | 0.027 | 10/43 (RPMI-7951, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.067 | 9/42 (HS-578T, NCI-H1573, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.17 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0881× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[COLO 205 (line)]] | alt | 8.91 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0788× (z -8.8) |
| [[HOP62 (line)]] | alt | 7.18 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[NCI-H2030 (line)]] | alt | 8.03 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.131× (z -10.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 6.52 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0825× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 9.05 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -8.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0792× (z -9.1) |
| [[SNU-423 (line)]] | alt | 3.78 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 5 µM 0.0692× (z -8.9) |
| [[SW480 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP13P]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 | same gene group |
| [[BMS1P1-1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[BMS1P4-1]] | +0.57 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[FAN1]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ICE2]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ERMARD]] | +0.53 | +0.55 / +0.43 | both halves | 4e-05 |  |
| [[AGAP5]] | +0.53 | +0.59 / +0.46 | both halves | 3e-05 | same gene group; STRING 445 |
| [[ZNF18]] | +0.50 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[RPAP2]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ABRAXAS2]] | +0.50 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[DPP8]] | +0.49 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[SPG11]] | +0.49 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA7]] | -0.49 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[DVL2]] | -0.47 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[TGFB1]] | -0.46 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[IGF1R]] | -0.46 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[PHF13]] | -0.46 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[NPTN]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[KREMEN2]] | -0.45 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[MEF2D]] | -0.44 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[BBS9]] | -0.44 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[ZMIZ1]] | -0.43 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[CTBP2]] | -0.42 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[NLGN2]] | -0.42 | -0.39 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFB1]] | B | TGFB1 activity raises AGAP9's level | lines that do not express TGFB1 (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without TGFB1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZDHHC2, NUAK1, SLC22A4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.4, 21.3); signed map (18.2, -44.8). **Vector** length 38.4, 3.73% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.8 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.7 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.6 | -1.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +0.6 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -5.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with GTPase domain, ankyrin repeat and PH domain 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:47,501,854-47,523,638 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA301J7.2, FLJ00312; previously CTGLF6 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VTM2](https://www.uniprot.org/uniprotkb/Q5VTM2) (Arf-GAP with GTPase, ANK repeat and PH domain-containing protein 9):

> Putative GTPase-activating protein.

**Summary**, from NCBI Gene [642517](https://www.ncbi.nlm.nih.gov/gene/642517):

> Predicted to enable GTPase activator activity and GTPase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23463) · Entrez [642517](https://www.ncbi.nlm.nih.gov/gene/642517) · UniProt [Q5VTM2](https://www.uniprot.org/uniprotkb/Q5VTM2) · Ensembl [ENSG00000204172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204172)

## Data

Gene col 12823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12823); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12823]; `tensor/DDL_lfc|DDL_z.npy` [12823]; `embed/gene_vectors.npy` [12823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12823 or target_col == 12823). Every well: [[AGAP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGAP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
