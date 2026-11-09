---
symbol: "DIO2"
type: "gene"
col: 13060
ensembl_id: "ENSG00000211448"
name: "iodothyronine deiodinase 2"
location: "14q31.1"
module: 66
arm: "+"
pooled_cpm: 9.21
n_lines_expressing: 36
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 29
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 13
direction_downstream: 5
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# DIO2

*iodothyronine deiodinase 2* — 14q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.80× (z +21.3, q 0e+00, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.652× (z -5.8, q 3e-06, down in 18 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENM3]] (+0.64, fdr 7e-06), [[RIPK2-DT]] (+0.64, fdr 1e-05), [[ROS1]] (+0.64, fdr 7e-06); moves opposite to [[ZNF549]] (-0.60, fdr 4e-05), [[ANKRD13D]] (-0.59, fdr 1e-05), [[MPG]] (-0.59, fdr 2e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[KYNU]] → it (grade B ⚠); 5 go from it, the strongest it → [[KYNU]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.80×** | +21.3 | 0e+00 | 30/33 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.01×** | +13.4 | 3e-38 | 15/22 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.62×** | +11.9 | 2e-30 | 11/13 (J82, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.23×** | +11.3 | 2e-27 | 21/31 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.16×** | +11.1 | 2e-26 | 23/32 (NCI-H460, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.24×** | +10.5 | 1e-23 | 10/17 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.65×** | +9.0 | 1e-17 | 20/33 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **2.03×** | +6.8 | 6e-10 | 18/33 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.87×** | +5.9 | 2e-07 | 16/34 (NCI-H1792, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.88×** | +5.8 | 3e-07 | 16/32 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.77×** | +5.4 | 3e-06 | 16/34 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.3 | 5e-06 | 15/34 (BT-474, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 6e-06 | 15/34 (NCI-H1792, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.46×** | +5.0 | 2e-05 | 16/34 (NCI-H1792, J82, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 2e-05 | 13/33 (HOP62, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +4.7 | 1e-04 | 14/34 (NCI-H1792, J82, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.6 | 1e-04 | 8/34 (J82, Panc 03.27, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 1e-04 | 11/34 (HOP62, H4, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.652×** | -5.8 | 3e-06 | 18/34 (CHP-212, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.656×** | -4.1 | 0.013 | 13/33 (SW48, SNU-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.678×** | -3.8 | 0.033 | 12/33 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.721× | -3.2 | 0.22 | 4/33 (NCI-H460, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.8× (z +21.9) | — |
| [[J82 (line)]] | alt | 56.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 24.0× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.53× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +17.4) | — |
| [[A-172 (line)]] | wt | 11.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 98.7× (z +24.3) | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0162× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0848× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 35.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +25.0) | — |
| [[H4 (line)]] | wt | 27.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.5× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 7.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.6× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.74× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +14.1) | — |
| [[SW 900 (line)]] | alt | 8.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 52.0× (z +18.0) | — |
| [[A549 (line)]] | wt | 7.03 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0631× (z -9.8) ⚠ toxic |
| [[BT-474 (line)]] | alt | 3.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.7× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 7.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.89× (z +14.7) ⚠ position not correctable | — |
| [[NCI-H2347 (line)]] | alt | 3.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 7.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +11.1) | — |
| [[SW 1271 (line)]] | alt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.3× (z +10.6) | — |
| [[A-427 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENM3]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.64 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ROS1]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[KMO]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[TRIML2]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[LINC00882]] | +0.62 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[OLR1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MYPN]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[CACNA2D1]] | +0.61 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[CLIC2]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[TGFB2]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF549]] | -0.60 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD13D]] | -0.59 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[MPG]] | -0.59 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[CRYL1]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[UHRF2]] | -0.56 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[UBTD1]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[XYLT2]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[POGLUT2]] | -0.55 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[FLYWCH2]] | -0.54 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[CROCCP3]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[STARD3]] | -0.53 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[HMOX2]] | -0.53 | -0.53 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KYNU]] | B | KYNU activity raises DIO2's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without KYNU | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[LINC00882]] | B | LINC00882 activity raises DIO2's level | lines that do not express LINC00882 (17) vs lines expressing it (33) | 3.35× lower at baseline in the lines without LINC00882 | 0.040 | ⚠ within organs, on part of the lines; also absent: TUSC3, B3GALT1, EVC |
| [[SYNPO]] | B | SYNPO activity raises DIO2's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.23× lower at baseline in the lines without SYNPO | 0.067 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[PRECSIT]] | B | PRECSIT activity raises DIO2's level | lines that do not express PRECSIT (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without PRECSIT | 0.069 | ⚠ within organs, on part of the lines; also absent: FAM3B, CFAP45, ENSG00000283511; maybe low, not absent |
| [[OXTR]] | B | OXTR activity raises DIO2's level | lines that do not express OXTR (5) vs lines expressing it (45) | 3.55× lower at baseline in the lines without OXTR | 0.077 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[TLR6]] | B | TLR6 activity raises DIO2's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without TLR6 | 0.081 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[SPART]] | B | SPART activity raises DIO2's level | lines that do not express SPART (15) vs lines expressing it (35) | 3.32× lower at baseline in the lines without SPART | 0.089 | ⚠ within organs, on part of the lines; also absent: CCDC169, SPART-AS1, FIGN; its own permutation p |
| [[TGFB2]] | B | TGFB2 activity raises DIO2's level | lines that do not express TGFB2 (15) vs lines expressing it (35) | 2.71× lower at baseline in the lines without TGFB2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |
| [[MYOF]] | B | MYOF activity raises DIO2's level | lines that do not express MYOF (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without MYOF | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[LINC02057]] | B | LINC02057 activity raises DIO2's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without LINC02057 | 0.093 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[FBXW10B]] | B | FBXW10B activity raises DIO2's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without FBXW10B | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[KCNT2]] | B | KCNT2 activity raises DIO2's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 2.49× lower at baseline in the lines without KCNT2 | 0.094 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KYNU]] | B | DIO2 activity raises KYNU's level | lines that do not express DIO2 (14) vs lines expressing it (36) | 2.85× lower at baseline in the lines without DIO2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC01725, ENSG00000226640, RNF150 |
| [[LINC02057]] | B | DIO2 activity raises LINC02057's level | lines that do not express DIO2 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without DIO2 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC01725, ENSG00000226640, RNF150 |
| [[PAX8]] | B | DIO2 activity raises PAX8's level | lines that do not express DIO2 (14) vs lines expressing it (36) | 1.01× lower at baseline in the lines without DIO2 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC01725, ENSG00000226640, RNF150 |
| [[ALCAM]] | B | DIO2 activity raises ALCAM's level | lines that do not express DIO2 (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without DIO2 | 0.0995 | ⚠ within organs, on part of the lines; also absent: LINC01725, ENSG00000226640, RNF150 |
| [[LINC01725]] | C | DIO2 activity raises LINC01725's level | lines that do not express DIO2 (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without DIO2 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC01725, ENSG00000226640, RNF150; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 22.6); signed map (46.4, 21.5). **Vector** length 81.8, 17.6% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +21.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +5.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | -1.9 | -1.3 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.9 | -5.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | iodothyronine deiodinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.1 — chr14:80,197,526-80,387,757 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TXDI2, SelY, SELENOY |
| Gene groups (HGNC) | Selenoproteins; Iodothyronine deiodinase family |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 6 pathways, smallest: Metabolism of amine-derived hormones; Thyroxine biosynthesis; Transcriptional regulation of brown and beige adipocyte differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92813](https://www.uniprot.org/uniprotkb/Q92813) (Type II iodothyronine deiodinase):

> Plays a crucial role in the metabolism of thyroid hormones (TH) and has specific roles in TH activation and inactivation by deiodination. Catalyzes the deiodination of L-thyroxine (T4) to 3,5,3'-triiodothyronine (T3), 3,3',5'-triiodothyronine (rT3) to 3,3'-diiodothyronine (3,3'-T2) and 3',5'-diiodothyronine (3',5'-T2) to 3'-monoiodothyronine (3'-T1) via outer-ring deiodination (ORD). Catalyzes the phenolic ring deiodinations of 3,3',5'-triiodothyronamine and 3',5'- diiodothyronamine.

**Summary**, from NCBI Gene [1734](https://www.ncbi.nlm.nih.gov/gene/1734):

> The protein encoded by this gene belongs to the iodothyronine deiodinase family. It catalyzes the conversion of prohormone thyroxine (3,5,3',5'-tetraiodothyronine, T4) to the bioactive thyroid hormone (3,5,3'-triiodothyronine, T3) by outer ring 5'-deiodination. This gene is widely expressed, including in thyroid and brain. It is thought to be responsible for the 'local' production of T3, and thus important in influencing thyroid hormone action in these tissues. It has also been reported to be …

**Accessions** — [HGNC:2884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2884) · Entrez [1734](https://www.ncbi.nlm.nih.gov/gene/1734) · UniProt [Q92813](https://www.uniprot.org/uniprotkb/Q92813) · Ensembl [ENSG00000211448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211448)

## Data

Gene col 13060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13060); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13060]; `tensor/DDL_lfc|DDL_z.npy` [13060]; `embed/gene_vectors.npy` [13060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13060 or target_col == 13060). Every well: [[DIO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
