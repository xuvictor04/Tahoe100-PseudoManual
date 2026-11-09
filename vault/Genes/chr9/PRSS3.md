---
symbol: "PRSS3"
type: "gene"
col: 211
ensembl_id: "ENSG00000010438"
name: "serine protease 3"
location: "9p13.3"
module: 34
arm: "+"
pooled_cpm: 71.87
n_lines_expressing: 20
n_dd_up: 16
n_dd_down: 32
n_dd_up_clean: 13
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 60
direction_downstream: 65
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PRSS3

*serine protease 3* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +8.5, q 8e-15, up in 1 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.57× (z +8.3, q 4e-14, up in 9 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.452× (z -14.4, q 3e-44, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSG3]] (+0.78, fdr 7e-06), [[HS3ST1]] (+0.78, fdr 7e-06), [[FA2H]] (+0.75, fdr 7e-06).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[TMCC3]] → it (grade B ⚠); 65 go from it, the strongest it → [[GCKR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +8.5 | 8e-15 | 1/19 (SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +8.3 | 4e-14 | 9/18 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.5 | 2e-08 | 1/15 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +6.3 | 3e-08 | 12/18 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 3e-05 | 14/18 (HOP62, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.006 | 7/18 (Panc 03.27, NCI-H1792, …) | two highest doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.017 | 10/18 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.018 | 0/18 | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.035 | 7/18 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.039 | 0/18 | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.039 | 6/18 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.039 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.065 | 11/18 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vilanterol (drug)]] 5 µM |  | 1.19× | +3.1 | 0.065 | 5/19 (SW480, SW1417, …) | all doses, flat | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +3.1 | 0.065 | 6/18 (CHP-212, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.081 | 6/19 (CHP-212, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.081 | 8/18 (CHP-212, Panc 03.27, …) | two highest doses | position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.081 | 0/18 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.452×** | -14.4 | 3e-44 | 18/18 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.508×** | -8.4 | 2e-14 | 17/18 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.597×** | -6.6 | 7e-09 | 14/18 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.596×** | -6.1 | 1e-07 | 11/18 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -5.2 | 2e-05 | 3/19 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.753×** | -5.1 | 4e-05 | 6/18 (SW48, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.689×** | -4.8 | 2e-04 | 12/18 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.707×** | -4.4 | 6e-04 | 6/18 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.785×** | -4.4 | 7e-04 | 18/18 (AsPC-1, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.735×** | -4.3 | 0.001 | 9/20 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -4.2 | 0.001 | 9/18 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.753×** | -3.6 | 0.014 | 4/18 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.759×** | -3.5 | 0.019 | 7/18 (LoVo, LS 180, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.753×** | -3.5 | 0.020 | 16/18 (LS 180, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.022 | 9/18 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -3.4 | 0.026 | 12/18 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.762×** | -3.3 | 0.026 | 5/18 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.607×** | -3.3 | 0.026 | 2/18 (CFPAC-1, HOP62) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.832×** | -3.3 | 0.027 | 6/18 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.027 | 6/18 (A549, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 458 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -24.8) |
| [[LoVo (line)]] | wt | 498 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -28.0) |
| [[KATO III (line)]] | alt | 279 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -19.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.132× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 626 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -31.9) |
| [[COLO 205 (line)]] | alt | 313 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0707× (z -24.4) |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -17.9) |
| [[CFPAC-1 (line)]] | alt | 79.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.6) |
| [[SW480 (line)]] | alt | 45.2 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.30× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.8) |
| [[HOP62 (line)]] | alt | 26.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.2) |
| [[RKO (line)]] | wt | 41.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -19.6) |
| [[CHP-212 (line)]] | wt | 75.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 71.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -8.8) |
| [[Hs 766T (line)]] | wt | 52.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 49.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.1) |
| [[A549 (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -11.0) |
| [[HT-29 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -14.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SW1417 (line)]] | alt | 32.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.43× (z +9.4) | — |
| [[A-172 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.39 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.66 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSG3]] | +0.78 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.78 | +0.73 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[FA2H]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[SERPINB5]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TMC7]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CRYBG2]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[KCNK1]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[KLK10]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CALB1]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[PLEKHM1P1]] | +0.68 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[KIAA0040]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 12, C 48. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCC3]] | B | TMCC3 activity raises PRSS3's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.58× lower at baseline in the lines without TMCC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[MAP2K1]] | B | MAP2K1 activity raises PRSS3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[TMEM154]] | B | TMEM154 activity raises PRSS3's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without TMEM154 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[PTPRE]] | B | PTPRE activity raises PRSS3's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 3.61× lower at baseline in the lines without PTPRE | 0.042 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[IL1R2]] | B | IL1R2 activity raises PRSS3's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.69× lower at baseline in the lines without IL1R2 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[SEMA3F]] | B | SEMA3F activity lowers PRSS3's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 2.50× higher at baseline in the lines without SEMA3F | 0.056 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[LYPD3]] | B | LYPD3 activity raises PRSS3's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.04× lower at baseline in the lines without LYPD3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[PROSER2]] | B | PROSER2 activity raises PRSS3's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.96× lower at baseline in the lines without PROSER2 | 0.067 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[LINC00589]] | B | LINC00589 activity raises PRSS3's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 2.52× lower at baseline in the lines without LINC00589 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |
| [[CEMIP]] | B | CEMIP activity raises PRSS3's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.52× lower at baseline in the lines without CEMIP | 0.077 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[GCKR]] | B | GCKR activity raises PRSS3's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without GCKR | 0.091 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises PRSS3's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.90× lower at baseline in the lines without GRHL3 | 0.094 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |

### Downstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 29, C 36. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCKR]] | B | PRSS3 activity raises GCKR's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.44× lower at baseline in the lines without PRSS3 | 0.004 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[PLEKHM1P1]] | B | PRSS3 activity raises PLEKHM1P1's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.62× lower at baseline in the lines without PRSS3 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[MYRF]] | B | PRSS3 activity raises MYRF's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without PRSS3 | 0.016 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[PLEKHM1]] | B | PRSS3 activity raises PLEKHM1's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.57× lower at baseline in the lines without PRSS3 | 0.018 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[TMCC3]] | B | PRSS3 activity raises TMCC3's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without PRSS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[WNT7B]] | B | PRSS3 activity raises WNT7B's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.45× lower at baseline in the lines without PRSS3 | 0.026 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[PROSER2]] | B | PRSS3 activity raises PROSER2's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without PRSS3 | 0.027 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[ALS2CL]] | B | PRSS3 activity raises ALS2CL's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 3.20× lower at baseline in the lines without PRSS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[ABHD17C]] | B | PRSS3 activity raises ABHD17C's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without PRSS3 | 0.031 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[PTPRE]] | B | PRSS3 activity raises PTPRE's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 3.17× lower at baseline in the lines without PRSS3 | 0.040 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[S100A16]] | B | PRSS3 activity raises S100A16's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.30× lower at baseline in the lines without PRSS3 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[PLAUR]] | B | PRSS3 activity raises PLAUR's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.18× lower at baseline in the lines without PRSS3 | 0.050 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, 54.3); signed map (0.6, 39.2). **Vector** length 94.1, 36.1% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.1 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +3.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.4 | -5.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,750,679-33,799,231 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRY3, TRY4; previously PRSS4 |
| Gene groups (HGNC) | Serine proteases; Elastases |
| Hallmark sets | COMPLEMENT |
| Reactome | 8 pathways, smallest: Defensins; Uptake of dietary cobalamins into enterocytes; Antimicrobial peptides |
| Matched by | ensembl_id |

**Function**, from UniProt [P35030](https://www.uniprot.org/uniprotkb/P35030) (Trypsin-3):

> Digestive protease that cleaves proteins preferentially after an Arg residue and has proteolytic activity toward Kunitz-type trypsin inhibitors.

**Summary**, from NCBI Gene [5646](https://www.ncbi.nlm.nih.gov/gene/5646):

> This gene encodes a trypsinogen, which is a member of the trypsin family of serine proteases. This enzyme is expressed in the brain and pancreas and is resistant to common trypsin inhibitors. It is active on peptide linkages involving the carboxyl group of lysine or arginine. This gene is localized to the locus of T cell receptor beta variable orphans on chromosome 9. Four transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:9486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9486) · Entrez [5646](https://www.ncbi.nlm.nih.gov/gene/5646) · UniProt [P35030](https://www.uniprot.org/uniprotkb/P35030) · Ensembl [ENSG00000010438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010438)

## Data

Gene col 211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 211); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 211]; `tensor/DDL_lfc|DDL_z.npy` [211]; `embed/gene_vectors.npy` [211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 211 or target_col == 211). Every well: [[PRSS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
