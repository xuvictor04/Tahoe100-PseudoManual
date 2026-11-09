---
symbol: "YAE1"
type: "gene"
col: 14259
ensembl_id: "ENSG00000241127"
name: "YAE1 maturation factor of ABCE1"
location: "7p14.1"
module: 23
arm: "+"
pooled_cpm: 8.41
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# YAE1

*YAE1 maturation factor of ABCE1* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.37× (z +15.3, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.674× (z -5.0, q 4e-04, down in 16 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.734× (z -3.9, q 0.025, down in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (J82 0.0950×, C-33 A 0.111×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SNU-423 0.0703×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0562×); [[Resveratrol (drug)]] 0.5 µM in 1 line (Hs 766T 0.0902×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF606]] (+0.71, fdr 7e-06), [[SSBP1]] (+0.69, fdr 1e-05), [[THAP6]] (+0.69, fdr 7e-06); moves opposite to [[TTLL5]] (-0.54, fdr 3e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01535]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.37×** | +15.3 | 0e+00 | 43/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.85×** | +13.2 | 3e-37 | 39/44 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.02×** | +13.1 | 5e-37 | 32/37 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +12.4 | 2e-33 | 32/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.92×** | +11.6 | 6e-29 | 41/48 (A498, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +8.5 | 2e-15 | 34/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +7.9 | 3e-13 | 16/32 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.8 | 6e-13 | 25/43 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +6.9 | 3e-10 | 29/48 (A-172, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +6.0 | 9e-08 | 11/23 (LOX-IMVI, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.9 | 2e-07 | 24/47 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.9 | 2e-07 | 6/13 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +5.3 | 5e-06 | 22/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.3 | 5e-06 | 15/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +4.8 | 5e-05 | 20/45 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +4.8 | 6e-05 | 19/48 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.46×** | +4.8 | 7e-05 | 9/48 (A498, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 2e-04 | 15/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +4.3 | 5e-04 | 14/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 7e-04 | 9/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14259.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (J82 0.0950×, C-33 A 0.111×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SNU-423 0.0703×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0562×); [[Resveratrol (drug)]] 0.5 µM in 1 line (Hs 766T 0.0902×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -5.0 | 4e-04 | 16/45 (J82, C-33 A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -3.9 | 0.025 | 13/47 (H4, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.773× | -3.2 | 0.21 | 6/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.730× | -3.2 | 0.21 | 11/48 (C-33 A, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.740× | -3.0 | 0.27 | 11/47 (NCI-H460, H4, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.66× (z +12.5) | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.20× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 6.35 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0771× (z -8.7) |
| [[Hs 766T (line)]] | wt | 6.37 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0902× (z -8.9) |
| [[J82 (line)]] | alt | 5.07 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0950× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 8.84 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 8.42× (z +9.6) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 7.92 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.79× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 5.58 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0562× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 9.48 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.25× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 5.80 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0620× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.75× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 7.55 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0703× (z -10.6) |
| [[A-172 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF606]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[SSBP1]] | +0.69 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[THAP6]] | +0.69 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[ZNF596]] | +0.69 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[METTL6]] | +0.67 | +0.77 / +0.46 | both halves | 3e-05 |  |
| [[C3orf38]] | +0.67 | +0.76 / +0.42 | both halves | 4e-05 |  |
| [[FAM200A]] | +0.66 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[ARMCX5-GPRASP2]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[THBS4]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[THAP2]] | +0.64 | +0.74 / +0.40 | both halves | 5e-05 |  |
| [[ZNF621]] | +0.63 | +0.70 / +0.34 | both halves | 1e-04 |  |
| [[CCNT2]] | +0.63 | +0.44 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL5]] | -0.54 | -0.56 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01535]] | B | LINC01535 activity raises YAE1's level | lines that do not express LINC01535 (21) vs lines expressing it (29) | 1.32× lower at baseline in the lines without LINC01535 | 0.044 | ⚠ within organs, on part of the lines; also absent: MIR3681HG, AFF3, KCNJ6 |
| [[ZNF793]] | B | ZNF793 activity raises YAE1's level | lines that do not express ZNF793 (22) vs lines expressing it (28) | 1.16× lower at baseline in the lines without ZNF793 | 0.045 | ⚠ within organs, on part of the lines; also absent: PEG10, MAP6, ZNF570 |
| [[ZNF606]] | B | ZNF606 activity raises YAE1's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without ZNF606 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |
| [[ZNF382]] | B | ZNF382 activity raises YAE1's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without ZNF382 | 0.050 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[APBB1]] | B | APBB1 activity raises YAE1's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without APBB1 | 0.074 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-27.1, 16.8); signed map (14.4, -19.7). **Vector** length 77.8, 14.2% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.5 | +15.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +13.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.6 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +6.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.3 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.2 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | +4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | +4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.1 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +3.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | YAE1 maturation factor of ABCE1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:39,566,385-39,610,320 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GK003, CIAB2; previously C7orf36, YAE1D1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRH1](https://www.uniprot.org/uniprotkb/Q9NRH1) (Protein YAE1 homolog):

> The complex LTO1:YAE1 functions as a target specific adapter that probably recruits apo-ABCE1 to the cytosolic iron-sulfur protein assembly (CIA) complex machinery. May be required for biogenesis of the large ribosomal subunit and initiation of translation.

**Summary**, from NCBI Gene [57002](https://www.ncbi.nlm.nih.gov/gene/57002):

> Involved in protein maturation. Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24857) · Entrez [57002](https://www.ncbi.nlm.nih.gov/gene/57002) · UniProt [Q9NRH1](https://www.uniprot.org/uniprotkb/Q9NRH1) · Ensembl [ENSG00000241127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241127)

## Data

Gene col 14259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14259); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14259]; `tensor/DDL_lfc|DDL_z.npy` [14259]; `embed/gene_vectors.npy` [14259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14259 or target_col == 14259). Every well: [[YAE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YAE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
