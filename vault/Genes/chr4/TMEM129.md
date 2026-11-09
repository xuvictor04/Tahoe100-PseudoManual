---
symbol: "TMEM129"
type: "gene"
col: 9726
ensembl_id: "ENSG00000168936"
name: "transmembrane protein 129, E3 ubiquitin ligase"
location: "4p16.3"
module: 11
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TMEM129

*transmembrane protein 129, E3 ubiquitin ligase* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.01× (z +9.7, q 2e-19, up in 8 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +6.1, q 2e-07, up in 19 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.492× (z -6.5, q 5e-08, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPLA4]] (+0.63, fdr 1e-05), [[RNF135]] (+0.62, fdr 1e-05), [[OXLD1]] (+0.61, fdr 1e-05); moves opposite to [[ABAT]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRRC34]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +9.7 | 2e-19 | 8/8 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.5 | 5e-15 | 18/26 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.1 | 2e-07 | 19/39 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +6.0 | 3e-07 | 11/17 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.5 | 9e-04 | 14/32 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.012 | 11/45 (CFPAC-1, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.8 | 0.013 | 14/29 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.045 | 11/38 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.2 | 0.100 | 11/41 (A498, H4, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.14 | 11/40 (SW480, H4, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -6.5 | 5e-08 | 31/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -6.4 | 5e-08 | 28/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.512×** | -5.8 | 1e-06 | 24/42 (HT-29, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.551×** | -5.4 | 7e-06 | 23/46 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.683×** | -4.9 | 9e-05 | 23/40 (Hs 766T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.590×** | -4.8 | 1e-04 | 18/44 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -4.8 | 1e-04 | 18/39 (HT-29, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -4.8 | 1e-04 | 23/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.314×** | -4.3 | 0.001 | 20/41 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.619×** | -4.2 | 0.001 | 18/41 (NCI-H2030, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.719× | -3.0 | 0.13 | 14/47 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 4.82 | 0 | 3 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0953× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 5.35 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0613× (z -11.5) |
| [[Hs 766T (line)]] | wt | 5.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -11.6) |
| [[HT-29 (line)]] | alt | 6.47 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0914× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 3.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0928× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 5.92 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.163× (z -9.5) |
| [[SW480 (line)]] | alt | 5.65 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.180× (z -8.6) |
| [[A-172 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPLA4]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[RNF135]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | same gene group |
| [[OXLD1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[RCHY1]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZNF330]] | +0.58 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ACOT2]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[HOXA10-AS]] | +0.56 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TMEM250]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PCMTD1-DT]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ENDOG]] | +0.55 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[CZIB]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SCGB2B2]] | +0.54 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABAT]] | -0.46 | -0.38 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC34]] | B | LRRC34 activity lowers TMEM129's level | lines that do not express LRRC34 (20) vs lines expressing it (30) | 1.26× higher at baseline in the lines without LRRC34 | 0.066 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises TMEM129's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.314). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.5, 24.1); signed map (-9.2, -5.8). **Vector** length 47.7, 6.72% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.7 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 129, E3 ubiquitin ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,715,952-1,721,358 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D4S2561E |
| Gene groups (HGNC) | E3 ubiquitin ligases; RING finger E3 ubiquitin protein ligases |
| Reactome | 2 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [A0AVI4](https://www.uniprot.org/uniprotkb/A0AVI4) (E3 ubiquitin-protein ligase TM129):

> E3 ubiquitin-protein ligase involved in ER-associated protein degradation, preferentially associates with the E2 enzyme UBE2J2. Exploited by viral US11 proteins to mediate HLA class I proteins degradation.

**Summary**, from NCBI Gene [92305](https://www.ncbi.nlm.nih.gov/gene/92305):

> Enables ubiquitin protein ligase activity. Involved in protein polyubiquitination; retrograde protein transport, ER to cytosol; and ubiquitin-dependent protein catabolic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25137) · Entrez [92305](https://www.ncbi.nlm.nih.gov/gene/92305) · UniProt [A0AVI4](https://www.uniprot.org/uniprotkb/A0AVI4) · Ensembl [ENSG00000168936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168936)

## Data

Gene col 9726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9726); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9726]; `tensor/DDL_lfc|DDL_z.npy` [9726]; `embed/gene_vectors.npy` [9726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9726 or target_col == 9726). Every well: [[TMEM129 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM129.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
