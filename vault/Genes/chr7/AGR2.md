---
symbol: "AGR2"
type: "gene"
col: 2773
ensembl_id: "ENSG00000106541"
name: "anterior gradient 2, protein disulphide isomerase family member"
location: "7p21.1"
module: 49
arm: "+"
pooled_cpm: 43.6
n_lines_expressing: 18
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 14
direction_downstream: 37
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# AGR2

*anterior gradient 2, protein disulphide isomerase family member* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.56× (z +11.9, q 9e-30, up in 12 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +7.0, q 5e-10, up in 10 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 0.05 µM: 0.522× (z -4.2, q 0.014, down in 3 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.210×, NCI-H2347 0.257×, HT-29 0.323×, NCI-H1573 0.269×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (SNU-1 0.206×; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.156×; ⚠ toxic; cell-cycle shift, explains ~43% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.185×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D8B]] (+0.57, fdr 3e-05), [[SLC15A2]] (+0.56, fdr 3e-05), [[CREB3L2]] (+0.54, fdr 3e-05); moves opposite to [[DROSHA]] (-0.49, fdr 6e-05), [[ASAP1]] (-0.44, fdr 1e-04), [[ELAC2]] (-0.43, fdr 6e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LXN]] → it (grade B ⚠); 37 go from it, the strongest it → [[PPP1R15B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.56×** | +11.9 | 9e-30 | 12/16 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.84×** | +9.0 | 9e-17 | 10/12 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +7.0 | 5e-10 | 10/16 (AsPC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +6.5 | 1e-08 | 9/13 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +5.8 | 9e-07 | 15/16 (SNU-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +3.7 | 0.017 | 12/16 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.70×** | +3.7 | 0.018 | 1/16 (NCI-H2347) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.69×** | +3.6 | 0.019 | 6/16 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.66×** | +3.5 | 0.029 | 4/16 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.029 | 3/17 (SW 900, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.59× | +3.1 | 0.11 | 4/16 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2773.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.210×, NCI-H2347 0.257×, HT-29 0.323×, NCI-H1573 0.269×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (SNU-1 0.206×; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.156×; ⚠ toxic; cell-cycle shift, explains ~43% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.185×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | **0.522×** | -4.2 | 0.014 | 3/16 (AsPC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.619× | -3.1 | 0.64 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 141 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~43% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.185× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 241 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 531 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 43.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.206× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 260 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.65 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D8B]] | +0.57 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[SLC15A2]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[CREB3L2]] | +0.54 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[SMIM14]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DNAJB9]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[APOH]] | +0.53 | +0.27 / +0.49 | both halves | 3e-04 |  |
| [[LXN]] | +0.52 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[EAF2]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[SMIM31]] | +0.52 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[TMEM125]] | +0.52 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SERF2]] | +0.51 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[HID1]] | +0.51 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DROSHA]] | -0.49 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ASAP1]] | -0.44 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[ELAC2]] | -0.43 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[TRMT6]] | -0.42 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[PLCG1]] | -0.42 | -0.37 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LXN]] | B | LXN activity raises AGR2's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without LXN | 0.029 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[SMIM31]] | C | SMIM31 activity raises AGR2's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 7.77× lower at baseline in the lines without SMIM31 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881; co-absent with the target |
| [[ALDH3A1]] | C | ALDH3A1 activity raises AGR2's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 6.76× lower at baseline in the lines without ALDH3A1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises AGR2's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.72× lower at baseline in the lines without TMEM125 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[PIP5K1B]] | C | PIP5K1B activity raises AGR2's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 5.65× lower at baseline in the lines without PIP5K1B | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B; co-absent with the target |
| [[MPZL3]] | C | MPZL3 activity raises AGR2's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 3.50× lower at baseline in the lines without MPZL3 | 0.020 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1; co-absent with the target |
| [[ESRP1]] | C | ESRP1 activity raises AGR2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 4.96× lower at baseline in the lines without ESRP1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |
| [[ST8SIA6]] | C | ST8SIA6 activity raises AGR2's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 3.79× lower at baseline in the lines without ST8SIA6 | 0.030 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; co-absent with the target |
| [[GALNT3]] | C | GALNT3 activity raises AGR2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 4.58× lower at baseline in the lines without GALNT3 | 0.039 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1; co-absent with the target |
| [[TSPAN1]] | C | TSPAN1 activity raises AGR2's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 3.86× lower at baseline in the lines without TSPAN1 | 0.040 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises AGR2's level | lines that do not express PIGR (45) vs lines expressing it (5) | 4.69× lower at baseline in the lines without PIGR | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises AGR2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 4.06× lower at baseline in the lines without TJP3 | 0.045 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 26, C 11. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R15B]] | B | AGR2 activity raises PPP1R15B's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without AGR2 | 0.005 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[ASAP1]] | B | AGR2 activity weakens ASAP1's drug response | lines that do not express AGR2 (32) vs lines expressing it (17) | the lines without AGR2 respond 0.97× as strongly (z diff -0.15); strongest at Idarubicin (hydrochloride) 5 µM: 0.73x vs 1.15x (z diff -8.0) | 0.006 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1; target measured in part of the lines; both ways; artifact flags |
| [[GOLPH3L]] | B | AGR2 activity raises GOLPH3L's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without AGR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[SMIM14]] | B | AGR2 activity raises SMIM14's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.74× lower at baseline in the lines without AGR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[DNAJC3]] | B | AGR2 activity raises DNAJC3's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.73× lower at baseline in the lines without AGR2 | 0.011 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[PLCG1]] | B | AGR2 activity lowers PLCG1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.82× higher at baseline in the lines without AGR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[CCDC186]] | B | AGR2 activity raises CCDC186's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.58× lower at baseline in the lines without AGR2 | 0.022 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[DROSHA]] | B | AGR2 activity lowers DROSHA's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.24× higher at baseline in the lines without AGR2 | 0.029 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[ASAP1]] | B | AGR2 activity lowers ASAP1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.57× higher at baseline in the lines without AGR2 | 0.032 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[SSR4]] | B | AGR2 activity raises SSR4's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.31× lower at baseline in the lines without AGR2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[HID1]] | B | AGR2 activity raises HID1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without AGR2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[SEC31A]] | B | AGR2 activity raises SEC31A's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.28× lower at baseline in the lines without AGR2 | 0.044 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.409). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, 59.4); signed map (-52.0, 13.2). **Vector** length 54.1, 18.2% of its response variance represented; |z| ≥ 3 in 364 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | anterior gradient 2, protein disulphide isomerase family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:16,791,811-16,833,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XAG-2, HAG-2, AG2, PDIA17 |
| Gene groups (HGNC) | Protein disulfide isomerases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [O95994](https://www.uniprot.org/uniprotkb/O95994) (Anterior gradient protein 2 homolog):

> Required for MUC2 post-transcriptional synthesis and secretion. May play a role in the production of mucus by intestinal cells (By similarity). Proto-oncogene that may play a role in cell migration, cell differentiation and cell growth. Promotes cell adhesion.

**Summary**, from NCBI Gene [10551](https://www.ncbi.nlm.nih.gov/gene/10551):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, and a C-terminal ER-retention sequence. This protein plays a role in cell migration, cellular transformation and metastasis and is as a p53 inhibitor. As an ER-localized molecular chaperone, it plays a role in the …

**Accessions** — [HGNC:328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:328) · Entrez [10551](https://www.ncbi.nlm.nih.gov/gene/10551) · UniProt [O95994](https://www.uniprot.org/uniprotkb/O95994) · Ensembl [ENSG00000106541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106541)

## Data

Gene col 2773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2773); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2773]; `tensor/DDL_lfc|DDL_z.npy` [2773]; `embed/gene_vectors.npy` [2773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2773 or target_col == 2773). Every well: [[AGR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
