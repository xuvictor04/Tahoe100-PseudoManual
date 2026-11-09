---
symbol: "ATP5IF1"
type: "gene"
col: 5123
ensembl_id: "ENSG00000130770"
name: "ATP synthase inhibitory factor subunit 1"
location: "1p35.3"
module: 48
arm: "+"
pooled_cpm: 34.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ATP5IF1

*ATP synthase inhibitory factor subunit 1* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.17× (z +9.7, q 2e-19, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +4.4, q 0.001, up in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H460 5.95×, PANC-1 5.79×, SW480 5.10×, HEC-1-A 4.93×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 6.19×, PANC-1 5.81×, A-172 5.50×, NCI-H460 5.28×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.507× (z -4.6, q 0.003, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA2]] (+0.69, fdr 1e-05), [[COX5B]] (+0.66, fdr 2e-05), [[ARL6IP4]] (+0.66, fdr 7e-06); moves opposite to [[DDX21]] (-0.63, fdr 1e-05), [[GNL3L]] (-0.62, fdr 1e-05), [[PUM3]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5123.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H460 5.95×, PANC-1 5.79×, SW480 5.10×, HEC-1-A 4.93×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 6.19×, PANC-1 5.81×, A-172 5.50×, NCI-H460 5.28×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.17×** | +9.7 | 2e-19 | 42/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.16×** | +9.3 | 4e-18 | 36/36 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.38×** | +5.1 | 5e-05 | 33/40 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **2.12×** | +5.1 | 5e-05 | 40/45 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.4 | 0.001 | 36/47 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.0 | 0.005 | 40/45 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -4.6 | 0.003 | 39/47 (BT-474, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -3.5 | 0.089 | 32/48 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.668×** | -3.5 | 0.089 | 29/47 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.617× | -3.2 | 0.13 | 27/47 (Panc 03.27, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.324× | -3.2 | 0.13 | 32/45 (SW48, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.50× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 52.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 24.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Hs 766T (line)]] | wt | 47.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 7 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA2]] | +0.69 | +0.51 / +0.76 | both halves | 1e-05 | STRING 553 |
| [[COX5B]] | +0.66 | +0.47 / +0.74 | both halves | 2e-05 | STRING 707 |
| [[ARL6IP4]] | +0.66 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[NDUFB1]] | +0.65 | +0.37 / +0.80 | both halves | 7e-05 |  |
| [[ARF5]] | +0.63 | +0.30 / +0.71 | both halves | 2e-04 |  |
| [[IFI27L2]] | +0.63 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[DCAF5]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CWC15]] | +0.62 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[LAMTOR2]] | +0.61 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[UQCRQ]] ⚠ | +0.60 | +0.36 / +0.73 | both halves | 1e-04 | STRING 686; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB11]] ⚠ | +0.60 | +0.37 / +0.76 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX14]] | +0.60 | +0.38 / +0.69 | both halves | 7e-05 |  |
| [[NDUFC1]] | +0.60 | +0.45 / +0.80 | both halves | 3e-05 |  |
| [[CHCHD1]] | +0.60 | +0.41 / +0.71 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX21]] | -0.63 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.62 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[PUM3]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[PUS1]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.59 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[GART]] | -0.58 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[CPNE7]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PRMT3]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[MATR3-1]] | -0.57 | -0.32 / -0.62 | both halves | 1e-04 |  |
| [[NOLC1]] | -0.57 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[ZNF121]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SACS]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.2, -20.3); signed map (-37.7, 8.7). **Vector** length 51.0, 14.6% of its response variance represented; |z| ≥ 3 in 509 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.50 to 24); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.50 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +0.8 | +0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -2.8 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -2.7 | +9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -2.1 | +9.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase inhibitory factor subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,236,109-28,246,906 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATPI, IP, ATPIP, MGC1167, MGC8898; previously ATPIF1 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UII2](https://www.uniprot.org/uniprotkb/Q9UII2) (ATPase inhibitor, mitochondrial):

> Endogenous F(1)F(o)-ATPase inhibitor limiting ATP depletion when the mitochondrial membrane potential falls below a threshold and the F(1)F(o)-ATP synthase starts hydrolyzing ATP to pump protons out of the mitochondrial matrix. Required to avoid the consumption of cellular ATP when the F(1)F(o)-ATP synthase enzyme acts as an ATP hydrolase. Indirectly acts as a regulator of heme synthesis in erythroid tissues: regulates heme synthesis by modulating the mitochondrial pH and redox potential, …

**Summary**, from NCBI Gene [93974](https://www.ncbi.nlm.nih.gov/gene/93974):

> Enables several functions, including ATPase binding activity; angiostatin binding activity; and mitochondrial proton-transporting ATP synthase complex binding activity. Involved in several processes, including mitochondrial depolarization; negative regulation of cardiac muscle cell apoptotic process; and obsolete positive regulation of proteolysis involved in protein catabolic process. Located in cell surface and mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:871) · Entrez [93974](https://www.ncbi.nlm.nih.gov/gene/93974) · UniProt [Q9UII2](https://www.uniprot.org/uniprotkb/Q9UII2) · Ensembl [ENSG00000130770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130770)

## Data

Gene col 5123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5123); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5123]; `tensor/DDL_lfc|DDL_z.npy` [5123]; `embed/gene_vectors.npy` [5123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5123 or target_col == 5123). Every well: [[ATP5IF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5IF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
