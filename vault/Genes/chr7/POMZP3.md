---
symbol: "POMZP3"
type: "gene"
col: 7115
ensembl_id: "ENSG00000146707"
name: "POM121 and ZP3 fusion"
location: "7q11.23"
module: 21
arm: "+"
pooled_cpm: 11.34
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# POMZP3

*POM121 and ZP3 fusion* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +10.1, q 3e-21, up in 30 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (SW 900 0.0768×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPM1D]] (+0.69, fdr 7e-06), [[MIR34AHG]] (+0.62, fdr 1e-05), [[ZNF821]] (+0.62, fdr 1e-05); moves opposite to [[PSMG1]] (-0.55, fdr 3e-05), [[CLTC]] (-0.53, fdr 8e-05), [[UBR4]] (-0.52, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SLC35D1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +10.1 | 3e-21 | 30/44 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +9.4 | 2e-18 | 39/46 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +8.7 | 5e-16 | 34/39 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.17×** | +7.5 | 8e-12 | 38/47 (A-172, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +7.5 | 9e-12 | 29/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +7.2 | 5e-11 | 21/29 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +6.6 | 4e-09 | 29/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +5.1 | 3e-05 | 21/46 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +4.7 | 1e-04 | 18/46 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +4.3 | 1e-03 | 20/47 (A498, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.012 | 14/47 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +3.6 | 0.014 | 18/43 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.5 | 0.022 | 5/20 (SW480, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.034 | 12/47 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.048 | 11/48 (J82, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.068 | 3/48 (CFPAC-1, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.092 | 4/48 (COLO 205, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7115.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (SW 900 0.0768×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.772× | -3.2 | 0.71 | 9/47 (A-172, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +8.9) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A498 (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +14.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[KATO III (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.98× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 9.07 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.62× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 9.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 8.14 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0768× (z -10.6) |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1D]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MIR34AHG]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF821]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.60 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[ANKRD42-DT]] | +0.60 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ANKRA2]] | +0.59 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[FAM217A]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[TMA7]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[TICAM2-AS1]] | +0.56 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[BORCS7]] | +0.56 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[ZNF358]] | +0.56 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[PABPN1]] | +0.56 | +0.46 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | -0.55 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[CLTC]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[UBR4]] | -0.52 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[ANAPC1P4]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PRELID3B]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CCT5]] | -0.50 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[HUWE1]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PRKDC]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[DYNC1H1]] | -0.48 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35D1]] | C | POMZP3's natural level strengthens SLC35D1's drug response | POMZP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.08; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.1, 35.7); signed map (39.9, -25.6). **Vector** length 64.0, 10.7% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.3 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.2 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | POM121 and ZP3 fusion |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:76,609,986-76,627,279 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POM-ZP3, POM121 |
| Matched by | ensembl_id |

UniProt [Q6PJE2](https://www.uniprot.org/uniprotkb/Q6PJE2) carries no function annotation.

**Summary**, from NCBI Gene [22932](https://www.ncbi.nlm.nih.gov/gene/22932):

> This gene appears to have resulted from a fusion of DNA sequences derived from 2 distinct loci, specifically through the duplication of two internal exons from the POM121 gene and four 3' exons from the ZP3 gene. The 5' end of this gene is similar to the 5` coding region of the POM121 gene which encodes an integral nuclear pore membrane protein. However, the protein encoded by this gene lacks the nuclear pore localization motif. The 3' end of this gene is similar to the last 4 exons of the zona …

**Accessions** — [HGNC:9203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9203) · Entrez [22932](https://www.ncbi.nlm.nih.gov/gene/22932) · UniProt [Q6PJE2](https://www.uniprot.org/uniprotkb/Q6PJE2) · Ensembl [ENSG00000146707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146707)

## Data

Gene col 7115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7115); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7115]; `tensor/DDL_lfc|DDL_z.npy` [7115]; `embed/gene_vectors.npy` [7115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7115 or target_col == 7115). Every well: [[POMZP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POMZP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
