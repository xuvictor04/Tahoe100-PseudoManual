---
symbol: "GRHPR"
type: "gene"
col: 5970
ensembl_id: "ENSG00000137106"
name: "glyoxylate and hydroxypyruvate reductase"
location: "9p13.2"
module: 33
arm: "+"
pooled_cpm: 21.25
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# GRHPR

*glyoxylate and hydroxypyruvate reductase* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.53× (z +11.1, q 5e-26, up in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.45× (z +4.5, q 1e-03, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.782× (z -4.2, q 0.017, down in 23 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.203×, MIA PaCa-2 0.362×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLMH]] (+0.67, fdr 1e-05), [[PACSIN3]] (+0.65, fdr 1e-05), [[RPUSD3]] (+0.63, fdr 1e-05); moves opposite to [[TSBP1-AS1]] (-0.52, fdr 9e-05), [[ARL5B]] (-0.51, fdr 3e-05), [[LINC01135]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +11.1 | 5e-26 | 37/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.94×** | +7.6 | 7e-12 | 19/30 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.2 | 1e-07 | 23/39 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +5.9 | 6e-07 | 32/44 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 1e-03 | 24/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.003 | 22/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.049 | 21/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.2 | 0.090 | 16/43 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | 1.31× | +3.1 | 0.12 | 18/47 (C32, NCI-H1573, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.68× | +3.1 | 0.12 | 8/44 (SNU-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 1.78× | +3.0 | 0.12 | 9/44 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5970.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.203×, MIA PaCa-2 0.362×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.782×** | -4.2 | 0.017 | 23/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.754× | -3.4 | 0.20 | 18/48 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.762× | -3.3 | 0.20 | 17/47 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.770× | -3.1 | 0.20 | 12/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.552× | -3.1 | 0.20 | 11/45 (A-427, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.0) |
| [[PANC-1 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.3) |
| [[A-427 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLMH]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PACSIN3]] | +0.65 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RPUSD3]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[NT5C3B]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CUEDC2]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[NEIL2]] | +0.61 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[ZNF74]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MRPL4]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[FAM241B]] | +0.60 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[METTL5]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[MYG1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[RPP40]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSBP1-AS1]] | -0.52 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[ARL5B]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[LINC01135]] | -0.48 | -0.28 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers GRHPR's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-44.5, -7.3); signed map (-16.6, -25.5). **Vector** length 51.8, 8.96% of its response variance represented; |z| ≥ 3 in 498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | glyoxylate and hydroxypyruvate reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,422,666-37,436,990 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PH2; previously GLXR, GLYD |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM, HYPOXIA |
| Reactome | 2 pathways, smallest: Glyoxylate metabolism and glycine degradation; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBQ7](https://www.uniprot.org/uniprotkb/Q9UBQ7) (Glyoxylate reductase/hydroxypyruvate reductase):

> Enzyme with hydroxy-pyruvate reductase, glyoxylate reductase and D-glycerate dehydrogenase enzymatic activities. Reduces hydroxypyruvate to D-glycerate, glyoxylate to glycolate, oxidizes D-glycerate to hydroxypyruvate.

**Summary**, from NCBI Gene [9380](https://www.ncbi.nlm.nih.gov/gene/9380):

> This gene encodes an enzyme with hydroxypyruvate reductase, glyoxylate reductase, and D-glycerate dehydrogenase enzymatic activities. The enzyme has widespread tissue expression and has a role in metabolism. Type II hyperoxaluria is caused by mutations in this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4570) · Entrez [9380](https://www.ncbi.nlm.nih.gov/gene/9380) · UniProt [Q9UBQ7](https://www.uniprot.org/uniprotkb/Q9UBQ7) · Ensembl [ENSG00000137106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137106)

## Data

Gene col 5970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5970); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5970]; `tensor/DDL_lfc|DDL_z.npy` [5970]; `embed/gene_vectors.npy` [5970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5970 or target_col == 5970). Every well: [[GRHPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRHPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
