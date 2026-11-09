---
symbol: "FAM66C"
type: "gene"
col: 13551
ensembl_id: "ENSG00000226711"
name: "family with sequence similarity 66 member C"
location: "12p13.31"
module: 10
arm: "+"
pooled_cpm: 3.25
n_lines_expressing: 35
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 21
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FAM66C

*family with sequence similarity 66 member C* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.52× (z +6.6, q 2e-08, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +6.0, q 5e-07, up in 12 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.304× (z -8.8, q 7e-16, down in 26 of 30 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PJVK]] (+0.69, fdr 3e-05), [[LINC02026]] (+0.67, fdr 1e-05), [[KATNAL2]] (+0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GCAWKR]] → it (grade B ⚠); 21 go from it, the strongest it → [[ADAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +6.6 | 2e-08 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +6.0 | 5e-07 | 12/24 (NCI-H23, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.74×** | +4.1 | 0.006 | 12/28 (A-427, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +4.1 | 0.006 | 7/27 (SW480, BT-474, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +4.1 | 0.006 | 1/6 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.055 | 9/29 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.078 | 7/24 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.2 | 0.099 | 1/12 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 1.40× | +3.1 | 0.12 | 5/27 (LoVo, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.51× | +3.1 | 0.12 | 5/30 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.304×** | -8.8 | 7e-16 | 26/30 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.361×** | -7.6 | 1e-11 | 19/27 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.392×** | -6.9 | 7e-10 | 16/30 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.419×** | -6.5 | 2e-08 | 18/27 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.456×** | -5.8 | 6e-07 | 17/29 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.513×** | -4.9 | 7e-05 | 19/23 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.517×** | -4.9 | 9e-05 | 16/25 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.526×** | -4.6 | 3e-04 | 14/26 (KATO III, NCI-H2347, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.629×** | -3.4 | 0.039 | 7/30 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.627×** | -3.3 | 0.051 | 5/28 (NCI-H460, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0329× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0953× (z -12.3) |
| [[A-427 (line)]] | wt | 11.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0333× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.147× (z -9.0) |
| [[KATO III (line)]] | alt | 6.00 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0391× (z -12.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 3.80 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0541× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 3.34 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0514× (z -9.4) |
| [[HOP62 (line)]] | alt | 7.90 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0422× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 4.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0671× (z -8.8) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H2347 (line)]] | alt | 3.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0994× (z -8.8) |
| [[PANC-1 (line)]] | alt | 1.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0714× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.950 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJVK]] | +0.69 | +0.76 / +0.46 | both halves | 3e-05 |  |
| [[LINC02026]] | +0.67 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[KATNAL2]] | +0.67 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD20A21P]] | +0.65 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MEI1]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[LRRIQ3]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[LINC00466]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PSMG3-AS1]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.62 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[FRG1-DT]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ZMAT1]] | +0.62 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD18CP]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCAWKR]] | B | GCAWKR activity raises FAM66C's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.68× lower at baseline in the lines without GCAWKR | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[FAXC]] | B | FAXC activity raises FAM66C's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without FAXC | 0.030 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[ANKRD20A11P]] | B | ANKRD20A11P activity raises FAM66C's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.76× lower at baseline in the lines without ANKRD20A11P | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[AGA-DT]] | B | AGA-DT activity raises FAM66C's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without AGA-DT | 0.058 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[LINC02026]] | B | LINC02026 activity raises FAM66C's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without LINC02026 | 0.095 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |
| [[ZMAT1]] | C | ZMAT1 activity raises FAM66C's level | lines that do not express ZMAT1 (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without ZMAT1 | 0.015 | ⚠ within organs, on part of the lines; also absent: NTN1, C19orf81, LMX1B; co-absent with the target |
| [[SSPOP]] | C | SSPOP activity raises FAM66C's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.01× lower at baseline in the lines without SSPOP | 0.064 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 19, C 2. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAP2]] | B | FAM66C activity raises ADAP2's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without FAM66C | 0.008 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[BRPF3-AS1]] | B | FAM66C activity raises BRPF3-AS1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without FAM66C | 0.012 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[SYT9-AS1]] | B | FAM66C activity raises SYT9-AS1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without FAM66C | 0.025 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[F8]] | B | FAM66C activity raises F8's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.68× lower at baseline in the lines without FAM66C | 0.026 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[LINC03036]] | B | FAM66C activity raises LINC03036's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.36× lower at baseline in the lines without FAM66C | 0.027 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[LINC01341]] | B | FAM66C activity raises LINC01341's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.69× lower at baseline in the lines without FAM66C | 0.045 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[STAC3]] | B | FAM66C activity raises STAC3's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without FAM66C | 0.058 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[ZCWPW1]] | B | FAM66C activity raises ZCWPW1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.40× lower at baseline in the lines without FAM66C | 0.067 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[BRPF3-AS1]] | B | FAM66C activity strengthens BRPF3-AS1's drug response | lines that do not express FAM66C (14) vs lines expressing it (33) | the lines without FAM66C respond 0.73× as strongly (z diff +1.52); strongest at Digitoxin 5 µM: 0.32x vs 0.20x (z diff +3.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZFP2]] | B | FAM66C activity raises ZFP2's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without FAM66C | 0.073 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[FAXC]] | B | FAM66C activity raises FAXC's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without FAM66C | 0.075 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[APPBP2-DT]] | B | FAM66C activity raises APPBP2-DT's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without FAM66C | 0.079 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.1, 30.5); signed map (36.6, -9.3). **Vector** length 48.3, 8.85% of its response variance represented; |z| ≥ 3 in 725 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | -0.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.7 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -1.5 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 66 member C |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p13.31 — chr12:8,180,207-8,216,151 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with FAM root symbol |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21644) · Entrez [440078](https://www.ncbi.nlm.nih.gov/gene/440078) · Ensembl [ENSG00000226711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226711)

## Data

Gene col 13551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13551); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13551]; `tensor/DDL_lfc|DDL_z.npy` [13551]; `embed/gene_vectors.npy` [13551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13551 or target_col == 13551). Every well: [[FAM66C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM66C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
