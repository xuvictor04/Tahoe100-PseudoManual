---
symbol: "RPP38"
type: "gene"
col: 7632
ensembl_id: "ENSG00000152464"
name: "ribonuclease P/MRP subunit p38"
location: "10p13"
module: 11
arm: "+"
pooled_cpm: 16.47
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RPP38

*ribonuclease P/MRP subunit p38* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.53× (z +12.3, q 4e-32, up in 40 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0742×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SHP-77 0.118×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.265×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.117×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL14EP]] (+0.84, fdr 7e-06), [[ABRAXAS2]] (+0.79, fdr 7e-06), [[ERCC4]] (+0.77, fdr 7e-06); moves opposite to [[HDAC1]] (-0.69, fdr 1e-05), [[QSOX1]] (-0.65, fdr 1e-05), [[IGSF8]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RPP25]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.53×** | +12.3 | 4e-32 | 40/45 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +10.2 | 6e-22 | 41/46 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.20×** | +10.1 | 1e-21 | 39/46 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +9.9 | 5e-21 | 34/40 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +7.8 | 1e-12 | 28/47 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.4 | 1e-11 | 31/46 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +6.1 | 1e-07 | 30/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.1 | 3e-05 | 12/28 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.3 | 1e-03 | 18/46 (HT-29, RPMI-7951, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.32×** | +3.7 | 0.013 | 16/42 (SW480, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.038 | 13/47 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.040 | 15/47 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.043 | 19/48 (A-172, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.043 | 11/47 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.043 | 14/48 (RKO, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.078 | 14/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0742×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SHP-77 0.118×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.265×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.117×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 2 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0742× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 14.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.2) | — |
| [[A-427 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.11× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.91× (z +8.5) | — |
| [[KATO III (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.5) | — |
| [[LoVo (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.75× (z +9.3) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.118× (z -9.9) |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.117× (z -8.8) |
| [[SW 900 (line)]] | alt | 9.43 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.43× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL14EP]] | +0.84 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.77 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[NME6]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 | STRING 976 |
| [[UTP3]] | +0.76 | +0.80 / +0.66 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 853 |
| [[ZNF830]] | +0.76 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.76 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[PPCS]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[RDH14]] | +0.75 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[POLR3C]] | +0.75 | +0.73 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC1]] | -0.69 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.65 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.64 | -0.71 / -0.36 | both halves | 1e-04 |  |
| [[TSPAN13]] | -0.64 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPP25]] | B | RPP25 activity raises RPP38's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without RPP25 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.878). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.3, 6.2); signed map (1.6, -20.3). **Vector** length 87.2, 18.1% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +12.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.5 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.4 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease P/MRP subunit p38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:15,097,180-15,139,818 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Reactome | 6 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P78345](https://www.uniprot.org/uniprotkb/P78345) (Ribonuclease P protein subunit p38):

> Component of ribonuclease P, a ribonucleoprotein complex that generates mature tRNA molecules by cleaving their 5'-ends. Also a component of the MRP ribonuclease complex, which cleaves pre-rRNA sequences.

**Summary**, from NCBI Gene [10557](https://www.ncbi.nlm.nih.gov/gene/10557):

> Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Located in nucleolus. Part of multimeric ribonuclease P complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30329) · Entrez [10557](https://www.ncbi.nlm.nih.gov/gene/10557) · UniProt [P78345](https://www.uniprot.org/uniprotkb/P78345) · Ensembl [ENSG00000152464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152464)

## Data

Gene col 7632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7632); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7632]; `tensor/DDL_lfc|DDL_z.npy` [7632]; `embed/gene_vectors.npy` [7632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7632 or target_col == 7632). Every well: [[RPP38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPP38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
