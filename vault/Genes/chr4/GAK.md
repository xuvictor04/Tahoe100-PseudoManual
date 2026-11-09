---
symbol: "GAK"
type: "gene"
col: 10977
ensembl_id: "ENSG00000178950"
name: "cyclin G associated kinase"
location: "4p16.3"
module: 52
arm: "+"
pooled_cpm: 84.73
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# GAK

*cyclin G associated kinase* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.07× (z +9.3, q 1e-17, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.737× (z -4.7, q 0.002, down in 25 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.832× (z -4.1, q 0.010, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.174×, SW48 0.185×, SW480 0.325×, HEC-1-A 0.351×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.511×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.543×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFGAP1]] (+0.70, fdr 7e-06), [[TMEM104]] (+0.69, fdr 1e-05), [[GSDMB]] (+0.67, fdr 1e-05); moves opposite to [[WAC-AS1]] (-0.62, fdr 3e-05), [[ZNF518A]] (-0.61, fdr 3e-05), [[KIAA1586]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMAD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +9.3 | 1e-17 | 46/49 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +7.8 | 2e-12 | 39/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +7.5 | 1e-11 | 39/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +6.9 | 7e-10 | 41/48 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +6.5 | 9e-09 | 36/48 (HCT15, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +5.8 | 7e-07 | 37/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +5.1 | 2e-05 | 29/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +4.9 | 7e-05 | 31/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +4.6 | 2e-04 | 30/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.2 | 0.002 | 26/48 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.016 | 26/48 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.059 | 23/48 (SNU-423, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.065 | 26/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.098 | 23/48 (HEC-1-A, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10977.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.174×, SW48 0.185×, SW480 0.325×, HEC-1-A 0.351×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.511×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.543×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.737×** | -4.7 | 0.002 | 25/43 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.832×** | -4.1 | 0.010 | 25/48 (Hs 766T, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.802×** | -3.5 | 0.081 | 23/48 (HT-29, KATO III, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.806×** | -3.4 | 0.081 | 24/49 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (drug)]] 0.05 µM |  | 0.822× | -3.1 | 0.21 | 18/48 (C32, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.828× | -3.0 | 0.22 | 16/48 (KATO III, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 69.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +8.9) | — |
| [[KATO III (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 82.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.68× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 85.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.80× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 54.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.97× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 67.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 66.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.34× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 85.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 97.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP1]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 | pathway: Clathrin-mediated endocytosis |
| [[TMEM104]] | +0.69 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[GSDMB]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[FUBP3]] | +0.67 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[RER1]] | +0.67 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[YKT6]] | +0.66 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[VPS53]] | +0.66 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[LPCAT1]] | +0.65 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SEC13]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 | STRING 486 |
| [[DPH7]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SEC61A1]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[EPN1]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 | pathway: Clathrin-mediated endocytosis; STRING 758 |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WAC-AS1]] | -0.62 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[ZNF518A]] | -0.61 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[KIAA1586]] | -0.59 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TAF9]] | -0.58 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[FBXL3]] | -0.58 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[HHLA3]] | -0.57 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MARCHF7]] | -0.57 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[CMTR2]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[NFYB]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DPH6-DT]] | -0.56 | -0.61 / -0.36 | both halves | 9e-05 |  |
| [[RBM43]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TRMT5]] | -0.55 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD9]] | B | SMAD9 activity strengthens GAK's drug response | lines that do not express SMAD9 (11) vs lines expressing it (38) | the lines without SMAD9 respond 0.76× as strongly (z diff +1.46); strongest at Panobinostat 5 µM: 1.31x vs 1.68x (z diff +2.5) | 0.085 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.3, -27.5); signed map (-49.4, 3.5). **Vector** length 99.8, 27.2% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +6.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.0 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -6.5 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.9 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin G associated kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:849,276-932,373 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNAJC26 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; C2 tensin-type domain containing; Numb-associated kinase family |
| Reactome | 5 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O14976](https://www.uniprot.org/uniprotkb/O14976) (Cyclin-G-associated kinase):

> Associates with cyclin G and CDK5. Seems to act as an auxilin homolog that is involved in the uncoating of clathrin-coated vesicles by Hsc70 in non-neuronal cells. Expression oscillates slightly during the cell cycle, peaking at G1. May play a role in clathrin-mediated endocytosis and intracellular trafficking, and in the dynamics of clathrin assembly/disassembly.

**Summary**, from NCBI Gene [2580](https://www.ncbi.nlm.nih.gov/gene/2580):

> In all eukaryotes, the cell cycle is governed by cyclin-dependent protein kinases (CDKs), whose activities are regulated by cyclins and CDK inhibitors in a diverse array of mechanisms that involve the control of phosphorylation and dephosphorylation of Ser, Thr or Tyr residues. Cyclins are molecules that possess a consensus domain called the 'cyclin box.' In mammalian cells, 9 cyclin species have been identified, and they are referred to as cyclins A through I. Cyclin G is a direct …

**Accessions** — [HGNC:4113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4113) · Entrez [2580](https://www.ncbi.nlm.nih.gov/gene/2580) · UniProt [O14976](https://www.uniprot.org/uniprotkb/O14976) · Ensembl [ENSG00000178950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178950)

## Data

Gene col 10977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10977); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10977]; `tensor/DDL_lfc|DDL_z.npy` [10977]; `embed/gene_vectors.npy` [10977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10977 or target_col == 10977). Every well: [[GAK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
