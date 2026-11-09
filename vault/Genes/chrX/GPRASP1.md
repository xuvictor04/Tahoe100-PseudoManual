---
symbol: "GPRASP1"
type: "gene"
col: 12745
ensembl_id: "ENSG00000198932"
name: "G protein-coupled receptor associated sorting protein 1"
location: "Xq22.1"
module: 23
arm: "+"
pooled_cpm: 2.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# GPRASP1

*G protein-coupled receptor associated sorting protein 1* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +7.9, q 2e-12, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.464× (z -6.1, q 5e-07, down in 18 of 42 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMCX5-GPRASP2]] (+0.81, fdr 7e-06, ⚠ read-through risk), [[NPR2]] (+0.68, fdr 1e-05), [[GPRASP3]] (+0.68, fdr 1e-05), [[PPP1R3F]] (+0.65, fdr 1e-04); moves opposite to [[DHTKD1]] (-0.63, fdr 5e-05), [[SPTLC2]] (-0.59, fdr 2e-04), [[CMC2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01535]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RRN3P1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +7.9 | 2e-12 | 19/34 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.70×** | +6.0 | 7e-07 | 5/45 (PANC-1, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +5.7 | 2e-06 | 13/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +4.8 | 2e-04 | 10/30 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.3 | 0.002 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.004 | 15/42 (PANC-1, A498, …) | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.060 | 4/19 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.093 | 5/32 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.46× | +3.0 | 0.17 | 3/44 (NCI-H23, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.464×** | -6.1 | 5e-07 | 18/42 (H4, C-33 A, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.502×** | -5.5 | 9e-06 | 17/44 (hTERT-HPNE, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.653× | -3.4 | 0.12 | 13/46 (SW480, H4, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.688× | -3.0 | 0.38 | 11/46 (SNU-1, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.871 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.752 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.607 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX5-GPRASP2]] | +0.81 | +0.80 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of ARMCX5-GPRASP2 on the same strand (can correlate by spillover, not regulation) |
| [[NPR2]] | +0.68 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[GPRASP3]] | +0.68 | +0.69 / +0.57 | both halves | 1e-05 | same gene group |
| [[PPP1R3F]] | +0.65 | +0.64 / +0.33 | both halves | 1e-04 |  |
| [[DTX3]] | +0.65 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[AGER]] | +0.64 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[OXA1L-DT]] | +0.64 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[MYL5]] | +0.64 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[LINC00240]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[SPTY2D1OS]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ITFG2-AS1]] | +0.63 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[NSMCE1-DT]] | +0.62 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[CCDC17]] | +0.62 | +0.66 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHTKD1]] | -0.63 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[SPTLC2]] | -0.59 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[CMC2]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[L2HGDH]] | -0.57 | -0.55 / -0.20 | both halves | 7e-04 |  |
| [[NHP2]] | -0.57 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[KIAA1958]] | -0.57 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CARHSP1]] | -0.56 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[ABHD12]] | -0.56 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[LSM4]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[TSEN54]] | -0.55 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[KIAA1328]] | -0.55 | -0.52 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01535]] | B | LINC01535 activity raises GPRASP1's level | lines that do not express LINC01535 (21) vs lines expressing it (29) | 1.40× lower at baseline in the lines without LINC01535 | 0.027 | ⚠ within organs, on part of the lines; also absent: MIR3681HG, AFF3, KCNJ6 |
| [[HDAC6]] | B | HDAC6 activity raises GPRASP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRN3P1]] | C | GPRASP1's natural level weakens RRN3P1's drug response | GPRASP1's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.73, reverse +0.11; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-2.7, 17.1); signed map (16.4, -13.7). **Vector** length 46.5, 5.14% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.6 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.2 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.0 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.6 | -6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.2 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor associated sorting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:102,651,092-102,659,083 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GASP, GASP1 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JY77](https://www.uniprot.org/uniprotkb/Q5JY77) (G protein-coupled receptor-associated sorting protein 1):

> Modulates lysosomal sorting and functional down-regulation of a variety of G protein-coupled receptors. Targets receptors for degradation in lysosomes via its interaction with BECN2.

**Summary**, from NCBI Gene [9737](https://www.ncbi.nlm.nih.gov/gene/9737):

> This gene encodes a member of the GPRASP (G protein-coupled receptor associated sorting protein) family. The protein may modulate lysosomal sorting and functional down-regulation of a variety of G-protein coupled receptors. It targets receptors for degradation in lysosomes. The receptors interacting with this sorting protein include D2 dopamine receptor (DRD2), delta opioid receptor (OPRD1), beta-2 adrenergic receptor (ADRB2), D4 dopamine receptor (DRD4) and cannabinoid 1 receptor (CB1R). …

**Accessions** — [HGNC:24834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24834) · Entrez [9737](https://www.ncbi.nlm.nih.gov/gene/9737) · UniProt [Q5JY77](https://www.uniprot.org/uniprotkb/Q5JY77) · Ensembl [ENSG00000198932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198932)

## Data

Gene col 12745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12745); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12745]; `tensor/DDL_lfc|DDL_z.npy` [12745]; `embed/gene_vectors.npy` [12745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12745 or target_col == 12745). Every well: [[GPRASP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRASP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
