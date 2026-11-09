---
symbol: "CDH1"
type: "gene"
col: 458
ensembl_id: "ENSG00000039068"
name: "cadherin 1"
location: "16q22.1"
module: 31
arm: "+"
pooled_cpm: 154.43
n_lines_expressing: 19
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 96
direction_downstream: 151
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CDH1

*cadherin 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.46× (z +18.7, q 0e+00, up in 0 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.63× (z +7.4, q 3e-11, up in 0 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.537× (z -9.3, q 6e-18, down in 16 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST14]] (+0.82, fdr 7e-06), [[INAVA]] (+0.74, fdr 7e-06), [[CRYBG2]] (+0.71, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 96 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); 151 go from it, the strongest it → [[KPNA7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +18.7 | 0e+00 | 0/18 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +13.4 | 3e-38 | 1/16 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +7.7 | 3e-12 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.63×** | +7.4 | 3e-11 | 0/17 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.5 | 4e-06 | 7/17 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +4.1 | 0.004 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.005 | 7/18 (KATO III, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.005 | 8/17 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.009 | 0/18 | two highest doses | position effect removed |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.057 | 0/17 | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.085 | 0/18 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -9.3 | 6e-18 | 16/17 (LoVo, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -5.5 | 9e-06 | 0/19 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.704×** | -5.1 | 8e-05 | 13/17 (NCI-H2347, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -4.6 | 5e-04 | 7/17 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 5 µM |  | **0.817×** | -4.3 | 0.002 | 17/17 (HEC-1-A, SW1417, …) | top dose only | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.746×** | -4.1 | 0.005 | 0/17 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.763×** | -3.7 | 0.015 | 0/17 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.783×** | -3.7 | 0.018 | 8/17 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[AZD1390 (drug)]] 0.05 µM |  | **0.777×** | -3.6 | 0.023 | 0/17 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.780×** | -3.4 | 0.034 | 0/17 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.075 | 0/17 | two highest doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.800×** | -3.2 | 0.075 | 0/17 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.816× | -3.0 | 0.10 | 9/17 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.682× | -3.0 | 0.11 | 0/18 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 867 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -8.5) |
| [[LoVo (line)]] | wt | 397 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 435 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.418× (z -8.5) |
| [[COLO 205 (line)]] | alt | 644 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 340 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 124 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.54× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 324 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 422 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 2 | — | [[Oxaprozin (drug)]] 5 µM 0.0602× (z -11.8) |
| [[HT-29 (line)]] | alt | 603 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 382 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 360 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 383 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 407 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 407 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 264 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.75 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.59 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.58 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 21.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST14]] | +0.82 | +0.79 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 460 |
| [[INAVA]] | +0.74 | +0.61 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[CRYBG2]] | +0.71 | +0.60 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[OCLN]] | +0.71 | +0.67 / +0.79 | both halves | 7e-06 | pathway: Apoptosis; STRING 993 |
| [[FA2H]] | +0.70 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[JUP]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 999 |
| [[C1orf116]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MYO5B]] | +0.68 | +0.54 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[EPS8L1]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[LIPH]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[MAL2]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 | STRING 457 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*96 arrows, 96 of them with an alert ⚠; grade A 0, B 15, C 81. Shown: the 12 strongest; 84 more arrows (84 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity lowers CDH1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 12.62× higher at baseline in the lines without TTC28 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[LMTK3]] | B | LMTK3 activity raises CDH1's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 5.96× lower at baseline in the lines without LMTK3 | 0.006 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises CDH1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 5.17× lower at baseline in the lines without EPS8L1 | 0.010 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises CDH1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.87× lower at baseline in the lines without PLEKHG1 | 0.012 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[MYO1D]] | B | MYO1D activity raises CDH1's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 4.72× lower at baseline in the lines without MYO1D | 0.016 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises CDH1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 5.27× lower at baseline in the lines without GRHL3 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises CDH1's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 4.68× lower at baseline in the lines without LMO7 | 0.032 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises CDH1's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 4.65× lower at baseline in the lines without KPNA7 | 0.037 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[FAM83E]] | B | FAM83E activity raises CDH1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 5.54× lower at baseline in the lines without FAM83E | 0.053 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises CDH1's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 4.44× lower at baseline in the lines without TMEM51-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[GAREM1]] | B | GAREM1 activity raises CDH1's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 4.51× lower at baseline in the lines without GAREM1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[TMC6]] | B | TMC6 activity raises CDH1's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 5.21× lower at baseline in the lines without TMC6 | 0.083 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |

