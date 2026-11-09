---
symbol: "TIMM22"
type: "gene"
col: 10815
ensembl_id: "ENSG00000177370"
name: "translocase of inner mitochondrial membrane 22"
location: "17p13"
module: 7
arm: "+"
pooled_cpm: 7.49
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TIMM22

*translocase of inner mitochondrial membrane 22* — 17p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.04× (z +10.2, q 6e-22, up in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +10.0, q 2e-21, up in 28 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0813×); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H23 0.151×); [[Procainamide (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.0626×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C12orf43]] (+0.72, fdr 7e-06), [[KTI12]] (+0.71, fdr 7e-06), [[POP4]] (+0.68, fdr 7e-06); moves opposite to [[NAP1L1]] (-0.55, fdr 2e-05), [[PSIP1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KDF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.04×** | +10.2 | 6e-22 | 39/47 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.03×** | +10.2 | 6e-22 | 38/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.0 | 2e-21 | 28/43 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +9.5 | 2e-19 | 26/36 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.89×** | +9.1 | 8e-18 | 31/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +9.1 | 8e-18 | 30/42 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.84×** | +8.7 | 2e-16 | 33/47 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.90×** | +8.7 | 3e-16 | 28/44 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.78×** | +7.9 | 1e-13 | 25/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.2 | 2e-11 | 22/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +6.6 | 2e-09 | 25/47 (SW480, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +6.3 | 1e-08 | 20/46 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.34×** | +6.0 | 1e-07 | 20/43 (A549, NCI-H23, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +5.3 | 5e-06 | 16/42 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.44×** | +5.2 | 8e-06 | 17/46 (SHP-77, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +5.0 | 2e-05 | 13/47 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.2 | 7e-04 | 11/48 (A498, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.006 | 8/43 (NCI-H460, A-172, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.007 | 8/45 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.012 | 11/46 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.025 | 6/48 (HEC-1-A, NCI-H460, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.034 | 7/44 (NCI-H23, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10815.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0813×); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H23 0.151×); [[Procainamide (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.0626×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | 0.864× | -3.0 | 0.96 | 11/48 (HepG2/C3A, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 6.19 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0813× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.151× (z -10.1) |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0626× (z -9.4) |
| [[A-172 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf43]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[KTI12]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[POP4]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ABT1]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[FADD]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MRPS11]] | +0.64 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[COMMD5]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[POLR3F]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MRM3]] | +0.64 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[EXOSC4]] | +0.64 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[PFDN1]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L1]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PSIP1]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDF1]] | B | KDF1 activity lowers TIMM22's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.15× higher at baseline in the lines without KDF1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.4, 1.8); signed map (-3.9, -24.6). **Vector** length 49.8, 6.15% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.4 | +9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.1 | +8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.0 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +1.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.6 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13 — chr17:997,129-1,003,671 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIM22; previously TEX4 |
| Gene groups (HGNC) | TIM22 complex; Tim17 family |
| Reactome | 3 pathways, smallest: Mitochondrial protein import; Mitochondrial protein degradation; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y584](https://www.uniprot.org/uniprotkb/Q9Y584) (Mitochondrial import inner membrane translocase subunit Tim22):

> Essential core component of the TIM22 complex, a complex that mediates the import and insertion of multi-pass transmembrane proteins into the mitochondrial inner membrane. In the TIM22 complex, it constitutes the voltage-activated and signal-gated channel. Forms a twin-pore translocase that uses the membrane potential as external driving force in 2 voltage-dependent steps (By similarity).

**Summary**, from NCBI Gene [29928](https://www.ncbi.nlm.nih.gov/gene/29928):

> Multipass transmembrane proteins are brought into mitochondria and inserted into the mitochondrial inner membrane by way of the TIM22 complex. This complex has six subunits and is a twin-pore translocase. The protein encoded by this gene is a subunit of TIM22 and represents the voltage-activated and signal-gated channel. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:17317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17317) · Entrez [29928](https://www.ncbi.nlm.nih.gov/gene/29928) · UniProt [Q9Y584](https://www.uniprot.org/uniprotkb/Q9Y584) · Ensembl [ENSG00000177370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177370)

## Data

Gene col 10815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10815); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10815]; `tensor/DDL_lfc|DDL_z.npy` [10815]; `embed/gene_vectors.npy` [10815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10815 or target_col == 10815). Every well: [[TIMM22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
