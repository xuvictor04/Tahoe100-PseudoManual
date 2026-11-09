---
symbol: "MARVELD2"
type: "gene"
col: 7670
ensembl_id: "ENSG00000152939"
name: "MARVEL domain containing 2"
location: "5q13.2"
module: 68
arm: "+"
pooled_cpm: 16.77
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 6
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# MARVELD2

*MARVEL domain containing 2* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +20.0, q 0e+00, up in 26 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.641× (z -7.9, q 2e-12, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGALSL-DT]] (+0.71, fdr 1e-05), [[RPP38]] (+0.70, fdr 1e-05), [[MIER3]] (+0.70, fdr 3e-05); moves opposite to [[SLC27A1]] (-0.63, fdr 6e-05), [[NHP2]] (-0.59, fdr 0.001, ⚠ one half only (not replicated)), [[IGSF8]] (-0.59, fdr 2e-04), [[SHQ1]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[GRHL2]], [[LINC02967]] → it (grade B ⚠); 6 go from it, the strongest it → [[ZSCAN29]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +20.0 | 0e+00 | 26/30 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +13.0 | 3e-36 | 27/30 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +11.6 | 9e-29 | 24/29 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.9 | 5e-13 | 20/32 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +7.2 | 5e-11 | 18/31 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +6.8 | 1e-09 | 19/32 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +6.2 | 3e-08 | 13/33 (HT-29, KATO III, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +6.1 | 6e-08 | 20/33 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.9 | 3e-07 | 10/31 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.7 | 8e-07 | 12/32 (LoVo, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 3e-05 | 18/32 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 10/33 (A498, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.4 | 4e-04 | 6/20 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +4.4 | 4e-04 | 12/33 (SW480, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.002 | 11/33 (SW480, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.002 | 9/33 (SW480, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 9/34 (SW480, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 11/34 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.021 | 9/34 (A-427, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.641×** | -7.9 | 2e-12 | 19/33 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.664×** | -7.2 | 1e-10 | 22/33 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.670×** | -7.1 | 3e-10 | 22/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.788×** | -4.1 | 0.007 | 16/31 (SNU-423, LS 180, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | 0.708× | -3.2 | 0.16 | 11/30 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.9 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -11.9) |
| [[LoVo (line)]] | wt | 41.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.355× (z -10.8) |
| [[PANC-1 (line)]] | alt | 17.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 44.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -11.5) |
| [[KATO III (line)]] | alt | 39.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -9.6) |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0789× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.330× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 37.7 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -9.6) |
| [[A-427 (line)]] | wt | 24.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.99× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 9.99 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.45× (z +12.0) | — |
| [[HCT15 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.124× (z -11.1) |
| [[A-172 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALSL-DT]] | +0.71 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[RPP38]] | +0.70 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[MIER3]] | +0.70 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[LINC00857]] | +0.66 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PBDC1]] | +0.65 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NME6]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.64 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.63 | +0.65 / +0.34 | both halves | 1e-04 |  |
| [[PPCS]] | +0.63 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[KRCC1]] | +0.63 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[ARL14EP]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[LGALSL]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | -0.63 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[NHP2]] | -0.59 | -0.56 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[IGSF8]] | -0.59 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[SHQ1]] | -0.58 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[KHDRBS1]] | -0.58 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[FCHO1]] | -0.56 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[SNRPD2]] | -0.56 | -0.59 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[SNX1]] | -0.56 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[UQCRH]] | -0.56 | -0.63 / -0.28 | both halves | 3e-04 |  |
| [[LMTK3]] | -0.55 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[PCMT1]] | -0.55 | -0.52 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[HSPB11]] | -0.54 | -0.57 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRHL2]], [[LINC02967]] | B | GRHL2, LINC02967 activity raises MARVELD2's level | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (16) | 3.97× lower at baseline in the lines without GRHL2, LINC02967 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[LMTK3]] | B | LMTK3 activity raises MARVELD2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.86× lower at baseline in the lines without LMTK3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[EDN1]] | B | EDN1 activity raises MARVELD2's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 3.24× lower at baseline in the lines without EDN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises MARVELD2's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.55× lower at baseline in the lines without MTUS1-DT | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[HDAC6]] | B | HDAC6 activity raises MARVELD2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FGFR4]] | B | FGFR4 activity raises MARVELD2's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.84× lower at baseline in the lines without FGFR4 | 0.044 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[HLA-V-1]] | B | HLA-V-1 activity raises MARVELD2's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without HLA-V-1 | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[HNF1A]] | B | HNF1A activity raises MARVELD2's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 2.70× lower at baseline in the lines without HNF1A | 0.052 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[LINC00857]] | B | LINC00857 activity raises MARVELD2's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 3.17× lower at baseline in the lines without LINC00857 | 0.086 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |
| [[MARVELD3]] | C | MARVELD3 activity raises MARVELD2's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 4.42× lower at baseline in the lines without MARVELD3 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN29]] | B | MARVELD2 activity raises ZSCAN29's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.33× lower at baseline in the lines without MARVELD2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[IQCH-AS1]] | B | MARVELD2 activity raises IQCH-AS1's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without MARVELD2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[PPCS]] | B | MARVELD2 activity raises PPCS's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without MARVELD2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[ZNF747]] | B | MARVELD2 activity raises ZNF747's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.26× lower at baseline in the lines without MARVELD2 | 0.067 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[SRSF8]] | B | MARVELD2 activity raises SRSF8's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without MARVELD2 | 0.078 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[EDN1]] | B | MARVELD2 activity raises EDN1's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 4.27× lower at baseline in the lines without MARVELD2 | 0.096 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-8.8, 8.6); signed map (13.8, -20.8). **Vector** length 83.1, 20.3% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +20.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +13.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.3 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -4.1 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | MARVEL domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,415,065-69,444,330 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30532, TRIC; previously MRVLDC2, DFNB49 |
| Gene groups (HGNC) | MARVEL domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4S9](https://www.uniprot.org/uniprotkb/Q8N4S9) (MARVEL domain-containing protein 2):

> Plays a role in the formation of tricellular tight junctions and of epithelial barriers (By similarity). Required for normal hearing via its role in the separation of the endolymphatic and perilymphatic spaces of the organ of Corti in the inner ear, and for normal survival of hair cells in the organ of Corti.

**Summary**, from NCBI Gene [153562](https://www.ncbi.nlm.nih.gov/gene/153562):

> The protein encoded by this gene is a membrane protein found at the tight junctions between epithelial cells. The encoded protein helps establish epithelial barriers such as those in the organ of Corti, where these barriers are required for normal hearing. Defects in this gene are a cause of deafness autosomal recessive type 49 (DFNB49). Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:26401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26401) · Entrez [153562](https://www.ncbi.nlm.nih.gov/gene/153562) · UniProt [Q8N4S9](https://www.uniprot.org/uniprotkb/Q8N4S9) · Ensembl [ENSG00000152939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152939)

## Data

Gene col 7670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7670); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7670]; `tensor/DDL_lfc|DDL_z.npy` [7670]; `embed/gene_vectors.npy` [7670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7670 or target_col == 7670). Every well: [[MARVELD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARVELD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
