---
symbol: "SPIN2B"
type: "gene"
col: 11853
ensembl_id: "ENSG00000186787"
name: "spindlin family member 2B"
location: "Xp11.21"
module: 220
arm: "+"
pooled_cpm: 2.47
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# SPIN2B

*spindlin family member 2B* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.52× (z +7.5, q 5e-11, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.37× (z +3.7, q 0.061, up in 3 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.517× (z -5.6, q 1e-05, down in 17 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL22]] (+0.63, fdr 4e-05), [[FRG1GP]] (+0.57, fdr 5e-05), [[COA5]] (+0.56, fdr 1e-04); moves opposite to [[BZW1]] (-0.58, fdr 5e-05), [[IQGAP1]] (-0.53, fdr 5e-05), [[KPNA4]] (-0.52, fdr 1e-04).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +7.5 | 5e-11 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.061 | 3/44 (SHP-77, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +3.6 | 0.063 | 1/3 (A-172) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.5 | 0.063 | 3/15 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +3.4 | 0.063 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.3 | 0.085 | 9/46 (LS 180, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.517×** | -5.6 | 1e-05 | 17/43 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.576×** | -4.7 | 8e-04 | 15/45 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -4.3 | 0.003 | 20/28 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -4.1 | 0.007 | 13/46 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.639×** | -3.8 | 0.016 | 11/42 (KATO III, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 3.89 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0583× (z -8.5) |
| [[A-172 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.886 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL22]] | +0.63 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[FRG1GP]] | +0.57 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[COA5]] | +0.56 | +0.35 / +0.68 | both halves | 1e-04 |  |
| [[PPM1M]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[PKDCC]] | +0.55 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[NSUN5P1-1]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[C11orf1]] | +0.55 | +0.28 / +0.67 | both halves | 3e-04 |  |
| [[ZFAND2A-DT]] | +0.54 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[NSUN5P2-1]] ⚠ | +0.52 | +0.40 / +0.52 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RCHY1]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[GSEC]] | +0.50 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[TMEM218]] | +0.50 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[MRPL44]] | +0.50 | +0.27 / +0.57 | both halves | 3e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BZW1]] | -0.58 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[IQGAP1]] | -0.53 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[KPNA4]] | -0.52 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[TLN1]] | -0.49 | -0.20 / -0.60 | both halves | 7e-04 |  |
| [[AIDA]] | -0.47 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[CCDC200]] | -0.47 | -0.14 / -0.60 | ⚠ one half (not replicated) | 0.002 |  |
| [[MAPRE1]] | -0.46 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[TTL]] | -0.46 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[SEPTIN10]] | -0.46 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[CCDC47]] | -0.46 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[LAMC1]] | -0.45 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[DYNC1H1]] | -0.44 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[APLP2]] | -0.44 | -0.29 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SPIN2B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FRG1GP]] | B | FRG1GP activity raises SPIN2B's level | lines that do not express FRG1GP (28) vs lines expressing it (22) | 1.15× lower at baseline in the lines without FRG1GP | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: BAGE2, TPTE, CCDC144NL-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.0, 30.9); signed map (-23.6, -10.9). **Vector** length 33.2, 3.11% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.2 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.1 | -4.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | spindlin family member 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:57,118,551-57,121,548 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPIN-2, TDRD26 |
| Gene groups (HGNC) | Tudor domain containing; Spindlin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPZ2](https://www.uniprot.org/uniprotkb/Q9BPZ2) (Spindlin-2B):

> Involved in the regulation of cell cycle progression, this activity is related to the inhibition of apoptosis following the removal of essential growth factors. Exhibits H3K4me3-binding activity.

**Summary**, from NCBI Gene [474343](https://www.ncbi.nlm.nih.gov/gene/474343):

> Enables histone H3K4me3 reader activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be located in nucleus. Predicted to be active in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33147) · Entrez [474343](https://www.ncbi.nlm.nih.gov/gene/474343) · UniProt [Q9BPZ2](https://www.uniprot.org/uniprotkb/Q9BPZ2) · Ensembl [ENSG00000186787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186787)

## Data

Gene col 11853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11853); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11853]; `tensor/DDL_lfc|DDL_z.npy` [11853]; `embed/gene_vectors.npy` [11853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11853 or target_col == 11853). Every well: [[SPIN2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPIN2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
