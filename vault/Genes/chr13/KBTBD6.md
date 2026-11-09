---
symbol: "KBTBD6"
type: "gene"
col: 9147
ensembl_id: "ENSG00000165572"
name: "kelch repeat and BTB domain containing 6"
location: "13q14.11"
module: 12
arm: "+"
pooled_cpm: 4.94
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# KBTBD6

*kelch repeat and BTB domain containing 6* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +13.6, q 3e-39, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.550× (z -10.4, q 2e-22, down in 25 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL9]] (+0.76, fdr 7e-06), [[NSUN5]] (+0.75, fdr 7e-06), [[ZNF45]] (+0.75, fdr 7e-06); moves opposite to [[PPP1R15B-AS1]] (-0.62, fdr 4e-04), [[CCNT2-AS1]] (-0.60, fdr 8e-04, ⚠ one half only (not replicated)), [[KPNB1-DT]] (-0.59, fdr 4e-04), [[SLC25A53]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +13.6 | 3e-39 | 30/41 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.46×** | +10.7 | 3e-24 | 21/28 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.45×** | +10.6 | 5e-24 | 38/45 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.36×** | +10.6 | 5e-24 | 36/46 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +10.4 | 3e-23 | 38/47 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +10.0 | 2e-21 | 25/47 (J82, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +9.4 | 3e-19 | 25/40 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +9.1 | 4e-18 | 32/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +9.1 | 8e-18 | 31/47 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.61×** | +5.9 | 3e-07 | 12/28 (A-172, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.4 | 3e-06 | 10/47 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 4e-05 | 13/41 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.7 | 1e-04 | 16/47 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.002 | 9/47 (LoVo, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.010 | 10/47 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[NG25 (drug)]] 5 µM |  | **1.68×** | +3.4 | 0.027 | 1/37 (NCI-H460) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.097 | 3/48 (LoVo, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -10.4 | 2e-22 | 25/42 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -4.5 | 0.001 | 14/40 (NCI-H2347, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -4.5 | 0.001 | 15/42 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.24 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -10.2) |
| [[A498 (line)]] | wt | 7.21 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 5.80 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.3) |
| [[Hs 766T (line)]] | wt | 7.82 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -8.7) |
| [[KATO III (line)]] | alt | 4.02 | 0 | 1 | — | [[Clofarabine (drug)]] 0.5 µM 0.0981× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 4.97 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 2.41 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0735× (z -9.4) |
| [[SW1417 (line)]] | alt | 6.43 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -9.2) |
| [[SW48 (line)]] | wt | 8.42 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0694× (z -8.5) |
| [[A-427 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL9]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 914 |
| [[NSUN5]] | +0.75 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[ZNF45]] | +0.75 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[NUDT12]] | +0.75 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[MSL3P1]] | +0.73 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[KBTBD7]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 995 |
| [[ZNF22]] | +0.73 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[RP9]] | +0.70 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[GPATCH11]] | +0.70 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[ZNF182]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R15B-AS1]] | -0.62 | -0.25 / -0.62 | both halves | 4e-04 |  |
| [[CCNT2-AS1]] | -0.60 | -0.19 / -0.57 | ⚠ one half (not replicated) | 8e-04 |  |
| [[KPNB1-DT]] | -0.59 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[SLC25A53]] | -0.59 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[PRDM10]] | -0.59 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[IL18BP]] | -0.59 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[ATP11C]] | -0.58 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KBTBD6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.0, -1.3); signed map (-19.7, -15.7). **Vector** length 66.9, 10.1% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Sonidegib (drug)]] 0.5 µM |  | +0.8 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -10.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.3 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | kelch repeat and BTB domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:41,127,569-41,132,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp547E1912 |
| Gene groups (HGNC) | BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V97](https://www.uniprot.org/uniprotkb/Q86V97) (Kelch repeat and BTB domain-containing protein 6):

> As part of the CUL3(KBTBD6/7) E3 ubiquitin ligase complex functions as a substrate adapter for the RAC1 guanine exchange factor (GEF) TIAM1, mediating its 'Lys-48' ubiquitination and proteasomal degradation. By controlling this ubiquitination, regulates RAC1 signal transduction and downstream biological processes including the organization of the cytoskeleton, cell migration and cell proliferation. Ubiquitination of TIAM1 requires the membrane-associated protein GABARAP which may restrict …

**Summary**, from NCBI Gene [89890](https://www.ncbi.nlm.nih.gov/gene/89890):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Involved in proteasome-mediated ubiquitin-dependent protein catabolic process; protein K48-linked ubiquitination; and regulation of Rac protein signal transduction. Located in cytoplasm and nucleus. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25340) · Entrez [89890](https://www.ncbi.nlm.nih.gov/gene/89890) · UniProt [Q86V97](https://www.uniprot.org/uniprotkb/Q86V97) · Ensembl [ENSG00000165572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165572)

## Data

Gene col 9147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9147); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9147]; `tensor/DDL_lfc|DDL_z.npy` [9147]; `embed/gene_vectors.npy` [9147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9147 or target_col == 9147). Every well: [[KBTBD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
