---
symbol: "HNF1A"
type: "gene"
col: 5653
ensembl_id: "ENSG00000135100"
name: "HNF1 homeobox A"
location: "12q24.31"
module: 27
arm: "+"
pooled_cpm: 2.18
n_lines_expressing: 20
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 17
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# HNF1A

*HNF1 homeobox A* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.33× (z +11.0, q 2e-25, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.79× (z +9.9, q 8e-21, up in 7 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.544× (z -4.2, q 0.016, down in 11 of 16 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA10-AS]] (+0.69, fdr 1e-05), [[HOTAIR]] (+0.64, fdr 2e-05), [[HOXA7]] (+0.60, fdr 2e-05); moves opposite to [[LYPD3]] (-0.60, fdr 3e-05), [[RTN4]] (-0.56, fdr 3e-05), [[SEPTIN10]] (-0.52, fdr 4e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 17 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.33×** | +11.0 | 2e-25 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +9.9 | 8e-21 | 7/14 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +9.4 | 9e-19 | 9/15 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.69×** | +8.3 | 2e-14 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +6.1 | 9e-08 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.29×** | +5.7 | 1e-06 | 2/10 (HepG2/C3A, LoVo) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +5.2 | 2e-05 | 3/12 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.63×** | +4.7 | 2e-04 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +4.3 | 0.001 | 9/16 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +4.3 | 0.001 | 3/12 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.2 | 0.002 | 1/9 (LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +4.1 | 0.002 | 5/13 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.20×** | +3.8 | 0.005 | 1/14 (KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.75×** | +3.8 | 0.006 | 1/11 (HT-29) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.71×** | +3.6 | 0.014 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.68×** | +3.5 | 0.014 | 1/11 (HT-29) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.023 | 1/16 (A549) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.028 | 5/14 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.94×** | +3.2 | 0.034 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.057 | 3/15 (LoVo, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +3.0 | 0.064 | 6/16 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5653.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.544×** | -4.2 | 0.016 | 11/16 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.564×** | -3.9 | 0.024 | 12/16 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.583×** | -3.7 | 0.040 | 12/16 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.4 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 6.46× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.0760× (z -14.6) |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -10.5) |
| [[SW480 (line)]] | alt | 7.63 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0837× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +13.0) | — |
| [[A-172 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.587 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.604 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA10-AS]] | +0.69 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[HOTAIR]] | +0.64 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[HOXA7]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CDX2]] | +0.59 | +0.45 / +0.67 | both halves | 3e-05 | STRING 833 |
| [[STAP2]] | +0.58 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RPRD2]] | +0.58 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[P4HTM]] | +0.57 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[GRHL2]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[A1CF]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 | STRING 474 |
| [[CHDH]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MARVELD2]] | +0.55 | +0.46 / +0.32 | both halves | 2e-04 |  |
| [[MKX]] | +0.55 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPD3]] | -0.60 | -0.53 / -0.43 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[RTN4]] | -0.56 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SEPTIN10]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LMTK3]] | -0.52 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[FLNB]] | -0.52 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[LRRFIP1]] | -0.52 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[CAP1]] | -0.51 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[GNAI3]] | -0.51 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[MICAL2]] | -0.50 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[KIF21B]] | -0.49 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[SH3BGRL3]] | -0.48 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[SPAG9]] | -0.48 | -0.41 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HNF1A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LMTK3]] | B | LMTK3 activity raises HNF1A's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.80× lower at baseline in the lines without LMTK3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[A1CF]] | C | A1CF activity raises HNF1A's level | lines that do not express A1CF (35) vs lines expressing it (15) | 3.06× lower at baseline in the lines without A1CF | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[RASSF6]] | C | RASSF6 activity raises HNF1A's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without RASSF6 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6; co-absent with the target |
| [[MTUS1-DT]] | C | MTUS1-DT activity raises HNF1A's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.02× lower at baseline in the lines without MTUS1-DT | 0.025 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3; co-absent with the target |
| [[TSPAN8]] | C | TSPAN8 activity raises HNF1A's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without TSPAN8 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17; co-absent with the target |
| [[NPNT]] | C | NPNT activity raises HNF1A's level | lines that do not express NPNT (33) vs lines expressing it (17) | 2.61× lower at baseline in the lines without NPNT | 0.041 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[SPINT1-AS1]] | C | SPINT1-AS1 activity raises HNF1A's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without SPINT1-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3; co-absent with the target |
| [[LINC01610]] | C | LINC01610 activity raises HNF1A's level | lines that do not express LINC01610 (45) vs lines expressing it (5) | 1.52× lower at baseline in the lines without LINC01610 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC00879, LINC02099; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 8, C 9. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | HNF1A activity raises LMTK3's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without HNF1A | 0.031 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[SH3BGRL2]] | B | HNF1A activity raises SH3BGRL2's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 3.04× lower at baseline in the lines without HNF1A | 0.035 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[STX19]] | B | HNF1A activity raises STX19's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 1.98× lower at baseline in the lines without HNF1A | 0.041 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[LYPD3]] | B | HNF1A activity raises LYPD3's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without HNF1A | 0.047 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[MARVELD2]] | B | HNF1A activity raises MARVELD2's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 2.70× lower at baseline in the lines without HNF1A | 0.052 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[MBNL3]] | B | HNF1A activity raises MBNL3's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 2.76× lower at baseline in the lines without HNF1A | 0.062 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[LATS1]] | B | HNF1A activity lowers LATS1's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 1.11× higher at baseline in the lines without HNF1A | 0.083 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[HSD11B2]] | B | HNF1A activity raises HSD11B2's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without HNF1A | 0.091 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[RASSF6]] | C | HNF1A activity raises RASSF6's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 5.77× lower at baseline in the lines without HNF1A | 0.001 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent; co-absent with the target |
| [[NPNT]] | C | HNF1A activity raises NPNT's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 4.99× lower at baseline in the lines without HNF1A | 0.003 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent; co-absent with the target |
| [[TSPAN8]] | C | HNF1A activity raises TSPAN8's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 3.80× lower at baseline in the lines without HNF1A | 0.008 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent; co-absent with the target |
| [[MTUS1-DT]] | C | HNF1A activity raises MTUS1-DT's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without HNF1A | 0.012 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.1, 28.0); signed map (37.1, -17.2). **Vector** length 40.8, 11.1% of its response variance represented; |z| ≥ 3 in 306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | -0.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -1.4 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.2 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.2 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | HNF1 homeobox A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,978,543-121,002,512 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNF1, LFB1, HNF1α; previously MODY3, TCF1 |
| Gene groups (HGNC) | HNF class homeoboxes |
| Hallmark sets | PANCREAS_BETA_CELLS, KRAS_SIGNALING_DN |
| Reactome | 2 pathways, smallest: Regulation of gene expression in beta cells; Regulation of beta-cell development |
| Matched by | ensembl_id |

