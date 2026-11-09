---
symbol: "PCSK9"
type: "gene"
col: 9764
ensembl_id: "ENSG00000169174"
name: "proprotein convertase subtilisin/kexin type 9"
location: "1p32.3"
module: 86
arm: "+"
pooled_cpm: 4.51
n_lines_expressing: 22
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 23
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# PCSK9

*proprotein convertase subtilisin/kexin type 9* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.76× (z +10.9, q 8e-25, up in 18 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.690× (z -4.0, q 0.018, down in 9 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHCR7]] (+0.76, fdr 7e-06), [[HMGCR]] (+0.76, fdr 7e-06), [[FDPS]] (+0.75, fdr 7e-06); moves opposite to [[FCF1]] (-0.47, fdr 4e-05), [[CCDC90B]] (-0.47, fdr 2e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[COL9A3]] → it (grade B ⚠); 23 go from it, the strongest it → [[CD46]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.76×** | +10.9 | 8e-25 | 18/20 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +10.0 | 3e-21 | 6/11 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.83×** | +9.8 | 2e-20 | 5/5 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Berbamine (drug)]] 5 µM |  | **2.47×** | +9.7 | 6e-20 | 19/20 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.85×** | +9.4 | 4e-19 | 3/10 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.78×** | +7.4 | 1e-11 | 10/15 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.16×** | +5.8 | 4e-07 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.6 | 2e-06 | 4/17 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.37×** | +4.8 | 9e-05 | 2/4 (HEC-1-A, CFPAC-1) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.30×** | +4.7 | 1e-04 | 5/12 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.31×** | +4.5 | 3e-04 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.5 | 3e-04 | 2/12 (NCI-H2347, CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +4.2 | 1e-03 | 4/14 (AsPC-1, SW48, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.002 | 10/20 (AsPC-1, SW480, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.71×** | +4.0 | 0.002 | 7/19 (HEC-1-A, SW480, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.003 | 9/20 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Berbamine (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.004 | 10/19 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.004 | 4/20 (AsPC-1, HT-29, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.97×** | +3.7 | 0.007 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.007 | 8/20 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; position effect removed |
| [[Ritonavir (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.020 | 5/20 (LS 180, HEC-1-A, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.56×** | +3.4 | 0.020 | 0/19 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.036 | 5/19 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.041 | 5/18 (SNU-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.690×** | -4.0 | 0.018 | 9/20 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.592×** | -3.9 | 0.018 | 13/19 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -3.9 | 0.018 | 14/20 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -3.8 | 0.018 | 12/18 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.409×** | -3.6 | 0.040 | 6/20 (Panc 03.27, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Quinestrol (drug)]] 5 µM |  | **0.725×** | -3.5 | 0.042 | 6/20 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.452× | -3.2 | 0.12 | 2/20 (HEC-1-A, HCT15) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM |  | 0.576× | -3.0 | 0.17 | 2/20 (KATO III, LS 180) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 12.0 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0514× (z -10.1) |
| [[LoVo (line)]] | wt | 23.8 | 2 | 3 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 7.47× (z +14.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 16.1 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.28× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 56.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -14.0) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.292× (z -8.9) |
| [[SW480 (line)]] | alt | 4.99 | 1 | 1 | [[Cepharanthine (drug)]] 5 µM 4.03× (z +8.6) | [[GSK1059615 (drug)]] 0.5 µM 0.0530× (z -9.3) |
| [[LS 180 (line)]] | wt | 35.3 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 4.74× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 4.59 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0483× (z -9.4) |
| [[SW48 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.2) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHCR7]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 | STRING 421 |
| [[HMGCR]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 | STRING 910 |
| [[FDPS]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 | STRING 404 |
| [[MSMO1]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[FDFT1]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[FASN]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SCD]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ACSS2]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ACAT2]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[DHCR24]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[PNPLA3]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MVD]] | +0.67 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCF1]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[CCDC90B]] | -0.47 | -0.52 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL9A3]] | B | COL9A3 activity lowers PCSK9's level | lines that do not express COL9A3 (28) vs lines expressing it (22) | 1.46× higher at baseline in the lines without COL9A3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000259639, AK4P3, LINC01169 |
| [[FGFBP1]] | C | FGFBP1 activity raises PCSK9's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 4.03× lower at baseline in the lines without FGFBP1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[MSLN]] | C | MSLN activity raises PCSK9's level | lines that do not express MSLN (33) vs lines expressing it (17) | 3.60× lower at baseline in the lines without MSLN | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |
| [[LINC02474]] | C | LINC02474 activity raises PCSK9's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 4.24× lower at baseline in the lines without LINC02474 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises PCSK9's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 2.96× lower at baseline in the lines without EPCAM | 0.042 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises PCSK9's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.96× lower at baseline in the lines without ST6GALNAC1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises PCSK9's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.08× lower at baseline in the lines without MUC5B | 0.073 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises PCSK9's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.86× lower at baseline in the lines without MUC6 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 10, C 13. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD46]] | B | PCSK9 activity raises CD46's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without PCSK9 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[TSPAN14]] | B | PCSK9 activity raises TSPAN14's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.55× lower at baseline in the lines without PCSK9 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[LINC02580]] | B | PCSK9 activity raises LINC02580's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without PCSK9 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[MSMO1]] | B | PCSK9 activity raises MSMO1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without PCSK9 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[FADS1]] | B | PCSK9 activity lowers FADS1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 2.83× higher at baseline in the lines without PCSK9 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[FLVCR1]] | B | PCSK9 activity lowers FLVCR1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.27× higher at baseline in the lines without PCSK9 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[SNAI3-AS1]] | B | PCSK9 activity lowers SNAI3-AS1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.37× higher at baseline in the lines without PCSK9 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | PCSK9 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express PCSK9 (28) vs lines expressing it (20) | the lines without PCSK9: 0.81× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[ACAT2]] | B | PCSK9 activity lowers ACAT2's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.06× higher at baseline in the lines without PCSK9 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[TRIM2]] | B | PCSK9 activity raises TRIM2's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without PCSK9 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[EPCAM]] | C | PCSK9 activity raises EPCAM's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 7.83× lower at baseline in the lines without PCSK9 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1; co-absent with the target |
| [[MSLN]] | C | PCSK9 activity raises MSLN's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 3.51× lower at baseline in the lines without PCSK9 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1; co-absent with the target |

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, -49.4); signed map (-52.5, 32.4). **Vector** length 56.8, 15.4% of its response variance represented; |z| ≥ 3 in 523 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis* (reactome, mean cos +0.64 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.63 to 24); *Metabolism of steroids* (reactome, mean cos +0.63 to 25).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.7 | +7.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.6 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.8 | +9.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +4.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | proprotein convertase subtilisin/kexin type 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:55,039,445-55,064,852 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NARC-1, FH3; previously HCHOLA3 |
| Gene groups (HGNC) | Proprotein convertase subtilisin/kexin family |
| Hallmark sets | APICAL_SURFACE, COMPLEMENT |
| Reactome | 7 pathways, smallest: VLDLR internalisation and degradation; LDL clearance; Plasma lipoprotein clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBP7](https://www.uniprot.org/uniprotkb/Q8NBP7) (Proprotein convertase subtilisin/kexin type 9):

> Crucial player in the regulation of plasma cholesterol homeostasis. Binds to low-density lipid receptor family members: low density lipoprotein receptor (LDLR), very low density lipoprotein receptor (VLDLR), apolipoprotein E receptor (LRP1/APOER) and apolipoprotein receptor 2 (LRP8/APOER2), and promotes their degradation in intracellular acidic compartments. Acts via a non-proteolytic mechanism to enhance the degradation of the hepatic LDLR through a clathrin LDLRAP1/ARH-mediated pathway. May …

**Summary**, from NCBI Gene [255738](https://www.ncbi.nlm.nih.gov/gene/255738):

> This gene encodes a member of the subtilisin-like proprotein convertase family, which includes proteases that process protein and peptide precursors trafficking through regulated or constitutive branches of the secretory pathway. The encoded protein undergoes an autocatalytic processing event with its prosegment in the ER and is constitutively secreted as an inactive protease into the extracellular matrix and trans-Golgi network. It is expressed in liver, intestine and kidney tissues and …

**Accessions** — [HGNC:20001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20001) · Entrez [255738](https://www.ncbi.nlm.nih.gov/gene/255738) · UniProt [Q8NBP7](https://www.uniprot.org/uniprotkb/Q8NBP7) · Ensembl [ENSG00000169174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169174)

## Data

Gene col 9764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9764); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9764]; `tensor/DDL_lfc|DDL_z.npy` [9764]; `embed/gene_vectors.npy` [9764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9764 or target_col == 9764). Every well: [[PCSK9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCSK9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
