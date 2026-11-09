---
symbol: "REX1BD"
type: "gene"
col: 97
ensembl_id: "ENSG00000006015"
name: "required for excision 1-B domain containing"
location: "19p13.11"
module: 58
arm: "+"
pooled_cpm: 9.43
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# REX1BD

*required for excision 1-B domain containing* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.22× (z +10.4, q 1e-22, up in 30 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.79× (z +4.2, q 0.003, up in 28 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 6.87×, A498 5.83×, LoVo 7.07×, LS 180 6.14×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 6.08×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.476× (z -7.6, q 2e-11, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGFL7]] (+0.68, fdr 7e-06), [[TMEM256]] (+0.64, fdr 1e-04), [[POP5]] (+0.63, fdr 1e-04); moves opposite to [[KLRA1P]] (-0.52, fdr 5e-05), [[ZNF34]] (-0.52, fdr 5e-05), [[SSU72]] (-0.50, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC39A4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 97.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 6.87×, A498 5.83×, LoVo 7.07×, LS 180 6.14×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 6.08×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.22×** | +10.4 | 1e-22 | 30/32 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +8.6 | 3e-15 | 17/18 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +6.0 | 4e-07 | 24/27 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +4.2 | 0.003 | 28/46 (COLO 205, A549, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.78×** | +4.2 | 0.003 | 21/40 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.53× | +3.1 | 0.21 | 18/47 (HEC-1-A, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 97.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.476×** | -7.6 | 2e-11 | 39/45 (Panc 03.27, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -5.1 | 9e-05 | 33/43 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.531×** | -4.3 | 0.003 | 26/47 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.331×** | -4.0 | 0.008 | 26/43 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -3.4 | 0.064 | 19/47 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 97. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.08× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -9.2) |
| [[A498 (line)]] | wt | 9.68 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.07× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 9.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -9.5) |
| [[SW480 (line)]] | alt | 9.38 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 97), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 21 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGFL7]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TMEM256]] | +0.64 | +0.35 / +0.74 | both halves | 1e-04 |  |
| [[POP5]] | +0.63 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[NDUFA11]] ⚠ | +0.62 | +0.29 / +0.71 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[C4orf48]] | +0.61 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[MICOS13]] | +0.60 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[POLR2J]] ⚠ | +0.60 | +0.22 / +0.68 | both halves | 6e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HACL1]] | +0.60 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[IFI27L2]] | +0.60 | +0.31 / +0.71 | both halves | 2e-04 |  |
| [[CHCHD5]] | +0.58 | +0.32 / +0.68 | both halves | 2e-04 |  |
| [[VEZT]] | +0.58 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[PSMB4]] | +0.57 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PCSK1N]] | +0.56 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SSNA1]] | +0.56 | +0.32 / +0.56 | both halves | 2e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRA1P]] | -0.52 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ZNF34]] | -0.52 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[SSU72]] | -0.50 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[RRH]] | -0.48 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[SMIM15-AS1]] | -0.47 | -0.39 / -0.29 | both halves | 3e-04 |  |
| [[PSMD6-AS1]] | -0.46 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[SRSF1]] | -0.46 | -0.23 / -0.49 | both halves | 5e-04 |  |
| [[ZNF460]] | -0.46 | -0.15 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[LINC01355]] | -0.46 | -0.18 / -0.50 | ⚠ not reproduced | 1e-03 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC39A4]] | B | SLC39A4 activity lowers REX1BD's level | lines that do not express SLC39A4 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without SLC39A4 | 0.047 | ⚠ within organs, on part of the lines; also absent: LRRC8B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.0, -18.4); signed map (-33.7, 6.5). **Vector** length 52.9, 9.79% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.9 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | required for excision 1-B domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,588,685-18,592,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20850, FLJ30108, FLJ34606, FLJ37391; previously C19orf60 |
| Matched by | ensembl_id |

UniProt [Q96EN9](https://www.uniprot.org/uniprotkb/Q96EN9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26098) · Entrez [55049](https://www.ncbi.nlm.nih.gov/gene/55049) · UniProt [Q96EN9](https://www.uniprot.org/uniprotkb/Q96EN9) · Ensembl [ENSG00000006015](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006015)

## Data

Gene col 97: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 97); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 97, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 97]; `tensor/DDL_lfc|DDL_z.npy` [97]; `embed/gene_vectors.npy` [97]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 97 or target_col == 97). Every well: [[REX1BD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REX1BD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
