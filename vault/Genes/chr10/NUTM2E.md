---
symbol: "NUTM2E"
type: "gene"
col: 13658
ensembl_id: "ENSG00000228570"
name: "NUT family member 2E"
location: "10q22.3"
module: 35
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# NUTM2E

*NUT family member 2E* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.80× (z +19.6, q 0e+00, up in 33 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (SNU-1 0.0889×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00863]] (+0.80, fdr 7e-06), [[ZC2HC1C]] (+0.78, fdr 7e-06), [[TMEM202-AS1]] (+0.77, fdr 1e-05); moves opposite to [[FBXW2]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.80×** | +19.6 | 0e+00 | 33/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.78×** | +19.6 | 0e+00 | 34/36 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.17×** | +11.5 | 2e-28 | 33/42 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +9.7 | 4e-20 | 12/18 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +9.6 | 6e-20 | 2/4 (CFPAC-1, PANC-1) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +9.0 | 2e-17 | 6/9 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +7.7 | 9e-13 | 19/33 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +7.5 | 6e-12 | 19/36 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +7.1 | 7e-11 | 18/46 (SNU-423, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.6 | 2e-09 | 9/22 (A549, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +5.3 | 7e-06 | 15/46 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.0 | 3e-05 | 17/36 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.8 | 8e-05 | 12/45 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.003 | 9/45 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.004 | 10/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.8 | 0.004 | 10/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.43×** | +3.4 | 0.020 | 4/29 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.020 | 11/46 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.025 | 8/44 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13658.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (SNU-1 0.0889×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.809× | -3.1 | 0.65 | 1/48 (PANC-1) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 0.747× | -3.0 | 0.65 | 7/27 (NCI-H2347, SNU-423, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 3.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 3.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 4.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +8.7) | — |
| [[LoVo (line)]] | wt | 4.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 3.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 3.93 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.0889× (z -8.5) |
| [[SW 900 (line)]] | alt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.30× (z +8.5) | — |
| [[A-172 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00863]] | +0.80 | +0.82 / +0.63 | both halves | 7e-06 |  |
| [[ZC2HC1C]] | +0.78 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.77 | +0.80 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.77 | +0.80 / +0.48 | both halves | 2e-05 |  |
| [[C11orf71]] | +0.76 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.76 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[LINC02951]] | +0.74 | +0.76 / +0.42 | both halves | 4e-05 |  |
| [[SPEN-AS1]] | +0.74 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[RBMS3-AS3]] | +0.74 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[PATL2]] | +0.74 | +0.82 / +0.46 | both halves | 2e-05 |  |
| [[WAC-AS1]] | +0.74 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[PIGP]] | +0.74 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.65 | -0.66 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NUTM2E's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises NUTM2E's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without PLS3-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.8, 21.1); signed map (30.6, -3.6). **Vector** length 56.8, 7.65% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +19.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +19.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.3 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | +5.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | +1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | NUT family member 2E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:79,826,739-79,850,878 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM22E |
| Matched by | ensembl_id |

UniProt [B1AL46](https://www.uniprot.org/uniprotkb/B1AL46) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23448) · Entrez [283008](https://www.ncbi.nlm.nih.gov/gene/283008) · UniProt [B1AL46](https://www.uniprot.org/uniprotkb/B1AL46) · Ensembl [ENSG00000228570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228570)

## Data

Gene col 13658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13658); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13658]; `tensor/DDL_lfc|DDL_z.npy` [13658]; `embed/gene_vectors.npy` [13658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13658 or target_col == 13658). Every well: [[NUTM2E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUTM2E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
