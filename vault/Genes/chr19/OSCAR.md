---
symbol: "OSCAR"
type: "gene"
col: 10024
ensembl_id: "ENSG00000170909"
name: "osteoclast associated Ig-like receptor"
location: "19q13.42"
module: 21
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# OSCAR

*osteoclast associated Ig-like receptor* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.27× (z +9.1, q 5e-17, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +7.4, q 2e-11, up in 14 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.544× (z -4.9, q 6e-04, down in 19 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02755]] (+0.62, fdr 1e-05), [[LANCL1-AS1]] (+0.60, fdr 1e-05), [[COP1-DT]] (+0.60, fdr 1e-05); moves opposite to [[THEM6]] (-0.50, fdr 6e-05), [[PTGES2]] (-0.49, fdr 1e-04), [[RAPGEF5]] (-0.47, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +9.1 | 5e-17 | 2/2 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +7.7 | 4e-12 | 6/11 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +7.4 | 2e-11 | 14/31 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +6.0 | 4e-07 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.2 | 0.003 | 2/11 (MIA PaCa-2, LOX-IMVI) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.007 | 8/32 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.008 | 14/41 (Hs 766T, J82, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.62×** | +3.9 | 0.008 | 9/27 (LOX-IMVI, H4, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.5 | 0.025 | 2/9 (A498, SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +3.4 | 0.034 | 3/42 (MIA PaCa-2, A498, …) | top dose only | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.034 | 5/16 (LOX-IMVI, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.043 | 9/34 (A-172, HS-578T, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.2 | 0.050 | 5/25 (H4, CFPAC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.0 | 0.099 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -4.9 | 6e-04 | 19/38 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -4.4 | 0.003 | 13/41 (MIA PaCa-2, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -4.3 | 0.004 | 16/39 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.596×** | -4.2 | 0.005 | 16/41 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.612×** | -3.9 | 0.009 | 16/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.487× | -3.0 | 0.24 | 5/36 (NCI-H1792, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -13.3) |
| [[A-172 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.693 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.699 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.887 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.777 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.914 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.673 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.790 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.911 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02755]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LANCL1-AS1]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[COP1-DT]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[AQP4-AS1]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[C12orf40]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[IGF2BP2-AS1]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[HRG-AS1]] | +0.58 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[CFAP20DC-AS1]] | +0.57 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[A2ML1-AS1]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[HVCN1]] | +0.56 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[SPATA1]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[ZNF528-AS1]] | +0.55 | +0.35 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[PTGES2]] | -0.49 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[RAPGEF5]] | -0.47 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[CD24]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[POLR2E]] | -0.46 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises OSCAR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NHSL1-AS1]] | B | NHSL1-AS1 activity raises OSCAR's level | lines that do not express NHSL1-AS1 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without NHSL1-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: DLX2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.0, 24.5); signed map (31.9, 8.5). **Vector** length 44.2, 5.43% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +1.7 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +0.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +0.9 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.2 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[XRK3F2 (drug)]] 5 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | osteoclast associated Ig-like receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,094,668-54,102,692 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Immunoglobulin like domain containing |
| Reactome | 4 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYS5](https://www.uniprot.org/uniprotkb/Q8IYS5) (Osteoclast-associated immunoglobulin-like receptor):

> Regulator of osteoclastogenesis which plays an important bone-specific function in osteoclast differentiation.

**Summary**, from NCBI Gene [126014](https://www.ncbi.nlm.nih.gov/gene/126014):

> Osteoclasts are multinucleated cells that resorb bone and are essential for bone homeostasis. This gene encodes an osteoclast-associated receptor (OSCAR), which is a member of the leukocyte receptor complex protein family that plays critical roles in the regulation of both innate and adaptive immune responses. The encoded protein may play a role in oxidative stress-mediated atherogenesis as well as monocyte adhesion. Multiple alternatively spliced transcript variants encoding different isoforms …

**Accessions** — [HGNC:29960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29960) · Entrez [126014](https://www.ncbi.nlm.nih.gov/gene/126014) · UniProt [Q8IYS5](https://www.uniprot.org/uniprotkb/Q8IYS5) · Ensembl [ENSG00000170909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170909)

## Data

Gene col 10024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10024); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10024]; `tensor/DDL_lfc|DDL_z.npy` [10024]; `embed/gene_vectors.npy` [10024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10024 or target_col == 10024). Every well: [[OSCAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSCAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
