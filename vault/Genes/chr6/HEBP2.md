---
symbol: "HEBP2"
type: "gene"
col: 581
ensembl_id: "ENSG00000051620"
name: "heme binding protein 2"
location: "6q24.1"
module: 3
arm: "+"
pooled_cpm: 49.76
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HEBP2

*heme binding protein 2* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +10.1, q 5e-21, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SNU-423 3.80×, PANC-1 3.71×, A-427 5.73×, HEC-1-A 3.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 3.87×, SW480 3.29×, PANC-1 3.42×, SW 900 4.37×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.379× (z -12.4, q 1e-32, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PINK1]] (+0.63, fdr 9e-06), [[RALBP1]] (+0.63, fdr 1e-05), [[CAMLG]] (+0.61, fdr 1e-05); moves opposite to [[SF3B3]] (-0.57, fdr 1e-05), [[HNRNPL]] (-0.53, fdr 2e-05), [[PTBP1]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C19orf33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 581.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SNU-423 3.80×, PANC-1 3.71×, A-427 5.73×, HEC-1-A 3.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 3.87×, SW480 3.29×, PANC-1 3.42×, SW 900 4.37×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +10.1 | 5e-21 | 43/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +7.7 | 5e-12 | 29/38 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +4.8 | 2e-04 | 29/39 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.55×** | +4.1 | 0.006 | 35/45 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.379×** | -12.4 | 1e-32 | 41/47 (RKO, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -6.7 | 7e-09 | 40/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.511×** | -6.2 | 9e-08 | 43/47 (AsPC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.584×** | -5.0 | 1e-04 | 41/47 (AsPC-1, A-172, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.855× | -4.8 | 2e-04 | 13/48 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -4.7 | 2e-04 | 33/47 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.602×** | -4.7 | 2e-04 | 36/47 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -4.3 | 0.001 | 36/48 (LoVo, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -4.1 | 0.003 | 34/47 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -3.8 | 0.008 | 33/47 (NCI-H460, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.020 | 23/47 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -3.4 | 0.034 | 28/47 (SNU-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 58.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -13.8) |
| [[HOP62 (line)]] | alt | 43.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 38.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -12.9) |
| [[PANC-1 (line)]] | alt | 61.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.5) |
| [[A-427 (line)]] | wt | 32.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 60.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.0) |
| [[RKO (line)]] | wt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -25.4) |
| [[SW 900 (line)]] | alt | 42.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.9) |
| [[SW480 (line)]] | alt | 47.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 58.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.8) |
| [[A549 (line)]] | wt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.9) |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 57.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.8) |
| [[HS-578T (line)]] | alt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.4) |
| [[J82 (line)]] | alt | 29.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.9) |
| [[KATO III (line)]] | alt | 64.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 81.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.8) |
| [[LS 180 (line)]] | wt | 86.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 55.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 44.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 53.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -11.5) |
| [[SNU-423 (line)]] | alt | 87.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 47.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -9.2) |
| [[A498 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PINK1]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[RALBP1]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CAMLG]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CCNDBP1]] | +0.60 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[DHRS7]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CSTB]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[KLHL7]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MACO1]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CCDC126]] | +0.57 | +0.37 / +0.42 | both halves | 8e-05 |  |
| [[RALA]] | +0.57 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ARF5]] | +0.57 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B3]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PTBP1]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[HNRNPAB]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ERH]] | -0.52 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PFAS]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[C1QBP]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PSME3]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[METTL1]] | -0.51 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[NUP188]] | -0.51 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[REXO1]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[DNMT1]] | -0.51 | -0.46 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C19orf33]] | B | C19orf33 activity raises HEBP2's level | lines that do not express C19orf33 (19) vs lines expressing it (31) | 1.49× lower at baseline in the lines without C19orf33 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.3, -26.5); signed map (-20.9, 9.8). **Vector** length 66.7, 19.2% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | heme binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1 — chr6:138,403,531-138,422,197 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SOUL; previously C6orf34 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Z4](https://www.uniprot.org/uniprotkb/Q9Y5Z4) (Heme-binding protein 2):

> Can promote mitochondrial permeability transition and facilitate necrotic cell death under different types of stress conditions.

**Summary**, from NCBI Gene [23593](https://www.ncbi.nlm.nih.gov/gene/23593):

> The protein encoded by this gene is found predominately in the cytoplasm, where it plays a role in the collapse of mitochondrial membrane potential (MMP) prior to necrotic cell death. The encoded protein enhances outer and inner mitochondrial membrane permeabilization, especially under conditions of oxidative stress. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:15716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15716) · Entrez [23593](https://www.ncbi.nlm.nih.gov/gene/23593) · UniProt [Q9Y5Z4](https://www.uniprot.org/uniprotkb/Q9Y5Z4) · Ensembl [ENSG00000051620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051620)

## Data

Gene col 581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 581); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 581]; `tensor/DDL_lfc|DDL_z.npy` [581]; `embed/gene_vectors.npy` [581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 581 or target_col == 581). Every well: [[HEBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
