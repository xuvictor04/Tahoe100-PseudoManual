---
symbol: "LRRC14"
type: "gene"
col: 8400
ensembl_id: "ENSG00000160959"
name: "leucine rich repeat containing 14"
location: "8q24.3"
module: 7
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# LRRC14

*leucine rich repeat containing 14* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.13× (z +7.7, q 1e-11, up in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.44× (z +3.6, q 0.024, up in 5 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.658× (z -4.3, q 0.009, down in 15 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.0898×); [[Vilanterol (drug)]] 0.05 µM in 1 line (LS 180 0.0589×); [[(S)-Crizotinib (drug)]] 5 µM in 1 line (A549 0.0663×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL20-AS1]] (+0.68, fdr 7e-06), [[ASB6]] (+0.64, fdr 2e-05), [[BORCS8]] (+0.63, fdr 7e-06); moves opposite to [[PREPL]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.13×** | +7.7 | 1e-11 | 30/46 (RKO, AsPC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.15×** | +7.4 | 3e-11 | 2/6 (J82, NCI-H2347) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.03×** | +7.1 | 2e-10 | 25/43 (AsPC-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.85×** | +6.2 | 8e-08 | 17/45 (SW480, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.53×** | +6.1 | 1e-07 | 13/34 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.93×** | +5.6 | 2e-06 | 3/9 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.024 | 5/44 (LS 180, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.44×** | +3.5 | 0.030 | 9/26 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.42×** | +3.4 | 0.044 | 9/33 (SW480, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.096 | 10/35 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.097 | 6/45 (SW1417, SNU-423, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.097 | 5/23 (LoVo, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.78× | +3.0 | 0.10 | 2/10 (NCI-H2030, NCI-H1573) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8400.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.0898×); [[Vilanterol (drug)]] 0.05 µM in 1 line (LS 180 0.0589×); [[(S)-Crizotinib (drug)]] 5 µM in 1 line (A549 0.0663×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.658×** | -4.3 | 0.009 | 15/42 (SK-MEL-2, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **0.701×** | -3.7 | 0.064 | 12/35 (A-172, Hs 766T, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.02 | 0 | 1 | — | [[(S)-Crizotinib (drug)]] 5 µM 0.0663× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 3.55 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0959× (z -9.2) |
| [[HS-578T (line)]] | alt | 5.35 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0898× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 5.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 4.07 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0589× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 3.31 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0851× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.44 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.168× (z -8.5) |
| [[A-172 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL20-AS1]] | +0.68 | +0.76 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ASB6]] | +0.64 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[BORCS8]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TMEM115]] | +0.63 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[PIGQ]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[FLAD1]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[EMC8]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CPTP]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[IPO13]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[GLI4]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 | STRING 518 |
| [[DOLPP1]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[TPGS1]] | +0.58 | +0.59 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PREPL]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 | STRING 428 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRRC14's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.1, -0.7); signed map (-6.0, -27.2). **Vector** length 43.6, 4.82% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.1 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.8 | +3.6 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.8 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,517,992-144,525,172 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0014, LRRC14A |
| Reactome | 23 pathways, smallest: Regulation of NF-kappa B signaling; TAK1-dependent IKK and NF-kappa-B activation; MyD88 cascade initiated on plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15048](https://www.uniprot.org/uniprotkb/Q15048) (Leucine-rich repeat-containing protein 14):

> Negatively regulates Toll-like receptor-mediated NF-kappa-B signaling by disrupting IKK core complex formation through interaction with IKBKB.

**Summary**, from NCBI Gene [9684](https://www.ncbi.nlm.nih.gov/gene/9684):

> This gene encodes a leucine-rich repeat-containing protein. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:20419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20419) · Entrez [9684](https://www.ncbi.nlm.nih.gov/gene/9684) · UniProt [Q15048](https://www.uniprot.org/uniprotkb/Q15048) · Ensembl [ENSG00000160959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160959)

## Data

Gene col 8400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8400); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8400]; `tensor/DDL_lfc|DDL_z.npy` [8400]; `embed/gene_vectors.npy` [8400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8400 or target_col == 8400). Every well: [[LRRC14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
