---
symbol: "MCRS1"
type: "gene"
col: 11948
ensembl_id: "ENSG00000187778"
name: "microspherule protein 1"
location: "12q13.12"
module: 7
arm: "+"
pooled_cpm: 12.55
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MCRS1

*microspherule protein 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.16× (z +9.0, q 8e-17, up in 10 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.62× (z +4.3, q 0.004, up in 11 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.485× (z -12.4, q 2e-32, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KEAP1]] (+0.69, fdr 7e-06), [[INTS14]] (+0.68, fdr 7e-06), [[ZNF414]] (+0.67, fdr 7e-06); moves opposite to [[AP3S1]] (-0.58, fdr 1e-05), [[TMEM87B]] (-0.55, fdr 1e-05), [[AP1S2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +9.0 | 8e-17 | 10/48 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +4.3 | 0.004 | 11/44 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +4.3 | 0.004 | 11/47 (SW480, HCT15, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.012 | 7/42 (SW1417, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.8 | 0.020 | 14/41 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.3 | 0.083 | 4/36 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Imiquimod (maleate) (drug)]] 5 µM |  | 1.21× | +3.1 | 0.15 | 3/46 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.15 | 5/45 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | 1.20× | +3.0 | 0.15 | 9/40 (HOP62, A549, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.485×** | -12.4 | 2e-32 | 40/47 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.499×** | -11.9 | 4e-30 | 40/47 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.523×** | -11.1 | 3e-26 | 35/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.671×** | -9.5 | 3e-19 | 37/48 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -9.5 | 3e-19 | 32/46 (NCI-H23, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.599×** | -8.8 | 2e-16 | 28/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -8.4 | 5e-15 | 30/47 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -7.8 | 4e-13 | 27/47 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.730×** | -5.4 | 4e-06 | 20/46 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -5.3 | 7e-06 | 20/46 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.556×** | -5.2 | 8e-06 | 12/48 (SK-MEL-2, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.817×** | -3.5 | 0.026 | 6/47 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.0 | 0.11 | 14/47 (NCI-H460, KATO III, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -13.2) |
| [[RKO (line)]] | wt | 14.7 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -11.3) |
| [[A-172 (line)]] | wt | 8.49 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.124× (z -9.8) |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0647× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0718× (z -11.2) |
| [[LoVo (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -10.3) |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0719× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.137× (z -9.3) |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0795× (z -11.0) |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.128× (z -10.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KEAP1]] | +0.69 | +0.59 / +0.67 | both halves | 7e-06 | pathway: Deubiquitination |
| [[INTS14]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZNF414]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[YJU2]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[FEM1A]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[KAT5]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | pathway: Chromatin modifying enzymes; STRING 942 |
| [[CENPBD1P]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.66 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[NRDE2]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[AAR2]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 | STRING 460 |
| [[WDR18]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[DNAJC14]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3S1]] | -0.58 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TMEM87B]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[AP1S2]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PAIP2B]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TMEM65]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MCRS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.9, 8.9); signed map (-1.1, -24.7). **Vector** length 61.9, 9.49% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -9.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -11.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | microspherule protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,556,544-49,568,145 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ICP22BP, MSP58, P78, MCRS2, INO80Q |
| Gene groups (HGNC) | INO80 complex subunits; NSL histone acetyltransferase complex; Centriolar satellite proteins |
| Reactome | 12 pathways, smallest: DNA Damage Recognition in GG-NER; Formation of WDR5-containing histone-modifying complexes; UCH proteinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EZ8](https://www.uniprot.org/uniprotkb/Q96EZ8) (Microspherule protein 1):

> Modulates the transcription repressor activity of DAXX by recruiting it to the nucleolus. As part of the NSL complex, may be involved in acetylation of nucleosomal histone H4 on several lysine residues. Putative regulatory component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair. May also be an inhibitor of TERT telomerase activity. Binds to G-quadruplex structures in mRNA. Binds to RNA homomer poly(G) and …

**Summary**, from NCBI Gene [10445](https://www.ncbi.nlm.nih.gov/gene/10445):

> Enables RNA binding activity and telomerase inhibitor activity. Involved in several processes, including positive regulation of DNA-templated transcription; positive regulation of protein localization to nucleolus; and regulation of DNA metabolic process. Located in cytoplasm; nucleolus; and nucleoplasm. Part of Ino80 complex; MLL1 complex; and histone acetyltransferase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6960) · Entrez [10445](https://www.ncbi.nlm.nih.gov/gene/10445) · UniProt [Q96EZ8](https://www.uniprot.org/uniprotkb/Q96EZ8) · Ensembl [ENSG00000187778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187778)

## Data

Gene col 11948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11948); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11948]; `tensor/DDL_lfc|DDL_z.npy` [11948]; `embed/gene_vectors.npy` [11948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11948 or target_col == 11948). Every well: [[MCRS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCRS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
