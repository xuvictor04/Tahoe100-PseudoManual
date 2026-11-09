---
symbol: "BCAS1"
type: "gene"
col: 761
ensembl_id: "ENSG00000064787"
name: "brain enriched myelin associated protein 1"
location: "20q13.2"
module: 8
arm: "+"
pooled_cpm: 11.48
n_lines_expressing: 18
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 74
direction_downstream: 90
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# BCAS1

*brain enriched myelin associated protein 1* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.30× (z +14.9, q 0e+00, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 3.82× (z +14.2, q 3e-43, up in 12 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.566× (z -4.3, q 0.011, down in 11 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYNPR-AS1]] (+0.77, fdr 7e-06), [[BCL2L15]] (+0.75, fdr 7e-06), [[ERBB3]] (+0.74, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 74 arrows point to it, the strongest [[SORL1]] → it (grade B ⚠); 90 go from it, the strongest it → [[STX19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.30×** | +14.9 | 0e+00 | 8/10 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.82×** | +14.2 | 3e-43 | 12/14 (hTERT-HPNE, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.55×** | +10.9 | 2e-25 | 4/6 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.96×** | +10.3 | 8e-23 | 8/15 (hTERT-HPNE, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.15×** | +9.9 | 7e-21 | 5/7 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +9.6 | 9e-20 | 2/13 (hTERT-HPNE, MIA PaCa-2) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.17×** | +8.6 | 5e-16 | 5/13 (hTERT-HPNE, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +7.7 | 7e-13 | 1/12 (SW1417) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.59×** | +7.1 | 6e-11 | 11/14 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +4.3 | 8e-04 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +4.3 | 8e-04 | 9/14 (COLO 205, KATO III, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **2.90×** | +4.2 | 0.001 | 9/12 (BT-474, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +3.9 | 0.004 | 4/13 (hTERT-HPNE, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.8 | 0.006 | 2/11 (NCI-H1573, BT-474) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.63×** | +3.7 | 0.009 | 7/13 (KATO III, COLO 205, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +3.7 | 0.009 | 5/15 (hTERT-HPNE, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.019 | 3/13 (BT-474, COLO 205, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.019 | 7/13 (NCI-H1573, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.019 | 7/13 (LS 180, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.87×** | +3.4 | 0.023 | 4/13 (NCI-H1573, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 761.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.566×** | -4.3 | 0.011 | 11/13 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.595×** | -3.9 | 0.029 | 8/14 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.718×** | -3.5 | 0.080 | 1/14 (SW1417) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.631×** | -3.4 | 0.080 | 4/13 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 189 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0460× (z -23.5) |
| [[COLO 205 (line)]] | alt | 49.7 | 0 | 13 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0332× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -15.5) |
| [[NCI-H1573 (line)]] | alt | 42.9 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0804× (z -15.6) |
| [[HepG2_C3A (line)]] | wt | 31.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.63× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.0296× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 3.02 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 27.6× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 7.05 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.93× (z +8.7) | — |
| [[A-172 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNPR-AS1]] | +0.77 | +0.68 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.75 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ERBB3]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TJP3]] | +0.72 | +0.64 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RNF183]] | +0.72 | +0.74 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[HNF1A-AS1]] | +0.71 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[FAAH2]] | +0.70 | +0.66 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[POF1B]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[TM4SF4]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ST14]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CYP4F12]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 3, C 71. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORL1]] | B | SORL1 activity raises BCAS1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.34× lower at baseline in the lines without SORL1 | 0.086 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[FREM2]] | B | FREM2 activity raises BCAS1's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without FREM2 | 0.089 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity raises BCAS1's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without LINC01876 | 0.096 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[AGR3]] | C | AGR3 activity raises BCAS1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 8.61× lower at baseline in the lines without AGR3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises BCAS1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.68× lower at baseline in the lines without CDH17 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[PRR15L]] | C | PRR15L activity raises BCAS1's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 5.33× lower at baseline in the lines without PRR15L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises BCAS1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 4.48× lower at baseline in the lines without ARHGEF38 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises BCAS1's level | lines that do not express GABRP (44) vs lines expressing it (6) | 4.58× lower at baseline in the lines without GABRP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[LINC02967]] | C | LINC02967 activity raises BCAS1's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 3.71× lower at baseline in the lines without LINC02967 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises BCAS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.12× lower at baseline in the lines without TMPRSS2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[RORC]] | C | RORC activity raises BCAS1's level | lines that do not express RORC (30) vs lines expressing it (20) | 3.39× lower at baseline in the lines without RORC | 0.008 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises BCAS1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 4.95× lower at baseline in the lines without LYZ | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |

### Downstream of this gene

*90 arrows, 90 of them with an alert ⚠; grade A 0, B 28, C 62. Shown: the 12 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STX19]] | B | BCAS1 activity raises STX19's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without BCAS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[RASGEF1B]] | B | BCAS1 activity raises RASGEF1B's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without BCAS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[LNX1]] | B | BCAS1 activity raises LNX1's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 3.69× lower at baseline in the lines without BCAS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[CARD14]] | B | BCAS1 activity strengthens CARD14's drug response | lines that do not express BCAS1 (31) vs lines expressing it (14) | the lines without BCAS1 respond 0.97× as strongly (z diff +0.15); strongest at Dinaciclib 0.05 µM: 0.33x vs 0.92x (z diff +2.8) | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ; target measured in part of the lines; both ways; artifact flags |
| [[C4orf19]] | B | BCAS1 activity raises C4orf19's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without BCAS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[RSPH1]] | B | BCAS1 activity raises RSPH1's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 1.74× lower at baseline in the lines without BCAS1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[CARD14]] | B | BCAS1 activity raises CARD14's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 1.60× lower at baseline in the lines without BCAS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[BCL2L15]] | B | BCAS1 activity raises BCL2L15's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.02× lower at baseline in the lines without BCAS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[HNMT]] | B | BCAS1 activity raises HNMT's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without BCAS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[RBM47]] | B | BCAS1 activity raises RBM47's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 3.20× lower at baseline in the lines without BCAS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[MUC20]] | B | BCAS1 activity raises MUC20's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without BCAS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[SH3BGRL2]] | B | BCAS1 activity raises SH3BGRL2's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without BCAS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 52.4); signed map (59.5, 4.0). **Vector** length 64.9, 23.2% of its response variance represented; |z| ≥ 3 in 482 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +7.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | brain enriched myelin associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:53,936,777-54,070,594 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NABC1, AIBC1, PMES-2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75363](https://www.uniprot.org/uniprotkb/O75363) (Breast carcinoma-amplified sequence 1):

> Required for myelination.

**Summary**, from NCBI Gene [8537](https://www.ncbi.nlm.nih.gov/gene/8537):

> This gene resides in a region at 20q13 which is amplified in a variety of tumor types and associated with more aggressive tumor phenotypes. Among the genes identified from this region, it was found to be highly expressed in three amplified breast cancer cell lines and in one breast tumor without amplification at 20q13.2. However, this gene is not in the common region of maximal amplification and its expression was not detected in the breast cancer cell line MCF7, in which this region is highly …

**Accessions** — [HGNC:974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:974) · Entrez [8537](https://www.ncbi.nlm.nih.gov/gene/8537) · UniProt [O75363](https://www.uniprot.org/uniprotkb/O75363) · Ensembl [ENSG00000064787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064787)

## Data

Gene col 761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 761); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 761]; `tensor/DDL_lfc|DDL_z.npy` [761]; `embed/gene_vectors.npy` [761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 761 or target_col == 761). Every well: [[BCAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
