---
symbol: "UQCRC1"
type: "gene"
col: 202
ensembl_id: "ENSG00000010256"
name: "ubiquinol-cytochrome c reductase core protein 1"
location: "3p21.31"
module: 29
arm: "+"
pooled_cpm: 51.1
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# UQCRC1

*ubiquinol-cytochrome c reductase core protein 1* — 3p21.31

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +11.0, q 1e-25, up in 43 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A-172 4.10×, PANC-1 3.43×, NCI-H460 3.62×, SW480 3.05×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 3.81×, LoVo 3.66×, NCI-H460 3.35×, PANC-1 3.04×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.343×, NCI-H2347 0.541×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.286×, SW48 0.249×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.257×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM106C]] (+0.62, fdr 1e-05), [[LTA4H]] (+0.60, fdr 2e-05), [[ALDOA]] (+0.59, fdr 4e-05); moves opposite to [[EIF3J]] (-0.58, fdr 2e-05), [[CDR2]] (-0.57, fdr 3e-05), [[MYH3]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HACE1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A-172 4.10×, PANC-1 3.43×, NCI-H460 3.62×, SW480 3.05×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 3.81×, LoVo 3.66×, NCI-H460 3.35×, PANC-1 3.04×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.46×** | +11.0 | 1e-25 | 43/47 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.27×** | +9.7 | 1e-19 | 34/41 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.63×** | +5.6 | 5e-06 | 38/45 (C-33 A, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.36×** | +3.8 | 0.019 | 27/47 (Hs 766T, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.28× | +3.0 | 0.26 | 18/48 (RKO, SK-MEL-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.343×, NCI-H2347 0.541×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.286×, SW48 0.249×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.257×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyurea (drug)]] 5 µM |  | 0.764× | -3.1 | 0.35 | 21/48 (A-172, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.767× | -3.0 | 0.35 | 23/47 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.621× | -3.0 | 0.35 | 21/48 (HEC-1-A, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 60.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -10.7) |
| [[A549 (line)]] | wt | 35.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 56.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 59.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 36.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 40.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 43.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A498 (line)]] | wt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[H4 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HT-29 (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 51.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LS 180 (line)]] | wt | 81.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW48 (line)]] | wt | 70.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -9.3) |
| [[SW480 (line)]] | alt | 75.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[AN3 CA (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM106C]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.60 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ALDOA]] | +0.59 | +0.59 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 609 |
| [[ATP5MC3]] ⚠ | +0.59 | +0.42 / +0.56 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 614; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1B]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 969 |
| [[ALAD]] | +0.59 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ATP5F1A]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 970 |
| [[MDH2]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 921 |
| [[BRK1]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[OXA1L]] | +0.57 | +0.44 / +0.48 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 504 |
| [[MPP1]] | +0.57 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[LDHA]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 464 |
| [[BSG]] | +0.57 | +0.60 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3J]] | -0.58 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[CDR2]] | -0.57 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[MYH3]] | -0.55 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[MAFG]] | -0.54 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[EXOSC6]] | -0.54 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[TLNRD1]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[LTO1]] | -0.53 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SLC16A1-AS1]] | -0.53 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[PCF11]] | -0.53 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[SMCO2]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[USP36]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ZNF621]] | -0.52 | -0.41 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACE1]] | C | HACE1 activity raises UQCRC1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.44× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.465). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-20.1, -17.2); signed map (-36.9, -28.8). **Vector** length 56.6, 12.5% of its response variance represented; |z| ≥ 3 in 503 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +2.0 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -3.0 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -2.9 | +5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase core protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,599,002-48,610,976 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D3S3191, QCR1, UQCR1 |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits; M16 metallopeptidases |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P31930](https://www.uniprot.org/uniprotkb/P31930) (Cytochrome b-c1 complex subunit 1, mitochondrial):

> Component of the ubiquinol-cytochrome c oxidoreductase, a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular …

**Summary**, from NCBI Gene [7384](https://www.ncbi.nlm.nih.gov/gene/7384):

> Enables ubiquitin protein ligase binding activity. Predicted to be involved in obsolete protein processing involved in protein targeting to mitochondrion. Predicted to act upstream of or within mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrial inner membrane. Implicated in Alzheimer's disease and late onset Parkinson's disease. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12585) · Entrez [7384](https://www.ncbi.nlm.nih.gov/gene/7384) · UniProt [P31930](https://www.uniprot.org/uniprotkb/P31930) · Ensembl [ENSG00000010256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010256)

## Data

Gene col 202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 202); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 202]; `tensor/DDL_lfc|DDL_z.npy` [202]; `embed/gene_vectors.npy` [202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 202 or target_col == 202). Every well: [[UQCRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
