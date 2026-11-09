---
symbol: "CYP2S1"
type: "gene"
col: 9496
ensembl_id: "ENSG00000167600"
name: "cytochrome P450 family 2 subfamily S member 1"
location: "19q13.2"
module: 55
arm: "+"
pooled_cpm: 15.57
n_lines_expressing: 30
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 40
direction_downstream: 10
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# CYP2S1

*cytochrome P450 family 2 subfamily S member 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +6.2, q 2e-07, up in 14 of 26 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +5.6, q 7e-06, up in 16 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.489× (z -7.4, q 5e-11, down in 21 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO7B]] (+0.69, fdr 8e-06), [[AFAP1L2]] (+0.68, fdr 7e-06), [[EPS8L3]] (+0.67, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[LINC01819]] → it (grade B ⚠); 10 go from it, the strongest it → [[SOX9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +6.2 | 2e-07 | 14/26 (A-172, HS-578T, …) | inconsistent across doses | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +5.6 | 7e-06 | 16/28 (A498, A-172, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +4.8 | 2e-04 | 14/28 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.3 | 0.002 | 11/25 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.54×** | +4.3 | 0.002 | 15/28 (NCI-H1792, A549, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.077 | 9/28 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.082 | 8/28 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.12 | 9/28 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.34× | +3.0 | 0.14 | 5/28 (COLO 205, HT-29, …) | two highest doses | position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.36× | +3.0 | 0.14 | 7/28 (A549, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.489×** | -7.4 | 5e-11 | 21/28 (A549, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.529×** | -6.6 | 1e-08 | 20/28 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -6.3 | 6e-08 | 20/28 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -6.2 | 9e-08 | 19/27 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.605×** | -4.9 | 9e-05 | 18/28 (LS 180, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.632×** | -4.8 | 2e-04 | 18/27 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -4.8 | 2e-04 | 17/28 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.646×** | -4.4 | 9e-04 | 14/28 (LS 180, NCI-H2030, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.666×** | -4.2 | 0.002 | 8/28 (HOP62, A549, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -4.0 | 0.004 | 13/28 (HT-29, LS 180, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.686×** | -3.9 | 0.005 | 14/28 (A498, LoVo, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.689×** | -3.9 | 0.005 | 11/28 (HepG2/C3A, KATO III, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -3.8 | 0.008 | 12/21 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.776×** | -3.7 | 0.008 | 10/28 (A549, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.705×** | -3.6 | 0.010 | 12/28 (LS 180, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.735×** | -3.2 | 0.047 | 10/28 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.741×** | -3.1 | 0.056 | 10/28 (AsPC-1, SW48, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.059 | 10/28 (A549, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 59.3 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0767× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -13.6) |
| [[LS 180 (line)]] | wt | 80.0 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.171× (z -12.5) |
| [[COLO 205 (line)]] | alt | 30.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0460× (z -21.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.1) |
| [[KATO III (line)]] | alt | 92.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -14.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -12.8) |
| [[SW1417 (line)]] | alt | 88.1 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -17.3) |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0759× (z -19.2) |
| [[A549 (line)]] | wt | 38.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.262× (z -8.9) |
| [[SW480 (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0510× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -12.5) |
| [[A-172 (line)]] | wt | 5.32 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.29× (z +10.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0707× (z -9.0) |
| [[HS-578T (line)]] | alt | 8.28 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 5.79 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0402× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 25.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -9.1) |
| [[PANC-1 (line)]] | alt | 5.08 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.179× (z -8.8) |
| [[SW48 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.820 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO7B]] | +0.69 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[AFAP1L2]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PIK3C2B]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[MUC3A]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[LGALS4]] | +0.64 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[LGR6]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TMPRSS2]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SLC52A3]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 19, C 21. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01819]] | B | LINC01819 activity raises CYP2S1's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 3.11× lower at baseline in the lines without LINC01819 | 0.011 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent |
| [[IGSF9]] | B | IGSF9 activity raises CYP2S1's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without IGSF9 | 0.015 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[ATP8B1]] | B | ATP8B1 activity raises CYP2S1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.44× lower at baseline in the lines without ATP8B1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[CYP3A5]] | B | CYP3A5 activity raises CYP2S1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.62× lower at baseline in the lines without CYP3A5 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[ANO9]] | B | ANO9 activity raises CYP2S1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 3.07× lower at baseline in the lines without ANO9 | 0.030 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[UGT1A6]] | B | UGT1A6 activity raises CYP2S1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.91× lower at baseline in the lines without UGT1A6 | 0.069 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[TSPAN2]] | B | TSPAN2 activity raises CYP2S1's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without TSPAN2 | 0.072 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[MYO7B]] | B | MYO7B activity raises CYP2S1's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.50× lower at baseline in the lines without MYO7B | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[MUC5AC]] | B | MUC5AC activity raises CYP2S1's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.42× lower at baseline in the lines without MUC5AC | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[GPA33]] | B | GPA33 activity raises CYP2S1's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 4.94× lower at baseline in the lines without GPA33 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[ST14]] | B | ST14 activity raises CYP2S1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.69× lower at baseline in the lines without ST14 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[UGT1A1]] | B | UGT1A1 activity raises CYP2S1's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 3.46× lower at baseline in the lines without UGT1A1 | 0.078 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX9]] | B | CYP2S1 activity raises SOX9's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without CYP2S1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75 |
| [[ANO9]] | B | CYP2S1 activity raises ANO9's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without CYP2S1 | 0.045 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75 |
| [[IL22RA1]] | C | CYP2S1 activity raises IL22RA1's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 2.69× lower at baseline in the lines without CYP2S1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75; co-absent with the target |
| [[INAVA]] | C | CYP2S1 activity raises INAVA's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 3.42× lower at baseline in the lines without CYP2S1 | 0.032 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75; co-absent with the target |
| [[HNF4A]] | C | CYP2S1 activity raises HNF4A's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 4.26× lower at baseline in the lines without CYP2S1 | 0.033 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75; co-absent with the target |
| [[B3GNT3]] | C | CYP2S1 activity raises B3GNT3's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 3.10× lower at baseline in the lines without CYP2S1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75; co-absent with the target |
| [[RNF43]] | C | CYP2S1 activity raises RNF43's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 3.52× lower at baseline in the lines without CYP2S1 | 0.063 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75; co-absent with the target |
| [[EPS8L3]] | C | CYP2S1 activity raises EPS8L3's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 2.91× lower at baseline in the lines without CYP2S1 | 0.066 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75; co-absent with the target |
| [[GALNT5]] | C | CYP2S1 activity raises GALNT5's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 3.40× lower at baseline in the lines without CYP2S1 | 0.070 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75; co-absent with the target |
| [[LGR6]] | C | CYP2S1 activity raises LGR6's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 2.36× lower at baseline in the lines without CYP2S1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.5, 48.8); signed map (63.8, 9.7). **Vector** length 86.7, 24.3% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.1 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -6.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.7 | -1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 2 subfamily S member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,193,210-41,207,539 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cytochrome P450 family 2; Hydroperoxy icosatetraenoate dehydratases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 5 pathways, smallest: Miscellaneous substrates; Xenobiotics; Cytochrome P450 - arranged by substrate type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SQ9](https://www.uniprot.org/uniprotkb/Q96SQ9) (Cytochrome P450 2S1):

> A cytochrome P450 monooxygenase involved in the metabolism of retinoids and eicosanoids. In epidermis, may contribute to the oxidative metabolism of all-trans-retinoic acid. For this activity, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (NADPH--hemoprotein reductase). Additionally, displays peroxidase and isomerase activities toward various oxygenated …

**Summary**, from NCBI Gene [29785](https://www.ncbi.nlm.nih.gov/gene/29785):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This protein localizes to the endoplasmic reticulum. In rodents, the homologous protein has been shown to metabolize certain carcinogens; however, the specific function of the human protein has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15654) · Entrez [29785](https://www.ncbi.nlm.nih.gov/gene/29785) · UniProt [Q96SQ9](https://www.uniprot.org/uniprotkb/Q96SQ9) · Ensembl [ENSG00000167600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167600)

## Data

Gene col 9496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9496); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9496]; `tensor/DDL_lfc|DDL_z.npy` [9496]; `embed/gene_vectors.npy` [9496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9496 or target_col == 9496). Every well: [[CYP2S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP2S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
