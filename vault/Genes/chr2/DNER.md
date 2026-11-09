---
symbol: "DNER"
type: "gene"
col: 11961
ensembl_id: "ENSG00000187957"
name: "delta/notch like EGF repeat containing"
location: "2q36.3"
module: 104
arm: "+"
pooled_cpm: 79.49
n_lines_expressing: 18
n_dd_up: 46
n_dd_down: 7
n_dd_up_clean: 41
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# DNER

*delta/notch like EGF repeat containing* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +11.1, q 1e-25, up in 3 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +10.7, q 2e-24, up in 0 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.672× (z -5.0, q 4e-04, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PID1]] (+0.83, fdr 7e-06), [[DCN]] (+0.67, fdr 7e-06), [[ITGA10]] (+0.66, fdr 7e-06); moves opposite to [[LYPLAL1-AS1]] (-0.47, fdr 1e-04), [[PTHLH]] (-0.47, fdr 4e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[VSTM2L]] → it (grade B ⚠); 10 go from it, the strongest it → [[STXBP5-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +11.1 | 1e-25 | 3/13 (RPMI-7951, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +10.7 | 2e-24 | 0/17 | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +10.3 | 2e-22 | 7/16 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +10.1 | 6e-22 | 7/16 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.17×** | +10.1 | 1e-21 | 14/16 (A-172, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.15×** | +9.9 | 3e-21 | 14/16 (A-172, H4, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.06×** | +9.4 | 6e-19 | 14/16 (A-172, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +9.1 | 9e-18 | 6/16 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.7 | 3e-16 | 4/17 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.89×** | +8.3 | 9e-15 | 15/16 (A-172, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.98×** | +8.2 | 2e-14 | 13/15 (A-172, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +8.1 | 3e-14 | 4/16 (SK-MEL-2, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.91×** | +8.0 | 4e-14 | 14/17 (A-172, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.84×** | +7.9 | 2e-13 | 15/16 (HS-578T, H4, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.79×** | +7.5 | 2e-12 | 11/16 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.78×** | +7.5 | 3e-12 | 14/16 (A-172, H4, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +7.0 | 9e-11 | 6/16 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.672×** | -5.0 | 4e-04 | 13/16 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.515×** | -4.5 | 0.002 | 12/16 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -4.4 | 0.002 | 11/16 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.744×** | -3.6 | 0.049 | 2/16 (HOP62, A-172) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.773×** | -3.4 | 0.085 | 0/15 | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.777×** | -3.3 | 0.092 | 3/16 (SW 1088, HS-578T, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.781×** | -3.2 | 0.099 | 0/16 | two highest doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.776× | -3.2 | 0.10 | 0/16 | rises with dose |  |
| [[Vortioxetine (drug)]] 0.05 µM |  | 0.786× | -3.2 | 0.10 | 0/16 | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.847× | -3.1 | 0.12 | 5/16 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 57.6 | 21 (4 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 5.93× (z +14.7) | — |
| [[H4 (line)]] | wt | 48.4 | 19 | 0 | [[Triamcinolone (drug)]] 5 µM 6.60× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 72.9 | 19 | 0 | [[Triamcinolone (drug)]] 5 µM 4.07× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 153 | 18 | 0 | [[Dexamethasone (drug)]] 0.5 µM 4.87× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 123 | 9 | 4 (3 ⚠) | [[Triamcinolone (drug)]] 5 µM 3.10× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.223× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 376 | 0 | 10 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 492 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.208× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 239 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 569 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.231× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 133 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 26.3× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.279× (z -8.9) |
| [[SW 1271 (line)]] | alt | 405 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 46.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.8) | — |
| [[A-427 (line)]] | wt | 5.33 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.60 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.65 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.56 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.28 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.64 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.21 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.30 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PID1]] | +0.83 | +0.81 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[DCN]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ITGA10]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[FOXC2]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST3B1]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[HIPK2]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[HSD11B1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS9]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[CCND3]] | +0.63 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TLR2]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[KLF9]] | +0.62 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[SH3RF3]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLAL1-AS1]] | -0.47 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[PTHLH]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSTM2L]] | B | VSTM2L activity lowers DNER's level | lines that do not express VSTM2L (20) vs lines expressing it (30) | 1.16× higher at baseline in the lines without VSTM2L | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF829, PKD2L2-DT, ZNF625; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DNER's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WNT5A]] | C | WNT5A activity raises DNER's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.30× lower at baseline in the lines without WNT5A | 0.007 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[PID1]] | C | PID1 activity raises DNER's level | lines that do not express PID1 (22) vs lines expressing it (28) | 4.68× lower at baseline in the lines without PID1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600; co-absent with the target |
| [[SRGN]] | C | SRGN activity raises DNER's level | lines that do not express SRGN (30) vs lines expressing it (20) | 4.96× lower at baseline in the lines without SRGN | 0.057 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |
| [[NTS]] | C | NTS activity raises DNER's level | lines that do not express NTS (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without NTS | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, LINC03000, ENSG00000260364; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STXBP5-AS1]] | B | DNER activity raises STXBP5-AS1's level | lines that do not express DNER (32) vs lines expressing it (18) | 2.64× lower at baseline in the lines without DNER | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC |
| [[STXBP5]] | B | DNER activity raises STXBP5's level | lines that do not express DNER (32) vs lines expressing it (18) | 1.41× lower at baseline in the lines without DNER | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC |
| [[STXBP5-AS1]] | B | DNER activity strengthens STXBP5-AS1's drug response | lines that do not express DNER (28) vs lines expressing it (16) | the lines without DNER respond 0.70× as strongly (z diff +1.04); rises at some drug-doses, falls at others (34% from rises): Panobinostat 5 µM: 0.43x vs 0.23x (z diff +2.7); Belinostat 5 µM: 0.43x vs 0.24x (z diff +2.3); Clobetasol propionate 0.5 µM: 1.61x vs 4.40x (z diff +1.9) | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ADPRHL1]] | B | DNER activity raises ADPRHL1's level | lines that do not express DNER (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without DNER | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC |
| [[PID1]] | C | DNER activity raises PID1's level | lines that do not express DNER (32) vs lines expressing it (18) | 6.19× lower at baseline in the lines without DNER | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[WNT5A]] | C | DNER activity raises WNT5A's level | lines that do not express DNER (32) vs lines expressing it (18) | 6.44× lower at baseline in the lines without DNER | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[PCBP3]] | C | DNER activity raises PCBP3's level | lines that do not express DNER (32) vs lines expressing it (18) | 3.52× lower at baseline in the lines without DNER | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[SRGN]] | C | DNER activity raises SRGN's level | lines that do not express DNER (32) vs lines expressing it (18) | 5.86× lower at baseline in the lines without DNER | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[TMTC1]] | C | DNER activity raises TMTC1's level | lines that do not express DNER (32) vs lines expressing it (18) | 4.54× lower at baseline in the lines without DNER | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[DCN]] | C | DNER activity raises DCN's level | lines that do not express DNER (32) vs lines expressing it (18) | 3.52× lower at baseline in the lines without DNER | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.0, 15.6); signed map (17.8, 32.5). **Vector** length 95.4, 30.6% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.2 | +9.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.6 | +10.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.5 | +8.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.5 | +9.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.4 | +7.5 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | delta/notch like EGF repeat containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:229,357,629-229,714,555 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ26, bet |
| Reactome | 3 pathways, smallest: Activated NOTCH1 Transmits Signal to the Nucleus; Signaling by NOTCH1; Signaling by NOTCH |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFT8](https://www.uniprot.org/uniprotkb/Q8NFT8) (Delta and Notch-like epidermal growth factor-related receptor):

> Activator of the NOTCH1 pathway. May mediate neuron-glia interaction during astrocytogenesis (By similarity).

**Summary**, from NCBI Gene [92737](https://www.ncbi.nlm.nih.gov/gene/92737):

> Predicted to enable Notch binding activity. Involved in central nervous system development. Located in dendrite; early endosome; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24456) · Entrez [92737](https://www.ncbi.nlm.nih.gov/gene/92737) · UniProt [Q8NFT8](https://www.uniprot.org/uniprotkb/Q8NFT8) · Ensembl [ENSG00000187957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187957)

## Data

Gene col 11961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11961); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11961]; `tensor/DDL_lfc|DDL_z.npy` [11961]; `embed/gene_vectors.npy` [11961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11961 or target_col == 11961). Every well: [[DNER — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNER.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
