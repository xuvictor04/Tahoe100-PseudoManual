---
symbol: "LAD1"
type: "gene"
col: 8223
ensembl_id: "ENSG00000159166"
name: "ladinin 1"
location: "1q32.1"
module: 73
arm: "+"
pooled_cpm: 12.0
n_lines_expressing: 20
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 63
direction_downstream: 84
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# LAD1

*ladinin 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.08× (z +14.8, q 0e+00, up in 15 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.50× (z +4.2, q 0.001, up in 11 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.480× (z -7.8, q 4e-12, down in 16 of 18 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSE]] (+0.68, fdr 7e-06), [[KLK6]] (+0.68, fdr 7e-06), [[TMEM30B]] (+0.66, fdr 7e-06); moves opposite to [[IKBIP]] (-0.53, fdr 4e-05), [[TMEM258]] (-0.49, fdr 4e-05), [[SEC61G]] (-0.48, fdr 8e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 63 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 84 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +14.8 | 0e+00 | 15/16 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +12.7 | 2e-34 | 11/14 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.24×** | +12.0 | 6e-31 | 6/18 (AsPC-1, HepG2/C3A, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.13×** | +11.1 | 1e-26 | 12/15 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.75×** | +5.9 | 5e-07 | 5/18 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.76×** | +5.7 | 9e-07 | 10/18 (Panc 03.27, LoVo, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.54×** | +4.5 | 4e-04 | 9/18 (HEC-1-A, Panc 03.27, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.4 | 6e-04 | 13/17 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 0.001 | 11/18 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.0 | 0.004 | 3/17 (CFPAC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.004 | 1/17 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.004 | 10/18 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.6 | 0.015 | 5/11 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +3.3 | 0.039 | 9/17 (Panc 03.27, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.046 | 2/18 (HCT15, KATO III) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -7.8 | 4e-12 | 16/18 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.504×** | -7.3 | 1e-10 | 14/18 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.625×** | -5.0 | 1e-04 | 14/18 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.723×** | -3.5 | 0.062 | 0/18 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.723×** | -3.5 | 0.062 | 8/18 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.735×** | -3.3 | 0.094 | 8/18 (HT-29, SW48, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.720×** | -3.2 | 0.096 | 2/18 (LoVo, LS 180) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.744× | -3.2 | 0.12 | 1/18 (HCT15) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.539× | -3.0 | 0.15 | 7/18 (LoVo, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 16.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.69× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.212× (z -8.5) |
| [[LoVo (line)]] | wt | 34.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -14.0) |
| [[COLO 205 (line)]] | alt | 55.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -9.5) |
| [[LS 180 (line)]] | wt | 47.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 16.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +12.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 49.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 20.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.249× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +11.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -8.8) |
| [[SW48 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSE]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[KLK6]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[TMEM30B]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MUC2]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[KRT8]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[HR]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[KRT18]] | +0.64 | +0.74 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[CAPN8]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[DENND2D]] | +0.63 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[ADAP1]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ACSL5]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[COL17A1]] | +0.61 | +0.52 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKBIP]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[TMEM258]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SEC61G]] | -0.48 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[TULP3]] | -0.47 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[LAMTOR5]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 5, C 58. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises LAD1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.90× lower at baseline in the lines without EPS8L1 | 0.013 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises LAD1's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without HTR1D | 0.067 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises LAD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BAIAP2L2]] | B | BAIAP2L2 activity raises LAD1's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without BAIAP2L2 | 0.082 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[AGMAT]] | B | AGMAT activity raises LAD1's level | lines that do not express AGMAT (11) vs lines expressing it (39) | 3.62× lower at baseline in the lines without AGMAT | 0.086 | ⚠ within organs, on part of the lines; also absent: ETV7, LYPD5, TNK1; maybe low, not absent |
| [[TNNT2]] | C | TNNT2 activity raises LAD1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 10.52× lower at baseline in the lines without TNNT2 | 4e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises LAD1's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 9.20× lower at baseline in the lines without TRIM29 | 1e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises LAD1's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 10.05× lower at baseline in the lines without TMEM30B | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises LAD1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 9.78× lower at baseline in the lines without TMPRSS2 | 2e-05 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises LAD1's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 8.72× lower at baseline in the lines without EPCAM | 4e-05 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[PRSS22]] | C | PRSS22 activity raises LAD1's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 8.63× lower at baseline in the lines without PRSS22 | 7e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises LAD1's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 7.03× lower at baseline in the lines without COL17A1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |

### Downstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 34, C 50. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | LAD1 activity raises EPS8L1's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 5.01× lower at baseline in the lines without LAD1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[PKP3]] | B | LAD1 activity raises PKP3's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.79× lower at baseline in the lines without LAD1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[TMEM184A]] | B | LAD1 activity raises TMEM184A's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.87× lower at baseline in the lines without LAD1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[KRT8]] | B | LAD1 activity raises KRT8's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 4.70× lower at baseline in the lines without LAD1 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[ADAP1]] | B | LAD1 activity raises ADAP1's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.20× lower at baseline in the lines without LAD1 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[ABHD11]] | B | LAD1 activity raises ABHD11's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without LAD1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[ARMC7]] | B | LAD1 activity raises ARMC7's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without LAD1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[PSD4]] | B | LAD1 activity raises PSD4's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.27× lower at baseline in the lines without LAD1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[BAIAP2L2]] | B | LAD1 activity raises BAIAP2L2's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without LAD1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[IKBIP]] | B | LAD1 activity lowers IKBIP's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.38× higher at baseline in the lines without LAD1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[FAM83H]] | B | LAD1 activity raises FAM83H's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.42× lower at baseline in the lines without LAD1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[GJB2]] | B | LAD1 activity raises GJB2's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without LAD1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.4, 50.3); signed map (66.5, 10.4). **Vector** length 68.8, 25.6% of its response variance represented; |z| ≥ 3 in 401 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.7 | +12.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.4 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ladinin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,380,833-201,399,915 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O00515](https://www.uniprot.org/uniprotkb/O00515) (Ladinin-1):

> Anchoring filament protein which is a component of the basement membrane zone.

**Summary**, from NCBI Gene [3898](https://www.ncbi.nlm.nih.gov/gene/3898):

> The protein encoded by this gene may be an anchoring filament that is a component of basement membranes. It may contribute to the stability of the association of the epithelial layers with the underlying mesenchyme. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6472) · Entrez [3898](https://www.ncbi.nlm.nih.gov/gene/3898) · UniProt [O00515](https://www.uniprot.org/uniprotkb/O00515) · Ensembl [ENSG00000159166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159166)

## Data

Gene col 8223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8223); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8223]; `tensor/DDL_lfc|DDL_z.npy` [8223]; `embed/gene_vectors.npy` [8223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8223 or target_col == 8223). Every well: [[LAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
