---
symbol: "IGF2"
type: "gene"
col: 9440
ensembl_id: "ENSG00000167244"
name: "insulin like growth factor 2"
location: "11p15.5"
module: 50
arm: "+"
pooled_cpm: 207.35
n_lines_expressing: 18
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# IGF2

*insulin like growth factor 2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.32× (z +12.7, q 4e-34, up in 13 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +11.4, q 2e-27, up in 11 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Glycyrrhizic acid (drug)]] 0.5 µM: 0.562× (z -4.1, q 0.023, down in 3 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.293×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL6A1]] (+0.69, fdr 1e-05), [[COL6A2]] (+0.59, fdr 1e-05), [[ANPEP]] (+0.55, fdr 2e-05); moves opposite to [[MRPL46]] (-0.47, fdr 1e-04), [[TRIM16L-1]] (-0.47, fdr 5e-05), [[CDIN1]] (-0.45, fdr 1e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ITM2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.32×** | +12.7 | 4e-34 | 13/14 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +11.4 | 2e-27 | 11/17 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.68×** | +11.0 | 6e-26 | 13/17 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +7.3 | 3e-11 | 9/14 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.26×** | +6.2 | 7e-08 | 9/16 (SW480, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +4.9 | 1e-04 | 10/16 (hTERT-HPNE, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.66×** | +4.6 | 4e-04 | 13/16 (C32, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +3.9 | 0.006 | 6/13 (hTERT-HPNE, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.006 | 10/16 (Hs 766T, H4, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +3.9 | 0.006 | 1/16 (HT-29) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.008 | 12/16 (hTERT-HPNE, C32, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.012 | 3/16 (SW480, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.028 | 10/17 (Hs 766T, C32, …) | rises with dose | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.039 | 7/16 (C32, H4, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.81×** | +3.1 | 0.069 | 7/16 (Hs 766T, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9440.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.293×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.562×** | -4.1 | 0.023 | 3/16 (hTERT-HPNE, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.679× | -3.4 | 0.13 | 6/16 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.682× | -3.3 | 0.13 | 10/16 (NCI-H23, C32, …) | rises with dose | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.768× | -3.3 | 0.13 | 0/16 | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.700× | -3.2 | 0.14 | 11/16 (HepG2/C3A, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 3,240 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 176 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.43× (z +9.3) ⚠ transcription drop | — |
| [[NCI-H23 (line)]] | alt | 194 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.17× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 68.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 39.8 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 26.7 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 19.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 24.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9,744 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 714 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 379 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 26.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 29.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.3 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 34.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 21.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 579 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 25.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.0 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 47.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 26.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 31.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL6A1]] | +0.69 | +0.68 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[COL6A2]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ANPEP]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[CTSB]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GANAB]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[PRKCSH]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 | pathway: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| [[BSG]] | +0.51 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[MMP2]] | +0.51 | +0.45 / +0.38 | both halves | 7e-05 | pathway: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); STRING 779 |
| [[FURIN]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[LAMB2]] | +0.51 | +0.50 / +0.38 | both halves | 6e-05 | pathway: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| [[LENG8]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[GPR84-AS1]] | +0.51 | +0.34 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL46]] | -0.47 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[TRIM16L-1]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[CDIN1]] | -0.45 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[IWS1]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[PIGBOS1]] | -0.44 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[DENND1B]] | -0.44 | -0.46 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[TRIM16]] | -0.43 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[MAGEF1]] | -0.43 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[METTL2A]] | -0.43 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[RDH14]] | -0.42 | -0.39 / -0.26 | both halves | 3e-04 |  |
| [[AGGF1]] | -0.42 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[PSMA4]] | -0.42 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[GCLM]] | -0.42 | -0.46 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITM2C]] | B | IGF2 activity raises ITM2C's level | lines that do not express IGF2 (32) vs lines expressing it (18) | 1.52× lower at baseline in the lines without IGF2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF334, ENSG00000239268, CARMN |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.489). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.6, 18.2); signed map (24.3, 44.5). **Vector** length 30.1, 7.00% of its response variance represented; |z| ≥ 3 in 196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.8 | +4.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +0.7 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.1 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.7 | -0.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:2,129,112-2,158,391 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44734, IGF-II; previously C11orf43 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Neuropeptides; Insulin family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 16 pathways, smallest: Insulin-like Growth Factor-2 mRNA Binding Proteins (IGF2BPs/IMPs/VICKZs) bind RNA; SHC-related events triggered by IGF1R; CHD6, CHD7, CHD8, CHD9 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [P01344](https://www.uniprot.org/uniprotkb/P01344) (Insulin-like growth factor 2):

> The insulin-like growth factors possess growth-promoting activity (By similarity). Major fetal growth hormone in mammals. Plays a key role in regulating fetoplacental development. IGF2 is influenced by placental lactogen. Also involved in tissue differentiation. In adults, involved in glucose metabolism in adipose tissue, skeletal muscle and liver (Probable). Acts as a ligand for integrin which is required for IGF2 signaling. Positively regulates myogenic transcription factor MYOD1 function by …

**Summary**, from NCBI Gene [3481](https://www.ncbi.nlm.nih.gov/gene/3481):

> This gene encodes a member of the insulin family of polypeptide growth factors, which are involved in development and growth. It is an imprinted gene, expressed only from the paternal allele, and epigenetic changes at this locus are associated with Wilms tumour, Beckwith-Wiedemann syndrome, rhabdomyosarcoma, and Silver-Russell syndrome. A read-through INS-IGF2 gene exists, whose 5' region overlaps the INS gene and the 3' region overlaps this gene. Alternatively spliced transcript variants …

**Accessions** — [HGNC:5466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5466) · Entrez [3481](https://www.ncbi.nlm.nih.gov/gene/3481) · UniProt [P01344](https://www.uniprot.org/uniprotkb/P01344) · Ensembl [ENSG00000167244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167244)

## Data

Gene col 9440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9440); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9440]; `tensor/DDL_lfc|DDL_z.npy` [9440]; `embed/gene_vectors.npy` [9440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9440 or target_col == 9440). Every well: [[IGF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
