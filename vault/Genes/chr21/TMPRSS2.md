---
symbol: "TMPRSS2"
type: "gene"
col: 11483
ensembl_id: "ENSG00000184012"
name: "transmembrane serine protease 2"
location: "21q22.3"
module: 8
arm: "+"
pooled_cpm: 16.13
n_lines_expressing: 15
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 149
direction_downstream: 221
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TMPRSS2

*transmembrane serine protease 2* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +11.4, q 3e-27, up in 1 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +5.0, q 8e-05, up in 3 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.603× (z -5.5, q 3e-05, down in 10 of 13 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.526× (z -3.6, q 0.032, down in 11 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLIC5]] (+0.85, fdr 7e-06), [[EPS8L3]] (+0.82, fdr 7e-06), [[MUC13]] (+0.81, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 149 arrows point to it, the strongest [[TJP2]] → it (grade B ⚠); 221 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +11.4 | 3e-27 | 1/12 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +9.4 | 2e-18 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.8 | 2e-09 | 2/11 (CFPAC-1, Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.0 | 8e-05 | 3/13 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +4.7 | 2e-04 | 4/13 (Panc 03.27, CFPAC-1, …) | top dose only | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.003 | 0/13 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.003 | 2/13 (CFPAC-1, AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.009 | 8/13 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.49× | +3.1 | 0.12 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.34× | +3.1 | 0.12 | 7/13 (AsPC-1, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.603×** | -5.5 | 3e-05 | 10/13 (LoVo, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.613×** | -5.3 | 4e-05 | 11/13 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.648×** | -4.7 | 6e-04 | 11/13 (KATO III, LS 180, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.681×** | -4.1 | 0.005 | 10/13 (LS 180, LoVo, …) | two highest doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.526×** | -3.6 | 0.032 | 11/13 (NCI-H2347, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.032 | 11/13 (HT-29, SW1417, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.716×** | -3.5 | 0.044 | 9/13 (LoVo, SW480, …) | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.724×** | -3.2 | 0.091 | 0/13 | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.813× | -3.1 | 0.10 | 7/13 (LS 180, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.753× | -3.1 | 0.13 | 11/13 (LoVo, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 65.3 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0528× (z -17.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0952× (z -14.3) |
| [[COLO 205 (line)]] | alt | 162 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -18.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 114 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0556× (z -18.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -8.8) |
| [[KATO III (line)]] | alt | 54.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0448× (z -19.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.213× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 67.6 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -9.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -9.4) |
| [[SW1417 (line)]] | alt | 90.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -12.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.6) |
| [[SW480 (line)]] | alt | 19.3 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.149× (z -12.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 11.1 | 1 | 1 (1 ⚠) | [[Trametinib (drug)]] 0.05 µM 5.12× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.0912× (z -9.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HT-29 (line)]] | alt | 31.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -11.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIC5]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.82 | +0.79 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CDH17]] | +0.80 | +0.77 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.80 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[POF1B]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.80 | +0.77 / +0.81 | both halves | 7e-06 | same gene group |
| [[TOX3]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[LINC01559]] | +0.78 | +0.83 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TRIM31]] | +0.76 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[HEPH]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*149 arrows, 149 of them with an alert ⚠; grade A 0, B 13, C 136. Shown: the 12 strongest; 137 more arrows (137 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP2]] | B | TJP2 activity raises TMPRSS2's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.73× lower at baseline in the lines without TJP2 | 0.040 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises TMPRSS2's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.06× lower at baseline in the lines without MTUS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[GRHL3]] | B | GRHL3 activity raises TMPRSS2's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.24× lower at baseline in the lines without GRHL3 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises TMPRSS2's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.01× lower at baseline in the lines without HTR1D | 0.049 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[TNFRSF21]] | B | TNFRSF21 activity raises TMPRSS2's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.14× lower at baseline in the lines without TNFRSF21 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[FUT2]] | B | FUT2 activity raises TMPRSS2's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.70× lower at baseline in the lines without FUT2 | 0.057 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TMPRSS2's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.89× lower at baseline in the lines without ELF3-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[C4orf19]] | B | C4orf19 activity raises TMPRSS2's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without C4orf19 | 0.072 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises TMPRSS2's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without HNF4G | 0.073 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[SPATA6L]] | B | SPATA6L activity raises TMPRSS2's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.96× lower at baseline in the lines without SPATA6L | 0.077 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[DNAJC15]] | B | DNAJC15 activity raises TMPRSS2's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 2.59× lower at baseline in the lines without DNAJC15 | 0.091 | ⚠ within organs, on part of the lines; also absent: VILL |
| [[HDAC6]] | B | HDAC6 activity raises TMPRSS2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*221 arrows, 221 of them with an alert ⚠; grade A 0, B 77, C 144. Shown: the 12 strongest; 209 more arrows (209 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | TMPRSS2 activity raises EPS8L1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.73× lower at baseline in the lines without TMPRSS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SLC44A3]] | B | TMPRSS2 activity raises SLC44A3's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.34× lower at baseline in the lines without TMPRSS2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ELF3-AS1]] | B | TMPRSS2 activity raises ELF3-AS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.19× lower at baseline in the lines without TMPRSS2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TNFRSF21]] | B | TMPRSS2 activity raises TNFRSF21's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 5.67× lower at baseline in the lines without TMPRSS2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ANXA11]] | B | TMPRSS2 activity raises ANXA11's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.22× lower at baseline in the lines without TMPRSS2 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[PLS1]] | B | TMPRSS2 activity raises PLS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.53× lower at baseline in the lines without TMPRSS2 | 8e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SLC37A1]] | B | TMPRSS2 activity raises SLC37A1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.88× lower at baseline in the lines without TMPRSS2 | 1e-03 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ABHD11]] | B | TMPRSS2 activity raises ABHD11's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.18× lower at baseline in the lines without TMPRSS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TJP2]] | B | TMPRSS2 activity raises TJP2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.80× lower at baseline in the lines without TMPRSS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[FUT2]] | B | TMPRSS2 activity raises FUT2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.87× lower at baseline in the lines without TMPRSS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SERINC5]] | B | TMPRSS2 activity raises SERINC5's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.81× lower at baseline in the lines without TMPRSS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SLC44A3-AS1]] | B | TMPRSS2 activity raises SLC44A3-AS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.07× lower at baseline in the lines without TMPRSS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.3, 52.3); signed map (61.9, 5.7). **Vector** length 78.9, 38.1% of its response variance represented; |z| ≥ 3 in 415 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *O-linked glycosylation of mucins* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane serine protease 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:41,464,300-41,531,116 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRSS10 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Type II transmembrane serine proteases |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 9 pathways, smallest: Attachment and Entry_9678110; Induction of Cell-Cell Fusion; Attachment and Entry_9694614 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15393](https://www.uniprot.org/uniprotkb/O15393) (Transmembrane protease serine 2):

