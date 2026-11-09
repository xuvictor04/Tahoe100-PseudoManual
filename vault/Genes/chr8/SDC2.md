---
symbol: "SDC2"
type: "gene"
col: 9809
ensembl_id: "ENSG00000169439"
name: "syndecan 2"
location: "8q22.1"
module: 13
arm: "+"
pooled_cpm: 46.74
n_lines_expressing: 24
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 21
direction_downstream: 29
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SDC2

*syndecan 2* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.93× (z +16.0, q 0e+00, up in 11 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +10.4, q 5e-23, up in 8 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.652× (z -6.3, q 1e-07, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LOXL3]] (+0.71, fdr 7e-06), [[COL1A2]] (+0.66, fdr 7e-06), [[COL8A1]] (+0.65, fdr 7e-06); moves opposite to [[IQANK1]] (-0.46, fdr 1e-04), [[ARHGEF5]] (-0.44, fdr 1e-04), [[PATJ]] (-0.44, fdr 8e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[GXYLT2]] → it (grade B ⚠); 29 go from it, the strongest it → [[CPQ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +16.0 | 0e+00 | 11/23 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +14.7 | 0e+00 | 9/16 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +13.9 | 2e-41 | 9/20 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +10.4 | 5e-23 | 8/22 (C-33 A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +8.6 | 1e-15 | 8/22 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.3 | 3e-11 | 5/24 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +4.4 | 8e-04 | 10/22 (J82, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.019 | 6/22 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.2 | 0.081 | 2/18 (HS-578T, A-172) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -6.3 | 1e-07 | 14/22 (C32, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.681×** | -5.9 | 1e-06 | 17/22 (C32, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.675×** | -5.8 | 1e-06 | 14/22 (HepG2/C3A, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.703×** | -5.4 | 8e-06 | 9/21 (NCI-H460, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.706×** | -5.4 | 9e-06 | 13/22 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -5.1 | 3e-05 | 18/23 (HOP62, HS-578T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.703×** | -5.0 | 4e-05 | 4/22 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.742×** | -4.6 | 3e-04 | 13/22 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.743×** | -4.6 | 3e-04 | 8/22 (HepG2/C3A, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -4.3 | 8e-04 | 12/22 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.784×** | -3.7 | 0.009 | 11/22 (C32, SW 1088, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.789×** | -3.7 | 0.012 | 7/22 (H4, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.012 | 16/22 (HepG2/C3A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.024 | 9/21 (hTERT-HPNE, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.806×** | -3.3 | 0.032 | 9/21 (hTERT-HPNE, SW 1271, …) | two highest doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.682×** | -3.1 | 0.065 | 1/22 (C32) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 643 | 0 | 19 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 48.4 | 17 | 2 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 4.86× (z +10.5) | [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -8.7) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.255× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 243 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -13.6) |
| [[HS-578T (line)]] | alt | 496 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.328× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.385× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -9.5) |
| [[PANC-1 (line)]] | alt | 40.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.357× (z -9.5) |
| [[BT-474 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.0) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[H4 (line)]] | wt | 71.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 77.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +13.9) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -14.4) |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.373× (z -8.6) |
| [[SW 1088 (line)]] | alt | 202 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0913× (z -10.6) |
| [[A-427 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.72 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOXL3]] | +0.71 | +0.71 / +0.61 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[COL1A2]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[COL8A1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[SETBP1]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[COL4A2]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[CTHRC1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[COL15A1]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[AEBP1]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[PDE3A]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[FN1]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 | pathway: Cell surface interactions at the vascular wall; STRING 959 |
| [[PDGFRB]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_UV_RESPONSE_DN |
| [[KCNE4]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQANK1]] | -0.46 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ARHGEF5]] | -0.44 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[PATJ]] | -0.44 | -0.44 / -0.37 | both halves | 8e-05 | pathway: SARS-CoV-2 Infection |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 2, C 19. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | GXYLT2 activity raises SDC2's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 4.84× lower at baseline in the lines without GXYLT2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[CPQ]] | B | CPQ activity raises SDC2's level | lines that do not express CPQ (15) vs lines expressing it (35) | 4.06× lower at baseline in the lines without CPQ | 0.063 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[FLT1]] | C | FLT1 activity raises SDC2's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 5.82× lower at baseline in the lines without FLT1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises SDC2's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 6.57× lower at baseline in the lines without COL19A1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises SDC2's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 5.70× lower at baseline in the lines without EDNRB | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises SDC2's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 5.21× lower at baseline in the lines without PRRX1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises SDC2's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 3.76× lower at baseline in the lines without LOXL3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises SDC2's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 5.44× lower at baseline in the lines without C10orf90 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises SDC2's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 6.84× lower at baseline in the lines without FCRLA | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises SDC2's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 5.39× lower at baseline in the lines without IGFBP7 | 0.041 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises SDC2's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 6.36× lower at baseline in the lines without AEBP1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[ARHGEF6]] | C | ARHGEF6 activity raises SDC2's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 5.41× lower at baseline in the lines without ARHGEF6 | 0.052 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 5, C 24. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPQ]] | B | SDC2 activity raises CPQ's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 3.81× lower at baseline in the lines without SDC2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[ZCCHC24]] | B | SDC2 activity raises ZCCHC24's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.48× lower at baseline in the lines without SDC2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[GXYLT2]] | B | SDC2 activity raises GXYLT2's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without SDC2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[ATRNL1]] | B | SDC2 activity raises ATRNL1's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.81× lower at baseline in the lines without SDC2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[PCDHGC3]] | B | SDC2 activity raises PCDHGC3's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without SDC2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[FLT1]] | C | SDC2 activity raises FLT1's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without SDC2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[SPARC]] | C | SDC2 activity raises SPARC's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 6.42× lower at baseline in the lines without SDC2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[ARHGEF6]] | C | SDC2 activity raises ARHGEF6's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.79× lower at baseline in the lines without SDC2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[AEBP1]] | C | SDC2 activity raises AEBP1's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.77× lower at baseline in the lines without SDC2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[COL15A1]] | C | SDC2 activity raises COL15A1's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.80× lower at baseline in the lines without SDC2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[C10orf90]] | C | SDC2 activity raises C10orf90's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without SDC2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[STK32B]] | C | SDC2 activity raises STK32B's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 3.20× lower at baseline in the lines without SDC2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.3, 22.8); signed map (27.5, 41.5). **Vector** length 79.8, 22.3% of its response variance represented; |z| ≥ 3 in 731 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +13.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +10.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.1 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -6.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | syndecan 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:96,493,813-96,611,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | fibroglycan, SYND2, CD362; previously HSPG, HSPG1 |
| Gene groups (HGNC) | CD molecules; Syndecans |
| Hallmark sets | UV_RESPONSE_DN, GLYCOLYSIS, HYPOXIA |
| Reactome | 44 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; Defective B3GALT6 causes EDSP2 and SEMDJL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P34741](https://www.uniprot.org/uniprotkb/P34741) (Syndecan-2):

> Cell surface proteoglycan which regulates dendritic arbor morphogenesis.

**Summary**, from NCBI Gene [6383](https://www.ncbi.nlm.nih.gov/gene/6383):

> The protein encoded by this gene is a transmembrane (type I) heparan sulfate proteoglycan and is a member of the syndecan proteoglycan family. The syndecans mediate cell binding, cell signaling, and cytoskeletal organization and syndecan receptors are required for internalization of the HIV-1 tat protein. The syndecan-2 protein functions as an integral membrane protein and participates in cell proliferation, cell migration and cell-matrix interactions via its receptor for extracellular matrix …

**Accessions** — [HGNC:10659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10659) · Entrez [6383](https://www.ncbi.nlm.nih.gov/gene/6383) · UniProt [P34741](https://www.uniprot.org/uniprotkb/P34741) · Ensembl [ENSG00000169439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169439)

## Data

Gene col 9809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9809); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9809]; `tensor/DDL_lfc|DDL_z.npy` [9809]; `embed/gene_vectors.npy` [9809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9809 or target_col == 9809). Every well: [[SDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
