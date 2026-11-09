---
symbol: "ATP6V0E2"
type: "gene"
col: 10057
ensembl_id: "ENSG00000171130"
name: "ATPase H+ transporting V0 subunit e2"
location: "7q36.1"
module: 45
arm: "+"
pooled_cpm: 5.95
n_lines_expressing: 45
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ATP6V0E2

*ATPase H+ transporting V0 subunit e2* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.75× (z +14.5, q 1e-44, up in 11 of 12 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 3.94× (z +13.2, q 9e-38, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.560× (z -7.9, q 1e-12, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GVQW3]] (+0.68, fdr 1e-05), [[GAMT]] (+0.67, fdr 7e-06), [[CDK5]] (+0.65, fdr 1e-05); moves opposite to [[ZNF701]] (-0.59, fdr 4e-05), [[ZNF525]] (-0.57, fdr 1e-04), [[MRPL45P2]] (-0.57, fdr 7e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PADI2]] → it (grade B ⚠); 5 go from it, the strongest it → [[NDRG3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.75×** | +14.5 | 1e-44 | 11/12 (HEC-1-A, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.97×** | +13.3 | 6e-38 | 22/25 (C32, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.94×** | +13.2 | 9e-38 | 39/42 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.87×** | +13.1 | 6e-37 | 39/42 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.12×** | +11.0 | 4e-26 | 38/42 (PANC-1, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.93×** | +9.6 | 6e-20 | 12/15 (J82, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.49×** | +8.8 | 9e-17 | 38/42 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.3 | 7e-15 | 25/38 (A498, A549, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.8 | 8e-10 | 29/42 (SW480, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +6.1 | 7e-08 | 26/37 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 4e-04 | 17/39 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.64×** | +4.3 | 7e-04 | 7/41 (C32, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.54×** | +4.2 | 0.001 | 13/26 (NCI-H23, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.001 | 14/42 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.52×** | +3.9 | 0.004 | 12/29 (CFPAC-1, C-33 A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.021 | 5/41 (C32, HEC-1-A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.061 | 10/39 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.35×** | +2.9 | 0.100 | 1/42 (SW 1271) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10057.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.560×** | -7.9 | 1e-12 | 26/38 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.450×** | -7.7 | 4e-12 | 29/41 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -5.9 | 7e-07 | 16/35 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.632×** | -4.4 | 0.001 | 15/41 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -4.3 | 0.002 | 21/42 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -4.2 | 0.003 | 16/42 (A-427, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.42 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.84× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.67× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.221× (z -8.5) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 5.15 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -11.5) |
| [[SNU-1 (line)]] | wt | 9.23 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0343× (z -11.2) |
| [[A498 (line)]] | wt | 6.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.3) | — |
| [[A549 (line)]] | wt | 4.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.59× (z +9.0) | — |
| [[J82 (line)]] | alt | 7.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0804× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.4) |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.4) |
| [[A-172 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GVQW3]] | +0.68 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[GAMT]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[CDK5]] | +0.65 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TMEM106C]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.64 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ATP8A1]] | +0.64 | +0.39 / +0.54 | both halves | 6e-05 | pathway: Ion channel transport |
| [[PODXL2]] | +0.63 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[PPP1R14A]] | +0.62 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[FAM104B]] | +0.60 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[SLC25A23]] | +0.60 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ARL2]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF701]] | -0.59 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ZNF525]] | -0.57 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[MRPL45P2]] | -0.57 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[RAB30-DT]] | -0.57 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.57 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[KRBOX5]] | -0.56 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[TAS2R4]] | -0.56 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[C1S]] | -0.54 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[ZNF721]] | -0.54 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[ZNF621]] | -0.54 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[ZNF181]] | -0.54 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[MIRLET7IHG]] | -0.53 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PADI2]] | B | PADI2 activity raises ATP6V0E2's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without PADI2 | 0.012 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[ASRGL1]] | B | ASRGL1 activity raises ATP6V0E2's level | lines that do not express ASRGL1 (7) vs lines expressing it (43) | 2.57× lower at baseline in the lines without ASRGL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, LINC02026, MYO15B; maybe low, not absent |
| [[SORT1]] | B | SORT1 activity raises ATP6V0E2's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without SORT1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[UCP2]] | B | UCP2 activity raises ATP6V0E2's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.63× lower at baseline in the lines without UCP2 | 0.083 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[CDON]] | C | CDON activity raises ATP6V0E2's level | lines that do not express CDON (3) vs lines expressing it (47) | 3.94× lower at baseline in the lines without CDON | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG3]] | B | ATP6V0E2 activity raises NDRG3's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without ATP6V0E2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4 |
| [[TMEM98]] | B | ATP6V0E2 activity lowers TMEM98's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 1.78× higher at baseline in the lines without ATP6V0E2 | 0.057 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4 |
| [[SLC25A23]] | B | ATP6V0E2 activity raises SLC25A23's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without ATP6V0E2 | 0.082 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4 |
| [[OLFML2A]] | B | ATP6V0E2 activity raises OLFML2A's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without ATP6V0E2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4 |
| [[CDON]] | C | ATP6V0E2 activity raises CDON's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 2.37× lower at baseline in the lines without ATP6V0E2 | 0.024 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4; co-absent with the target |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.0, -7.3); signed map (-27.1, -3.3). **Vector** length 55.4, 8.94% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.7 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.5 | +14.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.0 | +9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +8.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit e2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:149,872,968-149,891,204 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C7orf32, ATP6V0E2L |
| Gene groups (HGNC) | V-type ATPase subunits |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHE4](https://www.uniprot.org/uniprotkb/Q8NHE4) (V-type proton ATPase subunit e 2):

> Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons (By similarity). V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it is responsible for acidifying the extracellular environment (By similarity).

**Summary**, from NCBI Gene [155066](https://www.ncbi.nlm.nih.gov/gene/155066):

> Multisubunit vacuolar-type proton pumps, or H(+)-ATPases, acidify various intracellular compartments, such as vacuoles, clathrin-coated and synaptic vesicles, endosomes, lysosomes, and chromaffin granules. H(+)-ATPases are also found in plasma membranes of specialized cells, where they play roles in urinary acidification, bone resorption, and sperm maturation. Multiple subunits form H(+)-ATPases, with proteins of the V1 class hydrolyzing ATP for energy to transport H+, and proteins of the V0 …

**Accessions** — [HGNC:21723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21723) · Entrez [155066](https://www.ncbi.nlm.nih.gov/gene/155066) · UniProt [Q8NHE4](https://www.uniprot.org/uniprotkb/Q8NHE4) · Ensembl [ENSG00000171130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171130)

## Data

Gene col 10057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10057); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10057]; `tensor/DDL_lfc|DDL_z.npy` [10057]; `embed/gene_vectors.npy` [10057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10057 or target_col == 10057). Every well: [[ATP6V0E2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0E2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