### Downstream of this gene

*151 arrows, 151 of them with an alert ⚠; grade A 0, B 64, C 87. Shown: the 12 strongest; 139 more arrows (139 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA7]] | B | CDH1 activity raises KPNA7's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.80× lower at baseline in the lines without CDH1 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[EPS8L1]] | B | CDH1 activity raises EPS8L1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 5.07× lower at baseline in the lines without CDH1 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[FAM83E]] | B | CDH1 activity raises FAM83E's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.77× lower at baseline in the lines without CDH1 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[TMC6]] | B | CDH1 activity raises TMC6's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 5.19× lower at baseline in the lines without CDH1 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[ANXA11]] | B | CDH1 activity raises ANXA11's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.38× lower at baseline in the lines without CDH1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[PTK2B]] | B | CDH1 activity raises PTK2B's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without CDH1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[TLDC2]] | B | CDH1 activity raises TLDC2's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.65× lower at baseline in the lines without CDH1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[PATJ]] | B | CDH1 activity raises PATJ's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.35× lower at baseline in the lines without CDH1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[RAB11FIP1]] | B | CDH1 activity raises RAB11FIP1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without CDH1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[LMO7]] | B | CDH1 activity raises LMO7's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.90× lower at baseline in the lines without CDH1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[TUFT1]] | B | CDH1 activity raises TUFT1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without CDH1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[TNFRSF21]] | B | CDH1 activity raises TNFRSF21's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.67× lower at baseline in the lines without CDH1 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.5, 56.5); signed map (57.1, 7.6). **Vector** length 89.4, 42.7% of its response variance represented; |z| ≥ 3 in 446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +18.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.9 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,737,292-68,835,537 (+) |
| Ensembl biotype | protein_coding |
| Also known as | uvomorulin, CD324; previously UVO |
| Gene groups (HGNC) | CD molecules; Type I classical cadherins |
| Hallmark sets | TGF_BETA_SIGNALING, APICAL_JUNCTION, ESTROGEN_RESPONSE_LATE |
| Reactome | 40 pathways, smallest: Epithelial-Mesenchymal Transition (EMT) during gastrulation; InlA-mediated entry of Listeria monocytogenes into host cells; Apoptotic cleavage of cell adhesion  proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P12830](https://www.uniprot.org/uniprotkb/P12830) (Cadherin-1):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types. CDH1 is involved in mechanisms regulating cell-cell adhesions, mobility and proliferation of epithelial cells. Promotes organization of radial actin fiber structure and cellular response to contractile forces, via its interaction with AMOTL2 which facilitates anchoring of radial …

**Summary**, from NCBI Gene [999](https://www.ncbi.nlm.nih.gov/gene/999):

> This gene encodes a classical cadherin of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature glycoprotein. This calcium-dependent cell-cell adhesion protein is comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cytoplasmic tail. Mutations in this gene are correlated with gastric, breast, colorectal, thyroid and …

**Accessions** — [HGNC:1748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1748) · Entrez [999](https://www.ncbi.nlm.nih.gov/gene/999) · UniProt [P12830](https://www.uniprot.org/uniprotkb/P12830) · Ensembl [ENSG00000039068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000039068)

## Data

Gene col 458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 458); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 458]; `tensor/DDL_lfc|DDL_z.npy` [458]; `embed/gene_vectors.npy` [458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 458 or target_col == 458). Every well: [[CDH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
