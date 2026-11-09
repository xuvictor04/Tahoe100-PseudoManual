---
symbol: "RTEL1"
type: "gene"
col: 15096
ensembl_id: "ENSG00000258366"
name: "regulator of telomere elongation helicase 1"
location: "20q13.33"
module: 4
arm: "+"
pooled_cpm: 16.34
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RTEL1

*regulator of telomere elongation helicase 1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.52× (z +4.7, q 0.002, up in 13 of 28 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.582× (z -8.9, q 4e-16, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFTUD2]] (+0.72, fdr 7e-06), [[SYMPK]] (+0.71, fdr 7e-06), [[TREX2]] (+0.69, fdr 7e-06); moves opposite to [[MPLKIP]] (-0.64, fdr 1e-05), [[KDM5B]] (-0.64, fdr 1e-05), [[CHMP2B]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.7 | 0.002 | 13/28 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +4.0 | 0.017 | 11/35 (Hs 766T, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.34× | +3.4 | 0.14 | 10/47 (NCI-H460, LOX-IMVI, …) | two highest doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.32× | +3.2 | 0.20 | 10/45 (C32, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.30× | +3.1 | 0.20 | 12/47 (HepG2/C3A, A549, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.20 | 7/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -8.9 | 4e-16 | 36/47 (NCI-H1792, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.644×** | -7.2 | 2e-10 | 30/47 (hTERT-HPNE, NCI-H2030, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.669×** | -4.7 | 6e-04 | 25/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.769×** | -4.3 | 0.002 | 23/48 (A-427, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -3.8 | 0.013 | 18/46 (RPMI-7951, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -3.8 | 0.013 | 21/48 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -3.7 | 0.015 | 19/47 (A-427, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.749×** | -3.2 | 0.090 | 19/47 (SK-MEL-2, NCI-H2030, …) | two highest doses | composition shift; position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 0.770× | -3.0 | 0.16 | 11/47 (NCI-H23, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -11.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.0984× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.595× (z -10.8) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.3) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -10.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[AsPC-1 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -9.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.107× (z -9.2) |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.6) |
| [[KATO III (line)]] | alt | 27.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-172 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[SYMPK]] | +0.71 | +0.75 / +0.71 | both halves | 7e-06 | STRING 549 |
| [[TREX2]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[E2F4]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NECAB3]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[CHID1]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 | STRING 448 |
| [[POLD1]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 | pathway: Chromosome Maintenance; STRING 819 |
| [[PPP5C]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[NOP9]] | +0.64 | +0.58 / +0.66 | both halves | 8e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPLKIP]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.64 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[CHMP2B]] | -0.63 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PIGP]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[LACTB]] | -0.58 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[OSER1-DT]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[LCA5]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[CERT1]] | -0.57 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[ZMYM5]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[AKAP1-DT]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FBXL3]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RTEL1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-16.5, -29.8); signed map (-25.7, -47.6). **Vector** length 85.2, 16.4% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.3 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.9 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.9 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.8 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.1 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | regulator of telomere elongation helicase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,657,810-63,696,253 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bK3184A7.3, NHL, DKFZP434C013, KIAA1088, RTEL; previously C20orf41 |
| Gene groups (HGNC) | DEAH-box helicases |
| Reactome | 13 pathways, smallest: Cytosolic iron-sulfur cluster assembly; Telomere Extension By Telomerase; Resolution of D-loop Structures through Synthesis-Dependent Strand Annealing (SDSA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ71](https://www.uniprot.org/uniprotkb/Q9NZ71) (Regulator of telomere elongation helicase 1):

> A probable ATP-dependent DNA helicase implicated in telomere-length regulation, DNA repair and the maintenance of genomic stability. Acts as an anti-recombinase to counteract toxic recombination and limit crossover during meiosis. Regulates meiotic recombination and crossover homeostasis by physically dissociating strand invasion events and thereby promotes noncrossover repair by meiotic synthesis dependent strand annealing (SDSA) as well as disassembly of D loop recombination intermediates. …

**Summary**, from NCBI Gene [51750](https://www.ncbi.nlm.nih.gov/gene/51750):

> This gene encodes a DNA helicase which functions in the stability, protection and elongation of telomeres and interacts with proteins in the shelterin complex known to protect telomeres during DNA replication. Mutations in this gene have been associated with dyskeratosis congenita and Hoyerall-Hreidarsson syndrome. Read-through transcription of this gene into the neighboring downstream gene, which encodes tumor necrosis factor receptor superfamily, member 6b, generates a non-coding transcript. …

**Accessions** — [HGNC:15888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15888) · Entrez [51750](https://www.ncbi.nlm.nih.gov/gene/51750) · UniProt [Q9NZ71](https://www.uniprot.org/uniprotkb/Q9NZ71) · Ensembl [ENSG00000258366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258366)

## Data

Gene col 15096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15096); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15096]; `tensor/DDL_lfc|DDL_z.npy` [15096]; `embed/gene_vectors.npy` [15096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15096 or target_col == 15096). Every well: [[RTEL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTEL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
