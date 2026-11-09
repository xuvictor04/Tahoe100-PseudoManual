---
symbol: "DNAH12"
type: "gene"
col: 10534
ensembl_id: "ENSG00000174844"
name: "dynein axonemal heavy chain 12"
location: "3p14.3"
module: 26
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 50
n_dd_up: 46
n_dd_down: 0
n_dd_up_clean: 38
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# DNAH12

*dynein axonemal heavy chain 12* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 15.1× (z +35.8, q 0e+00, up in 37 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.132×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0718×; ⚠ cell-cycle shift, explains ~14% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.89, fdr 7e-06), [[TMEM202-AS1]] (+0.85, fdr 7e-06), [[INTS6-AS1]] (+0.84, fdr 7e-06); moves opposite to [[L2HGDH]] (-0.72, fdr 4e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MUC20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **15.1×** | +35.8 | 0e+00 | 37/37 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.7×** | +33.5 | 0e+00 | 37/37 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **9.98×** | +21.5 | 0e+00 | 36/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.41×** | +15.8 | 0e+00 | 41/43 (A-172, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **5.18×** | +14.8 | 0e+00 | 35/41 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.05×** | +14.5 | 1e-45 | 9/10 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.52×** | +13.5 | 7e-40 | 31/35 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +12.8 | 7e-36 | 16/22 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.06×** | +12.6 | 2e-34 | 29/36 (HOP62, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.17×** | +12.3 | 4e-33 | 9/12 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.40×** | +11.4 | 2e-28 | 30/46 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.15×** | +10.1 | 2e-22 | 32/46 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.82×** | +9.7 | 2e-20 | 29/44 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.53×** | +8.6 | 2e-16 | 31/42 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.41×** | +8.2 | 1e-14 | 26/41 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +7.8 | 2e-13 | 26/45 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.31×** | +7.8 | 2e-13 | 24/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.73×** | +5.1 | 9e-06 | 12/47 (AsPC-1, A498, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.132×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0718×; ⚠ cell-cycle shift, explains ~14% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 27.6 | 5 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.83× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -10.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 4.06 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 68.5× (z +15.5) | — |
| [[HEC-1-A (line)]] | alt | 14.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +16.7) | — |
| [[NCI-H460 (line)]] | wt | 2.47 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 47.1× (z +19.1) | — |
| [[SW480 (line)]] | alt | 13.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +14.4) | — |
| [[LoVo (line)]] | wt | 5.83 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.5× (z +19.3) | — |
| [[NCI-H1573 (line)]] | alt | 4.09 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +14.3) | [[Digitoxin (drug)]] 0.05 µM 0.0718× (z -8.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[PANC-1 (line)]] | alt | 2.66 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.3× (z +19.8) | — |
| [[A-172 (line)]] | wt | 3.64 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +12.7) | — |
| [[A498 (line)]] | wt | 3.02 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.5× (z +16.0) | — |
| [[HOP62 (line)]] | alt | 3.64 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +14.2) | — |
| [[HS-578T (line)]] | alt | 3.39 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.8× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 2.75 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 58.4× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 4.43 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.3× (z +16.1) | — |
| [[NCI-H23 (line)]] | alt | 4.40 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 8.89 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +15.3) | — |
| [[A549 (line)]] | wt | 2.59 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 3.66 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 11.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +14.4) | — |
| [[J82 (line)]] | alt | 3.35 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 3.45 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.51 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 33.0× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 4.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 3.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 3.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 8.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 3.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 3.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 3.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 3.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 6.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 2.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +9.2) | — |
| [[SW48 (line)]] | wt | 3.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +10.2) | — |
| [[A-427 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.89 | +0.89 / +0.83 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.85 | +0.88 / +0.69 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.84 | +0.86 / +0.68 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.84 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[AK9]] | +0.83 | +0.86 / +0.71 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.83 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.82 | +0.86 / +0.61 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.81 | +0.87 / +0.56 | both halves | 1e-05 |  |
| [[GUCY2C-AS1]] | +0.80 | +0.85 / +0.60 | both halves | 7e-06 |  |
| [[MGAM]] | +0.79 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.79 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.79 | +0.80 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.72 | -0.63 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | MUC20 activity raises DNAH12's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without MUC20 | 0.021 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[LRRC17]] | B | LRRC17 activity raises DNAH12's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.50× lower at baseline in the lines without LRRC17 | 0.037 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[HLA-V-1]] | B | HLA-V-1 activity raises DNAH12's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.37× lower at baseline in the lines without HLA-V-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[TOP2A]] | B | TOP2A activity lowers DNAH12's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAPK8IP2]] | B | MAPK8IP2 activity raises DNAH12's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.14× lower at baseline in the lines without MAPK8IP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[RFX3-DT]] | C | RFX3-DT activity lowers DNAH12's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.16× higher at baseline in the lines without RFX3-DT | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.862). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.9, 16.8); signed map (24.8, 2.1). **Vector** length 81.2, 16.2% of its response variance represented; |z| ≥ 3 in 1,432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +35.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.1 | +15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +21.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +33.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +7.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +5.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.2 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | +7.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,293,699-57,544,344 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DLP12, Dnahc3, HL-19, hdhc3, DHC3, FLJ40427, FLJ44290; previously DNHD2, DNAH12L, DNAH7L |
| Gene groups (HGNC) | Dyneins, axonemal inner arm I1/f complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZR08](https://www.uniprot.org/uniprotkb/Q6ZR08) (Dynein axonemal heavy chain 12):

> Involved in spermiogenesis. Plays a role in the proper organization of axoneme in sperm flagella, but not in cilia, by recruiting DNAH1 and DNALI1 to flagellum.

**Summary**, from NCBI Gene [201625](https://www.ncbi.nlm.nih.gov/gene/201625):

> Predicted to enable several functions, including ATP binding activity; dynein intermediate chain binding activity; and dynein light intermediate chain binding activity. Involved in sperm axoneme assembly. Located in sperm flagellum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2943) · Entrez [201625](https://www.ncbi.nlm.nih.gov/gene/201625) · UniProt [Q6ZR08](https://www.uniprot.org/uniprotkb/Q6ZR08) · Ensembl [ENSG00000174844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174844)

## Data

Gene col 10534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10534); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10534]; `tensor/DDL_lfc|DDL_z.npy` [10534]; `embed/gene_vectors.npy` [10534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10534 or target_col == 10534). Every well: [[DNAH12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
