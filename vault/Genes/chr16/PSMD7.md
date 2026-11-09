---
symbol: "PSMD7"
type: "gene"
col: 2306
ensembl_id: "ENSG00000103035"
name: "proteasome 26S subunit, non-ATPase 7"
location: "16q23.1"
module: 7
arm: "+"
pooled_cpm: 74.87
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PSMD7

*proteasome 26S subunit, non-ATPase 7* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.48× (z +11.5, q 1e-27, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.696× (z -4.6, q 0.002, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNTTIP2]] (+0.83, fdr 7e-06), [[ERCC4]] (+0.81, fdr 7e-06), [[CBLL1]] (+0.76, fdr 7e-06); moves opposite to [[NPTN]] (-0.65, fdr 7e-06), [[GM2A]] (-0.62, fdr 1e-05), [[GMCL1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.48×** | +11.5 | 1e-27 | 47/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.34×** | +10.4 | 6e-23 | 48/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.35×** | +10.4 | 6e-23 | 46/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.25×** | +10.3 | 2e-22 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.76×** | +10.1 | 7e-22 | 38/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +9.7 | 3e-20 | 47/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.53×** | +8.3 | 7e-15 | 46/49 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +7.8 | 3e-13 | 46/48 (C32, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +7.3 | 2e-11 | 45/48 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +7.3 | 2e-11 | 46/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +6.4 | 8e-09 | 42/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.61×** | +5.8 | 3e-07 | 34/49 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +5.6 | 8e-07 | 33/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.55×** | +5.5 | 1e-06 | 39/48 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.52×** | +5.1 | 1e-05 | 37/47 (LoVo, H4, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.010 | 27/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.019 | 26/48 (NCI-H460, SW 900, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.025 | 27/47 (HOP62, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.027 | 24/47 (NCI-H460, HOP62, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.030 | 27/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.036 | 24/48 (NCI-H1792, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.696×** | -4.6 | 0.002 | 32/48 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.706×** | -4.4 | 0.003 | 31/48 (NCI-H2030, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.780× | -3.2 | 0.30 | 24/48 (A-427, LoVo, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 79.9 | 9 (4 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.46× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 64.3 | 8 (4 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.83× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 65.2 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.52× (z +10.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.18× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 43.8 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.99× (z +10.6) | — |
| [[SW480 (line)]] | alt | 112 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +12.8) | — |
| [[A549 (line)]] | wt | 66.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.24× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 45.4 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.27× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 54.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.5) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 43.2 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.72× (z +11.0) | — |
| [[KATO III (line)]] | alt | 94.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +8.9) | — |
| [[LoVo (line)]] | wt | 58.2 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.93× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 58.1 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.01× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 59.8 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.32× (z +9.7) | — |
| [[C32 (line)]] | wt | 53.7 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.29× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 79.1 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.14× (z +9.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.08× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 172 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.54× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 63.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.8) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[AsPC-1 (line)]] | alt | 46.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.06× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 48.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.24× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 112 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.73× (z +8.6) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 59.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.73× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 44.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 79.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.9) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[A-172 (line)]] | wt | 99.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNTTIP2]] | +0.83 | +0.86 / +0.79 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.81 | +0.77 / +0.77 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[CBLL1]] | +0.76 | +0.80 / +0.63 | both halves | 7e-06 | pathway: Activation of STAT3 by cadherin engagement |
| [[TACO1]] | +0.75 | +0.82 / +0.57 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[ASF1A]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.72 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[POP4]] | +0.72 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PSMA4]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[ABRAXAS2]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 | pathway: Deubiquitination; STRING 662 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.65 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[GM2A]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.62 | -0.66 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PSMD7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.7, 9.0); signed map (-2.8, -24.2). **Vector** length 95.4, 34.7% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.4 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.9 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +3.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | -3.0 | +4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -0.1 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | -1.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:74,296,814-74,306,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S12, P40, MOV34, Rpn8 |
| Gene groups (HGNC) | Proteasome; JAMM/MPN+ metallopeptidase family |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [P51665](https://www.uniprot.org/uniprotkb/P51665) (26S proteasome non-ATPase regulatory subunit 7):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair.

**Summary**, from NCBI Gene [5713](https://www.ncbi.nlm.nih.gov/gene/5713):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9565) · Entrez [5713](https://www.ncbi.nlm.nih.gov/gene/5713) · UniProt [P51665](https://www.uniprot.org/uniprotkb/P51665) · Ensembl [ENSG00000103035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103035)

## Data

Gene col 2306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2306); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2306]; `tensor/DDL_lfc|DDL_z.npy` [2306]; `embed/gene_vectors.npy` [2306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2306 or target_col == 2306). Every well: [[PSMD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
