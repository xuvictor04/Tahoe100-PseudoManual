---
symbol: "TMEM11"
type: "gene"
col: 10917
ensembl_id: "ENSG00000178307"
name: "transmembrane protein 11"
location: "17p11.2"
module: 119
arm: "+"
pooled_cpm: 12.94
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# TMEM11

*transmembrane protein 11* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.97× (z +10.3, q 6e-22, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.537× (z -9.1, q 4e-17, down in 26 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.749× (z -6.0, q 5e-07, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTF1]] (+0.74, fdr 7e-06), [[C16orf91]] (+0.74, fdr 1e-05), [[MIEF1]] (+0.74, fdr 7e-06).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.97×** | +10.3 | 6e-22 | 44/48 (SW480, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.10×** | +8.4 | 1e-14 | 32/43 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.9 | 8e-07 | 29/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +5.6 | 3e-06 | 23/48 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.1 | 4e-05 | 19/40 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 2e-04 | 14/47 (HOP62, SW 900, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.4 | 9e-04 | 2/48 (hTERT-HPNE, C-33 A) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.004 | 15/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +4.0 | 0.004 | 18/44 (LS 180, A549, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.6 | 0.021 | 7/22 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.25×** | +3.3 | 0.059 | 12/46 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -9.1 | 4e-17 | 26/36 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.749×** | -6.0 | 5e-07 | 28/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.754×** | -4.2 | 0.006 | 21/46 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.833×** | -3.8 | 0.019 | 19/48 (RPMI-7951, LS 180, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.024 | 16/47 (A498, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.5 | 0.047 | 13/46 (SK-MEL-2, A498, …) | top dose only | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.810× | -3.1 | 0.15 | 13/47 (MIA PaCa-2, Hs 766T, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 9.57 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.5 µM 0.171× (z -9.0) |
| [[KATO III (line)]] | alt | 23.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.67× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0686× (z -21.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -9.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.158× (z -9.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[LoVo (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 8.35 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTF1]] | +0.74 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[C16orf91]] | +0.74 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[MIEF1]] | +0.74 | +0.62 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SCNM1]] | +0.73 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[BRPF1]] | +0.72 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[TOMM70]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[BFAR]] | +0.72 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[MRPL10]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SDHAF1]] | +0.70 | +0.50 / +0.81 | both halves | 1e-05 |  |
| [[KTI12]] | +0.70 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.69 | +0.39 / +0.74 | both halves | 6e-05 |  |
| [[POP7]] | +0.69 | +0.53 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TMEM11's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.841). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.3, -8.5); signed map (-11.6, -10.6). **Vector** length 68.2, 11.7% of its response variance represented; |z| ≥ 3 in 689 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.4 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.0 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +4.7 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.2 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.0 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.5 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +1.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | +0.0 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Elagolix sodium (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:21,197,954-21,214,176 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMI, PM1; previously C17orf35 |
| Reactome | 3 pathways, smallest: Cristae formation; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [P17152](https://www.uniprot.org/uniprotkb/P17152) (Transmembrane protein 11, mitochondrial):

> Plays a role in mitochondrial morphogenesis.

**Summary**, from NCBI Gene [8834](https://www.ncbi.nlm.nih.gov/gene/8834):

> Involved in mitochondrion organization. Located in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16823) · Entrez [8834](https://www.ncbi.nlm.nih.gov/gene/8834) · UniProt [P17152](https://www.uniprot.org/uniprotkb/P17152) · Ensembl [ENSG00000178307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178307)

## Data

Gene col 10917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10917); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10917]; `tensor/DDL_lfc|DDL_z.npy` [10917]; `embed/gene_vectors.npy` [10917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10917 or target_col == 10917). Every well: [[TMEM11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
