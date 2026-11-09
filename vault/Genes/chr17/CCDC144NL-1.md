---
symbol: "CCDC144NL-1"
type: "gene"
col: 16568
ensembl_id: "ENSG00000291074"
name: ""
location: ""
module: 191
arm: "+"
pooled_cpm: 4.42
n_lines_expressing: 45
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# CCDC144NL-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.28× (z +16.6, q 0e+00, up in 26 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0715×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.111×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNAB1]] (+0.73, fdr 7e-06), [[LINC00624]] (+0.73, fdr 7e-06), [[COL26A1]] (+0.72, fdr 7e-06).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00408]] → it (grade B ⚠); 6 go from it, the strongest it → [[RN7SL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.28×** | +16.6 | 0e+00 | 26/36 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +14.5 | 4e-45 | 25/32 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +13.2 | 2e-37 | 4/13 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.48×** | +12.0 | 7e-31 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +11.0 | 6e-26 | 19/28 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +8.6 | 6e-16 | 17/30 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +8.4 | 3e-15 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +8.0 | 1e-13 | 25/40 (C-33 A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +7.9 | 2e-13 | 23/42 (C-33 A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +6.3 | 1e-08 | 17/37 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.3 | 2e-08 | 16/42 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +5.4 | 4e-06 | 16/40 (C-33 A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.48×** | +3.9 | 0.004 | 4/21 (HepG2/C3A, HOP62, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.7 | 0.010 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.021 | 3/35 (C-33 A, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.027 | 4/26 (SNU-423, AsPC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.061 | 1/28 (HEC-1-A) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.081 | 2/31 (HEC-1-A, HOP62) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +2.9 | 0.081 | 6/41 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16568.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0715×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.111×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.889× | -4.2 | 0.017 | 12/43 (J82, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 17.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 14.1× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 2 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0715× (z -12.1) |
| [[HS-578T (line)]] | alt | 17.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.99× (z +9.1) | — |
| [[A-172 (line)]] | wt | 5.41 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.8× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 2.30 | 1 | 0 | [[Auranofin (drug)]] 5 µM 84.8× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 4.05 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.5× (z +9.2) | — |
| [[A-427 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 86.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNAB1]] | +0.73 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[LINC00624]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[COL26A1]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[HULC]] | +0.69 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[RYR1]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[LINC01579]] | +0.67 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.67 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[DNAH3]] | +0.67 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[EAF1-AS1]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MAP3K20-AS1]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[RFTN2]] | +0.61 | +0.58 / +0.65 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00408]] | B | LINC00408 activity raises CCDC144NL-1's level | lines that do not express LINC00408 (38) vs lines expressing it (12) | 2.61× lower at baseline in the lines without LINC00408 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000287861, ANKRD20A9P, PHF2P2 |
| [[TMEM132D]] | B | TMEM132D activity raises CCDC144NL-1's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 2.23× lower at baseline in the lines without TMEM132D | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |
| [[UBBP4-1]] | B | UBBP4-1 activity raises CCDC144NL-1's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without UBBP4-1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RN7SL2]] | B | CCDC144NL-1 activity raises RN7SL2's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 1.19× lower at baseline in the lines without CCDC144NL-1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[KCNAB1]] | B | CCDC144NL-1 activity raises KCNAB1's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without CCDC144NL-1 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[NBEAP1]] | B | CCDC144NL-1 activity raises NBEAP1's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without CCDC144NL-1 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[LINC01422]] | B | CCDC144NL-1 activity raises LINC01422's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without CCDC144NL-1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[PWRN1]] | B | CCDC144NL-1 activity raises PWRN1's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without CCDC144NL-1 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[ZRANB2-AS1]] | B | CCDC144NL-1 activity raises ZRANB2-AS1's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 1.14× lower at baseline in the lines without CCDC144NL-1 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.826). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.0, 33.8); signed map (26.9, 16.5). **Vector** length 39.0, 4.08% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +16.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +14.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +12.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.7 | -2.2 |

## What is on record

> [!warning] No registry record
> CCDC144NL-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16568); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16568]; `tensor/DDL_lfc|DDL_z.npy` [16568]; `embed/gene_vectors.npy` [16568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16568 or target_col == 16568). Every well: [[CCDC144NL-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC144NL-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
