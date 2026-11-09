---
symbol: "SFTA1P"
type: "gene"
col: 13454
ensembl_id: "ENSG00000225383"
name: "surfactant associated 1, lncRNA"
location: "10p14"
module: 120
arm: "+"
pooled_cpm: 3.29
n_lines_expressing: 18
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 13
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# SFTA1P

*surfactant associated 1, lncRNA* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.59× (z +14.0, q 8e-42, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.40× (z +4.3, q 8e-04, up in 1 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.577× (z -4.0, q 0.036, down in 11 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF4]] (+0.64, fdr 7e-06), [[SRGAP1]] (+0.63, fdr 1e-05), [[DDAH1]] (+0.63, fdr 1e-05); moves opposite to [[VDAC2]] (-0.52, fdr 5e-05), [[SDHAP4]] (-0.51, fdr 6e-05), [[ZFYVE21]] (-0.48, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 13 go from it, the strongest it → [[DLC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.59×** | +14.0 | 8e-42 | 3/5 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.49×** | +10.8 | 1e-24 | 4/9 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.69×** | +10.3 | 2e-22 | 4/5 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.61×** | +6.9 | 9e-10 | 1/8 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +5.5 | 4e-06 | 6/12 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.91×** | +5.3 | 1e-05 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +5.2 | 1e-05 | 3/10 (A-427, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.0 | 5e-05 | 5/9 (RKO, Hs 766T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.3 | 8e-04 | 2/11 (HS-578T, HEC-1-A) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.40×** | +4.3 | 8e-04 | 1/11 (NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.16×** | +4.3 | 8e-04 | 2/5 (NCI-H2030, NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.49×** | +4.0 | 0.003 | 4/13 (A-427, RKO, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.004 | 1/15 (NCI-H2347) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.006 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.70×** | +3.8 | 0.006 | 1/11 (NCI-H2030) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.006 | 4/15 (NCI-H2347, J82, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.74×** | +3.6 | 0.008 | 0/12 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.98×** | +3.4 | 0.019 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.031 | 3/14 (SNU-423, C-33 A, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.043 | 2/11 (NCI-H2347, C-33 A) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.54×** | +3.1 | 0.049 | 1/11 (NCI-H2030) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +2.9 | 0.086 | 3/12 (Hs 766T, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.577×** | -4.0 | 0.036 | 11/14 (Hs 766T, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.607×** | -3.6 | 0.077 | 10/15 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.569×** | -3.5 | 0.077 | 9/16 (J82, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Fusidic acid (drug)]] 0.05 µM |  | 0.630× | -3.4 | 0.11 | 0/15 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.619× | -3.2 | 0.14 | 0/15 | inconsistent across doses |  |
| [[Cloxacillin (sodium) (drug)]] 0.5 µM |  | 0.647× | -3.2 | 0.14 | 0/14 | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.651× | -3.1 | 0.14 | 2/14 (NCI-H2347, RKO) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.646× | -3.1 | 0.16 | 2/15 (C-33 A, NCI-H2347) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 29.8 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -18.4) |
| [[A-427 (line)]] | wt | 50.3 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 5.77× (z +12.0) ⚠ cell-cycle shift, explains ~38% of this change | [[Belinostat (drug)]] 5 µM 0.247× (z -9.7) |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0613× (z -9.3) |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0754× (z -10.4) |
| [[HS-578T (line)]] | alt | 5.39 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0280× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 3.09 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0473× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.181× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 3.95 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0397× (z -9.0) |
| [[A-172 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.938 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.225 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.267 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF4]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SRGAP1]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LINC01776]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CCN1]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[IL31RA]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[FJX1]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SYDE2]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[STARD13]] | +0.56 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[LNCOG]] | +0.56 | +0.34 / +0.62 | both halves | 1e-04 | same gene group |
| [[CLCN4]] | +0.55 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[CCN2]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VDAC2]] | -0.52 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[SDHAP4]] | -0.51 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ZFYVE21]] | -0.48 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[PLD2]] | -0.48 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[SDHAP2]] | -0.45 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[HECTD3]] | -0.45 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[SEC11A]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SDHAP1]] | -0.45 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[UBAC1]] | -0.45 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[SDHAP4-1]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[OTULIN]] | -0.44 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[RTCA]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 8, C 5. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLC1]] | B | SFTA1P activity raises DLC1's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without SFTA1P | 0.013 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[CCN1]] | B | SFTA1P activity raises CCN1's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.48× lower at baseline in the lines without SFTA1P | 0.021 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[DDAH1]] | B | SFTA1P activity raises DDAH1's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.89× lower at baseline in the lines without SFTA1P | 0.036 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[CASC8]] | B | SFTA1P activity raises CASC8's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.45× lower at baseline in the lines without SFTA1P | 0.050 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[LTBP2]] | B | SFTA1P activity raises LTBP2's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without SFTA1P | 0.059 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[HDAC9]] | B | SFTA1P activity raises HDAC9's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without SFTA1P | 0.084 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[NAV3]] | B | SFTA1P activity raises NAV3's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.01× lower at baseline in the lines without SFTA1P | 0.085 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[FRMD6]] | B | SFTA1P activity raises FRMD6's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without SFTA1P | 0.095 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[KISS1]] | C | SFTA1P activity raises KISS1's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.10× lower at baseline in the lines without SFTA1P | 0.019 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1; co-absent with the target |
| [[LNCOG]] | C | SFTA1P activity raises LNCOG's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without SFTA1P | 0.043 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1; co-absent with the target |
| [[LINC01592]] | C | SFTA1P activity raises LINC01592's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without SFTA1P | 0.057 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1; co-absent with the target |
| [[BDNF]] | C | SFTA1P activity raises BDNF's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.57× lower at baseline in the lines without SFTA1P | 0.078 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.8, 12.5); signed map (14.0, 41.4). **Vector** length 30.3, 6.18% of its response variance represented; |z| ≥ 3 in 345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +1.9 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.8 | +2.0 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -0.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | surfactant associated 1, lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p14 — chr10:10,784,437-10,795,047 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SFTPF |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:18383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18383) · Entrez [207107](https://www.ncbi.nlm.nih.gov/gene/207107) · Ensembl [ENSG00000225383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225383)

## Data

Gene col 13454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13454); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13454]; `tensor/DDL_lfc|DDL_z.npy` [13454]; `embed/gene_vectors.npy` [13454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13454 or target_col == 13454). Every well: [[SFTA1P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFTA1P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
