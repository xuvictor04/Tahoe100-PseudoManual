---
symbol: "CHRNB1"
type: "gene"
col: 9911
ensembl_id: "ENSG00000170175"
name: "cholinergic receptor nicotinic beta 1 subunit"
location: "17p13.1"
module: 3
arm: "+"
pooled_cpm: 10.75
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CHRNB1

*cholinergic receptor nicotinic beta 1 subunit* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +4.2, q 0.012, up in 16 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.37×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.574× (z -7.9, q 1e-12, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN6-DT]] (+0.60, fdr 4e-05), [[PGPEP1]] (+0.60, fdr 1e-05), [[SIRT2]] (+0.58, fdr 4e-05); moves opposite to [[NUP155]] (-0.57, fdr 9e-05), [[XRCC5]] (-0.57, fdr 1e-04), [[DARS2]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TNNI3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9911.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.37×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.012 | 16/43 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.1 | 0.012 | 12/31 (NCI-H2030, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.42× | +3.3 | 0.19 | 9/24 (NCI-H2030, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.64× | +3.1 | 0.28 | 4/40 (NCI-H2030, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9911.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.574×** | -7.9 | 1e-12 | 26/41 (HCT15, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -5.8 | 2e-06 | 22/41 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.564×** | -5.6 | 5e-06 | 22/43 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.643×** | -4.5 | 0.001 | 20/45 (HCT15, HepG2/C3A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -4.0 | 0.007 | 13/42 (A549, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -3.9 | 0.009 | 20/45 (A549, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -3.9 | 0.009 | 15/41 (A549, SW 900, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.694×** | -3.5 | 0.033 | 15/45 (RKO, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.736× | -3.1 | 0.11 | 14/45 (RKO, SW480, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.739× | -3.1 | 0.12 | 16/45 (SW480, LS 180, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.37× (z +10.1) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -12.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.8) |
| [[A549 (line)]] | wt | 6.89 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -9.8) |
| [[HCT15 (line)]] | alt | 47.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.2) |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.1) |
| [[KATO III (line)]] | alt | 5.42 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0460× (z -10.6) |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 3.96 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0687× (z -8.5) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -11.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 4.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[RKO (line)]] | wt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.1) |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -9.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | +0.60 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[PGPEP1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SIRT2]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 | pathway: HALLMARK_MYOGENESIS |
| [[VASN]] | +0.57 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[MARCHF9]] | +0.57 | +0.26 / +0.67 | both halves | 3e-04 |  |
| [[FAM182B]] | +0.56 | +0.23 / +0.57 | both halves | 5e-04 |  |
| [[ARID3A]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SNHG19]] | +0.55 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[COMMD6]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[LAMTOR5]] | +0.53 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[ACAP1]] | +0.53 | +0.31 / +0.62 | both halves | 2e-04 |  |
| [[MIEN1]] | +0.53 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | -0.57 | -0.37 / -0.64 | both halves | 9e-05 |  |
| [[XRCC5]] | -0.57 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[DARS2]] | -0.55 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[PSME3]] | -0.55 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[IPO9]] | -0.55 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[FARSB]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.54 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[PDAP1]] | -0.53 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[PRKDC]] | -0.53 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[MACROH2A1]] | -0.52 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[CAPRIN1]] | -0.52 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[RUVBL1]] | -0.52 | -0.40 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNI3]] | B | TNNI3 activity raises CHRNB1's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without TNNI3 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.5, -33.5); signed map (-25.2, 13.4). **Vector** length 50.2, 6.71% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cholinergic receptor nicotinic beta 1 subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,445,061-7,457,710 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CHRNB |
| Gene groups (HGNC) | Cholinergic receptors nicotinic subunits |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P11230](https://www.uniprot.org/uniprotkb/P11230) (Acetylcholine receptor subunit beta):

> After binding acetylcholine, the AChR responds by an extensive change in conformation that affects all subunits and leads to opening of an ion-conducting channel across the plasma membrane.

**Summary**, from NCBI Gene [1140](https://www.ncbi.nlm.nih.gov/gene/1140):

> The muscle acetylcholine receptor is composed of five subunits: two alpha subunits and one beta, one gamma, and one delta subunit. This gene encodes the beta subunit of the acetylcholine receptor. The acetylcholine receptor changes conformation upon acetylcholine binding leading to the opening of an ion-conducting channel across the plasma membrane. Mutations in this gene are associated with slow-channel congenital myasthenic syndrome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1961) · Entrez [1140](https://www.ncbi.nlm.nih.gov/gene/1140) · UniProt [P11230](https://www.uniprot.org/uniprotkb/P11230) · Ensembl [ENSG00000170175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170175)

## Data

Gene col 9911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9911); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9911]; `tensor/DDL_lfc|DDL_z.npy` [9911]; `embed/gene_vectors.npy` [9911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9911 or target_col == 9911). Every well: [[CHRNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
