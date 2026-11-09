---
symbol: "SUCLA2"
type: "gene"
col: 5818
ensembl_id: "ENSG00000136143"
name: "succinate-CoA ligase ADP-forming subunit beta"
location: "13q14.2"
module: 3
arm: "-"
pooled_cpm: 66.68
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SUCLA2

*succinate-CoA ligase ADP-forming subunit beta* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.36× (z +8.8, q 8e-16, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.02× (z +7.4, q 5e-11, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.809× (z -4.3, q 0.010, down in 24 of 48 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.254×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.208×; ⚠ toxic); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H661 0.102×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW 1271 0.106×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIP12]] (+0.64, fdr 2e-05), [[TARDBP]] (+0.63, fdr 2e-05), [[ERMAP]] (+0.61, fdr 3e-05); moves opposite to [[CCDC107]] (-0.61, fdr 1e-05), [[ARID3A]] (-0.58, fdr 1e-05), [[ANKRD37]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APPAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +8.8 | 8e-16 | 38/48 (LS 180, HCT15, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +7.4 | 5e-11 | 38/49 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +6.8 | 2e-09 | 27/49 (AsPC-1, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.6 | 4e-06 | 22/48 (LOX-IMVI, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.3 | 1e-05 | 25/48 (A-172, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 6e-05 | 24/48 (HCT15, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +4.9 | 8e-05 | 29/47 (COLO 205, SNU-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.9 | 8e-05 | 28/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +4.8 | 8e-05 | 23/45 (HOP62, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.27×** | +4.8 | 9e-05 | 24/48 (LS 180, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.7 | 2e-04 | 21/42 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.2 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.22×** | +4.0 | 0.003 | 22/48 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 20/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **1.24×** | +3.7 | 0.007 | 19/49 (HOP62, RKO, …) | all doses, flat | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.039 | 9/48 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.12× | +3.2 | 0.039 | 3/48 (HS-578T, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5818.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.254×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.208×; ⚠ toxic); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H661 0.102×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW 1271 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.809×** | -4.3 | 0.010 | 24/48 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 123 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 53.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +16.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 72.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.1) | — |
| [[A498 (line)]] | wt | 50.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.7) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[AsPC-1 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.3) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[C-33 A (line)]] | alt | 48.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.208× (z -10.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 85.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.7) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[LOX-IMVI (line)]] | wt | 77.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 88.5 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.80× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 44.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 68.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.8) | — |
| [[NCI-H661 (line)]] | alt | 74.0 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.102× (z -9.8) |
| [[RKO (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -12.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 69.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 67.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.106× (z -9.4) |
| [[A-172 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 106 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 135 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP12]] | +0.64 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[TARDBP]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ERMAP]] | +0.61 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ANKAR]] | +0.61 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[AP5M1]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[RCBTB2]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ARPP19]] | +0.59 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[SMU1]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CHMP3]] | +0.59 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[HNRNPM]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CLHC1]] | +0.58 | +0.60 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC107]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ARID3A]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PPP2R5B]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[C7orf57]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[EML2]] | -0.55 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CDK2AP2]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[MINDY2]] | -0.54 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[SH3GL3]] | -0.54 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[CDKN2D]] | -0.54 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[UBE2Q2P2]] | -0.54 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[HEBP1]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APPAT]] | B | APPAT activity raises SUCLA2's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without APPAT | 0.012 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-53.2, 16.9); signed map (18.5, -37.7). **Vector** length 103, 25.0% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.7 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.8 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.8 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | +0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.7 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | succinate-CoA ligase ADP-forming subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:47,745,736-48,037,968 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LINC00444 |
| Gene groups (HGNC) | Succinate-CoA ligase subunits; ATP-grasp fold containing |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2R7](https://www.uniprot.org/uniprotkb/Q9P2R7) (Succinate--CoA ligase):

> ATP-specific succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of ATP and thus represents the only step of substrate-level phosphorylation in the TCA. The beta subunit provides nucleotide specificity of the enzyme and binds the substrate succinate, while the binding sites for coenzyme A and phosphate are found in the alpha subunit (By similarity). Also able to act as an ATP-specific itaconyl- and malyl-CoA synthetase.

**Summary**, from NCBI Gene [8803](https://www.ncbi.nlm.nih.gov/gene/8803):

> Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate to succinyl-CoA. Defects in this gene are a cause of myopathic mitochondrial DNA depletion syndrome. …

**Accessions** — [HGNC:11448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11448) · Entrez [8803](https://www.ncbi.nlm.nih.gov/gene/8803) · UniProt [Q9P2R7](https://www.uniprot.org/uniprotkb/Q9P2R7) · Ensembl [ENSG00000136143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136143)

## Data

Gene col 5818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5818); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5818]; `tensor/DDL_lfc|DDL_z.npy` [5818]; `embed/gene_vectors.npy` [5818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5818 or target_col == 5818). Every well: [[SUCLA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUCLA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
