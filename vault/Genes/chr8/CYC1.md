---
symbol: "CYC1"
type: "gene"
col: 10996
ensembl_id: "ENSG00000179091"
name: "cytochrome c1"
location: "8q24.3"
module: 58
arm: "+"
pooled_cpm: 32.19
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CYC1

*cytochrome c1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.33× (z +7.8, q 4e-12, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.329× (z -4.0, q 0.036, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 33 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCR10]] (+0.66, fdr 4e-05, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[KRTCAP2]] (+0.64, fdr 2e-05), [[MRPL12]] (+0.64, fdr 1e-05), [[ATP5MC1]] (+0.62, fdr 4e-05); moves opposite to [[CTTN]] (-0.61, fdr 3e-05), [[SNHG22]] (-0.58, fdr 2e-04), [[C8orf44-SGK3]] (-0.57, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.33×** | +7.8 | 4e-12 | 42/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.63×** | +6.4 | 5e-08 | 33/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.92×** | +4.5 | 0.002 | 36/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.99×** | +4.4 | 0.002 | 29/41 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.62× | +3.2 | 0.16 | 28/45 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.329×** | -4.0 | 0.036 | 34/45 (HOP62, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.360×** | -3.7 | 0.068 | 33/48 (LoVo, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.423× | -3.1 | 0.29 | 33/48 (LoVo, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.424× | -3.1 | 0.29 | 23/46 (SHP-77, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 22 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCR10]] ⚠ | +0.66 | +0.41 / +0.75 | both halves | 4e-05 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[KRTCAP2]] | +0.64 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[MRPL12]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 | STRING 653 |
| [[ATP5MC1]] | +0.62 | +0.41 / +0.74 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 947 |
| [[ATP5MF]] | +0.62 | +0.53 / +0.73 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 597 |
| [[ATP5PO]] ⚠ | +0.56 | +0.41 / +0.62 | both halves | 4e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 921; ⚠ in the vector space only through flagged drug-doses |
| [[TIMM17B]] ⚠ | +0.55 | +0.45 / +0.56 | both halves | 3e-05 | pathway: Mitochondrial protein import; STRING 703; ⚠ in the vector space only through flagged drug-doses |
| [[MRPL14]] | +0.54 | +0.19 / +0.60 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TMEM147]] | +0.54 | +0.29 / +0.66 | both halves | 2e-04 | pathway: Protein localization |
| [[TMEM205]] | +0.54 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[HSD17B10]] ⚠ | +0.54 | +0.48 / +0.59 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MC3]] ⚠ | +0.52 | +0.33 / +0.59 | both halves | 1e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 841; ⚠ in the vector space only through flagged drug-doses |
| [[DNPH1]] | +0.52 | +0.29 / +0.60 | both halves | 2e-04 |  |
| [[COX8A]] | +0.52 | +0.41 / +0.61 | both halves | 4e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 757 |
| [[YIF1A]] | +0.50 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[NUDT16L1]] | +0.50 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[NDUFA7]] | +0.50 | +0.27 / +0.62 | both halves | 3e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 936 |
| [[SAC3D1]] | +0.50 | +0.24 / +0.54 | both halves | 5e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTTN]] | -0.61 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[SNHG22]] | -0.58 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[C8orf44-SGK3]] | -0.57 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[ING4]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ZC3H3]] | -0.51 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[WDR45]] | -0.51 | -0.10 / -0.48 | ⚠ not reproduced | 0.003 |  |
| [[MTCH1]] | -0.51 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[EFCAB13-DT]] | -0.50 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[ERVK13-1]] | -0.50 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[ZNF514]] | -0.50 | -0.20 / -0.48 | both halves | 7e-04 |  |
| [[DYNLT2]] | -0.50 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[NPIPB2]] | -0.49 | -0.16 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[MTPN]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ANO7]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[DNAJB6]] | -0.48 | -0.31 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.7, -15.7); signed map (-38.1, -27.3). **Vector** length 55.3, 16.0% of its response variance represented; |z| ≥ 3 in 510 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.0 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.1 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -4.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -3.4 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -3.0 | +7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,095,039-144,097,525 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UQCR4 |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits; Apoptosome |
| Hallmark sets | ADIPOGENESIS, MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Complex III assembly; Mitochondrial protein import; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P08574](https://www.uniprot.org/uniprotkb/P08574) (Cytochrome c1, heme protein, mitochondrial):

> Component of the ubiquinol-cytochrome c oxidoreductase, a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular …

**Summary**, from NCBI Gene [1537](https://www.ncbi.nlm.nih.gov/gene/1537):

> This gene encodes a subunit of the cytochrome bc1 complex, which plays an important role in the mitochondrial respiratory chain by transferring electrons from the Rieske iron-sulfur protein to cytochrome c. Mutations in this gene may cause mitochondrial complex III deficiency, nuclear type 6. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:2579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2579) · Entrez [1537](https://www.ncbi.nlm.nih.gov/gene/1537) · UniProt [P08574](https://www.uniprot.org/uniprotkb/P08574) · Ensembl [ENSG00000179091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179091)

## Data

Gene col 10996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10996); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10996]; `tensor/DDL_lfc|DDL_z.npy` [10996]; `embed/gene_vectors.npy` [10996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10996 or target_col == 10996). Every well: [[CYC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
