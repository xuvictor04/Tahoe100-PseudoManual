---
symbol: "IGFL4"
type: "gene"
col: 12930
ensembl_id: "ENSG00000204869"
name: "IGF like family member 4"
location: "19q13.32"
module: 27
arm: "+"
pooled_cpm: 6.55
n_lines_expressing: 25
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 33
direction_downstream: 26
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# IGFL4

*IGF like family member 4* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.15× (z +14.5, q 6e-45, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.36× (z +11.2, q 9e-27, up in 12 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.567× (z -4.8, q 7e-04, down in 5 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA2]] (+0.77, fdr 7e-06), [[APCDD1]] (+0.76, fdr 7e-06), [[NKD1]] (+0.74, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[F10]] → it (grade B ⚠); 26 go from it, the strongest it → [[LINC02320]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.15×** | +14.5 | 6e-45 | 2/5 (LoVo, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.14×** | +12.1 | 3e-31 | 3/6 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +11.2 | 9e-27 | 12/20 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.17×** | +10.6 | 3e-24 | 4/10 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +9.4 | 7e-19 | 9/21 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +6.6 | 3e-09 | 8/20 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +6.2 | 5e-08 | 7/20 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.7 | 7e-07 | 2/18 (BT-474, NCI-H1573) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +5.3 | 9e-06 | 5/20 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +4.6 | 2e-04 | 9/20 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.59×** | +4.3 | 1e-03 | 6/20 (NCI-H23, A-427, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.2 | 0.001 | 2/15 (NCI-H1573, NCI-H460) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.013 | 4/18 (SW48, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.2 | 0.049 | 0/19 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.567×** | -4.8 | 7e-04 | 5/20 (COLO 205, C32, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.627×** | -4.2 | 0.009 | 10/20 (SW48, COLO 205, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -3.9 | 0.017 | 9/20 (SW480, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.761×** | -3.6 | 0.045 | 5/22 (SW480, SW1417, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.685×** | -3.5 | 0.045 | 10/22 (COLO 205, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.774×** | -3.4 | 0.070 | 6/21 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.711× | -3.2 | 0.13 | 8/20 (SW480, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.0 | 0 | 18 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -20.0) |
| [[COLO 205 (line)]] | alt | 22.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0684× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0908× (z -10.3) |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -9.3) |
| [[SW1417 (line)]] | alt | 31.4 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.129× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 9.94 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0222× (z -12.5) |
| [[SW48 (line)]] | wt | 21.9 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0427× (z -10.6) |
| [[A-172 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA2]] | +0.77 | +0.77 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[NKD1]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KCNH8]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PROX1-AS1]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PROX1]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[FGF19]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SLC30A10]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.70 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ST18]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[LINC02254]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[LINC02964]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 6, C 27. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F10]] | B | F10 activity raises IGFL4's level | lines that do not express F10 (19) vs lines expressing it (31) | 1.92× lower at baseline in the lines without F10 | 0.051 | ⚠ within organs, on part of the lines; also absent: SELENOP, NIHCOLE, NOTUM; maybe low, not absent |
| [[LINC01091]] | B | LINC01091 activity raises IGFL4's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without LINC01091 | 0.057 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[PKHD1]] | B | PKHD1 activity raises IGFL4's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.79× lower at baseline in the lines without PKHD1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[IL19]] | B | IL19 activity raises IGFL4's level | lines that do not express IL19 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without IL19 | 0.070 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |
| [[NELL2]] | B | NELL2 activity raises IGFL4's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 1.44× lower at baseline in the lines without NELL2 | 0.093 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[CACNA2D4]] | B | CACNA2D4 activity raises IGFL4's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.51× lower at baseline in the lines without CACNA2D4 | 0.095 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[SORL1]] | C | SORL1 activity raises IGFL4's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.52× lower at baseline in the lines without SORL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3; co-absent with the target |
| [[VSNL1]] | C | VSNL1 activity raises IGFL4's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without VSNL1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2; co-absent with the target |
| [[RNF43]] | C | RNF43 activity raises IGFL4's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.00× lower at baseline in the lines without RNF43 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1; co-absent with the target |
| [[OPRD1]] | C | OPRD1 activity raises IGFL4's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without OPRD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises IGFL4's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.36× lower at baseline in the lines without EPS8L3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[SPTSSB]] | C | SPTSSB activity raises IGFL4's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 3.77× lower at baseline in the lines without SPTSSB | 0.010 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 7, C 19. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | IGFL4 activity raises LINC02320's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.74× lower at baseline in the lines without IGFL4 | 0.042 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[CACNA1E]] | B | IGFL4 activity raises CACNA1E's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.48× lower at baseline in the lines without IGFL4 | 0.053 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[PSD2]] | B | IGFL4 activity raises PSD2's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without IGFL4 | 0.071 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[TGFBR3]] | B | IGFL4 activity strengthens TGFBR3's drug response | lines that do not express IGFL4 (22) vs lines expressing it (20) | the lines without IGFL4 respond 1.10× as strongly (z diff -0.12); strongest at Harringtonine 0.5 µM: 0.86x vs 0.54x (z diff +3.4) | 0.076 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[IL19]] | B | IGFL4 activity raises IL19's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without IGFL4 | 0.081 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[CHDH]] | B | IGFL4 activity raises CHDH's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.18× lower at baseline in the lines without IGFL4 | 0.089 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[CFAP298-TCP10L]] | B | IGFL4 activity raises CFAP298-TCP10L's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.49× lower at baseline in the lines without IGFL4 | 0.096 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[RNF43]] | C | IGFL4 activity raises RNF43's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 5.64× lower at baseline in the lines without IGFL4 | 8e-04 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[VSNL1]] | C | IGFL4 activity raises VSNL1's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 3.78× lower at baseline in the lines without IGFL4 | 0.008 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[BMP4]] | C | IGFL4 activity raises BMP4's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 3.82× lower at baseline in the lines without IGFL4 | 0.018 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[SORL1]] | C | IGFL4 activity raises SORL1's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 3.40× lower at baseline in the lines without IGFL4 | 0.019 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[DIO3OS]] | C | IGFL4 activity raises DIO3OS's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without IGFL4 | 0.026 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 43.8); signed map (63.5, 15.2). **Vector** length 63.8, 17.5% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +12.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +4.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | IGF like family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,039,182-46,077,118 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | IGF like family |
| Matched by | ensembl_id |

UniProt [Q6B9Z1](https://www.uniprot.org/uniprotkb/Q6B9Z1) carries no function annotation.

**Summary**, from NCBI Gene [444882](https://www.ncbi.nlm.nih.gov/gene/444882):

> Predicted to enable signaling receptor binding activity. Predicted to be located in extracellular region. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32931) · Entrez [444882](https://www.ncbi.nlm.nih.gov/gene/444882) · UniProt [Q6B9Z1](https://www.uniprot.org/uniprotkb/Q6B9Z1) · Ensembl [ENSG00000204869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204869)

## Data

Gene col 12930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12930); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12930]; `tensor/DDL_lfc|DDL_z.npy` [12930]; `embed/gene_vectors.npy` [12930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12930 or target_col == 12930). Every well: [[IGFL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
