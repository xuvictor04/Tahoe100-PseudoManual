---
symbol: "TSSC4"
type: "gene"
col: 11514
ensembl_id: "ENSG00000184281"
name: "tumor suppressing subtransferable candidate 4"
location: "11p15.5"
module: 7
arm: "+"
pooled_cpm: 5.88
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TSSC4

*tumor suppressing subtransferable candidate 4* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.56× (z +7.9, q 2e-12, up in 20 of 31 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.99× (z +6.0, q 3e-07, up in 25 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.688× (z -4.6, q 0.002, down in 18 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FEM1A]] (+0.76, fdr 7e-06), [[PSMD7]] (+0.75, fdr 7e-06), [[TMEM199]] (+0.73, fdr 7e-06); moves opposite to [[LYRM7]] (-0.61, fdr 3e-04), [[HDAC1]] (-0.59, fdr 3e-05), [[TWSG1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.56×** | +7.9 | 2e-12 | 20/31 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.69×** | +6.4 | 3e-08 | 22/39 (KATO III, C32, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **2.07×** | +6.4 | 4e-08 | 18/30 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +6.0 | 3e-07 | 25/39 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +5.5 | 5e-06 | 25/45 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.81×** | +5.2 | 2e-05 | 24/44 (PANC-1, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.2 | 2e-05 | 26/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.93×** | +4.9 | 6e-05 | 20/42 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.7 | 1e-04 | 22/41 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +4.6 | 3e-04 | 20/43 (PANC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.70×** | +4.4 | 5e-04 | 20/45 (HEC-1-A, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +4.3 | 9e-04 | 18/46 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.63×** | +4.1 | 0.002 | 0/9 | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.003 | 19/47 (Hs 766T, SW1417, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +3.8 | 0.005 | 18/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.27×** | +3.8 | 0.006 | 14/40 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.093 | 6/46 (SW480, A-427, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.688×** | -4.6 | 0.002 | 18/45 (A498, SW48, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.618×** | -4.1 | 0.014 | 16/42 (H4, A-172, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.641×** | -3.9 | 0.018 | 19/44 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.662×** | -3.6 | 0.041 | 8/47 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEM1A]] | +0.76 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[COMMD5]] | +0.73 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SMG8]] | +0.72 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.70 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[MRM3]] | +0.70 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.70 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.70 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[FAM32A]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYRM7]] | -0.61 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[HDAC1]] | -0.59 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TWSG1]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TSSC4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.8, 9.7); signed map (-4.7, -23.9). **Vector** length 59.9, 9.81% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.6 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tumor suppressing subtransferable candidate 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:2,400,488-2,403,878 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | U5 small nuclear ribonucleoprotein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5U2](https://www.uniprot.org/uniprotkb/Q9Y5U2) (U5 small nuclear ribonucleoprotein TSSC4):

> Protein associated with the U5 snRNP, during its maturation and its post-splicing recycling and which is required for spliceosomal tri-snRNP complex assembly in the nucleus. Has a molecular sequestering activity and transiently hinders SNRNP200 binding sites for constitutive splicing factors that intervene later during the assembly of the spliceosome and splicing. Together with its molecular sequestering activity, may also function as a molecular adapter and placeholder, coordinating the …

**Summary**, from NCBI Gene [10078](https://www.ncbi.nlm.nih.gov/gene/10078):

> This gene is one of several tumor-suppressing subtransferable fragments located in the imprinted gene domain of 11p15.5, an important tumor-suppressor gene region. Alterations in this region have been associated with the Beckwith-Wiedemann syndrome, Wilms tumor, rhabdomyosarcoma, adrenocortical carcinoma, and lung, ovarian, and breast cancer. This gene is located among several imprinted genes; however, this gene, as well as the pan-hematopoietic expression gene (PHEMX), escapes imprinting. This …

**Accessions** — [HGNC:12386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12386) · Entrez [10078](https://www.ncbi.nlm.nih.gov/gene/10078) · UniProt [Q9Y5U2](https://www.uniprot.org/uniprotkb/Q9Y5U2) · Ensembl [ENSG00000184281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184281)

## Data

Gene col 11514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11514); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11514]; `tensor/DDL_lfc|DDL_z.npy` [11514]; `embed/gene_vectors.npy` [11514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11514 or target_col == 11514). Every well: [[TSSC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSSC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
