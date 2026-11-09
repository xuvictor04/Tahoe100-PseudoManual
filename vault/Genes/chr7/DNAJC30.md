---
symbol: "DNAJC30"
type: "gene"
col: 10716
ensembl_id: "ENSG00000176410"
name: "DnaJ heat shock protein family (Hsp40) member C30"
location: "7q11.23"
module: 118
arm: "+"
pooled_cpm: 3.61
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# DNAJC30

*DnaJ heat shock protein family (Hsp40) member C30* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +9.0, q 9e-17, up in 24 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.595× (z -5.0, q 3e-04, down in 17 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0838×; ⚠ transcription drop; cell-cycle shift, explains ~17% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC3-AS1]] (+0.72, fdr 7e-06), [[CCDC142]] (+0.69, fdr 1e-05), [[TIMM8B]] (+0.67, fdr 1e-05); moves opposite to [[NCOR2]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[THBS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +9.0 | 9e-17 | 24/35 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +8.9 | 2e-16 | 4/11 (A498, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +7.8 | 1e-12 | 18/46 (A498, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.1 | 5e-05 | 13/30 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.8 | 2e-04 | 6/21 (NCI-H460, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.7 | 2e-04 | 1/6 (A498) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.6 | 3e-04 | 12/23 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.021 | 9/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.034 | 3/46 (A-427, NCI-H1792, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.37× | +3.1 | 0.12 | 6/37 (LS 180, RKO, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | 1.39× | +3.0 | 0.12 | 5/42 (J82, A-427, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.39× | +3.0 | 0.13 | 3/42 (HS-578T, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10716.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0838×; ⚠ transcription drop; cell-cycle shift, explains ~17% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.595×** | -5.0 | 3e-04 | 17/43 (KATO III, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -4.5 | 0.002 | 17/44 (H4, SNU-1, …) | two highest doses | position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.730× | -3.0 | 0.44 | 6/44 (NCI-H1792, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 6.19 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0838× (z -11.5) ⚠ transcription drop; cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC3-AS1]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[CCDC142]] | +0.69 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[TIMM8B]] | +0.67 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CNPY2-AS1]] | +0.67 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SP2-DT]] | +0.66 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[MED4]] | +0.66 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[FRS2]] | +0.65 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NGDN]] | +0.65 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[SCGB2B2]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TRUB2]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[EPM2AIP1]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD49]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOR2]] | -0.58 | -0.46 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS4]] | B | THBS4 activity lowers DNAJC30's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without THBS4 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DNAJC30's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers DNAJC30's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-47.7, 9.3); signed map (-5.0, -2.6). **Vector** length 41.4, 4.56% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.2 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +9.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.8 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,680,918-73,683,453 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously WBSCR18 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LL9](https://www.uniprot.org/uniprotkb/Q96LL9) (DnaJ homolog subfamily C member 30, mitochondrial):

> Mitochondrial protein enriched in neurons that acts as a regulator of mitochondrial respiration (By similarity). Associates with the ATP synthase complex and facilitates ATP synthesis (By similarity). May be a chaperone protein involved in the turnover of the subunits of mitochondrial complex I N-module. It facilitates the degradation of N-module subunits damaged by oxidative stress, and contributes to complex I functional efficiency.

**Summary**, from NCBI Gene [84277](https://www.ncbi.nlm.nih.gov/gene/84277):

> This intronless gene encodes a member of the DNAJ molecular chaperone homology domain-containing protein family. This gene is deleted in Williams syndrome, a multisystem developmental disorder caused by the deletion of contiguous genes at 7q11.23. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16410) · Entrez [84277](https://www.ncbi.nlm.nih.gov/gene/84277) · UniProt [Q96LL9](https://www.uniprot.org/uniprotkb/Q96LL9) · Ensembl [ENSG00000176410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176410)

## Data

Gene col 10716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10716); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10716]; `tensor/DDL_lfc|DDL_z.npy` [10716]; `embed/gene_vectors.npy` [10716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10716 or target_col == 10716). Every well: [[DNAJC30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
