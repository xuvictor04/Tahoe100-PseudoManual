---
symbol: "CNIH4"
type: "gene"
col: 6799
ensembl_id: "ENSG00000143771"
name: "cornichon family member 4"
location: "1q42.11"
module: 3
arm: "+"
pooled_cpm: 41.91
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CNIH4

*cornichon family member 4* — 1q42.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.54× (z +4.3, q 0.009, up in 30 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +4.2, q 0.009, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.617× (z -7.2, q 3e-10, down in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (A-172 0.348×, SNU-423 0.319×, HOP62 0.373×, NCI-H2347 0.481×, …); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H23 0.0416×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA7]] (+0.69, fdr 7e-06), [[NENF]] (+0.67, fdr 1e-05), [[FBXO42]] (+0.66, fdr 7e-06); moves opposite to [[THOC6]] (-0.67, fdr 7e-06), [[ZNF628]] (-0.67, fdr 7e-06), [[SFPQ]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.3 | 0.009 | 30/46 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.009 | 31/48 (A498, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.0 | 0.010 | 29/45 (PANC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.016 | 29/47 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.017 | 23/48 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | 1.34× | +3.1 | 0.15 | 23/46 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | 1.23× | +3.1 | 0.15 | 20/48 (CFPAC-1, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.0 | 0.15 | 21/47 (C32, NCI-H460, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.60× | +3.0 | 0.15 | 20/48 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.0 | 0.15 | 23/47 (HT-29, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6799.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (A-172 0.348×, SNU-423 0.319×, HOP62 0.373×, NCI-H2347 0.481×, …); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H23 0.0416×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -7.2 | 3e-10 | 37/47 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.496×** | -3.9 | 0.032 | 28/48 (NCI-H23, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.0416× (z -11.1) |
| [[A-172 (line)]] | wt | 74.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -12.4) |
| [[HOP62 (line)]] | alt | 57.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.4) |
| [[J82 (line)]] | alt | 39.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.2) |
| [[LS 180 (line)]] | wt | 48.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 83.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.2) |
| [[SNU-423 (line)]] | alt | 46.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.5) |
| [[A-427 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA7]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[NENF]] | +0.67 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[FBXO42]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ZC2HC1A]] | +0.65 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[ATXN3]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.64 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[PPOX]] | +0.63 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[DENND10]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PTPRA]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MTM1]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ENY2]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.67 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[ZNF628]] | -0.67 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.62 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[PPP1R10]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SSU72]] | -0.60 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[DNAH1]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[FAT1]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ILF3]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.58 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[PUF60]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[LINC00641]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CNIH4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TP53]] | C | TP53 activity strengthens CNIH4's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.80× as strongly (z diff +0.49); strongest at Idarubicin (hydrochloride) 5 µM: 1.23x vs 1.61x (z diff +2.2) | 0.603 over the table, 0.032 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.9, -20.5); signed map (-25.0, 5.7). **Vector** length 91.1, 28.2% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.9 | +4.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.1 | -1.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Omeprazole (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cornichon family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.11 — chr1:224,356,858-224,379,459 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC163 |
| Gene groups (HGNC) | Cornichon family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P003](https://www.uniprot.org/uniprotkb/Q9P003) (Protein cornichon homolog 4):

> Involved in G protein-coupled receptors (GPCRs) trafficking from the endoplasmic reticulum to the cell surface; it promotes the exit of GPCRs from the early secretory pathway, likely through interaction with the COPII machinery.

**Summary**, from NCBI Gene [29097](https://www.ncbi.nlm.nih.gov/gene/29097):

> Enables CCR5 chemokine receptor binding activity. Involved in endoplasmic reticulum to Golgi vesicle-mediated transport. Located in endoplasmic reticulum and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25013) · Entrez [29097](https://www.ncbi.nlm.nih.gov/gene/29097) · UniProt [Q9P003](https://www.uniprot.org/uniprotkb/Q9P003) · Ensembl [ENSG00000143771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143771)

## Data

Gene col 6799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6799); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6799]; `tensor/DDL_lfc|DDL_z.npy` [6799]; `embed/gene_vectors.npy` [6799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6799 or target_col == 6799). Every well: [[CNIH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNIH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
