---
symbol: "LRRC51"
type: "gene"
col: 11493
ensembl_id: "ENSG00000184154"
name: "leucine rich repeat containing 51"
location: "11q13.4"
module: 10
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# LRRC51

*leucine rich repeat containing 51* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.03× (z +15.7, q 0e+00, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.41× (z +5.7, q 2e-06, up in 13 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.784× (z -4.1, q 0.027, down in 14 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRC3]] (+0.63, fdr 1e-05), [[CASC2]] (+0.59, fdr 1e-05), [[ZC2HC1C]] (+0.56, fdr 1e-05); moves opposite to [[LPCAT1]] (-0.58, fdr 1e-05), [[BICD2]] (-0.51, fdr 5e-05), [[TMEM120B]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.03×** | +15.7 | 0e+00 | 4/4 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.14×** | +15.4 | 0e+00 | 5/5 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +14.4 | 8e-45 | 16/19 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +5.7 | 2e-06 | 13/36 (AsPC-1, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.4 | 0.001 | 7/43 (NCI-H2030, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.2 | 0.003 | 6/20 (CFPAC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.6 | 0.028 | 1/8 (NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.043 | 8/40 (AsPC-1, A-427, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.49×** | +3.3 | 0.056 | 1/10 (A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.057 | 4/41 (HOP62, A-427, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.3 | 0.057 | 7/26 (NCI-H2030, Hs 766T, …) | top dose only | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -4.1 | 0.027 | 14/44 (KATO III, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -3.9 | 0.027 | 13/45 (HS-578T, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.750× | -3.4 | 0.13 | 11/31 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Ritonavir (drug)]] 5 µM |  | 0.835× | -3.0 | 0.34 | 7/42 (Hs 766T, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRC3]] | +0.63 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CASC2]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ZC2HC1C]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PDCL3P4]] | +0.55 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[COQ7]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[PHYH]] | +0.54 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[CENPS]] | +0.53 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.53 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[TMEM35B]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ALDH16A1]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[MUTYH]] | +0.52 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[ACAD9-DT]] | +0.52 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT1]] | -0.58 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[BICD2]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TMEM120B]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[HMOX2]] | -0.49 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[LPCAT4]] | -0.48 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[RPL27]] | -0.47 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[TBC1D2]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[RBAK-RBAKDN]] | -0.47 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[RGS10]] | -0.47 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[ANKRD27]] | -0.46 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[GNB1L]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[TMEM184B]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[SUCLG2-DT]] | B | SUCLG2-DT activity lowers LRRC51's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.88× higher at baseline in the lines without SUCLG2-DT | 0.087 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-28.6, 28.0); signed map (3.5, 5.1). **Vector** length 36.4, 3.58% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +15.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +0.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.8 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.8 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.6 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 51 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,080,337-72,096,895 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q96E66](https://www.uniprot.org/uniprotkb/Q96E66) carries no function annotation.

**Summary**, from NCBI Gene [120356739](https://www.ncbi.nlm.nih.gov/gene/120356739):

> This gene belongs to the leucine-rich repeat containing family. The encoded protein contains a transmembrane domain and two leucine-rich repeat domains. Unlike in mouse and other mammals, readthrough transcription is observed in primates between this gene and the adjacent transmembrane O-methyltransferase (Tomt) gene. Previously, this locus was annotated as a single gene representing the readthrough transcripts as well as the two different transcript species that encoded different proteins. It …

**Accessions** — [HGNC:55526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55526) · Entrez [120356739](https://www.ncbi.nlm.nih.gov/gene/120356739) · UniProt [Q96E66](https://www.uniprot.org/uniprotkb/Q96E66) · Ensembl [ENSG00000184154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184154)

## Data

Gene col 11493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11493); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11493]; `tensor/DDL_lfc|DDL_z.npy` [11493]; `embed/gene_vectors.npy` [11493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11493 or target_col == 11493). Every well: [[LRRC51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
