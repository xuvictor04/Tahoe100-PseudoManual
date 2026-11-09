---
symbol: "RAB5IF"
type: "gene"
col: 2068
ensembl_id: "ENSG00000101084"
name: "RAB5 interacting factor"
location: "20q11.23"
module: 36
arm: "+"
pooled_cpm: 35.06
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# RAB5IF

*RAB5 interacting factor* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (16 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.37× (z +8.0, q 8e-13, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.310×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2M]] (+0.73, fdr 7e-06), [[PSMB3]] (+0.70, fdr 7e-06), [[AURKAIP1]] (+0.67, fdr 8e-06); moves opposite to [[NOTCH2NLC]] (-0.57, fdr 4e-05), [[SF1]] (-0.57, fdr 3e-05), [[SETDB2]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NMRAL2P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +8.0 | 8e-13 | 44/48 (COLO 205, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.23×** | +7.4 | 4e-11 | 46/47 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.19×** | +7.3 | 7e-11 | 41/48 (COLO 205, HOP62, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.15×** | +7.1 | 2e-10 | 41/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **2.26×** | +7.0 | 4e-10 | 38/44 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.01×** | +6.5 | 1e-08 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.63×** | +6.4 | 1e-08 | 34/47 (A549, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.98×** | +6.1 | 9e-08 | 29/35 (A498, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.98×** | +6.1 | 9e-08 | 36/46 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.89×** | +5.9 | 2e-07 | 40/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.86×** | +5.7 | 5e-07 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.83×** | +5.6 | 1e-06 | 40/47 (A-172, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +5.4 | 3e-06 | 36/48 (KATO III, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.74×** | +5.1 | 1e-05 | 34/45 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.73×** | +5.1 | 1e-05 | 36/47 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.005 | 28/48 (A549, SNU-423, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.85×** | +3.0 | 0.078 | 19/48 (NCI-H460, HT-29, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2068.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.310×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.497× | -3.4 | 0.27 | 25/48 (CFPAC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.705× | -3.2 | 0.27 | 22/48 (SW 1088, CFPAC-1, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.522× | -3.2 | 0.27 | 21/48 (A498, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.717× | -3.1 | 0.27 | 22/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.535× | -3.0 | 0.27 | 22/47 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.78 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.26× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.12× (z +8.5) | — |
| [[A-427 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 77.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.27× (z +8.9) | — |
| [[A-172 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2M]] | +0.73 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[PSMB3]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[AURKAIP1]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[HIRA]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[FBXW11]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[VPS53]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TUSC2]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PGP]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TM2D2]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[VTI1A]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[VPS13D]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ARPC5L]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLC]] | -0.57 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[SF1]] | -0.57 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[SETDB2]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SUGT1P3]] | -0.55 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[CD83]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[CEP63]] | -0.53 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[AMZ2P1]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[KPNA5]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[NR1D1]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PAN2]] | -0.52 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[BPHL]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CCDC25]] | -0.52 | -0.49 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P]] | B | NMRAL2P activity raises RAB5IF's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.49× lower at baseline in the lines without NMRAL2P | 0.031 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-14.7, -9.0); signed map (-46.6, -22.6). **Vector** length 79.2, 23.9% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.2 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.8 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.4 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | RAB5 interacting factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,605,779-36,612,557 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PNAS-11, RIP5, RCAF1, OPTI; previously C20orf24 |
| Gene groups (HGNC) | GEL complex subunits |
| Reactome | 5 pathways, smallest: Complex IV assembly; Cotranslational targeting of proteins to the endoplasmic reticulum; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUV8](https://www.uniprot.org/uniprotkb/Q9BUV8) (GEL complex subunit OPTI):

> Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes. The MPT complex takes over after the SEC61 complex: following membrane insertion of the first few transmembrane segments of proteins by the SEC61 complex, the MPT complex occludes the lateral gate of the SEC61 complex to promote insertion of subsequent transmembrane regions. Within the MPT complex, the GEL subcomplex may mediate insertion of …

**Summary**, from NCBI Gene [55969](https://www.ncbi.nlm.nih.gov/gene/55969):

> Involved in mitochondrial respirasome assembly and multi-pass transmembrane protein insertion into ER membrane. Located in mitochondrion. Part of multi-pass translocon complex. Implicated in craniofacial dysmorphism, skeletal anomalies, and impaired intellectual development syndrome 2. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15870) · Entrez [55969](https://www.ncbi.nlm.nih.gov/gene/55969) · UniProt [Q9BUV8](https://www.uniprot.org/uniprotkb/Q9BUV8) · Ensembl [ENSG00000101084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101084)

## Data

Gene col 2068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2068); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2068]; `tensor/DDL_lfc|DDL_z.npy` [2068]; `embed/gene_vectors.npy` [2068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2068 or target_col == 2068). Every well: [[RAB5IF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB5IF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