**Function**, from UniProt [P20823](https://www.uniprot.org/uniprotkb/P20823) (Hepatocyte nuclear factor 1-alpha):

> Transcriptional activator that regulates the tissue specific expression of multiple genes, especially in pancreatic islet cells and in liver (By similarity). Binds to the inverted palindrome 5'-GTTAATNATTAAC-3'. Activates the transcription of CYP1A2, CYP2E1 and CYP3A11 (By similarity).; (Microbial infection) Plays a crucial role for hepatitis B virus gene transcription and DNA replication. Mechanistically, synergistically cooperates with NR5A2 to up-regulate the activity of one of the critical …

**Summary**, from NCBI Gene [6927](https://www.ncbi.nlm.nih.gov/gene/6927):

> The protein encoded by this gene is a transcription factor required for the expression of several liver-specific genes. The encoded protein functions as a homodimer and binds to the inverted palindrome 5'-GTTAATNATTAAC-3'. Defects in this gene are a cause of maturity onset diabetes of the young type 3 (MODY3) and also can result in the appearance of hepatic adenomas. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:11621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11621) · Entrez [6927](https://www.ncbi.nlm.nih.gov/gene/6927) · UniProt [P20823](https://www.uniprot.org/uniprotkb/P20823) · Ensembl [ENSG00000135100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135100)

## Data

Gene col 5653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5653); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5653]; `tensor/DDL_lfc|DDL_z.npy` [5653]; `embed/gene_vectors.npy` [5653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5653 or target_col == 5653). Every well: [[HNF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
