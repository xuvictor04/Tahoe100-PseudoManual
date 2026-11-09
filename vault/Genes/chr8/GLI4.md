---
symbol: "GLI4"
type: "gene"
col: 14703
ensembl_id: "ENSG00000250571"
name: "GLI family zinc finger 4"
location: "8q24.3"
module: 96
arm: "+"
pooled_cpm: 4.45
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# GLI4

*GLI family zinc finger 4* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.06× (z +6.7, q 1e-08, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.66× (z +4.9, q 3e-04, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -8.0, q 7e-13, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFRP1]] (+0.64, fdr 8e-06), [[PGGHG]] (+0.60, fdr 1e-05), [[LRRC14]] (+0.59, fdr 1e-05); moves opposite to [[LINC01019]] (-0.51, fdr 3e-05), [[NSD3]] (-0.45, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +6.7 | 1e-08 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +4.9 | 3e-04 | 12/46 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.5 | 0.001 | 12/33 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.60×** | +4.4 | 0.002 | 10/28 (PANC-1, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.043 | 10/44 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | 1.38× | +3.1 | 0.16 | 10/43 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.38× | +3.1 | 0.16 | 5/26 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -8.0 | 7e-13 | 29/46 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.573×** | -7.6 | 9e-12 | 28/38 (HS-578T, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.460×** | -7.5 | 1e-11 | 31/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.282×** | -6.4 | 3e-08 | 25/42 (HS-578T, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -5.8 | 6e-07 | 22/38 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.586×** | -5.2 | 2e-05 | 19/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -4.3 | 0.002 | 18/39 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.718× | -3.2 | 0.10 | 14/46 (BT-474, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.719× | -3.1 | 0.14 | 8/44 (HepG2/C3A, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.14 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0335× (z -10.8) |
| [[C-33 A (line)]] | alt | 5.88 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 5 µM 0.0413× (z -9.5) |
| [[HOP62 (line)]] | alt | 3.50 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0739× (z -9.2) |
| [[HS-578T (line)]] | alt | 5.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0829× (z -13.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HT-29 (line)]] | alt | 3.39 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0681× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 4.24 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0892× (z -8.6) |
| [[A-172 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFRP1]] | +0.64 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[PGGHG]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[LRRC14]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 | STRING 518 |
| [[OPLAH]] ⚠ | +0.59 | +0.54 / +0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UCKL1]] | +0.58 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PLA2G4B]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[NSMF]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[WDR6]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.56 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[EME2]] | +0.56 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[LZTR1]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TEPSIN]] | +0.55 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TAF1C]] | +0.55 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01019]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NSD3]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity lowers GLI4's level | compounds that target TOP1: 2 of 3 raise it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.6, -23.8); signed map (-27.4, 0.4). **Vector** length 40.6, 4.22% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +3.1 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.1 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.8 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +1.5 | +4.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.1 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -8.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.3 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -4.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | GLI family zinc finger 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,267,433-143,276,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HKR4, ZNF928 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

UniProt [P10075](https://www.uniprot.org/uniprotkb/P10075) carries no function annotation.

**Summary**, from NCBI Gene [2738](https://www.ncbi.nlm.nih.gov/gene/2738):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4320) · Entrez [2738](https://www.ncbi.nlm.nih.gov/gene/2738) · UniProt [P10075](https://www.uniprot.org/uniprotkb/P10075) · Ensembl [ENSG00000250571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250571)

## Data

Gene col 14703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14703); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14703]; `tensor/DDL_lfc|DDL_z.npy` [14703]; `embed/gene_vectors.npy` [14703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14703 or target_col == 14703). Every well: [[GLI4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLI4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
