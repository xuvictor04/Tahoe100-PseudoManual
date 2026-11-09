---
symbol: "LGR6"
type: "gene"
col: 5410
ensembl_id: "ENSG00000133067"
name: "leucine rich repeat containing G protein-coupled receptor 6"
location: "1q32.1"
module: 55
arm: "+"
pooled_cpm: 7.38
n_lines_expressing: 15
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 28
direction_downstream: 61
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# LGR6

*leucine rich repeat containing G protein-coupled receptor 6* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.68× (z +12.4, q 8e-33, up in 1 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +11.0, q 6e-26, up in 0 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.620× (z -4.4, q 0.005, down in 9 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AFAP1L2]] (+0.77, fdr 7e-06), [[INPP5D]] (+0.76, fdr 7e-06), [[EDAR]] (+0.73, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.54, fdr 4e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[EDAR]] → it (grade C ⚠); 61 go from it, the strongest it → [[PITPNM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.68×** | +12.4 | 8e-33 | 1/9 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.75×** | +12.1 | 2e-31 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +11.0 | 6e-26 | 0/12 | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +10.0 | 2e-21 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +6.8 | 2e-09 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.5 | 4e-06 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.9 | 8e-05 | 4/12 (LS 180, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.4 | 7e-04 | 2/12 (RPMI-7951, SW1417) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.2 | 0.002 | 1/12 (Panc 03.27) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.53×** | +4.0 | 0.004 | 4/12 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.004 | 0/12 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.74×** | +3.8 | 0.007 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.8 | 0.007 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +3.7 | 0.008 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.009 | 1/12 (RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.023 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.026 | 1/12 (Hs 766T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -4.4 | 0.005 | 9/12 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.657×** | -4.1 | 0.012 | 5/12 (Hs 766T, AsPC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.666×** | -3.9 | 0.012 | 9/12 (SW480, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -3.9 | 0.012 | 8/12 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.673×** | -3.6 | 0.032 | 0/12 | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.681×** | -3.6 | 0.032 | 2/12 (Hs 766T, AsPC-1) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.719× | -3.2 | 0.11 | 9/12 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.730× | -3.1 | 0.16 | 9/12 (SW480, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 69.4 | 0 | 20 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0520× (z -23.4) |
| [[SW480 (line)]] | alt | 48.3 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0400× (z -22.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0469× (z -21.4) |
| [[KATO III (line)]] | alt | 19.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.5) |
| [[LoVo (line)]] | wt | 9.98 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0369× (z -17.2) |
| [[SW1417 (line)]] | alt | 32.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -18.9) |
| [[AsPC-1 (line)]] | alt | 19.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0761× (z -11.2) |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0329× (z -13.5) |
| [[LS 180 (line)]] | wt | 6.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -10.5) |
| [[A-172 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.000 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.865 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFAP1L2]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[INPP5D]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.72 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.72 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[FGD5]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ABO]] | +0.68 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[VWA2]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 0, C 28. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDAR]] | C | EDAR activity raises LGR6's level | lines that do not express EDAR (36) vs lines expressing it (14) | 5.33× lower at baseline in the lines without EDAR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[IL20RA]] | C | IL20RA activity raises LGR6's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 4.21× lower at baseline in the lines without IL20RA | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises LGR6's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 1.90× lower at baseline in the lines without PSG1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[PRR15]] | C | PRR15 activity raises LGR6's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 3.16× lower at baseline in the lines without PRR15 | 0.013 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises LGR6's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 2.87× lower at baseline in the lines without LINC01819 | 0.020 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[VSNL1]] | C | VSNL1 activity raises LGR6's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 3.48× lower at baseline in the lines without VSNL1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2; co-absent with the target |
| [[SPON1]] | C | SPON1 activity raises LGR6's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 3.55× lower at baseline in the lines without SPON1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[TMPRSS3]] | C | TMPRSS3 activity raises LGR6's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without TMPRSS3 | 0.031 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises LGR6's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 3.29× lower at baseline in the lines without FGFBP1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[ABO]] | C | ABO activity raises LGR6's level | lines that do not express ABO (32) vs lines expressing it (18) | 3.69× lower at baseline in the lines without ABO | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK; co-absent with the target |
| [[FGD5]] | C | FGD5 activity raises LGR6's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 3.06× lower at baseline in the lines without FGD5 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[SIM1]] | C | SIM1 activity raises LGR6's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 1.46× lower at baseline in the lines without SIM1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |

### Downstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 7, C 54. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PITPNM3]] | B | LGR6 activity raises PITPNM3's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without LGR6 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[MFSD6]] | B | LGR6 activity raises MFSD6's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.37× lower at baseline in the lines without LGR6 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[IGSF9]] | B | LGR6 activity raises IGSF9's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.23× lower at baseline in the lines without LGR6 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[TJP2]] | B | LGR6 activity raises TJP2's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.68× lower at baseline in the lines without LGR6 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[TSPAN2]] | B | LGR6 activity raises TSPAN2's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 1.84× lower at baseline in the lines without LGR6 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[DLG3]] | B | LGR6 activity raises DLG3's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.58× lower at baseline in the lines without LGR6 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[MGST2]] | B | LGR6 activity raises MGST2's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.31× lower at baseline in the lines without LGR6 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[SLC6A20]] | C | LGR6 activity raises SLC6A20's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 6.64× lower at baseline in the lines without LGR6 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[KLK10]] | C | LGR6 activity raises KLK10's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 10.40× lower at baseline in the lines without LGR6 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[SULF2]] | C | LGR6 activity raises SULF2's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 6.32× lower at baseline in the lines without LGR6 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[BMP4]] | C | LGR6 activity raises BMP4's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 6.08× lower at baseline in the lines without LGR6 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[COL17A1]] | C | LGR6 activity raises COL17A1's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 6.65× lower at baseline in the lines without LGR6 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.8, 48.4); signed map (63.7, 10.4). **Vector** length 59.5, 23.8% of its response variance represented; |z| ≥ 3 in 362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | -1.1 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -4.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing G protein-coupled receptor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,193,799-202,319,781 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14471 |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Reactome | 3 pathways, smallest: Regulation of FZD by ubiquitination; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBX8](https://www.uniprot.org/uniprotkb/Q9HBX8) (Leucine-rich repeat-containing G protein-coupled receptor 6):

> Receptor for R-spondins that potentiates the canonical Wnt signaling pathway and acts as a marker of multipotent stem cells in the epidermis. Upon binding to R-spondins (RSPO1, RSPO2, RSPO3 or RSPO4), associates with phosphorylated LRP6 and frizzled receptors that are activated by extracellular Wnt receptors, triggering the canonical Wnt signaling pathway to increase expression of target genes. In contrast to classical G protein-coupled receptors, does not activate heterotrimeric G proteins to …

**Summary**, from NCBI Gene [59352](https://www.ncbi.nlm.nih.gov/gene/59352):

> This gene encodes a member of the leucine-rich repeat-containing subgroup of the G protein-coupled 7-transmembrane protein superfamily. The encoded protein is a glycoprotein hormone receptor with a large N-terminal extracellular domain that contains leucine-rich repeats important for the formation of a horseshoe-shaped interaction motif for ligand binding. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19719) · Entrez [59352](https://www.ncbi.nlm.nih.gov/gene/59352) · UniProt [Q9HBX8](https://www.uniprot.org/uniprotkb/Q9HBX8) · Ensembl [ENSG00000133067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133067)

## Data

Gene col 5410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5410); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5410]; `tensor/DDL_lfc|DDL_z.npy` [5410]; `embed/gene_vectors.npy` [5410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5410 or target_col == 5410). Every well: [[LGR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
