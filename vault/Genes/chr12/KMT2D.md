---
symbol: "KMT2D"
type: "gene"
col: 9485
ensembl_id: "ENSG00000167548"
name: "lysine methyltransferase 2D"
location: "12q13.12"
module: 5
arm: "+"
pooled_cpm: 87.09
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# KMT2D

*lysine methyltransferase 2D* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.81× (z +8.6, q 4e-15, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.439× (z -12.1, q 1e-30, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCFC1]] (+0.74, fdr 7e-06), [[TOR1A]] (+0.70, fdr 7e-06), [[PRCC]] (+0.69, fdr 7e-06); moves opposite to [[UGCG]] (-0.64, fdr 2e-05), [[RYBP]] (-0.59, fdr 1e-05), [[UBE2B]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DUSP5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +8.6 | 4e-15 | 45/48 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +6.8 | 2e-09 | 39/48 (NCI-H1573, SW48, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +5.8 | 1e-06 | 41/48 (COLO 205, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.6 | 7e-04 | 23/49 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.004 | 32/48 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.004 | 25/48 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.0 | 0.006 | 30/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.009 | 24/49 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.011 | 31/48 (A498, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.013 | 28/48 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.091 | 23/48 (SW48, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9485.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.439×** | -12.1 | 1e-30 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.450×** | -11.7 | 3e-29 | 47/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.603×** | -7.4 | 2e-11 | 42/48 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.726×** | -6.7 | 4e-09 | 46/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.663×** | -5.6 | 3e-06 | 31/45 (H4, RKO, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.727×** | -4.7 | 3e-04 | 35/49 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.754×** | -4.2 | 0.002 | 30/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.783×** | -3.6 | 0.021 | 27/48 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.793×** | -3.4 | 0.038 | 24/49 (A-427, NCI-H23, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 161 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.401× (z -9.3) |
| [[BT-474 (line)]] | alt | 89.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -11.9) |
| [[J82 (line)]] | alt | 73.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 144 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -11.4) |
| [[LS 180 (line)]] | wt | 89.5 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.389× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 99.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -9.4) |
| [[RKO (line)]] | wt | 90.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -9.7) |
| [[SW1417 (line)]] | alt | 86.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -11.3) |
| [[SW480 (line)]] | alt | 114 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -11.9) |
| [[A-427 (line)]] | wt | 164 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.465× (z -8.7) |
| [[C-33 A (line)]] | alt | 118 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -10.8) |
| [[KATO III (line)]] | alt | 88.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 137 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 93.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.439× (z -9.9) |
| [[PANC-1 (line)]] | alt | 86.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.460× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 95.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.415× (z -8.6) |
| [[A-172 (line)]] | wt | 73.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 66.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.444× (z -8.7) |
| [[C32 (line)]] | wt | 71.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -9.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[COLO 205 (line)]] | alt | 71.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.00× (z +8.7) | — |
| [[H4 (line)]] | wt | 83.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 85.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -10.5) |
| [[HT-29 (line)]] | alt | 82.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.315× (z -10.4) |
| [[LoVo (line)]] | wt | 127 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.454× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 61.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.360× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 54.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 62.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.546× (z -8.7) |
| [[SW48 (line)]] | wt | 100.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -9.9) |
| [[A549 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 | pathway: Chromatin modifying enzymes; STRING 599 |
| [[TOR1A]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PRCC]] | +0.69 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ZNF142]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MCM3AP]] | +0.67 | +0.57 / +0.64 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[SETD1B]] | +0.66 | +0.54 / +0.59 | both halves | 1e-05 | same gene group; pathway: Chromatin modifying enzymes; STRING 896 |
| [[PRDM15]] | +0.65 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[DVL3]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RANBP3]] | +0.64 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[MFN2]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[INPP5E]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGCG]] | -0.64 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[RYBP]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 | pathway: Transcriptional regulation by RUNX1 |
| [[UBE2B]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SPAG9]] | -0.54 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[ORC4]] | -0.54 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[RNF114]] | -0.54 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ARHGAP12]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TCAF1]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises KMT2D's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.33× lower at baseline in the lines without MSI1 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises KMT2D's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises KMT2D's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AIFM2]] | C | AIFM2 activity lowers KMT2D's level | lines that do not express AIFM2 (3) vs lines expressing it (47) | 1.71× higher at baseline in the lines without AIFM2 | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: FLVCR2, FUCA2, SLC9A3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP5]] | B | the direction of KMT2D's effect on DUSP5's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of KMT2D in 11 lines vs 32 not recorded | the KMT2D-altered lines respond 1.30× as strongly (z diff -1.50); strongest at Cobimetinib 5 µM: 0.33x vs 0.46x (z diff -2.3) | 0.072 | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.4, -28.3); signed map (-9.0, -28.6). **Vector** length 129, 40.2% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.2 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.8 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -6.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -12.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -7.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.0 | -2.0 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | lysine methyltransferase 2D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,018,975-49,060,794 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALR, MLL4, CAGL114; previously TNRC21, MLL2 |
| Gene groups (HGNC) | PHD finger proteins; Histone lysine methyltransferases; SET domain containing |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 20 pathways, smallest: Loss of Function of KMT2D in Kabuki Syndrome; Loss of Function of KMT2D in MLL4 Complex Formation in Kabuki Syndrome; Disorders of Developmental Biology |
| Matched by | ensembl_id |

**Function**, from UniProt [O14686](https://www.uniprot.org/uniprotkb/O14686) (Histone-lysine N-methyltransferase 2D):

> Histone methyltransferase that catalyzes methyl group transfer from S-adenosyl-L-methionine to the epsilon-amino group of 'Lys-4' of histone H3 (H3K4). Part of chromatin remodeling machinery predominantly forms H3K4me1 methylation marks at active chromatin sites where transcription and DNA repair take place. Acts as a coactivator for estrogen receptor by being recruited by ESR1, thereby activating transcription.

**Summary**, from NCBI Gene [8085](https://www.ncbi.nlm.nih.gov/gene/8085):

> The protein encoded by this gene is a histone methyltransferase that methylates the Lys-4 position of histone H3. The encoded protein is part of a large protein complex called ASCOM, which has been shown to be a transcriptional regulator of the beta-globin and estrogen receptor genes. Mutations in this gene have been shown to be a cause of Kabuki syndrome. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:7133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7133) · Entrez [8085](https://www.ncbi.nlm.nih.gov/gene/8085) · UniProt [O14686](https://www.uniprot.org/uniprotkb/O14686) · Ensembl [ENSG00000167548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167548)

## Data

Gene col 9485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9485); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9485]; `tensor/DDL_lfc|DDL_z.npy` [9485]; `embed/gene_vectors.npy` [9485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9485 or target_col == 9485). Every well: [[KMT2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
