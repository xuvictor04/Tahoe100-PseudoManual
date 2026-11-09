---
symbol: "RDH11"
type: "gene"
col: 1001
ensembl_id: "ENSG00000072042"
name: "retinol dehydrogenase 11"
location: "14q24.1"
module: 86
arm: "+"
pooled_cpm: 50.76
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# RDH11

*retinol dehydrogenase 11* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +9.2, q 2e-17, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[4EGI-1 (drug)]] 0.5 µM: 0.661× (z -4.2, q 0.009, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.320×, MIA PaCa-2 0.484×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.322×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDFT1]] (+0.63, fdr 7e-06), [[HMGCR]] (+0.62, fdr 7e-06), [[ACSS2]] (+0.61, fdr 1e-05); moves opposite to [[ELFN2]] (-0.43, fdr 5e-05), [[SFPQ]] (-0.43, fdr 5e-04), [[SF1]] (-0.42, fdr 2e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02432]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.2 | 2e-17 | 39/48 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.81×** | +8.1 | 2e-13 | 40/48 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +7.4 | 2e-11 | 42/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +7.4 | 2e-11 | 39/48 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.38×** | +6.6 | 5e-09 | 33/48 (LoVo, HOP62, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.38×** | +6.5 | 7e-09 | 38/49 (LoVo, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.47×** | +5.4 | 7e-06 | 34/48 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.39×** | +4.6 | 4e-04 | 27/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.002 | 26/48 (NCI-H23, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.9 | 0.005 | 24/43 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.008 | 24/48 (CFPAC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.008 | 22/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.29×** | +3.7 | 0.011 | 23/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.012 | 27/48 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.021 | 23/48 (CHP-212, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.021 | 21/48 (A549, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.026 | 16/48 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.044 | 17/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.044 | 16/48 (HOP62, COLO 205, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1001.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.320×, MIA PaCa-2 0.484×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.322×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.661×** | -4.2 | 0.009 | 30/48 (KATO III, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.735×** | -4.2 | 0.009 | 26/48 (LS 180, HS-578T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.841× | -3.5 | 0.096 | 21/48 (A498, C32, …) | rises with dose | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.637× | -3.4 | 0.11 | 22/48 (SW480, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.642× | -3.3 | 0.11 | 18/48 (BT-474, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.648× | -3.2 | 0.11 | 24/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.790× | -3.2 | 0.11 | 20/47 (SW48, LS 180, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | 0.654× | -3.2 | 0.11 | 19/48 (LS 180, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | 0.741× | -3.1 | 0.14 | 17/48 (KATO III, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.809× | -3.0 | 0.15 | 13/48 (KATO III, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 112 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.499× (z -8.6) ⚠ cell-cycle shift, explains ~75% of this change |
| [[CFPAC-1 (line)]] | alt | 53.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 38.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +12.4) | — |
| [[LoVo (line)]] | wt | 43.6 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.26× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 30.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.36× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 54.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 38.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.1) | — |
| [[A-172 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDFT1]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[HMGCR]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ACSS2]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FDPS]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_PEROXISOME |
| [[SCD]] | +0.58 | +0.63 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[MSMO1]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[MVD]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[EBP]] | +0.56 | +0.48 / +0.62 | both halves | 2e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[STARD4]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ABCB6]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PNPLA3]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[LNPK]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELFN2]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[SFPQ]] | -0.43 | -0.23 / -0.49 | both halves | 5e-04 |  |
| [[SF1]] | -0.42 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[SLC24A1]] | -0.42 | -0.43 / -0.33 | both halves | 1e-04 | pathway: Sensory Perception |
| [[SCG2]] | -0.42 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[DNAH7]] | -0.42 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[SRSF10]] | -0.41 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[ST6GALNAC5]] | -0.41 | -0.43 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02432]] | B | LINC02432 activity lowers RDH11's level | lines that do not express LINC02432 (36) vs lines expressing it (14) | 1.33× higher at baseline in the lines without LINC02432 | 0.098 | ⚠ within organs, on part of the lines; also absent: TCN1, FGF19, TFF2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.2, -49.1); signed map (-53.4, 33.2). **Vector** length 117, 35.3% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Lanosterol biosynthesis* (reactome, mean cos +0.51 to 10); *PPARA activates gene expression* (reactome, mean cos +0.51 to 6); *Regulation of lipid metabolism by PPARalpha* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +8.1 |
|  | [[Berbamine (drug)]] 5 µM |  | +6.2 | +6.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +5.9 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.5 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -4.4 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -1.7 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.8 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.8 | -2.9 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | retinol dehydrogenase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:67,676,800-67,695,793 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MDT1, SDR7C1, ARSDR1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM, MTORC1_SIGNALING |
| Reactome | 9 pathways, smallest: The canonical retinoid cycle in rods (twilight vision); RA biosynthesis pathway; Retinoid metabolism and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC12](https://www.uniprot.org/uniprotkb/Q8TC12) (Retinol dehydrogenase 11):

> Retinol dehydrogenase with a clear preference for NADP. Displays high activity towards 9-cis, 11-cis and all-trans-retinol, and to a lesser extent on 13-cis-retinol. Exhibits a low reductive activity towards unsaturated medium-chain aldehydes such as cis -6-nonenal and no activity toward nonanal or 4-hydroxy-nonenal. Has no dehydrogenase activity towards steroid.

**Summary**, from NCBI Gene [51109](https://www.ncbi.nlm.nih.gov/gene/51109):

> Enables all-trans-retinol dehydrogenase (NADP+) activity. Involved in cellular detoxification of aldehyde and retinoid metabolic process. Acts upstream of or within retinal metabolic process. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17964) · Entrez [51109](https://www.ncbi.nlm.nih.gov/gene/51109) · UniProt [Q8TC12](https://www.uniprot.org/uniprotkb/Q8TC12) · Ensembl [ENSG00000072042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072042)

## Data

Gene col 1001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1001); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1001]; `tensor/DDL_lfc|DDL_z.npy` [1001]; `embed/gene_vectors.npy` [1001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1001 or target_col == 1001). Every well: [[RDH11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RDH11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
