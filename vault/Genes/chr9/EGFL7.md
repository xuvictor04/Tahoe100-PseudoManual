---
symbol: "EGFL7"
type: "gene"
col: 10310
ensembl_id: "ENSG00000172889"
name: "EGF like domain multiple 7"
location: "9q34.3"
module: 48
arm: "+"
pooled_cpm: 6.56
n_lines_expressing: 41
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# EGFL7

*EGF like domain multiple 7* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +8.8, q 1e-15, up in 17 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +4.0, q 0.009, up in 18 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.405× (z -9.6, q 3e-19, down in 30 of 32 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCSK1N]] (+0.73, fdr 9e-06), [[REX1BD]] (+0.68, fdr 7e-06), [[GAMT]] (+0.63, fdr 5e-05); moves opposite to [[UPF3A]] (-0.62, fdr 5e-05), [[METTL6]] (-0.57, fdr 2e-04), [[LINC00174]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HLA-DRA]] → it (grade B ⚠); 6 go from it, the strongest it → [[RABAC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.18×** | +8.8 | 1e-15 | 17/20 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.24×** | +8.5 | 4e-15 | 7/10 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.16×** | +5.4 | 1e-05 | 10/13 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.009 | 18/37 (SW480, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.6 | 0.036 | 10/21 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.58×** | +3.5 | 0.048 | 14/38 (LOX-IMVI, NCI-H1573, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.56×** | +3.4 | 0.060 | 10/25 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.060 | 8/33 (A-172, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.060 | 13/35 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.060 | 15/36 (SW480, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.405×** | -9.6 | 3e-19 | 30/32 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.329×** | -8.4 | 1e-14 | 28/31 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -4.5 | 0.001 | 17/37 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.550×** | -4.3 | 0.002 | 17/33 (RKO, HOP62, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.380×** | -3.8 | 0.015 | 12/39 (NCI-H460, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.611×** | -3.7 | 0.019 | 13/36 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.631×** | -3.5 | 0.043 | 12/33 (HOP62, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -3.2 | 0.076 | 12/37 (SW48, SW480, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.631×** | -3.2 | 0.076 | 10/38 (AN3 CA, NCI-H2030, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.653×** | -3.2 | 0.076 | 12/38 (AN3 CA, A498, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.637×** | -3.1 | 0.084 | 11/38 (CHP-212, SW480, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.662×** | -3.1 | 0.084 | 11/38 (Hs 766T, H4, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.456×** | -3.1 | 0.084 | 3/39 (Hs 766T, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.665×** | -3.1 | 0.084 | 15/37 (AN3 CA, A-172, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.468×** | -3.0 | 0.100 | 8/36 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | **0.755×** | -3.0 | 0.100 | 11/36 (LOX-IMVI, LoVo, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 30.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -15.7) |
| [[SW480 (line)]] | alt | 4.67 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0567× (z -13.3) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.7) |
| [[A498 (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -8.6) |
| [[BT-474 (line)]] | alt | 3.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0955× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 6.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 5.48 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 9.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -11.5) |
| [[PANC-1 (line)]] | alt | 8.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -8.5) |
| [[SW1417 (line)]] | alt | 2.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0337× (z -9.6) |
| [[A-427 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCSK1N]] | +0.73 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[REX1BD]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[GAMT]] | +0.63 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[AP2S1]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[C4orf48]] | +0.61 | +0.43 / +0.59 | both halves | 4e-05 |  |
| [[IGSF8]] | +0.60 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[ZNF277]] | +0.60 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ATP6V0E2]] | +0.58 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TSPAN33]] | +0.57 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[TMEM256]] | +0.57 | +0.37 / +0.59 | both halves | 9e-05 |  |
| [[COX7C]] | +0.57 | +0.38 / +0.56 | both halves | 7e-05 | same gene group |
| [[TMEM160]] | +0.57 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPF3A]] | -0.62 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[METTL6]] | -0.57 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[LINC00174]] | -0.57 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TRMT13]] | -0.57 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[TXNRD2]] | -0.57 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[CCT6P3]] | -0.56 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ZNF181]] | -0.56 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[ST7L]] | -0.56 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[FBXO4]] | -0.55 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[TIMMDC1]] | -0.55 | -0.62 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[NDUFS1]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MAGOHB]] | -0.55 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[AFG3L1P]] | -0.55 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRA]] | B | HLA-DRA activity lowers EGFL7's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.55× higher at baseline in the lines without HLA-DRA | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EGFL7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RABAC1]] | B | EGFL7 activity lowers RABAC1's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without EGFL7 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[ZNF277]] | B | EGFL7 activity raises ZNF277's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without EGFL7 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[TSPAN33]] | B | EGFL7 activity raises TSPAN33's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.78× lower at baseline in the lines without EGFL7 | 0.055 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[PCBD1]] | B | EGFL7 activity raises PCBD1's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without EGFL7 | 0.066 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[SBK1]] | B | EGFL7 activity raises SBK1's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 2.29× lower at baseline in the lines without EGFL7 | 0.068 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[AP2S1]] | B | EGFL7 activity lowers AP2S1's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.37× higher at baseline in the lines without EGFL7 | 0.071 | ⚠ within organs, on part of the lines; also absent: KCTD15 |

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-7.4, 0.4); signed map (-33.8, 6.3). **Vector** length 50.2, 8.85% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.6 | +3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +0.7 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.8 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | EGF like domain multiple 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,658,856-136,672,678 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNEU1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHF1](https://www.uniprot.org/uniprotkb/Q9UHF1) (Epidermal growth factor-like protein 7):

> Regulates vascular tubulogenesis in vivo. Inhibits platelet-derived growth factor (PDGF)-BB-induced smooth muscle cell migration and promotes endothelial cell adhesion to the extracellular matrix and angiogenesis.

**Summary**, from NCBI Gene [51162](https://www.ncbi.nlm.nih.gov/gene/51162):

> This gene encodes a secreted endothelial cell protein that contains two epidermal growth factor-like domains. The encoded protein may play a role in regulating vasculogenesis. This protein may be involved in the growth and proliferation of tumor cells. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:20594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20594) · Entrez [51162](https://www.ncbi.nlm.nih.gov/gene/51162) · UniProt [Q9UHF1](https://www.uniprot.org/uniprotkb/Q9UHF1) · Ensembl [ENSG00000172889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172889)

## Data

Gene col 10310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10310); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10310]; `tensor/DDL_lfc|DDL_z.npy` [10310]; `embed/gene_vectors.npy` [10310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10310 or target_col == 10310). Every well: [[EGFL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGFL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
