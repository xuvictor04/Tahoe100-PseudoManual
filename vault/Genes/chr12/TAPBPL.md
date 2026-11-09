---
symbol: "TAPBPL"
type: "gene"
col: 6277
ensembl_id: "ENSG00000139192"
name: "TAP binding protein like"
location: "12p13.31"
module: 68
arm: "+"
pooled_cpm: 5.02
n_lines_expressing: 49
n_dd_up: 33
n_dd_down: 16
n_dd_up_clean: 27
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TAPBPL

*TAP binding protein like* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.88× (z +25.3, q 0e+00, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.552× (z -7.8, q 3e-12, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PATL2]] (+0.83, fdr 7e-06), [[STAT5A]] (+0.76, fdr 7e-06), [[MED12]] (+0.74, fdr 7e-06); moves opposite to [[WASF3]] (-0.71, fdr 2e-05), [[GNA12]] (-0.68, fdr 2e-05), [[ANKRD27]] (-0.66, fdr 8e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[BTC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.88×** | +25.3 | 0e+00 | 33/38 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.82×** | +13.1 | 5e-37 | 34/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +11.6 | 7e-29 | 24/39 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +10.5 | 1e-23 | 31/42 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.5 | 3e-15 | 15/29 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +8.4 | 6e-15 | 4/8 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.5 | 5e-09 | 11/36 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +6.2 | 3e-08 | 8/18 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.9 | 3e-07 | 11/32 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.2 | 1e-05 | 12/35 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 9e-05 | 13/45 (NCI-H1573, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.8 | 9e-05 | 11/47 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 8/45 (LS 180, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +4.4 | 4e-04 | 6/47 (KATO III, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 8e-04 | 16/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 7/44 (A549, LoVo, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.002 | 6/44 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.003 | 15/41 (A498, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.004 | 5/47 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -7.8 | 3e-12 | 23/46 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.648×** | -5.7 | 3e-06 | 18/46 (KATO III, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.662×** | -5.4 | 1e-05 | 19/39 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.472×** | -5.2 | 3e-05 | 12/44 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.679×** | -5.1 | 4e-05 | 17/39 (A549, SK-MEL-2, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.714×** | -4.4 | 9e-04 | 11/45 (RPMI-7951, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.721×** | -4.3 | 0.001 | 13/45 (BT-474, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -4.0 | 0.004 | 10/47 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.740×** | -4.0 | 0.005 | 11/46 (H4, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.011 | 13/45 (Hs 766T, NCI-H2347, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.748×** | -3.7 | 0.012 | 15/44 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.763×** | -3.5 | 0.018 | 6/45 (A549, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -3.5 | 0.024 | 10/43 (NCI-H23, COLO 205, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.779×** | -3.3 | 0.040 | 8/46 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.785×** | -3.2 | 0.056 | 13/46 (A-172, LoVo, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.784×** | -3.1 | 0.074 | 5/46 (MIA PaCa-2, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.51 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.6× (z +23.0) | — |
| [[SW 900 (line)]] | alt | 6.78 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +9.0) | [[Radotinib (drug)]] 0.5 µM 0.0800× (z -9.4) |
| [[BT-474 (line)]] | alt | 7.38 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.5 µM 0.0742× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 7.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +14.5) | — |
| [[LoVo (line)]] | wt | 9.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +12.0) | — |
| [[A-172 (line)]] | wt | 4.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 6.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 4.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +13.3) | — |
| [[J82 (line)]] | alt | 5.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.62× (z +14.3) | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 7.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.45× (z +15.0) | — |
| [[NCI-H2030 (line)]] | alt | 3.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +16.5) | — |
| [[NCI-H2347 (line)]] | alt | 4.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 3.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 4.59 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0762× (z -9.6) |
| [[SW48 (line)]] | wt | 5.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +12.7) | — |
| [[A-427 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | +0.83 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[STAT5A]] | +0.76 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[MED12]] | +0.74 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TAPBP]] | +0.74 | +0.55 / +0.73 | both halves | 1e-05 | same gene group; STRING 661 |
| [[LINC00240]] | +0.73 | +0.78 / +0.33 | both halves | 1e-04 |  |
| [[STAP2]] | +0.73 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SCAMP1-AS1]] | +0.72 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[LINC00869-1]] | +0.72 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ZC2HC1C]] | +0.71 | +0.75 / +0.43 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.71 | +0.73 / +0.27 | both halves | 3e-04 |  |
| [[PAXIP1-AS2]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | +0.71 | +0.71 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.71 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[GNA12]] | -0.68 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD27]] | -0.66 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[PCMT1]] | -0.66 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[TMEM120B]] | -0.65 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TPST2]] | -0.64 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[PBX4]] | -0.64 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ST6GALNAC4]] | -0.63 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[PACC1]] | -0.63 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[BICD2]] | -0.63 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC5]] | -0.63 | -0.64 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTC]] | B | BTC activity raises TAPBPL's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without BTC | 0.024 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[CXCL2]] | B | CXCL2 activity raises TAPBPL's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without CXCL2 | 0.027 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[TOP2A]] | B | TOP2A activity lowers TAPBPL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CTSO]] | B | CTSO activity raises TAPBPL's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without CTSO | 0.035 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[CXCL3]] | B | CXCL3 activity raises TAPBPL's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without CXCL3 | 0.077 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[SERTAD4]] | B | SERTAD4 activity raises TAPBPL's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.27× lower at baseline in the lines without SERTAD4 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[HSD17B14]] | C | HSD17B14 activity lowers TAPBPL's level | lines that do not express HSD17B14 (3) vs lines expressing it (47) | 1.76× higher at baseline in the lines without HSD17B14 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BFSP1, DNAJB5, MYADM; maybe low, not absent; its own permutation p |
| [[PSMB8]] | C | PSMB8 activity raises TAPBPL's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without PSMB8 | 0.098 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (19.3, 4.8); signed map (22.9, -16.7). **Vector** length 82.1, 14.5% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +25.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.6 | +4.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.7 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | TAP binding protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,451,690-6,466,517 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAPBP-R, FLJ10143, TAPBPR |
| Gene groups (HGNC) | V-set domain containing; C1-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX59](https://www.uniprot.org/uniprotkb/Q9BX59) (Tapasin-related protein):

> Component of the antigen processing and presentation pathway, which binds to MHC class I coupled with beta2-microglobulin/B2M. Association between TAPBPR and MHC class I occurs in the absence of a functional peptide-loading complex (PLC).

**Summary**, from NCBI Gene [55080](https://www.ncbi.nlm.nih.gov/gene/55080):

> Tapasin, or TAPBP (MIM 601962), is a member of the variable-constant Ig superfamily that links major histocompatibility complex (MHC) class I molecules to the transporter associated with antigen processing (TAP; see MIM 170260) in the endoplasmic reticulum (ER). The TAPBP gene is located near the MHC complex on chromosome 6p21.3. TAPBPL is a member of the Ig superfamily that is localized on chromosome 12p13.3, a region somewhat paralogous to the MHC.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30683) · Entrez [55080](https://www.ncbi.nlm.nih.gov/gene/55080) · UniProt [Q9BX59](https://www.uniprot.org/uniprotkb/Q9BX59) · Ensembl [ENSG00000139192](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139192)

## Data

Gene col 6277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6277); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6277]; `tensor/DDL_lfc|DDL_z.npy` [6277]; `embed/gene_vectors.npy` [6277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6277 or target_col == 6277). Every well: [[TAPBPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAPBPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
