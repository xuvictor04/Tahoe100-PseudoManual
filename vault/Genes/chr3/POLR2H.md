---
symbol: "POLR2H"
type: "gene"
col: 8801
ensembl_id: "ENSG00000163882"
name: "RNA polymerase II, I and III subunit H"
location: "3q27.1"
module: 24
arm: "+"
pooled_cpm: 32.24
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# POLR2H

*RNA polymerase II, I and III subunit H* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.90× (z +6.7, q 1e-08, up in 36 of 45 measured lines) ⚠ transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.43× (z +5.3, q 2e-05, up in 31 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.0678×, A-427 0.103×, hTERT-HPNE 0.0939×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.102×, A-427 0.176×, J82 0.288×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.110×, C-33 A 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMP3]] (+0.73, fdr 2e-05), [[LAGE3]] (+0.72, fdr 3e-05), [[NUDT22]] (+0.70, fdr 1e-05); moves opposite to [[EWSR1]] (-0.63, fdr 3e-05), [[EIF3F]] (-0.59, fdr 4e-05), [[PAPOLA]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +6.7 | 1e-08 | 36/45 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.9 | 1e-06 | 36/45 (A498, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.3 | 2e-05 | 31/48 (MIA PaCa-2, KATO III, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.64×** | +5.2 | 3e-05 | 35/48 (COLO 205, NCI-H2347, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.53×** | +4.4 | 1e-03 | 31/48 (COLO 205, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.50×** | +4.3 | 0.002 | 29/47 (COLO 205, C-33 A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.46×** | +3.9 | 0.006 | 31/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.016 | 27/48 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.42×** | +3.6 | 0.017 | 26/48 (AsPC-1, NCI-H2347, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.93×** | +3.4 | 0.034 | 24/46 (SW480, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.92×** | +3.4 | 0.034 | 27/48 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +3.3 | 0.052 | 25/48 (A498, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.38×** | +3.2 | 0.054 | 22/48 (A498, LS 180, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.095 | 19/47 (A-172, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.35×** | +3.0 | 0.095 | 23/47 (A498, LS 180, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.097 | 20/47 (KATO III, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.0678×, A-427 0.103×, hTERT-HPNE 0.0939×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.102×, A-427 0.176×, J82 0.288×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.110×, C-33 A 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.487× | -3.4 | 0.38 | 23/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.751× | -3.0 | 0.46 | 19/48 (AsPC-1, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 67.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 50.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0678× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0939× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 45.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 14 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMP3]] | +0.73 | +0.48 / +0.77 | both halves | 2e-05 | STRING 569 |
| [[LAGE3]] | +0.72 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[NUDT22]] | +0.70 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[UQCC3]] | +0.69 | +0.37 / +0.76 | both halves | 8e-05 |  |
| [[CIAO2B]] | +0.67 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[C19orf81]] | +0.66 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[MINCR]] | +0.66 | +0.34 / +0.69 | both halves | 1e-04 |  |
| [[DCXR]] | +0.66 | +0.32 / +0.77 | both halves | 2e-04 |  |
| [[B3GAT3]] | +0.66 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[RPP21]] | +0.65 | +0.40 / +0.70 | both halves | 5e-05 |  |
| [[TMEM134]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TRPT1]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.63 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[EIF3F]] | -0.59 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[PAPOLA]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[ILF3]] | -0.58 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[PSMD11]] | -0.57 | -0.42 / -0.61 | both halves | 4e-05 | pathway: HIV Infection |
| [[CAPRIN1]] | -0.56 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[SLC25A24]] | -0.56 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[UBQLN1]] | -0.56 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[SMARCD1]] | -0.55 | -0.42 / -0.59 | both halves | 4e-05 | pathway: Affinity selection of immunoglobulins |
| [[LIN7C]] | -0.55 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[DHFR]] | -0.55 | -0.23 / -0.60 | both halves | 5e-04 |  |
| [[MAPK9]] | -0.55 | -0.41 / -0.67 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises POLR2H's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.34× lower at baseline in the lines without HES6 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HES7]] | B | HES7 activity raises POLR2H's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.19× lower at baseline in the lines without HES7 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers POLR2H's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.7, -19.4); signed map (-30.5, 10.0). **Vector** length 90.4, 26.2% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.5 | +5.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.0 | +3.7 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.0 | +4.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +1.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -8.8 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -8.3 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -7.9 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II, I and III subunit H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,361,710-184,368,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPB8 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR, UV_RESPONSE_UP |
| Reactome | 94 pathways, smallest: RNA Polymerase III Chain Elongation; Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P52434](https://www.uniprot.org/uniprotkb/P52434) (DNA-directed RNA polymerases I, II, and III subunit RPABC3):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Common component of RNA polymerases I, II and III which synthesize ribosomal RNA precursors, mRNA precursors and many functional non-coding RNAs, and small RNAs, such as 5S rRNA and tRNAs, respectively.

**Summary**, from NCBI Gene [5437](https://www.ncbi.nlm.nih.gov/gene/5437):

> The three eukaryotic RNA polymerases are complex multisubunit enzymes that play a central role in the transcription of nuclear genes. This gene encodes an essential and highly conserved subunit of RNA polymerase II that is shared by the other two eukaryotic DNA-directed RNA polymerases, I and III. Alternative splicing results in multiple transcript variants of this gene. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:9195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9195) · Entrez [5437](https://www.ncbi.nlm.nih.gov/gene/5437) · UniProt [P52434](https://www.uniprot.org/uniprotkb/P52434) · Ensembl [ENSG00000163882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163882)

## Data

Gene col 8801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8801); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8801]; `tensor/DDL_lfc|DDL_z.npy` [8801]; `embed/gene_vectors.npy` [8801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8801 or target_col == 8801). Every well: [[POLR2H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
