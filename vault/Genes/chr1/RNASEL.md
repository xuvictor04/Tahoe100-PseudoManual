---
symbol: "RNASEL"
type: "gene"
col: 5761
ensembl_id: "ENSG00000135828"
name: "ribonuclease L"
location: "1q25.3"
module: 12
arm: "+"
pooled_cpm: 5.36
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RNASEL

*ribonuclease L* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.42× (z +4.8, q 9e-04, up in 11 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.354× (z -10.0, q 1e-20, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC43]] (+0.59, fdr 1e-05), [[DNAJB4]] (+0.59, fdr 1e-05), [[RSRC2]] (+0.58, fdr 3e-05); moves opposite to [[PACS2]] (-0.55, fdr 3e-05), [[TRAP1]] (-0.54, fdr 3e-05), [[QSOX2]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02967]] → it (grade B ⚠); 9 go from it, the strongest it → [[TRIM38]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.8 | 9e-04 | 11/43 (LS 180, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.010 | 11/39 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.0 | 0.010 | 1/8 (A498) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.9 | 0.013 | 11/31 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.016 | 11/42 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.016 | 11/40 (CFPAC-1, A-172, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.064 | 10/41 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.37× | +3.2 | 0.10 | 7/43 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.38× | +3.1 | 0.12 | 7/41 (NCI-H460, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5761.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.354×** | -10.0 | 1e-20 | 31/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.382×** | -9.3 | 6e-18 | 29/40 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.463×** | -7.4 | 3e-11 | 26/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.586×** | -7.3 | 6e-11 | 25/38 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.505×** | -6.6 | 6e-09 | 25/40 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.506×** | -6.5 | 6e-09 | 23/42 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.284×** | -6.3 | 2e-08 | 24/38 (KATO III, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.525×** | -6.2 | 5e-08 | 24/41 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.530×** | -5.9 | 3e-07 | 20/33 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.837× | -5.7 | 7e-07 | 19/43 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.324×** | -5.7 | 7e-07 | 22/37 (NCI-H1573, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.620×** | -4.6 | 2e-04 | 16/41 (COLO 205, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.631×** | -4.4 | 4e-04 | 21/36 (NCI-H1573, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[EX229 (drug)]] 5 µM |  | **0.471×** | -3.8 | 0.006 | 10/36 (SW 900, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.682×** | -3.7 | 0.009 | 11/43 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.682×** | -3.7 | 0.009 | 14/37 (Panc 03.27, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.765×** | -3.6 | 0.010 | 13/43 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.727×** | -3.1 | 0.067 | 12/40 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0318× (z -27.8) |
| [[NCI-H460 (line)]] | wt | 8.19 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0845× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -10.5) |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0976× (z -11.6) |
| [[HOP62 (line)]] | alt | 3.38 | 0 | 2 | — | [[Decitabine (drug)]] 0.5 µM 0.0707× (z -9.0) |
| [[A549 (line)]] | wt | 5.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 2.94 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0512× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 2.63 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0384× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 3.71 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0819× (z -9.2) |
| [[RKO (line)]] | wt | 4.03 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0325× (z -10.4) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC43]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[DNAJB4]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[RSRC2]] | +0.58 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SLC4A1AP]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[NAT1]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CHD8]] | +0.57 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[CASP4]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_APOPTOSIS |
| [[LINC02967]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LINC01684]] | +0.55 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SNW1]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[PSMA4]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CASP7]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_APOPTOSIS |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACS2]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TRAP1]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[QSOX2]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ITPR3]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[COLGALT1]] | -0.52 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[ARL6IP6]] | -0.52 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[TCF3]] | -0.51 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[MSH5]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD36]] | -0.50 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[MAPK1]] | -0.49 | -0.34 / -0.53 | both halves | 1e-04 | pathway: Interferon Signaling |
| [[SFXN2]] | -0.48 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TBCD]] | -0.48 | -0.22 / -0.56 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02967]] | B | LINC02967 activity raises RNASEL's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 1.54× lower at baseline in the lines without LINC02967 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[GBP3]] | B | GBP3 activity raises RNASEL's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without GBP3 | 0.020 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[CARD6]] | B | CARD6 activity raises RNASEL's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without CARD6 | 0.032 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[PTGR1]] | B | PTGR1 activity raises RNASEL's level | lines that do not express PTGR1 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without PTGR1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises RNASEL's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.58× lower at baseline in the lines without NMRAL2P-1 | 0.068 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[FRMD4B]] | B | FRMD4B activity raises RNASEL's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without FRMD4B | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[TLR3]] | B | TLR3 activity raises RNASEL's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without TLR3 | 0.098 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM38]] | B | RNASEL activity raises TRIM38's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 4.34× lower at baseline in the lines without RNASEL | 0.021 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[GBP3]] | B | RNASEL activity raises GBP3's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 5.89× lower at baseline in the lines without RNASEL | 0.024 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[CASP4]] | B | RNASEL activity raises CASP4's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 4.00× lower at baseline in the lines without RNASEL | 0.024 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[TLR6]] | B | RNASEL activity raises TLR6's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 3.05× lower at baseline in the lines without RNASEL | 0.052 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[PSMB6]] | B | RNASEL activity lowers PSMB6's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 1.46× higher at baseline in the lines without RNASEL | 0.068 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[TYW3]] | B | RNASEL activity lowers TYW3's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 1.37× higher at baseline in the lines without RNASEL | 0.084 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[LINC02328]] | B | RNASEL activity raises LINC02328's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 3.14× lower at baseline in the lines without RNASEL | 0.090 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[ZFAND5]] | B | RNASEL activity raises ZFAND5's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 1.34× lower at baseline in the lines without RNASEL | 0.091 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[ERAP2]] | C | RNASEL activity raises ERAP2's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 3.34× lower at baseline in the lines without RNASEL | 0.081 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.439). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (25.6, -31.6); signed map (6.9, -9.8). **Vector** length 61.3, 10.3% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -6.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | -6.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.8 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:182,573,634-182,589,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RNS4, PRCA1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Pseudokinases; Endoribonucleases |
| Hallmark sets | APOPTOSIS |
| Reactome | 5 pathways, smallest: OAS antiviral response; Interferon alpha/beta signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05823](https://www.uniprot.org/uniprotkb/Q05823) (2-5A-dependent ribonuclease):

> Endoribonuclease that functions in the interferon (IFN) antiviral response. In INF treated and virus infected cells, RNASEL probably mediates its antiviral effects through a combination of direct cleavage of single-stranded viral RNAs, inhibition of protein synthesis through the degradation of rRNA, induction of apoptosis, and induction of other antiviral genes. RNASEL mediated apoptosis is the result of a JNK-dependent stress-response pathway leading to cytochrome c release from mitochondria …

**Summary**, from NCBI Gene [6041](https://www.ncbi.nlm.nih.gov/gene/6041):

> This gene encodes a component of the interferon-regulated 2-5A system that functions in the antiviral and antiproliferative roles of interferons. The protein is involved in innate immunity and is active against multiple RNA viruses, including the influenza and SARS-CoV-2 viruses. Mutations in this gene have been associated with predisposition to prostate cancer and this gene is a candidate for the hereditary prostate cancer 1 (HPC1) allele. [provided by RefSeq, Nov 2021]

**Accessions** — [HGNC:10050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10050) · Entrez [6041](https://www.ncbi.nlm.nih.gov/gene/6041) · UniProt [Q05823](https://www.uniprot.org/uniprotkb/Q05823) · Ensembl [ENSG00000135828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135828)

## Data

Gene col 5761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5761); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5761]; `tensor/DDL_lfc|DDL_z.npy` [5761]; `embed/gene_vectors.npy` [5761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5761 or target_col == 5761). Every well: [[RNASEL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASEL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
