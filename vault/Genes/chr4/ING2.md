---
symbol: "ING2"
type: "gene"
col: 9668
ensembl_id: "ENSG00000168556"
name: "inhibitor of growth family member 2"
location: "4q35.1"
module: 20
arm: "-"
pooled_cpm: 31.03
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ING2

*inhibitor of growth family member 2* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +8.0, q 1e-12, up in 44 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 3.14×, A549 3.40×, A498 2.63×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 3.08×, KATO III 2.68×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.640× (z -4.8, q 0.001, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~69% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 0.302×; ⚠ cell-cycle shift, explains ~69% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAP]] (+0.74, fdr 7e-06), [[NUDT22]] (+0.74, fdr 3e-05), [[INAFM1]] (+0.73, fdr 7e-06); moves opposite to [[MRPL42]] (-0.75, fdr 7e-06), [[VMA21]] (-0.74, fdr 7e-06), [[RPSA]] (-0.71, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ENKD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9668.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 3.14×, A549 3.40×, A498 2.63×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 3.08×, KATO III 2.68×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +8.0 | 1e-12 | 44/46 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.53×** | +4.7 | 7e-04 | 29/47 (PANC-1, A549, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.70×** | +4.0 | 0.010 | 31/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.60×** | +3.7 | 0.031 | 29/46 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.49× | +3.0 | 0.26 | 25/48 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9668.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 0.302×; ⚠ cell-cycle shift, explains ~69% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.640×** | -4.8 | 0.001 | 33/48 (NCI-H2347, C32, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.620× | -3.5 | 0.13 | 27/47 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.645× | -3.1 | 0.25 | 24/40 (HS-578T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.646× | -3.1 | 0.25 | 24/48 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 24.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.7) | — |
| [[LoVo (line)]] | wt | 20.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.302× (z -11.9) ⚠ cell-cycle shift, explains ~69% of this change |
| [[PANC-1 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | +0.74 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[NUDT22]] | +0.74 | +0.45 / +0.80 | both halves | 3e-05 |  |
| [[INAFM1]] | +0.73 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[MED19]] | +0.71 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.71 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[PMM1]] | +0.69 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.69 | +0.54 / +0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | +0.69 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[PURA]] | +0.69 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[RNF181]] | +0.68 | +0.44 / +0.75 | both halves | 3e-05 |  |
| [[KRTCAP2]] | +0.68 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[C1orf35]] | +0.68 | +0.41 / +0.78 | both halves | 4e-05 |  |
| [[TMEM258]] | +0.68 | +0.44 / +0.75 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL42]] | -0.75 | -0.60 / -0.78 | both halves | 7e-06 |  |
| [[VMA21]] | -0.74 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[RPSA]] | -0.71 | -0.61 / -0.74 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.71 | -0.58 / -0.76 | both halves | 8e-06 |  |
| [[EWSR1]] | -0.69 | -0.47 / -0.77 | both halves | 2e-05 |  |
| [[ARPP19]] | -0.69 | -0.41 / -0.73 | both halves | 4e-05 |  |
| [[TMEM33]] | -0.69 | -0.58 / -0.70 | both halves | 8e-06 |  |
| [[LIN7C]] | -0.68 | -0.38 / -0.75 | both halves | 6e-05 |  |
| [[SRSF1]] | -0.67 | -0.49 / -0.73 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.67 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.67 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[TMX3]] | -0.66 | -0.50 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENKD1]] | B | ENKD1 activity lowers ING2's level | lines that do not express ENKD1 (5) vs lines expressing it (45) | 1.13× higher at baseline in the lines without ENKD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.8, -28.9); signed map (-14.5, 0.3). **Vector** length 107, 38.0% of its response variance represented; |z| ≥ 3 in 491 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.9 | +4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.0 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.7 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -5.7 | -4.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.4 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of growth family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:183,505,058-183,512,429 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p33ING2; previously ING1L |
| Gene groups (HGNC) | PHD finger proteins; Inhibitor of growth family |
| Reactome | 7 pathways, smallest: PI5P Regulates TP53 Acetylation; Regulation of TP53 Activity through Acetylation; SUMOylation of transcription cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H160](https://www.uniprot.org/uniprotkb/Q9H160) (Inhibitor of growth protein 2):

> Seems to be involved in p53/TP53 activation and p53/TP53-dependent apoptotic pathways, probably by enhancing acetylation of p53/TP53. Component of a mSin3A-like corepressor complex, which is probably involved in deacetylation of nucleosomal histones. ING2 activity seems to be modulated by binding to phosphoinositides (PtdInsPs).

**Summary**, from NCBI Gene [3622](https://www.ncbi.nlm.nih.gov/gene/3622):

> This gene is a member of the inhibitor of growth (ING) family. Members of the ING family associate with and modulate the activity of histone acetyltransferase (HAT) and histone deacetylase (HDAC) complexes and function in DNA repair and apoptosis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:6063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6063) · Entrez [3622](https://www.ncbi.nlm.nih.gov/gene/3622) · UniProt [Q9H160](https://www.uniprot.org/uniprotkb/Q9H160) · Ensembl [ENSG00000168556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168556)

## Data

Gene col 9668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9668); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9668]; `tensor/DDL_lfc|DDL_z.npy` [9668]; `embed/gene_vectors.npy` [9668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9668 or target_col == 9668). Every well: [[ING2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ING2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
