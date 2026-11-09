---
symbol: "BRF2"
type: "gene"
col: 2429
ensembl_id: "ENSG00000104221"
name: "BRF2 general transcription factor IIIB subunit"
location: "8p11.23"
module: 12
arm: "+"
pooled_cpm: 6.64
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# BRF2

*BRF2 general transcription factor IIIB subunit* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 4.31× (z +18.8, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.714× (z -6.5, q 5e-08, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYG1]] (+0.73, fdr 7e-06), [[POLR2C]] (+0.72, fdr 7e-06), [[RBSN]] (+0.70, fdr 7e-06); moves opposite to [[FAM81A]] (-0.60, fdr 1e-05), [[EPB41L2]] (-0.56, fdr 1e-05), [[TFRC]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2429.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **4.31×** | +18.8 | 0e+00 | 43/43 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.36×** | +16.5 | 0e+00 | 42/45 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.31×** | +16.3 | 0e+00 | 44/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +11.4 | 5e-28 | 37/45 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +8.8 | 1e-16 | 26/41 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.19×** | +8.2 | 2e-14 | 21/25 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +7.6 | 2e-12 | 18/42 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.21×** | +7.2 | 4e-11 | 27/45 (SW480, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +6.6 | 2e-09 | 20/45 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +6.1 | 8e-08 | 15/38 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 8e-06 | 18/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.29×** | +3.5 | 0.026 | 7/41 (J82, A498, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.051 | 8/35 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.25× | +3.0 | 0.11 | 7/45 (HS-578T, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2429.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -6.5 | 5e-08 | 23/43 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -4.5 | 0.002 | 19/40 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.736×** | -4.2 | 0.006 | 20/31 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -4.0 | 0.009 | 14/47 (A498, C-33 A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -3.8 | 0.016 | 16/38 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.742×** | -3.8 | 0.016 | 10/19 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -3.7 | 0.017 | 7/8 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.783×** | -3.3 | 0.061 | 15/43 (RPMI-7951, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.067 | 14/46 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 7.56 | 1 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.62× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.37 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -11.1) |
| [[SW480 (line)]] | alt | 7.44 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.22× (z +9.7) | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -12.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 7.78 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 5.36 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.26 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.307× (z -8.9) |
| [[KATO III (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.33× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 5.00 | 0 | 1 | — | [[Gallic acid (drug)]] 0.05 µM 0.104× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 5.09 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.123× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 5.01 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -9.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 8.66 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYG1]] | +0.73 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[POLR2C]] | +0.72 | +0.78 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 496 |
| [[RBSN]] | +0.70 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.70 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[ZFAND2A]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[PSMD3]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[SLC10A7]] | +0.66 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[SDE2]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[UBC]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZNF761]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.56 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[TFRC]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[CD9]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[PIGX]] | -0.55 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ADAM10]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BRF2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-41.7, -4.7); signed map (-23.5, -23.4). **Vector** length 85.9, 16.2% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +18.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.8 | +16.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.3 | +16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +11.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.3 | +8.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +0.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | -4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | BRF2 general transcription factor IIIB subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:37,843,268-37,849,861 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11052, BRFU, TFIIIB50 |
| Gene groups (HGNC) | General transcription factor IIIB complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 4 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 3 Promoter; RNA Polymerase III Transcription Initiation; RNA Polymerase III Abortive And Retractive Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAW0](https://www.uniprot.org/uniprotkb/Q9HAW0) (Transcription factor IIIB 50 kDa subunit):

> General activator of RNA polymerase III transcription. Factor exclusively required for RNA polymerase III transcription of genes with promoter elements upstream of the initiation sites. Contributes to the regulation of gene expression; functions as activator in the absence of oxidative stress. Down-regulates expression of target genes in response to oxidative stress. Overexpression protects cells against apoptosis in response to oxidative stress.

**Summary**, from NCBI Gene [55290](https://www.ncbi.nlm.nih.gov/gene/55290):

> This gene encodes one of the multiple subunits of the RNA polymerase III transcription factor complex required for transcription of genes with promoter elements upstream of the initiation site. The product of this gene, a TFIIB-like factor, is directly recruited to the TATA-box of polymerase III small nuclear RNA gene promoters through its interaction with the TATA-binding protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17298) · Entrez [55290](https://www.ncbi.nlm.nih.gov/gene/55290) · UniProt [Q9HAW0](https://www.uniprot.org/uniprotkb/Q9HAW0) · Ensembl [ENSG00000104221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104221)

## Data

Gene col 2429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2429); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2429]; `tensor/DDL_lfc|DDL_z.npy` [2429]; `embed/gene_vectors.npy` [2429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2429 or target_col == 2429). Every well: [[BRF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
