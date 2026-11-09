---
symbol: "MRPL58"
type: "gene"
col: 9551
ensembl_id: "ENSG00000167862"
name: "mitochondrial ribosomal protein L58"
location: "17q25.1"
module: 11
arm: "+"
pooled_cpm: 11.0
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRPL58

*mitochondrial ribosomal protein L58* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.25× (z +9.7, q 1e-19, up in 36 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.0923×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (BT-474 0.0820×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.303×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL14EP]] (+0.77, fdr 7e-06), [[NSUN5]] (+0.76, fdr 7e-06), [[PHAX]] (+0.74, fdr 7e-06); moves opposite to [[TMED4]] (-0.73, fdr 7e-06), [[TMBIM6]] (-0.65, fdr 1e-05), [[MLEC]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CCDC137]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +9.7 | 1e-19 | 36/43 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.73×** | +9.3 | 3e-18 | 37/45 (A549, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +8.9 | 1e-16 | 38/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +8.6 | 2e-15 | 41/46 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.85×** | +7.4 | 2e-11 | 36/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +6.7 | 1e-09 | 28/38 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.6 | 3e-09 | 12/19 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.52×** | +5.0 | 4e-05 | 18/35 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.50×** | +4.9 | 8e-05 | 20/41 (NCI-H460, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +4.4 | 6e-04 | 16/28 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **2.05×** | +4.2 | 0.001 | 14/42 (HS-578T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +3.5 | 0.019 | 16/47 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.030 | 15/45 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.037 | 13/48 (NCI-H2347, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.065 | 11/40 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9551.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.0923×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (BT-474 0.0820×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.303×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.751× | -3.5 | 0.17 | 12/47 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.819× | -3.4 | 0.17 | 17/43 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.769× | -3.2 | 0.27 | 15/46 (HT-29, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 7.76 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0820× (z -9.2) |
| [[KATO III (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0923× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 14.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -9.0) |
| [[A-172 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL14EP]] | +0.77 | +0.86 / +0.75 | both halves | 7e-06 |  |
| [[NSUN5]] | +0.76 | +0.77 / +0.81 | both halves | 7e-06 |  |
| [[PHAX]] | +0.74 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.74 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[ZNF23]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[ZNF197]] | +0.73 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[VPS72]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[GLRX2]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.72 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.70 | +0.74 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED4]] | -0.73 | -0.72 / -0.69 | both halves | 7e-06 |  |
| [[TMBIM6]] | -0.65 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[MLEC]] | -0.63 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[APLP2]] | -0.62 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[PDIA6]] | -0.62 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[LAPTM4A]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC137]] | C | MRPL58's natural level strengthens CCDC137's drug response | MRPL58's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.01; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-31.6, 5.6); signed map (2.4, -22.4). **Vector** length 69.9, 13.2% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.1 | +9.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L58 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,012,670-75,021,261 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DS-1, mL62; previously ICT1 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins; Mitochondrial translation release factor family |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14197](https://www.uniprot.org/uniprotkb/Q14197) (Large ribosomal subunit protein mL62):

> Essential peptidyl-tRNA hydrolase component of the mitochondrial large ribosomal subunit. Acts as a codon-independent translation release factor that has lost all stop codon specificity and directs the termination of translation in mitochondrion, possibly in case of abortive elongation. Involved in the hydrolysis of peptidyl-tRNAs that have been prematurely terminated and thus in the recycling of stalled mitochondrial ribosomes.

**Summary**, from NCBI Gene [3396](https://www.ncbi.nlm.nih.gov/gene/3396):

> The protein encoded by this gene is a peptidyl-tRNA hydrolase and a vital component of the large mitochondrial ribosome. The encoded protein serves as a ribosome release factor for this ribosome, which translates mitochondrial genes. This protein may be responsible for degrading prematurely-terminated polypeptides and for reusing stalled ribosomes. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:5359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5359) · Entrez [3396](https://www.ncbi.nlm.nih.gov/gene/3396) · UniProt [Q14197](https://www.uniprot.org/uniprotkb/Q14197) · Ensembl [ENSG00000167862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167862)

## Data

Gene col 9551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9551); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9551]; `tensor/DDL_lfc|DDL_z.npy` [9551]; `embed/gene_vectors.npy` [9551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9551 or target_col == 9551). Every well: [[MRPL58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