> Plasma membrane-anchored serine protease that cleaves at arginine residues. Participates in proteolytic cascades of relevance for the normal physiologic function of the prostate. Androgen-induced TMPRSS2 activates several substrates that include pro-hepatocyte growth factor/HGF, the protease activated receptor-2/F2RL1 or matriptase/ST14 leading to extracellular matrix disruption and metastasis of prostate cancer cells. In addition, activates trigeminal neurons and contribute to both spontaneous …

**Summary**, from NCBI Gene [7113](https://www.ncbi.nlm.nih.gov/gene/7113):

> This gene encodes a protein that belongs to the serine protease family. The encoded protein contains a type II transmembrane domain, a receptor class A domain, a scavenger receptor cysteine-rich domain and a protease domain. Serine proteases are known to be involved in many physiological and pathological processes. This gene was demonstrated to be up-regulated by androgenic hormones in prostate cancer cells and down-regulated in androgen-independent prostate cancer tissue. The protease domain …

**Accessions** — [HGNC:11876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11876) · Entrez [7113](https://www.ncbi.nlm.nih.gov/gene/7113) · UniProt [O15393](https://www.uniprot.org/uniprotkb/O15393) · Ensembl [ENSG00000184012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184012)

## Data

Gene col 11483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11483); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11483]; `tensor/DDL_lfc|DDL_z.npy` [11483]; `embed/gene_vectors.npy` [11483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11483 or target_col == 11483). Every well: [[TMPRSS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMPRSS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
